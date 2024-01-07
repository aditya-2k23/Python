def print_all_numbers_then_all_pair_sums(numbers):
    print("these are the numbers:")
    for number in numbers:
        print(number)

    print("and these are their sums:")
    for i in numbers:
        for j in numbers:
            print(i + j)


x = [1, 2, 3, 4, 5]
print_all_numbers_then_all_pair_sums(x)
