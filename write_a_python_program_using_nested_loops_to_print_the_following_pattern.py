# -*- coding: utf-8 -*-
"""Write a Python program using nested loops to print the following pattern.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1i7XSSEhkwBmmk2k4XAjVZ8j0hKlsPV_L
"""

for i in range(1,6):
  for j in range(i):
    print('*',end='')

  print()

"""# Right-Aligned ***Triangle*


"""

rows=5
for i in range(1,rows+1):
  for j in range(1,rows+1-i):
    print(' ',end=' ')
  for k in range(1,i+1):
    print('*',end=' ')
  print()

rows=5
for i in range(1,rows+1):
  print(' '*(rows -i) + '*'*i)

rows = 5
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * i)

"""# * Inverted Triangle*"""

rows=5
for i in range(rows,0,-1):
  for j in range(0,rows-i):
    print(end=' ')
  for k in range(0,i):
    print('*',end=' ')

  print()

rows=5
for i in range(rows,0,-1):
  print(' ' * (rows-i)+'*'*i)

"""# ***Pyramid***"""

rows=5
for i in range(1,rows+1):

  print(" " * (rows-i)+"*"*(2*i-1))

rows = 5
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))

"""# ***Diamond***"""

rows=5
for i in range(1,rows+1):
  print(' '*(rows-i)+'*'*(2*i-1))
for j in range(rows-1,0,-1):
  print(' '*(rows-j)+'*'*(2*j-1))

rows = 5

# Upper part of the diamond
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))

# Lower part of the diamond
for i in range(rows - 1, 0, -1):
    print(" " * (rows - i) + "*" * (2 * i - 1))

"""# Hollow Square"""

rows=5
for i in range(1,rows+1):
  if i==1 or i==rows:
    print('*'*rows)
  else:
    print('*'+' '*(rows-2)+'*')

"""# Hollow Pyramid"""

rows = 5
for i in range(1, rows + 1):
    if i == rows:
        print("*" * (2 * rows - 1))  # Bottom row
    else:
        print(" " * (rows - i) + "*" + " " * (2 * i - 3) + ("*" if i > 1 else ""))

"""# Number Triangle"""

rows=5
for i in range(1,rows+1):
  for j in range(1,i+1):
    print(j,end=' ')

  print()

rows=5
for i in range(rows,0,-1):
  for j in range(1,i+1):
    print(j,end=' ')
  print()

"""# Floyd's Triangle"""

rows=5
num=1
for i in range(1,rows+1):
  for j in range(1,i+1):
    print(num,end=' ')
    num +=1
  print()



"""# Checkerboard"""

rows=4
for i in range(rows):
  for j in range(rows):
    if (i+j)%2==0:
      print('*',end=' ')
    else:
      print(' ',end=' ')
  print()

rows = 8
for i in range(rows):
    for j in range(rows):
        if (i + j) % 2 == 0:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()