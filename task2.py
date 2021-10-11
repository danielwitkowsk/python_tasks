letters = [['a','b','c'],
['d','e','f'],
['g','h','i'],
['j','k','l'],
['m','n','o'],
['p','q','r','s'],
['t','u','v'],
['w','x','y','z']]

digits="27242"
final=[]
if digits.isdigit():
    if not digits:
        print(final)
    else:
        if digits[0] != '1' and digits[0] != '0':
            result =letters[ord(digits[0])-50]
            for x in range(1,len(digits)):
                if digits[x] != '1' and digits[x] != '0':
                    temp=letters[ord(digits[x])-50]
                    for y in result:
                        for z in temp:
                            final.append(y+z)
                    result=final
                    final=[]
                else:
                    print("error")
            print(result)
        else:
            print("error")
else:
    print("digits should be digits")

