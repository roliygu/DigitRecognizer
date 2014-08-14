DigitRecognizer
===============

a competition in kaggle

###数据规格
* 28*28的点阵,每个像素点为[0,255]的值
* 0到9分别有4132,4684,4177,4351,4072,3795,4137,4401,4063,4188个训练数据

当前任务,读十个测试文件中的数据,随机把9个的数据合成train.剩一个做test.
test中元素的个数为4196个







外部文件以CSV或TXT结尾
TrainCSV:
	原始TRAINCSV文件
TestCSV:
	原始TESTCSV文件
RowTrainTXT:
	根据TrainCSVList分发成10个文件,每个文件保存对应数字的原始数值,并且已经28个一行分好行,数字与数字之间不分行
RowTestTXT:
	根据TestCSVList得到的1个文件,保存测试数据
MixtureTrainTXT:
	将10个BitTrainList各自分10份,10个BitTrainList拼接而来的10个MixtureTrainTXT

内部对象以List,Number或Data结尾
TrainCSVList:
	TrainCSV去掉第一行表头的列表L,列表的元素是785长的列表LL,LL首元素是标签,LL其他元素是[0,255]的数值
TestCSVList:
	TestCSV直接读来的列表L,列表元素是784长的列表LL,LL元素是[0,255]的数值
BitTiranList:
	每个RowTrainTXT对应一个BitTiranList,也就是说存在10个BitTiranList;每个BitTiranList是二维0/1列表,第一维长度是RowTrainTXT行数,第二维长度是28
BitTestList:
	BitTestList从RowTestTXT而来
TrainData:
	MixtureTrainTXT任取其9组成训练集
TestData:
	MixtureTrainTXT取剩下一份,做测试集
