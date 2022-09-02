from jovian.pythondsa import evaluate_test_cases

tests2 = []

# case 0
tests2.append({
    # add your test case here
    'input': {
        'nums': [4, 5, 6, 7, 0, 1, 2],
        'target': 0
    },
    'output': 4
})

# case 1
tests2.append({
    # add your test case here
    'input': {
        'nums': [4, 5, 6, 7, 0, 1, 2],
        'target': 3
    },
    'output': -1
})

# case 2
tests2.append({
    # add your test case here
    'input': {
        'nums': [1],
        'target': 0
    },
    'output': -1
})

# case 3
tests2.append({
    # add your test case here
    'input': {
        'nums': [1],
        'target': 1
    },
    'output': 0
})

# case 4
tests2.append({
    # add your test case here
    'input': {
        'nums': [],
        'target': 1
    },
    'output': -1
})

# case 5
tests2.append({
    # add your test case here
    'input': {
        'nums': [1, 3],
        'target': 1
    },
    'output': 0
})


def find_element(nums, target):

    # generic binary search algorithm
    def binary_search(low, high, condition):
        while (low <= high):
            mid = (low + high) // 2
            result = condition(mid)
            if (result == 'found'):
                return mid
            elif (result == 'left'):
                high = mid - 1
            else:
                low = mid + 1
        return -1

    # logic to find pivot
    def findPivotCondition(mid):
        if (mid > 0 and nums[mid] < nums[mid - 1]):
            return 'found'
        elif (nums[mid] < nums[0]):
            return 'left'
        else:
            return 'right'

    # logic to search target in ascending sorted list
    def findTargetCondition(mid):          
        if (nums[mid] == target):
            return 'found'
        elif (nums[mid] > target):
            return 'left'
        else:
            return 'right'

    # get mid index to get pivot value
    low, high = 0, len(nums) - 1
    pivot = binary_search(low, high, findPivotCondition)
    print(pivot)

    # if no pivot found, do binary search on whole array
    if (pivot == -1):
        return binary_search(low, high, findTargetCondition)

    # if pivot found, compare with target
    if (nums[pivot] == target):
        return pivot

    # split list into L and R of the pivot to get 2 sorted list

    # if target is smaller than first value in list, search the second sorted half
    if (nums[0] > target):
        print ("search rightNums:", nums[pivot:], "low: ", pivot, " high:", high) 
        return binary_search(pivot, high, findTargetCondition)
    # if target is greater or equal to first value in list, search first half
    else:
        print ("search leftNums:", nums[:pivot], "low: ", low, " high:", pivot) 
        return binary_search(low, pivot, findTargetCondition)

if __name__ == "__main__":
    find_element([1, 2, 3, 4, 5, 2, 3, 4], 2)
    evaluate_test_cases(find_element, tests2)
