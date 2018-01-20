# #!/usr/bin/python3
# # -*- cording: UTF-8 -*-
# def lmy( m, n ):
# 	print ("we are in %s"%__name__)
# 	print ( n + m )
#
#
# #if __name__ == '__main__':
# #lmy( 2, 3 )
#
# def lmy1 ( m1 ):
# 	print ( m1 )
#
# #�ĸ�����1234�����û�ظ�����λ��
# def lmyCombina():
# 	for i in range(1, 5):
# 		for j in range (1, 5):
# 			for k in range (1, 5):
# 				if (i != j) and ( i != k) and ( j != k ):
# 					print(i, j, k)
#
#
#
# #һ��������������100�ͼ���268����һ����ȫƽ����
# import math
# def lmySqrt( x ):
# 	for i in range(0, x):
# 		a1 = int (math.sqrt(i + 100))
# 		a2 = int (math.sqrt(i + 268))
# 		if (a1 * a1 == i +100) and (a2 * a2 == i +268):
# 			print(i)
# 		#else:
# 			#print('number is no')
#
#
#
# #����һ���ַ����ֱ�ͳ�Ƴ�����Ӣ����ĸ���ո����ֺ������ַ��ĸ���
#
#
# if __name__ == '__main__':
# 	# ����һ
# 	a = [1,4,6,9,13,16,19,28,40,100,0]
# 	print ('original list is:')
# 	b = len(a)
# 	print(b)
# 	for i in range(len(a)):
# 		print a[i]
# 	number = int(raw_input("insert a new number:\n"))
# 	end = a[9]
# 	if number > end:
# 		a[10] = number
# 	else:
# 		for i in range(10):
# 			if a[i] > number:
# 				temp1 = a[i]
# 				a[i] = number
# 				for j in range(i + 1,11):
# 					temp2 = a[j]
# 					a[j] = temp1
# 					temp1 = temp2
# 				break
# 	for i in range(11):
# 		print a[i]