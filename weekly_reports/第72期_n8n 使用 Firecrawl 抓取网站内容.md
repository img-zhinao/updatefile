**《智脑时代周刊》第72期**

# **在 n8n 中集成 Firecrawl 实现任何网站内容的抓取**

                                                                                                          编制：卢向彤2025.7.16

## **第一部分：基础策略：构建您的 n8n 与 Firecrawl 解决方案架构**

在启动任何自动化项目之前，制定清晰的战略蓝图至关重要。本部分将阐述构建高效、可扩展的网页抓取工作流所需的基础架构决策，这些决策将直接影响后续的实施路径和技术选型。

### **1.1 AI优先的数据提取导论**

n8n 是一个功能强大的低代码、源可用工作流自动化平台，它通过一个可视化的、基于节点的界面来连接不同的服务并编排复杂的业务逻辑 1。其核心优势在于其灵活性，既支持无代码的拖拽式构建，也允许开发者为复杂任务编写自定义 JavaScript 代码 4。

与此相辅相成的是 Firecrawl，这是一种专为 AI 应用设计的原生 API 服务，旨在将整个网站无缝转换为干净、可供大语言模型 (LLM) 直接使用的数据格式，如 Markdown 或结构化的 JSON 5。Firecrawl 的核心价值在于它抽象并解决了现代网页抓取中的诸多难题，包括 JavaScript 渲染、反机器人机制、代理管理和请求速率限制等 6。

当 n8n 与 Firecrawl 结合使用时，便构成了一个强大且可扩展的自动化数据提取管道。在这个组合中，n8n 扮演着业务流程的“指挥中心”或编排引擎，而 Firecrawl 则作为专业的、能够适应网站结构变化的“数据采集工具”，二者协同工作，实现高效、稳定的数据自动化 8。

### **1.2 n8n 托管决策：云版本与自托管的影响**

在集成 Firecrawl 之前，必须做出的首要且最关键的架构决策是选择 n8n 的托管模式。这不仅仅是基础设施的选择，它从根本上决定了可用的集成方法、数据治理的策略以及后期的维护开销。

* **n8n Cloud (云版本)**：这是一个完全托管的、生产就绪的解决方案，优先考虑易用性和可扩展性，用户无需担心任何运维问题 2。选择此路径意味着，与 Firecrawl 的集成将  
  **仅限于使用 HTTP 请求节点**，因为云版本不支持安装社区节点 11。  
* **n8n Self-Hosted (自托管版本)**：这是一个免费的、源可用的选项，为用户提供了对环境的完全控制权、更高的数据隐私保障，并且能够安装由社区开发的节点 2。然而，这条路径需要用户具备一定的技术能力，例如使用 Docker 进行部署和持续的系统维护 15。至关重要的是，自托管是  
  **使用简化版 Firecrawl 社区节点的唯一途径** 11。

这一托管选择构成了集成策略的一个根本性分水岭。它并非简单的偏好问题，而是一个硬性约束。选择 n8n Cloud 的用户必须掌握相对复杂的 HTTP 请求节点的配置，以换取部署的便捷性。而倾向于社区节点简单性的用户，则必须承担自托管所带来的技术和维护责任。因此，这个决策必须在项目之初就明确，因为它将对后续所有步骤产生连锁反应。

### **1.3 Firecrawl 的操作二分法：Scrape 与 Crawl**

在调用 Firecrawl API 时，理解其两个核心操作的区别至关重要，因为它们对应着截然不同的用例和工作流设计模式。

* **Scrape (抓取)**：这是一个同步操作，专为从**单个 URL** 进行定点数据提取而设计。它响应迅速，直接在 API 的返回结果中包含抓取到的数据 9。此操作非常适合于目标页面已知且明确的场景，例如抓取一篇特定的新闻文章或一个产品详情页。  
* **Crawl (爬取)**：这是一个异步的、基于任务 (job-based) 的操作，用于递归地遍历和提取**整个网站**或网站某个大规模分区的内容。它不会立即返回数据，而是返回一个 jobId。用户必须通过轮询 (polling) 这个 jobId 来检查任务状态，直至任务完成才能获取最终数据 17。此操作专为大规模、全面的数据采集而构建。

Firecrawl 的 Crawl API 设计本身就强制要求在 n8n 中采用异步处理模式。这并非一个可选的“最佳实践”，而是一项硬性要求。任何试图用简单的线性工作流来处理大规模爬取任务的尝试都将失败。Crawl API 的初始 POST 请求仅返回一个 jobId 20，而 n8n 的标准工作流是按顺序执行节点的。这意味着，在一个简单的流程中，工作流会在爬取任务远未完成时就移动到下一步。为了获取最终数据，n8n 工作流必须被设计成能够暂停、循环并重复检查状态检查端点 (

GET /v1/crawl/{id}) 的模式 20。这种在 n8n 社区中被称为“轮询”的模式，是处理外部长时间运行任务的标准方法 23。因此，使用 Firecrawl 最强大的

