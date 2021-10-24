import time

def bubble_sort(numbers):
    iterations = 0
    for i in range(len(numbers)):
        for x in range(len(numbers) - 1):
            if numbers[x] >= numbers[x+1]:
                numbers[x], numbers[x+1] = numbers[x+1], numbers[x]
                iterations += 1
    
    return numbers,iterations





nums = [89, 80, 30, 43, 34, 58, 40, 5]
list, iter = bubble_sort(nums)
print(f"Original List = {nums}: \n  Bubble Sort list: {list} \n     Iterations:{iter}")

