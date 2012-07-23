# -*- coding:UTF-8 -*-
'''
Created on 2012-7-21

@author: Administrator



interactive mode : 
    1. execute 'python' to python console
    2. execute a script with a -i param
    3. last returned value is persisted in _ identify.
    4.triple quotes  are more easy to declare a long string.
normal mode :


use "sys" model to get the startup parameters. [sys.argv[x]]
        the first argument is always the file name in experiment.
        when use -c , argv[0] = -c,
        when use -m , argv[0] = -m. 
        when option parameter after -c,-m, the interpreter doesn't use that. but will left in argv arrays and ready for py or module.
        
try to type ctrl + c when command executing. raise an KeyboardInterrupt exception 

encoding declaration : refer to the first line.    


customize the module : two hook are provided. 
    sitecustomize.py hook:    system/computer/environment level hook
    usercustomize.py hook:    user level hook
    save these files under [site.getusersitepackages()] folder, 
    they are in same function, different in usage. sitecustomize.py is on the first position.
    they will be disable when startup the program with -s option   


    a variable must be initialized before use [same as java]
    up to the higher number type when mixed type numbers were operated.[same as java]
    use * notation on a string means append itself by * times. [special feature]
    a quick access on array by using double position sign. such as word[2:4] word[:2], a string is also a fixed array, can't be modified  [special feature]
    a reverse-access by using negative number [special feature]
        word = "abcd"; word[-1] = d
        if use a out-of-range index. will get a '' on string.
    str() change u to normal, unicode() change normal to unicode, "中文".encode("utf-8") get the code
    a quick assigning value method: v1,v2,v3.. = expr1,expr2,epxr3...[ special feature]
        this syntax like a atomic operation. the expression on right are reading the original data[before change]
        for example :
            a = 1;
            b = 2
            a,b = b, a+b
            then : a = 2 and b = 3  
'''
# use this to get the startup parameters
import sys
print sys.argv[0]

# use this to get some environment parameters
import os 
print os.environ.get("test");

# not clear. get some environment parameters.
import site
print site.getusersitepackages();

# encode
print u"中文".encode("utf-8")

# the list allowed mixed type elements.
vlist = ["a","b",1,2]
alist = vlist[:] # return a new list
print "adfd"[:]
# this is a powerful syntax to handle the list data
# insert
vlist[:0] = ["a"] # also can write in "a" form
print vlist
# delete 
vlist[1:2] = []
print vlist
# clear 
vlist[:] = []
print vlist

# embed list
q = [1,2]
p = [q,3,4]
print p

p[0][:0] = [0]
print p 


# sum total of 1 ... 100
vs,ve,tot = 1,100,0 # quickly assign value
while vs <= ve:
    tot += vs
    vs += 1
print tot


# handy output.
print """1 ... 100's sum is """,tot # works as + in java.


# output a shape
slong,i,j = 7,1,1
sline = '';
while i <= slong:
    while j <= slong:
        if j >= slong /2+i or j <= slong /2 +2 :
            sline += "*"
        else:
            sline += " "
        j += 1
    print sline
    i,j,sline = i+1,1,''        