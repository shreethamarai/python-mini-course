
try:
    nums = [1,2,3]
    print(nums[2])
    value = int('abc')

except (IndexError, ValueError) as e:
    print("Caught error:", e)
