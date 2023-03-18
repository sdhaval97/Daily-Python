# Q. To print to STDERR

# importing print_function and sys
from __future__ import print_function
import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

eprint("abc", "efg", "xyz", sep="--")

# the print_function from __future__ module enables the use of the newer print function syntax
# sys module allows us access to system specific parameters and functions
# the code prints the output to a different output stream that is the standard error output stream
