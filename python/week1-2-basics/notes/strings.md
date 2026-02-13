d### STRING EXAMPLES

## TEXT

single quotes ' ' and double quotes " " ceated strings

>>> 'grocery shopping' # single quotes
'grocery shopping'
>>> "I play basketball" # double quotes
'I play basketball'
>>> '200,312'
'200,312' # numbers quoted
>>>



To quoTo quote a quote, we need to “escape” it, by preceding it with \. Alternatively, we can use the other type of quotation marks:
```bash
>>> 'don\'t' # use \ to escape the single quote
"don't"
>>> "doesn't" # double quotes eliminates the need for \
"doesn't"
>>> '"Yes" they said.'
'"Yes" they said.'
>>> "\"Yes,\" they said."
'"Yes," they said.'
>>> '"Isn\'t," they said.'
'"Isn\'t," they said.'  
>>> 'Isn\'t, they said.'
"Isn't, they said."
>>>
```

### print() function

print() provides a readable output,
```bash
>>> a = 'First line.\nSecond line.' # \n means new line
>>> a # without print() special characters will be included for the output of a variable
'First line.\nSecond line.'
>>> print(a)
First line.
Second line.
>>>
```

### raw strings (r'string')

To avaoid including characters preferanced by \ being interppreted as special characters, use raw strings by adding an r before the first quote:
```bash
>>> print('C:\some\name') # \n means newline
C:\some
ame
>>> 
>>> print(r'C:\some\name') # r before the quote prevents a newline being created
C:\some\name
>>> 
```

