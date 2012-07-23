'''
Created on 2012-7-21

@author: Administrator


# if

x = int(raw_input('enter a number:\r\n'))

if x  == 0:
    print 'zero'
elif x > 0:
    if x >= 100:
        print 'more than 100.'
    else:
        print 'normal number' 
else: 
    print 'negative number'
''' 
    
# for , different from other java, more like iterator and for statement in pl/sql 

vlist =["windows","linux","ios"]
for x in vlist:
    print x,len(x)
    
for x in vlist[:]: # slice a copy of vlist
    if len(x) == 5 : vlist[len(vlist):] = [x]
print vlist

# range function : a way to generate list quickly.
print range(10) # generate 0...9
print range(5,10) # generate 5...9
print range(0,10,3) # generate 0,3,6,9   - 3rd argument means step

# another way to iterate to vlist
for x in range(len(vlist)):
    print 'pos:%(x)i value:%(v)s' % {"x":x,"v":vlist[x]}
    
# use enumerate function,yeild function    [sf]
print '''# use enumerate function : ''',vlist
def printele(pos):
    print pos.count
#printele(enumerate(vlist))     


# else in for/while statement
# else executed when iteration end or while's condition become false
for x in [1,2,3]:   # attend ! then the x variable is global [sf]
    print x
else:
    print 'end'
# but will never invoke when loop stop by 'break' statement [sf]
for x in [1,2,3]:
    print x
    if x == 3 : break
else:
    print 'end'
    
# sample: find the prime number from 2 to 10
xc = 2
while xc <= 10:
    for y in [2,xc-1]:
        if xc % y == 0 :
            print '%(n)i is prime' % {"n":xc}
            break
    else:
        print xc,'is not prime'    
    xc += 1;
    
# pass, just like the 'null' in pl/sql, it's logic notation with no action
xy = 2
while xy <= 10:
    for y in [2,xy-1]:
        if xy % y == 0 :
            print '%(n)i is prime' % {"n":xy}
            break
    else:
        pass    
    xy += 1;
    
    
# func definition 
# fibonacci series up to 30
def prinfibonacci(upto=30):
    """Print a Fibonacci series up to n.""" # this is the documentation of the method.
    a,b,temp =0,1,0
    # all variable declared here are stored into local symbol table
    # there are a some context 
    # first look up : local symbol table -> local symbol table of enclosing table
    #               ->global symbol table -> table of build-in names
    ni = 0;
    while ni < upto:
        temp = a;
        a = b;
        b += temp;
        print 'month ',ni,' number : ',b
        ni +=1

prinfibonacci(10)

print prinfibonacci
