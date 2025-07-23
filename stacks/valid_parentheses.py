def valid_p(str) -> bool:
        dict = {"(": ")", "[": "]", "{": "}"}
        stack = []
        for c in str:
            if c in dict:
                stack.append(c)
            elif c in dict.values():
                if not stack or dict[stack.pop()] != c:
                     return False
        return not stack

print(f"'({{a+b}})' -> {valid_p('({a+b})')}")
print(f"'))((a+b){{' -> {valid_p('))((a+b){')}")
print(f"'((a+b))' -> {valid_p('((a+b))')}")
print(f"'))))' -> {valid_p('))')}")
print(f"'[a+b]*(x+2y)*{{gg+kk}}' -> {valid_p('[a+b]*(x+2y)*{gg+kk}')}")