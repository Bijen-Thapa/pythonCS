import read as r
import display as d
import write as w
import display as t


def great():
    print("""
    
    
  $$\                                               $$$$$$$\                       $$\               $$\           
$$ |                                              $$  __$$\                      $$ |              $$ |          
$$ |      $$$$$$\$$$$\   $$$$$$\   $$$$$$\        $$ |  $$ | $$$$$$\  $$$$$$$\ $$$$$$\    $$$$$$\  $$ | $$$$$$$\ 
$$ |      $$  _$$  _$$\  \____$$\ $$  __$$\       $$$$$$$  |$$  __$$\ $$  __$$\\_$$  _|   \____$$\ $$ |$$  _____|
$$ |      $$ / $$ / $$ | $$$$$$$ |$$ /  $$ |      $$  __$$< $$$$$$$$ |$$ |  $$ | $$ |     $$$$$$$ |$$ |\$$$$$$\  
$$ |      $$ | $$ | $$ |$$  __$$ |$$ |  $$ |      $$ |  $$ |$$   ____|$$ |  $$ | $$ |$$\ $$  __$$ |$$ | \____$$\ 
$$$$$$$$\ $$ | $$ | $$ |\$$$$$$$ |\$$$$$$  |      $$ |  $$ |\$$$$$$$\ $$ |  $$ | \$$$$  |\$$$$$$$ |$$ |$$$$$$$  |
\________|\__| \__| \__| \_______| \______/       \__|  \__| \_______|\__|  \__|  \____/  \_______|\__|\_______/ 
                                                                                                                                                                                                                                                                                                                                                                                                
                                                                                                                                                                                                   
    """)


class CustomerReq:  # describe concept properly in code and in docx
    def __init__(self):
        self.name = input("""                       Name: """)
        self.address = input("""                        Address: """)
        while True:
            try:
                self.phone = int(input("""                      Phone: """))
                if len(self.phone.__str__()) == 10:
                    break
                else:
                    print("Phone number must me 10 digits long")
                    pass
            except ValueError:
                print("""                       Invalid phone no. """)
                pass
        self.itemDetail = []
        self.item = 0
        self.qty = 0
        self.days = 0
        self.no = 0
        self.itemPrice = 0
        self.vat = 0
        self.qtyAll = []

    def rent(self):
        t.showRecord()
        while True:
            if len(self.itemDetail) == 0:
                try:
                    self.days = int(input("""                       Enter no. of days to rent the items for: """))
                    if int(self.days):
                        if (self.days % 5) == 0:
                            w.updateItemQty(self.item, self.qty)
                            self.rentP()
                            return True
                        else:
                            print("""                       Items can only be rented on 5 day basis""")
                except ValueError:
                    print("""                       Invalid input""")
                except KeyboardInterrupt:
                    print("""                       \nInput interrupted""")
            else:
                self.rentP()
                return True

    def rentP(self):
        while True:
            try:
                self.item = int(input("""                       Enter the item's SN: """))
                if int(self.item):
                    if 1 <= self.item <= len(r.readInventory()):
                        v = (r.readInventory()[self.item - 1])
                        v.append(self.item - 1)
                        v[-3] = int(v[-3][-1])
                        self.itemDetail.append(v)
                        while True:
                            try:
                                self.qty = int(input("""                        Enter the quantity: """))
                                if int(self.qty):
                                    if 1 <= self.qty <= int(r.readItemQty()[self.item - 1]):
                                        self.itemDetail[self.no][3] = self.qty
                                        self.qtyAll.append(self.qty)
                                        self.no += 1
                                        return True
                            except ValueError:
                                print("""                       Invalid input""")
                    else:
                        print("""                       Item with the given SN doesn't exist """)
            except ValueError:
                print("""                       Invalid input """)

    def bill(self):
        price = []
        vat = []
        for i in self.itemDetail:
            realPrice = i[-3] - (0.13 * i[-3])
            price.append((i[-2] * realPrice) * self.days)
            vat.append((i[-3] * 0.13)*i[-2] * self.days)
        return price, sum(vat)


class ReturnItem:
    def __init__(self):
        self.valid = False
        # self.rentDays =
        while True:
            try:
                self.bill = int(input("Enter your bill no: "))
            except Exception:
                print("Invalid input")

            finally:
                if int(self.bill):
                    if self.bill == int(r.readInvoiceValid(f"Customer_Bill\Bill_no_{self.bill}.txt")[1]):
                        while True:
                            self.days = input("Enter teh days: ")
                            if int(self.days):
                                self.valid = True
                                break
                            else:
                                print("Invalid days")
                                pass
                    else:
                        print("The provided Bill no. doesn't exist")
                        pass
                    break
                else:
                    print("Invalid bill no.")
                    pass
                break

    def returnItem(self):
        # f = open(f"Company_Bill_Record\Bill_no_{self.bill}.txt", "r")
        with open(f"Company_Bill_Record\Bill_no_{self.bill}.txt", "r") as f:
            print(f.read())

        while True:
            give = input("Enter y to return all item or n to exit: ")
            if give.lower() == "y":
                self.returnAll()
                break
            elif give.lower() == "n":
                break
            else:
                pass

    def returnAll(self, qty):
        oldQty = r.readItemQty()
        addQty = qty
        updatedQty = []
        for i in range(len(oldQty)):
            updatedQty.append(qty[i]+addQty[i])
            w.updateItemQty(i, updatedQty[i])
