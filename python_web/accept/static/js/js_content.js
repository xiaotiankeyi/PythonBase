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
    // 显示登录界面
    if (thi.className == 'login-btn right') {
        var a = document.getElementsByClassName('login-page')[0]
        a.style.display = "block"

        var b = document.getElementsByClassName('background-div')[0]
        b.style.display = "block"

    } else {
        var a = document.getElementsByClassName('registered')[0]
        a.style.display = "block"

        var b = document.getElementsByClassName('background-div')[0]
        b.style.display = "block"
    }
}

function hide(thi) {
    // 隐藏登录界面
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
    phone_login()
}


function show_phone(thi) {
    // 通过判断none值来控制显示和隐藏区位下拉列表
    var c = document.getElementsByClassName("select-ul")[0]
    // console.log('点了', c)

    if (c.style.display == 'none') {
        c.style.display = "block"
    } else {
        c.style.display = "none"
    }
    // console.log(c.style.display)
}


$(document).mouseup(function (e) {
    // 现实点击空白区域下拉列表弹窗消失
    var _con = $('.select-con');   // 设置目标区域

    if (!_con.is(e.target) && _con.has(e.target).length === 0) { // Mark 1
        var a = document.getElementsByClassName('select-ul')[0]
        // console.log('空白点击')
        a.style.display = "none"
    }
});

// 点击手机号登录
function phone_login(thi) {

    var a = document.getElementsByClassName('phone-item')[0]
    a.style.display = "block"

    var font = document.getElementsByClassName('phone-login')[0]
    font.style.color = "#f8aa00"


    var u = document.getElementsByClassName('username-item')[0]
    u.style.display = "none"

    var user = document.getElementsByClassName('username-login')[0]
    // user.style.removeProperty('color')
    user.style.setProperty('color', '#444')
    // $(".user-name").text(" ")
    document.getElementsByClassName("user-name")[0].value=""

}


// 点击用户名登录
function user_login(thi) {
    var a = document.getElementsByClassName('phone-item')[0]
    a.style.display = "none"
    document.getElementsByClassName("login-phone")[0].value=""

    // $(".login-phone").text(" ")

    var phone = document.getElementsByClassName('phone-login')[0]
    // phone.style.removeProperty('color')
    phone.style.setProperty('color', '#444')

    var u = document.getElementsByClassName('username-item')[0]
    u.style.display = "block"
    thi.style.color = "#f8aa00"
}

// 现实点击图标开显示或隐藏密码
function pwd_display_show(thi) {
    // console.log('显示')

    var pwd_show = $(".show-tag")
    // console.log(pwd_show.attr('alt'))

    if (pwd_show.attr("alt") === '显示') {
        var hide = document.getElementsByClassName('hide-tag')[0]
        // console.log(hide)
        hide.style.display = 'inline'

        // pwd_show.style.display = 'none'
        pwd_show.css('display', 'none')
        pwd_style = $('.pwd');
        pwd_style.prop('type', 'text')
    }
}

function pwd_display_hide(thi) {
    // console.log('隐藏')
    // console.log(thi.alt)
    if (thi.alt === '隐藏') {
        var hide = document.getElementsByClassName('show-tag')[0]
        // console.log(hide);
        hide.style.display = 'inline';

        thi.style.display = 'none';
        pwd_style = $('.pwd');
        pwd_style.prop('type', 'password');
    }
}


$(document).ready(function () {
    // 实现用户登录信息验证

    // $(".login-phone").blur(function () {
    //     // 手机号码输入框失焦后验证
    //
    //     validation_telephone(this.value)
    // });

    function validation_telephone(value) {
        // 手机号码验证功能
        console.log(value)
        var re_phone = /^1[3456789]\d{9}$/
        if (value === "" || value === undefined) {
            var error_tag1 = $(".error-tips")
            error_tag1.text("手机号码不能为空")
            error_tag1.show()
            tips_hide()
            return false
        }

        if (re_phone.test(value) === false) {
            var error_tag2 = $(".error-tips")
            error_tag2.text("手机号码格式不正确")
            error_tag2.show()
            tips_hide()
            return false
        }
        return true
    };

    // $(".user-name").blur(function () {
    //     // 用户名输入框失焦验证
    //     validation_username(this.value)
    // });

    function validation_username(value) {
        // 用户名验证功能
        console.log(value)
        if (value === "" || value === null) {
            var error_tag3 = $(".error-tips")
            error_tag3.text("用户名不能为空")
            error_tag3.show()
            tips_hide()
            return false
        }
        return true
    }

    // $(".pwd-info").blur(function () {
    //     // 密码输入框失焦验证
    //     validation_password(this.value)
    // });

    function validation_password(value) {
        // 密码验证功能
        console.log(value)
        if (value === "" || value === null) {
            var error_tag4 = $(".error-tips")
            error_tag4.text("密码不能为空")
            error_tag4.show()
            tips_hide()
            return false
        }
        return true
    };

    function tips_hide() {
        // 自动隐藏错误提示信息
        setTimeout(function () {
            var error_tag5 = $(".error-tips");
            error_tag5.hide()
        }, 1000)
    };

    $(".click-login").click(function () {
        // 点击登录后进行用户输入信息验证
        var phone_elememnt_status = $(".phone-item").is(":hidden")

        var name_element_status = $(".username-item").is(":hidden")


        if (phone_elememnt_status == false) {
            var login_phone_thi = $(".login-phone")
            console.log(login_phone_thi)
            if (validation_telephone(login_phone_thi.val())) {

                // 密码验证
                var login_pwd_thi = $(".pwd-info")
                console.log(login_pwd_thi)
                if (validation_password(login_pwd_thi.val())) {
                    send_ajax(login_phone_thi.val(), login_pwd_thi.val())
                }
            }
        } else {
            var login_name_thi = $(".user-name")
            console.log(login_name_thi)
            if (validation_username(login_name_thi.val())) {

                // 密码验证
                var login_pwd_thi = $(".pwd-info")
                console.log(login_pwd_thi)
                if (validation_password(login_pwd_thi.val())) {
                    send_ajax(login_name_thi.val(), login_pwd_thi.val())
                }
            }
        }

    });

    function send_ajax(send_name_value, send_pwd_value) {
        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function () {
            if (xhttp.readyState == 4 && xhttp.status == 200) {
                alert(xhttp.responseText)
            }
        };

        xhttp.onerror = function () {
            // console.log()
        };

        var pwd = $(".pwd").val()

        var parameter = {"name": send_name_value, "pwd": send_pwd_value}
        parameter = JSON.stringify(parameter)
        console.log(parameter)

        xhttp.open('POST', '/string/', true)
        xhttp.setRequestHeader('Content-Type', 'application/json')
        // xhttp.open("GET", "/string/", true);
        xhttp.send(parameter);
    };
})
