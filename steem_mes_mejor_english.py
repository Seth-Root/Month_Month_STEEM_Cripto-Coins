# -*- coding: utf-8 -*-
# -*- decoding: utf-8 -*-
    
import json  
import datetime 

from operator import itemgetter 



import matplotlib.pyplot as plt
import matplotlib.dates as mdates

import os
#os.system("rm STEEM_2016.json")

#os.system("wget http://coinmarketcap.northpole.ro/api/v5/history/STEEM_2016.json")

data_file= open('STEEM_2016.json')   
data = json.load(data_file)  
data_history = data['history']
    
dict_days = {}  
list_in_BTC = []
list_in_dolar = []
list_dict_days = []
for all_days in data_history:   
                    prices_day = data_history[all_days]['price']
                    in_dolar = prices_day['usd']
                    list_in_dolar.append(in_dolar)
                    in_BTC = prices_day['btc']
                    list_in_BTC.append(in_BTC)
                    all_days = datetime.datetime.strptime(all_days,'%d-%m-%Y')
                    dict_days = {'usd':in_dolar, 'date': all_days, 'btc': in_BTC}
                    list_dict_days.append(dict_days)










n_dict = sorted( list_dict_days, key = itemgetter('date') ,reverse=False)

iterer = 0
print "                "
print "               Value STEEM for 12 months 2016"
print "                "
last_10_days_prices = []
last_10_days_dates = []

value_max_steem = 0
value_min_steem = 100000000000000000000000

dictionary_montsh_value = {}

