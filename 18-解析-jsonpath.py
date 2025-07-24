import json
import jsonpath

obj = json.load(open('./store.json', 'r', encoding='utf-8'))

# 书店所有书的作者
result = jsonpath.jsonpath(obj=obj, expr='$.store.book[*].author')
# ['Nigel Rees', 'Evelyn Waugh', 'Herman Melville', 'J. R. R. Tolkien']
print(result)

# 所有的作者
result = jsonpath.jsonpath(obj, '$..author')
# ['Nigel Rees', 'Evelyn Waugh', 'Herman Melville', 'J. R. R. Tolkien', 'Jack']
print(result)

# store的所有元素
result = jsonpath.jsonpath(obj, '$.store.*')
# [[{'category': 'reference', 'author': 'Nigel Rees', 'title': 'Sayings of the Century', 'price': 8.95}, {'category': 'fiction', 'author': 'Evelyn Waugh', 'title': 'Sword of Honour', 'price': 12.99}, {'category': 'fiction', 'author': 'Herman Melville', 'title': 'Moby Dick', 'isbn': '0-553-21311-3', 'price': 8.99}, {'category': 'fiction', 'author': 'J. R. R. Tolkien', 'title': 'The Lord of the Rings', 'isbn': '0-395-19395-8', 'price': 22.99}], {'author': 'Jack', 'color': 'red', 'price': 19.95}]
print(result)

# store里面所有东西的price
result = jsonpath.jsonpath(obj, '$.store..price')
# [8.95, 12.99, 8.99, 22.99, 19.95]
print(result)

# 第三个书
result = jsonpath.jsonpath(obj, '$..book[2]')
# [{'category': 'fiction', 'author': 'Herman Melville', 'title': 'Moby Dick', 'isbn': '0-553-21311-3', 'price': 8.99}]
print(result)

# 最后一本书
result = jsonpath.jsonpath(obj, '$..book[(@.length-1)]')
# [{'category': 'fiction', 'author': 'J. R. R. Tolkien', 'title': 'The Lord of the Rings', 'isbn': '0-395-19395-8', 'price': 22.99}]
print(result)

# 前面的两本书
result = jsonpath.jsonpath(obj, '$..book[0,1]')
result = jsonpath.jsonpath(obj, '$..book[:2]')
# [{'category': 'reference', 'author': 'Nigel Rees', 'title': 'Sayings of the Century', 'price': 8.95}, {'category': 'fiction', 'author': 'Evelyn Waugh', 'title': 'Sword of Honour', 'price': 12.99}]
print(result)

# 过滤出所有的包含isbn的书
result = jsonpath.jsonpath(obj, '$..book[?(@.isbn)]')
# [{'category': 'fiction', 'author': 'Herman Melville', 'title': 'Moby Dick', 'isbn': '0-553-21311-3', 'price': 8.99}, {'category': 'fiction', 'author': 'J. R. R. Tolkien', 'title': 'The Lord of the Rings', 'isbn': '0-395-19395-8', 'price': 22.99}]
print(result)

# 过滤出价格低于10的书
result = jsonpath.jsonpath(obj, '$..book[?(@.price<20)]')
# [{'category': 'reference', 'author': 'Nigel Rees', 'title': 'Sayings of the Century', 'price': 8.95}, {'category': 'fiction', 'author': 'Evelyn Waugh', 'title': 'Sword of Honour', 'price': 12.99}, {'category': 'fiction', 'author': 'Herman Melville', 'title': 'Moby Dick', 'isbn': '0-553-21311-3', 'price': 8.99}]
print(result)

# 所有元素
result = jsonpath.jsonpath(obj, '$..*')
# [{'book': [{'category': 'reference', 'author': 'Nigel Rees', 'title': 'Sayings of the Century', 'price': 8.95}, {'category': 'fiction', 'author': 'Evelyn Waugh', 'title': 'Sword of Honour', 'price': 12.99}, {'category': 'fiction', 'author': 'Herman Melville', 'title': 'Moby Dick', 'isbn': '0-553-21311-3', 'price': 8.99}, {'category': 'fiction', 'author': 'J. R. R. Tolkien', 'title': 'The Lord of the Rings', 'isbn': '0-395-19395-8', 'price': 22.99}], 'bicycle': {'author': 'Jack', 'color': 'red', 'price': 19.95}}, [{'category': 'reference', 'author': 'Nigel Rees', 'title': 'Sayings of the Century', 'price': 8.95}, {'category': 'fiction', 'author': 'Evelyn Waugh', 'title': 'Sword of Honour', 'price': 12.99}, {'category': 'fiction', 'author': 'Herman Melville', 'title': 'Moby Dick', 'isbn': '0-553-21311-3', 'price': 8.99}, {'category': 'fiction', 'author': 'J. R. R. Tolkien', 'title': 'The Lord of the Rings', 'isbn': '0-395-19395-8', 'price': 22.99}], {'author': 'Jack', 'color': 'red', 'price': 19.95}, {'category': 'reference', 'author': 'Nigel Rees', 'title': 'Sayings of the Century', 'price': 8.95}, {'category': 'fiction', 'author': 'Evelyn Waugh', 'title': 'Sword of Honour', 'price': 12.99}, {'category': 'fiction', 'author': 'Herman Melville', 'title': 'Moby Dick', 'isbn': '0-553-21311-3', 'price': 8.99}, {'category': 'fiction', 'author': 'J. R. R. Tolkien', 'title': 'The Lord of the Rings', 'isbn': '0-395-19395-8', 'price': 22.99}, 'reference', 'Nigel Rees', 'Sayings of the Century', 8.95, 'fiction', 'Evelyn Waugh', 'Sword of Honour', 12.99, 'fiction', 'Herman Melville', 'Moby Dick', '0-553-21311-3', 8.99, 'fiction', 'J. R. R. Tolkien', 'The Lord of the Rings', '0-395-19395-8', 22.99, 'Jack', 'red', 19.95]
print(result)
