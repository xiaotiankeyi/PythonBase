with open("study_file.txt", 'w') as s:
    s.write("student\nteachers")

    """判断是否可以写入...."""
    print(s.writable())

    """与列表形式写入文件......"""
    s.writelines(["\nclass","\n","subjects"])

    """在使用with时不需要手动关闭，，函数会自动关闭打开的文件....."""

"""
< w+ (读、写、覆盖、创建、指针在开始) >/打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。
如果该文件不存在，创建新文件。
"""