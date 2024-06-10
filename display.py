import read as r


def spacing(file):  # this method returns an int list representing the maximum character of the colum
    max_length = []
    nu = 0
    while nu < len(file[0]):
        max_length.append(0)
        for s in range(len(file)):
            space = len(str(file[s][nu]))
            if space > max_length[nu]:
                max_length[nu] = space
        nu += 1
    return max_length


def show(file):     # this method prints a table of all the details from the list
    for ik in range(len(file)):
        for j in range(len(file[ik])):
            blank = ""
            for k in range(spacing(file)[j]-len(str(file[ik][j]))):
                blank = blank+" "
            print(file[ik][j], end=blank+" | ")
        print()


def showRecord():     # this method prints a table of all the details from the list
    itemSpace = " "*(spacing(r.readInventory())[0]-4)
    brandSpace = " "*(spacing(r.readInventory())[1]-5)
    rateSpace = " "*(spacing(r.readInventory())[2]-4)
    qtySpace = " "*(spacing(r.readInventory())[3]-3)
    for i in spacing(r.readInventory()):
        print("-"*(i+5), end="")
    print()
    print(f"""| item{itemSpace}  || Brand{brandSpace}  || Rate{rateSpace}  || Qty{qtySpace}  |""")
    for i in spacing(r.readInventory()):
        print("-" * (i+5), end="")
    print()
    for ik in range(len(r.readInventory())):
        for j in range(len(r.readInventory()[ik])):
            blank = ""
            for k in range(spacing(r.readInventory())[j]-len(str(r.readInventory()[ik][j]))):
                blank = blank+" "
            print("| ", r.readInventory()[ik][j], end=blank+" |")
        print()
        for i in spacing(r.readInventory()):
            print("-" * (i+5), end="")
        print()
