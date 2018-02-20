# user.py
# this represents a user of the library code
# that could potentially break due to changes
# in the core library that is beyond control
# how to catch it before runtime
# below is one to enforce a constraint on 
# library code from the user level;
# the Derived class has a constraint on the Base
# class, if not satisfied, it would fail loudly

from library import Base

# to ensure that foo() method is still there
assert hasattr(Base, 'foo'), "you broke it, you library fool!"

class Derived(Base):
    def bar(self):
        return self.foo()