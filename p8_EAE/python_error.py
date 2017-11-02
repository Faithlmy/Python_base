"""=== Errors  and  Exceptions ==="""

"""=== Syntax Errors ==="""

"""=== Exceptions ==="""
#whlie True print('hello')#SyntaxError : invalid syntax
#while True:print('hello')#endless loop

# while True:
#     try:
#         x = int(input('please enter a number:'))
#         break
#     except ValueError:
#         print('please input a integer number')


# import sys
#
# try:
#     f = open('myfile.txt')
#     s = f.readline()
#     i = int(s.strip())
# except OSError as err:
#     print("OS error: {0}".format(err))
# except ValueError:
#     print("Could not convert data to an integer.")
# except:
#     print("Unexpected error:", sys.exc_info()[0])
#     raise


# import  sys
# for arg in sys.argv[1:]:
#     try:
#         f = open(arg, 'r')
#     except OSError:
#         print('cannot open', arg)
#     else:
#         print(arg, 'has', len(f.readlines()), 'lines')
#         f.close()



def z():
    x = 1/0

try:
    z()
except ZeroDivisionError as error:
    print(error)
