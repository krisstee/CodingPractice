# This program looks for multiples of three and five from the natural numbers list [1,1000)
# and outputs the sum

n = 999
additional_sum = 0
# Solve for the max number as 990 (the highest number that is mutliple
# of both 3 and 5)

# Assuming we don't know the GCM, solve for it
for i in range(n,0,-1):
    if i % 3 == 0 and i % 5 == 0:
        gcm = i
        break
    if i % 3 == 0:
        additional_sum += i
    if i % 5 == 0:
        additional_sum += i


# Get the number of the multiples of 3 from [1,990]
multiples_of_three = gcm / 3
# Get the sum of the multiples of 3
# Given by the formula: (multiples_of_three(gcm + 3)) / 2
sum_of_three = (multiples_of_three * (gcm + 3)) / 2

# Do the same process for multiples of five
multiples_of_five = gcm / 5
sum_of_five = (multiples_of_five * (gcm + 5)) / 2

# Rule out the multiples of 15 (the LCM of 3 and 5)
multiples_of_fifteen = gcm / 15
sum_of_fifteen = (multiples_of_fifteen * (gcm + 15)) / 2

# Return the total sum
result = additional_sum + sum_of_three + sum_of_five - sum_of_fifteen
print(result)
