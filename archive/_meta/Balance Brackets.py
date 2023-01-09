def isBalanced(s):
    # Write your code here

    if not s:
        return False

    stack = []

    match = {
        '}': '{',
        ')': '(',
        ']': '['
    }

    for char in s:
        if char not in match:
            stack.append(char)
        else:

            if not stack:
                return False

            item = stack.pop()
            if match[char] != item:
                return False

    return not stack


s1 = "{[(])}"

res = isBalanced(s1)

print(res)
