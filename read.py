def readInventoryRaw():
    f = open("inventory.txt", "r")
    data = f.read().split("\n")
    f.close()
    dataList = []
    for i in data:
        dataList.append(i)
    return data


def readInventory():        # this function reads the main inventory file and returns it in a 2D list form
    """This function reads the current inventory and returns the data"""
    f = open("inventory.txt", "r")
    data = f.read().split("\n")
    f.close()
    dataList = []
    data.pop()
    for i in data:
        dataList.append(i.split(","))
    return dataList


def readInvoiceValid(file):
    f = open(file, "r")
    data = f.read().split("\n")
    f.close()
    List = []
    dataList = []
    dataq = []
    for i in data:
        List.append(i.split(","))
    for i in range(1, 3):
        dataList.append(List[i])
    for i in range(2):
        for j in dataList[i]:
            dataq.append(j.split().pop(-1))
    return dataq


def readItemQty():
    f = open("inventory.txt", "r")
    data = f.read().split("\n")
    f.close()
    dataList = []
    data.pop()
    for i in data:
        qty = i.split(",")
        dataList.append(int(qty[-1]))
        print(dataList)
    return dataList


def readBillQty(file):
    f = open(file, "r")
    data = f.read().split("][")
    f.close()
    dataList = []
    for i in data:
        qty = i.split(",")
        dataList.append(int(qty[3]))
    return dataList

