date, item, price =['December 23, 2015', 'Bread Gloves', 8.51]

def drop(grades):
    first , *middle, last = grades
    avg = sum(middle) / len(middle)

    return middle

print(drop([83,69,69,60,69,83]))