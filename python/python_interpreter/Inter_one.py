

class Interpreter:
    def __init__(self):
        self.stack = []

    def LOAD_VALUE(self, number):
        self.stack.append(number)

    def PRINT_ANSWER(self):
        answer = self.stack.pop()
        print(answer)

    def ADD_TWO_VALUE(self):
        first_num = self.stack.pop()
        second_num = self.stack.pop()
        toatal = first_num + second_num
        self.stack.append(toatal)

    def run_code(self, what_to_execute):
        instructions = what_to_execute['instructions']
        numbers = what_to_execute['numbers']
        for each_step in instructions:
            instructions, argument = each_step
            if instructions == "LOAD_VALUE":
                number = numbers[argument]
                self.LOAD_VALUE(number)
            elif instructions == "ADD_TWO_VALUES":
                self.ADD_TWO_VALUE()
            elif instructions == "PRINT_ANSWER":
                self.PRINT_ANSWER()


if __name__ == '__main__':
    what_to_execute = {
        "instructions": [("LOAD_VALUE", 0),  # the first number
                         ("LOAD_VALUE", 1),  # the second number
                         ("ADD_TWO_VALUES", None),
                         ("PRINT_ANSWER", None)],
        "numbers": [7, 5]}
    interpreter = Interpreter()
    interpreter.run_code(what_to_execute)
