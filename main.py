import tkinter as tk
from tkinter import messagebox
import random
#Tkinter kütüphanesini içe aktarıyoruz. Tkinter, GUI uygulamaları
# oluşturmak için kullanılan popüler bir Python kütüphanesidir.
# messagebox modülünü de içe aktarıyoruz. random kütüphanesini rastgele
# işlemler yapmak için kullanacağız.
def create_grid():
    square_size = 50
    padding = 5
    for i in range(10):
        for j in range(10):
            x1 = j * square_size + padding
            y1 = i * square_size + padding
            x2 = x1 + square_size
            y2 = y1 + square_size
            kare = canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="black")
            kareler.append(kare)
#create_grid fonksiyonu, 10x10 boyutunda bir kare ızgarası oluşturur. Her kare,
# canvas üzerinde dikdörtgen bir şekilde çizilir ve kareler listesine eklenir.
def select_kare(event):
    global selected_number

    if selected_number > 0:
        x = event.x
        y = event.y
        for kare in kareler:
            x1, y1, x2, y2 = canvas.coords(kare)
            if x1 <= x <= x2 and y1 <= y <= y2:
                if canvas.itemcget(kare, "fill") == "white":
                    canvas.itemconfig(kare, fill=selected_color)
                    selected_number -= 1
                    kalan_sayi_label.config(text="Kalan Sayı: " + str(selected_number))
                    break
    if selected_number == 0:
        all_same_color = True
        first_color = canvas.itemcget(kareler[0], "fill")
        for kare in kareler:
            if canvas.itemcget(kare, "fill") != first_color:
                all_same_color = False
                break
        if all_same_color:
            play_button.config(state="normal")
            reset_button.config(state="normal")
            canvas.unbind("<Button-1>")
            messagebox.showinfo("Bildirim", "Tüm kareler aynı renge boyandı. Oyun tamamlandı!")
        else:
            messagebox.showinfo("Bildirim", "Kareleri boyama hakkınızı kullandınız!")
#select_kare fonksiyonu, kullanıcının bir kareyi seçmesini ve boyamasını sağlar. Seçilen kare,
# seçilen renkle doldurulur ve selected_number değişkeni bir azaltılır. Eğer selected_number 0 ise,
# tüm karelerin aynı renkte olup olmadığı kontrol edilir. Eğer aynı renkte ise "Oyna" ve "Yeniden
# Başlat" düğmeleri etkinleştirilir, fare tıklamaları dinlemesi kapatılır ve bir bildirim mesajı
# gösterilir. Eğer farklı renklerde kareler varsa, bir bildirim mesaj gösterilir ve kullanıcının
# kareleri boyama hakkını kullandığı bilgilendirilir.
def reset_game():
    global selected_number, selected_color
    selected_number = 0
    selected_color = ""
    kalan_sayi_label.config(text="Kalan Sayı: 0")
    play_button.config(state="disabled")
    reset_button.config(state="disabled")  # Yeniden başlat düğmesini devre dışı bırak
    for kare in kareler:
        canvas.itemconfig(kare, fill="white")
#reset_game fonksiyonu, oyunu sıfırlamak için kullanılır. Seçilen sayıyı ve renki sıfırlar,
# kalan sayıyı ve düğmelerin durumunu günceller, ve tüm kareleri beyaz renge döndürür.
def play_game():
    global selected_number, selected_color
    selected_number = int(number_entry.get())
    selected_color = color_var.get()
    selected_kareler = random.sample(kareler, selected_number)  # Rastgele seçilen kareleri al
    result = random.choice(["kazandın", "kaybettin"])
    if result == "kazandın":
        messagebox.showinfo("Sonuç", "Kazandın!")
    else:
        messagebox.showinfo("Sonuç", "Kaybettin!")
        count = 0
        for kare in kareler:
            if canvas.itemcget(kare, "fill") == selected_color:
                canvas.itemconfig(kare, fill="white")
                count += 1
                if count == selected_number:
                    break
