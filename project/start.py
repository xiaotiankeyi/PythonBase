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

# 波色与对应数字的字典
color_wave_dict = {
    "红波": ["01", "02", "07", "08", "12", "13", "18", "19", "23", "24", "29", "30", "34", "35", "40", "45", "46"],
    "蓝波": ["03", "04", "09", "10", "14", "15", "20", "25", "26", "31", "36", "37", "41", "42", "47", "48"],
    "绿波": ["05", "06", "11", "16", "17", "21", "22", "27", "28", "32", "33", "38", "39", "43", "44", "49"]
}

def get_numbers_from_color(colors):
    """根据输入的波色列表获取对应的数字集合(去重)"""
    numbers = []
    for color in colors:
        if color in color_wave_dict:
            numbers.extend(color_wave_dict[color])
    # 去重并排序
    seen = set()
    unique_numbers = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            unique_numbers.append(num)
    return sorted(unique_numbers)

def filter_composite(val, composites):
    """合数过滤功能:支持批量输入,输入n退出"""
    composite_excluded = []
    print("\n=== 进入合数过滤(输入n退出)===")
    print(f"当前待过滤数字:{', '.join(val)}")
    
    while True:
        composite_input = input("请输入需要剔除的合数(多个用逗号分隔,如02,05):").strip()
        if composite_input.upper() == 'N':
            print(f"=== 退出合数过滤,累计剔除:{', '.join(composite_excluded) if composite_excluded else '无'} ===")
            return val, composite_excluded
        
        composite_list = [c.strip() for c in composite_input.split(',')]
        for composite in composite_list:
            if composite not in composites:
                print(f"无效的合数编号:{composite},仅支持01-13")
                continue
            
            composite_group = composites[composite]
            to_exclude = [num for num in composite_group if num in val]
            if to_exclude:
                composite_excluded.extend(to_exclude)
                val = [num for num in val if num not in to_exclude]
                print(f"已剔除{composite}合的数字:{', '.join(to_exclude)},当前剩余:{', '.join(val)}")
            else:
                print(f"{composite}合中无匹配当前组合的数字,无需剔除")

def filter_head_single_double(val):
    """头数单双过滤功能:支持多次输入,输入n退出"""
    head_check_excluded = []
    print("\n=== 进入头数单双过滤(输入n退出)===")
    print(f"当前待过滤数字:{', '.join(val)}")
    
    while True:
        head_input = input("请输入需要剔除的头数单双(格式:X-Y,如1-0表示1头双):").strip()
        if head_input.upper() == 'N':
            print(f"=== 退出头数单双过滤,累计剔除:{', '.join(head_check_excluded) if head_check_excluded else '无'} ===")
            return val, head_check_excluded
        
        if len(head_input) != 3 or head_input[1] != '-':
            print("格式错误！请按'X-Y'输入(如1-0表示1头双)")
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
            print("单双标识错误！Y必须是0(双)或1(单)")
            continue
        
        target_numbers = get_head_check_numbers(head_digit, is_single)
        to_exclude = [num for num in target_numbers if num in val]
        type_str = "单" if is_single else "双"
        
        if to_exclude:
            head_check_excluded.extend(to_exclude)
            val = [num for num in val if num not in to_exclude]
            print(f"已剔除{head_digit}头{type_str}的数字:{', '.join(to_exclude)},当前剩余:{', '.join(val)}")
        else:
            print(f"{head_digit}头{type_str}中无匹配当前组合的数字,无需剔除")

def filter_shengxiao(val):
    """生肖过滤功能:支持批量输入,输入n退出"""
    shengxiao_excluded = []
    print("\n=== 进入生肖过滤(输入n退出)===")
    print(f"当前待过滤数字:{', '.join(val)}")
    print(f"支持的生肖:{', '.join(shengxiao_dict.keys())}")
    
    while True:
        shengxiao_input = input("请输入需要剔除的生肖(多个用逗号分隔,如鼠,牛):").strip()
        if shengxiao_input.upper() == 'N':
            print(f"=== 退出生肖过滤,累计剔除:{', '.join(shengxiao_excluded) if shengxiao_excluded else '无'} ===")
            return val, shengxiao_excluded
        
        shengxiao_list = [s.strip() for s in shengxiao_input.split(',')]
        for shengxiao in shengxiao_list:
            if shengxiao not in shengxiao_dict:
                print(f"无效生肖:{shengxiao},仅支持{', '.join(shengxiao_dict.keys())}")
                continue
            
            target_numbers = shengxiao_dict[shengxiao]
            to_exclude = [num for num in target_numbers if num in val]
            if to_exclude:
                shengxiao_excluded.extend(to_exclude)
                val = [num for num in val if num not in to_exclude]
                print(f"已剔除{shengxiao}对应的数字:{', '.join(to_exclude)},当前剩余:{', '.join(val)}")
            else:
                print(f"{shengxiao}中无匹配当前组合的数字,无需剔除")

