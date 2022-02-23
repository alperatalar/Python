# -------------------------------------- K Ü T Ü P H A N E -------------------------------------- #
# ------------------------------------------------------------------------------------------------#

import sys
from PyQt5 import QtWidgets
# -- Form üzerinde oluşturduğumuz tüm widgetsler aslında "QtWidgets" adlı clas üzerinden türetilen claslar o yüzden bunu import etmemiz gerekiyor.
from PyQt5.QtWidgets import *
# -- Elemanlara erişitken kolaylık olması için yapıldı.
# -- Örn : QtWidgets.QApplication yazmaktansa direk QApplication yazabiliyoruz.
from AnaSayfaUI import *
# -- AnaSayfaUI üzerindeki tüm class örneklerini içeri aktar.
# -- AnaSayfaUI (ui_to_py.py aracılığıyla QtDesignerde oluşturduğumuz formu python koduna dönüştürdüğümüz yerimiz.)
from datetime import datetime
import pandas as pd

# ------------------------------- U Y G U L A M A   O L U Ş T U R ------------------------------- #
# ------------------------------------------------------------------------------------------------#

Uygulama = QApplication(sys.argv)
penAna = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(penAna)
penAna.show()

# ----------------------------- V E R İ T A B A N I   O L U Ş T U R ---------------------------- #
# ---------------------------------------------------------------------------------------------- #

import sqlite3
global curs
global conn

conn=sqlite3.connect('veritabani.db')

curs=conn.cursor()

sorguCreTblHesap=("CREATE TABLE IF NOT EXISTS Hesap(                               \
                Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,                  \
                Tarih_Hesap TEXT NOT NULL,                                       \
                Yetiskin_Hesap INTEGER NOT NULL,                                        \
                Cocuk_Hesap INTEGER NOT NULL,                                     \
                Paket_Hesap TEXT NOT NULL,                                           \
                Pnr_Hesap TEXT NOT NULL,                                           \
                Komisyon_Hesap INTEGER NOT NULL,                                              \
                Cep_Hesap INTEGER NOT NULL,                                           \
                Aractipi_Hesap TEXT NOT NULL,                                            \
                Isimsoyisim_Hesap TEXT NOT NULL,                                               \
                Tcno_Hesap INTEGER NOT NULL,                                               \
                Aracplaka_Hesap TEXT NOT NULL,                                               \
                Kuponkodu_Hesap INTEGER NOT NULL)")

sorguCreTblGenel=("CREATE TABLE IF NOT EXISTS Genel(                               \
                Id INTEGER NOT NULL,                  \
                Tarih_Genel TEXT NOT NULL,                                       \
                Yetiskin_Genel INTEGER NOT NULL,                                        \
                Cocuk_Genel INTEGER NOT NULL,                                     \
                Paket_Genel TEXT NOT NULL,                                           \
                Pnr_Genel TEXT NOT NULL,                                           \
                Komisyon_Genel INTEGER NOT NULL,                                              \
                Cep_Genel INTEGER NOT NULL,                                           \
                Aractipi_Genel TEXT NOT NULL,                                            \
                Isimsoyisim_Genel TEXT NOT NULL,                                               \
                Tcno_Genel INTEGER NOT NULL,                                               \
                Aracplaka_Genel TEXT NOT NULL,                                               \
                Kuponkodu_Genel INTEGER NOT NULL)")

sorguCreTblPortal=("CREATE TABLE IF NOT EXISTS Portal(                               \
                Id INTEGER NOT NULL,                  \
                Yetiskin_Portal INTEGER NOT NULL,                                        \
                Cocuk_Portal INTEGER NOT NULL,                                     \
                Paket_Portal TEXT NOT NULL,                                               \
                Pnr_Portal TEXT NOT NULL,                                               \
                Kuponkodu_Portal TEXT NOT NULL)")

