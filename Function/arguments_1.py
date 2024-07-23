#Area of Circle=PI*Radius*Radius

def Area(Radius,PI=3.14):
    print('Arguments:',Radius)
    print('Pi')
    Result=PI*Radius*Radius
    return Result

def main():
    #Position_Argument
 Output_1=Area(10)
 print('Area of circle:',Output_1)

#first argument is positional and second is default

main()


#Keyword Argument
Output_2= Area(PI=3,Radius=12)
print('Area of circle:',Output_2)
if __name__ == "__main__":
    main()
