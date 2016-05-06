#!/usr/bin/env python
# encoding: utf-8
import xlrd
data = xlrd.open_workbook('duizhang.xlsx')
table1 = data.sheets()[0]
table2 = data.sheets()[1]
nrows1 = table1.nrows
ncols1 = table1.ncols
nrows2 = table2.nrows
ncols2 = table2.ncols

for i in range(1,nrows1):
    if table1.cell(i,1).value == u'人工':
        row_begin = i
        print row_begin
        print table1.cell(row_begin,1).value
        break

for i in range(row_begin,nrows1):
    if table1.cell(i,1).value == u'其他':
        row_end = i
        print row_end
        print table1.cell(row_end,1).value
        break
row_end-=1
table1_dict = {}
for i in range(row_begin,row_end+1):
    # print type(table1.cell(i,8).value),table1.cell(i,8).value
    if '-' in table1.cell(i,2).value:
        if isinstance(table1.cell(i,8).value,str):
            table1_dict[table1.cell(i,2).value.split('-')[0]] = table1_dict.setdefault(table1.cell(i,2).value.split('-')[0],0)
        else:
            table1_dict[table1.cell(i,2).value.split('-')[0]] = table1_dict.setdefault(table1.cell(i,2).value.split('-')[0],0)+table1.cell(i,8).value
    else:
        table1_dict[table1.cell(i,2).value] = table1.cell(i,8).value
# print table1_dict
# for i in table1_dict:
#     print i
#     print table1_dict[i]
name_list = table1_dict.keys()
for i in table1_dict:
    for j in range(nrows2):
        if table2.cell(j,3).value==i:
            print table1_dict[i]
            print table2.cell(j,8).value
            if table2.cell(j,8).value!=table1_dict[i]:
                print i,'数值不对'
                name_list.remove(i)
                break
            else:
                print i,'数值正确'
                name_list.remove(i)
print len(name_list)