sorguCreTblPortalOdenenler=("CREATE TABLE IF NOT EXISTS PortalOdenenler(                               \
                Id INTEGER NOT NULL,                  \
                Yetiskin_Portal INTEGER NOT NULL,                                        \
                Cocuk_Portal INTEGER NOT NULL,                                     \
                Paket_Portal TEXT NOT NULL,                                               \
                Pnr_Portal TEXT NOT NULL,                                               \
                Kuponkodu_Portal TEXT NOT NULL)")

sorguCreTblCepGetir=("CREATE TABLE IF NOT EXISTS CepGetir(                               \
                Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,                  \
                Cep_CepGetir TEXT NOT NULL,                                        \
                AracTipi_CepGetir TEXT NOT NULL,                                     \
                IsimSoyisim_CepGetir TEXT NOT NULL,                                               \
                Tcno_CepGetir TEXT NOT NULL,                                                 \
                AracPlaka_CepGetir TEXT NOT NULL)")

sorguCreTblGenel_Ozet=("CREATE TABLE IF NOT EXISTS Genel_Ozet(                               \
                Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,                  \
                Tarih_Genel_Ozet TEXT NOT NULL,                                       \
                Yetiskin_Genel_Ozet INTEGER NOT NULL,                                        \
                Cocuk_Genel_Ozet INTEGER NOT NULL,                                     \
                Aractipi_Genel_Ozet TEXT NOT NULL,                                               \
                Komisyon_Genel_Ozet INTEGER NOT NULL,                                                 \
                Kuponkodu_Genel_Ozet TEXT NOT NULL)")


curs.execute(sorguCreTblGenel)
curs.execute(sorguCreTblHesap)
curs.execute(sorguCreTblPortal)
curs.execute(sorguCreTblPortalOdenenler)
curs.execute(sorguCreTblCepGetir)
curs.execute(sorguCreTblGenel_Ozet)

conn.commit()


# ------------------------------------------ TÜM FİLTRE TEMİZLEME İŞLEMLERİ ----------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #

def FILTRE_TEMIZLE_HESAP():

    ui.lneYetiskin.clear()
    ui.lneCocuk.clear()
    ui.lnePaket.clear()
    ui.lneKomisyon.clear()
    ui.lneCep.clear()
    ui.lneAractipi.clear()
    ui.lneIsimsoyisim.clear()
    ui.lneTcno.clear()
    ui.lneAracplaka.clear()
    ui.lneKuponkodu.clear()

def FILTRE_TEMIZLE_PORTAL():
    ui.lneYetiskinPortal.clear()
    ui.lneCocukPortal.clear()
    ui.lnePaketPortal.clear()
    ui.lneKuponPortal.clear()
    LISTELE_PORTAL()

# ---------------------------------------------- TÜM LİSTELEME İŞLEMLERİ --------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
def LISTELE_HESAP():
    ui.tblwHesap.clear()
    ui.tblwHesap.setHorizontalHeaderLabels(('Id','Tarih','Yetişkin','Çocuk','Paket','Pnr','Komisyon','Cep','Araç Tipi','İsim - Soyisim','Tc No','Araç Plakası','Kupon Kodu'))
    # ui.tblwHesap.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    curs.execute("SELECT * FROM Hesap")
    for satirIndeks, satirVeri in enumerate(curs):
        for sutunIndeks, sutunVeri in enumerate(satirVeri):
            ui.tblwHesap.setItem(satirIndeks, sutunIndeks, QTableWidgetItem(str(sutunVeri)))


    curs.execute("SELECT SUM(Yetiskin_Hesap) FROM Hesap")
    kayitSayisi = curs.fetchone()
    ui.lblYetiskintoplam_Hesap.setText(str(kayitSayisi[0]))

    curs.execute("SELECT SUM(Cocuk_Hesap) FROM Hesap")
    kayitSayisi1 = curs.fetchone()
    ui.lblCocuktoplam_Hesap.setText(str(kayitSayisi1[0]))

    curs.execute("SELECT SUM(Komisyon_Hesap) FROM Hesap")
    kayitSayisi2 = curs.fetchone()
    ui.lblKomisyontoplam_Hesap.setText(str(kayitSayisi2[0]))

