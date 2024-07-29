def substraction(No1,No2):
    Ans = No1-No2
    return Ans
def Decorated_function(function_name):
    def Inner(A,B):
       if(A<B):
           output = function_name(A,B)
           return output
    return Inner
def main():
    value_01 = int(input('Enter the first Number:'))
    Value_02 = int(input('Enter the second Number:'))
    New_Function = Decorated_function(substraction)
    Result = New_Function(value_01,Value_02)
    print(Result)
if __name__ == "__main__":
    main()