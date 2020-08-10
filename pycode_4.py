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
	in_mat = column_clear(in_mat)			#do the outside
	sub_mat = baby_mat(in_mat)			#take the baby

	if corr_size(in_mat) > 2:			#if not the smallest, then triangulate baby
		sub_mat = triangulate(sub_mat)		#baby is now 2x3, so let 3x4 adopt it
	
	in_mat = adopt(in_mat, sub_mat)			#adopt the baby
	return in_mat


def normalize(in_mat):
	corr = corr_size(in_mat)

	for i in range(corr):
		in_mat = rowchange(in_mat, 1/(in_mat[i*(corr+1) + (i)]) , i + 1, 1)
	return in_mat

def row_clear(in_mat):
	corr = corr_size(in_mat)
	for i in range(corr - 1):
		sub_value = in_mat[i+1]
		in_mat = rowmurder(in_mat, 1, i+2, sub_value)
	
	sub_mat = baby_mat(in_mat)
	if corr > 2:
		sub_mat = row_clear(sub_mat)

	in_mat = adopt(in_mat, sub_mat)
	return in_mat

def round(x): #round the small or weird numbers
	if x == -0:
		return 0
	elif (x > 0.9999999999) and (x < 1):
		return 1
	elif (x < 0.0000000001 ) and (x >0):
		return 0
	else:
		return x

def mat_round(in_mat):
	sub_mat = []
	for i in range(len(in_mat)):
		sub_mat.append(round(in_mat[i]))
	return sub_mat


#Finally I can use RREF now...
def rref(in_mat):
	return (mat_round(row_clear(normalize(triangulate(in_mat)))))


def mat_print(in_mat):
	corr = corr_size(in_mat)
	for i in range(len(in_mat)):
		print(in_mat[i], end=" ")
		if ((i+1)% ( corr + 1)) == 0:
			print(' ')

########################## TESTING_BENCH  #########################

#mat = [1, 2, 3, 4, 5, 6, 7, 8, 20]
#mat = [1, 1, 2, 3, 4, 5]
mat1 = [1, 5, 6, 8, 	2, 9, 5, 6, 	3, 4, 5, 6]
mat2 = [10, 5, 46, 5, 9, 	2, 5, 1, -59, 9, 	5, 6, 30, 7, 9,	 8, 14, 5, 6, 12]

########################## PRINTING_BENCH #########################

print('\nOriginal 3x4:')
mat_print(mat1)

print('\nRREF 3x4:')
mat_print(rref(mat1))



print('\nOriginal 4x5:')
mat_print(mat2)

print('\nRREF 4x5:')
mat_print(rref(mat2))