def filter_tail_number(val):
    """尾数过滤功能:输入0-9的数字,过滤所有尾数匹配的数字,支持批量输入"""
    tail_excluded = []
    print("\n=== 进入尾数过滤(输入n退出)===")
    print(f"当前待过滤数字:{', '.join(val)}")
    
    while True:
        tail_input = input("请输入需要剔除的尾数(多个用逗号分隔,0-9之间,如1,3):").strip()
        if tail_input.upper() == 'N':
            print(f"=== 退出尾数过滤,累计剔除:{', '.join(tail_excluded) if tail_excluded else '无'} ===")
            return val, tail_excluded
        
        # 处理批量输入
        tail_list = [t.strip() for t in tail_input.split(',')]
        for tail in tail_list:
            # 校验输入是否为0-9的数字
            if not tail.isdigit() or len(tail) != 1 or not (0 <= int(tail) <= 9):
                print(f"无效尾数:{tail},仅支持0-9的单个数字")
                continue
            
            # 筛选所有尾数匹配的数字
            to_exclude = [num for num in val if num.endswith(tail)]
            if to_exclude:
                tail_excluded.extend(to_exclude)
                val = [num for num in val if num not in to_exclude]
                print(f"已剔除尾数为{tail}的数字:{', '.join(to_exclude)},当前剩余:{', '.join(val)}")
            else:
                print(f"当前数字中无尾数为{tail}的数字,无需剔除")

def main():
    composites = generate_composite_numbers()
    
    # 步骤1:输入波色生成初始数字
    print("请输入波色(多个波色用逗号分隔,支持:红波,蓝波,绿波):")
    while True:
        color_input = input("> ").strip()
        if not color_input:
            print("波色不能为空,请重新输入")
            continue
            
        color_list = [c.strip() for c in color_input.split(',')]
        invalid = [c for c in color_list if c not in color_wave_dict]
        
        if invalid:
            print(f"无效波色:{', '.join(invalid)},请使用正确的波色名称(红波、蓝波、绿波)")
            continue
            
        val = get_numbers_from_color(color_list)
        print(f"\n波色对应的初始数字:{', '.join(val)}")
        break
    
    if not val:
        print("没有有效的数字可供处理,程序结束")
        return
    
    # 初始化各过滤环节的剔除记录
    all_composite_excluded = []
    all_head_excluded = []
    all_shengxiao_excluded = []
    all_tail_excluded = []  # 新增:尾数过滤记录
    
    # 菜单式过滤选择(新增尾数过滤选项)
    print("\n===== 过滤功能菜单 =====")
    print("请选择需要的过滤操作(输入对应数字,输入n结束所有过滤):")
    print("1 - 过滤合数(01-13合)")
    print("2 - 过滤头数单双(格式:X-Y)")
    print("3 - 过滤生肖(12生肖)")
    print("4 - 过滤尾数(0-9的数字)")  # 新增选项
    
    while True:
        menu_choice = input("\n请输入选择(1/2/3/4/n):").strip().upper()
        
        if menu_choice == 'N':
            print("\n===== 已退出所有过滤流程,正在生成最终结果 =====")
            break
        
        # 选择对应过滤功能
        if menu_choice == '1':
            val, composite_excluded = filter_composite(val, composites)
            all_composite_excluded.extend(composite_excluded)
        elif menu_choice == '2':
            val, head_excluded = filter_head_single_double(val)
            all_head_excluded.extend(head_excluded)
        elif menu_choice == '3':
            val, shengxiao_excluded = filter_shengxiao(val)
            all_shengxiao_excluded.extend(shengxiao_excluded)
        elif menu_choice == '4':  # 新增:调用尾数过滤
            val, tail_excluded = filter_tail_number(val)
            all_tail_excluded.extend(tail_excluded)
        else:
            print("无效选择！请输入1/2/3/4或n")
    
    # 整理最终剔除记录(去重排序)
    all_composite_excluded = sorted(list(set(all_composite_excluded)))
    all_head_excluded = sorted(list(set(all_head_excluded)))
    all_shengxiao_excluded = sorted(list(set(all_shengxiao_excluded)))
    all_tail_excluded = sorted(list(set(all_tail_excluded)))  # 尾数过滤结果
    
    # 输出最终结果
    print("\n===== 最终处理结果 =====")
    print(f"1. 合数剔除的数字:{', '.join(all_composite_excluded) if all_composite_excluded else '无'}")
    print(f"2. 头数单双剔除的数字:{', '.join(all_head_excluded) if all_head_excluded else '无'}")
    print(f"3. 生肖过滤剔除的数字:{', '.join(all_shengxiao_excluded) if all_shengxiao_excluded else '无'}")
    print(f"4. 尾数过滤剔除的数字:{', '.join(all_tail_excluded) if all_tail_excluded else '无'}")  # 新增
    print(f"5. 最终保留的数字:{', '.join(sorted(val)) if val else '无'}")
    
    # 新格式输出
    print("\n===== 筛选结果 =====")
    if all_composite_excluded:
        print(f"{', '.join(all_composite_excluded)}")
    if all_head_excluded:
        print(f"{', '.join(all_head_excluded)}")
    if all_shengxiao_excluded:
        print(f"{', '.join(all_shengxiao_excluded)}")
    if all_tail_excluded:  # 新增
        print(f"{', '.join(all_tail_excluded)}")
    print(f"{', '.join(sorted(val)) if val else '无'}")

if __name__ == "__main__":
    main()
    