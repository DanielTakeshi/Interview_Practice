
def twoSum(nums, target):
    """Sorry, misunderstood the question. :-(
    """
    table = {}
    for nidx,n in enumerate(nums):
        if n in table:
            table[n].append(nidx)
        else:
            table[n] = [nidx]
    for nidx,n in enumerate(nums):
        # cannot assume the *same index* (but it can be the same *number*)
        # This also means there can't be any length three or greater lists.
        second_num = target - n
        if second_num in table:
            other_idx = table[second_num][0]
            # only applies with the a special case
            if len(table[second_num]) == 2 and other_idx == nidx:
                other_idx = table[second_num][1]
            return [nidx, other_idx]
    # we should never arrive here if the problem assumptions are correct
    raise ValueError("nums: {}, target: {}".format(nums, target))


def longestPalindrome(s):
    """
    EDIT: argh, doesn't work ... please fix this solution!
    Honestly the indexing is driving me nuts. PLEASE KEEP A FIXED INDEXING CONVENTION.
    For this problem, it is easier if we make pal[i,j] to be INCLUSIVE on both ends.

    Faster dynamic programming solution.
    s: string
    """
    if len(s) == 0:
        return ""
    if len(s) == 1:
        return s[0]
    # But we may end up with length 1 palindromes later!
    longest_len = 1
    longest_sol = s[0]

    pal = {}

    # First base case.
    for i in range(0, len(s)-1):
        pal[(i,i+1)] = True

    # Second base case.
    for i in range(0, len(s)-2):
        pal[(i,i+2)] = s[i]==s[i+1]
        if pal[(i,i+2)] and longest_len != 2:
            longest_len = 2
            longest_sol = s[i:i+2]

    # For all three or longer palindromes.
    for plen in range(3, len(s)+1):
        for i in range(0, len(s)-plen+1):
            j = i+plen
            pal[(i,j)] = pal[(i+1,j-1)] and s[i]==s[j-1]
            if pal[(i,j)] and j-i > longest_len:
                longest_len = j-i
                longest_sol = s[i:j]

    for i in range(len(s)):
        for j in range(i+1, len(s)):
            print(i, j, pal[(i,j)])
    return longest_sol


# Problem 0011
def maxArea(height):
    # Ah, time limit exceeded :-)
    """
    max_area = -1
    for i in range(len(height)):
        for j in range(i+1, len(height)):
            area = (j-i) * min(height[i], height[j])
            max_area = max(max_area, area)
    return max_area
    """
    l = 0
    r = len(height)-1
    max_area = (r - l) * min(height[l], height[r])

    while l < r:
        new_left = l+1
        while new_left < r:
            if height[new_left] > height[l]:
                break
            new_left += 1

        new_right = r-1
        while new_right > new_left:
            if height[new_right] > height[r]:
                break
            new_right -= 1

        if new_left >= new_right:
            break

        # Three areas to consider.
        new_1 = (r - new_left)         * min(height[r],         height[new_left])
        new_2 = (new_right - l)        * min(height[new_right], height[l])
        new_3 = (new_right - new_left) * min(height[new_right], height[new_left])

        if new_1 > new_2 and new_1 > new_3 and new_1 > max_area:
            max_area = new_1
            l = new_left
        elif new_2 > new_1 and new_2 > new_3 and new_2 > max_area:
            max_area = new_2
            r = new_right
        elif new_3 > new_1 and new_3 > new_2 and new_3 > max_area:
            max_area = new_3
            l = new_left
            r = new_right
        else:
            l = l+1

    return max_area


def longestCommonPrefix(strs):
    """Problem 014. Naive solution.

    M = longest string length.
    N = number of items in the list.

    I think it's O(M^2 * N) time, O(M) space. The while loop effectively
    iterates through characters which we select from the prefix length.
    Then we do an O(N) iteration over strings, and the O(M) comparison among
    candidate and the string up until the length of the candidate.

    I suppose a trie could be faster, I guess?

    OH, a really easy and dumb way to fix the time complexity is to avoid doing
    full comparisons but just do single character comparisons. Ah ... that
    would bring it to O(M * N) because within the for loop over strings, I can
    only check the last relevant indices. Why do the earlier ones if we already
    know that it is OK?
    """
    # Handle some base cases.
    prefix = ""
    if len(strs) == 0:
        return prefix

    first_str = strs[0]
    done = False
    while not done:
        if len(first_str) <= len(prefix):
            break
        candidate = prefix + first_str[len(prefix)]
        for s in strs:
            if len(s) < len(candidate) or candidate != s[:len(candidate)]:
                done = True
                break
        if not done:
            prefix = candidate
    return prefix


# Problem 20 -- this is slow but I think because I actually made my own stack
# structure instead of using a simple list that we could use?
class Stack:
    def __init__(self):
        self.data = []

    def pop(self):
        last = self.data[-1]
        self.data = self.data[:-1]
        return last

    def push(self, item):
        self.data.append(item)

    def length(self):
        return len(self.data)

# Problem 20 - GAH DON'T FORGET it is stack.length(), NOT stack.length !!
# Also next time just develop a hash map for the different char types.
def isValid(s):
    stack = Stack()
    for char in s:
        if char in ['(', '{', '[']:
            stack.push(char)
        else:
            if stack.length() == 0:
                return False
            item = stack.pop()
            if char == ')' and item != '(':
                return False
            if char == ']' and item != '[':
                return False
            if char == '}' and item != '{':
                return False
    return stack.length() == 0


if __name__ == "__main__":
    if False:
        print('\n\nPROBLEM 0001 twoSum\n\n')
        print(twoSum(nums=[3,3], target=6))
        print(twoSum(nums=[1,3,3], target=6))

    if False:
        print('\n\nPROBLEM 0005 longestPalindrome\n\n')
        print(longestPalindrome('babad'))
        print(longestPalindrome('cbbd'))
        print(longestPalindrome('ccccc'))
        print(longestPalindrome('cccccc'))

    if False:
        print('\n\nPROBLEM 0011 maxArea\n\n')
        print(maxArea([1,8,6,2,5,4,8,3,7]))
        print(maxArea([1,8,6,2,5,4,8,3,7,1]))
        print(maxArea([1,8,6,2,5,4,8,3,7,19]))
        print(maxArea([1,3,5,1]))
        print(maxArea([1,4,5,1]))

    if False:
        print('\n\nPROBLEM 0014 longestCommonPrefix\n\n')
        print('prefix: {}'.format(longestCommonPrefix(['flower', 'flow', 'flight'])))
        print('prefix: {}'.format(longestCommonPrefix(['dog', 'racecar', 'car'])))
        print('prefix: {}'.format(longestCommonPrefix(['', 'racecar', 'car'])))
        print('prefix: {}'.format(longestCommonPrefix([''])))
        print('prefix: {}'.format(longestCommonPrefix([])))
        print('prefix: {}'.format(longestCommonPrefix(['flower', 'flow', 'flowht'])))

    if False:
        print('\n\nPROBLEM 0020 isValid\n\n')
        print(isValid('()'))
