#!/usr/bin/env python3
"""Day 5 code-along: Recall & Practice. Run: python3 <file> or ./<file>"""

# Example of Nested for loop 
       # c1 c2. c1 2 c1 c2
grid = [[1,2], [3,4],[5,6]]
total = 0
                        #print(grid)
for row in grid:
    for value in row:
        if value % 2 == 0: 
            total += value
print(total)

# Create a funtion that caluculates the area using the following : area(3,4)

def area(h,w):
    return h * w

print(area(3,4))
print(area(9,6))

# ===== 1. Loop + Conditional + Function, Together =====
# Count how many scores pass a threshold of 70. Here the answer is 3.
print('----- 1. Loop + Conditional + Function, Together -----')
# TODO: define count_passing(scores, threshold)
# TODO: return how many scores are >= threshold

#scores=[]



def counting_passing(scores, threshold):
    count = 0
    for val in scores: 
        if val >=  threshold: 
            count += 1 
    return count

# TODO: call it with [55, 82, 91, 40, 76] and 70; print the result
print(counting_passing([55, 82, 91, 40, 76],70))


def set_total():
    total = 100
print(total)


## in class example 


def count_long_shifts(hours):
    count = 0
    for h in hours:
        if h >= 4:
            count += 1
        return count
print(count_long_shifts([3, 4, 6, 2, 5]))

"f{name}"
print(name)