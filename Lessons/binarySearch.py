from jovian.pythondsa import evaluate_test_case
from jovian.pythondsa import evaluate_test_cases

# first test case
test = {'input': {'cards': [9, 8, 3, 2, 1], 'query': 2}, 'output': 3}

# list of test cases
tests = [{'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 7}, 'output': 3},
         {'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0],
                    'query': 1}, 'output': 6},
         {'input': {'cards': [3, -1, -9, -127], 'query': -127}, 'output': 3},
         {'input': {'cards': [6], 'query': 6}, 'output': 0},
         {'input': {'cards': [9, 7, 5, 2, -9], 'query': 4}, 'output': -1},
         {'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], 'query': 3},
          'output': 7},
         {'input': {'cards': [], 'query': 7}, 'output': -1},
         {'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], 'query': 3},
          'output': 7},
         {'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
                    'query': 6},
          'output': 2}]

# helper function
def testLocation(cards, query, mid):
    midNumber = cards[mid]
    print("mid:", mid, ", mid_number:", midNumber)
    if (query == midNumber):
        if mid - 1 >= 0 and cards[mid - 1] == query:
            return 'left'
        else:
            return 'found'
    elif (query > midNumber):
        return 'left'
    else:
        return 'right'

def locateCard(cards, query):   # linear search method (brute-force/simplest solution)

    # 1. Create a variable `position` with the value 0.
    position = 0

    print('cards:', cards)
    print('queury:', query)

    while position < len(cards):
        print('position:', position)
        # 3. Check whether the number at index `position` in `card` equals `query`.
        if cards[position] == query:

            # 4. If it does, `position` is the answer and can be returned from the function
            return position

        # 5. If not, increment the value of `position` by 1, and repeat steps 2 to 5 till we reach the last position.
        position += 1

    # 6. If the number was not found, return `-1`.
    return -1


def locateCardBS(cards, query):     # binary search method (optimized)

    low, high = 0, len(cards) - 1

    while low <= high:
        # 1. Find middle element of the list
        mid = round((low + high) / 2)
        result = testLocation(cards, query, mid)
        print("low:", low, ", high:", high,
              ", mid:", mid, ", midnumber:", cards[mid])

        # 2. if middle element matches the query, return middle element
        if (result == 'found'):
            return mid
        # 3. if the middle element is less than queury, repeat steps 1 and 2 on the right half.
        elif (result == 'left'):
            # high becomes the mid position minus 1
            high = mid - 1
        # 4. if the middle element is greater than the queury, repeat steps 1 and 2 on the left half.
        elif (result == 'right'):
            # low becomes mid position plus 1
            low = mid + 1

    # 5. if no more cards, return -1.
    return -1

def locateCard_BSrecursive(cards, query):

    low, high = 0, len(cards) - 1   

    # wrapped in inner function in order for outer function to just take 2 parameters
    def binarySearchRecursive(cards, query, low, high):

        if (low <= high):
        
            # 1. Find middle element of the list
            mid = (low + high) // 2
            result = testLocation(cards, query, mid)
            
            # 2. base case - if middle element matches the query, return middle element
            if (result == 'found'):
                return mid

            # 3. if the middle element is less than queury, repeat steps 1 and 2 on the right half.
            elif (result == 'left'):
                print('left')
                return binarySearchRecursive(cards, query, low, mid - 1)
            
            # 4. if the middle element is greater than the queury, repeat steps 1 and 2 on the left half.
            elif (result == 'right'):
                print('right')
                return binarySearchRecursive(cards, query, mid + 1, high)
            
        # 5. if no more cards, return -1.
        return -1

    return binarySearchRecursive(cards, query, low, high)

if __name__ == "__main__":
    
    # linear
    # evaluate_test_cases(locateCard, tests)                

    # binary search loop
    # evaluate_test_cases(locateCardBS, tests)              

    # binary search recursive
    # evaluate_test_case(locateCard_BSrecursive, test)
    evaluate_test_cases(locateCard_BSrecursive, tests)


# https://jovian.ai/jtsang02/python-binary-search
