def scope_test():
    def do_local():
        spam = "local spam"
        print('do_local >>>', spam)

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"
        print('do_non_local >>>', spam)

    def do_global():
        global spam
        spam = "global spam"
        print('do_global >>>', spam)

    spam = "spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)


scope_test()
print("In global scope:", spam)

"""output
do_local >>> local spam
After local assignment: spam
do_non_local >>> nonlocal spam
After nonlocal assignment: nonlocal spam
do_global >>> global spam
After global assignment: nonlocal spam
In global scope: global spam
"""
