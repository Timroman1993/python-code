#coding=utf-8
#http://blog.csdn.net/bullpride/article/details/51993817
#1 定义一个方法get_num(num),num参数是列表类型，判断列表里面的元素为数字类型。其他类型则报错，并且返回一个偶数列表：
#（注：列表里面的元素为偶数）。
import math
def is_even(n):
	if n%2==0:
		return n

def get_num(*num):   #也可以不用* 直接传一个list过来
	for i in num:
		if not isinstance(i,int):   #判断类型
			return "error"
	evenlist=list(filter(is_even,num))
	return evenlist
   



print(get_num(12,34,5,62,4,2,56,33))

assert get_num(1, 2, 3, 4) == [2, 4]
assert get_num(1, 2, 3, 'd') == 'error'
assert get_num() == [] 

#2 定义一个方法get_page(url),url参数是需要获取网页内容的网址，返回网页的内容。提示（可以了解python的urllib模块）。
import urllib

def get_page(url):
	return urllib.urlopen(url).read()

#print (get_page('http://www.baidu.com/'))

#3 定义一个方法 func，该func引入任意多的列表参数，返回所有列表中最大的那个元素。
'''
def func(*numlist):
	maxlist = []
	if len(numlist) == 0:
		return 'None'

	for i in numlist:
		if not isinstance(i,list):   #这样就有问题 应该改为两个循环判断
			return 'error'
		else:
			maxlist.append(max(i))
	return max(maxlist)

print func([1, 2], [3, 4], [5, 6])
print func(['a', '2'], [3, 4])


assert func([1, 2], [3, 4], [5, 6]) == 6  
assert func() == 'None'  
assert func(['a', '2'], [3, 4]) == 'error' 

'''



def func(*numlist):
	maxlist = []
	if len(numlist) == 0:
		return 'None'
	for k in numlist:
		for i in k:
			if isinstance(i,(int,float)):
				pass
			else:
				return 'error'
	maxlist.append(max(k))
	return max(maxlist)


 

print func([33,5,5,34],[345,6,547,78,6])

assert func([1, 2], [3, 4], [5, 6]) == 6  
assert func() == 'None'  
assert func(['a', '2'], [3, 4]) == 'error' 

#4 定义一个方法get_dir(f),
# f参数为任意一个磁盘路径，该函数返回路径下的所有文件夹组成的列表，如果没有文件夹则返回"Not dir"。


# os.path.isdir(path)可以用来判断这个路径所指的是不是一个文件夹  
# os.path.exists(path) 路径存在返回True，不存在则返回False  
# os.listdir(path)用来获得当前目录的内容  
import os
def get_dir(f):
	if not os.path.exists(f):
		return "not dir"
	list_all_dir = os.listdir(f)
	list_dir = filter(lambda k: os.path.isdir(f+'/'+k ), list_all_dir)

	return list_dir

print (get_dir('/Users/zoe/Documents'))