Crawl 功能与在 n8n 中实现一个更高级的、非线性的工作流模式是密不可分的。

为了帮助用户根据任务需求选择正确的 Firecrawl 操作，下表提供了一个清晰的决策框架。

**表 1: Firecrawl Scrape 与 Crawl API 对比**

| 特性 | Scrape API (/scrape) | Crawl API (/crawl) |
| :---- | :---- | :---- |
| **核心用途** | 针对性、单页面数据提取 17 | 全面性、多页面网站遍历 17 |
| **执行模型** | 同步 (数据在响应中直接返回) 9 | 异步 (响应中返回 jobId) 9 |
| **n8n 工作流复杂度** | 简单，线性工作流 | 复杂，需要实现轮询循环 23 |
| **主要输出** | 抓取到的内容 (Markdown, JSON 等) 9 | 任务 ID (jobId)，轮询成功后才返回抓取内容 20 |
| **理想场景** | 提取特定文章、产品页面、已知资源 | 归档整个文档网站、监控竞争对手所有博客文章 |

## **第二部分：通用方法：使用 HTTP 请求节点进行直接 API 集成**

本部分提供了一套详尽的、分步式的教程，旨在指导用户使用最灵活、最强大的集成方法。该方法适用于 n8n Cloud 和自托管两种环境，确保所有用户都能掌握核心集成技术。

### **2.1 设置与认证：获取并配置 Firecrawl API 密钥**

在与 Firecrawl API 交互之前，必须先完成账户创建和凭证设置。

1. **创建 Firecrawl 账户**：访问 firecrawl.dev 官方网站并完成注册流程。用户可以通过邮箱、GitHub 或 Google 账户快速注册 25。  
2. **定位 API 密钥**：登录后，在您的账户仪表盘中找到并复制 API 密钥 17。  
3. **在 n8n 中创建凭证**：为了安全和可复用性，最佳实践是将 API 密钥存储在 n8n 的凭证管理器中。  
   * 在 n8n 中，导航至“Credentials”并点击“Add credential”。  
   * 在凭证类型中搜索并选择“Header Auth”。  
   * 将凭证命名为易于识别的名称，例如 Firecrawl API。  
   * 在 Name 字段中输入 Authorization。  
   * 在 Value 字段中输入 Bearer {{YOUR\_API\_KEY}}，将 {{YOUR\_API\_KEY}} 替换为您从 Firecrawl 复制的实际密钥 18。保存凭证。

### **2.2 构建同步 Scrape 工作流**

此工作流的目标是抓取单个 URL，并以 Markdown 格式获取其内容。

* **节点 1: 手动触发器 (Manual Trigger)**：为了便于测试，工作流以一个手动触发器开始。  
* **节点 2: HTTP 请求节点 (Scrape)**：这是执行抓取的核心节点。  
  * **Authentication**: 选择“Header Auth”，并在“Credential to Use”中选择您刚刚创建的 Firecrawl API 凭证。  
  * **Method**: POST  
  * **URL**: https://api.firecrawl.dev/v1/scrape 18  
  * **Body Content Type**: JSON  
  * **Body**: 在 JSON 主体中提供一个包含目标 URL 的对象，例如：{ "url": "https://n8n.io/blog/" } 9。您也可以使用表达式从前一个节点动态传入 URL。  
* **数据处理**：执行该节点后，其输出将是一个 JSON 对象，其中包含一个 data 字段，data 字段内则有 markdown 内容 9。在 n8n 中，数据通常以  
  \[{ "json": {...} }\] 的结构存在，您可以使用表达式如 {{ $json.data.markdown }} 来引用所需的数据 28。

### **2.3 掌握异步 Crawl：构建轮询工作流**

这是一个更高级但至关重要的工作流，用于可靠地爬取整个网站并获取所有页面数据。

**工作流概览**: 启动爬取 \-\> 等待 \-\> 检查状态 \-\> IF 状态为 'completed' \-\> 结束。如果状态不是 'completed'，则循环回到 等待 节点。

* **节点 1: 触发器节点**：同样，以一个手动触发器开始。  
* **节点 2: HTTP 请求 (启动爬取)**：  
  * **Method**: POST  
  * **URL**: https://api.firecrawl.dev/v1/crawl 21  
  * **Authentication**: 选择 Firecrawl API 凭证。  
  * **Body**: { "url": "https://docs.firecrawl.dev/" }  
  * **输出**: 此节点将输出一个包含任务 ID 的 JSON 对象。该 ID 可以通过表达式 {{ $json.id }} 引用 20。  
* **节点 3: 等待 (Wait) 节点**：  
  * 在第一次检查状态之前，添加一个 Wait 节点以暂停工作流。设置一个合理的间隔，例如 10 秒 24。  
* **节点 4: HTTP 请求 (检查状态)**：  
  * **Method**: GET  
  * **URL**: https://api.firecrawl.dev/v1/crawl/{{ $node.json.id }}。这里使用表达式动态地从“启动爬取”节点获取 jobId。  
  * **Authentication**: 选择 Firecrawl API 凭证。  
  * **输出**: 一个包含 status 字段（其值可能为 "scraping", "completed", "failed"）的 JSON 对象。如果任务完成，还会包含一个 data 数组 9。  
