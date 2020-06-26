# class Sz :
#     def __init__(self,gs):
#         self.sz = [None] * gs
#         self.yx = 0
#
#     def cr(self,wz,z):
#         if wz < 0 or wz > self.yx :
#             raise Exception ('数组越界!!!')
#         if self.yx >= len(self.sz) :
#             self.kz()
#         for i in range(self.yx-1,wz-1,-1) :
#             self.sz[i+1] = self.sz[i]
#         self.sz[wz] = z
#         self.yx += 1
#
#     def kz(self):
#         new = [None] * len(self.sz) * 2
#         for i in range(self.yx) :
#             new[i] = self.sz[i]
#         self.sz = new
#
#     def sc(self):
#         for i in range(self.yx) :
#             print(self.sz[i],end='->')
#
# if __name__ == '__main__':
#     w = Sz(3)
#     w.cr(0,10)
#     w.cr(1,20)
#     w.cr(2,30)
#     w.cr(3,40)
#     w.cr(4,100)



#     w.sc()







































# class Sd:
#     def __init__(self, A3):
#         self.sd = [None] * A3
#         self.E = 0
#
#     def d(self, d5, e6):
#         if d5 < 0 or d5 > self.E:
#             raise Exception("sxjx!!!")
#         if self.E >= len(self.sd):
#             self.R()
#         for i in range(self .E - 1, d5 - 1, -1):
#             self.sd[i + 1] = self.sd[i]
#         self.sd[d5] = e6
#         self.E += 1
#
#     def R(self):
#         new = [None] * len(self.sd) * 2
#         for i in range(self. E):
#             new[i] = self.sd[i]
#         self.sd = new
#
#     def Q(self):
#         for i in range(self.E):
#             print(self.sd[i], end="->")
#
#
# if __name__ == '__main__':
#     w = Sd(4)
#     w.d(0, 100)
#     w.d(1, 230)
#     w.d(2, 222)
#     w.d(3, 3000)
#     w.d(4, 350)
#     w.Q()
























