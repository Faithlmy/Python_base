

"""
abs()   all()   any()   ascii()
bin()   bool()  bytearray()  bytes()
callable()  chr()   classmethod()   compile()   compliex()
"""
def faith_a():

    # abs
    print(abs(0.9), '\n',
          abs(-0.7), '\n',
          )

    # all ( All of object is not 0, '', false, None , the result is ture )
    print('""is: ', all(''), '\n',
          '" "is: ', all(' '), '\n',
          '0 is: ', all('0'), '\n',
          '[]is: ', all([]), '\n',
          '()is: ', all(()), '\n',
          ' """""" is:  ', all(""""""), '\n',

          '[0] is: ', all([0]), '\n',
          '(0) is: ', all(('0')), '\n',
          'one (' ') is: ', all(('')), '\n',
          'more () is: ', all(('', '')), '\n',

          '[1,3,2]is: ', all([1, 3, 2]), '\n',
          '[1,3,0]is: ', all([1, 3, 0]), '\n',
          '[1,3,""]is: ', all([1, 3, '']), '\n',
          '[1,3," "]is: ', all([1, 3, ' ']), '\n',

          '["a", "b", "c"] is: ', all(['a', 'b', 'c']), '\n',
          '["a", "b", ""] is: ', all(['a', 'b', '']), '\n',
          '["a", "b", " "] is: ', all(['a', 'b', ' ']), '\n',

          '(1,3,2)is: ', all((1, 3, 2)), '\n',
          '(1,3,0)is: ', all((1, 3, 0)), '\n',
          '(0) is: ', all((0,)), '\n',
          '(1,3,"")is: ', all((1, 3, '')), '\n',
          '(1,3," ")is: ', all((1, 3, ' ')), '\n',
          '(1,3, None)is: ', all((1, 3, None)), '\n',

          )

    # any
    print(
        'all[1, 3, 0]is: ', all([1, 3, 0]), '\n',
        'any[1, 3, 0]is: ', any([1, 3, 0]), '\n',

        'all[1, 3, ""]is: ', all([1, 3, '']), '\n',
        'any[1, 3, ""]is: ', any([1, 3, '']), '\n',

        'all[1, 3, ""]is: ', all([1, 3, ' ']), '\n',
        'any[1, 3, ""]is: ', any([1, 3, ' ']), '\n',

        'all(1, 3, "")is: ', all((1, 3, '')), '\n',
        'any(1, 3, "")is: ', any((1, 3, '')), '\n',
        'any(1, 3, "")is: ', any(('', '', '')), '\n',
        'any(1, 3, "")is: ', all(('', '', '')), '\n',
    )

def faith_b():

    # bin
    print(
        'bin(2)is: ', bin(2), '\n',

        'bool(0)is: ', bool(0), '\n',
        'bool(1)is: ', bool(1), '\n',
        'bool(134)is: ', bool(134), '\n',
        'bool("ad")is: ', bool('ad'), '\n',

        'bool(bool([]))is: ', bool([]), '\n',
        'bool(bool(()))is: ', bool(()), '\n',
        'bool(bool(""))is: ', bool(''), '\n',

        'bool(bool([1]))is: ', bool([1]), '\n',
        'bool(bool(("a")))is: ', bool(('a')), '\n',
        'bool(bool("b"))is: ', bool('b'), '\n',
    )

    # bytearray()
    print(
        'bytearray()is: ', bytearray(), '\n',
        # 'bytearray("a")is: ', bytearray('a'), '\n',
        'bytearray(2)is: ', bytearray(2), '\n',
        'bytearray()is: ', bytearray([1, 3, 4]), '\n',
        'bytearray(utf-8)is: ', bytearray('run', 'utf-8'), '\n',
        'bytearray("run",GBK)is: ', bytearray('run', 'gbk'), '\n',
    )

    # bytes()
    print(
        'bytes("run", "utf-8")is :', bytes('run', 'utf-8'), '\n',
        'bytes("和", "utf-8")is :', bytes('和', 'utf-8'), '\n',
        'bytes("run", "utf-8")is :', bytes('run'.encode('utf-8')), '\n',
        'bytes("哈", "utf-8")is :', bytes('哈'.encode('utf-8')), '\n',
        'bytes("哈", "GBK")is :', bytes('哈'.encode('GBK')), '\n',
        'bytes(2)is :', bytes(2), '\n',
        'bytes(12)is :', bytes(12), '\n',
    )
class A:
    pass
    # print(callable(faith_b()))
if __name__=='__main__':
    # faith_a()
    # faith_b()
    callable(A)
    pass