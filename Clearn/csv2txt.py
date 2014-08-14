# coding: utf-8

import csv
import random
import numpy as np
import datetime

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
TempTest = '../Data/TempTest'

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

def testRead():
	File = file(TempTest, 'r')
	Filelines = File.readlines()
	return F(Filelines,0)

def getStrokeDensity(List):
	# List是28*28的列表,得到笔划密度,长度为14
	index = [0,4,8,12,16,20,24]
	L = []
	for i in index:
		count = 0
		for j in range(28):
			if List[i][j] == 1:
				count += 1
		L.append(count)
	for i in index:
		count = 0
		for j in range(28):
			if List[j][i] == 1:
				count += 1
		L.append(count)
	return L

def getOutline(twoList):
	def getLR(oneList):
		# 返回的是某一维列表第一个'1'和最后一个'1'的下标
		# 如果返回的start=0,说明该行全为0
		start = 0
		end = 27
		for i in range(28):
			if oneList[i] == 1:
				start = i
				break
		if start != 0:
			while oneList[end] == 0 :
				end -= 1
		return (start, end)
	def getHL(twoList,index):
		start = 0
		end = 27
		for i in range(28):
			if twoList[i][index]==1:
				start = i
				break
		if start != 0:
			while twoList[end][index] == 0:
				end -= 1
		return (start, end)
	def Max(Tup):
		mmax = -1
		for i in Tup:
			if i[0]!=0 and i[1]-i[0]>mmax:
				mmax = i[1]-i[0]
		return mmax
	def getDiffMax(List, n):
		# n=0表示左差,n=1表示右差
		L = []
		for i in range(28):
			if i != 27:
				if List[i][0]==0 or List[i+1][0]==0:
					continue
				else:
					L.append(List[i+1][n]-List[i][n])
		return L
	def getWMinMax(List):
		minL = 30
		minR = 30
		maxL = -1
		maxR = -1
		for i in List:
			if i[0]!=0:
				if i[0]<minL:
					minL = i[0]
				if i[1]<minR:
					minR = i[1]
				if i[0]>maxL:
					maxL = i[0]
				if i[1]>maxR:
					maxR = i[1]
		return minL,minR,maxL,maxR
	Wide = [getLR(i) for i in twoList]
	Height = [getHL(twoList, i) for i in range(28)]
	MaxWide = Max(Wide)
	MaxHeight = Max(Height)
	Rate = MaxWide*1.0/28
	RateofWH = MaxWide*1.0/MaxHeight
	LDiff = getDiffMax(Wide, 0)
	RDiff = getDiffMax(Wide, 1)
	(MinL,MinR,MaxL,MaxR) = getWMinMax(Wide)
	(MinLD,MinRD,MaxLD,MaxRD) = (min(LDiff),min(RDiff),max(LDiff),max(RDiff))
	LP = abs(MinLD)+abs(MaxLD)
	RP = abs(MinRD)+abs(MaxRD)
	return [MaxWide,MaxHeight,round(Rate,4),round(RateofWH,4),MinL,MinR,MaxL,MaxR,MinLD,MinRD,MaxLD,MaxRD,LP,RP]

