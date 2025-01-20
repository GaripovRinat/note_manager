from _collections_abc import async_generator

from time import struct_time, strftime
username = "Plan orders"
title = "Application execution plan"
content = "Sales of 5,200 rubles"
status1 = "Completed"
status2 = "Not comleted"
created_date = '15-01-2025'
issue_date = '18-01-2025'
print(username, title, sep=',')
print(created_date, issue_date, sep="/")
print(content, status1, sep=',')
created_date = input("Введите дату в формате 'DD/MM/YYYY':")



