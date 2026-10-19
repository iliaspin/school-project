max_g = -1
max_name = ""
sname = input ("Enter school's name ")
while sname != "End":
    cls = int(input ("Enter amount of classes "))
    SS = 0
    AM_G = 0
    SG = 0
    AM_C = 0
    for i in range (0,cls):
        boys, girls = int(input("Enter nuber of boys ")), int(input("Enter number of girls "))
        SS = SS + boys + girls
        SG = SG + girls
        if boys+girls <15 :
            AM_C = AM_C + 1
        if girls > boys :
            AM_G = AM_G + 1
    if SG > max_g :
        max_g = SG
        max_name = sname
    print(f"Students: {SS}, Average Students: {SS/cls}, Amount of small classes: {AM_G}")
    if cls == AM_G :
        print ("Girls are more in all classes")
    elif AM_G == 0:
        print ("There is no class that girls are more than boys")
    else :
        print (f"The amout of classes that girls are more than boys is: {AM_G}")
    sname = input ("Enter school's name ")
print (f"the school's name with the max number of girls is:{max_name}")


        


