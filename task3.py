words = "hopefully everything works as expected"
maximum_width = 16
words_arr = words.split()

def fun(words_arr):
    result=""
    to_remove=""
    while len(words_arr):
        result+= words_arr[0]
        if len(result)==16:
            del words_arr[0]
            return result, words_arr
        if len(result)>16:
            to_remove=words_arr[0]
            break
        del words_arr[0]
        result+=" "
        if len(words_arr)==0:
            break
    result=result[:-(len(to_remove)+1)]

    cnt = result.count(" ")
    if cnt==0:
        return result, words_arr
    else:
        spaces = [result.find(" ", 0, len(result))]
        for x in range(0,cnt-1):
            spaces.append(result.find(" ", spaces[-1]+1, len(result)))

        for j in range(0,5):
            for i in range(0,cnt):
                result = result[:spaces[i]] + " " + result[spaces[i]:]
                for x in range(i+1,cnt):
                    spaces[x]+=1
                #print(result,spaces,i,len(result),maximum_width)
                if len(result)==maximum_width:
                    return result, words_arr
    return result, words_arr
    
while len(words_arr):
    result, words_arr = fun(words_arr)
    print(result)