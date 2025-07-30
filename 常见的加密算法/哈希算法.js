const CryptoJS = require('crypto-js')

s = '123456'

encrypt_s = CryptoJS.MD5(s).toString()
// encrypt_s = CryptoJS.SHA1(s).toString()

console.log(encrypt_s)