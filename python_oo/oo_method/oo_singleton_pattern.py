#单例模式

class Singleton():
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            _instance = super().__new__(cls, *args, **kwargs)
            cls._instance = _instance
        
        return cls._instance


class mycalss(Singleton):
    pass


c1 = mycalss()
c2 = mycalss()
print(id(c1))
print(id(c2))