Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> s1 = {1,2,3,4,5}
>>> s2 = {5,4,6,7,1}
>>> s2 = {5,4,6,7,1,'Hi','Bye'}
>>> s1.intersection(s2)
{1, 4, 5}
>>> s1.union(s2)
{1, 2, 3, 4, 5, 6, 7, 'Bye', 'Hi'}
>>> l = [1,2,3,4,2,5,6,7,2,3,4,8,9,0]
>>> set(l)
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
>>> x = set(l)
>>> x
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
>>> list(x)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> 
