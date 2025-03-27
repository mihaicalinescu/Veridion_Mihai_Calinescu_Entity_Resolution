my_list = [1, 2, 3]
my_list = ['STRING',100,23.2]
print (len(my_list))

new_list = ['a', 'e', 'x', 'b', 'c']
num_list = [4,1,8,3]


# new_list.sort()
sorted_list = new_list.sort()
print(sorted_list)
# nu poti salva asa o functie sortata, este de tip None, dar poti asa

new_list.sort()
my_sorted_list = new_list
print(my_sorted_list, new_list)

num_list.reverse()
print(num_list)

def filter_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]

numbers = [1, 2, 3, 4, 5, 6]
