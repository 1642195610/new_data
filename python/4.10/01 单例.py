# class Singleton:
#     instance =None
#     def __new__(cls, *args, **kwargs):
#         if cls.instance == None:
#             cls.instance = super().__new__(cls, *args, **kwargs)
#         return cls
# a = Singleton()
# b = Singleton()
# print(id(a),id(b))

# #单例
# class Singleton:
#     instance = None
#     def __new__(cls, *args, **kwargs):
#         if cls.instance == None:
#             cls.instance = super().__new__(cls, *args, ** kwargs)
#         return cls.instance
# a = Singleton()
# b = Singleton()
# c = Singleton()
# print(id(a), id(b), id(c))