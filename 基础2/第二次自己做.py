#2017.09
#!/usr/bin/python
#coding:UTF-8

a = [11,22,24,29,30,32]
a.append(28)
print (a)

a.insert(5,54)
#print (a)
del a[5]
#print a

a.insert(4,54)
print (a)
a[0]=6
print (a)
a.sort()
print (a)
print ("------------------------------")

b = [1,2,3,4,5]
b1 = [6,7,8]

b.extend(b1)
print ( b )
print ( b[-4:-6:-1] )   #string [ : ] ,list 有步长，反向搜索记得为负
print (2 in b)


b = [23,45,22,44,25,66,78]

c = [ x for x in b if x%2==1 ]
print c
print (['the content %s' % x for x in b [:2]] )
d = [x+2 for x in b  ]
print ( d )
print ("--------------------------------")

print range(11,40,11)
print [ x for x in range(10,40) if (x/10==x%10) ]
print ("--------------------------------")


a = (1,4,5,6,7)
print (4 in a)
b = list(a)
print (b)
b[2] = 8
print (b)
print (tuple(b))
print("----------------------------------")

setinfo = set('acbdfem')
finfo = set('sabcdef')
setinfo.add('abc')
print (setinfo)
setinfo.remove('m')
print (setinfo)

print (setinfo&finfo)
print (setinfo|finfo)
print ("---------------------------------")
'''
lm = {'name' : 'liming','age' : 25,'chinese' : 80, 'math' : 75, 'english' :85}
zq = dict(name='zhangqiang',age=23, chinese=75, math=82,english=78)

lm.update( {'python':60} )
zq.update( {'python':80} )
print (lm)
print (zq)

zq['math'] = 89
print (zq)

del lm['age']
print (lm)
'''
print ("注意字典的定义")

student = { 'lm':{'name':'lm','age':25,'score':{'chinese':80,'math':75,'english':85} } }
student['zq'] =  {'name':'zq','age':23,'score':{'chinese':75,'math':82,'english':78} } 

print student
student['lm']['score']['python'] = 60
student['zq']['score']['python'] = 60
print (student)

student['zq']['score']['math'] = 89
print student


del student['lm']['age'] 
print student['lm']

print("!!!!!字典内数据排序")

a=student['zq']['score'].values()
print a
a.sort()
print a

print student.pop('city','bj')







