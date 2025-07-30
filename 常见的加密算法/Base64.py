# 字符串编码和解码
import base64

s = '中文'.encode('utf-8')
s1 = '中文'.encode('gbk')
s2 = 'abc'.encode('utf-8')
# b'\xe4\xb8\xad\xe6\x96\x87'
print(s)
# b'\xd6\xd0\xce\xc4'
print(s1)
# b'abc'
print(s2)

s_64 = base64.b64encode(s)

# b'5Lit5paH'
print(s, s_64)

s_64_decode = base64.b64decode(s_64)
# b'\xe4\xb8\xad\xe6\x96\x87'
print(s_64_decode)
# 中文
print(s_64_decode.decode())
