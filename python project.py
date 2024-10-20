from datetime import datetime
from math import ceil
from random import randint, choices
import string

class grocery:
     items_list:list
     price_list:list
     qua:int
     qua_list:list
     qua_u_list:list
     price_u_list:list
     new:list
     newp:list
class admin:
     name:str
     pass_w:str
class bill:
    idi:eval
    money:int
    ext:float
    final_price:float
    c:str
    utr:str

bi = bill()
ad = admin()
gc = grocery()
gc.items_list = []
gc.price_list = []
gc.qua_list = []
gc.qua_u_list = []
gc.price_u_list = []
gc.new = []
gc.newp = []
bi.c = ""
bi.utr = ""

def intro():
     f5 = open("receipt.txt", "w")
     print("\t\t", end=50*"*")
     print("\t\t", end=50*"*", file=f5)
     print("\n\t\t", end=15*"*")
     print("\n\t\t", end=15*"*", file=f5)
     print("S.R.M Grocery store", end=15*"*")
     print("S.R.M Grocery store", end=15*"*", file=f5)
     print("\n\t\t", end=50*"*")
     print("\n\t\t", end=50*"*", file=f5)
     f5.close()

# Generate Bill Number
def number():
    bill = []
    bill.append(randint(0, 9))
    for i in range(1, 10):
        bill.append(randint(0, 9))
    for i in bill:
        bi.c += str(i)

# Opening Items File
f = open("items.txt", "r")
l = f.read().split(",")
for i in l:
     j = i.replace(' ', '')
     gc.items_list.append(j)
f.close()
number()

# Opening Prices File
f1 = open("prices.txt", "r")
l1 = f1.read().split(",")
for i in l1:
     j1 = i.replace(' ', '')
     gc.price_list.append(eval(i))
f1.close()

# Opening Quantity File
f2 = open("qua.txt", "r")
l2 = f2.read().split("\n")
for k in l2:
     if k.strip():
          gc.qua_u_list.append(int(k))
f2.close()

# Login Function
def login():
     intro()
     inp = int(input("\nPress 1 If You Are Admin or Press 2 If You Are Customer \n"))
     if inp == 1:
          ad.name = input("Enter your Name: ")
          if len(ad.name) > 3 and len(ad.name) < 20:
               pass_w1()
          else:
               print("Please Enter a correct name")
               login()
     else:
          items_list_fun()

# Login Password Function
def pass_w1():
     ad.pass_w = input("Enter Your password: ")
     if len(ad.pass_w) == 4:
          if ad.name == "admin" and ad.pass_w == "2116":
               print("Login successful!!!")
               updated()
          else:
               print("Kindly check Your Username and Password")
               login()
     else:
          pass_w1()

f3 = open("qua.txt", "w")

# Updated List of Items
def updated():
    print("S.no\t\t\tItems\t\t\t\t\t\tPrices\t\t\tRemaining Quantity")
    for i in range(1, len(gc.items_list) + 1):
        print(f'{i:>=1}\t\t\t{gc.items_list[i - 1]:<25}\t\t\t{gc.price_list[i - 1]:<5}\t\t\t{gc.qua_u_list[i - 1]:>0}')

# Displaying Items List
def items_list_fun():
     print("S.no\t\t\tItems\t\t\t\t\t\tPrices\t\t\tRemaining Quantity")
     for i in range(1, len(gc.items_list) + 1):
               print(f'{i:>=1}\t\t\t{gc.items_list[i - 1]:<25}\t\t\t{gc.price_list[i - 1]:<5}\t\t\t{gc.qua_u_list[i - 1]:>0}')
     while True:
          opt = int(input("Select your Item: "))
          for j in range(1, len(gc.items_list) + 1):
               if opt == j:
                    gc.qua = int(input("Enter Required quantity: "))
                    if gc.qua_u_list[j - 1] - gc.qua < 0:
                         print("No quantity is available")
                         items_list_fun()
                    else:
                         print(f"You have Selected {gc.items_list[opt - 1]}")
                         print("Press 0 to Continue for Billing")
                         gc.qua_list.insert(opt - 1, gc.qua)
                         gc.qua_u_list[opt - 1] -= gc.qua
                         gc.price_u_list.insert(opt - 1, gc.qua * gc.price_list[opt - 1])
                         gc.new.append(gc.items_list[opt - 1])
                         gc.newp.append(gc.price_list[opt - 1])
                         if gc.qua != 0:
                              for k in gc.qua_u_list:
                                   f3.write(str(k))
                                   f3.write("\n")
          if opt == 0:
                    payment()
                    pay()
                    break

