name="chakradhari'
  File "<stdin>", line 1
    name="chakradhari'
         ^
SyntaxError: unterminated string literal (detected at line 1)
>>> name="chakradhari"
>>> city="kadapa"
>>> "my name is {} and i live in{}.".format(name,city)
'my name is chakradhari and i live inkadapa.'
>>> "my name is {} and i live in {}."format(name,city)
  File "<stdin>", line 1
    "my name is {} and i live in {}."format(name,city)
                                     ^^^^^^
SyntaxError: invalid syntax
>>> "my name is {} and i live in {}".format(name,city)
'my name is chakradhari and i live in kadapa'
>>> "my name is // and i live in //".format(name,city)
'my name is // and i live in //'
>>> "my name is () and i live in ()".format(name,city)
'my name is () and i live in ()'
>>> "i got {0:f}% marks in /"english.".format(55)
  File "<stdin>", line 1
    "i got {0:f}% marks in /"english.".format(55)
                                     ^
SyntaxError: unterminated string literal (detected at line 1)
>>> "i got {0:f}% marks in /"english".".format(55)
  File "<stdin>", line 1
    "i got {0:f}% marks in /"english".".format(55)
                             ^^^^^^^
SyntaxError: invalid syntax
>>> "i got {0:f}% marks in \"english\".".format(55)
'i got 55.000000% marks in "english".'
>>> "i got {f}% marks in \"english\".".format(55)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'f'
>>> "i got {:f}% marks in \"english\".".format(55)
'i got 55.000000% marks in "english".'
>>> "i got {d}% marks in \"english\".".format(55)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'd'
>>> "i got {:d}% marks in \"english\".".format(55)
'i got 55% marks in "english".'
>>>
>>> "i got {:d}% marks in \'english\'.".format(55)
"i got 55% marks in 'english'."
>>> name="chakradhari'
KeyboardInterrupt
>>>
KeyboardInterrupt
>>>
KeyboardInterrupt
>>>
KeyboardInterrupt
>>>