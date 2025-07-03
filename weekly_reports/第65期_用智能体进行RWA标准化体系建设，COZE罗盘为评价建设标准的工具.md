                                    **《智脑时代周刊》第65期**

### **用Coze罗盘与n8n自动化构建RWA标准化体系**

                                                                                                       编制：卢向彤2025.7.3

本方案旨在将RWA标准化的理论框架转化为一个可执行、可自动化、并能持续自我优化的操作流程。我们将使用Coze作为智能化评估引擎（“Coze罗盘”），对RWA项目的合规性与质量进行多维度打分与分析；同时，利用n8n作为核心工作流自动化平台，串联起从资产准入到持续监控的全过程，实现高效、透明、可追溯的标准化管理。

#### **第一阶段：奠定基础——定义RWA标准与Coze罗盘评估框架**

此阶段的目标是确立一套清晰、可量化的RWA标准，并将其转化为Coze平台可以理解和执行的评估模型。

1. **固化核心标准**：基于我们前期的研究，将RWA标准明确为三大支柱，每个支柱下设具体审查点：  
   * **法律-结构层**：  
     * **SPV有效性**：是否设立了独立的特殊目的载体（SPV）以实现破产隔离 1。  
     * **所有权清晰度**：法律文件是否清晰界定了从代币到最终资产的、可强制执行的所有权链条 3。  
     * **司法管辖与合规**：项目是否符合其运营所在地的证券法、AML/KYC法规 5。  
   * **技术-互操作层**：  
     * **代币标准**：是否采用合规原生代币标准（如ERC-3643），将合规逻辑嵌入代币底层 7。  
     * **数据可验证性**：是否采用Chainlink储备金证明（PoR）等机制，对链下资产进行持续、可信的链上验证 8。  
     * **互操作性**：是否采用Chainlink CCIP等行业标准协议，确保资产能在多链环境中安全流转 11。  
   * **运营-信任层**：  
     * **资产托管**：链下资产和链上私钥是否由持牌、信誉良好的托管方进行专业管理 3。  
     * **审计完备性**：项目是否拥有完整的第三方审计报告，涵盖智能合约审计、链上数据取证和链下资产验证 14。  
     * **风险管理**：是否针对非流动性资产建立了清晰的估值方法和违约清算机制 17。  
2. **构建Coze罗盘评估模型**：“Coze罗盘”是我们为这套评估体系赋予的名称，其本质是在Coze平台内构建的一个复杂的评估智能体。其设计灵感源于COMPASS等多维评估框架，旨在实现对RWA项目的全面审视 18。  
   * **定义评估维度**：将上述三大支柱（法律、技术、运营）作为罗盘的核心评估维度。  
   * **量化KPI**：为每个审查点设定一个可量化的关键绩效指标（KPI）。例如：  
     * **法律维度KPI**：“SPV文件是否明确包含‘破产隔离’条款？”（是/否/部分）。  
     * **技术维度KPI**：“PoR数据更新频率是否低于24小时？”（是/否）。  
     * **运营维度KPI**：“智能合约审计报告是否存在未修复的高危漏洞？”（是/否）。

#### **第二阶段：配置Coze评估环境**

此阶段专注于在Coze平台中，将“罗盘”模型具体实现为一个可被API调用的自动化评估服务。

1. **创建评估数据集**：在Coze中，评估的准确性高度依赖于高质量的测试用例 19。我们需要创建一个或多个CSV或JSON格式的评估数据集。  
   * **数据集结构**：每一行代表一个虚拟的RWA项目，列则对应我们定义的审查点。

| projectId | assetType | jurisdiction | spvDocsUrl | tokenStandard | poRFeedUrl | auditReportUrl |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| RWA001 | Real Estate | Switzerland | http://... | ERC-3643 | [https://data.chain.link/por](https://www.google.com/search?q=https://data.chain.link/por) | http://... |
| RWA002 | Private Credit | Singapore | (empty) | ERC-20 | (none) | (none) |
| RWA003 | T-Bills | USA | http://... | ERC-20 | [https://data.chain.link/por](https://www.google.com/search?q=https://data.chain.link/por) | http://... |
| \* **数据多样性**：数据集中应包含完全合规的“黄金案例”、部分合规的“灰色案例”以及完全不合规的“负面案例”，以确保评估模型的鲁棒性 19。 |  |  |  |  |  |  |

