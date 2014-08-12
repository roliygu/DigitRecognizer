# coding: utf-8

# def StrRow2L(S):
# 	# 将一行字符串转成列表
# 	L = []
# 	for i in range(len(S)/2):
# 		L.append(int(S[i*2]))
# 	return L

# def F(add):
# 	file = open(add, 'r')
# 	D = file.readlines()
# 	return D

#D = F('../Data/test')
#print D
#print StrRow2L(D[0])

S = "aaaaaaaaaa"

def F():
	L = []
	for i in range(10):		
		L.append(S[:i]+str(i)+S[i+1:])
	return L

print F()

# file0 = open('../Data/input0.txt','r')
# file1 = open('../Data/input1.txt','r')
# file2 = open('../Data/input2.txt','r')
# file3 = open('../Data/input3.txt','r')
# file4 = open('../Data/input4.txt','r')
# file5 = open('../Data/input5.txt','r')
# file6 = open('../Data/input6.txt','r')
# file7 = open('../Data/input7.txt','r')
# file8 = open('../Data/input8.txt','r')
# file9 = open('../Data/input9.txt','r')


