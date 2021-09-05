# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 11:59:30 2021

@author: Yosef Shor

"""


import csv
import pandas as pd
import numpy as np
from itertools import permutations,combinations

data = pd.read_excel(r'C:\Users\user\Downloads\PPC_data_analyst_test.xlsx')
data.head()

my_data = data.loc[:,['FTD Exists','Gdevice','Lead Status','Initial Lead Status','Call Center (Conversion Owner) (User)','UtmCreative','G_geo cname','User Agent','keyword/targeting method ','network']]

my_data['FTD 0/1'] = [1 if i == 'Yes' else 0 for i in my_data['FTD Exists']]

p = my_data.where(my_data['FTD 0/1'] == 1).dropna()  #.count()
my_data['FTD Exists'].count()
mi[mi['FTD 0/1'] == 1]

the_best_FTD = pd.DataFrame()

information_of_the_great_L2FTD = []


categorys = ['FTD Exists','Gdevice','Lead Status','Initial Lead Status','Call Center (Conversion Owner) (User)','UtmCreative','G_geo cname','User Agent','keyword/targeting method ','network']

my_new_data = my_data.loc[:,['FTD 0/1','Gdevice','Call Center (Conversion Owner) (User)','UtmCreative','G_geo cname', 'keyword/targeting method ','network']]
my_new_categories = ['Gdevice','Call Center (Conversion Owner) (User)','UtmCreative','G_geo cname', 'keyword/targeting method ','network']


def check_ptd(data, i, j, unique_name):
    global information_of_the_great_L2FTD
    sum_of_FTD = np.sum(data['FTD 0/1'])
    sum_of_all_row = len(data['FTD 0/1'])
    if sum_of_FTD > 10:
        print(i, "   ", j, unique_name)
        print("we have here more than 10 segment ")
        L2FTD = np.round((sum_of_FTD / sum_of_all_row) * 100, 2)
        print('FTD = Yes => {}, and the length of all FTD => {}'.format(sum_of_FTD, sum_of_all_row))
#        L2FTD  = str(L2FTD) +'%'
#        print(L2FTD)
        information_of_the_great_L2FTD.append([sum_of_FTD, sum_of_all_row, i, j, unique_name, L2FTD])
    return 

def write_to_excel(the_best_FTD):
    (max_row, max_col) = the_best_FTD.shape
    writer = pd.ExcelWriter('worst_L2FTD.xlsx', engine='xlsxwriter')
    the_best_FTD.to_excel(writer, sheet_name='Sheet1', startrow=1, header=False, index=False)
    workbook = writer.book
    worksheet = writer.sheets['Sheet1']
    column_settings = [{'header': column} for column in the_best_FTD.columns]

    worksheet.add_table(0, 0, max_row, max_col - 1, {'columns': column_settings})
    worksheet.set_column(0, max_col - 1, 12)
    writer.save()
    return


def build_the_max_table(information_of_the_great_L2FTD):
    global the_best_FTD
    the_best_FTD = pd.DataFrame()
    temp_table = pd.DataFrame()
    sorted_by_max = sorted(information_of_the_great_L2FTD, key = lambda x : x[-1], reverse=True)
    sorted_by_max = sorted_by_max[:10]
    for i in sorted_by_max:
        sum_of_FTD, sum_of_all_row, i, j, unique_name, L2FTD = i[0],i[1],i[2],i[3],i[4],i[5]
        print(L2FTD)
      
    df1 = pd.DataFrame(sorted_by_max,columns=['sum_of_FTD_Yes', 'sum_of_FTD', 'category', 'list_categories', 'unique_name', 'L2FTD'])
    write_to_excel(df1)


df1 = pd.DataFrame(columns=['sum_of_FTD_Yes', 'sum_of_all_row', 'category', 'list_categories', 'unique_name', 'L2FTD'])       

df1 = pd.DataFrame(sorted_by_max,columns=['sum_of_FTD_Yes', 'sum_of_FTD', 'category', 'list_categories', 'unique_name', 'L2FTD'])


# =============================================================================
#         mi = pd.concat([my_new_data['FTD 0/1'],my_new_data[j]], axis=1)
#         data = mi.where(mi[i] == unique_name).dropna()
#         temp_table = data[data[i] == unique_name]
#         the_best_FTD = temp_table[temp_table['FTD 0/1'] == 1]
#         the_best_FTD['L2FTD'] = L2FTD
#         write_to_excel(the_best_FTD)
#         
#         
#         df2.to_excel(writer, sheet_name='Sheet1', startcol=3)
#         df3.to_excel(writer, sheet_name='Sheet1', startrow=6)
#       
# =============================================================================

comb = []
for i in range(1,len(my_new_categories)):
    comb += combinations(my_new_categories, i)
comb = [i for i in comb]
m = pd.DataFrame()


for j in comb:
    print(len(j))
    for i in j:
        unique_ids = dictionaty[i]
        for unique_name in unique_ids:
            m = my_new_data.where(my_new_data[i] == unique_name).dropna()
            check_ptd(m, i, j, unique_name)
#            print(p.count())        
        



def check_second_ftd(data, i, j, unique_name):
    global L2FTD_information
    data_1 = [1 if k == unique_name else 0 for k in data[i]]
    
    sum_of_FTD = np.sum(data_1[i])
    sum_of_all_row = len(data_1[i])
    if sum_of_FTD > 10:
        print(i, "   ", j, unique_name)
        print("we have here more than 10 segment ")
        L2FTD = np.round((sum_of_FTD / sum_of_all_row) * 100, 2)
        print('FTD = Yes => {}, and the length of all FTD => {}'.format(sum_of_FTD, sum_of_all_row))
#        L2FTD  = str(L2FTD) +'%'
#        print(L2FTD)
        L2FTD_information.append([sum_of_FTD, sum_of_all_row, i, j, unique_name, L2FTD])
    return 


L2FTD_information = []
comb_L2 = []
l2max_categories = ['Gdevice','UtmCreative','G_geo cname', 'keyword/targeting method ','network']
data_L2_max = my_new_data.where(my_new_data[sorted_by_max[0][2]] == sorted_by_max[0][4]).dropna()
data_L2_max = data_L2_max.where(data_L2_max['FTD 0/1'] == 1).dropna()
data_L2_max1 = data_L2_max.iloc[:,[0,1,3,4,5,6]]

data_l2_two_keys = data_L2_max.iloc[:,[0,2]]

for i in range(1,len(L2max_categories)):
    print(i)
    comb_L2 += combinations(L2max_categories, i)
comb_L2 = [i for i in comb_L2]
l2_dictionaty = {}
for j in L2max_categories:    
    l2_dictionaty[j] = my_data[j].unique()  
data_1 = pd.DataFrame()

for j in comb_L2:
    print(j)
    print(len(j))
    l2_mi = data_L2_max1
#    m = mi
    for i in j:
        l2_unique_ids = l2_dictionaty[i]
        for unique_name in l2_unique_ids:
            l2_mi = l2_mi.where(l2_mi[i] == unique_name).dropna()
            data_1.loc[i] = [1 if k == unique_name else 0 for k in l2_mi[i]]
            sum_of_FTD = np.sum(data_1)
            sum_of_all_row = len(data_1)
            print(sum_of_FTD, sum_of_all_row)  
            check_second_ftd(l2_mi, i, j, unique_name)



data_L2_max = my_new_data.where(my_new_data[sorted_by_max[0][2]] == sorted_by_max[0][4]).dropna()
first = data_L2_max.where(data_L2_max['network'] == 'g').dropna()
second = data_L2_max.where(data_L2_max['Gdevice'] == 'm').dropna()
(max_row, max_col) = first.shape
second = second.where(data_L2_max['network'] == 'g').dropna()
third = data_L2_max.where(data_L2_max['Gdevice'] == 'c').dropna()
third = third.where(data_L2_max['network'] == 'g').dropna()
four = data_L2_max.where(data_L2_max['UtmCreative'] == 'https://www.fortrader.com/').dropna()
four = four.where(data_L2_max['network'] == 'g').dropna()
writer = pd.ExcelWriter('L2FTD_Table.xlsx', engine='xlsxwriter')
second.to_excel(writer, sheet_name='Sheet1', startrow = 1, header=False, index=False)
#workbook = writer.book
#worksheet = writer.sheets['Sheet1']
#column_settings = [{'header': column} for column in second.columns]
#worksheet.add_table(0, 0, max_row, max_col - 1, {'columns': column_settings})
#worksheet.set_column(0, max_col - 1, 12)
#writer.save()

writer = pd.ExcelWriter('Max_L2FTD.xlsx', engine='xlsxwriter')
first.to_excel(writer, sheet_name='report_1')
second.to_excel(writer, sheet_name='report_2')
third.to_excel(writer, sheet_name='report_3')
four.to_excel(writer, sheet_name='report_4')
writer.save()


      
with open(path_file, 'a+') as f:
    df.to_excel(f, header=f.tell() == 0, encoding='utf-8', index=False)
    
def append_df(path_file, df):
    with open(path_file, 'a+') as f:
        df.to_excel(f, header=f.tell() == 0, encoding='utf-8', index=False)

len([i for i in my_data['Gdevice'] if i == 'c'])
len([i for i in my_data['Gdevice'] if i == 't'])
len([i for i in my_data['Gdevice'] if i == 'm'])

df.groupby('STNAME').agg({'CENSUS2010POP': np.average}) 

dictionaty = {}
for j in categorys:    
    dictionaty[j] = my_data[j].unique()  
unique_data_in_my_data = pd.Series(dictionaty)

for k,v in unique_data_in_my_data.items():
    print(k,v)
    


comb = []
for i in range(1,len(my_new_categories)):
    comb += combinations(my_new_categories, i)
comb = [i for i in comb]
m = pd.DataFrame()

for j in comb:
    print(len(j))
    mi = pd.concat([my_new_data['FTD 0/1'],my_new_data[j]], axis=1)
#    m = mi
    for i in j:
        unique_ids = dictionaty[i]
        for unique_name in unique_ids:
            m = mi.where(mi[i] == unique_name).dropna()
            check_ptd(m, i, j, unique_name)
#            print(p.count())    
       
mq = pd.concat([my_new_data['FTD 0/1'], my_new_data['Gdevice','Call Center (Conversion Owner) (User)','UtmCreative']],axis=1)            
perm = [permutations(my_new_categories, i) for i in range(len(my_new_categories))]
for i in list(perm):
    print (next(i))
    
perm = permutations(my_new_categories, 2)
for i in list(perm):
    print (i)    

comb = combinations([1, 2, 3], 2)
comb = list(combinations(my_new_categories, 2))        
mi = pd.concat([my_new_data['FTD 0/1'],my_new_data[comb[0]], axis=1)        
for i in mi[comb[0][0]].unique():
    p = mi.where(mi[comb[0]] == i)      #.dropna()  #.count()
    check_ptd(p)
    print(p.count())
      
        
        
        
        print(i)
        dictionaty[d[2][0]]:
        p = mi.where(mi[comb[0]] == i)      #.dropna()  #.count()
        check_ptd(p)
        print(p.count())
        
mi[comb[0][0]].value_counts(),mi['FTD 0/1'].value_counts()

p = pd.DataFrame(my_new_data.iloc[:,[0,1,2]])
p1 = pd.DataFrame(p.groupby(level = -1)['Gdevice'])

o = pd.Series(my_data.groupby(['Gdevice']).agg({'avg': np.average, 'sum': np.sum}))

print(o.agg({'avg': np.average, 'sum': np.sum})))

   
for i in list(comb):
    print (next(i))   
    
    
    
#df.groupby("A")
#a = my_new_data.groupby(["FTD 0/1"])
#my_new_data.describe() 
#my_new_data['Gdevice'].unique()

my_new_data['keyword/targeting method '].unique()
len(my_new_data['keyword/targeting method '].unique())

for state in df['STNAME'].unique():
    avg = np.average(df.where(df['STNAME'] == state).dropna()['CENSUS2010POP'])
    print('Counties in state ' + state + ' have an average population of ' + str(avg))
    
    
p.fillna(method='ffill')


rows = ['POPESTIMATE2010',
        'POPESTIMATE2011',
        'POPESTIMATE2012',
        'POPESTIMATE2013',
        'POPESTIMATE2014',
        'POPESTIMATE2015']
df.apply(lambda x: np.max(x[rows]), axis = 1)


df = df.set_index('STNAME')

def fun(item):
    if item[0] < 'M':
        return 0
    if item[0] < 'Q':
        return 1
    return 2

for group, frame in df.groupby(fun):
    print('There are ' + str(len(frame)) + ' records in group ' + str(group) + ' for processing.')


df.groupby('STNAME').agg({'CENSUS2010POP': np.average})

(df.set_index('STNAME').groupby(level = 0)['CENSUS2010POP'].agg({'avg': np.average, 'sum': np.sum, 'min':np.min}))

(df.set_index('STNAME').groupby(level = 0)['POPESTIMATE2010','POPESTIMATE2011']
    .agg({'avg': np.average, 'sum': np.sum}))

#p = my_data.where(my_data['FTD Exists'] == 'Yes').dropna()  #.count()
#my_data['FTD Exists'].count()
#p.dropna()
#p.count()



sum_of_FTD = np.sum(my_data['FTD 0/1'])
sum_of_all_row = len(my_data['FTD 0/1'])

L2FTD = np.round((sum_of_FTD / sum_of_all_row) * 100, 2)
L2FTD  = str(L2FTD) +'%'
print(L2FTD)





