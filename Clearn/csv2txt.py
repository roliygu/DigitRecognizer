# coding: utf-8

import csv
import random

Train  = '../Data/train.csv'
Test   = '../Data/test.csv'
OutPut = '../Data/output.txt'
TrainBit = '../Data/trainbit.txt'
TestBit = '../Data/testbit.txt'
NumFile = ["../Data/Num"+str(i) for i in range(10)]
TestFile = ["../Data/Test"+str(i) for i in range(10)]


def line2list(line):
	return [line[i*2] for i in range(28)]

#def makeTrainData(filename, )

class OneNumber:
	def __init__(self, List, lab):
		'''
		 从一个长度为28,每个元素为一行字符串的列表中格式化成28*28的数字列表
		'''
		self.data = [int(List[i*2]) for i in range(28)]
		self.label = lab

def load_csv2list(CSV):
	# 装载csv数据,并转成列表
	csvfile = file(CVS, 'rb')
	L = list(csv.reader(csvfile))
	csvfile.close()
	return L

def load2list(filename):
	# 装载filename数据,并转成列表,filename是str
	datafile = open(filename, 'r')
	L = list(datafile.readlines())
	datafile.close()
	return L

def csv2txt(CVS, TXT):
	# 将csv转成txt,得到的txt末尾多一换行,需手动去掉
	csvfile = file(CVS, 'rb')
	txtfile = file(TXT, 'w')
	reader = csv.reader(csvfile)
	for i in reader:
		for j in i:
			txtfile.write(j)
			txtfile.write(' ')
		txtfile.write('\n')
	csvfile.close()
	txtfile.close()
	print "CSV2TXT Completed\n"

def LoadDataCVS(add):
	# 
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
	File = [open(i,'w') for i in NumFilek]
	index = 0 
	while index < len(Allines):
		setNum(Allines, index)
		index += 29
	for i in File:
		i.close()

def getNum_Divide():
	# 从单独的数字文件中得到数字,分成10个测试集
	def wri(rlist, wfile, start, numer):
		for i in range(numer):
			wfile.write(rlist[start+i])
		return start+numer
	readfile = [open(i,'r') for i in NumFile]
	writefile = [open(i,'w') for i in TestFile]
	readfilelines = [i.readlines() for i in readfile]
	for i in range(10):
	Num = [413,468,417,435,407,379,413,440,406,418]
	for i in range(10):
		index = 0
		for j in range(10):
			index = wri(readfilelines[i], writefile[j], index, 28*Num[i])

def get_TestTrain():
	# 从10个测试集中随机选9个做训练集,一个做测试集
	L = [i for i in range(10)]
	random.shuffle(L)
	train = L[:9]
	test = L[10]




def Show(D):
	outfile = open(OutPut,'w')
	for i in range(28):
		for j in range(28):
			outfile.write(str(D[i*28+j]))
			outfile.write(' ')
		outfile.write('\n')
	outfile.close()

