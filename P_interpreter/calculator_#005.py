# calculator v5

INTEGER, PLUS, MINUS, DIV, MUL, EOF = ('INTEGER', 'PLUS', 'MINUS', 'DIV', 'MUL', 'EOF')


class Token(object):
    def __init__(self, t_ype, value):
        self.t_ype = t_ype
        self.value = value

    def __str__(self):
        return 'Token({t_ype}, {value})'.format(t_ype=self.t_ype, value=self.value)

    def __repr__(self):
        return self.__str__()


class Lexer(object):
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos]

    def error(self):
        raise Exception('Invalid character.')

    def advance(self):
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]

    def skip_space(self):
        if self.current_char is not None and self.current_char.isspace():
            self.advance()

    def integer(self):
        result = ''
        if self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
            return int(result)

    def get_next_token(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_space()
                continue
            if self.current_char.isdigit():
                return Token(INTEGER, self.integer())
            if self.current_char == '+':
                self.advance()
                return Token(PLUS, '+')
            if self.current_char == '-':
                self.advance()
                return Token(MINUS, '-')
            if self.current_char == '*':
                self.advance()
                return Token(MUL, '*')
            if self.current_char == '/':
                self.advance()
                return Token(DIV, '/')
            self.error()

        return Token(EOF, None)


class Interpreter(object):
    def __init__(self, text):
        self.text = text
        self.current_token = self.text.get_next_token()

    def error(self):
        raise Exception('Invalid syntax.')

    def eat(self, token_type):
        if self.current_token.t_ype == token_type:
            self.current_token = self.text.get_next_token()
        else:
            self.error()

    def factor(self):
        token = self.current_token
        self.eat(INTEGER)
        return token.value

    def term(self):
        """term : factor ((MUL | DIV) factor)*"""
        result = self.factor()

        while self.current_token.t_ype in (MUL, DIV):
            token = self.current_token
            if token.t_ype == MUL:
                self.eat(MUL)
                result = result * self.factor()
            elif token.t_ype == DIV:
                self.eat(DIV)
                result = result / self.factor()

        return result

    def expr(self):
        """Arithmetic expression parser / interpreter.

        calc>  14 + 2 * 3 - 6 / 2
        17

        expr   : term ((PLUS | MINUS) term)*
        term   : factor ((MUL | DIV) factor)*
        factor : INTEGER
        """
        result = self.term()

        while self.current_token.t_ype in (PLUS, MINUS):
            token = self.current_token
            if token.t_ype == PLUS:
                self.eat(PLUS)
                result = result + self.term()
            elif token.t_ype == MINUS:
                self.eat(MINUS)
                result = result - self.term()

        return result


def main():
    while True:
        try:
            # To run under Python3 replace 'raw_input' call
            # with 'input'
            text = input('calc> ')
        except EOFError:
            break
        if not text:
            continue
        lexer = Lexer(text)
        interpreter = Interpreter(lexer)
        result = interpreter.expr()
        print(result)


if __name__ == '__main__':
    main()
