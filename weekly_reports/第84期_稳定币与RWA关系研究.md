**《智脑时代周刊》第84期**

# **稳定币与RWA：互联共生、区域实践与未来图景的报告**

                                                                                                                                          **编制：卢向彤2025.9.2**

### **执行摘要**

本报告旨在对稳定币与现实世界资产（Real World Assets, RWA）之间的关系进行深入分析。报告核心发现，稳定币与RWA并非平行概念，而是互为依托、交织共生的关系。稳定币本身是一种特殊的RWA，即通证化现金与储备资产，而其他RWA则作为抵押物，为稳定币提供收益和稳定性，由此开辟了“生息稳定币”（yield-bearing stablecoin）的新范式。

报告聚焦中国香港作为区域性试验场的独特地位。随着《稳定币条例》的正式生效，香港正成为连接中国大陆与全球数字资产市场的独特合规桥梁。这为大陆企业在境外探索稳定币与RWA业务提供了审慎且可行的路径，但前提是必须严格遵守中国大陆的政策红线，尤其是用户隔离和跨境数据合规要求。

本报告揭示了在“一国两制”框架下，政策制定者如何以香港为“缓冲带”和“沙盒”，在保障境内金融安全的同时，稳慎推进人民币国际化战略。报告还剖析了RWA为稳定币提供收益的商业逻辑，并阐明了RWA通证化背后复杂的技术与法律结构，如特殊目的载体（SPV）在连接链上代币与链下资产中的关键作用。

战略建议方面，报告呼吁大陆企业在港参与时，必须将合规置于首位，严格执行用户隔离和数据出境安全评估等规定。同时，建议政策制定者加强与香港的监管协同，利用香港的桥梁作用，为离岸人民币稳定币与跨境RWA融资探索提供系统性规划和实践空间。

### **第一章：稳定币与RWA：概念、分类与演进**

#### **1.1 稳定币的本质与全球市场格局**

稳定币是一种旨在维持与某一特定资产（通常是法定货币）相对稳定价值的虚拟资产 1。其核心价值在于解决了比特币、以太坊等加密货币价格剧烈波动的问题，使其能够作为一种可靠的支付媒介、价值储存工具和结算手段 2。

根据底层资产和稳定机制的不同，稳定币可分为多种类型，但全球市场格局高度集中。目前，市场主流为由法币或其等价物全额储备支持的法币锚定稳定币，其中美元稳定币占据绝对主导地位，其总市值在2024年底已达到约2120亿美元 5，并在2025年初飙升至超过2500亿美元 4。以USDT和USDC为代表的美元稳定币，合计占据了超过90%的市场份额，这凸显了美元在全球数字金融体系中的主导地位 4。相较之下，曾一度引起广泛关注的算法稳定币，如TerraUSD，因其缺乏高流动性资产支持，在市场动荡中极易发生“脱钩”和崩溃，严重损害了市场信心 2。报告显示，商品抵押稳定币因受限于储备管理和赎回机制，其流动性和普及度也难以与法币锚定稳定币相媲美 4。

#### **1.2 RWA通证化：从概念到实践**

现实世界资产（RWA）是指存在于数字世界之外、具有有形或无形价值的资产，例如房地产、政府债券、私人信贷、艺术品和知识产权等 7。RWA通证化（Tokenization）是一个将这些链下资产的所有权或权益，以链上数字代币的形式进行表示的过程 8。这一创新融合了传统金融的价值基础与区块链技术的效率优势。

RWA通证化的核心优势在于其能够显著提升资产的流动性、透明度和可及性 9。传统高价值资产，如房地产或私募股权，通常流动性差且投资门槛高。通过通证化，这些资产可以被分割成更小的、可交易的数字份额（

**“可分割性”**），从而大大降低投资门槛，使更广泛的投资者群体能够参与 10。此外，由于交易记录被永久、透明地记录在区块链上，这减少了对传统中介机构的依赖，降低了交易成本并加速了结算 9。

当前，RWA通证化的应用已覆盖多个领域：

* **私人信贷与贸易融资**：Centrifuge协议通过将消费贷款、房地产过渡贷款和贸易融资等资产池通证化，为去中心化金融（DeFi）市场提供了新的抵押品和收益来源 9。  
* **国债与货币市场基金**：Ondo Finance等平台将美国国债和货币市场基金通证化，让链上投资者能够直接获取来自这些传统低风险资产的固定收益 16。  
* **房地产**：RealT等平台将房产的所有权分割为可交易的代币，并利用智能合约自动化租金收入的分配，使得房地产投资变得更加灵活和易于管理 10。  
* **知识产权与奢侈品**：高价值艺术品、稀有文学作品、音乐版权等无形资产也可被通证化，实现部分所有权或收益权共享 13。

为了清晰地阐明稳定币与RWA通证化之间的区别与联系，本报告将二者的核心特性归纳如下表。

| 特性\\类型 | 稳定币（法币锚定） | RWA通证（如国债、房地产） |
| :---- | :---- | :---- |
| **底层资产** | 银行存款、短期国债、现金等价物 | 实体资产（如房产）、金融资产（如债券、信贷） |
| **价值支撑** | 100%储备金全额抵押 | 链下实体资产或法律权益 |
| **主要用例** | 支付媒介、价值储存、交易对 | 投资、融资、收益获取、流动性释放 |
| **可分割性** | 高（通常为最小单位的法币，如美元的 0.01） | 高（可分割为小数份额，降低投资门槛） |
| **核心风险** | 发行方透明度、储备金风险、监管风险 | 法律风险、托管风险、流动性风险 |