2. **设计评估规则（Prompt Engineering）**：这是Coze评估的核心，即为“裁判模型”（Judge Model）编写清晰的系统提示（System Prompt） 20。  
   * **示例Prompt**：  
     You are a world-class RWA compliance analyst. Your task is to evaluate the submitted RWA project based on our 'Coze Compass' framework.  
     Input data will be a JSON object containing project details.  
     You must:  
     1\. Score the project on a scale of 0-100 for each of the three dimensions: Legal, Technical, and Operational.  
     2\. For each score, provide a detailed, bullet-pointed rationale, referencing specific fields from the input JSON.  
     3\. If a critical field like 'spvDocsUrl' is missing or the link is invalid, the Legal score cannot exceed 40\.  
     4\. If 'poRFeedUrl' is not a recognized Chainlink PoR feed, the Technical score should be penalized by at least 30 points.  
     5\. If 'auditReportUrl' does not point to a report from a reputable firm, the Operational score is capped at 50\.  
     Output your response in a structured JSON format: {"scores": {"legal": \<score\>, "technical": \<score\>, "operational": \<score\>}, "rationale": {"legal": \["...", "..."\], "technical": \["...", "..."\], "operational": \["...", "..."\]}}

3. **构建并发布Coze评估智能体**：  
   * 在Coze中创建一个新的智能体（Agent） 21。  
   * 将上述评估规则设置为该智能体的核心Prompt。  
   * 根据Coze的指引，将此智能体发布为一个API服务，并获取相应的API密钥和Bot ID，以便n8n进行调用 22。

#### **第三阶段：设计n8n全流程自动化工作流**

这是将所有部件连接起来，实现端到端自动化的核心阶段。我们将创建一个n8n工作流来模拟RWA项目的生命周期管理 24。

1. **触发器 (Trigger Node)**：  
   * 使用**Webhook**节点。当有新的RWA项目通过线上表单或API提交时，Webhook会接收到包含项目基础信息的POST请求，并自动启动整个工作流 26。  
2. **数据提取与尽职调查 (HTTP Request & Code Nodes)**：  
   * **文件抓取**：使用**HTTP Request**节点，根据提交的spvDocsUrl和auditReportUrl等链接，抓取相关的法律和审计文件内容。  
   * **链上数据验证**：使用**HTTP Request**节点调用Chainlink等预言机服务的API，验证poRFeedUrl提供的数据是否真实、足额 9。  
   * **数据结构化**：使用**Code**节点（支持JavaScript/Python），将所有收集到的信息（包括文件内容和API返回数据）整合成一个符合Coze评估智能体输入要求的JSON对象 26。  
3. **调用Coze罗盘进行评估 (HTTP Request Node)**：  
   * 配置一个新的**HTTP Request**节点，向第二阶段发布的Coze Agent API端点发送POST请求 22。  
   * 请求的Body部分即为上一步整合好的项目数据JSON。请求的Headers中需包含Coze的认证信息（API Key）。  
4. **决策与分发 (Switch & Notification Nodes)**：  
   * **解析结果**：Coze API会返回包含分数和理由的JSON。n8n会自动解析这个JSON。  
   * **智能决策**：使用**Switch**节点，根据返回的scores进行路径选择 26：  
     * **路径1 (自动批准)**：如果所有维度得分均 \> 85，则进入此路径。  
     * **路径2 (人工审核)**：如果任何一个维度得分在50-85之间，则进入此路径。  
     * **路径3 (自动拒绝)**：如果任何一个维度得分 \< 50，则进入此路径。  
   * **执行动作**：  
     * **路径1**：使用**Google Sheets**或**Notion**节点，将项目状态更新为“已批准”，并记录Coze的评估报告。  
     * **路径2**：使用**Slack**或**Email**节点，将项目信息和Coze的评估报告发送给合规团队，并在消息中明确指出需要关注的低分项。  
     * **路径3**：自动向项目提交方发送一封礼貌的拒绝邮件，并附上Coze评估报告中的关键拒绝理由，以保持透明度。

#### **第四阶段：集成、测试与持续优化**

1. **端到端测试**：使用为Coze准备的评估数据集，通过n8n的Webhook手动触发工作流，检查每个节点是否按预期执行，数据流转是否正确。利用n8n的执行日志进行调试 24。  
2. **上线运行**：将n8n工作流设置为“Active”，使其能够7x24小时自动处理新的RWA项目申请。  
3. **持续监控与迭代**：  
   * 定期在Coze的“Analysis”页面查看评估智能体的调用频率、Token消耗和用户满意度等数据，以评估其性能 27。  
   * 在n8n中查看工作流的执行历史，识别瓶颈或常见故障点 24。  
   * 随着监管政策的变化或市场出现新的最佳实践，应及时更新Coze罗盘的评估规则和数据集，并相应调整n8n工作流的逻辑，确保整个标准化体系与时俱进。

通过以上四个阶段，您将构建一个强大且灵活的自动化系统，它不仅能高效地执行您设定的RWA标准，还能通过Coze罗盘的智能化评估，提供深刻的洞察，从而不断提升您在RWA领域的治理水平。