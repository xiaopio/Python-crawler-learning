from lxml import etree

# xpath解析
# 本地文件
# 服务器响应的数据

# xpath解析本地文件
tree = etree.parse('./xpath的基本使用.html')
# tree.xpath('xpath路径')
#   //: 查找所有的子孙节点,不考虑层级关系
#   /:  找直接子节点
# 查找ul下的li
li_list = tree.xpath('//body/ul/li')
# 7
print(len(li_list))

# 谓词查询
# 查找所有有id属性的li标签
li_list = tree.xpath('//ul/li[@id]')
# 4
print(len(li_list))
# 找id为11的li标签里的内容
content = tree.xpath('//ul/li[@id="11"]/text()')
# ['北京']
print(content)

# 属性查询
# 查找id为11的标签的class属性值
content = tree.xpath('//ul/li[@id="11"]/@class')
# ['beijing']
print(content)

# 模糊查询
# 查询id中包含c的标签

li_list = tree.xpath('//ul/li[contains(@id, "c")]/text()')
# ['上海', '深圳', '武汉']
print(li_list)

# 查询id的值以c开头的li标签
li_list = tree.xpath('//ul/li[starts-with(@id,"c")]/text()')
# ['深圳', '武汉']
print(li_list)

# 逻辑运算

# 查询id为c1,class为shenzhen的li标签
li = tree.xpath('//ul/li[@id="c1" and @class="shenzhen"]/text()')
# ['深圳']
print(li)

# 查询id为c1或id为c2的标签
li_list = tree.xpath('//ul/li[@id="c1"]/text() | //ul/li[@id="c2"]/text()')
# ['深圳', '武汉']
print(li_list)
