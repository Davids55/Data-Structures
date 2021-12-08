
stack = [1, 2, 3, 4, 5]

new_stack = []

while len(stack) != 0:
    new = stack.pop()
    new_stack.append(new)

print(new_stack)
