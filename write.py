import datetime
import json

import operation

import display as d
import read as r

today = datetime.date.today()


def newBill(customer_log: operation.CustomerReq):
    print(r.readInventory())
    space = d.spacing(r.readInventory())
    fileNum = 1
    while True:
        filename = f"Bill_no_{fileNum}.txt"
        try:
            with open(f"Customer_Bill\{filename}", "x") as f:
                break
        except FileExistsError:
            fileNum += 1
    f = open(f"Customer_Bill\{filename}", "a")
    head = f"""
        DATE: {today}
        Bill No : {fileNum}                                                  
                                                                            Rent.co                            
                                                                            Address,                                                   
                                                                            City: Pokhara   ZIP: 33700
        Bill to:                                                            Phone: 9898989898
        Name: {customer_log.name}
        Address: {customer_log.address}
        Phone: {customer_log.phone}

         ___________________{"_" * space[0]}{"_" * space[1]}{"_" * space[2]}{"_" * space[3]}__________________________________________________________
        | SN | Item{" " * (space[0] - 4)} | Brand{" " * (space[1] - 5)}| Rate(Including VAT) | Quantity{" " * 3} | Duration{" " * 5} | Amount(Excluding VAT) |
        -------------------------------------------{"-" * space[0]}{"-" * space[1]}{"-" * space[2]}{"-" * space[3]}------------------------------------"""
    body = []
    for i in range(len(customer_log.itemDetail)):
        body.append(f"""
        | {(customer_log.itemDetail[i][-1]) + 1}{" " * (2 - len(str(customer_log.itemDetail[i][-1])))} | {customer_log.itemDetail[i][0]}{
        " " * (space[0] - len(customer_log.itemDetail[i][0]))} |{customer_log.itemDetail[i][1]}{" " * (space[1] - len(customer_log.itemDetail[i][1]))} | ${
        customer_log.itemDetail[i][2]}{" " * ((19 - len(chr(customer_log.itemDetail[i][2]))) - 1)} | {customer_log.itemDetail[i][3]}{
        " " * (11 - len(chr(customer_log.itemDetail[i][3])))} | {customer_log.days} Day/s{" " * (13 - len(customer_log.days.__str__()) - 6)} | ${
        round((customer_log.bill()[0][i]), 2)}{" " * (21 - len(round((customer_log.bill()[0][i]), 2).__str__()) - 1)} | """)
    f.write(head)
    c = open(f"Company_Bill_Record\{filename}", "a")
    c.write(head)
    for i in range(len(customer_log.itemDetail)):
        f.write(body[i])
        c.write(body[i])
    tail = f"""\n         -------------------------------------------{"-" * space[0]}{"-" * space[1]}{"-" * space[2]}{"-" * space[3]}----------------------------------

                                                                                               Total item price(Excluding VAT): ${round((sum(customer_log.bill()[0])), 2)}
                                                                                               VAT: ${round((customer_log.bill()[1]), 2)}
                                                                                               Total price: ${round((sum(customer_log.bill()[0]) + customer_log.bill()[1]), 2)}

                                    ***TERMA AND POLICIES***
"""
    f.write(tail)
    c.write(tail)
    f.close()
    c.close()

    with open(f"Company_Bill_Record\{filename}", "r") as f:
        print(f.read())
    with open(f"Rent_record\{filename}", "w") as f:
        for i in customer_log.itemDetail:
            f.write(str(i))


def updateItemQty(item, qty):
    f = open("inventory.txt", "r")
    data = f.readlines()
    f.close()
    item = item-1
    dataList = []
    updatedData = []
    for i in data:
        dataList.append(i.split(","))
    print(dataList)
    dataList[item][-1] = " "+str(int(dataList[item][-1]) - qty)+"\n"
    print(dataList)
    for i in dataList:
        u = ""
        for j in i[:3]:
            u += j+","
        updatedData.append(u)
    for i in range(len(dataList)):
        updatedData[i] += dataList[i][-1]
    f = open("inventory.txt", "w")
    print(updatedData)
    f.writelines(updatedData)
    f.close()
