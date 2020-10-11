def rabin_karp(data,text):
    x = 'abcdefghijklmnopqrstuvwxyz'
    dct = {}
    lst = []
    path = ''
    x_len = 0
    text_len = 0
    for i in text:
        text_len = text_len + 1
    for j in x:
        x_len = x_len + 1

    for j in range(1,x_len+1):
        dct[x[j-1]] = j
    lower = data.lower()
    for j in text:
        path = path + str(dct[j])

    for i in range(x_len):
        temp = ''
        try:
            string = lower[i:i + text_len]
            for j in string:
                temp = temp + str(dct[j])
                if int(path) == int(temp):
                    lst.append(i)
        except:
            pass

    return lst


print(rabin_karp('my name is shahzaib' , 'shah'))