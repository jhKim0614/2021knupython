#
import mod1

boogie = mod1.Friends('Boogie', 5)
boogie.hello()

print(mod1.add_to_N(10))


#
from mod1 import Friends, add_to_N

boogie = mod1.Friends('Boogie', 5)
boogie.hello()

print(add_to_N(10))


#
from mod1 import Friends as Fr
from mod1 import add_to_N as aN

boogie = Fr('Boogie', 5)
boogie.hello()

print(aN(10))
