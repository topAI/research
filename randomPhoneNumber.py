#!/usr/bin/env python
# -*- coding: utf-8-*-

import numpy as np
import pandas as pd

import functools
import random

codMobile = [ 67, 68, 96, 97, 98, 50, 66, 95, 99, 63,  91, 92,  93, 94]

totalNumber = 300 #введіть занальну кільсть номерів
'''
listA =  ['3806777674225',
'3809299128200',
'3806755628027',
'3806635256605',
'3809783973478',
'3806675157665',
'3806617496612',
'3806395634293',
'3809233724047',
'3806621521617',
'3809299128330',
'3806755628027',
'3806635256605',
'3809783973478',
'3806675157665',
'3806617496612',
'3805095634293',
'3809233724047',
'3806621521617']

'''
listA =[]
while(len(listA) < totalNumber):
	a = functools.partial(random.randint, 0, 9)
	b = random.choice(codMobile)
	x = lambda: "380{}{}{}{}{}{}{}{}{}".format(b,  a(), a(), a(), a(), a(), a(), a(), a())

	if x not in listA:
		listA.append(x())

	
print('введи початок номеру:')		
onlyNumеral = input()



if onlyNumеral.isdigit() == True:
	onlyNumеral = str(onlyNumеral)
	listB = []
	
	if len(onlyNumеral)<11 and len(onlyNumеral)>2:
		if len(onlyNumеral)==3:	
			if onlyNumеral == '380':
		
				for i in range(len(listA)):		
					listB.append(listA[i]) 
				if len(listB)>0:
					print(listB[:10])
			else:
				print('Перші три цифри номера в Україні мають бути "380" ')		
			
		elif len(onlyNumеral)==4:
			if onlyNumеral.startswith('380')==True:
				if onlyNumеral[3]==	'5' or onlyNumеral[3]=='6' or onlyNumеral[3]=='9':
					for e in range(len(listA)):						
						if listA[e].startswith(onlyNumеral)==True:
							listB.append(listA[e])  
					
					if len(listB)>0:
						print(listB[:10])
			
				else:
					print('Перші три цифри мають бути 380, четверта цифра має бути 5, 6 або 9 ')		
			else:
				print('Перші три цифри номера в Україні мають бути "380" ')		
				
			
		elif len(onlyNumеral)==5:
			if int(onlyNumеral[3:5]) in codMobile:
			
				for e in range(len(listA)):						
					if listA[e].startswith(onlyNumеral)==True:
						listB.append(listA[e])  
				
				if len(listB)>0:
					print(listB[:10])
				else:
					print('співпадінь не знайдено')
			else:
				print('введіть правильний код оператора, після цифр 38 код оператора має бути:\nКиєвстар 067, 068, 096, 097, 098;\nВодафон 050, 066, 095, 099;\nЛайфселл 063, 093;\nUtel 091;\nPEOPLEnet 092;\nИнтертелеком 094;'
				)
			
				
		elif len(onlyNumеral)>5:
			if onlyNumеral.startswith('380')==True:
				if int(onlyNumеral[3:5]) in codMobile:
					for e in range(len(listA)):						
						if listA[e].startswith(onlyNumеral)==True:
							listB.append(listA[e])  
					
					
					if len(listB)>0:
						print(listB[:10])
					else:
						print('співпадінь не знайдено')
					
				else:
					print('введіть правильний код оператора, після цифр 38 код оператора має бути:\nКиєвстар 067, 068, 096, 097, 098;\nВодафон 050, 066, 095, 099;\nЛайфселл 063, 093;\nUtel 091;\nPEOPLEnet 092;\nИнтертелеком 094;')		
			else:	
				print('Перші три цифри мають бути 380 четверта цифра має бути 5, 6 або 9')		
		
		else:	
			print('Перші три цифри мають бути 380 четверта цифра має бути 5, 6 або 9')				
	else:	
		print('Введене число має містити мінімум 3 та максимум 10 цифр')		
else:
	print('Ви ввели некооректний номер, він має складатися лише з цифр')
