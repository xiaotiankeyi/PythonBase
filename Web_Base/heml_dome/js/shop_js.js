var option = document.getElementsByName("option");

function options(thi) {
	// 实现全选操作
	var fang = thi.checked;

	for (var i in option) {
		option[i].checked = fang;
	}
	if (thi.checked) {
		// 计算已经选择了多少商品数
		var goods_number = document.getElementsByClassName("fine");
		// console.log(goods_number)
		var number = 0;
		for (var j = 0; j < goods_number.length; j++) {
			// console.log(goods_number[j].value)
			num = goods_number[j].value;
			number += Number(num);
		}
		// console.log(number);
		document.getElementById("digital").innerText = number;

		// 总计出结算价格
		var all_price = document.getElementsByName("price");
		// console.log(all_price)
		var count = 0;
		for (var i = 0; i < all_price.length; i++) {
			// console.log(all_price[i].innerHTML.substr(1))
			price = all_price[i].innerHTML.substr(1)
			count += Number(price)
		}
		// console.log(count)
		document.getElementById("total").innerHTML = "¥" + count

	} else {
		document.getElementById("digital").innerText = 0;
		document.getElementById("total").innerHTML = "¥" + 0;
	}

}

function one_option(thi) {
	// 定位数量
	var goods_number = thi.parentNode.parentNode.children[5];

	// 定位总数量
	var count_num = document.getElementById("digital");

	// 定位总价格
	var count_price = document.getElementById("total")

	// 定位商品价格
	var all_price = thi.parentNode.parentNode.children[6].innerHTML.substr(1);

	var uu = 0;
	if (thi.checked) {
		// 计算已经选择了多少商品数
		// console.log(goods_number.children[1].value)
		// 赋值商品总数
		count_num.innerHTML = Number(count_num.innerHTML) + Number(goods_number.children[1].value)


		// 总计出总价格
		// console.log(all_price)
		var new_digital = count_price.innerHTML.substr(1)

		// console.log(count_price.innerHTML.substr(1))
		// console.log(Number(new_digital) + Number(all_price)

		var d = Number(new_digital) + Number(all_price)
		count_price.innerHTML = "¥" + d
		uu++;
	} else {
		// 减少总数量

		count_num.innerHTML = Number(count_num.innerHTML) - Number(goods_number.children[1].value)
		// 减少总价格
		var new_digital = count_price.innerHTML.substr(1)
		var d = Number(new_digital) - Number(all_price)
		count_price.innerHTML = "¥" + d
	}

	// 实现单选决定全选
	var fang = true;
	for (var i = 1; i < option.length - 1; i++) {
		if (!option[i].checked) {
			fang = false;
			break;
		}
	}
	// 勾选第一个全选
	option[0].checked = fang;
	// 勾选第二个全选
	option[option.length - 1].checked = fang;
}


function modify_number(thi, digital) {
	// 实现数量的加一减一

	// 实现加减数量来控制价格
	var gg = thi.parentNode.parentNode.children[0].firstChild;
	console.log(gg.checked);
	if (gg.checked) {
		// 如果勾选
		if (digital == "1") {
			var element = thi.nextElementSibling;
			if (Number(element.value) > 0) {
				element.value = Number(element.value) - 1;

				// 总数变化
				var tt = document.getElementById("digital")
				tt.innerHTML = Number(tt.innerHTML) - 1

				// 实现总价格变化
				var price = element.parentNode.previousElementSibling.innerHTML;
				// // console.log(price)
				var count_price = Number(price) * Number(element.value);
				element.parentNode.nextElementSibling.innerText = "¥" + count_price;

				// // 结算总价格变化
				var oo = document.getElementById("total");
				var yy = Number(oo.innerHTML.substr(1)) - Number(price);
				oo.innerHTML = "￥" + yy;
				return true
			}
		} else {
			var element = thi.previousElementSibling;
			var val = Number(element.value) + 1;
			element.value = val;
			// 总数变化
			var tt = document.getElementById("digital")
			tt.innerHTML = Number(tt.innerHTML) + 1

			// 实现总价格变化
			var price = element.parentNode.previousElementSibling.innerHTML;
			// console.log(price)
			var count_price = Number(price) * Number(element.value);

			element.parentNode.nextElementSibling.innerText = "¥" + count_price;

			var oo = document.getElementById("total");
			// console.log(oo.innerHTML.substr(1))

			// 结算总价格变化
			var ee = Number(oo.innerHTML.substr(1)) + Number(price);
			oo.innerHTML = "￥" + ee
			return true
		}

	}

	if (digital == "1") {
		var element = thi.nextElementSibling;
		if (Number(element.value) > 0) {
			element.value = Number(element.value) - 1;

		}
	} else {
		var element = thi.previousElementSibling;
		var val = Number(element.value) + 1;
		element.value = val;
	}
	// 实现总价格变化
	var price = element.parentNode.previousElementSibling.innerHTML;
	// console.log(price)
	var count_price = Number(price) * Number(element.value);

	element.parentNode.nextElementSibling.innerText = "¥" + count_price;
	return true
}

function delete_node(thi) {
	// 实现删除
	var parent = thi.parentNode.parentNode.parentNode;
	// console.log(parent);
	parent.remove();
}
