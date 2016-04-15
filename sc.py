import os

fo = open("sc.txt","r")
s = fo.read()
s= s.split('\n')
for i in s:
	print i
	os.system(i)
