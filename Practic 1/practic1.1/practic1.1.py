alfavit_EU =  'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
smeshenie = int(input('Шаг шифровки: '))
shifr = ''
deshifr=''

for i in alfavit_EU:
    mesto = alfavit_EU.find(i)
    new_mesto = mesto + smeshenie
    shifr += alfavit_EU[new_mesto]
print ("Зашифрованный текст:", shifr)

for i in shifr:
    mesto = shifr.find(i)
    new_mesto = mesto - smeshenie
    deshifr += shifr[new_mesto]
print ("Расшифрованный текст:", deshifr)