#coding:UTF-8
#author: zoezhao
import math
#1 定义一个方法get_fundoc(func),
#func参数为任意一个函数对象，返回该函数对象的描述文档，如果该函数没有描述文档，则返回"not found"
def test_func(arg1,arg2):
	return arg1+arg2

def get_fundoc(func):
	if  not dir(func.__code__):
		return 'not find'
	else:
		return dir(func.__code__)

print get_fundoc(test_func)

'''
3 定义一个方法list_info(list), 参数list为列表对象，怎么保证在函数里对列表list进行一些相关的操作，
不会影响到原来列表的元素值

http://m.blog.csdn.net/bullpride/article/details/52004194

'''
def not_change_orginal_one(TestSet):
	temp = [TestSet[i] for i in xrange(0,len(TestSet))]   #若直接写 temp = TestSet ,则会改变 a 的值 
	temp[0] = 5
	print ('temp is:'),
	print temp
	return temp

a = [1,2,3]
print (not_change_orginal_one(a))
print (a)


def quadratic(a,b,c):
	'''求解二元一次方程'''
	delta = b**2 - 4*a*c
	if delta>=0:
		x1 = (-b+math.sqrt(delta))/(2*a)
		x2 = (-b-math.sqrt(delta))/(2*a)
		return x1,x2
	else:
		return 'error'

'''
print (quadratic(2,3,1))
print (quadratic(1,3,-4))
'''

def score(**kw):
	for name,score in kw.items():
		print ('name: %s  score: %d' % (name,score)) 


data = {'aa':99,'bb':88,'cc':77}
score(**data)  #注意是**data