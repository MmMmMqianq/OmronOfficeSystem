import calendar
from selenium import webdriver

ca = calendar.Calendar()
print(ca.itermonthdays(2022, 2))
l = list()
for i in ca.itermonthdays2(2022, 1):
	if i[0]>20:
		print(i)
		l.append(i[0])
print(l)
