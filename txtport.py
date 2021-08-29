def jia(a):
    f = open("1w.txt", "a")  # 似乎这个r+是关键 此方法是新增用户 是否加入if来判断已经存在
    s = "##"+a
    f.write(s)
    b = "aaaa"
    for i in range(5):
        f.write(b)

    f.close()
    return 1
#print(jia("14"))
def gai(b,k):#b:插入的数值，k=身份码
    file = open('1w.txt', 'r+')
    i=0
    while(True):
        fi = file.read(24)
        if k==fi[0:4]:
            if fi[4]=="a":
                t = i * 24+4
            elif fi[8]=="a":
                t = i * 24+8
            elif fi[12]=="a":
                t = i * 24+12
            elif fi[16]=="a":
                t = i * 24+16
            elif fi[20]=="a":
                t = i * 24+20
            else:
                print("error")
                return 0
            break
        else:
            i+=1

    file.seek(t, 0)
    file.write(b)
    file.close()
    return t

#print(gai("yyyy","##12"))






#print("hello")