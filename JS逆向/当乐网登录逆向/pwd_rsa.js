const {setMaxDigits} = require('./BigInt')
const {RSAKeyPair, encryptedString} = require('./RSA.js')

var rsa = function (arg) {
    setMaxDigits(130);
    var PublicExponent = "10001";
    var modulus = "be44aec4d73408f6b60e6fe9e3dc55d0e1dc53a1e171e071b547e2e8e0b7da01c56e8c9bcf0521568eb111adccef4e40124b76e33e7ad75607c227af8f8e0b759c30ef283be8ab17a84b19a051df5f94c07e6e7be5f77866376322aac944f45f3ab532bb6efc70c1efa524d821d16cafb580c5a901f0defddea3692a4e68e6cd";
    var key = new RSAKeyPair(PublicExponent, "", modulus);
    return encryptedString(key, arg);
};

pwd = '123456'
pwd = rsa(pwd)
console.log(rsa(pwd));

submitData = {
    "name": "18857587458",
    "pwd": "b2927281520eba726728c6f5e9579228a3102f1462c52d708ba8ee622b2124a97545d0e3a6d0315bd84e457e7550ab2357e3c019fe23bf4a57ab2ead172d2e9ce8ae1e167d54a4530a200ba9be5b2fbe08b7cbfe07f914c3c09ccfa37488cc531f9452f625e0195ab41ec88546378ae304f5f774aa2de8891446ff77aae799d8",
    "to": "https%3A%2F%2Fwww.d.cn%2F",
    "reqId": "pd4kwwcw8r98k0ldxb9mgr1ruapddxmq",
    "geetest_challenge": "74585f4382825987a2f00f5ab0a4c220",
    "geetest_validate": "e82cc5d4b2f41214b013f3f6432ca006",
    "geetest_seccode": "e82cc5d4b2f41214b013f3f6432ca006|jordan"
}