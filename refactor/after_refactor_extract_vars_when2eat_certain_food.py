# after_refactor_extract_vars_when2eat_certain_food.py

MONTHS = ('January', 'February', 'March', 
    'April', 'May', 'June', 'July', 'August',
    'September', 'October', 'November', 'December')

def what_to_eat(month):
    # By extract meaningful variables
    lowered = month.lower()
    ends_in_r = lowered.endswith('r')
    ends_in_ary = lowered.endswith('ary')
    index = MONTHS.index(month)
    summer = 8 > index > 4

    if ends_in_r or ends_in_ary:
        print(f'{month}: oysters')
    elif summer:
        print(f'{month}: tomatoes')
    else:
        print(f'{month}: asparagus')


if __name__ == '__main__':
    what_to_eat('November')
    what_to_eat('July')
    what_to_eat('March')

