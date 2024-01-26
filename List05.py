def main(numbers1, numbers2):
    numbers1.extend(numbers2)
    return numbers1
print(main([6, 8, 1],[3,5,7]))