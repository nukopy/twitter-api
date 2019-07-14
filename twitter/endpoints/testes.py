def scope_test():
    def do_local():
        spam = "local spam"
        print('func: do_local', spam)

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"
        print('func: do_non_local', spam)

    def do_global():
        global spam
        spam = "global spam"
        print('func: do_global', spam)

    spam = "spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)


scope_test()
print("In global scope:", spam)
