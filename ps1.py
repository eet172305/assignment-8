###### this is the first .py file ###########

####### write your code here ##########

class cell:
    def __init__(self, char):
        self.char = char
        self.top = 0
        self.down = 0
	self.left=0
	self.right=0
	self.val=0;
	self.visit=0;
# find the largest and second largest elemet in the matrix
def Range(list1): 
	if( len(list1) >0):
		largest = list1[0] 
		largest2 = list1[0]  
		for item in list1:        
			if item > largest:  
				largest = item 
			elif largest2!=largest and largest2 < item: 
				largest2 = item       
		print("Largest element is:", largest*4+1) 
		print("Second Largest element is:", largest2*4+1) 

m = int(input("Enter k1 "))# enter k1
n = int(input("Enter k2 "))# enter k2
matrix = []; columns = []
for i in range(0,m):
  matrix += [0]
# initialize the number of columns
for j in range (0,n):
  columns += [0]
# initialize the matrix
for i in range (0,m):
  matrix[i] = columns
for i in range (0,m):
	matrix[i]=raw_input().split(" ") # input matrix row from user

array=[]
# defind structure matrix
mat = [[0 for x in range(m)] for x in range(n)]
# initialize the new matrix
for i in range(m):
	for j in range(n):
		mat[i][j]=cell(matrix[i][j])
# assign the values of top left up down from the original matrix
for i in range(m):
	for j in range(n):
		if (mat[i][j].char == 'S'):
			if (i-1>=0  and mat[i-1][j].char =='S'):
				mat[i][j].top=mat[i][j].top+1
			if (i+1<n  and mat[i+1][j].char =='S'):
				mat[i][j].down=mat[i][j].down+1
			if (j-1>=0  and mat[i][j-1].char =='S'):
				mat[i][j].left=mat[i][j].left+1
			if (j+1<n  and mat[i][j+1].char =='S'):
				mat[i][j].right=mat[i][j].right+1
			mat[i][j].val=min(mat[i][j].left,mat[i][j].right,mat[i][j].top,mat[i][j].down)
			array.append(mat[i][j].val)
# function call for the largest and second largest grid
Range(array) 

