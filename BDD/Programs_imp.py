import re
#1 Program to check if the input is Palindrome or not
#Method 1  using the index
Name = input('enter the value')
if Name[::] == Name[::-1]:
    print('The given charter is a Palindrome')
else:
    print('The given character is not a palindrome')
#Method 2 using reverse keyword
Name = input('enter the value')
if Name == reversed(Name):
    print('The given charter is a Palindrome')
else:
    print('The given character is not a palindrome')
#Method 3 using condition
Name = input('enter the value')
i= len(Name)-1
Rname = ''
while i >= 0:
    Rname = Rname + Name[i]
    i = i-1
if Rname == Name:
    print('Palindrome')
else:
    print('Not palindrome')

#2 Program to find the occurrences of each character
#Method1 Using count
Name = input('enter the value')
outsingle = []
for ch in Name:
    if ch not in outsingle:
        outsingle.append(ch)
for final in outsingle:
    print('{} occurs {} times'.format(final, Name.count(final)))
#Method2 Using set function but not in word order
Name = input('enter the value')
outsingle = set(Name)
for final in sorted(outsingle):
    print('{} occurs {} time'.format(final, Name.count(final)))
#Method3 using the dictionary method
Name = input('entr the value')
d = {}
for x in Name:
    d[x] = d.get(x,0)+1
for k,v in d.items():
    print(k, 'occured', v, 'times')

#3 Program of Anagram
Name1 = input('Enter the first value')
Name2 = input('Enter the second value')
if sorted(Name1) == sorted(Name2):
    print('The values are anagram')
else:
    print('The values are not anagram')

#4 Program to find the factorial
#Method1 using recursive function(function which calls itself)
def fact(num):
    if num==0:
        result = 1
    else:
        result = num * fact(num-1)
    return result
print('The factorial of num is', fact(5))
#Method2 without recursion
def fact(num):
    result =1
    while num>=1:
        result = result * num
        num = num-1
    return result
print('The factoriaL of 5 is', fact(5))

#5 Program to swap the values
#Method1 using third variable
A = int(input('Enter the a value'))
B= int(input('Enter the b value'))
C = A
A = B
B = C
print('The value of A is', A)
print('The value of B is', B)
#Method2 direct swap value allocation
A = int(input('Enter the a value'))
B= int(input('Enter the b value'))
A, B = B, A
print('The value of A is', A)
print('The value of B is', B)

#6 Program to remove the special characters
def modified(text):
    result = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return result
print('The modified string is', modified('J*yo$%thi'))





