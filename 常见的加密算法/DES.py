from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import base64


def des_encrypt(key, data):
    """
    使用DES算法加密数据
    :param key: 加密密钥，必须是8字节
    :param data: 待加密的数据
    :return: 加密后的Base64字符串
    """
    try:
        # 确保密钥是8字节
        if len(key) != 8:
            raise ValueError("DES密钥必须是8字节长度")

        # 创建DES实例，使用ECB模式
        cipher = DES.new(key.encode('utf-8'), DES.MODE_ECB)

        # 对数据进行填充，使其长度为8的倍数
        padded_data = pad(data.encode('utf-8'), DES.block_size)

        # 加密并进行Base64编码
        encrypted_data = cipher.encrypt(padded_data)
        return base64.b64encode(encrypted_data).decode('utf-8')
    except Exception as e:
        return f"加密失败: {str(e)}"


def des_decrypt(key, encrypted_data):
    """
    使用DES算法解密数据
    :param key: 解密密钥，必须是8字节
    :param encrypted_data: 待解密的Base64字符串
    :return: 解密后的原始数据
    """
    try:
        # 确保密钥是8字节
        if len(key) != 8:
            raise ValueError("DES密钥必须是8字节长度")

        # 创建DES实例，使用ECB模式
        cipher = DES.new(key.encode('utf-8'), DES.MODE_ECB)

        # 对Base64编码的数据进行解码
        decoded_data = base64.b64decode(encrypted_data)

        # 解密并去除填充
        decrypted_data = unpad(cipher.decrypt(decoded_data), DES.block_size)
        return decrypted_data.decode('utf-8')
    except Exception as e:
        return f"解密失败: {str(e)}"


if __name__ == "__main__":
    # 密钥必须是8字节
    key = "12345678"

    # 原始数据
    original_data = "这是一个DES加密解密的测试案例"
    print(f"原始数据: {original_data}")

    # 加密
    encrypted = des_encrypt(key, original_data)
    print(f"加密后: {encrypted}")

    # 解密
    decrypted = des_decrypt(key, encrypted)
    print(f"解密后: {decrypted}")
