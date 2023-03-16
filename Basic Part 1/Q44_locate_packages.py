# Q. Locate the site packages

# import site
import site

# printing the site packages
print(site.getsitepackages())

# the site module provides functions that help us access info about the python installation
# and site package directories
# the getsitepackages function returns a list of paths to the site-packages directories 
# for the current python installation