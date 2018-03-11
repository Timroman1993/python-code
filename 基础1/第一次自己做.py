#2017.09
#!usr/bin/python
#coding:UTF-8

s="i,am,lilei"
print (s[2:4])
print (s.split(',')[1])

file = open("test.txt","r")
content = file.read()
print ( content)


dcontent = content.decode('utf-8')
print ( len(dcontent) )


print (content.replace("\n",""))

print (content.replace("2012","2013"))

newfile = open("test1.txt","w")
newfile.write( content.replace("2012","2013"))
newfile.close()

mid = len(dcontent)/2
print (mid)

print (dcontent[mid:mid+5])
print (dcontent[mid:mid+5]).encode("utf-8")

print (dcontent[-2:]).encode("utf-8")


print (dcontent[0:11])



# 6.-----------------
import sys

a = "中文编程"  ##引用计数开始是3，然后a变量引用了字符串对象3 + 1 =4

print sys.getrefcount('中文编程')
b = a


c = a


print sys.getrefcount('中文编程')##输出结果是6
print 'ssss'
a = "python编程"


b = u'%s' % a.decode('utf-8')


print sys.getrefcount('中文编程')##输出结果是4

d = "中文编程"
print "d:%s" % id(d)###新建一个变量，引用字符串 4 + 1 = 5

e = a
print "e:%s" % id(e)

c = b
print "c:%s" % id(c)### c引用另外一个字符串对象，5 - 1 = 4

print sys.getrefcount('中文编程')


b2 = a.replace("中","中")
print "b2:%s" % id(b2)

print 'result-----------------'
print sys.getrefcount('中文编程')
print sys.getrefcount('python编程')


# 7.--------------------------------------

print ("_______________________________")


str1 = "ssss"
str2 = "aaaa"

print (str1+str2)

print ( "%s%s" ) % (str1,str2)

print ( "{}{}".format(str1,str2))

print ("".join([str1,str2]))


print (",".join([str1,str2]))


import string


num = string.digits


low = string.lowercase


dot = string.punctuation



upper = string.uppercase##大写字母
print '\n'

print (num)
print (low)
print (dot)
print (upper)
print ("\nend")

str = []
str.append(num)

print (str)
'''
ss = []
ss.append(string.digits)
print (ss)

'''
str.append(low)
str.append(dot)
str.append(upper)

print (str)
print ("".join(str))

# 9_____________________

print ("-----------------------------------")

a = "i,am,a,boy,in,china"
print a.find('i',a.find('china'))


print ( a.find("i", a.find("china")))

