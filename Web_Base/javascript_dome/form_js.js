function verify() {
	// 生成验证码
	// 随机获取3位数字
	var num = Math.floor(Math.random() * 900 + 100);
	// console.log(num);

	// 随机获取2个字母
	var str = "";
	for (var i = 0; i < 3; i++) {
		str += String.fromCharCode(Math.floor(Math.random() * 26) + "a".charCodeAt(0));
	}
	// console.log(str)

	var ver_span = document.getElementById("verify_span")
	// console.log(ver_span)

	var code = str + num
	ver_span.innerText = code
	// ver_span.style.fontSize = "10px"

}

function verify_info(element, span_element, re) {
	// form表单验证,提取公共部分
	var element_value = document.getElementById(element);

	var span = document.getElementsByClassName(span_element)[0]
	// console.log(span)

	if (element_value.value == null || element_value.value == "") {
		span.innerHTML = element_value.alt + "不能为空"
		span.style.color = "red"
		return false
	} else if (re.test(element_value.value)) {
		span.innerHTML = element_value.alt + "符合要求"
		span.style.color = "green"
		return true
	} else {
		span.innerHTML = element_value.alt + "不符合要求"
		span.style.color = "red"
		return false
	}
}

function username_verify() {
	// 用户名验证
	var re = /^[\u4e00-\u9fa5]{3,}$/
	return verify_info("username", "username_span", re)
}

function password_verify() {
	// 密码验证
	var re = /^[A-Za-z0-9]{6,12}$/
	return verify_info("password", "password_span", re)
}

function telphone_verify() {
	// 电话号码验证
	var re = /^(13[0-9]|14[5|7]|15[0|1|2|3|5|6|7|8|9]|18[0|1|2|3|5|6|7|8|9])\d{8}$/
	return verify_info("telphone", "telphone_span", re)
}

function email_verify() {
	// 邮箱验证
	var re = /^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$/
	return verify_info("email", "email_span", re)
}

function verify_code() {
	// 验证码验证
	var span = document.getElementById("verify_span")
	// 获取验证码
	// console.log(span.textContent)

	var verify_value = document.getElementById("verify").value
	// 获取输入的验证码
	// console.log(verify_value)

	if (span.textContent != verify_value || verify_value == "" || verify_value == null) {
		span.innerHTML = "验证码效验失败"
		span.style.color = "red"
		span.removeAttribute("id")
		return false
	} else {
		span.innerHTML = "验证码效验成功"
		span.style.color = "green"
		// span.removeAttribute("id")
		span.setAttribute("id", "")
		return true
	}
}

function verify_deal() {
	// 判断是否勾选了协议
	var deal_element = document.getElementById("deal")

	var register_element = document.getElementById("register")
	// 取反
	register_element.disabled = !deal_element.checked
}

function verify_address() {
	提交最后验证
	var option = document.getElementById("options").value
	console.log(option)
	if (option == 0) {
		var addre_span = document.getElementsByClassName("address_span")[0]
		addre_span.innerText = "请选择籍贯";
		addre_span.style.color = "red";
		return false
	} else {
		return true
	}
}


function commit() {

	// onsubmit控制在信息不全的前提下不准提交,效验顺序要注意
	var result = username_verify() && password_verify() && telphone_verify() && email_verify() &&
		verify_code()

	return result;
}
