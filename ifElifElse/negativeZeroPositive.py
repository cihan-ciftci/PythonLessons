"""
Girilen bir sayının negatif sifir ve positive bir sayı olup olmadığını
kontrol eden python uygulamasını yapınız.
"""

numb = int(input('Enter a number: '))
if numb > 0:
    print('{0} is Positive'.format(numb))
elif numb == 0:
    print('{0} is Zero'.format(numb))
else:
    print('{0} is Negative'.format(numb))