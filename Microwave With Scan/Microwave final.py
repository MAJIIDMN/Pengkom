#PROGRAM SMART MICROWAVE
#...

#KAMUS
#class
    #comp: Berisi komponen penting untuk berjalannya Mikrowave (suhu, waktu, kelembapan)
    #mode: berisi pintasan mode otomatis untuk menjalankan microwave
    #vegetable: Berisi mode memasakn otomatis untuk sayuran
    #incode: Berisi mode memasakn otomatis untuk Seafood
    #Microwave: Berisi logika utama berjalannya program, mulai dari tampilan sampai pemrosesan input dan output

#Fungsi
    ##Comp
        #moisture1: berfungsi untuk menentukan kelembapan akhir setelah melewati proses memasak, dengan batas kelembapan yang sudah diatur(disesuaikan)
    ##mode
        #quick_heat: mode untuk memasak cepat biasa untuk memanansakn makanan
        #Deforst: mode untuk mencairkan makanan beku
        #Grill: mode untuk melakukan proses pemanggangan dengan suhu tinggi
    ##Vegetable
        #menu: Berisi daftar sayuran yang dapat dimasak otomatis
        #wortel : mode memasak otomatis untuk wortel
        #kembang_kol: mode memasak otomatis untuk kembang kol
        #bayam : mode memasak otomatis untuk bayam
        #jagung_manis : mode memasak otomatis untuk jagung manis
        #paprika : mode memasak otomatis untuk paprika
        #zuicchini : mode memasak otomatis untuk zuicchini
    ##seafood
        #menu: Berisi daftar Seafood yang dapat dimasak otomatis
        #fish: mode memasak otomatis untuk ikan fillet(tuna dan sebagainya)
        #shirmp: mode memasak otomatis untuk udang
        #squid: mode memasak otomatis untuk cumi-cumi
        #shellfish: mode memasak otomatis untuk kerang
        #lobster: mode memasak otomatis untuk lobster
        ##incode
        #detectscan: berfungsi untuk medeteksi(mengenali) barcode yang discan
        #scancode: berfungsi untuk menjalankan fungsi kamera untuk melakukan scanning
        #detect: berfungsi untuk mencocokan barcode hasil scan dengan database, dan mengimport data yang diperlukan
        #cook: mode memasak otomatis untuk makanan yang berhasil discan
    ##Microwave
        #displayup: berfungsi sebagai batas atas pada display layar microwave
        #displaydown: berfungsi sebagai batas bawah pada display layar microwave
        #display1: berfungsi untuk memberikan tampilan awal saat microwave dijalakan atau direstart(start display)
        #display2: berfungsi untuk memberikan tampilan saat microwave sedang melakuakn proses memasak, menampilkan suhu terkini, sisa waktu, dan temperatur terkini.
        #displayClean: berfungsi untuk meberikan tampilan saat microwave menjalankan fungsi Cleaning
        #displayCleanDone: berfungsi untuk meberikan tampilan saat microwave selesai menjalankan fungsi Cleaning
        #displayover: berfungsi untuk memberikan tampilan saat makanan yang dimasak overcook (kelembapan kurang dari 40%)
        #displaydry: berfungsi untuk memberikan tampilan saat makanan yang dimasak sudah kering (kelembapan 0%)
        #displaydone: berfungsi untuk memberikan tampilan saat makanan yang dimasak sudah matang sempurna
        #menu: menampilkan pilihan menu dari fitur microwave yang dapat dijalankan
        #menulock: menampilkan pilihan menu dari fitur microwave ketika dalam mode Child Lock
        #Start: berisi logika utama dalam menjalankan semua fitur mikrowave serta memproses input dan output user

