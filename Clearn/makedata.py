# coding: utf-8

import csv
import csv2txt

Train  = '../Data/train.csv'
Test   = '../Data/test.csv'
TrainBit = '../Data/trainbit.txt'
TestBit = '../Data/testbit.txt'

(num,Data) = csv2txt.LoadData(Train)

def DealWith(D):
	
