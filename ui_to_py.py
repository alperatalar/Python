from PyQt5 import uic
#pyqt5 kütüphanesinden uic özelliğini import ediyoruz.
#QtDesignerde oluşturduğumuz formumuzu python koduna dönüştürecek.

with open ('AnaSayfaUI.py', 'w', encoding="utf-8") as fout:
    uic.compileUi('AnaSayfa.ui', fout)

#'w' ile 'AnaSayfaUI.py' isminde dosyayı açıyoruz, dosyayı açarken yukarda impor ettiğimiz uic özelliğinin,
  # -- compileUi özelliğinden yararlanıyoruz.
#AnaSayfa.ui formundaki tüm bilgileri AnaSayfaUI.py ismindeki dosyaya pyhton'ın anlayabileceği dile çeviriyor.