def LISTELE_GENEL():
    ui.tblwGenel.clear()
    ui.tblwGenel.setHorizontalHeaderLabels(('Id','Tarih','Yetişkin','Çocuk','Paket','Pnr','Komisyon','Cep','Araç Tipi','İsim - Soyisim','Tc No','Araç Plakası','Kupon Kodu'))
    ui.tblwGenel.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    curs.execute("SELECT * FROM Genel")
    for satirIndeks, satirVeri in enumerate(curs):
        for sutunIndeks, sutunVeri in enumerate(satirVeri):
            ui.tblwGenel.setItem(satirIndeks, sutunIndeks, QTableWidgetItem(str(sutunVeri)))

    curs.execute("SELECT SUM(Komisyon_Genel) FROM Genel")
    kayitSayisi = curs.fetchone()
    ui.lblKomisyontoplam_Genel.setText(str(kayitSayisi[0]))

def LISTELE_GENEL_OZET():
    ui.tblwGenel_Ozet.clear()
    ui.tblwGenel_Ozet.setHorizontalHeaderLabels(('Id','Tarih','Yetişkin','Çocuk','Araç Tipi','Komisyon','Kupon Kodu'))
    ui.tblwGenel_Ozet.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    curs.execute("SELECT * FROM Genel_Ozet")
    for satirIndeks, satirVeri in enumerate(curs):
        for sutunIndeks, sutunVeri in enumerate(satirVeri):
            ui.tblwGenel_Ozet.setItem(satirIndeks, sutunIndeks, QTableWidgetItem(str(sutunVeri)))

    curs.execute("SELECT SUM(Komisyon_Genel_Ozet) FROM Genel_Ozet")
    kayitSayisi = curs.fetchone()
    ui.lblKomisyontoplam_GenelOzet.setText(str(kayitSayisi[0]))

def LISTELE_PORTAL_ODENENLER():
    ui.tblwPortal_2.clear()
    ui.tblwPortal_2.setHorizontalHeaderLabels(('Id','Yetişkin','Çocuk','Paket','PNR','Kupon'))
    ui.tblwPortal_2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    curs.execute("SELECT * FROM PortalOdenenler")
    for satirIndeks, satirVeri in enumerate(curs):
        for sutunIndeks, sutunVeri in enumerate(satirVeri):
            ui.tblwPortal_2.setItem(satirIndeks, sutunIndeks, QTableWidgetItem(str(sutunVeri)))




def LISTELE_PORTAL():
    ui.tblwPortal.clear()
    ui.tblwPortal.setHorizontalHeaderLabels(('Id','Yetişkin','Çocuk','Paket','PNR','Kupon'))
    ui.tblwPortal.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    curs.execute("SELECT * FROM Portal EXCEPT SELECT * FROM PortalOdenenler ORDER BY Kuponkodu_Portal DESC")
    # Listeleme işlemini büyükten küçüğe doğru yapıyor, bu sayede en üstte en alta doğru ***,**,* şeklinde gidiyor. En son işlemimiz, yıldızsız olduğu için onu işliyoruz
      # - bu sayede PortalÖdenecek/Ödenen ekranınında kullandığımız sql sorgusu düzgün çalışıyor. (Sorgu BITIR def inde)
    for satirIndeks, satirVeri in enumerate(curs):
        for sutunIndeks, sutunVeri in enumerate(satirVeri):
            ui.tblwPortal.setItem(satirIndeks, sutunIndeks, QTableWidgetItem(str(sutunVeri)))
    LISTELE_PORTAL_ODENENLER()






# ----------------------------------------- E K L E  ---------------------------------------- #
# ---------------------------------------------------------------------------------------------- #

