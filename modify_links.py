import sys
from bs4 import BeautifulSoup

file_path = 'docs/index.html'
target_url = 'https://github.com/img-zhinao/updatefile/blob/main/README.md'

try:
    with open(file_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')

    # 查找所有的 <a> 标签
    for a_tag in soup.find_all('a'):
        # 修改 href 属性为目标 URL
        a_tag['href'] = target_url

    # 以 UTF-8 编码写回修改后的 HTML 文件
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(str(soup))

    print(f'Successfully updated links in {file_path} to {target_url}')

except FileNotFoundError:
    print(f'Error: {file_path} not found.')
    sys.exit(1)
except Exception as e:
    print(f'An error occurred: {e}')
    sys.exit(1)
