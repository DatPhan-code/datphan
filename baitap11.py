import zlib

s ="hello helloo helloo"
t = zlib.compress(s.encode("utf-8"))

print(t)
print(zlib.decompress(t))


# shuffle() : tron list
from random import shuffle
li = [1,23.4]
shuffle(li)
print(li)


