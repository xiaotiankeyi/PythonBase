"""
一.关系运算
　　有如下两个集合，pythons是报名python课程的学员名字集合，linuxs是报名linux课程的学员名字集合
　　pythons={'alex','egon','yuanhao','wupeiqi','gangdan','biubiu'}
　　linuxs={'wupeiqi','oldboy','gangdan'}"""

pythons = {'alex', 'egon', 'yuanhao', 'wupeiqi', 'gangdan', 'biubiu'}
linuxs = {'wupeiqi', 'oldboy', 'gangdan'}

"""1. 求出即报名python又报名linux课程的学员名字集合........求并集"""
print(pythons & linuxs)

"""2. 求出所有报名的学生名字集合........求交集"""
print(pythons | linuxs)

"""3. 求出只报名python课程的学员名字.........求差集"""
print(pythons - linuxs)

"""4. 求出没有同时报这两门课程的学员名字集合..........交叉补集"""
print(pythons ^ linuxs)
