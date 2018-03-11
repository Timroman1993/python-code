#coding=utf-8

'''
1.定义一个func(name)，该函数效果如下。
assert func("lilei") = "Lilei"
assert func("hanmeimei") = "Hanmeimei"
assert func("Hanmeimei") = "Hanmeimei"
'''

def capital_the_first(name):
	return name.capitalize()

assert capital_the_first("lilei") == "Lilei"
assert capital_the_first("hanmeimei") == "Hanmeimei"
assert capital_the_first("Hanmeimei") == "Hanmeimei"

"""
2.定义一个func(name,callback=None),效果如下。
assert func("lilei") == "Lilei"
assert func("LILEI",callback=string.lower) == "lilei"
assert func("lilei",callback=string.upper) == "LILEI"

"""
import string 
def func(name,callback=None):
	if callback == None:
		return name.capitalize()
	else:
		return callback(name)

assert func("lilei") == "Lilei"
assert func("LILEI",callback=string.lower) == "lilei"
assert func("lilei",callback=string.upper) == "LILEI"


"""
3.定义一个func(*kargs),效果如下。

l = func(1,2,3,4,5)
for i in l:
	print i,
#输出 1 2 3 4 5

l = func(5,3,4,5,6)
for i in l:
	print i
#输出 5 3 4 5 6

"""
def get_items(*kargs):
	return kargs

l = get_items(1,2,3,4,5)
for i in l:
	print i,
print ('\n')

l =get_items(5,3,4,5,6)
for i in l:
	print i,
print ('\n')

"""
4.定义一个func(*kargs)，该函数效果如下。

assert func(222,1111,'xixi','hahahah') == "xixi"
assert func(7,'name','dasere') == 'name'
assert func(1,2,3,4) == None


"""

def get_str1(*kargs):
	strlist = filter(lambda x:isinstance(x,str),kargs)
	if strlist ==():
		return
	else:
		return strlist[0]

assert get_str1(222,1111,'xixi','hahahah') == "xixi"
assert get_str1(7,'name','dasere') == 'name'
assert get_str1(1,2,3,4) == None

'''
test = (1,2,3,4)
strlist = filter(lambda x:isinstance(x,str),test)
print strlist
'''

"""
5.定义一个func(name=None,**kargs),该函数效果如下。

assert func(“lilei”) == "lilei"
assert func("lilei",years=4) == "lilei,years:4"
assert func("lilei",years=10,body_weight=20) == "lilei,years:4,body_weight:20"

"""


def func5(name=None,**kwargs):
	lis = ["%s:%s" % (x,y) for x,y in kwargs.items()]
	lis.insert(0,name)
	return ','.join(lis)

assert func5("lilei") == "lilei"
assert func5("lilei",years=4) == "lilei,years:4"
assert func5("lilei",years=10,body_weight=20) == "lilei,body_weight:20,years:10"

















