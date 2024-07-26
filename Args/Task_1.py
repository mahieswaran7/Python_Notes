# def variable_length(*args):
#     counts = 0
#     print(args)
#     for trash in args:
#         counts+=trash
#     return counts

# print(variable_length(1,2,3,4,5,6,7,8,9))


def argu(*args):
    print(args)
    print(type(args))
    for trash in args:
        print(trash)
        print(type(trash))
        for trash1 in trash:
            print(type(trash1))
            print(trash1)

def main():
    argu(['eswaran','aravindan','bala','yokesh','dinesh','thiru'])


if __name__ == "__main__":
    main()

# def kwargs(**kwargs):
#     for value in kwargs.values():
#         print(value)

# def main():
#     changepond = {"name":"Eswaran Arumugam","age":21,"mobilenumber":8925708431}
#     kwargs(**changepond)

# if __name__ == "__main__":
#     main()