### **第二章：稳定币与RWA的内在关系与核心驱动力**

#### **2.1 稳定币作为一种特殊的RWA形式**

稳定币与RWA的关系并非截然对立，而是存在着一个深刻的内在逻辑：稳定币本身就是一种特殊且高度流动的RWA。这一关系的理解是剖析整个数字金融生态系统的关键。

法币锚定的稳定币，其价值并非凭空创造，而是直接来源于其链下的储备资产。这些储备资产通常包括银行存款、短期政府债券或其他高流动性、低风险的传统金融工具 2。例如，USDC的发行方Circle通过持有美国国债来支撑其稳定币的价值。从本质上看，USDC代币代表了对这些链下美元储备资产的赎回权。因此，稳定币可以被视为一种\*\*“通证化的储备金”

**或**“通证化的现金等价物”\*\* 5。这种关系是层次性的：稳定币是RWA的子集，是通证化概念在现金及现金等价物上的最广泛应用。

#### **2.2 RWA为稳定币提供收益与稳定性的新范式**

RWA通证化的兴起，正从根本上重塑稳定币的发行模式，解决了困扰传统稳定币市场的“无收益”痛点，并为其提供了更稳健的价值支撑。

**传统稳定币的“收益悖论”**：在传统模式下，中心化稳定币的发行方通过持有高收益的储备资产来赚取巨额利润。例如，Circle通过其储备金（主要是美国国债）获取的利息收入达数十亿美元，但这些收益并不会分配给稳定币持有人 3。这导致了一种不公平的现象：用户承担着稳定币的托管和脱钩风险，却无法分享底层资产所产生的收益。

**RWA-backed稳定币的解决方案**：RWA通证化为这一悖论提供了直接的解决方案。新的发行方将收益型RWA（如国债、信贷）通证化，并将这些代币作为稳定币的抵押品 14。通过这种方式，稳定币持有人能够直接或间接地从底层资产中获得收益，从而创造出一种“生息稳定币”。这种模式直接将传统金融的收益率引入到链上，为DeFi生态带来了急需的稳定收益来源 14。

这一新范式的出现是市场需求驱动的结果。在全球传统银行存款利率持续低迷的背景下，RWA-backed稳定币以其“稳定收益”和“透明度”的特性，正吸引越来越多的机构和个人投资者 18。它为寻求稳定回报的投资者提供了一个独特的链上选择，尤其是在传统金融收益不佳且DeFi收益波动性大的市场环境中。

**案例分析**：

* **MakerDAO**：作为DeFi领域的先驱，MakerDAO在早期主要依赖超额抵押加密资产来发行去中心化稳定币DAI。然而，随着市场发展，其已开始引入RWA作为抵押品，通过私人信贷和房地产贷款等资产为DAI提供收益和价值支持，从而将DeFi与传统金融连接起来 8。  
* **Ondo Finance**：该平台是RWA-backed稳定币的典型代表。Ondo Finance专注于将美国国债等机构级金融产品通证化，并发行了如USDY（U.S. Dollar Yield Token）等带收益的稳定币。其模式要求用户完成KYC验证，并在存款后等待一定的处理时间才能获得代币，这清晰地展示了传统金融的合规流程与链上资产的融合 16。  
* **技术与法律支撑**：预言机（如Chainlink）在其中扮演了关键角色，它为RWA-backed稳定币提供了链下资产价值、储备金状况的实时、可信数据 24。通过“储备金证明”（Proof of Reserve）服务，预言机能够自主、可靠地验证储备资产的真实性，从而确保了RWA-backed稳定币的透明度和可信度 8。

### **第三章：香港作为稳定币与RWA融合的试验场：政策、市场与机遇**

#### **3.1 香港《稳定币条例》：全球领先的监管框架解读**

香港特区政府于2025年5月21日通过了《稳定币条例草案》，并于同年8月1日正式生效 25。这一立法进程使其成为全球首个针对法币稳定币建立全面监管框架的司法管辖区，其速度甚至超越了欧盟的《加密资产市场监管法案》（MiCA） 26。

该条例秉承“相同活动、相同风险、相同监管”的原则，为稳定币发行人设立了严格的持牌要求 26：

* **主体资质**：申请人必须是在香港设立的公司，且最低实缴资本为港币2500万元或等值金额 26。  
* **储备资产**：发行人需维持100%的高质量流动性资产储备，其市值需始终不低于流通中稳定币的总面值。这些储备资产必须与发行人自有资产严格隔离托管，以防范挪用风险 26。  
* **本地实体与赎回保障**：持牌人必须在香港维持实体存在以便金管局实施本地化监管 26。条例还赋予了稳定币持有人按面值随时无附加条件赎回的法定权利 26。  
* **反洗钱/反恐融资**：对超过8000港元的交易强制进行客户尽职调查（KYC），并要求使用区块链分析等技术进行持续监控，强制报告可疑交易 27。

