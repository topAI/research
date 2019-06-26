
import numpy as np
import pandas as pd

import functools
import random
import pytest



codMobile = [ 67, 68, 96, 97, 98, 50, 66, 95, 99, 63,  91, 92,  93, 94]

listA = [
'3806777674225', 
'3809299128200', 
'3806755628027',
'3806635256605',
'3809783973478',
'3806675157665',
'3806617496612',
'3806395634293',
'3809233724047',
'3806621521617'
]

def func(onlyNumеral):

	if onlyNumеral.isdigit() == True:
		onlyNumеral = str(onlyNumеral)
		listB = []
		
		if len(onlyNumеral)<11 and len(onlyNumеral)>2:
			if len(onlyNumеral)==3:	
				if onlyNumеral == '380':
			
					for i in range(len(listA)):		
						listB.append(listA[i]) 
					if len(listB)>0:
						return(listB[:10])
				else:
					return('Перші три цифри номера в Україні мають бути "380" ')		
				
			elif len(onlyNumеral)==4:
				if onlyNumеral.startswith('380')==True:
					if onlyNumеral[3]==	'5' or onlyNumеral[3]=='6' or onlyNumеral[3]=='9':
						for e in range(len(listA)):						
							if listA[e].startswith(onlyNumеral)==True:
								listB.append(listA[e])  
						
						if len(listB)>0:
							return(listB[:10])
						else:
							return('співпадінь не знайдено')
					else:
						return('четверта цифра має бути 5, 6 або 9 ')		
				else:
					return('Перші три цифри номера в Україні мають бути "380" ')		
					
				
			elif len(onlyNumеral)==5:
				if int(onlyNumеral[3:5]) in codMobile:
				
					for e in range(len(listA)):						
						if listA[e].startswith(onlyNumеral)==True:
							listB.append(listA[e])  
					
					if len(listB)>0:
						return(listB[:10])
					else:
						return('співпадінь не знайдено')
				else:
					return('введіть правильний код оператора, після цифр 38 код оператора має бути:\nКиєвстар 067, 068, 096, 097, 098;\nВодафон 050, 066, 095, 099;\nЛайфселл 063, 093;\nUtel 091;\nPEOPLEnet 092;\nИнтертелеком 094;')			
				
					
			elif len(onlyNumеral)>5:
				if onlyNumеral.startswith('380')==True:
					if int(onlyNumеral[3:5]) in codMobile:
						for e in range(len(listA)):						
							if listA[e].startswith(onlyNumеral)==True:
								listB.append(listA[e])  
						
						
						if len(listB)>0:
							return(listB[:10])
						else:
							return('співпадінь не знайдено')
						
					else:
						return('введіть правильний код оператора, після цифр 38 код оператора має бути:\nКиєвстар 067, 068, 096, 097, 098;\nВодафон 050, 066, 095, 099;\nЛайфселл 063, 093;\nUtel 091;\nPEOPLEnet 092;\nИнтертелеком 094;')		
				else:	
					return('Перші три цифри мають бути 380 четверта цифра має бути 5, 6 або 9')		
			
			else:	
				return('Перші три цифри мають бути 380 четверта цифра має бути 5, 6 або 9')				
		else:	
			return('Введене число має містити мінімум 3 та максимум 10 цифр')		
	else:
		return('Ви ввели некооректний номер, він має складатися лише з цифр')

def test_answer1(): # користувач ввів символ, який не є числом
  	assert func('380b') == 'Ви ввели некооректний номер, він має складатися лише з цифр'

def test_answer2():	# користувач ввів три цифри, які не дорівнюють 380
  	assert func('580') == 'Перші три цифри номера в Україні мають бути "380" '
	
def test_answer3(): # користувач ввів неправильну четверту цифру
  	assert func('3802') == 'четверта цифра має бути 5, 6 або 9 '

def test_answer4():# користувач ввів неправильні перші 3 цифри
  	assert func('4802') == 'Перші три цифри номера в Україні мають бути "380" '
	
def test_answer5():# користувач ввів менше 3 цифр
  	assert func('1') == 'Введене число має містити мінімум 3 та максимум 10 цифр'
	
def test_answer6(): # користувач ввів 6 правільних цифри, але номерів, що починалися б з цих цифр в базі немає
  	assert func('380676') == 'співпадінь не знайдено'
	
def test_answer7(): # користувач ввів 5 правильних цифр, але номерів, що починалися б з цих цифр в базі немає
  	assert func('38095') == 'співпадінь не знайдено'	
	
def test_answer8():# користувач ввів більше 10 цифр
  	assert func('3806735353535') == 'Введене число має містити мінімум 3 та максимум 10 цифр'
	
def test_answer9():# користувач ввів 4 правильні, а п'яту неправильну цифру
  	assert func('38062') == 'введіть правильний код оператора, після цифр 38 код оператора має бути:\nКиєвстар 067, 068, 096, 097, 098;\nВодафон 050, 066, 095, 099;\nЛайфселл 063, 093;\nUtel 091;\nPEOPLEnet 092;\nИнтертелеком 094;'
	
def test_answer10():# користувач ввів 380 подається 10 перших номерів в базі
  	assert func('380') ==  [
'3806777674225', 
'3809299128200', 
'3806755628027',
'3806635256605',
'3809783973478',
'3806675157665',
'3806617496612',
'3806395634293',
'3809233724047',
'3806621521617'
]

def test_answer11():# користувач ввів 4 правильні цифри, і номери існують, подається 10 перших номерів в базі
  	assert func('3806') ==  [
'3806777674225', 
'3806755628027',
'3806635256605',
'3806675157665',
'3806617496612',
'3806395634293',
'3806621521617'
]
def test_answer12():# користувач ввів 4 правильні цифри, номерів в базі не існує
  	assert func('3805') == 'співпадінь не знайдено'


def test_answer13():# користувач ввів 5 правильних цифр і номери в базі  існують, подається 10 перших номерів в базі
  	assert func('38067') ==  [
'3806777674225', 
'3806755628027',
]

def test_answer14():# користувач ввів 7 правильних цифр і номери в базі  існують, подається 10 перших номерів в базі
  	assert func('3806635') ==  [
'3806635256605'
]