def EKLE():
    try:
        _lneTarih = datetime.now()
        _lneYetiskin = ui.lneYetiskin.text()
        _lneCocuk = ui.lneCocuk.text()
        _lnePaket = ui.lnePaket.text()
        _lnePnr = ui.lnePnr.text()
        _lneAractipi = ui.lneAractipi.text()
        _lneKomisyon = ui.lneKomisyon.text()

        if _lneKomisyon =="":
            if _lneAractipi == "VT":
                if _lnePaket == "VIP":
                    _lneKomisyon = (int(_lneYetiskin) * 175) + (int(_lneCocuk) * 170)
                elif _lnePaket == "DIAMOND":
                    _lneKomisyon = (int(_lneYetiskin) * 125) + (int(_lneCocuk) * 120)
                elif _lnePaket == "ELITE":
                    _lneKomisyon = (int(_lneYetiskin) * 80) + (int(_lneCocuk) * 75)
                elif _lnePaket == "NORMAL":
                    _lneKomisyon = (int(_lneYetiskin) * 60) + (int(_lneCocuk) * 55)
                else:
                    _lneKomisyon = (int(_lneYetiskin) * 0) + (int(_lneCocuk) * 0)
            else:
                _lneKomisyon = (int(_lneYetiskin) * 60) + (int(_lneCocuk) * 55)
        else:
            _lneKomisyon = ui.lneKomisyon.text()

        _lneCep = ui.lneCep.text()
        #_lneAractipi = ui.lneAractipi.text()
        _lneIsimsoyisim = ui.lneIsimsoyisim.text()
        _lneTcno = ui.lneTcno.text()
        _lneAracplaka = ui.lneAracplaka.text()

        _lneKuponkodu = ui.lneKuponkodu.text()

        curs.execute("INSERT INTO hesap (Tarih_Hesap,Yetiskin_Hesap,Cocuk_Hesap,Paket_Hesap,Pnr_Hesap,Komisyon_Hesap,Cep_Hesap,Aractipi_Hesap,Isimsoyisim_Hesap,Tcno_Hesap,Aracplaka_Hesap,Kuponkodu_Hesap)   \
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?)", (_lneTarih,_lneYetiskin,_lneCocuk,_lnePaket,_lnePnr,_lneKomisyon,_lneCep,_lneAractipi,_lneIsimsoyisim,_lneTcno,_lneAracplaka,_lneKuponkodu))

        conn.commit()

        ui.lneYetiskin.clear()
        ui.lneCocuk.clear()
        ui.lnePaket.clear()
        ui.lneKomisyon.clear()
        ui.lnePnr.clear()

        LISTELE_HESAP()

    except Exception as Hata:
        ui.statusbar.showMessage("Şöyle bir hata ile karşılaşıldı.:" + str(Hata))

# ------------------------------------------- TÜM TABLO SIRA SEÇME İŞLEMLERİ ----------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #

def PORTAL_TABLO_SIRA():
    try:
        secili = ui.tblwPortal.selectedItems()

        ui.lneYetiskin.setText(secili[1].text())
        ui.lneCocuk.setText(secili[2].text())
        ui.lnePaket.setText(secili[3].text())
        ui.lnePnr.setText(secili[4].text())
        ui.lneKuponkodu.setText(secili[5].text())

        # yil = int(secili[7].text()[0:4])
        # ay = int(secili[7].text()[5:7])
        # gun = int(secili[7].text()[8:10])
        # ui.cwDTarihi.setSelectedDate(QtCore.QDate(yil, ay, gun))


    except Exception as Hata:
        ui.statusbar.showMessage("Şöyle bir hata ile karşılaşıldı.:" + str(Hata))






