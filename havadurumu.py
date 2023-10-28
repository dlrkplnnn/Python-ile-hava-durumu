import tkinter as tk
import requests
from tkinter import messagebox

API_key='0e573da4d96419da16adb419691baf67'

def hava_durumu():

    city=giris.get()
    url= f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}&units=metric'
    
    cevap=requests.get(url)
    veri=cevap.json()
    print(veri)

    if veri['cod']=='404':

        messagebox.showerror(title="Hata", message="'Bilgi Alınamadı'")
        eror_message='Böyle Bir Şehir Bulunmamaktadır. \n Lütfen Geçerli Bir Şehir Adı Giriniz'
        ekranda_göster.config(text=eror_message)

    elif veri:

        havadurum=veri['weather'][0]['description']
        sicaklik = veri['main']['temp']
        hissedilen_sicaklik = veri['main']['feels_like']
        nem = veri['main']['humidity']
        rüzgar_hizi = veri['wind']['speed']
        bulutlar = veri['clouds']['all']

        sonuc=f"""
        Hava Durumu: {havadurum}
        Sıcaklık: {sicaklik}°C
        Hissedilen Sıcaklık: {hissedilen_sicaklik} °C
        Nem: {nem} %
        Rüzgar Hızı: {rüzgar_hizi} m/sn
        Bulut : {bulutlar} bulut
        """
            
        ekranda_göster.config(text=sonuc)


        print(f"""
        Hava Durumu: {havadurum}
        Sıcaklık: {sicaklik}°C
        Hissedilen Sıcaklık: {hissedilen_sicaklik} °C
        Nem: {nem} %
        Rüzgar Hızı: {rüzgar_hizi} m/s
        Bulut : {bulutlar} bulut
        """)


def press_enter(event): 
    hava_durumu()

pencere = tk.Tk()
pencere.title("Hava Durumu")
pencere.geometry('300x300')


etiket = tk.Label(text='Lütfen Şehir Girin: ',font='verdana 10 italic')
etiket.pack()

giris=tk.Entry()
giris.pack()
giris.bind('<Return>', press_enter)

giris_buton=tk.Button(text='Hava Durumunu Göster',command=hava_durumu)
giris_buton.pack()


çikis = tk.Button(text='Çıkış', command=pencere.destroy)
çikis.pack()

pencere.protocol('WM_DELETE_WINDOW', pencere.destroy)
pencere.protocol('')



ekranda_göster = tk.Label(pencere, text='-------')
ekranda_göster.pack()

pencere.mainloop()