f5 = open("receipt.txt", "w")

# Payment Process and Receipt Printing
def payment():
     name = input("Enter your Name: ")
     ph_no = input("Enter Your Phone Number: ")
     while len(ph_no) != 10:
          ph_no = input("Enter Correct Phone Number: ")
     gst = (sum(gc.price_u_list) * 5) / 100
     bi.final_price = gst + sum(gc.price_u_list)
     print(25*"-", "SRM GROCERY STORE AND MANAGEMENT", 21*"-")
     f5.write("\n")
     print(25*"-", "SRM GROCERY STORE AND MANAGEMENT", 21*"-", file=f5)
     print(35*"-", "WELCOME", 35*"-")
     print(35*"-", "WELCOME", 35*"-", file=f5)
     print("BILL NO: ", bi.c)
     print("BILL NO: ", bi.c, file=f5)
     print("NAME: ", name, 40*" ")
     print("NAME: ", name, 40*" ", file=f5)
     print("DATE: ", datetime.now())
     print("DATE: ", datetime.now(), file=f5)
     print("PHONE NUMBER: ", ph_no)
     print("PHONE NUMBER: ", ph_no, file=f5)
     print(80*"-")
     print(80*"-", file=f5)
     print(f'{"S.no":>1}\t\t\t{"ITEMS":<15}\t\t{"QUANTITY":>10}\t\t{"PRICE":<5}')
     print(f'{"S.no":>1}\t\t\t{"ITEMS":<15}\t\t{"QUANTITY":>10}\t\t{"PRICE":<5}', file=f5)
     for i in range(len(gc.qua_list)):
          print(f'{i + 1:>1}\t\t\t{gc.new[i]:<15}\t\t{gc.qua_list[i]:>10}\t\t{gc.newp[i]:<5}')
          print(f'{i + 1:>1}\t\t\t{gc.new[i]:<15}\t\t{gc.qua_list[i]:>10}\t\t{gc.newp[i]:<5}', file=f5)
     print(80*"-")
     print(80*"-", file=f5)
     print(25*" ", "TOTAL AMOUNT: ", "Rs", float(sum(gc.price_u_list)))
     print(25*" ", "TOTAL AMOUNT: ", "Rs", float(sum(gc.price_u_list)), file=f5)
     print("gst Amount ", 10*" ", "\t\tGst   :\t Rs  ", float(gst))
     print("gst Amount ", 10*" ", "\t\tGst   :\t Rs  ", float(gst), file=f5)
     print(80*"-")
     print(80*"-", file=f5)
     print(25*" ", "FINAL AMOUNT: ", "Rs", bi.final_price)
     print(25*" ", "FINAL AMOUNT: ", "Rs", bi.final_price, file=f5)
     print(80*"-")
     print(80*"-", file=f5)

# UPI Payment and UTR Number Input
def upi():
    print("\nOPEN THE UPI MOBILE APP AND APPROVE THE bill")
    utr_number = input("Enter the UTR Number after payment: ")  # Customer enters UTR
    bi.utr = utr_number
    print(f"\nUTR Number entered: {utr_number}")
    print("Thank you! Printing the bill now.")
    print_receipt(utr_number)

# Print Receipt with UTR Number
def print_receipt(utr_number):
    print(25 * "-", "SRM GROCERY STORE AND MANAGEMENT", 21 * "-")
    print(f"BILL NO: {bi.c}")
    print(f"YOUR UTR NUMBER: {utr_number}")  # Print UTR number
    # Add other receipt printing details as necessary
    print(25 * "-", "THANKS FOR VISITING", 25 * "-")
    f5.write(f"BILL NO: {bi.c}\n")
    f5.write(f"YOUR UTR NUMBER: {utr_number}\n")  # Write UTR number to the file
    f5.close()

# Payment Options
def pay():
    pay = int(input("\nPlease Choose Payment Option\n1.Debit/Credit Card\n2.UPI\n3.Pay on Delivery\n"))
    if pay == 1:
        print("\nWELCOME TO DEBIT/CREDIT CARD METHOD\n")
    elif pay == 2:
        upi()  # Call UPI function
    elif pay == 3:
        print("\nWELCOME TO COD METHOD\n")
    else:
        print("\nChoose a correct Option!!!")
        pay()

login()
f3.close()
