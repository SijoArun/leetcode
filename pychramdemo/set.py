s={12,13,1212,"test",121,992}
print(s)
s.update({3,1})
print(s)
s.remove(12)
print(s)

f=frozenset(s)
print(f)