这一监管框架的建立，向全球释放了一个明确信号：监管并非为了打压创新，而是为了\*\*“为可信赖的创新提供稳定结构”\*\* 32。它将稳定币从一个高风险的灰色地带转变为可被纳入传统金融服务体系的工具，为大规模金融机构的介入提供了制度保障 1。

#### **3.2 中国大陆政策红线与“境外参与”的审慎空间**

中国大陆对虚拟货币采取了严格的禁止政策，明确禁止境内一切虚拟货币的发行和交易活动 32。同时，人民币作为受到严格资本管制的货币，其“自由流动”特性与稳定币的“自由流动”特性存在根本性张力 32。

然而，在“一国两制”的框架下，研究材料揭示了一个独特的\*\*“监管缝隙空间”\*\* 32。该通知的适用范围局限于境内活动，因此，大陆企业若在境外（例如香港）设立公司并取得稳定币发行牌照，只要不向大陆用户推广、销售或赎回，目前并未明确违反大陆监管规定 32。

这一“监管缝隙空间”的形成并非偶然。它体现了中国大陆在金融创新与金融安全之间寻求动态平衡的战略考量。中国一方面坚持境内金融安全，优先发展央行数字货币（e-CNY）以筑牢金融安全防线，应对美元霸权带来的风险 33。另一方面，中国有推进人民币国际化的长期战略目标，而稳定币有望成为一种新的跨境支付工具，降低对以SWIFT为中心的美元支付体系的依赖 33。香港的稳定币监管框架为此提供了一个理想的\*\*“沙盒”

**和**“缓冲带”\*\* 29，允许中国企业在可控的离岸环境中探索新型跨境支付和结算工具，这与大陆的长期战略目标高度契合 33。

以下表格将香港的稳定币监管框架与中国大陆的相关政策进行了对比，以更清晰地展示这一独特的“缝隙空间”。

| 特性\\地点 | 中国香港 | 中国大陆 |
| :---- | :---- | :---- |
| **稳定币政策** | 明确的持牌制度，支持合规稳定币发行和交易 26 | 严格限制与禁止，虚拟货币相关业务活动被视为非法金融活动 32 |
| **资本管制** | 自由港，资金自由流动 32 | 严格的资本管制 32 |
| **用户推广** | 允许向公众推广，但有严格的消费者保护和反洗钱要求 27 | 法律禁止向境内用户推广、销售、赎回境外稳定币 32 |
| **数据流通** | 需遵守香港地方法律，如《数据隐私条例》 32 | 需遵守《网络安全法》、《数据安全法》等，涉及重要数据或大量个人信息出境需进行安全评估 37 |
| **法律风险** | 需满足牌照和合规要求，否则面临法律制裁 26 | 触犯“非法吸收公众存款”或“非法经营支付业务”等刑事指控 32 |

#### **3.3 大湾区协同效应：稳定币与RWA的融合应用场景**

香港的监管框架为大湾区乃至更广范围内的稳定币与RWA融合应用提供了合规路径。

**跨境支付与贸易结算**：稳定币的核心优势在于其能够显著提高跨境支付的效率。相比传统的T+1或更长的结算时间，合规稳定币能够实现“实时”处理，并绕开传统SWIFT通道，降低交易成本 26。京东币链科技在香港布局稳定币正是为了优化其跨境电商生态中的供应链结算，解决跨境支付中的效率痛点 40。

**RWA通证化融资**：研究指出，内地企业可以利用香港这一平台，进行基于稳定币的RWA融资。例如，京东供应链的应收账款完全可以进行基于香港稳定币的RWA融资 41。这种模式通常利用境外特殊目的载体（SPV）进行代币发行，由内地资产提供保障，同时遵守香港的监管要求 41。

**数据流转的合规性**：在这一模式中，如何处理跨境数据流转是关键的合规挑战 32。根据《数据出境安全评估办法》，任何涉及境内个人信息和重要数据的跨境流转都必须申报安全评估 32。研究表明，通过采用“跨链桥”技术，将境外发行的RWA通证与境内链上数据进行映射和绑定，可以实现资产数据在链上的透明和可追溯性，同时规避跨境数据传输的合规红线 41。

### **第四章：关键市场参与者与技术生态**

#### **4.1 香港稳定币沙盒参与者案例分析**

香港金管局于2024年3月推出了稳定币发行人“沙盒”机制，并于同年7月公布了首批参与者名单，其中包括多家来自中国大陆的科技巨头和传统金融机构 42。这些参与者的战略布局，反映了其对香港作为数字金融枢纽的重视。

* **京东币链科技（香港）**：作为京东科技的子公司，其在香港的战略布局与其核心业务场景紧密结合。其核心优势在于京东庞大的境外电商生态和跨境零售支付场景 40。京东币链旨在通过发行港币等稳定币，优化其供应链结算，解决跨境支付中的痛点 40。  
* **蚂蚁集团**：蚂蚁国际和蚂蚁数科均已启动香港稳定币牌照申请，这表明其将香港作为全球战略的重要支点。其计划将人工智能、区块链和稳定币创新应用于全球财资管理，凸显了其在Web3领域的战略雄心 1。  
* **渣打银行（香港）联合体**：由渣打银行（香港）、香港电讯（HKT）和Animoca Brands组成的联合体，代表了传统金融机构、电信巨头与Web3企业的跨界合作。该联合体旨在探索稳定币在零售和跨境支付中的应用，为虚拟资产与传统金融体系的衔接提供了跨界合作的典范 26。

