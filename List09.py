def main(fruits):
    l=[]
    l.append(fruits.count('apple'))
    i=0
    while i<len(fruits):
        if fruits[i]=="apple":
            l.append(i)
        i+=1
    return l
print(main(["apple", "banana", "apple", "pear", "apple"]))