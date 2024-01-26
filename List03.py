def main(fruits1, fruits2):
    fruits1.extend(fruits2)
    return fruits1
print(main( ["apple", "banana"],["kiwi", "pear"]))
