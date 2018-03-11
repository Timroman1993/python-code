#coding:UTF-8
#2017.10
a = "aAsmr3idd4bgs7Dlsf9eAF"
#help(str)
print ("the orginal one:"),
print a 
print ("already changed one:"),
print (a.swapcase())
numlist = []
for x in a:
	if x.isdigit():
		numlist.append(x)
	else:
		pass
print (numlist)
print "".join(numlist)

#{ 'a':4,'b':2 }
a = a.lower()    
c = dict( [ (x,a.count(x)) for x in set(a) ] )
print (c)

a = "aAsmr3idd4bgs7Dlsf9eAF"
b = list(set(a))
print "".join(b)
a = "aAsmr3idd4bgs7Dlsf9eAF"
a_list = list(a) #string转为list
back_a_list = list( set(a_list) ) #用set去重，再转回list形式
back_a_list.sort( key=a_list.index ) #以原来a的顺序进行排列

print ( "".join(back_a_list) )  #不带‘’的输出

a = "aAsmr3idd4bgs7Dlsf9eAF"
print a
print a[-1::-1]

'''
去除a字符串内的数字后，
请将该字符串里的单词重新排序（a-z），并且重新输出一个排序后的字符 串。（保留大小写,a与A的顺序关系为：A在a前面。例：AaBb）
'''

a = "aAsmr3idd4bgs7Dlsf9eAF"
b = [x for x in a if  not x.isdigit()]
c = "".join(b)
print c

upperlist = []
lowerlist = []
#print dir(a)
for x in c :
	if x.islower():
		lowerlist.append(x)
	else:

		upperlist.append(x)

print(upperlist)
print(lowerlist)
#help(str.find)  'list' object has no attribute 'find' 

for y in upperlist:
	ylow = y.lower()
	if ylow in lowerlist:
		lowerlist.insert(lowerlist.index(ylow),y)
print ( "".join(lowerlist) )

#请判断 'boy'里出现的每一个字母，是否都出现在a字符串里。如果出现，则输出True，否则，则输 出False.

a = "aAsmr3idd4bgs7Dlsf9eAF"
#search = list("boy")
search = "boygirlbirddirty"
print type(search)
size = len(search)
print size
i = 0
target = 0
'''
while i<size:
	
	for x in a :
		if search[i]==x:
			target = 1
    	else:
    		pass
    i = i+1

if target==1 :
	print ("already have")
else:
	if target==0:
		print ("do not have")
 	else:
 		pass
'''
while i<size:
	for x in a:
		if search[i]==x:
			target=1
		else:
			pass
	i=i+1
if target==1:
	print("already have")
elif target==0:
	print ("do not have")
else:
	pass


a = "aAsmr3idd4bgs7Dlsf9eAF"
s = [(x,a.count(x)) for x in set(a)] 
print (type(s))
print (s)
'''
valuelist = s.values()
valuelist.sort(reverse = True)
print valuelist

'''
s.sort( key = lambda k:k[1],reverse = True)
print (s[0][0])



















