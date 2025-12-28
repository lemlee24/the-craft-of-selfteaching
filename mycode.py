def is_prime(n):
    """
    Return a boolean value based upon
    whether the argument n is a prime number.
    """
    if n < 2:
        return False
    if n == 2:
        return True
    for m in range(2, int(n**0.5)+1):
        if (n % m) == 0:
            return False
    else:
        return True

def say_hi(*names, greeting='Hello', capitalized=False):
    """
    Print a string, with a greeting to everyone.
    :param *names: tuple of names to be greeted.
    :param greeting: 'Hello' as default.
    :param capitalized: Whether name should be converted to capitalzed before print. False as default.
    :returns: None
    """
    for name in names:
        if capitalized:
            name = name.capitalize()
        print(f'{greeting}, {name}!')




# age = input('Please tell me your age: ')
# if age < 18:
#     print('I can not sell you drinks...')
# else:
#     print('Have a nice drink!')



# print('Example of str.find():')
# s = """Simple is better than complex.
# Complex is better than complicated."""
# s.lower().find('mpl')
# s.lower().find('mpl', 10)
# s.lower().find('mpl', 10, 20) # 没有找到就返回 -1
# print()


# print('Example of str.rfind():')
# # str.rfind(sub[, start[, end]])
# # rfind() 返回最后 sub 出现的那次的位置；find()是最早的那次
# s.lower().rfind('mpl')
# s.lower().rfind('mpl', 10)
# s.lower().rfind('mpl', 10, 20) # 没有找到就返回 -1
# print()

# print('Example of str.index():')
# # str.index(sub[, start[, end]])
# # 作用与 find() 相同，但如果没找到的话，会触发 ValueError 异常
# # https://docs.python.org/3/library/exceptions.html#ValueError
# s.lower().index('mpl')
# # str.rindex(sub[, start[, end]])
# # 作用与 rfind() 相同，但如果没找到的话，会触发 ValueError 异常
# s.lower().rindex('mpl')
# print()

# print([chr(92), chr(923), chr(94), chr(95)])
