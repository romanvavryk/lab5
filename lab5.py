from tabulate import tabulate
import nashpy as nash
import numpy as np
from scipy.optimize import linprog
np.set_printoptions(suppress=True)

f_string = [i.strip('\n').split(',') for i in open('data.txt')]
def fileConvert(fileName):
    dataArray = np.loadtxt(fileName)
    return dataArray

for i in range(0 ,5):
	for j in range(0, 5):
		f_string[i][j] = int(f_string[i][j])

for i in f_string:
	print(i)
print()

max_min_arr = []
min_max_arr = []

def solution():
	for i in range(0, 5):
		max_min_arr.append(min(f_string[i]))
	
	for i in range(0, 5):
		compare_list = []
		for j in range(0, 5):
			compare_list.append(f_string[j][i])

		min_max_arr.append(max(compare_list))

	print(min_max_arr)
	print(max_min_arr)
	# print(max_min_arr, min_max_arr)
	max_min = max(max_min_arr)
	min_max = min(min_max_arr)

	# print(max_min, min_max)
	if max_min == min_max:
		saddle_point = []
		saddle_point.append(max_min_arr.index(max_min) + 1)
		saddle_point.append(min_max_arr.index(min_max) + 1)
		value = min_max + max_min

		# print(tabulate(['Straight strategy', res, value], headers=['Strategy','saddle_point','Value'], tablefmt='orgtbl'))
	
	else:
		def reduceRowColDim(a):

		    strategyCheck = []
		    
		    for i in range(len(a[0])):
		        for j in range(len(a[0])):
		            
		            for k in range(len(a[0])-i):
		                if a[i][j] > a[i+k][j]:
		                    strategyCheck.append([i, i+k, a[i][j]])
		                elif a[i][j] < a[i+k][j]:
		                    strategyCheck.append([i+k, i, a[i][j]])
		                elif a[i][j] == a[i+k][j]:
		                    strategyCheck.append([i+k, i, 0])

		    return a                

		A = fileConvert("data1.txt")
		B = A.transpose()

		A = reduceRowColDim(A)
		B = reduceRowColDim(B)

		B_b = np.array([1, 1, 1, 1, 1])
		C_c = B_b

		print("\n/////////////////////////////////////")
		print("Player A: X probalities")
		print("\n")
		res = linprog(-C_c, A, B_b)
		print(res)

		print("\n/////////////////////////////////////")
		print("Player B: Y probalities")
		print("\n")
		res2 = linprog(C_c, -B, -B_b)
		print(res2)
		print("\n/////////////////////////////////////")
		
solution()
