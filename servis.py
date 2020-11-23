import time

departmanlar = ["Muhasebe","Halkla İlişkiler","İnsan Kaynakları","Teknik"]
#####Classları Oluşturma#####
class Araba():
    def __init__(self,marka = "-",model = "-",renk = "-",ağırlık = "-",plaka = "-",silindir = "-",beygirGücü = "-",lastik = "-",bulunanBayi="-"):
        self.marka = marka
        self.model = model
        self.renk = renk
        self.ağırlık = ağırlık
        self.plaka = plaka
        self.silindir = silindir
        self.beygirGücü = beygirGücü
        self.lastik = lastik
        self.bulunanBayi = bulunanBayi
    
    def bilgileriGöster(self):
        print("""
        Araba Bilgileri
        ===============
        Marka = {}
        Model = {}
        Renk = {}
        Ağırlık = {}
        Plaka = {}
        Silindir = {}
        Beygir Gücü = {}  
        Lastik Markası = {}  
        Bulunan Bayi = {}    
        """.format(self.marka,self.model,self.renk,self.ağırlık,self.plaka,self.silindir,self.beygirGücü,self.lastik,self.bulunanBayi))
    
    def hasarGöster(self,hasar):
        print("""
        Araba Hasarı = {}
        """.format(hasar))

    def boyama(self,boya):
        print("Boyama İşlemi Yapılıyor...")
        self.renk = boya
    
    def lastikDeğişimi(self,marka):
        print("Lastikler Değişiyor...")
        self.lastik = marka

class Çalışan():
    def __init__(self, isim = "-", soyisim = "-", yaş = "-", departman = "-", idNo = "-", maaş = "-"):
        self.isim = isim
        self.soyisim = soyisim
        self.yaş = yaş
        self.departman = departman
        self.idNo = idNo
        self.maaş = maaş
    
    def bilgileriGöster(self):
        print("""
        Çalışan Bilgileri
        =================
        İsim = {}
        Soyisim = {}
        Yaş = {}
        Departman = {}
        ID = {}
        Maaş = {}       
        """.format(self.isim,self.soyisim,self.yaş,self.departman,self.idNo,self.maaş))

    def zamYap(self, miktar):
        print("Maaşa {} TL Zam Yapılıyor...".format(miktar))
        self.maaş += miktar

    def maaşDüşürme(self, miktar):
        print("Maaş {} TL Düşürülüyor...".format(miktar))
        self.maaş -= miktar
    
    def idDeğiştir(self, yeniId):
        print("ID DEĞİŞTİRİLİYOR...")
        self.idNo = yeniId

    def departmanDeğiştir(self, x):
        print("Departman Değiştiriliyor...")
        self.departman = departmanlar[x-1]
    
    def maaşKontrol(self):
        print("Geçerli maaş: {}".format(self.maaş))
    
    def idGöster(self):
        print("Geçerli ID: {}".format(self.idNo))

class Müşteri():
    def __init__(self,isim = "-",soyisim = "-",sebep = "-"):
        self.isim = isim
        self.soyisim = soyisim
        self.sebep = sebep
    
    def bilgileriGöster(self):
        print("""
        Müşteri Bilgileri
        =================
        İsim = {}
        Soyisim = {}
        Gelme Sebebi = {}
        """.format(self.isim,self.soyisim,self.sebep))

class Bayi():
    def __init__(self, il="-", ilçe="-", postaKodu="-", bayiNo="-"):
        self.il = il
        self.ilçe = ilçe
        self.postaKodu = postaKodu
        self.bayiNo = bayiNo
    
    def bilgileriGöster(self):
        print("""
        Bayi Bilgileri
        ==============
        İl = {}
        İlçe = {}
        Posta Kodu = {}
        Bayi No = {}
        """.format(self.il,self.ilçe,self.postaKodu,self.bayiNo))

print("""
  ___  _       ____                  _
 / _ \| |_ ___/ ___|  ___ _ ____   _(_)___
| | | | __/ _ \___ \ / _ | '__\ \ / | / __|
| |_| | || (_) ___) |  __| |   \ V /| \__ |
 \___/ \__\___|____/ \___|_|    \_/ |_|___/


İşlem numaraları:
[1] Müşteri
[2] Çalışan
[3] Araba
""")
#!!!Kullanıcının oluşturması lazım!!!
müşteri = Müşteri("Tunç","Akay","Yağ Sızıntısı")
çalışan = Çalışan("Demirkan","Doğru",17,departmanlar[3],15786,3000)
araba = Araba("VOLVO","XC60","Siyah",3100,"35 DDD 35", 16,270,"BridgeStone")

while True:
    islem = input("İşlem giriniz(Çıkmak için q'ya basınız): ").lower()
    if islem == "q":
        print("!!Çıkış Yapılıyor!!")
        time.sleep(2)
    elif islem =="1":
        müşteri.bilgileriGöster()
    elif islem == "2":
        print("""
        Çalışan İşlemleri:
        [1] Bilgileri Göster
        [2] Zam Yap
        [3] Maaş Düşür
        [4] ID Değiştir
        [5] Departman Değiştir 
        [6] Geçerli Maaş Gösterme       
        """)
        while True:
            print("**************************")
            calisanIslem = input("İşlem no giriniz(Çıkmak için q'ya basın): ").lower()

            if calisanIslem == "q":
                break

            elif calisanIslem == "1":
                çalışan.bilgileriGöster()

            elif calisanIslem == "2":
                zam = float(input("Zam miktarı giriniz: "))
                çalışan.zamYap(zam)
                print("Yapılan zam = {}".format(zam))
                çalışan.maaşKontrol()

            elif calisanIslem == "3":
                düşürme = float(input("Düşürülecek miktar: "))
                çalışan.maaşDüşürme(düşürme)
                print("Azalan miktar = {}".format(düşürme))
                çalışan.maaşKontrol()

            elif calisanIslem == "4":
                yeni_id = input("Yeni ID giriniz: ")
                çalışan.idDeğiştir(yeni_id)
                çalışan.idGöster()
            
            elif calisanIslem == "5":
                print("1: Muhasebe/2: Halkla İlişkiler/3: İnsan Kaynakları/4: Teknik")
                depa = int(input("Departman no giriniz: "))
                çalışan.departmanDeğiştir(depa)
            
            elif calisanIslem == "6":
                çalışan.maaşKontrol()
    
    elif islem == "3":
        print("""
        Araba İşlemleri: 
        [1] Bilgileri Göster
        [2] Hasar 
        [3] Boyama
        [4] Lastik Değişim
        """)

        while True:
            print("**************************")
            arabaIslem = input("İşlem no giriniz(Çıkmak için q'ya basın): ").lower()

            if arabaIslem == "q":
                break
            
            elif arabaIslem == "1":
                araba.bilgileriGöster()
            
            elif arabaIslem == "2":
                araba.hasarGöster()
            
            elif arabaIslem == "3":
                renk = input("Arabanın yeni rengini giriniz: ")
                araba.boyama(renk)
            
            elif arabaIslem == "4":
                marka = input("Lastik markasını giriniz: ")
                araba.lastikDeğişimi(marka)
            
        