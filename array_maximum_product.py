def maxProduct(nums):
    if not nums:
        return 0
        
    max_product = nums[0]
    min_product = nums[0]
    result = nums[0]
    
    for i in range(1, len(nums)):
        if nums[i] < 0:
            max_product, min_product = min_product, max_product
        
        max_product = max(nums[i], max_product * nums[i])
        min_product = min(nums[i], min_product * nums[i])
        
        result = max(result, max_product)
        
    return result

nums = [-2,3,5,-2,-4]
sumon = maxProduct(nums)
print(sumon)

