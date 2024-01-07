def print_first_item_then_first_half_then_say_hi_100_times(items):
    print(items[0])

    middle_index = len(items) // 2
    index = 0
    while index < middle_index:
        print(items[index])
        index += 1

    for _ in range(100):
        print("hi")


x = input("Enter the numbers: ").split(" ")
print_first_item_then_first_half_then_say_hi_100_times(x)
