from copy import copy
from mixColTables import *

def mixColumn(column):
	col = copy(column)
	column[0] = table_2[col[0]] ^ table_3[col[1]] ^ col[2] ^ col[3]
	column[1] = col[0] ^ table_2[col[1]] ^ table_3[col[2]] ^ col[3]
	column[2] = col[0] ^ col[1] ^ table_2[col[2]] ^ table_3[col[3]]
	column[3] = table_3[col[0]] ^ col[1] ^ col[2] ^ table_2[col[3]]
	return column


def mixColumns(col):
	outCol = []
	for i in range(0,len(col),4):
		outCol.append(mixColumn(col[i:i+4]))
	return listoflist2singlelist(outCol)

def mixColumnInv(column):
	col = copy(column)
	column[0] = table_14[col[0]] ^ table_11[col[1]] ^ table_13[col[2]] ^ table_9[col[3]]
	column[1] = table_9[col[0]] ^ table_14[col[1]] ^ table_11[col[2]] ^ table_13[col[3]]
	column[2] = table_13[col[0]] ^ table_9[col[1]] ^ table_14[col[2]] ^ table_11[col[3]]
	column[3] = table_11[col[0]] ^ table_13[col[1]] ^ table_9[col[2]] ^ table_14[col[3]]
	return column


def mixColumnsInv(col):
	intList = []
	for i in range(0,len(col),4):
		intList.append(mixColumnInv(col[i:i+4]))
	return listoflist2singlelist(intList)

def listoflist2singlelist(column):
	columnList = []
	for row in column:
		for i in range(0,len(row)):
			columnList.append(row[i])
	return columnList
