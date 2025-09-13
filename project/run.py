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

def get_head_check_numbers(head_digit, is_single):
    """获取指定头数的单/双数集合"""
    numbers = []
    start = head_digit * 10
    end = (head_digit + 1) * 10
    
    for num in range(start, end):
        num_str = f"{num:02d}"
        last_digit = int(num_str[-1])
        if (last_digit % 2 == 1 and is_single) or (last_digit % 2 == 0 and not is_single):
            numbers.append(num_str)
    return numbers

# 生肖与对应数字的字典
shengxiao_dict = {
    "鼠": ["06", "18", "30", "42"],
    "牛": ["05", "17", "29", "41"],
    "虎": ["04", "16", "28", "40"],
    "兔": ["03", "15", "27", "39"],
    "龙": ["02", "14", "26", "38"],
    "蛇": ["01", "13", "25", "37", "49"],
    "马": ["12", "24", "36", "48"],
    "羊": ["11", "23", "35", "47"],
    "猴": ["10", "22", "34", "46"],
    "鸡": ["09", "21", "33", "45"],
    "狗": ["08", "20", "32", "44"],
    "猪": ["07", "19", "31", "43"]
}

def get_numbers_from_zodiac(zodiacs):
    """根据输入的生肖列表获取对应的数字集合（去重）"""
    numbers = []
    for zodiac in zodiacs:
        if zodiac in shengxiao_dict:
            numbers.extend(shengxiao_dict[zodiac])
    # 去重并保持顺序
    seen = set()
    unique_numbers = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            unique_numbers.append(num)
    return sorted(unique_numbers)  # 排序后返回

def main():
    composites = generate_composite_numbers()
    
    # 步骤1：输入生肖生成初始数字
    print("请输入生肖（多个生肖用逗号分隔，如：鼠,牛,虎）：")
    while True:
        zodiac_input = input("> ").strip()
        if not zodiac_input:
            print("生肖不能为空，请重新输入")
            continue
            
        zodiac_list = [z.strip() for z in zodiac_input.split(',')]
        invalid = [z for z in zodiac_list if z not in shengxiao_dict]
        
        if invalid:
            print(f"无效生肖：{', '.join(invalid)}，请使用正确的生肖名称（鼠、牛、虎、兔、龙、蛇、马、羊、猴、鸡、狗、猪）")
            continue
            
        # 生成初始数字列表
        val = get_numbers_from_zodiac(zodiac_list)
        print(f"\n生肖对应的初始数字：{', '.join(val)}")
        break
    
    if not val:
        print("没有有效的数字可供处理，程序结束")
        return
    
    # 步骤2：合数剔除
    composite_excluded = []
    print("\n请输入需要剔除的合数（如02表示02合，输入空格或N结束）：")
    while True:
        composite_input = input("> ").strip()
        if composite_input in ['', 'N', 'n']:
            break
            
        if composite_input not in composites:
            print(f"无效的合数编号，仅支持01-13之间的编号")
            continue
        
        composite_group = composites[composite_input]
        to_exclude = [num for num in composite_group if num in val]
        if to_exclude:
            composite_excluded.extend(to_exclude)
            val = [num for num in val if num not in to_exclude]
            print(f"已剔除{composite_input}合的数字：{', '.join(to_exclude)}")
        else:
            print(f"{composite_input}合中无匹配当前组合的数字，无需剔除")
    
    composite_excluded = list(set(composite_excluded))
    
    # 步骤3：头数单双剔除
    head_check_excluded = []
    head_check_continue = input("\n是否需要进行头数单双剔除？(Y/N)：").strip().upper()
    if head_check_continue == 'Y':
        print("请输入需要剔除的头数单双（格式：X-Y，输入N结束，如1-0）：")
        while True:
            head_input = input("> ").strip()
            if head_input.upper() == 'N':
                break
                
            if len(head_input) != 3 or head_input[1] != '-':
                print("格式错误！请按'X-Y'输入（如1-0表示1头双）")
                continue
                
            try:
                head_digit = int(head_input[0])
                is_single = int(head_input[2]) == 1
            except ValueError:
                print("头数和单双标识必须是数字（X=0-4，Y=0/1）")
                continue
                
            if head_digit < 0 or head_digit > 4:
                print(f"头数{head_digit}超出范围，仅支持0-4")
                continue
                
            if head_input[2] not in ['0', '1']:
                print("单双标识错误！Y必须是0（双）或1（单）")
                continue
            
            target_numbers = get_head_check_numbers(head_digit, is_single)
            to_exclude = [num for num in target_numbers if num in val]
            type_str = "单" if is_single else "双"
            if to_exclude:
                head_check_excluded.extend(to_exclude)
                val = [num for num in val if num not in to_exclude]
                print(f"已剔除{head_digit}头{type_str}的数字：{', '.join(to_exclude)}")
            else:
                print(f"{head_digit}头{type_str}中无匹配当前组合的数字，无需剔除")
    
    head_check_excluded = list(set(head_check_excluded))
    
    # 输出最终结果
    print("\n===== 最终处理结果 =====")
    print(f"1. 合数剔除的数字：{', '.join(composite_excluded) if composite_excluded else '无'}")
    print(f"2. 头数单双剔除的数字：{', '.join(head_check_excluded) if head_check_excluded else '无'}")
    print(f"3. 最终保留的数字：{', '.join(val) if val else '无'}")
    
    # 新格式输出
    print("\n===== 筛选结果 =====")
    if composite_excluded:
        print(f"{', '.join(composite_excluded)}")
    if head_check_excluded:
        print(f"{', '.join(head_check_excluded)}")
    print(f"{', '.join(val) if val else '无'}")

if __name__ == "__main__":
    main()
    