# Preface

- <https://www.oreilly.com/catalog/errata.csp?isbn=0636920045267>
- <https://greenteapress.com/wp/think-python-2e/>
- <http://www.greenteapress.com/thinkpython2/code/>
- <http://shop.oreilly.com/product/0636920045267.do>

# C1

- <http://www.allendowney.com/wp/books/think-python-2e/>
- <https://wiki.python.org/moin/BitwiseOperators>

```Python
>>> 2++2
4
```

# C2

```Python
>>> 9 ** 2 ** 3 # exponentiation is evaluated from right to left
43046721
```

String Operations:
1. The `+` operator performs string concatenation.
2. The `*` operator performs repetition. If one of the values is a string,
   the other has to be an integer.

```Python
>>> 0*'abc'
''
>>> -1*'abc'
''
>>> (-5)*'abc'
''
```

```Python
>>> x = y = 1
>>> x
1
>>> y
1
```

```Python
>>> import math
>>> math.pi
```


# C3

- `type`
- `int`
- `float`
- `str`
- `math.log10`
- `math.log`
- `math.sin`
- `math.sqrt`
- `math.exp`

A function definition can have calls to other functions which are defined 
later in the code:
```Python
def foo():
    bar()

def bar():
    print("bar")

foo()
```

<http://greenteapress.com/thinkpython2/code/do_four.py>

