"""高级的文件夹,文件,压缩包处理模块"""

import shutil

"""将文件内容拷贝到例外一个文件夹中"""
shutil.copyfileobj(open('a.txt', 'r'), open('s.txt', 'w'))

"""拷贝文件,目标文件无需存在"""
shutil.copyfile('s.txt', 's2.txt')

"""拷贝文件和权限"""
# shutil.copy('', '')

"""递归的去删除文件"""
# time.sleep(2)
# shutil.rmtree()
#
"""递归的去移动文件"""
# shutil.move("",'')

# ==================================================
shutil.make_archive(
    base_name='压缩文件',
    format='zip',
    root_dir="C:/Users/admin/PycharmProjects/python/python_module/shutil_file")
