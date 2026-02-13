### NUMBERS

## integers vs floating numbers

Whole numbers such as 1, 2, 3, 10, 27, 59, 113 etc.. are considered to be integers

Fraction like numbers such as 1.2, 3.1, 21.3, 47.9 etc are considered to be floating numbers

```bash
>>> 2+2
4
>>> 50 - 5*6
20
>>> 100-50
50
>>> (100-50) / 5 # division alwas returns floating number
10.0
>>>
```

## operators +, -, *, /, %

```bash
>>> 17/3
5.666666666666667
>>> 17//3 # floor division discards the fractional part
5
>>> 17 // 3 # floor division discards the fractional pard of the number
5
>>> 17 % 3 # the % operator returns the remainder of the division eg: 3, 6, 9, 12, 15 >> THEN 17 - 15 = 2 
2
>>> 5 * 3 + 2 # floored quotient * divisor + remainder
17
>>> 
```

the operator ** caculates powers

```bash
>>> 5 ** 2 # 5 squared
25
>>> 2 ** 10 # 2 to the power of 10
1024
>>> 
```

## mix operators/operands

Mixed type operands convert integer to floating number
```bash
>>> 2 * 2.50 - 2
3.0
>>>
```

## variables and values

The = sets a value to a variable

```bash
>>> weight = 20
>>> height = 10 + 10
>>> weight * height
400
>>> 
```

receive an error when variable is not defined

```bash
>>> n
Traceback (most recent call last):
  File "<python-input-20>", line 1, in <module>
    n
NameError: name 'n' is not defined
>>> 
```

Last printed expression is assigned to the variable _
```bash
>>> tax = 12.5 / 100
>>> price = 100.50
>>> price * tax
12.5625
>>> price + _
113.0625
>>> round(_, 3) # round to the 3rd decimal
113.062
>>>
```