# AES、DES、3DES

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

# CBC，iv 偏移量
# ECB, 不需要iv

def aes_encrypt(key, iv, plain_text):
    """
    AES加密
    :param key: 密钥
    :param iv: 偏移量
    :param plain_text: 原始数据
    :return: 经过Base64编码后的密文
    """
    # key 密钥， mod 模式， iv 偏移量
    cipher = AES.new(key=key, mode=AES.MODE_CBC, iv=iv)
    # 进行填充处理，原始数据 key的长度
    plain_text_pad = pad(plain_text, AES.block_size)
    # 加密
    cipher_text = cipher.encrypt(plain_text_pad)
    # b'5"!L\xb1\xdf\xaczY\x10\xab\x94\x8a\xe7\xc6\xb9\xb1\n\xb5lm\xe6\xe1\xd2\x9a\'\x9bN\\y=\xf4'
    # print(cipher_text)

    cipher_text_b64 = base64.b64encode(cipher_text).decode()
    # NSIhTLHfrHpZEKuUiufGubEKtWxt5uHSmiebTlx5PfQ=
    # print(cipher_text_b64)
    return cipher_text_b64


def aes_decrypt(key, iv, cipher_text_b64):
    """
    AES解密数据
    :param key: 密钥
    :param iv: 偏移量
    :param cipher_text_b64: 经过Base64编码后的密文
    :return:
    """
    cipher_text = base64.b64decode(cipher_text_b64)

    cipher = AES.new(key=key, mode=AES.MODE_CBC, iv=iv)

    plain_text_unpad = cipher.decrypt(cipher_text)

    plain_text = unpad(plain_text_unpad, AES.block_size)

    # print(plain_text.decode())
    return plain_text.decode()


if __name__ == '__main__':
    key = b'0123456789abcdef'  # byte
    iv = b'0123456789abcdef'
    # CBC   iv 偏移量
    # ECB
    # 原始数据经过encode变成utf-8二进制字节流
    plain_text = '这是原始数据'.encode()
    cipher_text_b64 = aes_encrypt(key, iv, plain_text)
    print(cipher_text_b64)
    text = aes_decrypt(key, iv, cipher_text_b64)
    print(text)
