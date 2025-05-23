import os
import re
from pathlib import Path
import logging


# 配置参数
REPORT_DIR = "weekly_reports"           # 周报文件存放目录
README_PATH = "README.md"     # README 文件路径
MAX_ENTRIES = 1              # 最多显示的周报数量
DATE_PATTERNS = [
    r"(第\d+期)_(.*?)\.md",      # 第1期_描述.md
    r"week(\d+)(?:_(.*?))?\.md", # week1_描述.md 或 week1.md
    r"report_(\d{4}-\d{2}-\d{2})(?:_(.*?))?\.md",  # report_2025-04-28_描述.md 或 report_2025-04-28.md
]

# 配置日志
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def extract_report_info(filename):
    """
    从文件名中提取期数或日期信息
    返回示例：{"issue": "第1期", "filename": "第1期_周报.md"}
    """
    for pattern in DATE_PATTERNS:
        match = re.match(pattern, filename)
        if match:
            issue = match.group(1) if match.group(1) else ""
            return {
                "issue": issue,
                "filename": filename,
            }
    logging.warning(f"文件名 {filename} 不符合任何规则: {DATE_PATTERNS}")
    return None


def generate_markdown(reports):
    """
    生成 Markdown 内容，添加「第 X 期:」前缀，[ ] 中只显示核心标题
    """
    markdown = ""  # 初始化字符串
    for report in reports:
        filename = report["filename"]
        issue = report["issue"]

        # 提取核心标题（去除前缀）
        if filename.startswith("第"):
            parts = filename.split("_", 1)
            title_part = parts[1] if len(parts) > 1 else filename
        elif filename.startswith("week"):
            title_part = filename.split("_", 1)[1] if "_" in filename else filename
        elif filename.startswith("report_"):
            title_part = filename.split("_", 2)[-1] if "_" in filename else filename
        else:
            title_part = filename

        # 去除 .md 扩展名
        title = os.path.splitext(title_part)[0]

        # 添加「第 X 期:」前缀
        if issue:
            issue_with_space = re.sub(r"(第)(\d+)(期)", r"\1 \2 \3", issue)
            prefix = f"{issue_with_space}: "
        else:
            prefix = ""

        # 生成 GitHub 链接
        file_path = Path(REPORT_DIR) / filename
        file_url = f"{file_path.as_posix()}"
        markdown += f"- {prefix}[{title}]({file_url})\n"
    return markdown


def update_readme():
    """更新 README.md 中的自动生成部分"""
    try:
        # 获取所有周报文件
        report_dir = Path(REPORT_DIR)
        if not report_dir.exists():
            logging.error(f"报告目录 {REPORT_DIR} 不存在")
            return

        files = [f.name for f in report_dir.iterdir() if f.is_file() and f.suffix.lower() == ".md"]
        logging.info(f"找到 {len(files)} 个 Markdown 文件")

        # 提取并排序
        reports = []
        for filename in files:
            info = extract_report_info(filename)
            if info:
                reports.append(info)

        if not reports:
            logging.warning("未找到符合规则的周报文件")
            return

        # 根据期数或日期排序
        def sort_key(report):
            if re.match(r"第\d+期", report["issue"]):
                return int(re.search(r"\d+", report["issue"]).group())
            elif re.match(r"\d{4}-\d{2}-\d{2}", report["issue"]):
                return report["issue"]  # 日期字符串自然排序
            else:
                return 0  # 默认排序

        reports.sort(key=lambda x: sort_key(x), reverse=True)
        reports = reports[:MAX_ENTRIES]
        logging.info(f"已筛选出 {len(reports)} 个有效周报文件")

        # 生成 Markdown 内容
        new_content = generate_markdown(reports)

        # 读取并更新 README
        if not os.path.exists(README_PATH):
            logging.error(f"README 文件 {README_PATH} 不存在")
            return

        with open(README_PATH, "r", encoding="utf-8") as f:
            readme_lines = f.readlines()

        start_marker = "<!-- AUTOGENERATED_REPORTS -->\n"
        end_marker = "<!-- END_AUTOGENERATED -->\n"
        new_readme = []
        in_section = False

        # 遍历 README 行，插入内容到 <!-- END_AUTOGENERATED --> 后面
        for line in readme_lines:
            if line == start_marker:
                in_section = True
                new_readme.append(line)
            elif line == end_marker:
                in_section = False
                new_readme.append(line)
                new_readme.append(new_content + "\n")  # 插入新内容到 end_marker 后
            elif not in_section:
                new_readme.append(line)

        # 比较内容是否变化
        current_content = "".join(readme_lines)
        new_content_full = "".join(new_readme)
        if current_content == new_content_full:
            logging.info("内容无变化，跳过更新 README.md")
            return

        with open(README_PATH, "w", encoding="utf-8") as f:
            f.writelines(new_readme)

        logging.info("README.md 已更新，并在 <!-- END_AUTOGENERATED --> 后添加了新内容。")

    except Exception as e:
        logging.error(f"更新 README 时发生错误: {e}")


if __name__ == "__main__":
    update_readme()