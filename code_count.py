"""
代码统计
"""
import os
from typing import List, Dict


def get_py_file(src: str) -> List[str]:
    """
    获取目标目录下所有的.py文件
    :param src: 根目录
    :return: 目录下所有.py文件的绝对路径
    """
    files = []
    for parent, dirnames, filenames in os.walk(src):
        for file in filenames:
            if os.path.splitext(file)[-1] == ".py":
                abspath = os.path.abspath(os.path.join(parent, file))
                files.append(abspath)
    return files


def format_map(file: str) -> Dict[str, int]:
    """
    统计代码中的空白、代码、注释
    'space'
    'code'
    'comment'
    :param file: 文件名
    :return: 统计后的字典
    """
    d = {}

    def _count_item(key, start=0) -> None:
        d[key] = d.get(key, start) + 1

    isdoc = False
    with open(file) as f:
        for line in f:
            if line.rstrip() == '"' * 3:
                isdoc = not isdoc
                _count_item('comment')
            if isdoc:
                _count_item('comment')
                continue
            if line.isspace():
                _count_item('space')
            elif line.lstrip().startswith('#'):
                _count_item('comment')
            else:
                _count_item('code')

    return d


d = {}
src = "./"
for file in get_py_file(src):
    d[file] = format_map(file)
print(d)
