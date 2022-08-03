def quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers
    else:
        pivot = numbers[0]
        smaller_nums = [i for i in numbers[1:] if i <= pivot]
        bigger_nums =  [i for i in numbers[1:] if i > pivot]
        return quick_sort(smaller_nums) + [pivot] + quick_sort(bigger_nums)
