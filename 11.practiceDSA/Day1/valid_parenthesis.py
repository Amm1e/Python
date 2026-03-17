#s='({[]})'

def valid_paranthesis(String:s):
    pair ={")":"(", "}":"{","]":"["}
    stack= []
    for char in s:
        if char in "{[(":
            stack.append(char)
        elif char in ")}]":
            if stack and stack[-1] == pair[char]:
                stack.pop()
            else:
                return False
    return len(stack) == 0

s = "({[})"
print(valid_paranthesis(s))


