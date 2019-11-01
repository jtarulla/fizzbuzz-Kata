class FizzBuzz(object):
    def __init__(self, value):
        if FizzBuzz.is_valid_number(value):
            self.value = value

    @property 
    def result(self):
        if self._is_divisible_by(3,5):
            return 'FizzBuzz'
        if self._is_divisible_by(3):
            return 'Fizz'
        if self._is_divisible_by(5):
            return 'Buzz'
        return self.value

    def _is_divisible_by(self, first_divisor, second_divisor=None):
        if second_divisor is not None and \
                self.value % first_divisor == 0:
            return self.value % second_divisor == 0
        return self.value % first_divisor == 0

    # the solution that I've checked uses staticmethod, why?
    #@staticmethod
    def is_valid_number(value):
        if value <= 0 or value > 100:
            raise ValueError('Number must be between 0 and 100.')
        return True

