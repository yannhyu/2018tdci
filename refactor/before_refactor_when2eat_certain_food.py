# before_refactor_when2eat_certain_food.py

MONTHS = ('January', 'February', 'March', 
    'April', 'May', 'June', 'July', 'August',
    'September', 'October', 'November', 'December')

def what_to_eat(month):
    if (month.lower().endswith('r') or
        month.lower().endswith('ary')):
        print(f'{month}: oysters')
    elif 8 > MONTHS.index(month) > 4:
        print(f'{month}: tomatoes')
    else:
        print(f'{month}: asparagus')


if __name__ == '__main__':
    what_to_eat('November')
    what_to_eat('July')
    what_to_eat('March')