* **节点 5: IF 节点**：  
  * 这是轮询循环的核心。配置此节点以检查“检查状态”节点的输出。  
  * **Condition**: {{ $json.status }} \- String \- Equals \- completed。  
  * 此节点将有两个输出路径：true (如果条件满足) 和 false (如果不满足)。  
* **循环连接**：将 IF 节点的 false 输出连接回 Wait 节点。这就创建了轮询循环 24。  
* **退出路径**：IF 节点的 true 输出则继续工作流的其余部分。此时，“检查状态”节点的输出中已包含完整的爬取数据。

### **2.4 实践应用：将抓取数据存储到 Google Sheets**

此部分演示如何将已完成的爬取任务返回的页面数组，逐行保存到 Google Sheets 中。

* **前提条件**: 工作流已成功完成上一节中的轮询循环，并且数据位于“检查状态”节点的输出中，具体路径为 {{ $node.json.data }}。  
* **节点 6: Item Lists 节点**：  
  * n8n 的 Google Sheets 节点在追加行时，通常一次处理一个项目 (item)。而爬取操作的输出是一个包含页面数组的单一项目。  
  * 因此，需要使用 Item Lists 节点及其“Split Out Items”操作，将这个包含数组的单一项目拆分为多个项目，每个项目对应数组中的一个页面 29。需要拆分的字段是  
    data。  
* **节点 7: Google Sheets 节点**：  
  * 将此节点连接在 Item Lists 节点之后。  
  * **Authentication**: 指导用户设置 Google Sheets 的 OAuth2 凭证。  
  * **Operation**: 选择 Append Row。  
  * **Spreadsheet ID & Sheet Name**: 配置目标电子表格和工作表 30。  
  * **Columns**: 将每个项目的数据映射到工作表中相应的列。例如：  
    * URL 列: {{ $json.metadata.sourceURL }}  
    * Title 列: {{ $json.metadata.title }}  
    * Markdown 列: {{ $json.markdown }}  
* **结果**: 执行工作流后，Google Sheets 将被填充数据，Firecrawl 爬取的每个页面都对应表中的一行 31。

## **第三部分：简化方法：Firecrawl 社区节点 (自托管)**

对于选择自托管 n8n 的用户，存在一种更简化的集成路径。本部分将详细介绍这一替代方案。

### **3.1 安装与配置**

此方法的一个硬性要求是，它**仅适用于 n8n 的自托管实例** 11。n8n Cloud 用户无法使用此方法。

* **安装步骤**:  
  1. 在您的自托管 n8n 实例中，导航至 Settings \> Community Nodes 14。  
  2. 点击 Install。  
  3. 在 npm 包名输入框中，输入 n8n-nodes-firecrawl 13。  
  4. 同意使用社区节点的风险提示，然后点击 Install。  
  * 注意：社区中存在其他类似的节点，如 n8n-nodes-firecrawl-scraper 34 和  
    @rxap/n8n-nodes-firecrawl 35，但  
    n8n-nodes-firecrawl 是被引用最多的。本报告将重点介绍这一个。  
* **配置步骤**:  
  * 安装成功后，在工作流中添加 Firecrawl 节点。首次使用时，它会提示您创建凭证。点击创建，然后输入您的 Firecrawl API 密钥即可完成一次性设置 13。

### **3.2 使用社区节点构建工作流**

社区节点的最大优势在于它将复杂的 HTTP 请求配置抽象为简单的用户界面。

* **节点 1: Firecrawl 节点**:  
  * 将 Firecrawl 节点添加到画布上，它会带有一个特殊的社区节点图标 14。  
  * **Credential**: 选择已配置好的 Firecrawl 凭证。  
  * **Resource**: 选择 Scrape 或 Crawl 等资源。  
  * **Operation**: 节点提供了一个操作下拉菜单，例如 Scrape a URL and get its content 或 Submit a crawl job 11。  
  * **Parameters**: 无需手动编写 JSON 主体，节点将参数暴露为 UI 字段，如用于输入 URL 的文本框和用于选择格式的下拉菜单 13。

值得注意的是，尽管社区节点简化了操作，但它似乎并未完全封装异步轮询的复杂性。其文档列出了一个名为“Check crawl job status”的独立操作 11，这强烈暗示即使用户使用了社区节点，在执行

Crawl 操作时，**仍然需要手动构建与第二部分中描述的类似的轮询循环**。

### **3.3 战略分析：直接 API vs. 社区节点**

虽然社区节点提供了简化的用户界面，但这种简化是以牺牲灵活性、功能完整性和时效性为代价的。直接使用 HTTP 请求节点虽然设置更为手动，但它保证了能够访问 Firecrawl API 的全部、最新的功能。

社区节点由第三方维护，其更新可能滞后于官方 API 的发布 33。Firecrawl 官方 API 文档详细说明了许多高级功能和端点，例如

