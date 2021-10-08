import re
from utils.reversed_polish_notation import conv_to_rpn, compute_rpn
from utils.reversed_polish_notation import OPERATORS

HELP_INFO = """This program is created for dealing with simple equations containing brackets, and supports the following operators:
+, -, *, /, %, ^. User can also declare his own variables (e.g. a = 5). Please read about program limitations below to
avoid errors:

- Input need to be typed with INTEGERS, floating point numbers will not work (still, result can be shown as float).
- variable name can contain ONLY letters, and it's case sensitive.
- If you need to use brackets, remember to close them, as without it program may work incorrectly or error may be printed out.
- For raising to power, you need to use '^' operator. Double star (**) won't work.

Use /exit command if you want to close application.

Program created by Beniamin Przychodzki, 2021."""


class Calculator:
    variables = {}

    def __init__(self):
        self.isRunning = True

    @classmethod
    def handle_variables(cls, variable: str):
        variable = variable.split(
            "=", 1
        )  # making sure that multiple value declarations are impossible (a = 2 = 5 etc.)
        if (
            variable[0].isalpha() and variable[1].isdigit()
        ):  # variable is properly added, add it to dictionary
            cls.variables[variable[0]] = variable[1]
        elif (
            variable[0].isalpha() and variable[1] in cls.variables
        ):  # use variable value from previously saved variables
            cls.variables[variable[0]] = cls.variables[variable[1]]
        elif not variable[0].isalpha():  # if variable name is invalid, print an error
            print("Invalid identifier")
        elif not variable[1].isdigit():
            print("Invalid assignment")

    def handle_commands(self, command: str):
        if command == "/exit":
            print("Bye!")
            self.isRunning = False
        elif command == "/help":
            print(HELP_INFO)
        else:
            print("Unknown command")

    def handle_input(self) -> None:
        input_data = self.get_input()
        if input_data.startswith("/"):
            self.handle_commands(input_data)
        elif "=" in input_data:
            self.handle_variables(input_data)
        elif input_data:
            equation_raw = self.replace_variables(input_data)
            if equation_raw:
                equation = self.check_equation(equation_raw)
                if equation:
                    print(compute_rpn(conv_to_rpn(equation)))
                else:
                    print("Invalid expression")
            else:
                print("Unknown variable")

    @staticmethod
    def replace_variables(equation_data: str):
        for key, value in Calculator.variables.items():
            if key in equation_data:  # change variables in string to int values
                equation_data = equation_data.replace(key, value)
        if equation_data[-1] in OPERATORS or re.search(
            "[a-zA-Z]", equation_data
        ):  # search for undefined variables in equation or misplaced operators
            return None
        return equation_data

    @staticmethod
    def check_equation(input_data: str):
        symbols = [
            x
            for x in re.findall(r"[+]+|[-]+|[/]+|[*]+|[\^]+|[%]+|[()]|\d+", input_data)
        ]  # search and seperate operators from digits
        fixed_equation = ""
        for symbol in symbols:
            if symbol.isdigit() or symbol in "()":
                fixed_equation += symbol
            elif (
                symbol[0] in "+-−"
            ):  # if there is more than one plus or minus operator, change it to plus, or keep only one
                if symbol.count(symbol[0]) % 2 == 0:
                    fixed_equation += "+"
                elif symbol.count(symbol[0]) % 2 == 1:
                    fixed_equation += symbol[0]
            elif (
                symbol[0] in "*/^%"
            ):  # if there is more than one operator, raise an error
                if symbol.count(symbol[0]) > 1:
                    return None
                fixed_equation += symbol[0]
        if fixed_equation.count("(") == fixed_equation.count(
            ")"
        ):  # check if all brackets are closed
            return fixed_equation
        return None

    @staticmethod
    def compute(number_list):
        return sum(number_list)

    @staticmethod
    def get_input():
        return input().replace(" ", "")


def main():
    calculator = Calculator()
    while calculator.isRunning:
        calculator.handle_input()


if __name__ == "__main__":
    main()
