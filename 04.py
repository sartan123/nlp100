s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
s = s.replace('.', '')
s = s.split(" ")
x = (1, 5, 6, 7, 8, 9, 15, 16, 19)

s_n = {i: j[0] if i in x else j[:2] for i, j in enumerate(s)}

print(s_n)
