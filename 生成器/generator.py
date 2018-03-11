#coding=utf-8

#列表生成式：
L = [x*x for x in range(10)]
#生成器
generator = (x*x for x in range(10))
print (L)
print (generator)

#列表生成式与生成器区别： [] <-----> ()

#可以通过next()函数获得generator的下一个返回值,但是这样太麻烦，而且没有更多的元素时，抛出StopIteration的错误。
print (next(generator))
#正确访问生成器

for g in generator:
	print (g),
print ('====================================')	
#定义generator的另一种方法。
#如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator：

def odd():
	

	#generator的函数，在每次调用next()的时候执行，
	#遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
	#相当于yield会记住之前的
	print('1.')
	yield(1111111111)
	print('2.')
	yield(3333333333)
	print('3.')
	yield(5555555555)
 

 #调用
o = odd()
print (next(o))
print (next(o))
print (next(o))
#print (next(o))
#odd不是普通函数，而是generator，在执行过程中，遇到yield就中断，下次又继续执行。执行3次yield后，已经没有yield可以执行了，所以，第4次调用next(o)就报错。

#杨辉三角

def triangles():
	L = [1]
	
	while(True):   #don't know why , but missing this line will throw an error  -__- ''' 
		yield (L)
		L = [1] + [ x+y for x,y in zip(L[1:],L[:-1]) ] +[1]   #zip把列表的（第一个到最后一个，第0个到倒数第一个）打包，每次对应位置相加
		#相当于错位存了两个列表
'''
错误调用
t = triangles()
for n in range(10):
	print (t)
'''
n=0
for t in triangles():
	print (t)
	n+=1
	if n==10:
		break








