import display as t
import write as w
from operation import CustomerReq, great, ReturnItem
from os import system


def program():
    great()
    while True:
        print("""
        Select options:
        1 to see the records
        2 to make an order
        3 to return items
        4 to exit
        """)
        valid = True
        try:
            i = int(input("Input: "))
        except ValueError:
            print("\nInvalid input")
            valid = False
            pass
        except KeyboardInterrupt:
            print("\nInvalid input")
            valid = False
            pass
        finally:
            if valid:
                if i == 1:
                    system('cls')
                    t.showRecord()
                elif i == 2:
                    system('cls')
                    customer = CustomerReq()
                    a = True
                    while a:
                        if customer.rent():
                            # qty.append(customer.qty)
                            # print(qty)
                            while True:
                                again = input("Order more(y/n): ")
                                if again == "y":
                                    break
                                elif again == "n":
                                    a = False
                                    break
                                else:
                                    print("Invalid input")
                    w.newBill(customer)
                    if input("press enter key to continue: "):
                        pass
                elif i == 3:
                    system("cls")
                    returning = ReturnItem()
                    if returning.valid:
                        returning.returnItem()
                        # returning.returnAll(qty)

                elif i == 4:
                    break
                else:
                    print("\nEnter a proper number")
            else:
                pass


program()
