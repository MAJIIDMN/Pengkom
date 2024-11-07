import time
import os
import csv

class comp:
    def __init__(self, time:int, temp:int, moisture:int):
        self.time = time*60
        self.temp = temp
        self.moisture = moisture
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
        comp.moisture1(self, 40)
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
        print(" 1. brokoli")
        print(" 2. wortel\n 3. kembang kol\n 4. bayam")
        print(" 5. jagung manis\n 6. paprika")
        print(" 7. zucchini")
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
        print(" 1. Ikan fillet")
        print(" 2. Udang")
        print(" 3. Cumi-cumi")
        print(" 4. Kerang")
        print(" 5. Lobster")
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
    def __init__(self, time:int, temp:int, moisture:int, barcode:int, namefood):
        super().__init__(time, temp, moisture)
        self.barcode = barcode
        namefood = namefood        
    def detect(self, code):
        csvfile = open('pengkom\\barcodes.csv', newline='')
        foodcode = csv.reader(csvfile)
        next(foodcode)
        barcode = []
        namefood = []
        timefood = []
        tempfood = []
        moisturefood = []
        for row in foodcode:
            barcode.append(int(row[1]))
            namefood.append(row[2])
            timefood.append(int(row[3])*60)
            tempfood.append(int(row[4]))
            moisturefood.append(int(row[5]))
        csvfile.close()
        for i in range(len(barcode)):
            if code == barcode[i]:
                self.namefood = namefood[i]
                self.barcode = barcode[i]
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
                            elif moisture<100:
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
            time.sleep(0.0001) 
            self.time -= 1
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
        print(f'||==================================||')
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
        print(f'||==================================||')

    def Start():
        ChildLock = False
        Microwave.display1()
        while True:
            if ChildLock == False:
                Microwave.menu()
                choice = int(input("Pilih menu : "))
                os.system('cls')
                if choice == 1:
                    Microwave.display1()
                    time = int(input("Masukan waktu Memasak(menit) : "))
                    temp = int(input("Masukan Temperatur(°C) : "))
                    moisture = 100
                    food = Microwave(time, temp, moisture)
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
                elif choice == 6:
                    while True:
                        seafood.menu()
                        seaf = int(input("Pilih Seafood : "))
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
                elif choice == 7:
                    while True:
                        code = int(input("Masukan Code barcode: "))
                        food = incode(0,0,0,0,0)
                        food.detect(code)
                        confirm = input(f'{food.namefood}? (y/n): ').lower()
                        if confirm == 'y':
                            food.cook()
                            break
                elif choice == 8:
                    Microwave.display1()
                    print("Microwave telah dibersikan")
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
                pin = int(input("Masukan PIN :"))
                if pin == Pinlock:
                    ChildLock = False
                    os.system('cls')
                    Microwave.display1()
                elif pin == 0:
                    print("Terima Kasih telah menggunakan produk kami hehehe")
                    break
                else:
                    os.system('cls')
                                 
Microwave.Start()
