#coding=utf-8
'''
定义一个学生类。有下面的类属性：
 姓名
 年龄
 成绩（语文，数学，英语)[每课成绩的类型为整数]
类方法：
 获取学生的姓名：get_name() 返回类型:str
 获取学生的年龄：get_age() 返回类型:int
 返回3门科目中最高的分数。get_course() 返回类型:int
test:  zm = student('zhangming',20,[69,88,100])
 '''

class student(object):
	def __init__(self,name,age,score):
 		self.name = name
 		self.age = age
 		self.score = score
 	def get_name(self):
 		return self.name
 	def get_age(self):
 		return self.age
 	def get_course(self):
 		return max(self.score)

zm = student('zhangming',20,[69,88,100])	
print (zm.get_name())
print (zm.get_age())
print (zm.get_course())



lq = student('liqiang',23,[82,60,99])
print (lq.get_name())
print (lq.get_age())
print (lq.get_course())

'''
二：定义一个字典类：dictclass。完成下面的功能：


dict = dictclass({你需要操作的字典对象})

1 删除某个key

del_dict(key)


2 判断某个键是否在字典里，如果在返回键对应的值，不存在则返回"not found"

get_dict(key)

3 返回键组成的列表：返回类型;(list)

get_key()

4 合并字典，并且返回合并后字典的values组成的列表。返回类型:(list)

update_dict({要合并的字典})

'''
print ('---------------------------------')
class dictclass(object):
	
	def __init__(self,dic):
		self.dic = dic
	
	def del_dic(self,key):
		if self.dic.has_key(key):
			del self.dic.key
		else:
			return 'no such key'
	
	def get_dic(self,key):
		if self.dic.has_key(key):
			return self.dic[key]
		else:
			return 'not find'

	def get_keys(self):
		return self.dic.keys()

	def update_dic(self,dic2):
		self.dic = dict(self.dic,**dic2)
		return self.dic.values()

A = dictclass({'a': 1, 'b': 2})
print A.get_dic('c')
print A.del_dic('c')
print A.get_keys()
print A.update_dic({'c': 3, 'd': 4})


'''
关于合并字典
A = {'a': 1, 'b': 2, 'c': 3}
B = {'d': 4, 'e': 5, 'f': 6}
C = dict(A.items() + B.items())
D = dict(A, **B)  # 这种合并方法会比上一种快很多对于重复的key，B会覆盖A
'''


'''
写一个网页数据操作类。完成下面的功能：

提示：需要用到urllib模块

get_httpcode()获取网页的状态码，返回结果例如：200,301,404等 类型为int

get_htmlcontent() 获取网页的内容。返回类型:str

get_linknum()计算网页的链接数目。

'''
print ('---------------------------------')
import urllib
import urllib2

class web_data(object):
	def __init__(self,url):
		self.url = url
	def get_httpcode(self):
		status = urllib.urlopen(self.url).code
		return status
	def get_htmlcontent(self):
		content_str = urllib2.urlopen(self.url).read()
		return content_str
	def get_linknum(self):
		content = urllib2.urlopen(self.url).read()
		linknum = len(content.split('<a href='))-1
		return linknum
'''
A = web_data("http://www.baidu.com")
print A.get_httpcode()
print A.get_htmlcontent()
print A.get_linknum()

'''


'''
定义一个列表的操作类：Listinfo

包括的方法: 

1 列表元素添加: add_key(keyname)  [keyname:字符串或者整数类型]
2 列表元素取第num个元素：get_key(num) [num:整数类型]
3 列表合并：update_list(list)	  [list:列表类型]
4 删除并且返回最后一个元素：del_key() 

'''
print ('---------------------------------')
class Listinfo(object):
	def __init__(self,list_var):
		self.mylist = list_var


	
	def add_key(self,keyname):
		if isinstance(keyname,(int,str)):
			self.mylist.append(keyname)
			return self.mylist
		else:
			return "the insert value isn't a legal one"

	def get_key(self,num):
		if num >= 0 and num <= len(self.mylist):
			return self.mylist[num]
		else:
			return 'no such value'


	def update_list(self,new_list):
		self.mylist.extend(new_list)
		return self.mylist

	def del_key(self):
		if len(self.mylist) >= 0:
			return self.mylist.pop(-1)
		else:
			return 'the list already clear'


list1 = [44, 222, 111, 333, 454, 'sss', '333']
list_info = Listinfo(list1)
print (list1)
print (list_info.add_key('1111'))
print (list_info.get_key(4))
print (list_info.update_list(['1', '2', '3']))
print (list_info.del_key())

'''
定义一个集合的操作类：Setinfo

包括的方法: 

1 集合元素添加: add_setinfo(keyname)  [keyname:字符串或者整数类型]
2 集合的交集：get_intersection(unioninfo) [unioninfo :集合类型]
3 集合的并集： get_union(unioninfo)[unioninfo :集合类型]
4 集合的差集：del_difference(unioninfo) [unioninfo :集合类型]

set_info =  Setinfo(你要操作的集合)
'''
print ('---------------------------------')
class Setinfo(object):
	def __init__(self,set_var):
		self.myset = set_var

	def add_setinfo(self,keyname):
		if isinstance(keyname,(str,int)):
			self.myset.add(keyname)
			return self.myset
		else:
			return "the insert value isn't a legal one"
	def get_intersection(self,unioninfo):
		if isinstance(unioninfo,set) :
		    return self.myset & unioninfo
		else:
		    return "error" 

	def get_union(self,unioninfo):
		if isinstance(unioninfo,set):
			return self.myset | unioninfo
		else:
			return 'error'

	def del_difference(self,unioninfo):
		if isinstance(unioninfo,set):
			return self.myset - unioninfo
		else:
		    return "error" 


A = set([1, 2, 3, 4, 5, 2])
B = set([5, 6, 3])
set_info = Setinfo(A)
print set_info.add_setinfo('f')
print set_info.get_intersection(B)
print set_info.get_union(B)
print set_info.del_difference(B)		   

print ('---------------------------------')

class SchoolMember:
    '''Represents any school member.'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print '(Initialized SchoolMember: %s)' % self.name

    def tell(self):
        '''Tell my details.'''
        print 'Name:"%s" Age:"%s"' % (self.name, self.age),

class Teacher(SchoolMember):
    '''Represents a teacher.'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print '(Initialized Teacher: %s)' % self.name

    def tell(self):
        print 'Salary: "%d"' % self.salary

class Student(SchoolMember):
    '''Represents a student.'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print '(Initialized Student: %s)' % self.name

    def tell(self):
        print 'Marks: "%d"' % self.marks

t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 22, 75)
print ('-------')	
members = [t, s]
for member in members:
    member.tell()


































