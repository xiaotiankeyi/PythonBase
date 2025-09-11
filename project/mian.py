def generate_composite_numbers():
    """生成01合至13合各组合数包含的数字"""
    composite_numbers = {}
    for i in range(1, 14):
        start = i
        numbers = []
        current = start
        while len(numbers) < 5 and current <= 49:
            numbers.append(f"{current:02d}")
            current += 9
        composite_numbers[f"{i:02d}"] = numbers
    return composite_numbers

def combine_numbers(head, tail):
    """将头数和尾数组合,过滤掉"00" """
    result = []
    for h in head:
        for t in tail:
            combined = f"{h}{t}"
            if combined != "00":
                result.append(combined)
    return result

def get_head_check_numbers(head_digit, is_single):
    """获取指定头数的单/双数集合(头数0-4,对应00-09至40-49)"""
    numbers = []
    start = head_digit * 10
    end = (head_digit + 1) * 10
    
    for num in range(start, end):
        num_str = f"{num:02d}"
        last_digit = int(num_str[-1])
        if (last_digit % 2 == 1 and is_single) or (last_digit % 2 == 0 and not is_single):
            numbers.append(num_str)
    return numbers

def input_with_range(prompt, valid_range, input_type="digit"):
    """带范围校验的输入函数"""
    while True:
        user_input = input(prompt).strip()
        if not user_input:
            print(f"{input_type}不能为空,请重新输入")
            continue
        invalid_chars = [c for c in user_input if c not in valid_range]
        if invalid_chars:
            print(f"输入包含无效{input_type}:{','.join(invalid_chars)},仅支持{','.join(valid_range)}")
            continue
        unique_input = list(set(user_input))
        unique_input_sorted = sorted(unique_input, key=lambda x: user_input.index(x))
        return unique_input_sorted

# 生肖与对应数字的字典(修正后)
shengxiao_dict = {
    "鼠": ["06", "18", "30", "42"],
    "牛": ["05", "17", "29", "41"],
    "虎": ["04", "16", "28", "40"],
    "兔": ["03", "15", "27", "39"],
    "龙": ["02", "14", "26", "38"],
    "蛇": ["01", "13", "25", "37", "49"],  # 蛇对应5个数字
    "马": ["12", "24", "36", "48"],
    "羊": ["11", "23", "35", "47"],
    "猴": ["10", "22", "34", "46"],
    "鸡": ["09", "21", "33", "45"],
    "狗": ["08", "20", "32", "44"],
    "猪": ["07", "19", "31", "43"]
}

