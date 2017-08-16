# Comma Code Project
# Say you have a list value like this:
# spam = ['apples', 'bananas', 'tofu', 'cats']
# Write a function that takes a list value as an argument and returns a string
# with all the items separated by a comma and a space, with 'and' inserted before the last item.
# For example, passing the previous spam list to the function would return
# 'apples, bananas, tofu, and cats'.
# But your function should be able to work with any list value passed to it.

spam = ['apples', 'bananas', 'tofu', 'cats']

def comma(list):
    '''(list) -> str

    Returns a str with all items in the list joined up with 'and'
    before the last item

    >>> spam = ['apples', 'bananas', 'tofu', 'cats']
    >>> comma(spam)
    'apples, bananas, tofu, and cats'
    '''

    start = list[:len(list) -1]
    end = list[-1]
    s = ''
    for item in start:
        s += str(item) + ', '
    return s + 'and ' + str(end)
    

