from bs4 import BeautifulSoup

# 解析本地文件
soup = BeautifulSoup(open('./bs4基本使用.html', 'r', encoding='utf-8'), 'lxml')

print(soup.a)
# (1) find
print(soup.find('a'))

print(soup.find('a', title='a2'))

print(soup.find('a', class_='a1'))

# (2) find_all
print(soup.find_all('a'))

print(soup.find_all(['a', 'span']))

print(soup.find_all('li', limit=2))

# (3) select
print(soup.select('a'))

print(soup.select('.a1'))

print(soup.select('#a2'))

print(soup.select('li[id]'))

print(soup.select('li[id="zhangsan"]'))

# 层级选择器
# 后代选择器
print(soup.select('div li'))
# 子代选择器
print(soup.select('div > ul > li'))
# 所有标签
print(soup.select('li, a'))
print(soup.select('div li,div a'))

# 节点信息
obj = soup.select('#d1')[0]
# 如果标签对象中除了内容还有标签, string获取不到数据, 推荐使用get_text()
print(obj.string)
print(obj.get_text())

# 节点的属性
obj = soup.select('#plpl')[0]
# 标签的名字
print(obj.name)
# 属性值作为字典返回
print(obj.attrs)

# 获取节点的属性
print(obj.attrs.get('class'))
print(obj.get('class'))
print(obj['class'])

# 解析网络文件
