nums = input('введите элементы масива через пробел: ').split()
print(nums) 
for i in range(len(nums)):
    nums[i] = int(nums[i])
    