#play_game fonksiyonu, oyunu başlatmak için kullanılır. Kullanıcının girdiği sayıyı ve seçtiği
# rengi alır. Ardından, seçilen sayı kadar kare rastgele seçilir. Sonuç rastgele bir şekilde
# belirlenir (kazandın ya da kaybettin). Eğer kaybettiyse, seçilen renkteki kareler girdiğimiz
# sayı kadar silinir.
window = tk.Tk()
window.title("Renkli Kare Oyunu")
canvas = tk.Canvas(window, width=510, height=510)
canvas.pack()
kareler = []
create_grid()
selected_number = 0
selected_color = ""
#Bu bölümde, tkinter penceresi oluşturulur ve başlık "Renkli Kare Oyunu" olarak ayarlanır.
# Ardından, 510x510 boyutunda bir tuval (canvas) oluşturulur ve ekrana yerleştirilir. kareler
# isimli bir boş liste tanımlanır.
color_var = tk.StringVar()
color_var.set("red")
color_label = tk.Label(window, text="Renk Seçin:")
color_label.pack()
color_radio_frame = tk.Frame(window)
color_radio_frame.pack()
color_radios = [
    ("Kırmızı", "red"),
    ("Sarı", "yellow"),
    ("Mavi", "blue"),
    ("Siyah", "black")
]
for text, color in color_radios:
    color_radio = tk.Radiobutton(color_radio_frame, text=text, variable=color_var, value=color).pack(side="left")
#Bu kısımda, renk seçimini sağlayacak radyo düğmeleri oluşturulur. color_var isimli bir StringVar nesnesi oluşturulur
# ve başlangıçta "red" değeri atanır. Renk seçimini gösteren bir etiket (label) oluşturulur ve
# ekrana yerleştirilir. Daha sonra, radyo düğmelerini tutacak bir çerçeve (frame) oluşturulur ve
# ekrana yerleştirilir. color_radios isimli bir liste tanımlanır, her bir radyo düğmesinin metnini
# ve değerini içerir. Her bir radyo düğmesi için bir döngü oluşturulur ve çerçeveye eklenir.
number_label = tk.Label(window, text="Sayı Girin:")
number_label.pack()
number_entry = tk.Entry(window)
number_entry.pack()
#Bu bölümde, kullanıcının sayı girebileceği bir etiket (label) ve giriş kutusu (entry) oluşturulur.
# Etiket ve giriş kutusu ekrana yerleştirilir.
play_button = tk.Button(window, text="Oyna", command=play_game)
play_button.pack()
reset_button = tk.Button(window, text="Yeniden Başlat", command=reset_game, state="disabled")
reset_button.pack()
kalan_sayi_label = tk.Label(window, text="Kalan Sayı: 0")
kalan_sayi_label.pack()
#Bu kısımda, "Oyna" ve "Yeniden Başlat" adında iki düğme (button) oluşturulur. Oyna düğmesi play_game
# fonksiyonunu çağıracak şekilde ayarlanır, Yeniden Başlat düğmesi ise reset_game fonksiyonunu
# çağıracak şekilde ayarlanır. Yeniden Başlat düğmesi başlangıçta devre dışı (disabled) olarak
# ayarlanır. Ayrıca, "Kalan Sayı: 0" yazısını göstermek için bir etiket (label) oluşturulur ve
# ekrana yerleştirilir.
canvas.bind("<Button-1>", select_kare)
window.mainloop()
#Bu kısımda, tuvale (canvas) sol fare tıklamasını (<Button-1>) dinleyen bir bağlama (binding)
# yapılır. Fare tıklandığında select_kare fonksiyonu çağrılacaktır.
#Son olarak, window.mainloop() çağrısı, tkinter penceresinin ana döngüsünün başlatılmasını
# sağlar ve kullanıcı arayüzünün etkileşimli hale gelmesini sağlar.



