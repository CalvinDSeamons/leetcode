# Two Sums python solution. 



# This is a bad O(n^2) solution. 
def bad_two_sums(nums, target): 
    # Nested for-loop comparing i,j over and over again (very bad)
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                print(f"Solution found: {nums[i]} and {nums[j]} makes {target}")
                return i,j
    print("No sum found")
    return None

# This is a good solution O(n)
def good_two_sums(nums, target):
    seen = {} # Create our seen dict.
    for i, num in enumerate(nums):
        needed = target-num # every index we create a needed value. 
        if needed in seen: # If it exists we can exit as we've found two sums.
            print(f"Solution found: {nums[(seen[needed])]} and {nums[(i)]} makes {target}")
            return None
        seen[num] = i # If needed is not there we add a new value to the seen dict. 
    print("No sum found") # If we exit loop no two sum pair was found.
    return None


nums = [1,3,5,7,2,8,11,4]

bad_two_sums(nums, 18)  # results found
bad_two_sums(nums, 67)  # result not found

good_two_sums(nums, 11) # results found
good_two_sums(nums, 22) # result not found
 