# --------------------------------------------TÜM ARAMA İŞLEMLERİ ------------------------------------------- #
# ---------------------------------------------------------------------------------------------- #
def PORTAL_ARA():
    try:
        if ui.lneKuponPortal.text() == "":
            print("Kupon text BOŞ!")
            LISTELE_PORTAL()
        else:
            aranan1 = "%"+ui.lneKuponPortal.text()+"%"
            # aranan2 = ui.lnePaketPortal.text()

            # curs.execute("SELECT * FROM Portal WHERE like Kuponkodu_Portal=? OR Paket_Portal=?", (aranan1,aranan2))
            # curs.execute("SELECT * FROM Portal WHERE Kuponkodu_Portal='%s'" % aranan1)
            curs.execute("SELECT * FROM Portal WHERE Kuponkodu_Portal LIKE '%s' ORDER BY Kuponkodu_Portal DESC" % aranan1)
            # Kursör de 2 sorgu var, 1.si : aranan1'deki değeri içinde geçip geçmediğini arıyor. 2.si : bulduğu sonuçları büyükten küçüğe sıralıyor.

            conn.commit()
            ui.tblwPortal.clear()
            for satirIndeks, satirVeri in enumerate(curs):
                for sutunIndeks, sutunVeri in enumerate(satirVeri):
                    ui.tblwPortal.setItem(satirIndeks, sutunIndeks, QTableWidgetItem(str(sutunVeri)))
    except Exception as Hata:
        ui.statusbar.showMessage("Şöyle bir hata ile karşılaşıldı.:" + str(Hata))

def HESAP_CEP_ARA():
    try:
        aranan1 = ui.lneCep.text()
        aranan2 = ui.lneCep.text()


        curs.execute("SELECT * FROM CepGetir WHERE (Cep_CepGetir=? OR Cep_CepGetir=?)", (aranan1,aranan2))
        conn.commit()
        data = curs.fetchall()
        print(data)

        if data == [] :
            print("kayıt bulunamadı")
            ui.lneAractipi.setText("")
            ui.lneIsimsoyisim.setText("")
            ui.lneTcno.setText("")
            ui.lneAracplaka.setText("")
        else:
            xlneAractipi=(data[0][2])
            xlneIsimsoyisim=(data[0][3])
            xlneTcno=((data[0][4]))
            xlneAracplaka=(data[0][5])


            ui.lneAractipi.setText(xlneAractipi)
            ui.lneIsimsoyisim.setText(xlneIsimsoyisim)
            ui.lneTcno.setText(xlneTcno)
            ui.lneAracplaka.setText(xlneAracplaka)



    except Exception as Hata:
        ui.statusbar.showMessage("Şöyle bir hata ile karşılaşıldı.:" + str(Hata))

def GENEL_ARA():
    try:
        aranan1 = ui.lneTarihGenel.text()
        aranan2 = ui.lneYetiskinGenel.text()
        aranan3 = ui.lneCocukGenel.text()
        aranan4 = ui.lnePaketGenel.text()
        aranan5 = ui.lneKomisyonGenel.text()
        aranan6 = ui.lneCepGenel.text()
        aranan7 = ui.lneAractipiGenel.text()
        aranan8 = ui.lneIsimsoyisimGenel.text()
        aranan9 = ui.lneTcnoGenel.text()
        aranan10 = ui.lneAracplakaGenel.text()
        aranan11 = ui.lneKuponkoduGenel.text()
        aranan12 = ui.lnePnrGenel.text()

        curs.execute("SELECT * FROM Genel WHERE Tarih_Genel=? OR Yetiskin_Genel=? OR Cocuk_Genel=? OR Paket_Genel=? OR Komisyon_Genel=? OR Cep_Genel=? OR Aractipi_Genel=? OR Isimsoyisim_Genel=? OR Tcno_Genel=? OR Aracplaka_Genel=? OR Kuponkodu_Genel=? OR Pnr_Genel=?", (aranan1,aranan2,aranan3,aranan4,aranan5,aranan6,aranan7,aranan8,aranan9,aranan10,aranan11,aranan12))
        conn.commit()
        ui.tblwGenel.clear()
        for satirIndeks, satirVeri in enumerate(curs):
            for sutunIndeks, sutunVeri in enumerate(satirVeri):
                ui.tblwGenel.setItem(satirIndeks, sutunIndeks, QTableWidgetItem(str(sutunVeri)))
    except Exception as Hata:
        ui.statusbar.showMessage("Şöyle bir hata ile karşılaşıldı.:" + str(Hata))


