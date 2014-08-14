# coding: utf-8

import csv
import random

TrainCSV  = '../Data/train.csv'
TestCSV   = '../Data/test.csv'
OutPut = '../Data/output.txt'
TrainBit = ['../Data/TrainBit'+str(i) for i in range(10)]
TestBit = '../Data/TestBit'
NumFile = ["../Data/Num"+str(i) for i in range(10)]
TestFile = ["../Data/Test"+str(i) for i in range(10)]
RowTrainTXT = ["../Data/RowTrainTXT"+str(i) for i in range(10)]
RowTestTXT = "../Data/RowTestTXT"
MixtureTrainTXT = ["../Data/MixtureTrainTXT"+str(i) for i in range(10)]
Number = [413,468,417,435,407,379,413,440,406,418]
BULL = '../Data/Bull'

def closeFiles(Files):
	for i in Files:
		i.close()

def CSV2List(CSV):
	# info=0表示是Train,=1是Test
	L = []
	csvfile = file(CSV, 'rb')
	reader = csv.reader(csvfile)
	mark = 0
	for i in reader:
		if mark != 0:
			L.append(i)
		mark = 1
	csvfile.close()
	return L

def CSVList2RowTXT(info, List):
	# info=0表示是Train,=1是Test
	def dealwith784(file, list):
		count = 0
		for i in range(784):
			file.write(str(list[i]))
			file.write(' ')
			if i%28 == 27:
				file.write('\n')
			count+=1
	def dealwith785(list):
		dealwith784(openfile[int(list[0])], list[1:])
	if info == 0:
		openfile = [open(i, 'w') for i in RowTrainTXT]
		for i in List:
			dealwith785(i)
		close = [i.close() for i in openfile]
	else:
		openfile = open(RowTestTXT, 'w')
		for i in List:
			dealwith784(openfile, i)
		openfile.close()	

def RowTXT2BitList(File):
	def change(n):
		if n==0:
			return 0
		else:
			return 1
	def line2list(line):
		L = line.split(" ")
		return [change(int(i)) for i in L[:-1]]
	openfile = open(File, 'r')
	allines = openfile.readlines()
	return [line2list(i) for i in allines]

def List2TXT(File, List):
	for i in List:
		for j in i:
			File.write(str(j))
			File.write(' ')
		File.write('\n')

def BitList2BitTXT(File, BitList):
	openfile = open(File,'w')
	List2TXT(openfile, BitList)
	openfile.close()

def BitList2MixTXT(BitLists):	
	openfile = [open(i, 'w') for i in MixtureTrainTXT]
	def dive2(List, Files, Num):
		# Files是10个文件,BitList是1个List,函数将BitList分发到10个File中
		index = 0
		for i in range(10):
			List2TXT(openfile[i], List[index:index+28*Num])
			index += 28*Num
	for i in range(10):
		dive2(BitLists[i], openfile, Number[i])
	for i in openfile:
		i.close()

def F(List, start):
	# 返回List[start]开始的28行,拼成一个int二维列表
	data = []
	for i in range(28):
		temp = [int(i) for i in List[start+i].split(' ')[:-1]]
		data.append(temp)
	return data

def MixTXT2TrainData():
	Data = []
	openfile = [open(i,'r') for i in MixtureTrainTXT[:-1]]
	for File in openfile:
		Filelines = File.readlines()
		index = 0
		for i in range(10):
			for j in range(Number[i]):
				data = F(Filelines, index)
				Data.append((data,i))
				index+=28
	closeFiles(openfile)
	return Data

def MixTXT2TestData():
	Data = []
	openfile = open(MixtureTrainTXT[9])
	Filelines = openfile.readlines()
	index = 0
	for i in range(10):
		for j in range(Number[i]):
			data = F(Filelines, index)
			Data.append((data,i))
			index+=28
	openfile.close()
	return Data

def Show(DataTup):
	for i in range(28):
		for j in range(28):
			print DataTup[0][i][j],
		print '\n'
	print "####"
	print DataTup[1]

def Write(Data):
	File = open(BULL, 'w')
	for Datatup in Data:
		File.write(str(Datatup[1]))
		for i in range(28):
			for j in range(28):
				File.write(str(Datatup[0][i][j]))
				File.write(' ')
			File.write('\n')
		File.write("#####")
	File.close()
