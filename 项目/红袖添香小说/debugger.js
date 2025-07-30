// 方法1：基础版 - 重写debugger语句（适用于直接调用debugger;的场景）
(function() {
    // 保存原始debugger函数
    const originalDebugger = window.debugger;
    // 重写为无操作函数
    window.debugger = function() {
        console.log("已拦截debugger调用");
        // 如需临时允许某次debugger，可取消下一行注释
        // originalDebugger.apply(this, arguments);
    };

    // 拦截eval中的debugger（部分网站会动态生成代码）
    const originalEval = window.eval;
    window.eval = function(code) {
        // 替换代码中的debugger为注释
        const modifiedCode = code.replace(/debugger;/g, '// debugger;');
        return originalEval.call(this, modifiedCode);
    };
})();

// 方法2：进阶版 - 检测并跳过无限debugger循环（适用于循环调用的场景）
(function() {
    let debuggerCount = 0;
    const maxAllowed = 3; // 允许前3次debugger，之后拦截

    // 重写debugger
    const originalDebugger = window.debugger;
    window.debugger = function() {
        debuggerCount++;
        if (debuggerCount > maxAllowed) {
            console.log(`已跳过第${debuggerCount}次debugger`);
            return;
        }
        // 前几次允许执行，避免触发网站反制
        originalDebugger.apply(this, arguments);
    };
})();


// 加混淆的网站
// 补充：替换混淆后的debugger
const replaceObfuscatedDebugger = () => {
    // 匹配常见的混淆写法，如 (()=>{debugger})()
    const scriptTags = document.getElementsByTagName('script');
    for (let tag of scriptTags) {
        if (tag.innerHTML) {
            tag.innerHTML = tag.innerHTML
                .replace(/\(\s*\(\)\s*=>\s*\{\s*debugger\s*\}\s*\)\(\s*\)/g, '// 已移除混淆debugger')
                .replace(/\(\s*function\s*\(\)\s*\{\s*debugger\s*\}\s*\)\(\s*\)/g, '// 已移除混淆debugger');
        }
    }
};

// 在DOM加载完成后执行替换
window.addEventListener('DOMContentLoaded', replaceObfuscatedDebugger);


(function() {
    'use strict';
    const originalFunctionConstructor = unsafeWindow.Function.prototype.constructor;

    unsafeWindow.Function.prototype.constructor = function(...args) {
        let functionContent = args;
        if (typeof functionContent === 'string' && functionContent.includes('debugger')) {
            // Remove all debugger expressions from the function's content
            functionContent = functionContent.replace(/\bdebugger\b/gi, '');
            // Replace the original function content with the modified one
            args = functionContent;
        }
        // Call the original Function constructor with potentially modified arguments
        return originalFunctionConstructor.apply(this, args);
    };

    // Optional: Redefine console.clear to prevent spamming
    if (unsafeWindow.console && unsafeWindow.console.clear) {
        unsafeWindow.console.clear = function() {}; // No-op
    }
})();