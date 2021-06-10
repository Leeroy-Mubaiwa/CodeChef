
# cook your dish here
T = int(input())
for i in range(T):
    D, d, P, Q = map(int, input().split())
    n = D//d
    ans = n*P*d + (Q*(n*(n-1))//2)*d +(D%d)*(P+n*Q)
    print(ans)


T = int(input())
for i in range(T):
    
    D, d, P, Q = map(int, input().split())
    total = 0
    Qin = 0
    [number for number in range(D) if number % 5==0]
    #while i in range(D) and (d <= D):
    dt = i+1
    total += (P+Qin)
    if dt % d == 0:
            Qin += Q
    i +=1
print(total)