#!/usr/bin/python
#coding:UTF-8
#2017.10
a = "aAsmr3idd4bgs7Dlsf9eAF"
print type(a)
#help(str)
#大小写转换
print (a)
print("大小写转换后"),
print (a.swapcase())
#取出数字成新列表
b = "".join( [ s for s in a if s.isdigit() ] )  #注意是s.isdigit(),因为是对s进行的判断. s是a中的每一项 ——>
print (b)
#请统计a字符串出现的每个字母的出现次数（忽略大小写，a与A是同一个字母），并输出成一个字典。 例 {'a':4,'b':2}
a = a.lower()
print  ( dict( [ (x,a.count(x)) for x in set(a) ] )  ) #用set(a)是为了去重,不去重，dict赋值会出错

#请去除a字符串多次出现的字母，仅留最先出现的一个。例 'abcabb'，经过去除后，输出 'abc'
a = "aAsmr3idd4bgs7Dlsf9eAF"
a_list = list(a) #string转为list
back_a_list = list( set(a_list) ) #用set去重，再转回list形式
back_a_list.sort( key=a_list.index ) #以原来a的顺序进行排列
print("去重之后字符为："),
print ( "".join(back_a_list) )  #不带‘’的输出

#将a字符串反转并输出。例：'abc'的反转是'cba'

#注意 string 里面没有reverse
print("反序输出字符串："),
print a[::-1]

'''
去除a字符串内的数字后，请将该字符串里的单词重新排序（a-z），
并且重新输出一个排序后的字符串。（保留大小写,a与A的顺序关系为：A在a前面。例：AaBb）
思路：先排序，把大小写f分别放入两个表，然后再把大写的插在小写前面
'''
l = sorted(a)  #string没有.sort  
print l
 
lower_list = []
upper_list = []

for x in l:
	if x.islower():
		lower_list.append(x)
	elif x.isupper():           #注意elif的用法
	    upper_list.append(x)
	else:
		pass


print (lower_list)
print ( upper_list)


for y in upper_list:
	y_lower = y.lower()                                        #如果大写字母表中的字母在小写字母表中也能找到，则插入
	if y_lower in lower_list:
		lower_list.insert( lower_list.index(y_lower),y )       #insert（位置，对象）
		 #str.index(str, beg=0, end=len(string) ） str -- 指定检索的字符串  beg -- 开始索引，默认为0  end -- 结束索引，默认为字符串的长度。
         # .insert()返回一个位置，这个位置中插入y
print ( "".join(lower_list))

#请判断 'boy'里出现的每一个字母，是否都出现在a字符串里。如果出现，则输出True，否则，则输 出False.
'''
b = 'boy'
c = list(b)
print c
x= -1
while x <len(c) :
	x = x+1
	if c[x] in a:
		print "ture"
	else:
		print "false"
'''

search = 'boy'
u = set(a)
u.update(list(search))    #如果是插入了新的字符，长度会增加
print len(set(a)) == len(u)   

'''
要求如1.7，此时的单词判断，由'boy'改为四个，
分别是 'boy','girl','bird','dirty'，请判断如上这4个字符串里的每个字母，是否都出现在a字符串里。
'''
a = "aAsmr3idd4bgs7Dlsf9eAF"
search = ['boy','girl','bird','dirty']
b = set(a)
for i in search:
	b.update(list(i))
print ( len(b) == len(set(a)) )

#输出a字符串出现频率最高的字母
l =  ( [ (x,a.count(x) )for x in set(a) ] )
l.sort( key= lambda k:k[1], reverse = True)  #key是用哪个排序，用（  ）里面第二个 即k[1]来排序
print l[0][0]

#在python命令行里，输入import this 以后出现的文档，统计该文档中，"be" "is" "than" 的出现次数。

import os  #os模块可直接在程序中执行命令
m = os.popen('python -m this').read() # -m this 等价于 import this ，这条语句可以执行并读出来里面内容
print type(m)
m = m.replace('\n',' ')   #将换行符改为空格，因为有时候换行会改变语意
#help(m.split)
l = m.split(' ')  #变成list形式 便于之后查找 用空格分开单词  
#type（l)
print ( [ ( x,l.count(x) ) for x in [ 'be','is','then' ] ])



#一文件的字节数为 102324123499123，请计算该文件按照kb与mb计算得到的大小。
size = 102324123499123
kb = size>>10
mb = size>>20

#  a =  [1,2,3,6,8,9,10,14,17],请将该list转换为字符串，例如 '123689101417'.
'''
a = [1,2,3,6,8,9,10,14,17]
b = str(a)[1:-1]  #取出来，去掉[]
print (b)
c = b.replace(",","")
print (c)
'''
a = [1,2,3,6,8,9,10,14,17]
b = str(a)[1:-1].replace(',','')
print b