def getShadow(twoList):
	# 得到8个边框的的投影长度,和4个中间投影,共12个特征
	def countOne(L):
		count = 0
		for i in L:
			if i==1:
				count +=1
		return count
	up1 = [0*i for i in range(14)]
	up2 = [0*i for i in range(14)]
	down1 = [0*i for i in range(14)]
	down2 = [0*i for i in range(14)]
	for i in range(7):
		for j in range(14):
			if twoList[i][j]==1:
				up1[j] = 1
			if twoList[i][j+14]==1:
				up2[j] = 1
			if twoList[i+21][j]==1:
				down1[j] = 1
			if twoList[i+21][j+14]==1:
				down2[j] = 1
	left1 = [0*i for i in range(14)]
	left2 = [0*i for i in range(14)]
	right1 = [0*i for i in range(14)]
	right2 = [0*i for i in range(14)]
	for i in range(14):
		for j in range(7):
			if twoList[i][j]==1:
				left1[i] = 1
			if twoList[i+14][j]==1:
				left2[i] = 1
			if twoList[i][j+21]==1:
				right1[i] = 1
			if twoList[i+14][j+21]:
				right2[i] = 1
	mid1 = [0*i for i in range(7)]
	mid2 = [0*i for i in range(7)]
	mid3 = [0*i for i in range(7)]
	mid4 = [0*i for i in range(7)]
	(StartX, StartY) = (7, 7)
	for i in range(7):
		for j in range(7):
			if twoList[StartX+i][StartY+j] == 1:
				mid1[i] = 1
				mid4[j] = 1
			if twoList[StartX+i+7][StartY+j] == 1:
				mid1[i] = 1
				mid2[j] = 1
			if twoList[StartX+i+7][StartY+j] == 1:
				mid2[j] = 1
				mid3[i] = 1
			if twoList[StartX+i+7][StartY+j+7]:
				mid3[i] = 1
				mid4[j] = 1
	L = [countOne(i) for i in [up1,up2,down1,down2,left1,left2,right1,right2,mid1,mid2,mid3,mid4]]
	return L

def getCore(twoList):
	def getDisCore(x,y):
		# 得到四个小块的重心矩
		CoreCount = 0
		for i in range(x+1):
			tempsum = 0
			for j in range(y+1):
				tempsum += (i-countM)*(j-countN)
			CoreCount+=tempsum
		return round(CoreCount,4)
	count = 0
	for i in range(28):
		for j in range(28):
			if twoList[i][j]==1:
				count+=1
	countM = 0
	for i in range(28):
		sumM = 0
		for j in range(28):
			sumM += twoList[i][j]*j*1.0/count
		countM += sumM
	countM = round(countM,4)
	countN = 0
	for i in range(28):
		sumN = 0
		for j in range(28):
			sumN += twoList[i][j]*i*1.0/count
		countN += sumN
	countN = round(countN,4)
	CoreDis = [getDisCore(i[0],i[1]) for i in [(0,0),(0,1),(1,0),(1,1)]]
	return [countN, countM]+CoreDis

def getFirstBlackPoint(twoList):
	# 返回角线上首个黑点的位置,四个二维点
	L = []
	for i in range(28):
		if twoList[i][i] == 1:
			L += [i,i]
			break
	for i in range(28):
		if twoList[27-i][27-i] == 1:
			L += [27-i, 27-i]
			break
	for i in range(28):
		if twoList[27-i][i] == 1:
			L += [27-i,i]
			break
	for i in range(28):
		if twoList[i][27-i] == 1:
			L += [i, 27-i]
			break
	return L

def getNetBlock(twoList):
	# 将原点阵分成16个小点阵,统计1的个数,得到一个16维列表
	L = []
	for n in range(4):
		for m in range(4):
			count = 0
			for i in range(7):
				for j in range(7):
					if twoList[n*7+i][m*7+j] == 1:
						count +=1
			L.append(count)
	return L

def getFFT(twoList):
	L = []
	FFT = np.fft.fft2(twoList)
	for i in range(4):
		for j in range(4):
			L.append(FFT[i][j])
			L.append(FFT[i][j+24])
			L.append(FFT[i+24][j])
			L.append(FFT[i+24][j+24])
	Min = min(L)
	Max = max(L)
	LL = [round((i-Min)*1.0/(Max-Min),4) for i in L]
	return LL

def getALL(twoList):
	L = getStrokeDensity(twoList)+getOutline(twoList)+getShadow(twoList)+getCore(twoList)+getFirstBlackPoint(twoList)+getNetBlock(twoList)+getFFT(twoList)
	return L

starttime = datetime.datetime.now()	
Data = MixTXT2TrainData()
print "Lade it"
endtime = datetime.datetime.now()	
for i in Data:
	getALL(i[0])
endtime2 = datetime.datetime.now()	
print (endtime2-endtime).seconds
