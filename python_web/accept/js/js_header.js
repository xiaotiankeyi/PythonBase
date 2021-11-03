// jQuery
$(document).ready(function () {
    $(".search-icon").bind({
        // bind() 方法为被选元素添加一个或多个事件处理程序，并规定事件发生时运行的函数。
        mouseover: function () {
            // 当鼠标指针位于元素上方时时，改变元素的背景色
            $(this).css("filter", "drop-shadow(0 0 0 red)");
        },
        mouseout: function () {
            // 当鼠标从元素上移开时，改变元素的背景色
            $(this).css("filter", "drop-shadow(0 0 0)");
        }
    });

    $("div .action-nav").bind({
        // bind() 方法为被选元素添加一个或多个事件处理程序，并规定事件发生时运行的函数。
        mouseover: function () {
            // 当鼠标指针位于元素上方时时，改变元素的背景色
            $(this).css("filter", "brightness(120%)");
        },
        mouseout: function () {
            // 当鼠标从元素上移开时，改变元素的背景色
            $(this).css("filter", "brightness(100%)");
        }
    });
})

// js
function show(thi) {
    // 显示
    if(thi.className == 'login-btn right'){
            var a = document.getElementsByClassName('login-page')[0]
            a.style.display = "block"

            var b = document.getElementsByClassName('background-div')[0]
            b.style.display = "block"
            // console.log(thi.className)
    }else {
            var a = document.getElementsByClassName('registered')[0]
            a.style.display = "block"

            var b = document.getElementsByClassName('background-div')[0]
            b.style.display = "block"
            // console.log(thi.className)
    }
}

function hide(thi) {
    // 隐藏
    if(thi.className == 'call-tag'){
        var a = document.getElementsByClassName('login-page')[0]
        a.style.display = "none"

        var b = document.getElementsByClassName('background-div')[0]
        b.style.display = "none"
        // console.log(thi.className)
    }else {
        var a = document.getElementsByClassName('registered')[0]
        a.style.display = "none"

        var b = document.getElementsByClassName('background-div')[0]
        b.style.display = "none"
        // console.log(thi.className)
    }

}

// function center(obj, width, height) {
//     // 实现居中
//     var screenWidth = $(window).width()      //当前浏览器窗口的 宽高
//     console.log(screenWidth)
//
//     var scrollheight = $(window).height(); //获取浏览器窗口 高度
//     console.log(scrollheight)
//
//     var objLeft = (screenWidth - width) / 2;
//     // console.log(objLeft)
//
//     var objTop = (scrollheight - height) / 2;
//     // console.log(objTop)
//
//     obj.style.left = objLeft + 'px'
//     obj.style.top = objTop + 'px'
//     obj.style.display = "block"
// }
//
// $(window).resize(function () {
//     // 浏览器窗口大小改变时就改变
//     var obj = document.getElementsByClassName('login-page')[0]
//     var w = $(".login-page").width();
//
//     var screenWidth = $(window).width(), screenHeight = $(window).height(); //当前浏览器窗口的 宽高
//     var objLeft = (screenWidth - w) / 2;
//     obj.style.left = objLeft + 'px'
// });