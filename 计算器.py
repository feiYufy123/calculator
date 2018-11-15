import tkinter

win = tkinter.Tk()        # 创建主窗口
win.title("李秀刚大晚上的秀啊")      # 设置标题
win.geometry("182x271+40+40")       # 设置大小和位置
# 进入消息循环

v = tkinter.StringVar()     # 这即是输入框中的内容
v.set(0)                    # 用于显示默认数字0

#标签显示板
lab = tkinter.Label(win, bg="white",width = 100,height = 4,font = ("黑体",16), anchor="se",textvariable = v)#font可改变标签框与下面的距离
lab.pack(fill=tkinter.X, side=tkinter.TOP)
lab.pack()

button1 = tkinter.Button(win,text = "c",command = lambda : yunSuan("c"))
button1.place(x = 5,y = 100,width = 40, height = 30)
button2 = tkinter.Button(win,text = "/",command = lambda : yunSuan("/"))
button2.place(x = 50, y = 100, width = 40, height = 30)
button3 = tkinter.Button(win,text = "*",command = lambda : yunSuan("*"))
button3.place(x = 95,y = 100,width = 40, height = 30)
button4 = tkinter.Button(win,text = "←",command = lambda : yunSuan("←"))
button4.place(x = 140, y = 100, width = 40, height = 30)

button5 = tkinter.Button(win,text="7",command = lambda : pressNum("7"))
button5.place(x = 5,y = 135,width = 40, height = 30)
button6 = tkinter.Button(win,text = "8",command = lambda : pressNum("8"))
button6.place(x = 50, y = 135, width = 40, height = 30)
button7 = tkinter.Button(win,text = "9",command = lambda : pressNum("9"))
button7.place(x = 95,y = 135,width = 40, height = 30)
button8 = tkinter.Button(win,text = "-",command = lambda : yunSuan("-"))
button8.place(x = 140, y = 135, width = 40, height = 30)

button9 = tkinter.Button(win,text = "4",command = lambda : pressNum("4"))
button9.place(x = 5,y = 170,width = 40, height = 30)
button10 = tkinter.Button(win,text = "5",command = lambda : pressNum("5"))
button10.place(x = 50, y = 170, width = 40, height = 30)
button11 = tkinter.Button(win,text = "6",command = lambda : pressNum("6"))
button11.place(x = 95,y = 170,width = 40, height = 30)
button12 = tkinter.Button(win,text = "+",command = lambda : yunSuan("+"))
button12.place(x = 140, y = 170, width = 40, height = 30)

button13 = tkinter.Button(win,text = "1",command = lambda : pressNum("1"))
button13.place(x = 5,y = 205,width = 40, height = 30)
button14 = tkinter.Button(win,text = "2",command = lambda : pressNum("2"))
button14.place(x = 50, y = 205, width = 40, height = 30)
button15 = tkinter.Button(win,text = "3",command = lambda : pressNum("3"))
button15.place(x = 95,y = 205,width = 40, height = 30)

button16 = tkinter.Button(win,text = "=",command = lambda : end())
button16.place(x = 140, y = 205, width = 40, height = 65)
button17 = tkinter.Button(win,text = "0",command = lambda : pressNum("0"))
button17.place(x = 5, y = 240, width = 85, height = 30)
button18 = tkinter.Button(win,text = ".",command = lambda : yunSuan("."))
button18.place(x = 95, y = 240, width = 40, height = 30)


# 操作函数
list1 = []   # 创建一个列表，保存运算数字和符号
ispressSign = False   # 判断是否按下运算符号的标志，假设一开始没有按下
ispressNum = False

#数字函数
def pressNum(num):    #判断是否按下数字，并且在显示板上显示
    global list1      # 全局化list1和按钮状态ispressSign
    global ispressSign
    if ispressSign == False:
        pass
    else:      #重新设置状态变为  False
        v.set(0)
        ispressSign = False

    oldnum = v.get()   # 判断显示板数字是否为0
    if oldnum == "0":  #显示板若是为0，则按下获取的数字
        v.set(num)
    else:
        newNum = oldnum + num   #显示板上的数字不为0，则连接上新按下的数字
        v.set(newNum)           # 将新数字写到显示板中


def yunSuan(sign):
    global list1
    global ispressSign
    num = v.get()    # 获取显示板上的数字
    list1.append(num)     #保存显示板数字到列表中

    list1.append(sign)   #将按下的运算符号也存到列表中
    ispressSign = True

    if sign == "c":    #按“c”键，清空列表，重新默认为0
        list1.clear()
        v.set(0)
    if sign == "←":
        a = num[0:-1]
        list1.clear()
        v.set(a)

#获取结果
def end():
    global list1
    global ispressSign

    curnum = v.get()       #设置当前数字变量，并获取，再添加到列表中
    list1.append(curnum)

    str1 = "".join(list1)
    endNum = eval(str1)

    v.set(endNum)


win.mainloop()