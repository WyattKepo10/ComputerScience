# NOTE I am working with Ryan on this assignment.

# Sample unsorted list
numbers = [34, 7, 23, 32, 5, 62]

print(numbers)

def bubble_sort(n):
    # Implement bubble sort using for loops
    steps = 0
    for i in range(0, len(n)-1):

        for i in range(0, len(n)-1):
            if n[i] > n[i + 1]:

                n[i], n[i + 1] = n[i + 1], n[i]


            steps += 1
            
    print(n)

    print(str(steps) + " steps to complete.")

bubble_sort(numbers)

def quick_sort(n):
    steps = 0

    for i in range()