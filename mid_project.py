import os
#EX1
def log_parser():
    dict={'ERROR':0,'WARNING':0,'INFO':0}
    with open('log.txt','r') as file:
        lines=file.readlines()
        for line in lines:
            if 'ERROR' in line:
                dict['ERROR']+=1
            elif 'WARNING' in line:
                dict['WARNING']+=1
            elif 'INFO' in line:
                dict['INFO']+=1
    print(dict)
log_parser()

#EX2
def add_item_to_cart():
    os.system("cls")
    x = input("please write an item name: ")
    y = input("please write a price for this item: ")
    z = input("please write a quuntity you need to buy: ")
    shop_list[x] = {'price': y,'quantity': z}
    return
def del_item_from_cart():
    os.system("cls")
    userinput=input("write the item name you want to remove: ")
    shop_list.pop(userinput)
    return
def update_item_in_cart():
    os.system("cls")
    userinputi=input("write the item name you want to update: ")
    userinputq=input("write the new quantity for this item: ")
    shop_list[userinputi]["quantity"] = userinputq
    #or we can use with update function
    #shop_list[userinputi].update({'quantity': '5'})
    return
def show_cart():
    os.system("cls")
    for x, y in shop_list.items():
        print(x, y)
    os.system("pause")
   # print(shop_list)
def calculate_cart():
    os.system("cls")
    #print("111")
    #os.system("pause")
    total_price=0
    for key, obj in shop_list.items():
        total_price+=int(obj["price"])
        #print(obj["price"])
    print("The total price is:",total_price)
    os.system("pause")
    #return

shop_list={}
while True:
    os.system("cls")
    userinput=input("press 1 to add item\n"
    "press 2 to delete item\n"
    "press 3 to update item\n"
    "press 4 to show shoping cart\n"
    "press 5 to calculate shoping cart\n"
    "press 'x' to exit: ")
    try:
        if userinput=='x': break
        elif int(userinput)==1: add_item_to_cart()
        elif int(userinput)==2: del_item_from_cart()
        elif int(userinput)==3: update_item_in_cart()
        elif int(userinput)==4: show_cart()
        elif int(userinput)==5: calculate_cart()
    except:
        print("maybe you wrote bad things...")
print(shop_list)