#variable
    #barcodes(list): menyimpan data hasil decode barcode yang ditangkap pada tiap frame 
    #barcode(int): menyimpan nilai barcode makanan yang sesuai
    #barcode_data(sting): menyimpan data barcode(nomornya) dari hasil decode
    #barcode(int): menyimpan barcode yang berhasil di deteksi
    #barcode_number(int): berisi value dari variabel barcode_data
    #cap(Videocapture): menjalankan fungsi scan(kamera)
    #ChildLock(boolean): parameter mode Child lock(true jika sedang dalam mode child lock)
    #Choice(int): menyimpan pilihan fitur yang akan digunakan user
    #code(Tuple): menyimpan data barcode makanan yang berhasil di scan
    #codefood(list): menyimpan semua data barcode makanan yang ada dalam database
    #confirm(string): menyimpan inputan user terkait konfirmasi nama makanan yang akan dimasak melalui fitur scan barcode
    #csvfile(file csv(list)): berisi file csv yang menyimpan data makanan 
    #foodcode(string): menyimpan nama makanan yang sesuai barcode
    #foodcode(list): menyimpan data yang berasal dari database csvfile
    #frame(MatLike(Matriks)): menyimpan data tiap frame pada video
    #limit(int): nilai batas kelembapan saat menjalankan fungsi masak otomatis
    #min(int): menyimpan nilai menit waktu memasak(hasil pembagian time dengan 60)
    #moisture(int): menyimpan pengaturan kelembapan microwave
    #moisturefood(list): menyimpan semua data batas kelembapan makanan yang ada dalam database
    #namefood(list): menyimpan semua data nama makanan yang ada dalam database
    #pinlock(int): menyimpan PIN yang digunakan pada mode Child Lock
    #ret(boolean): perameter untuk mendeteksi apakah fungsi kamera telah dijalankan(kamera nyala)
    #sec(int): menyimpan nilai detik waktu memasak(sisa pembagian time dengan 60)
    #side_h(int): menyimpan nilai batas horizontal dislpay
    #side_v(int): menyimpan nilai batas vertikal dislpay
    #sayur(int): menyimpan pilihan mode memasak sayuran yang akan digunakan user
    #temp(int): menyimpan pengaturan suhu microwave
    #tempfood(list): menyimpan semua data tempratur untuk memesak makanan yang ada dalam database
    #time(int): menyimpan pengaturan waktu microwave
    #timefood(list): menyimpan semua data waktu memasak makanan yang ada dalam database
    #vegen(int): menyimpan pilihan mode memasak seafood yang akan digunakan user



import time
import os
import csv
import cv2
from pyzbar.pyzbar import decode

class comp:
    #fungsi untuk mendefinisikan Varibel utama yang akan digunakan
    def __init__(self, time:int, temp:int, moisture:int):
        self.time = time*60
        self.temp = temp
        self.moisture = moisture
    #fungsi untuk menentukan kelembapan akhir makanan setelah dimasak
    def moisture1(self, limit):
        if self.moisture >= limit:
            time = self.time
            while time > 0:
                self.moisture = self.moisture - (self.temp/1200)
                if self.moisture <= limit:
                    break
                time -= 1     

class mode(comp):
    def __init__(self, time, temp, moisture):
        super().__init__(time, temp, moisture)
    def quick_heat(self):
        #menjalankan proses memasak otomatis dengan batas kelembapan makanan yang sudah ditentukan
        comp.moisture1(self, 40)
        #menampilkan display mikrowave yang sedang berjalan
        Microwave.display2(self)
    def Deforst(self):
        comp.moisture1(self, 60)
        Microwave.display2(self)   
    def Grill(self):
        comp.moisture1(self, 30)
        Microwave.display2(self)
         
class vegetable(comp):
    def __init__(self, time, temp, moisture):
        super().__init__(time, temp, moisture)

    def menu():
        Microwave.display1()
        print(f'======================================')
        print(f'||1. brokoli      ||5. jagung manis ||')
        print(f'||==================================||')
        print(f'||2. wortel       ||6. paprika      ||')
        print(f'||==================================||')
        print(f'||3. kembang kol  ||7. zucchini     ||')
        print(f'||==================================||')
        print(f'||4. bayam        ||0. Kembali      ||')
        print(f'======================================')

    def brokoli(self):
        comp.moisture1(self, 70)
        Microwave.display2(self)
         
    def wortel(self):
        comp.moisture1(self, 60)
        Microwave.display2(self)
         
    def kembang_kol(self):
        comp.moisture1(self, 70)
        Microwave.display2(self)
         
    def bayam(self):
        comp.moisture1(self, 80)
        Microwave.display2(self)
         
    def jagung_manis(self):
        comp.moisture1(self, 70)
        Microwave.display2(self)
         
    def paprika(self):
        comp.moisture1(self, 60)
        Microwave.display2(self)
         
    def zucchini(self):
        comp.moisture1(self, 70)
        Microwave.display2(self)
         
