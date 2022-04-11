'''
字符串的布局
'''
coding = 'project,scan,sampler,sec,agent'
# ___center___设置宽度,并将内容居中,,,(*)两边都显示(*)
print(coding.center(50, '*'))

# ___ljust___往左移动50个宽度,实现左对齐,
print(coding.ljust(50, '%'))

# ___rjust___往右移动50宽度,实现右对齐
print(coding.rjust(50))