这些案例表明，中国大陆企业并非简单地将香港作为绕开监管的避风港，而是将其视为一个重要的“国际化试验田”。其在香港的布局都与其核心业务场景紧密结合，且严格遵循了合规路径。

#### **4.2 RWA通证化背后的法律与技术结构**

RWA通证化的核心挑战是如何在链上的数字代币和链下的物理资产或法律权益之间建立一个可信且可执行的连接 43。这一过程需要复杂的法律与技术结构的协同。

特殊目的载体（SPV）与法律包装：  
RWA通证化并非完全的“去中介化”，它引入了一种名为特殊目的载体（SPV）的法律实体，来充当连接链上与链下的“法律包装”（Legal Wrapper） 44。SPV是一个独立的法律实体，其唯一目的就是持有链下资产（如房地产、债券）。通证化代币代表了对该SPV的权益（例如股权或债券），而非直接代表链下资产本身。这种模式通过法律框架，确保了资产所有权和债务关系的清晰界定 45。SPV模式的引入使得RWA通证化成为一种\*\*“混合型”金融基础设施\*\*，它结合了区块链的自动化和透明度，同时保留了传统法律体系的保障。尽管如此，它仍然需要律师、托管人、会计师等传统中介机构来处理法律和财务事宜 48。  
资产托管与预言机：  
资产托管是RWA-backed稳定币信任机制的基石 14。链下资产的物理或数字托管，确保了底层资产的真实存在和安全性。香港的监管要求储备资产需由持牌银行或独立托管机构保管，以保障投资者的资产安全 31。  
预言机（Oracle）则是连接链下数据与链上智能合约的桥梁 24。RWA通证的价值与链下资产紧密挂钩，因此其价格、资产负债表、储备金状况等信息必须实时、安全地同步到链上。预言机通过\*\*“储备金证明”（Proof of Reserve）\*\*等服务，提供了对储备资产进行自主、可靠验证的能力，从而确保了RWA-backed稳定币的透明度和可信度 8。

以下表格将主要RWA通证化平台的核心业务模式、通证化资产类型和关键优势进行了梳理。

| 平台/项目 | 业务模式 | 通证化资产类型 | 核心优势 |
| :---- | :---- | :---- | :---- |
| **MakerDAO** | 去中心化稳定币协议 | 私人信贷、房地产、国债 | 将RWA引入DeFi，为DAI提供收益与稳定性 8 |
| **Ondo Finance** | 机构级资产通证化平台 | 美国国债、货币市场基金 | 为链上投资者提供低风险、合规的固定收益产品 16 |
| **Centrifuge** | 链上信贷平台 | 消费信贷、贸易融资、房地产贷款 | 将实体信贷引入链上，为DeFi提供非波动性收益 9 |
| **Blocksquare** | 房地产通证化基础设施 | 商业与住宅房地产 | 提供标准化协议，实现房地产的代币化和部分所有权 19 |
| **京东币链** | 供应链金融与跨境支付 | 港币稳定币、应收账款 | 依托京东电商生态，优化跨境结算效率 40 |
| **蚂蚁集团** | Web3与财资管理 | 稳定币（待定） | 将AI、区块链与稳定币融合，探索全球财资管理新模式 1 |
| **渣打联合体** | 跨界合作 | 港币稳定币 | 融合传统金融、电信与Web3，探索零售与跨境支付场景 26 |

### **第五章：挑战、风险与未来的展望**

#### **5.1 技术与运营风险**

稳定币与RWA的融合虽然前景广阔，但其技术与运营风险不容忽视。首先，RWA通证化严重依赖智能合约，其代码中的漏洞可能导致重大安全风险，而区块链上错误的或欺诈性的交易往往无法撤销 10。其次，不同的区块链网络通常互不兼容，这可能导致市场碎片化和流动性问题 5。尽管通证化旨在提高流动性，但在缺乏活跃二级市场和清晰监管框架的情况下，通证化资产可能面临流动性不足的困境，甚至可能加剧金融系统的压力 5。

#### **5.2 法律与合规挑战**

法律与合规是稳定币与RWA融合面临的最严峻挑战。首先，证券法在不同国家和地区差异巨大，一个司法管辖区内合规的通证化证券在另一地可能面临不同的分类和交易限制，从而限制了其全球可及性 10。其次，对于大陆企业而言，任何涉及境内个人信息和重要数据的跨境流转，都必须遵守《数据出境安全评估办法》等严格的规定 32。此外，在大陆，未明确区分用户的情况下，在境外发行的稳定币或RWA通证若向境内居民推广，可能面临“非法吸收公众存款”或“非法经营支付业务”等刑事指控 32。

#### **5.3 未来展望**

尽管存在诸多挑战，但市场对RWA通证化的热情持续高涨。研究预测，RWA通证化市场将在未来几年内迎来爆发式增长，到2030年市场规模可能达到2万亿美元 10。

