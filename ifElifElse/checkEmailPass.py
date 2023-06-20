# Email ve parola bilgileri ile giris kontrolu yapınız.

email = 'ci.ciftci.com'
password = '45'

yMail = input('enter your mail :')
yPass = input('enter your password :')

if (yMail == email) and (yPass == password):
    print('giris basarili')
elif yMail != email:
    print('email hesabiniz hatali')
elif yPass != password:
    print('passwordunuz hatali')
