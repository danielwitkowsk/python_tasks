def reversed(to_reverse,flag):
    result=0
    while(to_reverse):
        to_add = to_reverse % 10
        result *= 10
        result += to_add
        to_reverse //= 10
        if result>2147483647 or result<-2147483647:
            return 0
    if flag==0:
        return result
    elif flag==1:
        return -result
        
num = -555555555
flag=0

if (num<0):
    flag = 1
print(reversed(abs(num),flag))
