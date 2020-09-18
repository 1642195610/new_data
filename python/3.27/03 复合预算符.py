# 案例: 有人花了8块钱买了一只鸡,9块钱卖出去了,10块钱买回来了,11块钱卖出去了?
# 问,最后亏了还是赚了,亏了多少钱,赚了多少钱?

money=0
# money = money - 8
money -=8
# money = money + 9
money +=9
# money = money - 10
money -=10
# money = money + 11
money +=11
print(money)

# 用程序表示出来

# 从数学的角度看: 赚2块钱  (没有错)

# 从产品的角度看,亏了,亏了1块钱: 本来能挣3块钱;最后才挣了2块钱; 相当于亏了1块钱

