rownum=5
space=rownum-1
for i in range(1,rownum +1):
    for j in range(1,space+1):
        print(end =" ")
    space= space-1
    for j in range(2*i-1):
        print(end ="*")
    print()
space=1
for i in range(1,rownum):
    for j in range(1,space+1):
        print(end =" ")
    space= space+1
    for j in range(1,2*(rownum-i)):
        print(end ="*")
    print()