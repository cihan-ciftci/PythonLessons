"""
Trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki bilgilere göre hesaplayan
python uygulamasını yapınız.

1. Bakım => 1. yıl

2. Bakım => 2. yıl

3. Bakım => 3. yıl

** Süre hesabını alınan gün, ay, yıl bilgisine göre gün bazlı hesaplayınız..

*** datetime modülünü kullanmanız gerekiyor. (simdi) - (2018/8/1) => gün

"""

import datetime

firstDate = input('araciniz ilk trafige ne zaman cikti : (2012/4/7) ')
firstDate = firstDate.split('/')
trafficDate = datetime.datetime(int(firstDate[0]), int(firstDate[1]), int(firstDate[2]))

rNow = datetime.datetime.now()
diff = rNow - trafficDate
days = diff.days

if days <= 365:
    print('1.servis aralığı')
elif days > 365 and days <= 365 * 2:
    print('2.servis aralığı')
elif days > 365 * 2 and days <= 365 * 3:
    print('3.servis aralığı')
else:
    print('hatalı süre.')
"""

bu soruya tekrar donulecek datetime konusu henuz ogrenilmedi
soru hata veriyor elif lere ugramadan else gidiyor
"""