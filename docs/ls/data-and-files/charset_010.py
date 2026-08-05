# 2026-08-05  charset_010.py

# 010-words-as-numbers.md 中提到的字符集

def get_ord(c: str) -> int:
    if len(c) != 1:
        raise ValueError("Not a single character")
    if c.islower():
        return 1 + ord(c) - ord('a')
    if c.isupper():
        return 27 + ord(c) - ord('A')
    if c == '\'':
        return 53
    if c == '.':
        return 54
    if c == '_':
        return 55
    if c == ' ':
        return 56
    if c == '\n':
        return 57
    if c.isdigit():
        return 58 + int(c)
    raise ValueError("Unrecognized character")

text = "It's me.\nMy name is LS_Hower."

for c in text:
    print(f"`{c}` 对应 {get_ord(c)}；")

print([get_ord(c) for c in text])

print([get_ord(c) for c in "He is 67 years old."])

print([get_ord(c) for c in " LS_Hower"])
