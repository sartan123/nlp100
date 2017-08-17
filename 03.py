s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
s = s.replace(',', '')
s = s.replace('.', '')
s_n = [len(i) for i in s.split(" ")]
print(s_n)
