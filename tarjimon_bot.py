# import pyttsx3
# men=pyttsx3.init()
# men.say('Shohmalik the best')
# men.runAndWait()
from googletrans import Translator

try:
    print('Qaysi tilga tarjima qilinsin/uz,re,ko,en')
    apk=Translator()
    til=input()
    print('Matn kiriting:')
    matn=input()
    tarjima=apk.translate(matn,dest=til)
    print(tarjima.text)

except ValueError:
    print('Afsus bunday til yo`q')
except:
    print('Xatolik bor')
else:
    with open('matn.txt','a') as file:
        file.write(f'{matn}\n')
        file.close()
    with open('tarjima.txt','a') as file:
        file.write(f'{tarjima.text}\n')
        file.close()
