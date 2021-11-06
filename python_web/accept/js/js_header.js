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

    // 实现电话区位切换
    $(".select-li span").click(function () {
        var s = $(this).parent('li').attr('data-value').split('+')[1]
        // console.log(this.innerText)

        $(".select-value").text(this.innerText)
        $(".select-value").attr('data-value', '+' + s)

    });

})

// js
function show(thi) {
    // 显示
    if (thi.className == 'login-btn right') {
        var a = document.getElementsByClassName('login-page')[0]
        a.style.display = "block"

        var b = document.getElementsByClassName('background-div')[0]
        b.style.display = "block"
        // console.log(thi.className)
    } else {
        var a = document.getElementsByClassName('registered')[0]
        a.style.display = "block"

        var b = document.getElementsByClassName('background-div')[0]
        b.style.display = "block"
        // console.log(thi.className)
    }
}

function hide(thi) {
    // 隐藏
    if (thi.className == 'call-tag') {
        var a = document.getElementsByClassName('login-page')[0]
        a.style.display = "none"

        var b = document.getElementsByClassName('background-div')[0]
        b.style.display = "none"
        // console.log(thi.className)
    } else {
        var a = document.getElementsByClassName('registered')[0]
        a.style.display = "none"

        var b = document.getElementsByClassName('background-div')[0]
        b.style.display = "none"
        // console.log(thi.className)
    }
}


function show_phone(thi) {
    // 通过判断none值来控制显示和隐藏
    var c = document.getElementsByClassName("select-ul")[0]
    console.log('点了', c)

    if (c.style.display == 'none') {
        c.style.display = "block"
    } else {
        c.style.display = "none"
    }
    console.log(c.style.display)
}


$(document).mouseup(function (e) {
    // 现实点击空白区域弹窗消失
    var _con = $('.select-con');   // 设置目标区域

    if (!_con.is(e.target) && _con.has(e.target).length === 0) { // Mark 1
        var a = document.getElementsByClassName('select-ul')[0]
        console.log('空白点击')
        a.style.display = "none"
    }
});

// 点击手机号登录
function phone_login(thi){

    var a = document.getElementsByClassName('phone-item')[0]
    a.style.display = "block"
    thi.style.color = "#f8aa00"


    var u = document.getElementsByClassName('username-item')[0]
    u.style.display = "none"

    var user = document.getElementsByClassName('username-login')[0]
    // user.style.removeProperty('color')
    user.style.setProperty('color', '#444')

}


// 点击用户名登录
function user_login(thi){
    var a = document.getElementsByClassName('phone-item')[0]
    a.style.display = "none"

    var phone = document.getElementsByClassName('phone-login')[0]
    // phone.style.removeProperty('color')
    phone.style.setProperty('color', '#444')

    var u = document.getElementsByClassName('username-item')[0]
    u.style.display = "block"
    thi.style.color = "#f8aa00"
}