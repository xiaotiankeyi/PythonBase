$(document).ready(function (){
    $(".search-icon").bind({
            // bind() 方法为被选元素添加一个或多个事件处理程序，并规定事件发生时运行的函数。
            mouseover: function() {
                // 当鼠标指针位于元素上方时时，改变元素的背景色
                $(this).css("filter", "drop-shadow(0 0 0 red)");
            },
            mouseout: function() {
                // 当鼠标从元素上移开时，改变元素的背景色
                $(this).css("filter", "drop-shadow(0 0 0)");
            }
        });

    $("div .action-nav").bind({
        // bind() 方法为被选元素添加一个或多个事件处理程序，并规定事件发生时运行的函数。
        mouseover: function() {
            // 当鼠标指针位于元素上方时时，改变元素的背景色
            $(this).css("filter", "brightness(120%)");
        },
        mouseout: function() {
            // 当鼠标从元素上移开时，改变元素的背景色
            $(this).css("filter", "brightness(100%)");
        }
    });

    // $(".login-btn").click(function (){
    //     console.log('点击了')
    //         $(".login").css("display", "block")
    //         // $("div .login").show()
    //
    // });
    //
    // $(".call-tag").click(function (){
    //         $(".login").css("display", "none");
    //         // $("div .login").hide()
    //
    // });
})

function show(){
    var a = document.getElementsByClassName('login-page')[0]
    console.log(a)
    a.style.display = "block"
}

function hide(){
    var a = document.getElementsByClassName('login-page')[0]
    console.log(a)
    a.style.display = "none"
}