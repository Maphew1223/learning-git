numbers = list(range(101))
div = [number for number in numbers if number % 5 == 0]
print(div)
cube = [number * number * number for number in div]
print(cube)