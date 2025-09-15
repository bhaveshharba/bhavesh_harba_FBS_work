# 4. Write a Python program that finds all pairs of elements in a list whose
# sum is equal to a given value.

li= [2, 4, 3, 5, 7, 8, -1]
target_sum = 7

pairs = []

for i in range(len(li)):
    for j in range(i + 1, len(li)):
        if li[i] + li[j] == target_sum:
            pairs.append((li[i], li[j]))

print("Pairs with sum equal to", target_sum, "are:", pairs)
