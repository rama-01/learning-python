def foo():
    b = 'hello'

    # Python中可以在函数内部再定义函数
    def bar():
        nonlocal b
        b = 'world'
        c = True
        print(a)
        # print(b)
        print(c)

    bar()
    print(b)
    # print(c)  # NameError: name 'c' is not defined


if __name__ == '__main__':
    a = 100
    # print(b)  # NameError: name 'b' is not defined
    foo()

# 总结，使用global指示变量来自于全局作用域，使用nonlocal指示变量来自于嵌套作用域
