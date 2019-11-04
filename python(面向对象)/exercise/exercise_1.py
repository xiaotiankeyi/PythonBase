"""面向对象思路设计对战小游戏"""

class Riven:    #角色瑞雯
    camp='Noxus'
    def __init__(self,nickname,
                 aggressivity=54,
                 life_value=414,
                 money=1001,
                 armor=3):
        self.nickname=nickname
        self.aggressivity=aggressivity
        self.life_value=life_value
        self.money=money
        self.armor=armor
    def attack(self,enemy):
        damage_value=self.aggressivity-enemy.armor
        enemy.life_value-=damage_value

class Garen:        #角色盖伦
    camp='Demacia'
    def __init__(self,nickname,
                 aggressivity=58,
                 life_value=455,
                 money=100,
                 armor=10):
        self.nickname=nickname
        self.aggressivity=aggressivity
        self.life_value=life_value
        self.money=money
        self.armor=armor
    def attack(self,enemy):
        damage_value=self.aggressivity-enemy.armor
        enemy.life_value-=damage_value

class BlackCleaver:     #装备多兰之刃
    def __init__(self,price=475,aggrev=9,life_value=100):
        self.price=price
        self.aggrev=aggrev
        self.life_value=life_value
    def update(self,obj):
        obj.money-=self.price #减钱
        obj.aggressivity+=self.aggrev #加攻击
        obj.life_value+=self.life_value #加生命值
    def fire(self,obj): #这是该装备的主动技能,喷火,烧死对方
        obj.life_value-=1000 #假设火烧的攻击力是1000


if __name__ == "__main__":
    r1 = Riven('草丛伦')
    g1 = Garen('盖文')
    b1 = BlackCleaver()

    print(r1.aggressivity, r1.life_value, r1.money)  # r1的攻击力,生命值,护甲

    if r1.money > b1.price:     #角色金钱对比
        r1.b1 = b1
        b1.update(r1)

    print(r1.aggressivity, r1.life_value, r1.money)  # r1的攻击力,生命值,护甲

    print(g1.life_value)
    r1.attack(g1)  # 普通攻击
    print(g1.life_value)
    r1.b1.fire(g1)  # 用装备攻击
    print(g1.life_value)  # g1的生命值小于0就死了
