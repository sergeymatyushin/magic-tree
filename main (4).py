# tree growth
a = 4
a1 = 4
x = 1
while True:
    print("enter humidity(%): ")
    h = int(input())
    h= h / 100
    if 0.03 <= h <= 0.12:
        a = a + (x+x * 5/100)
        print("current size of magic tree is: ", a)
        print("diff is: ",a-a1)
        a1=a
    elif 0.13<= h <=0.16:
        a =a + (x + x * 5/100)
        print("current size of magic tree is: ", a)
        print("diff is: ", a-a1)
        a1=a
    elif 0.17<= h <= 0.26:
        a =a + (x+x * 3/100)
        print("current size of magic tree is: ", a)
        print("diff is: ", a-a1)
        a1=a
    else:
        print("Tree died...")
        break