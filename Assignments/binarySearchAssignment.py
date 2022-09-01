from jovian.pythondsa import evaluate_test_case

test = {
    'input': {
        'nums': [19, 25, 29, 3, 5, 6, 7, 9, 11, 14]
    },
    'output': 3
}


def count_rotations_binary(nums):
    
    lo, hi = 0 , len(nums) - 1
    
    while (lo <= hi):

        mid = (lo + hi) // 2
        mid_number = nums[mid]
        
        # Uncomment the next line for logging the values and fixing errors.
        print("lo:", lo, ", hi:", hi, ", mid:", mid, ", mid_number:", mid_number)
        
        if (mid > 0 and mid_number < nums[mid-1]):   # The middle position is the answer
            return mid

        elif (mid_number < nums[hi]):                       # Answer lies in the left half
            hi = mid - 1

        else:                                        # Answer lies in the right half
            lo = mid + 1
    
    return 0

if __name__ == "__main__":
    evaluate_test_case(count_rotations_binary, test)