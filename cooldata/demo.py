def myfunc(param0, param1="World", param2=100, param3=[1, 2, 3, 4]):
    return "Hello {} -> {}".format(param1, param0)


if __name__ == '__main__':
    print(myfunc("foo"))
