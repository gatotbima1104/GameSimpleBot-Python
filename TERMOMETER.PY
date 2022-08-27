'''print('\n\tPROGRAM KONVERSI SUHU\t\n')

celcius = float(input('masukkan suhu dalam celcius : '))
print('suhu dalam celsius adalah : ', celcius, 'celcius')

reamur = 4/5 * celcius
print('suhu dalam reamur adalah : ', reamur, 'reamur')

fahrenheit = 9/5 * celcius + 32
print('suhu dalam fahrenheit adalah : ', fahrenheit, 'fahrenheit')

kelvin = celcius + 273
print('suhu dalam kelvin adalah : ', kelvin, 'kelvin')'''
fr = float (input('masukkan suhu : '))
print('suhu dalam fr :', fr, 'frhnt')

kelvin = (5/9*(fr - 32))+273
print('suhu dalam kelvin :', kelvin, 'kelvin')
print('==================================')
kelvin = float (input('masukkan suhu dalam kelvin : ')) 
print ('suhu dalam kelvin : ', kelvin)

fr = (kelvin - 273) * 9/5 + 32
print('suhu dalam fr :', fr, 'frhnt')