class seafood(comp):
    def __init__(self, time, temp, moisture):
        super().__init__(time, temp, moisture)

    def menu():
        Microwave.display1()
        print(f'======================================')
        print(f'||1. Ikan Fillet  ||4. Kerang       ||')
        print(f'||==================================||')
        print(f'||2. Udang        ||5. Lobster      ||')
        print(f'||==================================||')
        print(f'||3. Cumi-cumi    ||0. Kembali      ||')
        print(f'======================================')

    def fish(self):
        comp.moisture1(self, 70)
        Microwave.display2(self)
         
    def shrimp(self):
        comp.moisture1(self, 75)
        Microwave.display2(self)
         
    def squid(self):
        comp.moisture1(self, 70)
        Microwave.display2(self)
         
    def shellfish(self):
        comp.moisture1(self, 70)
        Microwave.display2(self)
         
    def lobster(self):
        comp.moisture1(self, 70)
        Microwave.display2(self)
         
class incode(comp):
    def __init__(self, time:int, temp:int, moisture:int, barcode:int, foodname):
        super().__init__(time, temp, moisture)
        self.barcode = barcode
        self.foodname = foodname

    def detectscan(image):
        #barcode menyimpan hasil decode dari parameter (gambar barcode) yang berhasil dideteksi
        barcodes = decode(image)
        #perulangan untuk mengambil nilai barcode(codenya saja)
        for code in barcodes:
            barcode_data = code.data.decode("utf-8")
            #mengembalikan nilai output fungsi berupa Variabel barcode_data
            return barcode_data
    
    def scancode(self):
        #menyalkan kamera
        cap = cv2.VideoCapture(0)
        #perulangan untuk menampilkan hasil capture dan mengambil tiap frame pada videocapture 
        while True:
            #menyimpan indikator(nyala atau tidaknya kamera) serta frame yang ditangkap
            ret, frame = cap.read()
            #merubah hasil frame jadi berwarna abu" agar lebih mudah dideteksi (hitam putih)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            #melihat apakah kamera nyala atau tidak
            if not ret:
                print("Failed to capture image")
                #jika kamera mati maka selesaikan pengambilan video
                break
            barcode_number = incode.detectscan(frame)
            #kondisi ketika barcode sudah terdeteksi maka perulangan(pengambilan video) berhenti
            if barcode_number:
                self.barcode = int(barcode_number)
                break 
            #menampilkan hasil Capture(pengambilan video)
            cv2.imshow("Barcode Scanner", frame)
            #menekan tombol 'n' pada keyboard akan menghentikan proses scanning
            if cv2.waitKey(1) & 0xFF == ord('n'):
                break
        cap.release()
        cv2.destroyAllWindows()   
    
    def detect(self, code):
        #membuka dan menyimpan nilai file database(csv)
        csvfile = open('PYTHON\\pengkom\\barcodes.csv', newline='')
        foodcode = csv.reader(csvfile)
        #skip baris pertama pada file csv(header)
        next(foodcode)
        codefood = []
        namefood = []
        timefood = []
        tempfood = []
        moisturefood = []
        #perulangan untuk mengambil dan memisakan antara value yang dibutuhkan pada database
        for row in foodcode:
            codefood.append(int(row[1]))
            namefood.append(row[2])
            timefood.append(int(row[3])*60)
            tempfood.append(int(row[4]))
            moisturefood.append(int(row[5]))
        #menutuk kembali file database(csv)
        csvfile.close()
        #mencocokan barcode yang sesuai dengan hasil scan atau input dengan data pada database 
        for i in range(len(codefood)):
            #jika data sudah ditemukan maka perulangan akan dihentikan
            if code == codefood[i]:
                self.foodname = namefood[i]
                self.barcode = codefood[i]
                self.time = timefood[i]
                self.temp = tempfood[i]
                self.moisture = moisturefood[i]
                break               
    def cook(self):
        comp.moisture1(self, 0)
        Microwave.display2(self)
         
