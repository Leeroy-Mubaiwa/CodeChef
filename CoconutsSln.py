T=int(input())
for i in range(T):
    xa, xb, Xa, Xb = map(int, input("Input numbers seperated by space").split())
    TypeA=Xa/xa
    TypeB=Xb/xb
    print(int(TypeA+TypeB))





