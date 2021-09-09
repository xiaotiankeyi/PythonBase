var option = document.getElementsByName("option");

function options(thi) {
	// 实现全选操作
	var fang = thi.checked;

	for (var i in option) {
		option[i].checked = fang;
	}
}

function one_option() {
	var fang = true;
	for (var i = 1; i < option.length - 1; i++) {
		if (!option[i].checked) {
			fang = false;
			break;
		}
	}
	option[0].checked = fang;
	option[option.length - 1].checked = fang;
}
