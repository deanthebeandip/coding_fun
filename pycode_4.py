#RREF CALCULATOR
import math
import numpy as np

def check(n):
	return n**2 + n

def corr_size(in_mat): #return the correct size, 0 if false
	n = 2
	length = len(in_mat)
	while (check(n)) <= length:
		if check(n) == length:
			return n
		n+=1 #update n to search the next n...
	print("Nothing Found!")
	return 0

def rowchange(in_mat, in_val , row_number, option): #INPUT(matrix, value, row number, option[0sub, 1mul])
	rowsize = corr_size(in_mat) + 1
	if ((rowsize-1)<row_number) or (row_number < 1):
		print("Invalid row number! No change...")
		return in_mat

	sub_mat = []
	for i in range(len(in_mat)):
		if (i >= rowsize*(row_number-1)) and (i < rowsize*row_number) and option: #multiply
			sub_mat.append(in_mat[i]*in_val)
		elif (i >= rowsize*(row_number-1)) and (i < rowsize*row_number) : #subtract
			sub_mat.append(in_mat[i]-in_val)
		else:
			sub_mat.append(in_mat[i])
	return sub_mat

def rowmurder(in_mat, op_row, perp_row): #INPUT(matrix, operation row, row that will be the perpetrator)
	rowsize = corr_size(in_mat) + 1
	if ((rowsize-1)<(op_row or perp_row)) or ((op_row or perp_row) < 1) or (op_row == perp_row):
		print("Invalid row number! No change...")
		return in_mat

	sub_mat = []
	for i in range(len(in_mat)):
		if (i >= rowsize*(op_row-1)) and (i < rowsize*op_row):
			sub_mat.append(in_mat[i] - in_mat[i + rowsize*(perp_row - op_row)])
		else:
			sub_mat.append(in_mat[i])
	return sub_mat	




def rref(in_mat):
	#rowmurder(in_mat, op_row, perp_row): Op = Op - Perp
	#rowchange(in_mat, in_val , row_number, option): option 0 sub, 1 mul
	
	#what do i wanna do? when given a correct matrix, i want to keep reducing it until its a 2x3 matrix, the base matrix

	if corr_size(in_mat) == 2: # Base 2x3 case...
		#rowchange(in_mat, )
	else:
		print("Not ready for that matrix yet...")
		
	return in_mat




def mat_print(in_mat):
	corr = corr_size(in_mat)
	for i in range(len(in_mat)):
		print(in_mat[i], end=" ")
		if ((i+1)% ( corr + 1)) == 0:
			print(' ')

########################## TESTING_BENCH ##########################

#mat = [1, 2, 3, 4, 5, 6, 7, 8, 20]
#mat = [1, 1, 2, 3, 4, 5]
mat  = [1, 1, 1, 1, 2, 2, 2, 2, 3, 4, 5, 6]
#mat = [1, 2, 0, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]

mat_print(rref(mat))





