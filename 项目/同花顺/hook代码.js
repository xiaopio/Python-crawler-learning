// hook cookie
(function () {
    'use strict'
    Object.defineProperty(document, 'cookie', {
        get: function () {
            return "";
        },
        set: function (value) {
            debugger;
            return value;
        },
    });
})()