def GENEL_ARA_PNR():
    try:
        if ui.lnePnrGenel.text() == "":
            print("Pnr text BOŞ!")
            LISTELE_GENEL()
        else:
            aranan1 = ui.lnePnrGenel.text()
            aranan2 = ui.lnePnrGenel.text()

            curs.execute("SELECT * FROM Genel WHERE Pnr_Genel=? OR Pnr_Genel=?", (aranan1,aranan2))
            conn.commit()
            ui.tblwGenel.clear()
            for satirIndeks, satirVeri in enumerate(curs):
                for sutunIndeks, sutunVeri in enumerate(satirVeri):
                    ui.tblwGenel.setItem(satirIndeks, sutunIndeks, QTableWidgetItem(str(sutunVeri)))
    except Exception as Hata:
        ui.statusbar.showMessage("Şöyle bir hata ile karşılaşıldı.:" + str(Hata))

# --------------------------------------------- S İ L ------------------------------------------ #
# ---------------------------------------------------------------------------------------------- #
def SIL():
    cevap = QMessageBox.question(penAna,"KAYIT SİL","Kaydı silmek istediğinize emin misiniz ?",QMessageBox.Yes | QMessageBox.No)
    if cevap == QMessageBox.Yes:
        secili = ui.tblwHesap.selectedItems()
        silinecek = secili[0].text()
        try:
            curs.execute("DELETE FROM Hesap WHERE Id='%s'" %(silinecek))
            conn.commit()

            LISTELE_HESAP()

            ui.statusbar.showMessage("Kayıt silme işlemi başarıyla gerçekleşti.",10000)
        except Exception as Hata:
            ui.statusbar.showMessage("Şöyle bir hata ile karşılaşıldı.:"+str(Hata))
    else:
        ui.statusbar.showMessage("Silme işlemi iptal edildi.", 10000)

# --------------------------------------------- B İ T İ R ------------------------------------------ #
# ---------------------------------------------------------------------------------------------- #
def BITIR():
    cevap = QMessageBox.question(penAna,"KAYIT BİTİR","Kaydı bitirmek istediğinize emin misiniz ?",QMessageBox.Yes | QMessageBox.No)
    if cevap == QMessageBox.Yes:
        try:
            #conn = sqlite3.connect('veritabani.db')
            #curs = conn.cursor()


            curs.execute("INSERT INTO Genel SELECT * FROM Hesap")
            # Hesap tablosundaki tüm verileri Genel tablosuna aktarıyor.

            secili = ui.tblwPortal.selectedItems()
            ArananKuponKodu = "%"+secili[5].text()+"%"
            curs.execute("INSERT INTO PortalOdenenler SELECT * FROM Portal WHERE Kuponkodu_Portal LIKE '%s'" % ArananKuponKodu)


            curs.execute("DELETE FROM Hesap")


            _lneTarih = datetime.now()
            _lneYetiskin = ui.lneYetiskin.text()
            _lneCocuk = ui.lneCocuk.text()
            _lnePaket = ui.lnePaket.text()
            _lnePnr = ui.lnePnr.text()
            _lneKomisyon = ui.lneKomisyon.text()
            _lneCep = ui.lneCep.text()
            _lneAractipi = ui.lneAractipi.text()
            _lneIsimsoyisim = ui.lneIsimsoyisim.text()
            _lneTcno = ui.lneTcno.text()
            _lneAracplaka = ui.lneAracplaka.text()
            _lneKuponkodu = ui.lneKuponkodu.text()

            _lblYetiskintoplam_Hesap = ui.lblYetiskintoplam_Hesap.text()
            _lblCocuktoplam_Hesap = ui.lblCocuktoplam_Hesap.text()
            _lblKomisyontoplam_Hesap = ui.lblKomisyontoplam_Hesap.text()

            curs.execute("INSERT INTO Genel_Ozet (Tarih_Genel_Ozet,Yetiskin_Genel_Ozet,Cocuk_Genel_Ozet,Aractipi_Genel_Ozet,Komisyon_Genel_Ozet,Kuponkodu_Genel_Ozet)   \
                                            VALUES (?,?,?,?,?,?)", (
            _lneTarih, _lblYetiskintoplam_Hesap, _lblCocuktoplam_Hesap, _lneAractipi, _lblKomisyontoplam_Hesap,
            _lneKuponkodu))

            conn.commit()

            aranan1 = ui.lneCep.text()
            aranan2 = ui.lneCep.text()


            curs.execute("SELECT * FROM CepGetir WHERE (Cep_CepGetir=? OR Cep_CepGetir=?)", (aranan1, aranan2))

            conn.commit()

            data = curs.fetchall()

            if data == []:
                print("kayıt bulunamadı2")

                curs.execute("INSERT INTO CepGetir (Cep_CepGetir,AracTipi_CepGetir,IsimSoyisim_CepGetir,Tcno_CepGetir,AracPlaka_CepGetir)   \
                VALUES (?,?,?,?,?)", (_lneCep, _lneAractipi, _lneIsimsoyisim, _lneTcno, _lneAracplaka))

                conn.commit()

            else:
                print("Kayıt var")


            LISTELE_HESAP()
            LISTELE_GENEL()
            LISTELE_GENEL_OZET()
            LISTELE_PORTAL()
            LISTELE_PORTAL_ODENENLER()

            FILTRE_TEMIZLE_HESAP()
            FILTRE_TEMIZLE_PORTAL()

            ui.statusbar.showMessage("Kayıt silme işlemi başarıyla gerçekleşti.",10000)
        except Exception as Hata:
            ui.statusbar.showMessage("Şöyle bir hata ile karşılaşıldı(BITIR).:"+str(Hata))
    else:
        ui.statusbar.showMessage("Silme işlemi iptal edildi.", 10000)

