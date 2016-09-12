class Checker(object):

    NO_GUESS = 0
    POSITION_AND_COLOR = 1
    COLOR = 2
    MAX_LENGTH = 4

    def __init__(self, secret_code):
        self.secret_code = secret_code

    def check_code(self, code):
        red = self.check_red(code)
        yellow = abs(red - self.check_yellow(code))
        return self.format_result(red, yellow)

    def check_red(self, code):
        """
        Check if code is in the same color and position

        :param code: list of 4 elements
        :return: an integer to check for position and color
        """
        result = 0
        for index in range(len(code)):
            if code[index] == self.secret_code[index]:
                result += 1
        return result

    def check_yellow(self, code):
        """
        Check if code is in place and position

        :param code: list of 4 elements
        :return: an integer to check for color
        """
        copy = self.secret_code[:]
        result = 0
        for value in code:
            try:
                copy.remove(value)
                result += 1
            except ValueError:
                pass
        return result

    def format_result(self, position, color):
        result = []
        for i in range(position):
            result.append(self.POSITION_AND_COLOR)
        for i in range (color):
            result.append(self.COLOR)
        current_length = len(result)
        for i in range(self.MAX_LENGTH - current_length):
            result.append(self.NO_GUESS)
        return result