## This program is to set correctly the root directory for project
#python_utilities is project root and hence that should be there in PYTHONPATH.

print("all paths defined in PYTHONPATH")
import sys

for p in sys.path:
    print(p)

## how to set a path in PYTHONPATH - set it from environment variable or using cmd below
#set PYTHONPATH=%PYTHONPATH%;D:\study\python\python_utilities\

# D:\study\python\python_utilities
# D:\study\python
# C:\Users\mahib\AppData\Local\Programs\Python\Python37\python37.zip
# C:\Users\mahib\AppData\Local\Programs\Python\Python37\DLLs
# C:\Users\mahib\AppData\Local\Programs\Python\Python37\lib
# C:\Users\mahib\AppData\Local\Programs\Python\Python37
# C:\Users\mahib\AppData\Local\Programs\Python\Python37\lib\site-packages