# --------------------------------------------- Y E N İ L E  /  G Ü N C E L L E  ------------------------------------------ #
# ---------------------------------------------------------------------------------------------- #




# --------------------------------------------- D O L D U R - H E S A P ------------------------------------------ #
# ---------------------------------------------------------------------------------------------- #

def DOLDUR_HESAP():
    try:
        secili = ui.tblwHesap.selectedItems()

        ui.lneYetiskin.setText(secili[2].text())
        ui.lneCocuk.setText(secili[3].text())
        ui.lnePaket.setText(secili[4].text())
        ui.lneKomisyon.setText(secili[5].text())
        ui.lneCep.setText(secili[6].text())
        ui.lneAractipi.setText(secili[7].text())
        ui.lneIsimsoyisim.setText(secili[8].text())
        ui.lneTcno.setText(secili[9].text())
        ui.lneAracplaka.setText(secili[10].text())
        ui.lneKuponkodu.setText(secili[11].text())


        #yil = int(secili[7].text()[0:4])
        #ay = int(secili[7].text()[5:7])
        #gun = int(secili[7].text()[8:10])
        #ui.cwDTarihi.setSelectedDate(QtCore.QDate(yil, ay, gun))


    except Exception as Hata:
        ui.statusbar.showMessage("Şöyle bir hata ile karşılaşıldı.:" + str(Hata))

# --------------------------------------------- D O L D U R - G E N E L ------------------------------------------ #
# ---------------------------------------------------------------------------------------------- #

def DOLDUR_GENEL():
    try:
        secili = ui.tblwGenel.selectedItems()

        ui.lneYetiskin.setText(secili[2].text())
        ui.lneCocuk.setText(secili[3].text())
        ui.lnePaket.setText(secili[4].text())
        ui.lneKomisyon.setText(secili[5].text())
        ui.lneCep.setText(secili[6].text())
        ui.lneAractipi.setText(secili[7].text())
        ui.lneIsimsoyisim.setText(secili[8].text())
        ui.lneTcno.setText(secili[9].text())
        ui.lneAracplaka.setText(secili[10].text())
        ui.lneKuponkodu.setText(secili[11].text())


        #yil = int(secili[7].text()[0:4])
        #ay = int(secili[7].text()[5:7])
        #gun = int(secili[7].text()[8:10])
        #ui.cwDTarihi.setSelectedDate(QtCore.QDate(yil, ay, gun))


    except Exception as Hata:
        ui.statusbar.showMessage("Şöyle bir hata ile karşılaşıldı.:" + str(Hata))

