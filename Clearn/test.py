# coding: utf-8

def getLR(List):
	# 返回的是某一维列表第一个'1'和最后一个'1'的下标
	start = 0
	end = 27
	for i in range(28):
		if List[i] == 1:
			start = i
			break
	if start != 0:
		while List[end] == 0 :
			end -= 1
	return (start, end)


L1 = [0*i for i in range(28)]
L2 = [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0]
L3 = [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

print getLR(L1)
print getLR(L2)
print getLR(L3)