/extract 和 /search，以及复杂的 jsonOptions 和 scrapeOptions 参数 18。社区节点很可能无法支持 Firecrawl 发布的每一个新参数和特性。因此，需要使用尖端功能（如基于 schema 的提取）或特定参数的开发者，将被迫使用 HTTP 请求节点。而对于执行基础抓取任务的用户，则可以从社区节点的简单性中受益。

**表 2: 集成方法对比：HTTP 请求节点 vs. Firecrawl 社区节点**

| 属性 | HTTP 请求节点 | Firecrawl 社区节点 |
| :---- | :---- | :---- |
| **n8n 兼容性** | 云版本 & 自托管 13 | 仅限自托管 13 |
| **设置复杂度** | 较高 (需手动配置 JSON 主体、头部等) | 较低 (提供 UI 字段和下拉菜单) 13 |
| **API 覆盖率** | 100% (可访问所有端点和参数) | 有限 (仅支持节点开发者实现的功能) |
| **维护** | n8n 核心节点，由 n8n 团队维护 | 依赖社区开发者更新，可能滞后 33 |
| **灵活性** | 最大化的控制权 | 简化，但可能存在功能限制 |
| **推荐场景** | 复杂任务、需要完全 API 控制、n8n Cloud 用户 | 简单、常见的任务，并且使用自托管实例 |

## **第四部分：高级技术与生产最佳实践**

本部分将超越基础设置，探讨在实际生产环境中进行网页抓取时遇到的挑战，并展示如何利用 Firecrawl 的高级功能在 n8n 中解决这些问题。

### **4.1 绕过防御：处理反抓取与动态内容**

现代网站普遍使用 JavaScript (AJAX) 动态加载内容，并部署如 Cloudflare 等反机器人服务，这些服务会阻止标准的数据中心 IP 发出的 HTTP 请求 38。Firecrawl 的设计初衷就是为了应对这些挑战，它通过使用无头浏览器来渲染 JavaScript，并内置了代理管理功能 6。

* **处理动态内容**:  
  * 对于需要延迟加载的内容，可以在 HTTP 请求主体的 scrapeOptions 或 pageOptions 对象中使用 waitFor 参数，例如 "waitFor": 3000 (等待 3 秒) 37。  
  * 对于需要用户交互（如点击、滚动或表单输入）后才可见的页面，应使用 actions 参数。例如，可以定义一个动作来点击“加载更多”按钮，然后再执行抓取 9。  
* **处理反机器人/IP 封锁**:  
  * 对于有严格封锁策略的网站，可以在请求主体中使用 proxy 参数。Firecrawl 提供 basic、stealth 和 auto 三种模式。stealth 模式使用更高级的代理，成功率更高，但会消耗更多积分 21。

### **4.2 精准规模化：掌握爬虫范围与效率**

爬取一个大型网站的全部内容通常是缓慢、昂贵且不必要的。目标应该是只获取相关数据。Firecrawl 的 crawlerOptions 提供了精确控制爬取范围的工具。

* **关键参数**:  
  * **maxDepth 与 maxDiscoveryDepth**: 这两个参数有细微但重要的区别。maxDepth 基于 URL 路径的层级（如 /a/b/c 的深度为 3），而 maxDiscoveryDepth 基于从起始页开始的链接“跳数” 21。  
    maxDiscoveryDepth 更适合控制爬取广度，而 maxDepth 则用于限制爬取到网站的特定分区。  
  * **includePaths 与 excludePaths**: 使用正则表达式来指定爬取的目标区域（如 /blog/.\*）或避开无关区域（如 /careers/.\*） 21。  
  * **limit**: 一个至关重要的参数，用于限制爬取的总页数，以控制成本和执行时间 21。  
  * **crawlEntireDomain**: 默认情况下，爬虫只会深入子路径。将此参数设置为 true 可以允许爬虫访问同级或父级路径（例如从 domain.com/blog/post 访问 domain.com/about） 21。

### **4.3 AI 驱动的提取：从原始内容到结构化 JSON**

从抓取中获得的原始 Markdown 内容通常需要在 n8n 中进行大量的后处理（例如使用 Code 节点和正则表达式）才能提取出结构化的实体数据。Firecrawl 通过其 /extract 端点或 /scrape 端点中的 jsonOptions 参数，提供了一种更高效的解决方案。该功能利用 LLM 在服务器端直接完成数据提取 6。

* **实施方法**:  
  * 在 HTTP 请求节点的请求主体中，包含一个 schema 对象来定义期望的 JSON 输出结构，并提供一个 prompt 来指导 LLM，例如：“从这篇文章中提取作者姓名、发布日期和摘要。” 9。

这种方法将数据转换的负担从 n8n 工作流转移到了 Firecrawl API。一个典型的 n8n 提取流程可能是 HTTP Request (Scrape) \-\> Code Node (Parse/Extract) \-\> Set Node (Map Data)。而使用 Firecrawl 的 AI 提取功能后，流程可以简化为 HTTP Request (Extract) \-\> (直接处理结构化数据)。这极大地简化了 n8n 工作流，减少了节点数量和自定义代码，从而提高了自动化的可维护性。这是一个在计算成本（Firecrawl 积分）和工程成本（n8n 开发与维护时间）之间的战略权衡。

