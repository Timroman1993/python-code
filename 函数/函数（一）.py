#coding=UTF-8

#http://blog.csdn.net/bullpride/article/details/51982158

#1.定义一个方法 func，该func可以引入任意多的整型参数，结果返回其中最大与最小的值。
def func1(*num):
	for i in num :
		if not isinstance(i,int):
			print ("num not qualified")
	return max(num),min(num)


#2.定义一个方法func，该func可以引入任意多的字符串参数，结果返回（长度）最长的字符串。
def func2(*str1):
	max_str = ''
	for i in str1:
		#print ('now is:' ),
		#print (i)
		if not isinstance(i,str):
			print ("not string")
		else:
			if len(i)>len(max_str):
				max_str = i
			else:
				pass
	return max_str

ss = func2("dgag","dsgag","jmfadjgasdf") 
print (ss)
#print (type(ss)) #传入的是元组，ss类型是由返回值max_str定的

#3.定义一个方法get_doc(module)，module参数为该脚本中导入或定义的模块对象，该函数返回module的帮助文档。
def get_doc(module):
	return help(module)

#doc = get_doc(str) #直接就输出帮助文档了 因为help就直接输出的


#4.定义一个方法get_text(f),f参数为任意一个文件的磁盘路径，该函数返回f文件的内容。
def get_text(f):
	a = open(f)
	return a.read()

#5.定义一个方法get_dir(folder),folder参数为任意一个文件夹，该函数返回folder文件夹的文件列表。提示（可以了解python的glob模块）
# glob模块很简单，用到三个通配符*?[], *匹配0个或多个字符，?匹配单个字符，[]匹配指定范围内的字符  
# 字符串前面加r防止转义字符的作用，路径中就要加 
import glob

def get_dir(folder):
	return glob.glob(folder+'/*')

print (get_dir('/Users/zoe/Documents/python程序'))













