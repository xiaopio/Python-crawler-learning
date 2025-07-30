s = '123456'

s_64 = btoa(s)
// MTIzNDU2
console.log(s_64);

s_64_decode = atob(s_64)
// 123456
console.log(s_64_decode);