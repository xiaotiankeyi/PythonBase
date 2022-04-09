"""
    概念:
        1、标签语言
        2、自闭和标签、非闭合标签

"""
import xml.etree.ElementTree as ET

"""获取根节点标签名字"""
tree = ET.parse("xmltest.xml")      #获取文档地址
root = tree.getroot()
# print(root.tag)

"""遍历xml文档"""
# for child in root:
#     """输出子节点标签及属性"""
#     print('=======', child.tag,child.attrib,child.attrib["name"])
#     for i in child:
#         print(i.tag, i.attrib, i.text)

"""查询__只遍历year节点"""
for node in root.iter('year'):
    print(node.tag, node.text)

"""修改"""
# for node in root.iter('year'):
#     new_year = int(node.text) +1
#     node.text = str(new_year)
#     node.set('updated', 'yes')
#     node.set('version', '1.0')
#     # print(new_year)
# tree.write('test_xml.xml')

"""删除node"""
for country in root.findall('country'):
    rank = int(country.find('rank').text)
    if rank > 50:
        root.remove(country)

tree.write('output.xml')
