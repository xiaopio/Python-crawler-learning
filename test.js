function get_sign() {
    return 'hello JS'
}

cookieTemp = '';
Object.defineProperty(document, 'cookie', {
    set: function (val) {
        if (val.indexOf('__dfp') != -1) {
            debugger;
        }
        console.log('Hook捕获到cookie设置->', val);
        cookieTemp = val;
        return val;
    },
    get: function () {
        return cookieTemp;
    }
})