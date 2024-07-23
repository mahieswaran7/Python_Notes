def add_funtion(menu_card,add_list):
    menu_card.append(add_list)
    return menu_card

def update_function(menu_card,update_list,update_item):
    menu_card[update_list]=update_item
    return menu_card

def delete_function(menu_card,remove_list):
    menu_card.remove(remove_list)
    return menu_card

def main():
    menu_card=["paneer Naan","Corn with pepper","veg salad","french fries","cheesy burger"]
    choice=int(input("Enter your choice from 1 to 4 : "))
    while(True):
        if(choice==1):
            print(menu_card)
            break
        elif(choice==2):
            add_list=input("which starter  food you want to add in the startermenu : ")
            print(add_funtion(menu_card,add_list))
            break
        elif(choice==3):
            update_list=int(input("enter the index to be update : "))
            update_item=input("enter the item : ")
            print(update_function(menu_card,update_list,update_item))
            break
        elif(choice==4):
            remove_list=input("enter the item to be removed :")
            print(delete_function(menu_card,remove_list))
            break
        else:
            print("you have enter the wrong choice...")
            break

if __name__=="__main__":
    main()