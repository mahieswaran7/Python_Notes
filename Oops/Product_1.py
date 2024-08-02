def task_1():
    class Product:
        _product_id = 0
        
        def  add_function(self,pname,pprice,pdesc):
            self.pname = pname
            self.pprice = pprice
            self.pdesc = pdesc
            Product._product_id += 1 
            self.__id = self._product_id
            print("Prodect add sucessfully")
        def get_product_names(self):
            print(f"product name: {self.pname}")
            print(f"product price: {self.pprice}")
            print(f"product description: {self.pdesc}")
            print(f"product id: {self.__id}")
           
    product_1 = Product()
    product_1.add_function(pname=input("Enter the product name: "),
                           pprice=int(input("Enter the product price: ")),
                           pdesc=input("Enter the product description: "))
    product_1.get_product_names()
    product_2 = Product()
    product_2.add_function(pname=input("Enter the product name: "),
                           pprice=int(input("Enter the product price: ")),
                           pdesc=input("Enter the product description: "))
    product_2.get_product_names()
    product_3 = Product()
    product_3.add_function(pname=input("Enter the product name: "),
                           pprice=int(input("Enter the product price: ")),
                           pdesc=input("Enter the product description: "))
    product_3.get_product_names()
    product_4 = Product()
    product_4.add_function(pname=input("Enter the product name: "),
                           pprice=int(input("Enter the product price: ")),
                           pdesc=input("Enter the product description: "))
    product_4.get_product_names()

def main():
    task_1()

if __name__ == "__main__":
    main()