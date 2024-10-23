def find_min(nums):
    # TODO: implement the function to find the minimum number from a list
    number_min = None
    def search_min(nums, number_min):
        if len(nums) <= 0:
            return number_min
            
        if number_min != None and number_min > nums[0]:
            number_min = nums[0]
            
        elif number_min == None:
            number_min = nums[0]
               
        
        return search_min(nums[1:], number_min)
    return search_min(nums, number_min)
data_muns = [8,5,8,3]
print(find_min(data_muns))