# Sum of natural numbers

def func(n):
    iteration = 0
    result = n * (n + 1) / 2
    iteration += 1
    print(f"For input size {n}, iteration is: {iteration}")
    return result

print(func(5))
print(func(500))

# Constant Time complexity: O(1)
