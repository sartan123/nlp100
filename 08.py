def f(c):
    return c if c >= "a" and c <= "z" else chr(219 - ord(c))


def cipher(s):
    s2 = [f(c) for c in s]
    return s2

s = "Hello youtube"
print("".join(cipher(s)))