### **4.4 常见故障排除**

* **问题 1: HTTP 403 Forbidden 错误**  
  * **症状**: n8n 的 HTTP 请求节点失败并返回 403 错误，但同样的请求在本地浏览器或 cURL 中可以成功 40。  
  * **原因**: 目标网站的安全系统（如 Cloudflare）识别出 n8n 服务器的 IP（无论是 n8n Cloud 的 IP 范围还是您自托管服务器的 IP）为数据中心 IP，并将其屏蔽。而您的本地计算机拥有一个受信任的住宅 IP 40。  
  * **解决方案**: 使用 Firecrawl 内置的代理功能。在请求主体中将 proxy 参数设置为 "stealth" 或 "auto" 43。这将通过一个受信任的轮换代理网络路由请求，从而绕过封锁。  
* **问题 2: 抓取结果中缺少动态内容**  
  * **症状**: 抓取到的 Markdown 中缺少网站上实际可见的数据 38。  
  * **原因**: 这部分内容是在初始页面加载后由 JavaScript 动态加载的。抓取器在 JavaScript 执行完毕前就捕获了 HTML。  
  * **解决方案**: 使用 waitFor 参数增加一个延迟，或使用更稳健的 actions 参数来等待某个特定的元素加载完毕后再进行抓取 9。  
* **问题 3: 无效或格式错误的 JSON**  
  * **症状**: n8n 的下游节点因无法解析 JSON 而失败。  
  * **原因**: API 可能返回一个看起来像 JSON 但格式不正确的字符串，或者读取的文件本身不是有效的 JSON 49。  
  * **解决方案**: 在 n8n 的 Code 节点中使用 JSON.parse() 并将其包裹在 try...catch 块中以安全地解析字符串。对于来自外部脚本的格式错误数据，可以使用字符串操作（如 .indexOf(), .substring()）来分离出有效的 JSON 部分，然后再进行解析 49。

**表 3: 高级抓取参数参考**

| 挑战 | 关键 Firecrawl 参数 | n8n 实施说明 |
| :---- | :---- | :---- |
| **网站屏蔽我的请求 (403错误)** | proxy: "stealth" 或 proxy: "auto" | 在 HTTP 请求节点的 JSON 主体中设置。 |
| **内容延迟加载** | waitFor: \<milliseconds\> | 在 pageOptions/scrapeOptions 中设置。 |
| **需要先点击按钮** | actions: | 在 pageOptions/scrapeOptions 中定义一个动作序列。 |
| **只想爬取博客部分** | crawlerOptions: { includePaths: \["/blog/.\*"\] } | 在 Crawl 操作的请求主体中定义。 |
| **爬取范围太大/成本太高** | crawlerOptions: { limit: 100, maxDiscoveryDepth: 2 } | 结合使用 limit 和深度控制参数来限制爬取范围。 |
| **需要结构化数据而非Markdown** | jsonOptions: { schema: {...}, prompt: "..." } | 在 Scrape 或 Extract 操作的请求主体中定义。 |

## **第五部分：战略建议与未来展望**

### **5.1 常见用例的推荐工作流架构**

* **用例 1: 实时新闻监控与告警**  
  * **架构**: RSS Feed Trigger \-\> Item Lists \-\> HTTP Request (Scrape) \-\> AI Node (Summarize) \-\> Slack/Email Node  
  * **原理**: 使用 RSS 触发器捕获新内容，对每篇新文章单独进行 Scrape 操作（同步模式非常适合），利用 AI 进行摘要，最后发送通知。  
* **用例 2: 从文档构建 RAG 知识库**  
  * **架构**: Manual Trigger \-\> HTTP Request (Crawl with Polling Loop) \-\> Item Lists \-\> Text Splitter Node \-\> Vector DB Node (e.g., Weaviate)  
  * **原理**: 这是一个一次性或定期的规模化操作。需要使用强大的 Crawl 端点和轮询模式。输出结果随后被分块并存储到向量数据库中，供 AI 应用使用。  
* **用例 3: 电商价格与库存追踪**  
  * **架构**: Schedule Trigger \-\> Google Sheets (Get URLs) \-\> Item Lists \-\> HTTP Request (Scrape with jsonOptions) \-\> Google Sheets (Update Row)  
  * **原理**: 这是一个在已知 URL 列表上进行的、定期的重复性任务。使用 Scrape 端点和 AI 驱动的 jsonOptions 来可靠地提取结构化的价格/库存数据，并更新到数据库或电子表格中。

### **5.2 智能自动化的发展轨迹**

Firecrawl 这类工具的出现和普及，标志着自动化领域的一个重要趋势：对脆弱、低级别任务的抽象化。传统的网页抓取严重依赖于易变的 CSS 选择器，一旦网站布局改变，抓取器便会失效 8。而 AI 原生工具则利用语义理解，使其对网站变化具有更强的适应性，从而大幅降低了维护负担。

