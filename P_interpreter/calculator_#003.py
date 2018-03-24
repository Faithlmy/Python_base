# calculator v3.0
# Token type

INTEGER, PLUS, MINUS, EOF = 'INTEGER', 'PLUS', 'MINUS', 'EOF'


class Token(object):
    def __init__(self, t_ype, value):
        """
        :param t_ype: INTEGER, PLUS, MINUS, EOF
        :param value: 1, 2, 3, 4, 5, 6, 7, 8, 9, + , -, or None
        """
        self.t_ype = t_ype
        self.value = value

    def __str__(self):
        """
        :return:
        """
        return 'Token({t_ype}, {value})'.format(
            t_ype=self.t_ype,
            value=repr(self.value)
        )

    def __repr__(self):
        """
        :return:
        """
        return self.__str__()


class Interpreter(object):
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_token = None
        # current token instance
        self.current_char = self.text[self.pos]

    def error(self):
        raise Exception('Error parsing input.')

    def advance(self):
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]

    def skip_space(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def integer(self):
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)

    def get_next_token(self):
        """
        This method is responsible for breaking a sentence apart into token
        :return:
        """
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
            self.error()
        return Token(EOF, None)

    def eat(self, token_type):
        if self.current_token.t_ype == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()

    def term(self):
        token = self.current_token
        self.eat(INTEGER)
        return token.value

    def expr(self):
        self.current_token = self.get_next_token()

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
        # left = self.current_token
        # self.eat(INTEGER)
        #
        # op = self.current_token
        # # self.eat(PLUS)
        # if op.t_ype == PLUS:
        #     self.eat(PLUS)
        # else:
        #     self.eat(MINUS)
        #
        # right = self.current_token
        # self.eat(INTEGER)
        #
        # # result = left.value + right.value
        # if op.t_ype == PLUS:
        #     result = left.value + right.value
        # else:
        #     result = left.value - right.value
        # return result


def main():
    while True:
        try:
            text = input('cal> ')
        except EOFError:
            break

        if not text:
            continue

        interpreter = Interpreter(text)
        result = interpreter.expr()
        print(result)


if __name__ == '__main__':
    main()
