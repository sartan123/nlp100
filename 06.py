def n_gram(s, n):
    return [s[i:i + n] for i in range(0, len(s), n)]


s1 = "paraparaparadise"
s2 = "paragraph"

s1 = set(n_gram(s1, 2))
s2 = set(n_gram(s2, 2))

print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
print("se" in s1)
print("se" in s2)
