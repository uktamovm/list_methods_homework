def main(fruits):
    i=0
    n=[]
    while i<len(fruits):
        if fruits[i]=='apple':
            fruits.pop(i)
        i+=1


    return fruits
print(main(["apple", "banana", "apple", "pear", "apple"]))