def main():
    composites = generate_composite_numbers()
    HEAD_VALID_RANGE = {'0', '1', '2', '3', '4'}
    TAIL_VALID_RANGE = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
    
    # 步骤1:获取头数和尾数
    head = input_with_range(
        prompt="请输入头数(仅支持0-4的数字,可输入多个,如012):",
        valid_range=HEAD_VALID_RANGE,
        input_type="头数"
    )
    print(f"已确认有效头数:{','.join(head)}")
    
    tail = input_with_range(
        prompt="请输入尾数(仅支持0-9的数字,可输入多个,如485):",
        valid_range=TAIL_VALID_RANGE,
        input_type="尾数"
    )
    print(f"已确认有效尾数:{','.join(tail)}")
    
    # 步骤2:生成初始组合
    val = combine_numbers(head, tail)
    print(f"\n头数和尾数的组合结果:{', '.join(val) if val else '无'}")
    if not val:
        print("提示:所有组合均为'00',已全部过滤,程序结束")
        return
    
    # 步骤3:合数剔除(保持原逻辑)
    composite_excluded = []
    while True:
        composite_input = input("\n请输入需要剔除的合数(如02表示02合,输入空格或N结束):").strip()
        if composite_input in ['', 'N', 'n']:
            break
        if composite_input not in composites:
            print(f"无效的合数编号,仅支持01-13之间的编号")
            continue
        
        composite_group = composites[composite_input]
        to_exclude = [num for num in composite_group if num in val]
        if to_exclude:
            composite_excluded.extend(to_exclude)
            val = [num for num in val if num not in to_exclude]
            print(f"已剔除{composite_input}合的数字:{', '.join(to_exclude)}")
        else:
            print(f"{composite_input}合中无匹配当前组合的数字,无需剔除")
    composite_excluded = list(set(composite_excluded))
    
    # 步骤4:头数单双剔除(优化交互)
    head_check_excluded = []
    head_check_continue = input("\n是否需要进行头数单双剔除?(Y/N):").strip().upper()
    if head_check_continue == 'Y':
        print("请输入需要剔除的头数单双(格式:X-Y,输入N结束,如1-0):")
        while True:
            head_input = input("> ").strip()
            if head_input.upper() == 'N':
                break  # 输入N直接退出当前环节
            
            # 校验输入格式
            if len(head_input) != 3 or head_input[1] != '-':
                print("格式错误!请按'X-Y'输入(如1-0表示1头双)")
                continue
            try:
                head_digit = int(head_input[0])
                is_single = int(head_input[2]) == 1
            except ValueError:
                print("头数和单双标识必须是数字(X=0-4,Y=0/1)")
                continue
            if head_digit < 0 or head_digit > 4:
                print(f"头数{head_digit}超出范围,仅支持0-4")
                continue
            if head_input[2] not in ['0', '1']:
                print("单双标识错误!Y必须是0(双)或1(单)")
                continue
            
            # 执行剔除
            target_numbers = get_head_check_numbers(head_digit, is_single)
            to_exclude = [num for num in target_numbers if num in val]
            type_str = "单" if is_single else "双"
            if to_exclude:
                head_check_excluded.extend(to_exclude)
                val = [num for num in val if num not in to_exclude]
                print(f"已剔除{head_digit}头{type_str}的数字:{', '.join(to_exclude)}")
            else:
                print(f"{head_digit}头{type_str}中无匹配当前组合的数字,无需剔除")
    head_check_excluded = list(set(head_check_excluded))
    
    # 步骤5:生肖过滤(优化交互)
    shengxiao_excluded = []
    shengxiao_continue = input("\n是否需要进行生肖过滤?(Y/N):").strip().upper()
    if shengxiao_continue == 'Y':
        print("请输入需要剔除的生肖(输入N结束,如猴):")
        while True:
            shengxiao_input = input("> ").strip()
            if shengxiao_input.upper() == 'N':
                break  # 输入N直接退出当前环节
            
            if shengxiao_input not in shengxiao_dict:
                print("无效的生肖,仅支持十二生肖:鼠、牛、虎、兔、龙、蛇、马、羊、猴、鸡、狗、猪")
                continue
            
            target_numbers = shengxiao_dict[shengxiao_input]
            to_exclude = [num for num in target_numbers if num in val]
            if to_exclude:
                shengxiao_excluded.extend(to_exclude)
                val = [num for num in val if num not in to_exclude]
                print(f"已剔除{shengxiao_input}对应的数字:{', '.join(to_exclude)}")
            else:
                print(f"{shengxiao_input}中无匹配当前组合的数字,无需剔除")
    shengxiao_excluded = list(set(shengxiao_excluded))
    
    # 最终结果
    print("\n===== 最终处理结果 =====")
    print(f"1. 合数剔除的数字:{', '.join(composite_excluded) if composite_excluded else '无'}")
    print(f"2. 头数单双剔除的数字:{', '.join(head_check_excluded) if head_check_excluded else '无'}")
    print(f"3. 生肖过滤剔除的数字:{', '.join(shengxiao_excluded) if shengxiao_excluded else '无'}")
    print(f"4. 最终保留的数字:{', '.join(val) if val else '无'}")

if __name__ == "__main__":
    main()
    