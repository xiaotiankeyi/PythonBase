class Foo():
    pass
    def __str__(self):  #可以自定义修改return
        return 'None'

    def __repr__(self):
        return 'None'

print(dir(Foo))
print(Foo.__dict__)