class Microwave(comp):
    def __init__(self, time, temp, moisture):
        super().__init__(time, temp, moisture)
    def displayup():
        print('='*38)
        print('||',end='')
        print('='*18,end='')
        print('||',end='')
        print('='*14,end='')
        print('||')
    def displaydown():
        print('||',end='')
        print('='*18,end='')
        print('||',end='')
        print('='*14,end='')
        print('||')
        print('='*38)
    def display1():
        Microwave.displayup()
        side_v = 6
        #perulangan untuk membuat display awal microwave tiap baris
        while side_v>0:
            side_h = 38
            while side_h>0:
                if (side_h == 38) or (side_h == 37) or (side_h == 18) or (side_h == 17) or (side_h == 2):
                    print('|', end='')
                elif (side_h == 1):
                    print('|')
                elif side_h<37 and side_h>18:
                    print(' ',end='')
                elif side_h == 16:
                    if side_v == 6:
                        print(f'Temp || --- ||',end='')
                    elif side_v == 5:
                        print(f'Time ||--:--||',end='')
                    elif side_v == 4:
                        print(f'Mois || --- ||',end='')
                    elif side_v == 3:
                        print(" _ _ _ _ _ ___",end='')
                    elif side_v == 2:
                        print("|1|3|4|5|6|   ",end='')
                    else:
                        print("|7|8|0| 99|___",end='')
                side_h-=1
            side_v-=1
        Microwave.displaydown()
    def display2(self):
        #perulangan untuk menyesuaikan sisa waktu mikrowave bekerja
        while self.time >= 0:
            os.system('cls')
            Microwave.displayup()
            side_v = 6
            while side_v>0:
                side_h = 38
                while side_h>0:
                    if (side_h == 38) or (side_h == 37) or (side_h == 18) or (side_h == 17) or (side_h == 2):
                        print('|', end='')
                    elif (side_h == 1):
                        print('|')
                    elif side_h<37 and side_h>18:
                        print(' ',end='')
                    elif side_h == 16:
                        #penyesuain perubahan suhu, waktu, dan kelembapan makanan saat microwave sedang bekerja
                        if side_v == 6:
                            if self.temp < 10:
                                print(f'Temp || {self.temp}°C ||',end='')
                            elif self.temp < 100:
                                print(f'Temp || {self.temp}°C||',end='')
                            else:
                                print(f'Temp ||{self.temp}°C||',end='')
                        elif side_v == 5:
                            min, sec = divmod(self.time, 60)
                            print(f'Time ||{min:02d}:{sec:02d}||',end='')
                        elif side_v == 4:
                            moisture = self.moisture + (self.temp/1500)*self.time
                            if moisture <10:
                                print(f'Mois ||   {int(round(moisture, 0))}%||',end='')
                            elif moisture<=99:
                                print(f'Mois ||  {int(round(moisture, 0))}%||',end='')
                            else:
                                moisture = 100
                                print(f'Mois || {int(round(moisture, 0))}%||',end='')
                        elif side_v == 3:
                            print(" _ _ _ _ _ ___",end='')
                        elif side_v == 2:
                            print("|1|3|4|5|6|   ",end='')
                        else:
                            print("|7|8|0| 99|___",end='')
                    side_h-=1
                side_v-=1
            Microwave.displaydown()
            #jeda waktu microwave berjalan(countdown)
            time.sleep(0.001) 
            self.time -= 1
    def displayClean(self):
         while self.time >= 0:
            os.system('cls')
            Microwave.displayup()
            side_v = 6
            while side_v>0:
                side_h = 38
                while side_h>0:
                    if (side_h == 38) or (side_h == 37) or (side_h == 18) or (side_h == 17) or (side_h == 2):
                        print('|', end='')
                    elif (side_h == 1):
                        print('|')
                    elif side_h<37 and side_h>18:
                        print(' ',end='')
                    elif side_h == 16:
                        if side_v == 6:
                            print(f'Temp || --- ||',end='')
                        elif side_v == 5:
                            min, sec = divmod(self.time, 60)
                            print(f'Time ||{min:02d}:{sec:02d}||',end='')
                        elif side_v == 4:
                            print(f'Mois || --- ||',end='')
                        elif side_v == 3:
                            print(" _ _ _ _ _ ___",end='')
                        elif side_v == 2:
                            print("|1|3|4|5|6|   ",end='')
                        else:
                            print("|7|8|0| 99|___",end='')
                    side_h-=1
                side_v-=1
            Microwave.displaydown()
            time.sleep(0.001) 
            self.time -= 1
    def displayCleanDone():
        Microwave.displayup()
        side_v = 6
        while side_v>0:
            side_h = 38
            while side_h>0:
                if (side_h == 38) or (side_h == 37) or (side_h == 18) or (side_h == 17) or (side_h == 2):
                    print('|', end='')
                elif (side_h == 1):
                    print('|')
                elif side_h<37 and side_h>18:
                    if side_v == 4:
                        if side_h>31 or side_h<23:
                            print(' ',end='')
                        elif side_h == 31:
                            print("Microwave", end='')
                    elif side_v == 3:
                        if side_h>35 or side_h<20:
                            print(' ',end='')
                        elif side_h == 35:
                            print("telah dibersikan", end='')
                    else:
                        print(' ',end='')
                elif side_h == 16:
                    if side_v == 6:
                        print(f'Temp || --- ||',end='')
                    elif side_v == 5:
                        print(f'Time ||00:00||',end='')
                    elif side_v == 4:
                        print(f'Mois || --- ||',end='')
                    elif side_v == 3:
                        print(" _ _ _ _ _ ___",end='')
                    elif side_v == 2:
                        print("|1|3|4|5|6|   ",end='')
                    else:
                        print("|7|8|0| 99|___",end='')
                side_h-=1
            side_v-=1
        Microwave.displaydown()
    def displayover(self):
        Microwave.displayup()
        side_v = 6
        while side_v>0:
            side_h = 38
            while side_h>0:
                if (side_h == 38) or (side_h == 37) or (side_h == 18) or (side_h == 17) or (side_h == 2):
                    print('|', end='')
                elif (side_h == 1):
                    print('|')
                elif side_h<37 and side_h>18:
                    #memberikan Tampilan keadaan makan yang dimasak pada layar Microwave
                    if side_v == 4:
                        if side_h>29 or side_h<26:
                            print(' ',end='')
                        elif side_h == 29:
                            print("OVER", end='')
                    elif side_v == 3:
                        if side_h>29 or side_h<26:
                            print(' ',end='')
                        elif side_h == 29:
                            print("COOK", end='')
                    else:
                        print(' ',end='')
                elif side_h == 16:
                    if side_v == 6:
                        if self.temp < 10:
                            print(f'Temp || {self.temp}°C ||',end='')
                        elif self.temp < 100:
                            print(f'Temp || {self.temp}°C||',end='')
                        else:
                            print(f'Temp ||{self.temp}°C||',end='')
                    elif side_v == 5:
                        print(f'Time ||00:00||',end='')
                    elif side_v == 4:
                        if self.moisture<10:
                            print(f'Mois ||   {int(round(self.moisture, 0))}%||',end='')
                        else:
                            print(f'Mois ||  {int(round(self.moisture, 0))}%||',end='')
                    elif side_v == 3:
                        print(" _ _ _ _ _ ___",end='')
                    elif side_v == 2:
                        print("|1|3|4|5|6|   ",end='')
                    else:
                        print("|7|8|0| 99|___",end='')
                side_h-=1
            side_v-=1
        Microwave.displaydown()
    def displaydry(self):
        Microwave.displayup()
        side_v = 6
        while side_v>0:
            side_h = 38
            while side_h>0:
                if (side_h == 38) or (side_h == 37) or (side_h == 18) or (side_h == 17) or (side_h == 2):
                    print('|', end='')
                elif (side_h == 1):
                    print('|')
                elif side_h<37 and side_h>18:
                    if side_v == 4:
                        if side_h>29 or side_h<27:
                            print(' ',end='')
                        elif side_h == 29:
                            print("DRY", end='')
                    elif side_v == 3:
                        if side_h>29 or side_h<26:
                            print(' ',end='')
                        elif side_h == 29:
                            print("COOK", end='')
                    else:
                        print(' ',end='')
                elif side_h == 16:
                    if side_v == 6:
                        if self.temp < 10:
                            print(f'Temp || {self.temp}°C ||',end='')
                        elif self.temp < 100:
                            print(f'Temp || {self.temp}°C||',end='')
                        else:
                            print(f'Temp ||{self.temp}°C||',end='')
                    elif side_v == 5:
                        print(f'Time ||00:00||',end='')
                    elif side_v == 4:
                        if self.moisture<10:
                            print(f'Mois ||   {int(round(self.moisture, 0))}%||',end='')
                        else:
                            print(f'Mois ||  {int(round(self.moisture, 0))}%||',end='')
                    elif side_v == 3:
                        print(" _ _ _ _ _ ___",end='')
                    elif side_v == 2:
                        print("|1|3|4|5|6|   ",end='')
                    else:
                        print("|7|8|0| 99|___",end='')
                side_h-=1
            side_v-=1
        Microwave.displaydown()
    def displaydone(self):
        Microwave.displayup()
        side_v = 6
        while side_v>0:
            side_h = 38
            while side_h>0:
                if (side_h == 38) or (side_h == 37) or (side_h == 18) or (side_h == 17) or (side_h == 2):
                    print('|', end='')
                elif (side_h == 1):
                    print('|')
                elif side_h<37 and side_h>18:
                    if side_v == 4:
                        if side_h>29 or side_h<26:
                            print(' ',end='')
                        elif side_h == 29:
                            print("WELL", end='')
                    elif side_v == 3:
                        if side_h>29 or side_h<26:
                            print(' ',end='')
                        elif side_h == 29:
                            print("DONE", end='')
                    else:
                        print(' ',end='')
                elif side_h == 16:
                    if side_v == 6:
                        if self.temp < 10:
                            print(f'Temp || {self.temp}°C ||',end='')
                        elif self.temp < 100:
                            print(f'Temp || {self.temp}°C||',end='')
                        else:
                            print(f'Temp ||{self.temp}°C||',end='')
                    elif side_v == 5:
                        print(f'Time ||00:00||',end='')
                    elif side_v == 4:
                        if self.moisture<10:
                            print(f'Mois ||   {int(round(self.moisture, 0))}%||',end='')
                        else:
                            print(f'Mois ||  {int(round(self.moisture, 0))}%||',end='')
                    elif side_v == 3:
                        print(" _ _ _ _ _ ___",end='')
                    elif side_v == 2:
                        print("|1|3|4|5|6|   ",end='')
                    else:
                        print("|7|8|0| 99|___",end='')
                side_h-=1
            side_v-=1
        Microwave.displaydown()
    def menu():
        print(f'======================================')
        print(f'||1. Manual mode  ||6. Seafood      ||')
        print(f'||==================================||')
        print(f'||2. Quick Heat   ||7. input kode   ||')
        print(f'||==================================||')
        print(f'||3. Defrost      ||8. Cleaning     ||')
        print(f'||==================================||')
        print(f'||4. Grill        ||0. Stop         ||')
        print(f'||==================================||')
        print(f'||5. Vegetable    ||99. Child Lock  ||')
        print(f'======================================')
    def menulock():
        print(f'======================================')
        print(f'||1. Manual mode🔒||6. Seafood🔒    ||')
        print(f'||==================================||')
        print(f'||2. Quick Heat🔒 ||7. input kode🔒 ||')
        print(f'||==================================||')
        print(f'||3. Defrost🔒    ||8. Cleaning🔒   ||')
        print(f'||==================================||')
        print(f'||4. Grill🔒      ||0. Stop🔒       ||')
        print(f'||==================================||')
        print(f'||5. Vegetable🔒  ||99.Child Lock🔒 ||')
        print(f'======================================')

    def Start():
        ChildLock = False
        Microwave.display1()
        while True:
            #percabangan untuk menentukan apakah sedang dalam mode Child Lock atau tidak
            if ChildLock == False:
                #menampilkan menu
                Microwave.menu()
                #meminta inputan user terkait fitur yang akan digunkan
                choice = int(input("Pilih menu : "))
                #menghapus tampilan terminal
                os.system('cls')
                #mode memasak manual
                if choice == 1:
                    Microwave.display1()
                    time = int(input("Masukan waktu Memasak(menit) : "))
                    temp = int(input("Masukan Temperatur(°C) : "))
                    moisture = 100
                    #membuat objek baru sesuai dengan inputan user
                    food = Microwave(time, temp, moisture)
                    #menjalanka proses memasak
                    food.moisture1(0.8)
                    food.display2()
                    if food.moisture < 1:
                        os.system('cls')
                        food.displaydry()
                    elif food.moisture < 40:
                        os.system('cls')
                        food.displayover()
                    else:
                        os.system('cls')
                        food.displaydone()
                elif choice == 2:
                    #membuat Condisional Object sesuai dengan fitur yang dipilih user
                    food = mode(2, 150, 90)
                    food.quick_heat()
                elif choice == 3:
                    food = mode(8, 40, 90)
                    food.Deforst()
                elif choice == 4:
                    food = mode(7, 230, 100)
                    food.Grill()
                elif choice == 5:
                    while True:
                        vegetable.menu()
                        sayur = int(input("Pilih Sayur : "))
                        os.system('cls')
                        if sayur == 1:
                            vegen = vegetable(2, 200, 100)
                            vegen.brokoli()
                            break
                        elif sayur == 2:
                            vegen = vegetable(4, 200, 100)
                            vegen.wortel()
                            break
                        elif sayur == 3:
                            vegen = vegetable(4, 180, 100)
                            vegen.kembang_kol()
                            break
                        elif sayur == 4:
                            vegen = vegetable(3, 160, 100)
                            vegen.bayam()
                            break
                        elif sayur == 5:
                            vegen = vegetable(4, 180, 100)
                            vegen.jagung_manis()
                            break
                        elif sayur == 6:
                            vegen = vegetable(4, 200, 100)
                            vegen.paprika()
                            break
                        elif sayur == 7:
                            vegen = vegetable(4, 180, 100)
                            vegen.zucchini()
                            break
                        elif sayur == 0:
                            Microwave.display1()
                            break
                elif choice == 6:
                    while True:
                        seafood.menu()
                        seaf = int(input("Pilih Seafood : "))
                        os.system('cls')
                        if seaf == 1:
                            ikan = seafood(5, 90, 100)
                            ikan.fish()
                            break
                        elif seaf == 2:
                            udang = seafood(3, 80, 100)
                            udang.shrimp()
                            break
                        elif seaf == 3:
                            cumi = seafood(3, 80, 100)
                            cumi.squid()
                            break
                        elif seaf == 4:
                            kerang = seafood(4, 80, 100)
                            kerang.shellfish()
                            break
                        elif seaf == 5:
                            lobster = seafood(7, 90, 100)
                            lobster.lobster()
                            break
                        elif seaf == 0:
                            Microwave.display1()
                            break
                elif choice == 7:
                    while True:
                        food = incode(0,0,0,0,0)
                        food.scancode()
                        if food.barcode == 0:
                            food.barcode = int(input("Masukan Code barcode: "))
                        food.detect(food.barcode)
                        if food.temp == 0:
                            os.system('cls')
                            Microwave.display1()
                            break
                        confirm = input(f'{food.foodname}? (y/n): ').lower()
                        if confirm == 'y':
                            food.cook()
                            break
                elif choice == 8:
                    clean = Microwave(2,0,0)
                    clean.displayClean()
                    os.system('cls')
                    Microwave.displayCleanDone()
                elif choice == 99:
                    Pinlock = int(input("Atur PIN :"))
                    ChildLock = True
                    os.system('cls')
                elif choice == 0:
                    print("Terima Kasih telah menggunakan produk kami hehehe")
                    break
            else:
                Microwave.display1()
                Microwave.menulock()
                #meminta inputan user terkait PIN untuk menonaktifkan Child Lock Mode
                pin = int(input("Masukan PIN :"))
                #mencocokna PIn yang dimasukan oleh user dengan PIN yang di set user
                if pin == Pinlock:
                    ChildLock = False
                    os.system('cls')
                    Microwave.display1()
                elif pin == 0:
                    print("Terima Kasih telah menggunakan produk kami hehehe")
                    break
                else:
                    os.system('cls')
 
#Mulai jalankan Program                                       
Microwave.Start()