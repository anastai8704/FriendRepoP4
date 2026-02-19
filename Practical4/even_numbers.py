evens = [i for i in range(1, 51) if i % 2 == 0]

print("Even numbers (1 to 50):")
print(evens)
print("Three minimum even numbers:", evens[:3])
print("Three maximum even numbers:", evens[-3:])
print("Average of even numbers:", sum(evens)/len(evens))
