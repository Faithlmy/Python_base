

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

    # all
    print(all(''), '\n',
          all(' '), '\n',
          all('0'), '\n',
          all([]), '\n',
          all(""""""), '\n',
          all(()), '\n',

          all([0]), '\n',
          all(('0')), '\n',
          'one (' ') is: ', all(('')), '\n',
          'more () is: ', all(('', '')), '\n',


          )

if __name__=='__main__':
    faith_a()
    pass