从区域战略角度看，香港作为连接中国大陆与世界的桥梁，其在离岸人民币稳定币和RWA通证化领域的探索，具有深远的战略意义。尽管存在资本管制和监管协调的挑战，但香港作为试验田，其在“一带一路”沿线构建人民币稳定币流动性网络，以支持更广泛的跨境投融资需求的探索值得期待 34。

稳定币与RWA的融合将加速全球金融基础设施的重塑。它不仅为传统金融机构提供了新的增长点，还为发展中国家提供了一种新的跨境支付和价值储存工具 33。这种模式最终可能创造一个更加开放、高效且普惠的全球金融生态系统。

### **第六章：战略建议与行动指南**

#### **6.1 对金融机构与企业的建议**

**合规先行，风险隔离**：大陆企业若有意通过香港参与稳定币和RWA市场，必须将合规置于首位。应参照香港《稳定币条例》的核心要求，建立严谨的内部合规防火墙、储备金管理、KYC/AML体系 31。尤其要通过法律和财务上的职能切割，将发行、钱包、储备管理等职能予以隔离，以防范涉嫌非法集资等刑事风险 32。

**用户与数据绝对隔离**：严格执行对大陆用户的绝对隔离是参与香港市场的核心前提。这包括但不限于：不向大陆用户推广、销售、赎回产品；实施IP地址封锁、实名验证和地理限制等技术手段；并严格遵守《数据出境安全评估办法》，在涉及跨境数据流转时提前完成备案或评估手续 32。

**探索沙盒机制**：对于新进入者而言，优先参与香港金管局的稳定币沙盒是明智的策略。这不仅能在受控环境中测试业务模型，还能与监管机构建立沟通渠道，为正式牌照申请奠定基础 26。

#### **6.2 对投资者的建议**

**识别法律风险**：境内投资者应充分认识到稳定币与加密货币在大陆的严格监管政策，避免直接参与。在与境内主体有关的交易中直接使用稳定币结算，可能会面临法律风险和资金冻结的风险 36。

**寻求专业帮助**：投资者若在境外参与，应寻求专业的法律和合规团队帮助，在合规框架内构建自身的投资体系。持续关注世界主要国家或地区的监管政策动向，是规避风险的必要措施 36。

#### **6.3 对政策制定者的启示与建议**

**利用香港的桥梁作用**：充分利用香港作为“一国两制”下的独特制度优势，将其作为数字金融创新的“缓冲带”和国际化试验田。香港的探索可以为大陆在未来发展离岸人民币稳定币和探索跨境RWA融资提供宝贵的经验 34。

**加强监管协同**：由于稳定币和RWA天然具备跨境特性，加强两地监管协同至关重要。建议建立与香港等境外监管机构的联合工作机制，优化跨境监管协调，尤其是在反洗钱和数据流通方面 34。

**完善数据流通机制**：在保障国家安全和社会公共利益的前提下，积极探索便利化的数据跨境流动安全管理机制，为合规的数字经济发展提供支持，以适应稳定币与RWA融合带来的新需求 38。

#### **引用的著作**

