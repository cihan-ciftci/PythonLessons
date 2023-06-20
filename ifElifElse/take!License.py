""" - Kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet alabilme
    durumunu kontrol eden python uygulamasını yapınız.
** Ehliyet alma koşulu en az 18 ve eğitim durumu lise ya da üniversite olmalıdır. """

name = input('your name : ?')
age = int(input('your age : ?'))
education = input('education : ?')

if age >= 18:

    if education == 'lise' or education == 'universite':
        print(f' {name} ehliyet alabilir')
    else:
        print(f' {name} ehliyet alamazsin egitim durumun yetersiz')
else:
    print(f' {name} ehliyet alamazsin yasin tutmuyor')
