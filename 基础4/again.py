#coding:UTF-8
#2017.10
import linecache
import time

#help(time)
right_now = time.localtime()
print (right_now)
now = time.time()

data_keys = ('bid','uid','username','v_class',\
	'content','img','time','source','rt_num',\
	'cm_num','rt_uid','rt_username','rt_v_class',\
	'rt_content','rt_img','src_rt_num','src_cm_num',\
	'gender','rt_mid','location','rt_mid','mid','lat',\
	'lon','lbs_type','lbs_title','poiid','links','hashtags',\
	'ats','rt_links','rt_hashtags','rt_ats','v_url','rt_v_url')

keys = {data_keys[k]:k for k in xrange(0,len(data_keys))}

f = linecache.getlines('t.txt')
lines = [x[1:-2].split('","') for x in f]
#print type(x[1:-1])
#help(str.split)



#1 输出用户总数

people = [ line[keys["username"]] for line in lines]
user = set(people)
user_total = len(user)
print (user_total)


#2.该文本里，每一个用户的名字。

name = list(user)
#print (name)

#3 有多少个2012年11月发布的tweets

lines_from_201211 = filter( lambda line:line[keys['time']].startswith('2012-11'),lines)

num_of_201211 = len(lines_from_201211)

print (num_of_201211)

#4.该文本里，有哪几天的数据？ （要求：输出为一个list，例：['2012-03-04','2012-03-05']）
date = list(set( line[keys['time']].split(' ')[0] for line in lines ) )
date.sort()
print (date)




