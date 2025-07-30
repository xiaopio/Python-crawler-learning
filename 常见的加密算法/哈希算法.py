from hashlib import md5, sha1, sha256, sha512

# obj = md5()
# obj = sha1()
# obj = sha256()
obj = sha512()

text = '123456'.encode('utf-8')

obj.update(text)

encrypt_text = obj.hexdigest()  # 转换为16进制的数据
print(encrypt_text, len(encrypt_text))
# md5
# e10adc3949ba59abbe56e057f20f883e 32
# sha1
# 7c4a8d09ca3762af61e59520943dc26494f8941b 40
# sha256
# 8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92 64
# sha512
# ba3253876aed6bc22d4a6ff53d8406c6ad864195ed144ab5c87621b6c233b548baeae6956df346ec8c17f5ea10f35ee3cbc514797ed7ddd3145464e2a0bab413 128
