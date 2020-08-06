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

def rowmurder(in_mat, op_row, perp_row, sub_value): #INPUT(matrix, operation row, row that will be the perpetrator)
	rowsize = corr_size(in_mat) + 1
	if ((rowsize-1)<(op_row or perp_row)) or ((op_row or perp_row) < 1) or (op_row == perp_row):
		print("Invalid row number! No change...")
		return in_mat

	sub_mat = []
	for i in range(len(in_mat)):
		if (i >= rowsize*(op_row-1)) and (i < rowsize*op_row):
			sub_mat.append(in_mat[i] - in_mat[i + rowsize*(perp_row - op_row)]*sub_value)
		else:
			sub_mat.append(in_mat[i])
	return sub_mat	

def column_clear(in_mat):
	corr = corr_size(in_mat)
	for i in range(corr - 1):
		if in_mat[0] == 0:
			sub_value = 0
		else: 
			sub_value = in_mat[ (corr + 1)*(i+1) ] / in_mat[0]

		in_mat = rowmurder(in_mat, i+2 , 1, sub_value)

	return in_mat

def baby_mat(in_mat):
	corr = corr_size(in_mat)
	sub_mat = []
	for i in range(corr + 2, len(in_mat)):
		if (i%(corr+1) != 0):
			sub_mat.append(in_mat[i]) 
	return sub_mat

def adopt(mother, baby):
	corr = corr_size(mother)
	sub_mat = []
	baby_count = 0
	for i in range(len(mother)):
		if (i%(corr+1) != 0) and (i > corr):
			sub_mat.append(baby[baby_count])
			baby_count += 1
		else:
			sub_mat.append(mother[i]) 
	return sub_mat


def triangulate(in_mat):
	corr = corr_size(in_mat)
	in_mat = column_clear(in_mat)			#do the outside
	sub_mat = column_clear(baby_mat(in_mat))	#do the baby

	if corr > 2:					#if not the smallest, then keep going down
		sub_mat = triangulate(sub_mat)
	
	in_mat = adopt(in_mat, sub_mat)			#adopt the baby
	return in_mat


def normalize(in_mat):
	corr = corr_size(in_mat)

	for i in range(corr):
		in_mat = rowchange(in_mat, 1/(in_mat[i*(corr+1) + (i)]) , i + 1, 1)


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
#mat = [1, 5, 6, 8, 	2, 9, 5, 6, 	3, 4, 5, 6]
#mat = [1, 2, 0, 4, 5,  6, 7, 8, 9, 10,  11, 12, 13, 14, 15, 0]
mat = [10, 5, 6, 5, 9, 	2, 6, 5, 5, 9, 	5, 7, 5, 7, 9,	 8, 6, 5, 6, 9]

print('\nOriginal:')
mat_print(mat)

print('\nChanged:')
mat_print(normalize(triangulate(mat)))



