import tkinter as tk
import time
import datetime

def tarih_saat_guncelle():
    tarih_saat = time.strftime("%d/%m/%Y %H:%M:%S")
    saat_etiket.config(text=tarih_saat)
    uygulama_arayuzu.after(1000, tarih_saat_guncelle)

def set_background_color():
    now = datetime.datetime.now()
    if now.hour >= 6 and now.hour < 18:  # Sabah 6'dan akşam 6'ya kadar
        uygulama_arayuzu.configure(bg="white")
    else:
        uygulama_arayuzu.configure(bg="black")

def clear_page():
    for widget in uygulama_arayuzu.winfo_children():
        widget.destroy()

# def clear_page():
#     for widget in uygulama_arayuzu.winfo_children():
#         widget.destroy()

def show_original_content():
    clear_page()
    configure_page()
    # ismetinonukimdir.pack()
    # mustafakamalataturkkimdir.pack()


def show_content0():
    clear_page()
    back_button = tk.Button(uygulama_arayuzu, text="Geri Dön", command=show_original_content)
    back_button.pack()
    back_button.place(x=10,y=10)
    back_button.config(font=('Ink Free',10,'bold'))
    back_button.config(bg='#6F77FF')
    back_button.config(fg='#BEC1F8')
    back_button.config(activebackground='#2430FB')
    back_button.config(activeforeground='#4C55FB')

    content0= tk.Label(text="ATATÜRK")
    content0.config (font=('Montserrat',18,'bold'))
    content0.place(x=190,y=8)
    atatürk_hayati = """
    Mustafa Kemal Atatürk, 19 Mayıs 1881 tarihinde Selanik, Osmanlı İmparatorluğu'nda doğdu. 
    Çanakkale Savaşı'ndaki 
    kahramanlığıyla tanındı ve Kurtuluş Savaşı'nı 
    başlatarak Türkiye Cumhuriyeti'ni kurdu.
    1923 yılında Cumhuriyet'in ilan edilmesiyle 
    birlikte Türkiye'nin ilk Cumhurbaşkanı oldu.
    Atatürk, Türkiye'yi çağdaşlaştırmak için bir dizi reform 
    gerçekleştirdi ve eğitim, dil ve hukuk alanlarında önemli değişiklikler yaptı.
    10 Kasım 1938'de İstanbul'da vefat etti, 
    ancak mirası hala Türkiye'nin temel değerlerinden biridir.
    """
    content0= tk.Label(text=atatürk_hayati)
    content0.config (font=('Montserrat',8,'bold'))
    content0.place(x=8,y=44)


def show_content1():
    clear_page()
    back_button = tk.Button(uygulama_arayuzu, text="Geri Dön", command=show_original_content)
    back_button.pack()
    back_button.place(x=10,y=10)
    back_button.config(font=('Ink Free',10,'bold'))
    back_button.config(bg='#6F77FF')
    back_button.config(fg='#BEC1F8')
    back_button.config(activebackground='#2430FB')
    back_button.config(activeforeground='#4C55FB')

    

def show_content2():
    clear_page()
    back_button = tk.Button(uygulama_arayuzu, text="Geri Dön", command=show_original_content)
    back_button.pack()
    back_button.place(x=10,y=10)
    back_button.config(font=('Ink Free',10,'bold'))
    back_button.config(bg='#6F77FF')
    back_button.config(fg='#BEC1F8')
    back_button.config(activebackground='#2430FB')
    back_button.config(activeforeground='#4C55FB')



def show_content3():
    clear_page()
    back_button = tk.Button(uygulama_arayuzu, text="Geri Dön", command=show_original_content)
    back_button.pack()
    back_button.place(x=10,y=10)
    back_button.config(font=('Ink Free',10,'bold'))
    back_button.config(bg='#6F77FF')
    back_button.config(fg='#BEC1F8')
    back_button.config(activebackground='#2430FB')
    back_button.config(activeforeground='#4C55FB')


def show_content4():
    clear_page()
    back_button = tk.Button(uygulama_arayuzu, text="Geri Dön", command=show_original_content)
    back_button.pack()
    back_button.place(x=10,y=10)
    back_button.config(font=('Ink Free',10,'bold'))
    back_button.config(bg='#6F77FF')
    back_button.config(fg='#BEC1F8')
    back_button.config(activebackground='#2430FB')
    back_button.config(activeforeground='#4C55FB')


def show_content5():
    clear_page()
    back_button = tk.Button(uygulama_arayuzu, text="Geri Dön", command=show_original_content)
    back_button.pack()
    back_button.place(x=10,y=10)
    back_button.config(font=('Ink Free',10,'bold'))
    back_button.config(bg='#6F77FF')
    back_button.config(fg='#BEC1F8')
    back_button.config(activebackground='#2430FB')
    back_button.config(activeforeground='#4C55FB')


