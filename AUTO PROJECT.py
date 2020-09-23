# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 10:52:43 2020

@author: krupa
"""


import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
import seaborn as sns
import matplotlib.pyplot as plt

def rosh(com):
# com=input('Enter name:' )

 globals()[com+'_income']=pd.read_csv(r'R:\Project\{}\{}_income.csv'.format(com,com))
 globals()[com+'_cashflow']=pd.read_csv(r'R:\Project\{}\{}_cashflow.csv'.format(com,com))
 globals()[com+'_balance']=pd.read_csv(r'R:\Project\{}\{}_balance.csv'.format(com,com))

 print(globals()[com+'_income'].head())


 cashflow1=globals()[com+'_cashflow'].set_index('field_name').T
 cashflow1=cashflow1.reindex(index=cashflow1.index[::-1])
 income1=globals()[com+'_income'].set_index('field_name').T
 income1=income1.reindex(index=income1.index[::-1])
 balance1=globals()[com+'_balance'].set_index('field_name').T
 balance1=balance1.reindex(index=balance1.index[::-1])


 globals()[com+'_new']=pd.concat([cashflow1,income1,balance1], axis=1)

 msft_null=globals()[com+'_new'].isnull().sum()
 msft_null

 globals()[com+'_new']=globals()[com+'_new'].dropna(axis=1, how='all')
 #msft_columns=new_msft.columns.to_list()
 #msft_columns1=new_msft.columns.to_list()

 imputer= SimpleImputer(missing_values=np.nan,strategy='mean')
 imputer=imputer.fit(globals()[com+'_new'])
 globals()[com+'_final']=pd.DataFrame(imputer.transform(globals()[com+'_new']), index=globals()[com+'_new'].index, columns=globals()[com+'_new'].columns)

def profit(Net_income,
           share_holder,
           Total_Asset,
           Total_current_liability,
           EPS,
           Revenue,
           Total_Liabilities,
           Long_Term_Debt,
           Cost_Of_Goods_Sold,
           Research_And_Development_Expenses,
           SGA_Expenses,
           Total_Current_Assets,
           Cash_Flow_From_Operating_Activities,
           Net_Change_In_Property_Plant_And_Equipment,
           Total_Depreciation_And_Amortization_Cash_Flow):
    
 globals()[com+'_final'][com+'_roa']=(Net_income/Total_Asset)*100
 globals()[com+'_final'][com+'_roe']=(Net_income/share_holder)*100
 globals()[com+'_final'][com+'_roce']=(Net_income/(share_holder+Total_current_liability))*100
 

 fig,ax=plt.subplots()
 ax.plot(globals()[com+'_final'].index, globals()[com+'_final'][com+'_roa'], marker="o",linestyle='--',label=com+'_roa')
 ax.plot(globals()[com+'_final'].index, globals()[com+'_final'][com+'_roe'], marker="o",linestyle='-.',label=com+'_roe')
 ax.plot(globals()[com+'_final'].index, globals()[com+'_final'][com+'_roce'], marker="o",label=com+'_roce')
 plt.xticks(rotation=90)
 ax.set_xlabel("year")
 ax.set_ylabel("msft profitability indicators")
 leg = ax.legend()
 plt.show()
 
 
 fig,ax=plt.subplots()
 ax.plot(globals()[com+'_final'].index, globals()[com+'_final']['EPS - Earnings Per Share'], marker="o",linestyle='--',label="msft_eps")
 plt.xticks(rotation=90)
 ax2=ax.twinx()
 ax2.plot(globals()[com+'_final']['EPS - Earnings Per Share'].pct_change()*100, marker='o',label="Percent increase")
 ax.set_xlabel("year")
 ax.set_ylabel("Yearly Earning per share")
 ax2.set_ylabel("Percent increase")
 leg = ax.legend()
 plt.show()
 
 globals()[com+'_final'][com+'_profit_margin']=((Net_income/Revenue)*100)

 fig,ax=plt.subplots()
 ax.plot(globals()[com+'_final'].index, globals()[com+'_final']['Revenue'], marker="o",linestyle='--',label="msft_revenue")
 ax.plot(globals()[com+'_final'].index, globals()[com+'_final']['Net Income'], marker="o",linestyle='-.',label="msft_net_income")
 plt.xticks(rotation=90)
 ax2 = ax.twinx()
 ax2.plot(globals()[com+'_final'][com+'_profit_margin'])
 ax.set_xlabel("year")
 ax.set_ylabel("Income")
 ax2.set_ylabel("Profit_margin")
 leg = ax.legend()
 plt.show()
 
 globals()[com+'_final']['msft_DebtRatio']=(Total_Liabilities/Total_Asset)
 globals()[com+'_final']['msft_DE_Ratio']=(Total_Liabilities/share_holder)
 globals()[com+'_final']['msft_long_term_DE_Ratio']=(Long_Term_Debt/share_holder)

 fig,ax=plt.subplots()
 ax.plot(globals()[com+'_final'].index, globals()[com+'_final'][com+'_DebtRatio'], marker="o",linestyle='--',label="msft_Debt Ratio")
 ax.plot(globals()[com+'_final'].index, globals()[com+'_final'][com+'_DE_Ratio'], marker="o",linestyle='-.',label="msft_DE_Ratio")
 ax.plot(globals()[com+'_final'].index, globals()[com+'_final'][com+'_long_term_DE_Ratio'],marker="o",label="msftlong term_DE_Ratio")
 plt.xticks(rotation=90)
 ax.set_xlabel("year")
 ax.set_ylabel("Debt Ratio")
 leg = ax.legend()
 plt.show()
 
 fig,ax=plt.subplots()
 ax.plot(globals()[com+'_final']['Operating Income'], marker="o",linestyle='-.',label="msft_Ope_income")
 ax.plot(globals()[com+'_final']['Net Income'], marker="o",linestyle='-.',label="msft_Net_income")
 ax.plot(globals()[com+'_final']['Revenue'], marker="o",linestyle='-.',label="msft_Revenue")
 p1=ax.bar(globals()[com+'_final'].index, globals()[com+'_final']['Cost Of Goods Sold'], color='r',label='COGS Exp')
 p2=ax.bar(globals()[com+'_final'].index, globals()[com+'_final']['Research And Development Expenses'],  bottom=globals()[com+'_final']['Cost Of Goods Sold'], color='b',label='R & D Exp')
 p3=ax.bar(globals()[com+'_final'].index, globals()[com+'_final']['SG&A Expenses'],bottom=globals()[com+'_final']['Cost Of Goods Sold']+globals()[com+'_final']['Research And Development Expenses'], color='g',label='SG & A Exp')


 plt.xlabel('Years', fontsize=12)
 plt.ylabel('Expenses', fontsize=12)
 plt.legend(handles=[p1,p2,p3])
 leg = ax.legend()
 plt.xticks(rotation=90)
 
 globals()[com+'_final'][com+'_current_ratio']=(Total_Current_Assets/Total_current_liability)
 fig,ax=plt.subplots()
 ax.plot(globals()[com+'_final']['msft_current_ratio'], marker="o",linestyle='--',label="msft_Current_ratio")
 leg=ax.legend()
 plt.xticks(rotation=90)
 
 globals()[com+'_final']['OCF/Rev']=((Cash_Flow_From_Operating_Activities/Revenue)*100)
 globals()[com+'_final']['FCF/OCF']=(((Cash_Flow_From_Operating_Activities
                      -(Net_Change_In_Property_Plant_And_Equipment+
                        Total_Depreciation_And_Amortization_Cash_Flow))
                      /Cash_Flow_From_Operating_Activities)*100)
 
 fig, ax=plt.subplots()
 ax.plot(globals()[com+'_final']['OCF/Rev'], marker="o",linestyle='--',label="msft_OCF/Rev")
 ax.plot(globals()[com+'_final']['FCF/OCF'], marker="o",linestyle='--',label="msft_FCF/OCF")
 leg=ax.legend()
 plt.xticks(rotation=90)
 

print('Hello, please, come to dash board. Are you ready?')
start=input("Enter yes or no (Enter only Y or N): ")
if start.lower() == 'y':
      print('good to go, Please, enter first four letters of the company')
      com=input('Give me company name to work :')
      if len(com)!=4:
           print('sorry,I only need first four letters')
      else:
           print('excellent')
           rosh(com)
           profit(globals()[com+'_final']['Net Income'],
                  globals()[com+'_final']['Share Holder Equity'],
                  globals()[com+'_final']['Total Assets'],
                  globals()[com+'_final']['Total Current Liabilities'],
                  globals()[com+'_final']['EPS - Earnings Per Share'],
                  globals()[com+'_final']['Revenue'],
                  globals()[com+'_final']['Total Liabilities'],
                  globals()[com+'_final']['Long Term Debt'],
                  globals()[com+'_final']['Cost Of Goods Sold'],
                  globals()[com+'_final']['Research And Development Expenses'],
                  globals()[com+'_final']['SG&A Expenses'],
                  globals()[com+'_final']['Total Current Assets'],
                  globals()[com+'_final']['Cash Flow From Operating Activities'],
                  globals()[com+'_final']['Net Change In Property, Plant, And Equipment'],
                  globals()[com+'_final']['Total Depreciation And Amortization - Cash Flow'])
elif start.lower() == 'n':
      print('Please, take your time and come later')  
else: 
    print("Please enter yes or no.") 
    

 

