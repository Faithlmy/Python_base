
#run_foo.py
from foo import *

print(bar)
print(baz)

# The following will trigger an exception, as "waz" is not exported by the module
# 下面的代码就会抛出异常，因为 "waz"并没有从模块中导出，因为 __all__ 没有定义
print(waz)