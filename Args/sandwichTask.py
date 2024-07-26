def sandwich(*dish): 
    for item in dish:
         print(item)
def main():
          toppings_add=[] 
          toppings=input("Enter the topings to add :")
          toppings_add=toppings.split(',') 
          sandwich(*toppings_add) 
if __name__=="__main__":
    main()