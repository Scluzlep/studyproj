for i in range(1,5):
    for j in range(1,2*i):
        print ('#',end = '')
    for j in range(9-2*i,0,-1):
        print('@',end = '')
    print()