list_months = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
for dict_dia_a_dia in n_dict:
         iterer += 1

         value_steem_dollar = dict_dia_a_dia['usd']
         value_steem_dollar = float(value_steem_dollar)
         date_day = dict_dia_a_dia['date'].date()
         month = date_day.month
         
         if date_day.day == 1:
                         value_max_steem = 0
                         value_min_steem = 100000000000000000000000
                         
         if date_day.month == 1:
                         if value_steem_dollar > value_max_steem:
                                         value_max_steem = value_steem_dollar
                                         date_value_max = date_day
                                         dictionary_montsh_value["max_value_JAN"] = value_max_steem
                                         dictionary_montsh_value["max_date_JAN"] = date_value_max


                         if value_steem_dollar > value_min_steem:
                                         value_min_steem = value_steem_dollar
                                         date_value_min = date_day
                                         dictionary_montsh_value["min_value_JAN"] = value_min_steem
                                         dictionary_montsh_value["min_date_JAN"] = date_value_min
                         
                         



         
         elif date_day.month == 2:

                         
                         if value_steem_dollar > value_max_steem:
                                         value_max_steem = value_steem_dollar
                                         date_value_max = date_day
                                         print "En ", list_months[month-1], "  el Valor Maximo es:", value_max_steem, "En date", date_value_max
                                         dictionary_montsh_value["max_value_FEB"] = value_max_steem
                                         dictionary_montsh_value["max_date_FEB"] = date_value_max


                         if value_steem_dollar < value_min_steem:
                                         value_min_steem = value_steem_dollar
                                         date_value_min = date_day
                                         print "En ", list_months[month-1], "  el Valor Minimo es:", value_min_steem, "En date", date_value_min
                                         dictionary_montsh_value["min_value_FEB"] = value_min_steem
                                         dictionary_montsh_value["min_date_FEB"] = date_value_min
                         
         


         
         elif date_day.month == 3:
                         
                         if value_steem_dollar > value_max_steem:
                                         value_max_steem = value_steem_dollar
                                         date_value_max = date_day
                                         dictionary_montsh_value["max_value_MAR"] = value_max_steem
                                         dictionary_montsh_value["max_date_MAR"] = date_value_max


                         if value_steem_dollar < value_min_steem:
                                         value_min_steem = value_steem_dollar
                                         date_value_min = date_day
                                         dictionary_montsh_value["min_value_MAR"] = value_min_steem
                                         dictionary_montsh_value["min_date_MAR"] = date_value_min
                         
         

         
         elif date_day.month == 4:
                         
                         if value_steem_dollar > value_max_steem:
                                         value_max_steem = value_steem_dollar
                                         date_value_max = date_day
                                         dictionary_montsh_value["max_value_APR"] = value_max_steem
                                         dictionary_montsh_value["max_date_APR"] = date_value_max


                         if value_steem_dollar < value_min_steem:
                                         value_min_steem = value_steem_dollar
                                         date_value_min = date_day
                                         dictionary_montsh_value["min_value_APR"] = value_min_steem
                                         dictionary_montsh_value["min_date_APR"] = date_value_min
                         
         
         elif date_day.month == 5:
                        
                         if value_steem_dollar > value_max_steem:
                                         value_max_steem = value_steem_dollar
                                         date_value_max = date_day
                                         dictionary_montsh_value["max_value_MAY"] = value_max_steem
                                         dictionary_montsh_value["max_date_MAY"] = date_value_max


                         if value_steem_dollar < value_min_steem:
                                         value_min_steem = value_steem_dollar
                                         date_value_min = date_day
                                         dictionary_montsh_value["min_value_MAY"] = value_min_steem
                                         dictionary_montsh_value["min_date_MAY"] = date_value_min
                         


         
         elif date_day.month == 6:
                   
                         if value_steem_dollar > value_max_steem:
                                         value_max_steem = value_steem_dollar
                                         date_value_max = date_day
                                         dictionary_montsh_value["max_value_JUN"] = value_max_steem
                                         dictionary_montsh_value["max_date_JUN"] = date_value_max


                         if value_steem_dollar < value_min_steem:
                                         value_min_steem = value_steem_dollar
                                         date_value_min = date_day
                                         dictionary_montsh_value["min_value_JUN"] = value_min_steem
                                         dictionary_montsh_value["min_date_JUN"] = date_value_min
                         


         
         elif date_day.month == 7:
                         
                   
                         if value_steem_dollar > value_max_steem:
                                         value_max_steem = value_steem_dollar
                                         date_value_max = date_day
                                         dictionary_montsh_value["max_value_JUL"] = value_max_steem
                                         dictionary_montsh_value["max_date_JUL"] = date_value_max


                         if value_steem_dollar < value_min_steem:
                                         value_min_steem = value_steem_dollar
                                         date_value_min = date_day
                                         dictionary_montsh_value["min_value_JUL"] = value_min_steem
                                         dictionary_montsh_value["min_date_JUL"] = date_value_min
                         
         
         elif date_day.month == 8:
                         
                         
                         if value_steem_dollar > value_max_steem:
                                         value_max_steem = value_steem_dollar
                                         date_value_max = date_day
                                         dictionary_montsh_value["max_value_AUG"] = value_max_steem
                                         dictionary_montsh_value["max_date_AUG"] = date_value_max


                         if value_steem_dollar < value_min_steem:
                                         value_min_steem = value_steem_dollar
                                         date_value_min = date_day
                                         dictionary_montsh_value["min_value_AUG"] = value_min_steem
                                         dictionary_montsh_value["min_date_AUG"] = date_value_min
                         
                         

         
         elif date_day.month == 9:
                         
                         if value_steem_dollar > value_max_steem:
                                         value_max_steem = value_steem_dollar
                                         date_value_max = date_day
                                         dictionary_montsh_value["max_value_SEP"] = value_max_steem
                                         dictionary_montsh_value["max_date_SEP"] = date_value_max


                         if value_steem_dollar < value_min_steem:
                                         value_min_steem = value_steem_dollar
                                         date_value_min = date_day
                                         dictionary_montsh_value["min_value_SEP"] = value_min_steem
                                         dictionary_montsh_value["min_date_SEP"] = date_value_min
                         


         
         elif date_day.month == 10:
                         
                         
                         if value_steem_dollar > value_max_steem:
                                         value_max_steem = value_steem_dollar
                                         date_value_max = date_day
                                         dictionary_montsh_value["max_value_OCT"] = value_max_steem
                                         dictionary_montsh_value["max_date_OCT"] = date_value_max


                         if value_steem_dollar < value_min_steem:
                                         value_min_steem = value_steem_dollar
                                         date_value_min = date_day
                                         dictionary_montsh_value["min_value_OCT"] = value_min_steem
                                         dictionary_montsh_value["min_date_OCT"] = date_value_min
                         
         elif date_day.month == 11:
                         
                       
                         if value_steem_dollar > value_max_steem:
                                         value_max_steem = value_steem_dollar
                                         date_value_max = date_day
                                         dictionary_montsh_value["max_value_NOV"] = value_max_steem
                                         dictionary_montsh_value["max_date_NOV"] = date_value_max


                         if value_steem_dollar < value_min_steem:
                                         value_min_steem = value_steem_dollar
                                         date_value_min = date_day
                                         dictionary_montsh_value["min_value_NOV"] = value_min_steem
                                         dictionary_montsh_value["min_date_NOV"] = date_value_min
                         
         
         elif date_day.month == 12:
                         
                         
                         if value_steem_dollar > value_max_steem:
                                         value_max_steem = value_steem_dollar
                                         date_value_max = date_day
                                         dictionary_montsh_value["max_value_DEC"] = value_max_steem
                                         dictionary_montsh_value["max_date_DEC"] = date_value_max


                         if value_steem_dollar < value_min_steem:
                                         value_min_steem = value_steem_dollar
                                         date_value_min = date_day
                                         dictionary_montsh_value["min_value_DEC"] = value_min_steem
                                         dictionary_montsh_value["min_date_DEC"] = date_value_min
                                         
                                         
