# 7. Python Program to Find the Intersection of Two Lists

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

intersection = []

for item in list1:
    if (item in list2 and item not in intersection):
        intersection.append(item)


print("Intersection of the two lists:", intersection)
