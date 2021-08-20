import pickle

dic = {'name': 'alvin', 'age': 23, 'sex': 'male'}
parameter = {'height': "65kg"}

print(type(dic))  # <class 'dict'>

j = pickle.dumps(dic)
g = pickle.dumps(parameter)

print(type(j))  # <class 'bytes'>

f = open('序列化对象_pickle', 'wb')  # 注意是w是写入str,wb是写入bytes,j是'bytes'
f.write(j)  # -------------------等价于pickle.dump(dic,f)

f.close()

a = open('序列化对象_pickle', 'ab')
a.write(g)
a.close()
# -------------------------反序列化

f = open('序列化对象_pickle', 'rb')

data = pickle.loads(f.read())  # 等价于data=pickle.load(f)

print(data)

"""======================================="""
import pickle

class add():
    def __init__(self, name):
        self.name = name
f1 = add('jack')
f2 = add('tom')

f = open('序列化对象_pickle', 'ab')  # 注意是w是写入str,wb是写入bytes,j是'bytes'
pickle.dump(f1, f)
f.close()
# -------------------------反序列化

v = open('序列化对象_pickle', 'rb')

data = pickle.load(v)

print(data.__dict__)
v.close()

# ----------------------------
import pickle

q = open('序列化对象_pickle', 'ab')
pickle.dump(f2, q)
q.close()

w = open('序列化对象_pickle', 'rb')

data = pickle.load(w)

print(data.__dict__)

w.close()
