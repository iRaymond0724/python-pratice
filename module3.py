
def foo():
    """
    Python pass 是空语句，是为了保持程序结构的完整性。
    pass 不做任何事情，一般用做占位语句
    """
    print("fooooooooooo")
    # pass


def bar():
    print("barrrrrrrrrrrr")
    # pass

    #print("From module3")

# 因為模塊名不是 __main__ ，導入 module3 時，不會直接執行模塊中的方法，
# 只有模塊名為 __main__ 時  會觸發
# if __name__ == '__main__':
#     print("From module3")


# if __name__ == 'module3':
#     print("From module31")
