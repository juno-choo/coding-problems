def isAnagram(s: str, t: str) -> bool:
    map = {}
    for char in s:
        if char in map:
            map[char] += 1
        else:
            map[char] = 1

    for char in t:
        if char in map:
            map[char] -= 1
        else:
            return False
        
    for value in map.values():
        if value != 0:
            return False
    return True
    
s = "dogee"
t = "egoed"
print(isAnagram(s,t))

