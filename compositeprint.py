for i in range(1,50):
    if i > 1:
        for f in range(2,i):
            if i % f == 0:
                print(i)
                break
        else:
            None