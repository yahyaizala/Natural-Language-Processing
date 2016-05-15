#-*- coding:utf-8 -*-
import urllib2, re,lxml.html
def cleanhtml(raw_html):
  cleanr =re.compile('<.*?>')
  cleantext = re.sub(cleanr,'', raw_html)
  return cleantext
def cleaner(r_html):
    page = lxml.html.document_fromstring(r_html)
    return page.cssselect('body')[0].text_content()
def getData():
    req = urllib2.urlopen("http://www.yahyakesenek.com")
    html = req.read()
    cleaned=cleanhtml(html)
    return  cleaned.decode("utf-8")
def to_turkish(strs):
    d={"ı":"i","İ":"I","Ç":"c","ç":"c","ğ":"g","Ğ":"G","Ü":"u","ü":"u","Ş":"S","ş":"s","Ö":"O","ö":"o"}
    pattern = re.compile(r'\b(' + '|'.join(d.keys()) + r')\b')
    result = pattern.sub(lambda x: d[x.group()], strs)
    return result.decode("utf-8")

def getDataManual():
    data='''Oluşturduğumuz apk dosyasını play store gibi mağazalarda
        yayınlamak için dijital olarak imzalamak gerekiyor.Bunun için
        programlar mevcut fakat komut satırında aynı işlemi yapabiliriz.
        **C:\Program Files\Java\jdk1.8.0\bin\ yolunu (sizde java versiyonu farklı olabilir) path e ekliyoruz.Burada singtool.exe jarsigner.exe ve zipalign.exe nin var olduğunu mutlaka görün.Komut satırını açarak apk dosyasının olduğu klasöre gidin.

        **keytool -genkey -v -keystore kycorp.keystore -alias TAKMAAD -keyalg RSA -keysize 2048 -validity 10000

        bu şekilde kycorp.keystore oluşturmak için seçenekleri doldurarak işlemi onaylayın.

        **jarsigner -verbose -sigalg SHA1withRSA -digestalg SHA1 -keystore kycorp.keystore Math6GAme-2.1-release-unsigned.apk TAKMAAD

        bu işlemler imzalamanın doğru olduğunu görmeniz gerekiyor.

        **zipalign -v 4 Math6GAme-2.1-release-unsigned.apk Math6GAme.apk

        bu işlemle de Math6GAme.apk dosyasını sunucuya yükleyebilirsiniz
    '''
    return data.decode("utf-8")
def getQues():
    data='''Merhaba arkadaşlar, Python için geçerli mobil framework bildiğim kadarıyla "Kivy" diye geçiyor.
    Web sitesinde incelediğimde, PLC alanındada kullanılması gerçekten çok ilginç, bu durum onun nekadar güçlü olduğunu kanıtlar niteliğinde olabilir düşüncesimdeyim. Sormak istediklerim :
    * Kivy dışında framework var mı?
    * Kivy ile yapılan mobil uygulamalar ile , prof. projelere girilebilir mi?
    * Kivy hakkında tecrübesi olan arkadaşların kişiyel tavsiyelerini bekliyorum.
    Ek olarak : Konuyu görüp kivy başlamak isteyen arkadaşlar için bir kaç link veryim
    ---------------------------------------------------------------------------------------
    Ana Site : https://kivy.org/
    Framework kullanım klavuzu : https://kivy.org/docs/api-kivy.html'''
    data=data.strip()
    return  to_turkish(data)
def stopwords():
    stops=['acaba', 'ama', 'aslında', 'az','bazı', 'belki','biri','birkaç','birşey', 'biz',
     'bu', 'çok', 'çünkü', 'da', 'daha', 'de', 'defa', 'diye', 'eğer', 'en', 'gibi', 'hem',
     'hep', 'hepsi', 'her','hiç', 'için', 'ile', 'ise', 'kez', 'ki', 'kim', 'mı', 'mu',
     'mü', 'nasıl', 'ne', 'neden', 'nerde', 'nerede', 'nereye', 'niçin', 'niye', 'o', 'sanki',
     'şey', 'siz', 'şu', 'tüm', 've', 'veya', 'ya', 'yani']
    #for i in range(len(stops)):
    #   stops[i]=to_turkish(stops[i])
    return stops
def getDataFile(fname="dosya.txt"):
    txt=""
    with open(fname,"r") as f:
        txt=f.read()
    return txt




def getManual():
    return '''No idea how I missed this in the docs: thanks for the info. I'm going to accept luc's answer tho because his uses the
    standard lib which I specified in the question (not important to me) and its probably of more general use to other people
    '''

