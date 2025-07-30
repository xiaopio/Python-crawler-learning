// 无限debugger
AAA = Function.prototype.constructor;
Function.prototype.constructor = function (a) {
    if (a == "debugger") {
        return function () {
        };
    }
    return AAA(a);
}

(function () {
    'use strict';
    var cookieTemp = '';
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
        },
    });
})();


// 编程猫
//当前版本hook工具只支持Content-Type为html的自动hook
//下面是一个示例:这个示例演示了hook全局的cookie设置点
(function () {
    //严谨模式 检查所有错误
    'use strict';
    //document 为要hook的对象   这里是hook的cookie
    var cookieTemp = "";
    Object.defineProperty(document, 'cookie', {
        //hook set方法也就是赋值的方法
        set: function (val) {
            //这样就可以快速给下面这个代码行下断点
            //从而快速定位设置cookie的代码
            console.log('Hook捕获到cookie设置->', val);
            cookieTemp = val;
            return val;
        },
        //hook get方法也就是取值的方法
        get: function () {
            return cookieTemp;
        }
    });
})();


// HOOK JSON.parse

(function () {
    var parse = JSON.parse;
    JSON.parse = function (params) {
        console.log("HOOK JSON.parse --> ", params);
        debugger;
        return parse(params)
    }
})();


// Hook JSON.stringify

(function () {
    var stringify = JSON.stringify;
    JSON.stringify = function (params) {
        console.log("HOOK JSON.stringify --> ", params);
        debugger;
        return stringify(params)
    }
})();


// HOOK eval

(function () {
    // 保留原始方法
    window.__cr_eval = window.eval;
    // 重写eval
    var myeval = function (src) {
        console.log(src);
        console.log("==============eval end==============");
        debugger;
        return window.__cr_eval(src)
    }
    // 屏蔽JS中对原生函数native属性的检测
    var _myeval = myeval.bind(null);
    _myeval.toString = window.__cr_eval.toString;
    Object.defineProperty(window, 'eval', {
        value: _myeval
    });
})();