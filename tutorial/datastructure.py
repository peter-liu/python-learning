'''
Created on 2012-7-23

@author: Administrator
'''
# list

# stack

# queue
from collections import deque
que = deque(["protest","economy","politics"])
que.append("demonstrate")
que.append("conservative")
que.appendleft("military")
print que
que.popleft();
print que
que.pop()
print que

# function tools
#   filter
def f(x): return x % 2 == 0 and x % 3 == 0
print filter(f,range(2,23))
f1 = lambda x : x % 3 == 0
print filter(f1,range(2,23)) # use a lambda, also refer to print filter(lambda x : x % 3 == 0,range(2,23)) form
print filter(lambda x : x == 'h',"hello hill")# can be a string a ?tuple?

#   map : execute the fn for each item, the list will be refill by the result
def dube(x): return x*x*x
print map(dube,range(1,11))
def add(x,y): return x+y;
print map(add,[1,2,3],[4,5,6]) # if one list is shorter than another, will pass in a None, more and more seq are allowed
testunpacking = [[1,2,3],[4,5,6]]# test use unpacking argument
print map(add,*testunpacking)


# reduce : return a single value, first pass first two value into fn, then pass the result and the next value into fn.
print reduce(add,range(1,11))
print reduce(add,[1])# single value, return the value directly without execute fn
#reduce(add,[])# get an exception
def sum1(seq):
    def add1(x,y):return x + y
    return reduce(add1,seq,10)# 10 is a extra value for compute.
print sum1([1,2,3,4,5,6,7,8,9,10])


# List comprehensions : q concise form to generate a list computed by complex logic
#   expression : a brackets containing a expression followed one or more for and if statement, the variable declared back are rely on the pre-declared
print '''[x*2 for x in range[-3,4]]:''',[x*2 for x in range(-3,4)]
print '''[x*y for x in range(1,4) for y in range(3,6)]:''',[x*y for x in range(1,4) for y in range(3,6)]
print '''[x*y for x in range(1,4)  if x != y for y in range(3,6)]:''',[x*y for x in range(1,4)  if x != y for y in range(3,6)]
print '''[x*y for x in range(1,4)  for y in range(3,6) if x != y]:''',[x*y for x in range(1,4)  for y in range(3,6) if x != y]
print [abs(x)+1 for x in range(-3,4)]#  expr and be any thing
print [(x,x+y) for x in range(-3,4) for y in [1]]#tuple
from math import pi
print [round(pi, x) for x in range(1,9,1)]
# nested comprehensions
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print [[r[l] for r in matrix] for l in range(3)]

print matrix
print zip(*matrix)
print zip(matrix)
print zip([1,2],[3,4])# compose same index value of more than one list  into a tuple



# del statement
# del a item by its position(remove() by value), and not return a value(differ to pop())
# can del a number of item(list[x:n] = [] can do this again)
vlist = [1,2,'a','c',1000,'politic','apply to']
del vlist[0]
print vlist
del vlist[1:3]
print vlist
del vlist[:]
print vlist
del vlist# this identify is a undefined value since this line
#print vlist # get an error

#Tuple and Sequence
uglytuple = 'a',
print uglytuple,len(uglytuple)
#unpack tuple
t = 12345, 54321, 'hello!'
x,y,z = t
print x,y,z
# unpack list
t = [12345, 54321, 'hello!']
x,y,z = t
print x,y,z


# Set: unorderd , no duplicate element.
# support mathematical operation. union,intersection,difference,symmetric difference
words=["opposite","concerned","evident","continuation","toward","liberal","suffer","psychology"
       "concerned","conservative","ecology","economy","military"]
uset = set(words)
print uset
print 'concerned' in uset , 'concerned' in words
# mathematical operation
seta = set("123")
setb = set("354")
print seta,setb
print seta - setb # in a but not in b
print seta ^ setb # in a or b but not both, difference
print seta | setb # union
print seta & setb # intersection