def exportToExcel():
    try:

        columnHeaders = []
        print("1")

        # create column header list
        for j in range(ui.tblwGenel.columnCount()):
            print("2")
            #secili = ui.tblwPortal.selectedItems()
            columnHeaders.append(ui.tblwGenel.horizontalHeaderItem(j).text())
            print("3")

        df = pd.DataFrame(columns=columnHeaders)
        print("4")
        print(df)

        # create dataframe object recordset
        for row in range(ui.tblwGenel.rowCount()):
            print("5")
            print(ui.tblwGenel.rowCount())
            for col in range(ui.tblwGenel.columnCount()):
                print("6")
                print(ui.tblwGenel.columnCount())
                df.at[row, col] = str(ui.tblwGenel.item(row, 3).text())
                #print(ui.tblwGenel.items(row, col))
                print("7")

        df.to_excel('XYZ.xlsx', index=False)
        print('Excel file exported')

    except Exception as Hata:
        ui.statusbar.showMessage("Şöyle bir hata ile karşılaşıldı.:" + str(Hata))

def DATA_SIFIRLA():
    cevap = QMessageBox.question(penAna, "DATA KAYIT SİL", "Data Kaydı silmek istediğinize emin misiniz ?",
                                 QMessageBox.Yes | QMessageBox.No)
    if cevap == QMessageBox.Yes:

        try:
            curs.execute("DROP TABLE Genel")
            curs.execute("DROP TABLE Genel_Ozet")
            curs.execute("DROP TABLE Hesap")
            curs.execute("DROP TABLE PortalOdenenler")

            curs.execute(sorguCreTblGenel)
            curs.execute(sorguCreTblHesap)
            curs.execute(sorguCreTblPortalOdenenler)
            curs.execute(sorguCreTblGenel_Ozet)

            conn.commit()

        except Exception as Hata:
            ui.statusbar.showMessage("Şöyle bir hata ile karşılaşıldı.:" + str(Hata))
    else:
        ui.statusbar.showMessage("Data Silme işlemi iptal edildi.", 10000)


# ------------------------------------ S İ N Y A L   S L O T ----------------------------------- #
# ---------------------------------------------------------------------------------------------- #

#----------------- H E S A P --------------------#
ui.btn_HesapEkle.clicked.connect(EKLE)
ui.btn_HesapSil.clicked.connect(SIL)
ui.btn_HesapBitir.clicked.connect(BITIR)
ui.btn_HesapFiltreTemizle.clicked.connect(FILTRE_TEMIZLE_HESAP)
ui.tblwHesap.itemSelectionChanged.connect(DOLDUR_HESAP)

ui.lneCep.editingFinished.connect(HESAP_CEP_ARA)

#----------------- G E N E L --------------------#
ui.tblwGenel.itemSelectionChanged.connect(DOLDUR_GENEL)
ui.btn_GenelAra.clicked.connect(GENEL_ARA)
ui.btn_GenelAra_3.clicked.connect(exportToExcel)
ui.lnePnrGenel.editingFinished.connect(GENEL_ARA_PNR)
ui.btn_GenelYenile.clicked.connect(LISTELE_GENEL)
ui.btn_GenelYenile_2.clicked.connect(LISTELE_GENEL_OZET)
ui.btn_GenelDataSifirla.clicked.connect(DATA_SIFIRLA)

#----------------- P O R T A L --------------------#
ui.tblwPortal.itemSelectionChanged.connect(PORTAL_TABLO_SIRA)
#ui.btn_PortalAraa.clicked.connect(PORTAL_ARA)
ui.lneKuponPortal.editingFinished.connect(PORTAL_ARA)

ui.btn_PortalFiltreTemizle.clicked.connect(FILTRE_TEMIZLE_PORTAL)
ui.btn_PortalKayitGetir.clicked.connect(LISTELE_PORTAL)


sys.exit(Uygulama.exec_())