#!coding = UTF-8
#逢7跳过（1-100）
print ('''
============================

          JUMP7

============================
''')

#for num in range(1,101):
#    if num % 7 != 0 and num % 10 != 7 and num // 10 != 7:
#        print(num)

num = 1
while num <= 100:
	if num % 7 != 0 and num % 10 != 7 and num // 10 != 7:
		print (num)
	num = num + 1
print ("DONE!")
