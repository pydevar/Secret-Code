class Checker(object):

    def __init__(self, secret_code):
        self.secret_code = secret_code

    def check_code(self, code):
        red, yellow = self.check_red(code), abs(self.check_red(code) - self.check_yellow(code))
        return red, yellow

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
