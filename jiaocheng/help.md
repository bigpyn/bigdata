很多常用的python函数或模块，经常需要查看帮助，很不方便。

在python的交互命令行下使用help()或在python文件中调用help()函数可以很方便的查看帮助。

 

一 查看所有的关键字：help("keywords")

复制代码
Here is a list of the Python keywords.  Enter any keyword to get more help.

and                 elif                import              return
as                  else                in                  try
assert              except              is                  while
break               finally             lambda              with
class               for                 not                 yield
continue            from                or
def                 global              pass
del                 if                  raise
复制代码
 

 

二 其他

查看python所有的modules：help("modules")

单看python所有的modules中包含指定字符串的modules： help("modules yourstr")

查看python中常见的topics： help("topics")

查看python标准库中的module：import os.path + help("os.path")

查看python内置的类型：help("list")

查看python类型的成员方法：help("str.find") 

查看python内置函数：help("open")

 

三 例如查看copy模块帮助如下： help("copy")

复制代码
Help on module copy:

NAME
    copy - Generic (shallow and deep) copying operations.

FILE
    c:\python31\lib\copy.py

DESCRIPTION
    Interface summary:
    
            import copy
    
            x = copy.copy(y)        # make a shallow copy of y
            x = copy.deepcopy(y)    # make a deep copy of y
    
    For module specific errors, copy.Error is raised.
    
    The difference between shallow and deep copying is only relevant for
    compound objects (objects that contain other objects, like lists or
    class instances).
    
    - A shallow copy constructs a new compound object and then (to the
      extent possible) inserts *the same objects* into it that the
      original contains.
    
    - A deep copy constructs a new compound object and then, recursively,
      inserts *copies* into it of the objects found in the original.
    
    Two problems often exist with deep copy operations that don't exist
    with shallow copy operations:
    
     a) recursive objects (compound objects that, directly or indirectly,
        contain a reference to themselves) may cause a recursive loop
    
     b) because deep copy copies *everything* it may copy too much, e.g.
        administrative data structures that should be shared even between
        copies
    
    Python's deep copy operation avoids these problems by:
    
     a) keeping a table of objects already copied during the current
        copying pass
    
     b) letting user-defined classes override the copying operation or the
        set of components copied
    
    This version does not copy types like module, class, function, method,
    nor stack trace, stack frame, nor file, socket, window, nor array, nor
    any similar types.
    
    Classes can use the same interfaces to control copying that they use
    to control pickling: they can define methods called __getinitargs__(),
    __getstate__() and __setstate__().  See the documentation for module
    "pickle" for information on these methods.

CLASSES
    builtins.Exception(builtins.BaseException)
        Error
    ... ...

FUNCTIONS
    copy(x)
        Shallow copy operation on arbitrary Python objects.
        
        See the module's __doc__ string for more info.
    
    deepcopy(x, memo=None, _nil=[])
        Deep copy operation on arbitrary Python objects.
        
        See the module's __doc__ string for more info.

DATA
    __all__ = ['Error', 'copy', 'deepcopy']


复制代码
 

 

完！
