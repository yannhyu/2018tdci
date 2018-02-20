# after_refactor_extract_vars_when2eat_certain_food.py

MONTHS = ('January', 'February', 'March', 
    'April', 'May', 'June', 'July', 'August',
    'September', 'October', 'November', 'December')

# By extract meaningful objects
class OystersGood:
    def __init__(self, month):
        lowered = month.lower()
        self.r = lowered.endswith('r')
        self.ary = lowered.endswith('ary')
        self._result = self.r or self.ary

    def __bool__(self):
        return self._result

class TomatoesGood:
    def __init__(self, month):
        self.index = MONTHS.index(month)
        self._result = 8 > self.index > 4

    def __bool__(self):
        return self._result


def what_to_eat(month):
    time_for_oysters = OystersGood(month)
    time_for_tomatoes = TomatoesGood(month)
    if time_for_oysters:
        print(f'{month}: oysters')
    elif time_for_tomatoes:
        print(f'{month}: tomatoes')
    else:
        print(f'{month}: asparagus')


if __name__ == '__main__':
    what_to_eat('November')
    what_to_eat('July')
    what_to_eat('March')

