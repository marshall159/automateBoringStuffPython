# Comma Code Project
'''Say you have a list value like this:
spam = ['apples', 'bananas', 'tofu', 'cats']
Write a function that takes a list value as an argument and returns a string
with all the items separated by a comma and a space, with 'and' inserted before the last item.
For example, passing the previous spam list to the function would return
'apples, bananas, tofu, and cats'.
But your function should be able to work with any list value passed to it.

spam = ['apples', 'bananas', 'tofu', 'cats']
'''

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

# Comma Code Project v2

def commaCode(list):
    '''
    (list) -> str

    Return items of a list as a string with all items separated by a comma
    and a space, with 'and' inserted before the last item.

    >>> commaCode(['apples', 'bananas', 'tofu', 'cats'])
    'apples, bananas, tofu, and cats'
    >>> commaCode(['one', 'two', 'three'])
    'one, two and three'
    '''

    s = ''
    for i in range(len(list)):
        if i == len(list) - 1:
            s += 'and ' + list[i]
        else:
            s += list[i] + ', '
    print(s)

spam = ['apples', 'bananas', 'tofu', 'cats']
commaCode(spam)


# Character Picture Grid Project
'''Say you have a list of lists where each value in the inner lists
is a one-character string, like this:


grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]
        
You can think of grid[x][y] as being the character at the x- and y-coordinates
of a “picture” drawn with text characters. The (0, 0) origin will be in the
upper-left corner, the x-coordinates increase going right, and the y-coordinates
increase going down.

Copy the previous grid value, and write code that uses it to print the image.


..OO.OO..
.OOOOOOO.
.OOOOOOO.
..OOOOO..
...OOO...
....O....

Hint: You will need to use a loop in a loop in order to print grid[0][0], then
grid[1][0], then grid[2][0], and so on, up to grid[8][0]. This will finish the
first row, so then print a newline. Then your program should print grid[0][1],
then grid[1][1], then grid[2][1], and so on. The last thing your program will
print is grid[8][5].

Also, remember to pass the end keyword argument to print() if you don’t want a
newline printed automatically after each print() call.
'''

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]


for i in range(len(grid[0])):
    print()
    for j in range(len(grid)):
        print(grid[j][i], end = '')
    
        


        



