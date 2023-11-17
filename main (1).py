# tree growth

a = int(4)

for i in range (7):
    print("enter humidity(%): ")
    h = int(input())
    h= h / 100
    if 0.03 < h < 0.12:
        a -= (a * 0.05/100)
        print("current size of magic tree is: ", a)
    elif 0.12< h <0.16:
        a += (a * 0.05/100)
        print("current size of magic tree is: ", a)
    elif 0.16< h < 0.26:
        a += (a * 0.03/100)
        print("current size of magic tree is: ", a)
    else:
        print("Tree died...")
        break


    
