// 引入CryptoJS库，实际使用时需要通过script标签引入
// <script src="https://cdnjs.cloudflare.com/ajax/libs/crypto-js/4.1.1/crypto-js.min.js"></script>
const CryptoJS = require('crypto-js')

/**
 * DES加密方法
 * @param {string} key 加密密钥，必须是8字节
 * @param {string} data 待加密的数据
 * @returns {string} 加密后的Base64字符串
 */
function desEncrypt(key, data) {
    try {
        // 验证密钥长度
        if (key.length !== 8) {
            throw new Error("DES密钥必须是8字节长度");
        }

        // 将密钥转换为WordArray
        const keyHex = CryptoJS.enc.Utf8.parse(key);

        // 加密，使用ECB模式和Pkcs7填充
        const encrypted = CryptoJS.DES.encrypt(data, keyHex, {
            mode: CryptoJS.mode.ECB,
            padding: CryptoJS.pad.Pkcs7
        });

        // 返回Base64格式的加密结果
        return encrypted.toString();
    } catch (e) {
        return `加密失败: ${e.message}`;
    }
}

/**
 * DES解密方法
 * @param {string} key 解密密钥，必须是8字节
 * @param {string} encryptedData 待解密的Base64字符串
 * @returns {string} 解密后的原始数据
 */
function desDecrypt(key, encryptedData) {
    try {
        // 验证密钥长度
        if (key.length !== 8) {
            throw new Error("DES密钥必须是8字节长度");
        }

        // 将密钥转换为WordArray
        const keyHex = CryptoJS.enc.Utf8.parse(key);

        // 解密
        const decrypted = CryptoJS.DES.decrypt(encryptedData, keyHex, {
            mode: CryptoJS.mode.ECB,
            padding: CryptoJS.pad.Pkcs7
        });

        // 将解密结果转换为UTF-8字符串
        return decrypted.toString(CryptoJS.enc.Utf8);
    } catch (e) {
        return `解密失败: ${e.message}`;
    }
}

/**
 * 主函数，演示DES加密解密流程
 */
function main() {
    // 密钥必须是8字节
    const key = "12345678";

    // 原始数据
    const originalData = "这是一个DES加密解密的测试案例";
    console.log(`原始数据: ${originalData}`);

    // 加密
    const encrypted = desEncrypt(key, originalData);
    console.log(`加密后: ${encrypted}`);

    // 解密
    const decrypted = desDecrypt(key, encrypted);
    console.log(`解密后: ${decrypted}`);
}

// 执行主函数
main();
