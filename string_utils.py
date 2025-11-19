def split_before_each_uppercases(formula):
    pass # Replace the `pass` with your code


from string import digits
def split_at_first_digit(formula):
    digit_place = None
    for idx , char in enumerate(formula):
        if char.isdigit():
            digit_place = idx
            prefix = formula[:digit_place]
            numrical_part = int(formula[digit_place :])
            break
        else:
            prefix = formula
            numrical_part = 1
    return (prefix , numrical_part)
