# coding: utf-8

import csv

Train  = '../Data/train.csv'
Test   = '../Data/test.csv'
OutPut = '../Data/output.txt'
TrainBit = '../Data/trainbit.txt'
TestBit = '../Data/testbit.txt'

def csv2txt(CVS, TXT):
	csvfile = file(CVS, 'rb')
	reader = csv.reader(csvfile)
	for i in reader:
		L.append(i)
	csvfile.close()
	txtfile = file(TXT,'w')
	for i in L:
		for j in i:
			txtfile.write(j)
			txtfile.write(' ')
		txtfile.write('\n')
	txtfile.close()
	print "Tranced Completed\n"

def LoadDataCVS(add):
	# 返回每个数据785维的全部数据列表
	Data = []
	count=0
	csvfile = file(add, 'rb')
	reader = csv.reader(csvfile)
	for i in reader:
		if count != 0:
			Temp = [int(j) for j in i]
			Data.append(Temp)
		count+=1
	print "LoadCVS Completed\n"
	return Data

def DealWithCVS(oldData):
	# 将Data转成bit点阵,转存到Bit文件
	def ren(n):
		if n==0:
			return 0
		else:
			return 1
	file = open(TestBit, 'w')
	for i in oldData:	
		index = 0
		for j in i:
			file.write(str(ren(j)))
			file.write(' ')
			if index%28==27:
				file.write('\n')
			index+=1

def StrRow2L(S):
	# 将一行字符串转成列表
	L = []
	for i in range(len(S)/2):
		L.append(int(S[i*2]))
	return L

def Divide():
	# 从bit点阵中读出数字,分发到各自的文件中
	def setNum(L,index):
		num = int(L[index][0])
		for i in range(1,29):
			File[num].write(L[i+index])
		return index+29
	file = open(TrainBit, 'r')
	Allines = file.readlines()
	Add = "../Data/Num"
	S = [ Add+str(i) for i in range(10)]
	File = [open(S[i],'w') for i in range(10)]
	index = 0 
	while index < len(Allines):
		setNum(Allines, index)
		index += 29
	for i in File:
		i.close()



def Show(D):
	outfile = open(OutPut,'w')
	for i in range(28):
		for j in range(28):
			outfile.write(str(D[i*28+j]))
			outfile.write(' ')
		outfile.write('\n')
	outfile.close()

