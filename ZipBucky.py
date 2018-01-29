first = ['Ashmin', 'Erika', 'Rebecca', 'Latina']
last = ['Babe', 'Perfect', 'Cutie', 'Chick']

names = zip(first, last)

for a, b  in names:
    print(a, b)


answer =  lambda x: x*7
print(answer(7))

Button(text="Click Me", command=lambda:custom)