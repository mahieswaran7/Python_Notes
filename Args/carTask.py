def make_car(manufacturer,model,**specifications):
     print(manufacturer) 
     print(model)
     for key,value in specifications.items(): 
        print(key,value)
def main():
            make_car('Lamborghini','outback',color = 'yellow' , mileage="30km/Ltr",price="10cr",Highspeed="200km/hr") 
if __name__=="__main__":
    main()