print "                           Month December"
print "   Value MAX    |     DATE       |    Value MIN     |     DATE          | "
print "  ",dictionary_montsh_value["max_value_DEC"],"    |  ", dictionary_montsh_value["max_date_DEC"],"  |    ", dictionary_montsh_value["min_value_DEC"],"    |  ", dictionary_montsh_value["min_date_DEC"],"     |  " 

print "                          "

print "                           Month November"
print "   Value MAX    |     DATE       |    Value MIN     |     DATE          | "
print "  ",dictionary_montsh_value["max_value_NOV"],"    |  ", dictionary_montsh_value["max_date_NOV"],"  |    ", dictionary_montsh_value["min_value_NOV"],"    |  ", dictionary_montsh_value["min_date_NOV"],"     |  " 

print "                          "

print "                           Month October"
print "   Value MAX    |     DATE       |    Value MIN     |     DATE          | "
print "  ",dictionary_montsh_value["max_value_OCT"],"    |  ", dictionary_montsh_value["max_date_OCT"],"  |    ", dictionary_montsh_value["min_value_OCT"],"    |  ", dictionary_montsh_value["min_date_OCT"],"     |  " 

print "                          "

print "                           Month September"
print "   Value MAX    |     DATE       |    Value MIN     |     DATE          | "
print "  ",dictionary_montsh_value["max_value_SEP"],"    |  ", dictionary_montsh_value["max_date_SEP"],"  |    ", dictionary_montsh_value["min_value_SEP"],"    |  ", dictionary_montsh_value["min_date_SEP"],"     |  " 

print "                          "

print "                           Month August"
print "   Value MAX    |     DATE       |    Value MIN     |     DATE          | "
print "  ",dictionary_montsh_value["max_value_AUG"],"    |  ", dictionary_montsh_value["max_date_AUG"],"  |    ", dictionary_montsh_value["min_value_AUG"],"    |  ", dictionary_montsh_value["min_date_AUG"],"     |  " 
print "                          "


print "                           Month July"
print "   Value MAX    |     DATE       |    Value MIN     |     DATE          | "
print "  ",dictionary_montsh_value["max_value_JUL"],"    |  ", dictionary_montsh_value["max_date_JUL"],"  |    ", dictionary_montsh_value["min_value_JUL"],"    |  ", dictionary_montsh_value["min_date_JUL"],"     |  " 
print "                          "


print "                           Month June"
print "   Value MAX    |     DATE       |    Value MIN     |     DATE          | "
print "  ",dictionary_montsh_value["max_value_JUN"],"    |  ", dictionary_montsh_value["max_date_JUN"],"  |    ", dictionary_montsh_value["min_value_JUN"],"    |  ", dictionary_montsh_value["min_date_JUN"],"     |  " 


print "                           Month MAY"
print "   Value MAX    |     DATE       |    Value MIN     |     DATE          | "
print "  ",dictionary_montsh_value["max_value_MAY"],"    |  ", dictionary_montsh_value["max_date_MAY"],"  |    ", dictionary_montsh_value["min_value_MAY"],"    |  ", dictionary_montsh_value["min_date_MAY"],"     |  " 
print "                          "


print "                           Month April"
print "   Value MAX    |     DATE       |    Value MIN     |     DATE          | "
print "  ",dictionary_montsh_value["max_value_APR"],"    |  ", dictionary_montsh_value["max_date_APR"],"  |    ", dictionary_montsh_value["min_value_APR"],"    |  ", dictionary_montsh_value["min_date_APR"],"     |  " 