uygulama_arayuzu = tk.Tk()
uygulama_arayuzu.title("Program denemesi")
uygulama_arayuzu.geometry("500x700")


turkluk= tk.Label(text="TÜRKLÜKTE ÖNEMLİ İNSANLAR")
turkluk.config (font=('Montserrat',18,'bold'))
turkluk.place(x=50,y=8)

saat_etiket = tk.Label(text="", font=('Montserrat', 18, 'bold'))
saat_etiket.place(x=130, y=600)



def configure_page():

    turkluk= tk.Label(text="TÜRKLÜKTE ÖNEMLİ İNSANLAR")
    turkluk.config (font=('Montserrat',18,'bold'))
    turkluk.place(x=50,y=8)

    mustafakamalataturk = tk.Label (text="Mustafa Kemal Atatürk")
    mustafakamalataturk.config(font=('Montserrat',10,'bold'))
    mustafakamalataturk.place(x=15,y=50)

    mustafakamalataturkkimdir = tk.Button(uygulama_arayuzu, text="Mustafa Kemal Atatürk Kimdir?", command=show_content0)
    mustafakamalataturkkimdir.pack()
    mustafakamalataturkkimdir.place(x=180,y=50)

    mustafakamalataturkkimdir.config(font=('Ink Free',10,'bold'))
    mustafakamalataturkkimdir.config(bg='#ff6200')
    mustafakamalataturkkimdir.config(fg='#fffb1f')
    mustafakamalataturkkimdir.config(activebackground='#FF0000')
    mustafakamalataturkkimdir.config(activeforeground='#fffb1f')

    ismetinonu = tk.Label (text="İsmet İnönü")
    ismetinonu.place(x=15,y=90)
    ismetinonu.config(font=('Montserrat',10,'bold'))


    ismetinonukimdir = tk.Button(text="İsmet İnönü Kimdir?",command=show_content2)
    ismetinonukimdir.place(x=180,y=90)

    ismetinonukimdir.config(font=('Ink Free',10,'bold'))
    ismetinonukimdir.config(bg='#ff6200')
    ismetinonukimdir.config(fg='#fffb1f')
    ismetinonukimdir.config(activebackground='#FF0000')
    ismetinonukimdir.config(activeforeground='#fffb1f')

    nihalatsiz = tk.Label (text="Nıhal Atsız")
    nihalatsiz.place(x=15,y=130)
    nihalatsiz.config(font=('Montserrat',10,'bold'))

    nihalatsizkimdir = tk.Button(text="Nihal Atsız Kimdir?",command=show_content3)
    nihalatsizkimdir.place(x=180,y=130)
    nihalatsizkimdir.config(font=('Ink Free',10,'bold'))
    nihalatsizkimdir.config(bg='#ff6200')
    nihalatsizkimdir.config(fg='#fffb1f')
    nihalatsizkimdir.config(activebackground='#FF0000')
    nihalatsizkimdir.config(activeforeground='#fffb1f')

    ziyagokalp = tk.Label (text="Ziya Gökalp")
    ziyagokalp.place(x=15,y=170)
    ziyagokalp.config(font=('Montserrat',10,'bold'))

    ziyagokalpkimdir = tk.Button(text="Ziya Gökalp Kimdir?",command=show_content4)
    ziyagokalpkimdir.place(x=180,y=170)
    ziyagokalpkimdir.config(font=('Ink Free',10,'bold'))
    ziyagokalpkimdir.config(bg='#ff6200')
    ziyagokalpkimdir.config(fg='#fffb1f')
    ziyagokalpkimdir.config(activebackground='#FF0000')
    ziyagokalpkimdir.config(activeforeground='#fffb1f')

    ismailgasrapli = tk.Label (text="İsmail Gasraplı")
    ismailgasrapli.place(x=15,y=210)
    ismailgasrapli.config(font=('Montserrat',10,'bold'))

    ismailgasraplikimdir = tk.Button(text="İsmail Gasraplı Kimdir?",command=show_content5)
    ismailgasraplikimdir.place(x=180,y=210)
    ismailgasraplikimdir.config(font=('Ink Free',10,'bold'))
    ismailgasraplikimdir.config(bg='#ff6200')
    ismailgasraplikimdir.config(fg='#fffb1f')
    ismailgasraplikimdir.config(activebackground='#FF0000')
    ismailgasraplikimdir.config(activeforeground='#fffb1f')

    saat_etiket = tk.Label(text="", font=('Montserrat', 18, 'bold'))
    saat_etiket.place(x=130, y=600)
    
    
    tarih_saat_guncelle()
    
    set_background_color()






tarih_saat_guncelle()

set_background_color()

configure_page()



uygulama_arayuzu.mainloop()
