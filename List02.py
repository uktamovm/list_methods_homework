def main(fruits,x,i):
    fruits.insert(i,"kiwi")
    return fruits
print(main(["apple","banana"],"kiwi",1))