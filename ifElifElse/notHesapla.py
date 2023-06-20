"""
- Bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre not aralığına
karşılık gelen not bilgisini yazdıran python uygulamasını yapınız.

0 -24 => 0

25-44 => 1

45-54 => 2

55-69 => 3

70-84 => 4

85-100 => 5
"""

firstExam = float(input('vize notunuzu giriniz : '))
secondExam = float(input('final notunuzu giriniz : '))
oralExam = float(input('sozlu notunuzu giriniz : '))

average = (firstExam + secondExam + oralExam) / 3

if (average >= 0) and (average < 24):
    print(f'your average is : {average} average : 0')
elif (average >= 25) and (average < 44):
    print(f'your average is : {average} average : 1')
elif (average >= 45) and (average < 54):
    print(f'your average is : {average} average : 2')
elif (average >= 55) and (average < 69):
    print(f'your average is : {average} average : 3')
elif (average >= 70) and (average < 84):
    print(f'your average is : {average} average : 4')
elif (average >= 85) and (average < 100):
    print(f'your average is : {average} average : 5')

else:
    print('something is wrong please try again!!!')