1. 互联网大厂竞逐稳定币 \- 证券时报, 访问时间为 九月 2, 2025， [https://www.stcn.com/article/detail/2041116.html](https://www.stcn.com/article/detail/2041116.html)  
2. Stablecoins: Market Developments, Risks and Regulation \- Reserve Bank of Australia, 访问时间为 九月 2, 2025， [https://www.rba.gov.au/publications/bulletin/2022/dec/pdf/stablecoins-market-developments-risks-and-regulation.pdf](https://www.rba.gov.au/publications/bulletin/2022/dec/pdf/stablecoins-market-developments-risks-and-regulation.pdf)  
3. Stablecoins: A new way to pay | Davy, 访问时间为 九月 2, 2025， [https://www.davy.ie/market-and-insights/insights/the-davy-wealth-view/2025/insights/stablecoins-a-new-way-to-pay.html](https://www.davy.ie/market-and-insights/insights/the-davy-wealth-view/2025/insights/stablecoins-a-new-way-to-pay.html)  
4. 10,000-Word Analysis of Stablecoins: New Infrastructure or New Risks?, 访问时间为 九月 2, 2025， [https://eu.36kr.com/en/p/3448884501763716](https://eu.36kr.com/en/p/3448884501763716)  
5. Tokenized Assets | Congress.gov, 访问时间为 九月 2, 2025， [https://www.congress.gov/crs-product/IF12670](https://www.congress.gov/crs-product/IF12670)  
6. RWA.xyz | Analytics on Tokenized Real-World Assets, 访问时间为 九月 2, 2025， [https://app.rwa.xyz/](https://app.rwa.xyz/)  
7. www.coinbase.com, 访问时间为 九月 2, 2025， [https://www.coinbase.com/learn/crypto-glossary/what-are-real-world-assets-rwa\#:\~:text=Real%2DWorld%20Assets%20(RWAs),engage%20with%20high%2Dvalue%20assets.](https://www.coinbase.com/learn/crypto-glossary/what-are-real-world-assets-rwa#:~:text=Real%2DWorld%20Assets%20\(RWAs\),engage%20with%20high%2Dvalue%20assets.)  
8. Real-World Assets (RWAs) Explained \- Chainlink, 访问时间为 九月 2, 2025， [https://chain.link/education-hub/real-world-assets-rwas-explained](https://chain.link/education-hub/real-world-assets-rwas-explained)  
9. Tokenized Private Credit: \- S\&P Global, 访问时间为 九月 2, 2025， [https://www.spglobal.com/content/dam/spglobal/global-assets/en/special-reports/Corp\_1022\_TokenizedPrivateCredit.pdf](https://www.spglobal.com/content/dam/spglobal/global-assets/en/special-reports/Corp_1022_TokenizedPrivateCredit.pdf)  
10. Real-world asset tokenization: What's hype and what's not \- Elliptic, 访问时间为 九月 2, 2025， [https://www.elliptic.co/blockchain-basics/real-world-asset-tokenization-whats-hype-and-whats-not](https://www.elliptic.co/blockchain-basics/real-world-asset-tokenization-whats-hype-and-whats-not)  
11. What Is RWA Tokenization? A Comprehensive Guide To Real-World Assets And Tokenization \- Huma Finance, 访问时间为 九月 2, 2025， [https://blog.huma.finance/what-is-rwa-tokenization-how-real-world-assets-are-shaping-the-future-of-finance](https://blog.huma.finance/what-is-rwa-tokenization-how-real-world-assets-are-shaping-the-future-of-finance)  
12. Demystifying RWA: The benefits and trends in Real-World Asset tokenization | Venly, 访问时间为 九月 2, 2025， [https://www.venly.io/blog/demystifying-rwa-the-benefits-and-trends-in-real-world-asset-tokenization](https://www.venly.io/blog/demystifying-rwa-the-benefits-and-trends-in-real-world-asset-tokenization)  
13. What Is Asset Tokenization? Meaning, Examples, Pros, & Cons | Britannica Money, 访问时间为 九月 2, 2025， [https://www.britannica.com/money/real-world-asset-tokenization](https://www.britannica.com/money/real-world-asset-tokenization)  
14. RWA-Backed Stablecoins: Growth, Benefits & How to Develop in 2025, 访问时间为 九月 2, 2025， [https://www.suffescom.com/blog/rwa-backed-stablecoins-growth-benefits-development](https://www.suffescom.com/blog/rwa-backed-stablecoins-growth-benefits-development)  
15. What are the Benefits of Real-World Asset Tokenization (RWA) for Founders? | Sparring, 访问时间为 九月 2, 2025， [https://sparring.io/what-are-the-benefits-of-real-world-asset-tokenization-for-founders/](https://sparring.io/what-are-the-benefits-of-real-world-asset-tokenization-for-founders/)  
16. What Is Ondo (ONDO)? \- Binance Academy, 访问时间为 九月 2, 2025， [https://academy.binance.com/en/articles/what-is-ondo-ondo](https://academy.binance.com/en/articles/what-is-ondo-ondo)  
17. Ondo Finance Price, ONDO Price, Live Charts, and Marketcap \- Coinbase, 访问时间为 九月 2, 2025， [https://www.coinbase.com/price/ondo-finance](https://www.coinbase.com/price/ondo-finance)  
18. Q2 2025 RWA Tokenization Market Report \- InvestaX, 访问时间为 九月 2, 2025， [https://www.investax.io/blog/q2-2025-rwa-tokenization-market-report](https://www.investax.io/blog/q2-2025-rwa-tokenization-market-report)  
19. Blocksquare (BST) \- Analysis & Overview \- Coinmetro, 访问时间为 九月 2, 2025， [https://www.coinmetro.com/price/bst](https://www.coinmetro.com/price/bst)  
20. 100 Use Cases of Real-World Asset (RWA) Tokenization \- Zoniqx, 访问时间为 九月 2, 2025， [https://www.zoniqx.com/resources/100-use-cases-of-real-world-asset-rwa-tokenization](https://www.zoniqx.com/resources/100-use-cases-of-real-world-asset-rwa-tokenization)  
21. RWA Marketing Trends 2025: What You Need to Know? | by Blockchain App Factory, 访问时间为 九月 2, 2025， [https://medium.com/predict/rwa-marketing-trends-2025-what-you-need-to-know-7bcfa5068eb3](https://medium.com/predict/rwa-marketing-trends-2025-what-you-need-to-know-7bcfa5068eb3)  
22. What is Ondo? Unlocking the Future of Tokenized Real-World Assets \- OKX, 访问时间为 九月 2, 2025， [https://www.okx.com/learn/what-is-ondo-tokenized-real-world-assets](https://www.okx.com/learn/what-is-ondo-tokenized-real-world-assets)  
23. What is Ondo? Why Tokenize Real-World Assets? \- BitKan.com, 访问时间为 九月 2, 2025， [https://bitkan.com/learn/what-is-ondo-why-tokenize-real-world-assets-23650](https://bitkan.com/learn/what-is-ondo-why-tokenize-real-world-assets-23650)  
24. Chainlink: The Industry-Standard Oracle Platform, 访问时间为 九月 2, 2025， [https://chain.link/](https://chain.link/)  
25. 《穩定幣條例》8月1日生效促進香港金融創新, 访问时间为 九月 2, 2025， [https://beltandroad.hktdc.com/tc/insights/hong-kong-opens-its-doors-stablecoins](https://beltandroad.hktdc.com/tc/insights/hong-kong-opens-its-doors-stablecoins)  
26. 香港《稳定币条例》正式生效：解读全球首个法币稳定币全面监管 ..., 访问时间为 九月 2, 2025， [https://www.dehenglaw.com/CN/tansuocontent/0008/034252/7.aspx?MID=0902\&AID=](https://www.dehenglaw.com/CN/tansuocontent/0008/034252/7.aspx?MID=0902&AID)  
27. 香港稳定币条例将于2025年8月1日生效，开启虚拟资产监管新时代, 访问时间为 九月 2, 2025， [https://www.sw-hk.com/zh/hong-kongs-stablecoins-ordinance-to-take-effect-on-1-august-2025-welcoming-a-new-era-for-virtual-asset-regulation/](https://www.sw-hk.com/zh/hong-kongs-stablecoins-ordinance-to-take-effect-on-1-august-2025-welcoming-a-new-era-for-virtual-asset-regulation/)  
28. 香港《稳定币条例》正式实施 \- Law.asia, 访问时间为 九月 2, 2025， [https://law.asia/zh-hans/hong-kong-stablecoins-legislation/](https://law.asia/zh-hans/hong-kong-stablecoins-legislation/)  
29. 大国博弈与新秩序|香港稳定币法案发布，全球风云再起 \- 中证鹏元, 访问时间为 九月 2, 2025， [https://www.cspengyuan.com/pengyuancmscn/credit-research/macro-research/20250604183256588/%E9%A6%99%E6%B8%AF%E7%A8%B3%E5%AE%9A%E5%B8%81%E6%B3%95%E6%A1%88%E5%8F%91%E5%B8%83%EF%BC%8C%E5%85%A8%E7%90%83%E9%A3%8E%E4%BA%91%E5%86%8D%E8%B5%B7.pdf](https://www.cspengyuan.com/pengyuancmscn/credit-research/macro-research/20250604183256588/%E9%A6%99%E6%B8%AF%E7%A8%B3%E5%AE%9A%E5%B8%81%E6%B3%95%E6%A1%88%E5%8F%91%E5%B8%83%EF%BC%8C%E5%85%A8%E7%90%83%E9%A3%8E%E4%BA%91%E5%86%8D%E8%B5%B7.pdf)  
30. 香港《稳定币条例》正式生效：发牌制度与市场影响全面解读, 访问时间为 九月 2, 2025， [https://www.zhonglun.com/research/articles/54623.html](https://www.zhonglun.com/research/articles/54623.html)  
31. 8月1日起实施！香港《稳定币条例》落地，要点解读（下）, 访问时间为 九月 2, 2025， [https://www.joius.com/news\_info.html?id=532](https://www.joius.com/news_info.html?id=532)  
32. 香港稳定币监管新规对中资企业的影响, 访问时间为 九月 2, 2025， [https://www.hanshenglaw.cn/CN/08/993cbb6d0aba4002.aspx](https://www.hanshenglaw.cn/CN/08/993cbb6d0aba4002.aspx)  
33. 从监管视角看中国稳定币未来发展, 访问时间为 九月 2, 2025， [https://pdf.dfcfw.com/pdf/H3\_AP202506251697484638\_1.pdf?1750883072000.pdf](https://pdf.dfcfw.com/pdf/H3_AP202506251697484638_1.pdf?1750883072000.pdf)  
34. 稳定币的法律监管与离岸人民币稳定币发展前景展望 \- 君泽君律师事务所, 访问时间为 九月 2, 2025， [https://www.junzejun.com/Publications/1111035919ed64-4.html](https://www.junzejun.com/Publications/1111035919ed64-4.html)  
35. 为人民币稳定币立规 \- 中国金融四十人论坛, 访问时间为 九月 2, 2025， [https://www.cf40.org.cn/article/1/289158](https://www.cf40.org.cn/article/1/289158)  
36. 香港《稳定币条例》颁布系列文章（中）——香港《稳定币条例》的 ..., 访问时间为 九月 2, 2025， [https://www.allbrightlaw.com/CN/10475/b55a3ebf6f82b360.aspx](https://www.allbrightlaw.com/CN/10475/b55a3ebf6f82b360.aspx)  
37. 数据出境安全评估办法\_国务院部门文件 \- 中国政府网, 访问时间为 九月 2, 2025， [https://www.gov.cn/zhengce/zhengceku/2022-07/08/content\_5699851.htm](https://www.gov.cn/zhengce/zhengceku/2022-07/08/content_5699851.htm)  
38. 我国数据跨境流动监管现状观察与建议 \- 安全内参, 访问时间为 九月 2, 2025， [https://www.secrss.com/articles/63072](https://www.secrss.com/articles/63072)  
39. 中国发布个人信息出境标准合同草案并明确数据出境机制 \- Latham & Watkins LLP, 访问时间为 九月 2, 2025， [https://www.lw.com/zh/admin/upload/SiteAttachments/Alert%202998.pdf](https://www.lw.com/zh/admin/upload/SiteAttachments/Alert%202998.pdf)  
40. 《大行》国金证券列出香港稳定币三组「沙盒」参与方对比(表), 访问时间为 九月 2, 2025， [http://www.aastocks.com/sc/stocks/news/aafn-news/NOW.1454449/3](http://www.aastocks.com/sc/stocks/news/aafn-news/NOW.1454449/3)  
41. 香港《稳定币条例草案》颁布后内地企业跨境RWA融资机会, 访问时间为 九月 2, 2025， [https://www.grandall.com.cn/guohaoanli/info.aspx?itemid=30939](https://www.grandall.com.cn/guohaoanli/info.aspx?itemid=30939)  
42. 香港金融管理局- 金管局宣布稳定币发行人「沙盒」参与者 \- Hong Kong Monetary Authority, 访问时间为 九月 2, 2025， [https://www.hkma.gov.hk/gb\_chi/news-and-media/press-releases/2024/07/20240718-4/](https://www.hkma.gov.hk/gb_chi/news-and-media/press-releases/2024/07/20240718-4/)  
43. Real-World Assets (RWA) Tokenization: Complete Web3 Guide \- Webisoft, 访问时间为 九月 2, 2025， [https://webisoft.com/articles/real-world-assets-rwa-tokenization-guide/](https://webisoft.com/articles/real-world-assets-rwa-tokenization-guide/)  
44. Governance & Jurisdiction in Tokenized Real Estate | Hedera, 访问时间为 九月 2, 2025， [https://hedera.com/blog/governance-jurisdiction-in-tokenized-real-estate](https://hedera.com/blog/governance-jurisdiction-in-tokenized-real-estate)  
45. Tokenized Stocks and the Next Evolution of Capital Markets \- InvestaX, 访问时间为 九月 2, 2025， [https://www.investax.io/blog/tokenized-stocks-and-the-next-evolution-of-capital-markets](https://www.investax.io/blog/tokenized-stocks-and-the-next-evolution-of-capital-markets)  
46. What is The Role of SPV Structure in Tokenization? \- Antier Solutions, 访问时间为 九月 2, 2025， [https://www.antiersolutions.com/blogs/the-role-of-spv-structure-in-tokenization-a-comprehensive-guide/](https://www.antiersolutions.com/blogs/the-role-of-spv-structure-in-tokenization-a-comprehensive-guide/)  
47. www.solulab.com, 访问时间为 九月 2, 2025， [https://www.solulab.com/spvs-in-asset-tokenization/\#:\~:text=As%20businesses%20adopt%20blockchain%20and,real%20estate%20or%20fine%20art.](https://www.solulab.com/spvs-in-asset-tokenization/#:~:text=As%20businesses%20adopt%20blockchain%20and,real%20estate%20or%20fine%20art.)  
48. The Future of Real Estate Tokenization: Bonds, SPVs, and Title Deeds Explained \- Scintilla, 访问时间为 九月 2, 2025， [https://www.scintillanetwork.com/blogs/the-future-of-real-estate-tokenization-bonds-spvs-and-title-deeds-explained](https://www.scintillanetwork.com/blogs/the-future-of-real-estate-tokenization-bonds-spvs-and-title-deeds-explained)  
49. Legal Compliance Checklist for The Tokenization of Real World Assets (RWAs) \- InvestaX, 访问时间为 九月 2, 2025， [https://www.investax.io/blog/legal-compliance-checklist-for-the-tokenization-of-real-world-assets-rwas](https://www.investax.io/blog/legal-compliance-checklist-for-the-tokenization-of-real-world-assets-rwas)  
50. Top 10 Real World Assets (RWA) Crypto in August 2025 | Tangem ..., 访问时间为 九月 2, 2025， [https://tangem.com/en/blog/post/real-world-assets-rwa/](https://tangem.com/en/blog/post/real-world-assets-rwa/)  
51. protocol \- Blocksquare | Tokenization infrastructure for real estate., 访问时间为 九月 2, 2025， [https://blocksquare.io/products/tokenization-protocol](https://blocksquare.io/products/tokenization-protocol)  
52. Top 6 Challenges in RWA Tokenization and How to Overcome Them \- Debut Infotech, 访问时间为 九月 2, 2025， [https://www.debutinfotech.com/blog/top-rwa-tokenization-challenges](https://www.debutinfotech.com/blog/top-rwa-tokenization-challenges)  
53. Compliance Challenges in RWA Tokenization \- RWA.io, 访问时间为 九月 2, 2025， [https://www.rwa.io/post/compliance-challenges-in-rwa-tokenization](https://www.rwa.io/post/compliance-challenges-in-rwa-tokenization)  
54. Tokenization of Real-World Assets: Opportunities, Challenges and the Path Ahead, 访问时间为 九月 2, 2025， [https://katten.com/tokenization-of-real-world-assets-opportunities-challenges-and-the-path-ahead](https://katten.com/tokenization-of-real-world-assets-opportunities-challenges-and-the-path-ahead)  
55. Tokenize Everything, But Can You Sell It? RWA Liquidity Challenges and the Road Ahead, 访问时间为 九月 2, 2025， [https://arxiv.org/html/2508.11651v1](https://arxiv.org/html/2508.11651v1)  
56. Legal Frameworks for Real-World Asset Tokenization \- RWA.io, 访问时间为 九月 2, 2025， [https://www.rwa.io/post/legal-frameworks-for-real-world-asset-tokenization](https://www.rwa.io/post/legal-frameworks-for-real-world-asset-tokenization)