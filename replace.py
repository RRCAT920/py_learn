import sys
import os
"""
全局替换程序
    写一个脚本，允许用户按以下方式执行时，即可以对指定文件内容进行全局替换
    python your_script.py old_str new_str filename
    替换完毕后打印替换了多少处内容
"""
new_file = sys.argv[3] + '.new'
count = 0
with open(sys.argv[3]) as fr:
    with open(new_file, 'w') as fw:
        for line in fr:
            if sys.argv[1] in line:
                count += 1
                fw.write(line.replace(sys.argv[1], sys.argv[2]))

os.rename(new_file, sys.argv[3])
print(count)