未来，工作流自动化的发展方向在于将像 Firecrawl 这样的智能化、专业化工具（用于数据采集）与像 n8n 这样的强大编排平台（用于逻辑和集成）相结合。开发者的角色将从编写脆弱的底层代码，转变为通过连接一流的 API 来构建稳健的系统架构。这种模式的转变将释放巨大的生产力，使自动化能够应对更复杂、更动态的挑战。

#### **引用的著作**

1. www.shakudo.io, 访问时间为 七月 16, 2025， [https://www.shakudo.io/integrations/n8n\#:\~:text=n8n%20is%20a%20versatile%20tool,alternative%20to%20conventional%20automation%20tools.](https://www.shakudo.io/integrations/n8n#:~:text=n8n%20is%20a%20versatile%20tool,alternative%20to%20conventional%20automation%20tools.)  
2. n8n: The workflow automation tool for the AI age \- WorkOS, 访问时间为 七月 16, 2025， [https://workos.com/blog/n8n-the-workflow-automation-tool-for-the-ai-age](https://workos.com/blog/n8n-the-workflow-automation-tool-for-the-ai-age)  
3. n8n-io/n8n-docs: Documentation for n8n, a fair-code licensed automation tool with a free community edition and powerful enterprise options. Build AI functionality into your workflows. \- GitHub, 访问时间为 七月 16, 2025， [https://github.com/n8n-io/n8n-docs](https://github.com/n8n-io/n8n-docs)  
4. What is n8n? Docs, Demo and How to Deploy \- Shakudo, 访问时间为 七月 16, 2025， [https://www.shakudo.io/integrations/n8n](https://www.shakudo.io/integrations/n8n)  
5. github.com, 访问时间为 七月 16, 2025， [https://github.com/mendableai/firecrawl\#:\~:text=Firecrawl%20is%20an%20API%20service,No%20sitemap%20required.](https://github.com/mendableai/firecrawl#:~:text=Firecrawl%20is%20an%20API%20service,No%20sitemap%20required.)  
6. Firecrawl: AI Web Crawler Built for LLM Applications \- DataCamp, 访问时间为 七月 16, 2025， [https://www.datacamp.com/tutorial/firecrawl](https://www.datacamp.com/tutorial/firecrawl)  
7. Firecrawl transforms websites into AI-ready data \- Autoritas Consulting, 访问时间为 七月 16, 2025， [https://autoritas.net/en/2024/11/29/firecrawl-transforms-websites-into-ai-ready-data/](https://autoritas.net/en/2024/11/29/firecrawl-transforms-websites-into-ai-ready-data/)  
8. How Firecrawl Cuts Web Scraping Time by 60%: Real Developer Results | Blott Studio, 访问时间为 七月 16, 2025， [https://www.blott.studio/blog/post/how-firecrawl-cuts-web-scraping-time-by-60-real-developer-results](https://www.blott.studio/blog/post/how-firecrawl-cuts-web-scraping-time-by-60-real-developer-results)  
9. Firecrawl: Quickstart, 访问时间为 七月 16, 2025， [https://docs.firecrawl.dev/introduction](https://docs.firecrawl.dev/introduction)  
10. n8n-Tutorial: Scraping websites with n8n and MCP \- ai-rockstars.com, 访问时间为 七月 16, 2025， [https://ai-rockstars.com/scrape-websites-n8n/](https://ai-rockstars.com/scrape-websites-n8n/)  
11. How to Use Firecrawl with n8n for Web Automation | by Girff | Jun, 2025 \- Medium, 访问时间为 七月 16, 2025， [https://girff.medium.com/how-to-use-firecrawl-with-n8n-for-web-automation-e16a59ee0625](https://girff.medium.com/how-to-use-firecrawl-with-n8n-for-web-automation-e16a59ee0625)  
12. n8n Free Self-Hosting vs. n8n Cloud: Which Is Better for AI Agent Automation? \- Reddit, 访问时间为 七月 16, 2025， [https://www.reddit.com/r/n8n/comments/1k1gvah/n8n\_free\_selfhosting\_vs\_n8n\_cloud\_which\_is\_better/](https://www.reddit.com/r/n8n/comments/1k1gvah/n8n_free_selfhosting_vs_n8n_cloud_which_is_better/)  
13. How to use Firecrawl with n8n for web automation, 访问时间为 七月 16, 2025， [https://www.firecrawl.dev/blog/firecrawl-n8n-web-automation](https://www.firecrawl.dev/blog/firecrawl-n8n-web-automation)  
14. n8n Tutorial: Step-by-Step Guide to Setting Up Community Nodes \- YouTube, 访问时间为 七月 16, 2025， [https://www.youtube.com/watch?v=E\_R0WP7oyrQ](https://www.youtube.com/watch?v=E_R0WP7oyrQ)  
15. Self-Hosted vs Managed vs Cloud n8n: What's the Right Choice for You? \- Sliplane, 访问时间为 七月 16, 2025， [https://sliplane.io/blog/self-hosted-managed-cloud-n8n-comparison](https://sliplane.io/blog/self-hosted-managed-cloud-n8n-comparison)  
16. How to install a community node on N8N \- Elestio blog, 访问时间为 七月 16, 2025， [https://blog.elest.io/how-to-install-a-community-node-on-n8n/](https://blog.elest.io/how-to-install-a-community-node-on-n8n/)  
17. How to Use Firecrawl to Scrape Web Data (Beginner's Tutorial) \- Apidog, 访问时间为 七月 16, 2025， [https://apidog.com/blog/firecrawl-web-scraping/](https://apidog.com/blog/firecrawl-web-scraping/)  
18. Introduction \- Firecrawl Docs, 访问时间为 七月 16, 2025， [https://docs.firecrawl.dev/api-reference/introduction](https://docs.firecrawl.dev/api-reference/introduction)  
19. Crawl | Firecrawl, 访问时间为 七月 16, 2025， [https://docs.firecrawl.dev/features/crawl](https://docs.firecrawl.dev/features/crawl)  
20. mendableai/firecrawl: Turn entire websites into LLM-ready markdown or structured data. Scrape, crawl and extract with a single API. \- GitHub, 访问时间为 七月 16, 2025， [https://github.com/mendableai/firecrawl](https://github.com/mendableai/firecrawl)  
21. Crawl \- Firecrawl Docs, 访问时间为 七月 16, 2025， [https://docs.firecrawl.dev/api-reference/endpoint/crawl-post](https://docs.firecrawl.dev/api-reference/endpoint/crawl-post)  
22. Get Crawl Status \- Firecrawl Docs, 访问时间为 七月 16, 2025， [https://docs.firecrawl.dev/api-reference/endpoint/crawl-get](https://docs.firecrawl.dev/api-reference/endpoint/crawl-get)  
23. Batch Process Prompts with Anthropic Claude API | n8n workflow template, 访问时间为 七月 16, 2025， [https://n8n.io/workflows/3409-batch-process-prompts-with-anthropic-claude-api/](https://n8n.io/workflows/3409-batch-process-prompts-with-anthropic-claude-api/)  
24. How to build a Polling Loop? \- Questions \- n8n Community, 访问时间为 七月 16, 2025， [https://community.n8n.io/t/how-to-build-a-polling-loop/110997](https://community.n8n.io/t/how-to-build-a-polling-loop/110997)  
25. How to get API Key from Firecrawl \- DEV Community, 访问时间为 七月 16, 2025， [https://dev.to/abdibrokhim/how-to-get-api-key-from-firecrawl-4d5g](https://dev.to/abdibrokhim/how-to-get-api-key-from-firecrawl-4d5g)  
26. Sign Up \- Firecrawl, 访问时间为 七月 16, 2025， [https://www.firecrawl.dev/signin/signup](https://www.firecrawl.dev/signin/signup)  
27. Firecrawl \- Lamatic.ai Docs, 访问时间为 七月 16, 2025， [https://lamatic.ai/docs/integrations/firecrawl](https://lamatic.ai/docs/integrations/firecrawl)  
28. Master JSON Data in n8n: Parsing & Manipulation Guide, 访问时间为 七月 16, 2025， [https://n8npro.in/n8n-basics/working-with-json-data-in-n8n/](https://n8npro.in/n8n-basics/working-with-json-data-in-n8n/)  
29. How to Insert an Array of Objects into Google Sheets using n8n? \- Questions, 访问时间为 七月 16, 2025， [https://community.n8n.io/t/how-to-insert-an-array-of-objects-into-google-sheets-using-n8n/52820](https://community.n8n.io/t/how-to-insert-an-array-of-objects-into-google-sheets-using-n8n/52820)  
30. How to Connect Google Sheets with n8n | Step-by-Step \- YouTube, 访问时间为 七月 16, 2025， [https://www.youtube.com/watch?v=czxMethJv8s](https://www.youtube.com/watch?v=czxMethJv8s)  
31. Help required for creating a Google Sheet entry from the Agent : r/n8n \- Reddit, 访问时间为 七月 16, 2025， [https://www.reddit.com/r/n8n/comments/1jcncvx/help\_required\_for\_creating\_a\_google\_sheet\_entry/](https://www.reddit.com/r/n8n/comments/1jcncvx/help_required_for_creating_a_google_sheet_entry/)  
32. Write Data to a Google Sheet Using n8n | Step-by-Step Automation Tutorial \- YouTube, 访问时间为 七月 16, 2025， [https://www.youtube.com/watch?v=8NEw5BKst0Q\&pp=0gcJCfwAo7VqN5tD](https://www.youtube.com/watch?v=8NEw5BKst0Q&pp=0gcJCfwAo7VqN5tD)  
33. n8n-nodes-firecrawl \- NPM, 访问时间为 七月 16, 2025， [https://www.npmjs.com/package/n8n-nodes-firecrawl](https://www.npmjs.com/package/n8n-nodes-firecrawl)  
34. leonardogrig/n8n-nodes-firecrawl-scraper \- GitHub, 访问时间为 七月 16, 2025， [https://github.com/leonardogrig/n8n-nodes-firecrawl-scraper](https://github.com/leonardogrig/n8n-nodes-firecrawl-scraper)  
35. rxap/n8n-nodes-firecrawl \- NPM, 访问时间为 七月 16, 2025， [https://www.npmjs.com/package/%40rxap%2Fn8n-nodes-firecrawl](https://www.npmjs.com/package/%40rxap%2Fn8n-nodes-firecrawl)  
36. The Easiest Way to Use Community Nodes in n8n \- YouTube, 访问时间为 七月 16, 2025， [https://www.youtube.com/watch?v=WI8ikp5YyRw](https://www.youtube.com/watch?v=WI8ikp5YyRw)  
37. Extract \- Firecrawl Docs, 访问时间为 七月 16, 2025， [https://docs.firecrawl.dev/api-reference/endpoint/extract](https://docs.firecrawl.dev/api-reference/endpoint/extract)  
38. Scraping Dynamic Website Which uses AJAX to Load Content \- Questions \- n8n Community, 访问时间为 七月 16, 2025， [https://community.n8n.io/t/scraping-dynamic-website-which-uses-ajax-to-load-content/141580](https://community.n8n.io/t/scraping-dynamic-website-which-uses-ajax-to-load-content/141580)  
39. HTTP Extract \- Dynamic Content \- Questions \- n8n Community, 访问时间为 七月 16, 2025， [https://community.n8n.io/t/http-extract-dynamic-content/88668](https://community.n8n.io/t/http-extract-dynamic-content/88668)  
40. Can't visit site on HTTP node 403 error \- Questions \- n8n Community, 访问时间为 七月 16, 2025， [https://community.n8n.io/t/cant-visit-site-on-http-node-403-error/148605](https://community.n8n.io/t/cant-visit-site-on-http-node-403-error/148605)  
41. Scrape \- Firecrawl Docs, 访问时间为 七月 16, 2025， [https://docs.firecrawl.dev/api-reference/endpoint/scrape](https://docs.firecrawl.dev/api-reference/endpoint/scrape)  
42. Scrape \- Firecrawl, 访问时间为 七月 16, 2025， [https://docs.firecrawl.dev/features/scrape](https://docs.firecrawl.dev/features/scrape)  
43. Stealth Mode \- Firecrawl, 访问时间为 七月 16, 2025， [https://docs.firecrawl.dev/features/stealth-mode](https://docs.firecrawl.dev/features/stealth-mode)  
44. How to Build LLM-Ready Datasets with Firecrawl: A Developer's Guide | Blott Studio, 访问时间为 七月 16, 2025， [https://www.blott.studio/blog/post/how-to-build-llm-ready-datasets-with-firecrawl-a-developers-guide](https://www.blott.studio/blog/post/how-to-build-llm-ready-datasets-with-firecrawl-a-developers-guide)  
45. Advanced Scraping Guide \- Firecrawl, 访问时间为 七月 16, 2025， [https://docs.firecrawl.dev/advanced-scraping-guide](https://docs.firecrawl.dev/advanced-scraping-guide)  
46. HTTP request works fine in terminal, but blocked when trying same request in n8n \- Reddit, 访问时间为 七月 16, 2025， [https://www.reddit.com/r/n8n/comments/1iq3uxn/http\_request\_works\_fine\_in\_terminal\_but\_blocked/](https://www.reddit.com/r/n8n/comments/1iq3uxn/http_request_works_fine_in_terminal_but_blocked/)  
47. HTTP Request Node Encountering Error When URL Returns 3XX Redirect Status, 访问时间为 七月 16, 2025， [https://community.n8n.io/t/http-request-node-encountering-error-when-url-returns-3xx-redirect-status/43945](https://community.n8n.io/t/http-request-node-encountering-error-when-url-returns-3xx-redirect-status/43945)  
48. Search \- Firecrawl Docs, 访问时间为 七月 16, 2025， [https://docs.firecrawl.dev/api-reference/endpoint/search](https://docs.firecrawl.dev/api-reference/endpoint/search)  
49. Get the JSON data from String \- Questions \- n8n Community, 访问时间为 七月 16, 2025， [https://community.n8n.io/t/get-the-json-data-from-string/27970](https://community.n8n.io/t/get-the-json-data-from-string/27970)  
50. Extract from JSON file? \- Questions \- n8n Community, 访问时间为 七月 16, 2025， [https://community.n8n.io/t/extract-from-json-file/42647](https://community.n8n.io/t/extract-from-json-file/42647)  
51. Web Scraping With FireCrawl Guide \- Medium, 访问时间为 七月 16, 2025， [https://medium.com/@datajournal/web-scraping-with-firecrawl-570f10a736c5](https://medium.com/@datajournal/web-scraping-with-firecrawl-570f10a736c5)