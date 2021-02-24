text = input('What you write : ')
x = "a"
y = "b"
if  text.replace(" ","").title() == 'Yes':
    if  x:
        print('You entered True')
    else:
        print('You entered False')
else:
    if  y:
        print('You entered True')
    else:
        print('You entered False')