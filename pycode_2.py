#Determinent calculator
import math
import numpy as np

def rank(in_mat): #return rank
	return int(len(in_mat)**.5)

def square(in_mat): #return if square or not
	if (rank(in_mat))%1 != 0:
		return 0
	else:
		return 1

def det(in_mat): #find determinent
	if not square(in_mat):
		print("Sorry can't help buddy")
	else: #input is square
		if rank(in_mat) == 2:
			return in_mat[0]*in_mat[3] - in_mat[1]*in_mat[2]
		else: #rank could be 3, 4, 5...
			det_sum = 0
			neg = 1
			for j in range(rank(in_mat)):
				sub_mat = [] #declare new array
				for k in range(rank(in_mat), len(in_mat)):
					if (k-j)%(rank(in_mat)) != 0:
						sub_mat.append(in_mat[k]) 
				det_sum += in_mat[j]*det(sub_mat)*neg
				neg*=-1
			return det_sum
				

def mat_print(in_mat):
	for i in range(len(in_mat)):
		print(in_mat[i], end=" ")
		if ((i+1)%rank(in_mat)) == 0:
			print(' ')


#mat = [1, 2, 3, 4]
#mat = [1, 2, 3, 4, 5, 6, 7, 8, 20]
mat = [1, 2, 0, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]
determinent = det(mat)


mat_print(mat)
print('Determinent of given matrix is:', determinent)




