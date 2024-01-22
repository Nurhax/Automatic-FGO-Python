import win32api as win1, win32con as win2
import keyboard as key
import pyautogui as pyg
import time as tm
import random as rand
import threading

#variabel global dari slider pas milih waver
slider = 338

#var loading boolean
loading = False

#function nunggu loading bjir
def tungguLoading():
    loading = True
    while True:
        try:
           while loading:
            pyg.locateCenterOnScreen('Y:\piton_kode\PersonalProj\AutoFGO\\Loading.jpg', region=(1300,900,632,181), confidence = 0.80)
            tungguGlobal()
            print("Masih loading")
        except:
            print("Udah Gak Loading")
            break
    

#procedure buat offset bot sekitar 3 detik
def tungguGlobal():
    tm.sleep(2.5)

#procedure nambah staminda di menu utama
def staminup():
    click(229,1033)
    tungguGlobal()
    click(525,502)
    tm.sleep(2)
    click(1188, 843)

#procedure pilih kartu random
def pilihkartu():
    kartu = rand.sample(range(1,6), k = 2)
    pencet(str(kartu[0]))
    pencet(str(kartu[1]))

#fungsi klik tombol mouse
def click(x,y):
    win1.SetCursorPos((x,y))
    win1.mouse_event(win2.MOUSEEVENTF_LEFTDOWN, 0,0)
    tm.sleep(0.2) #pause setengah detik buat skrip ini
    win1.mouse_event(win2.MOUSEEVENTF_LEFTUP, 0, 0)

#fungsi mencet suatu key di keyboard
def pencet(x):
    pyg.keyDown(x)
    tm.sleep(0.2)
    pyg.keyUp(x)

#fungsi scroll
def turun(y):
    tm.sleep(1)
    pyg.click(1751,y+72)

#Menu mulai

diam = False
stamina = 0
repeat = 0
ulang = int(input("Jumlah repeat farming: "))
stamina = int(input("Jumlah AP Saat ini: "))



#(Duluan):
#Tanya ke user udh masuk ke menu support atau belum, kalau belum mulai dari sini, kalau udah langsung ke code bawah
def menuFGO():
    maw = str(input("Langsung ke menu support? (Y/N): "))
    if maw == "N" or maw == "n" and diam == False:
        print("Mulai dari awal ya!")
        tungguGlobal()
        #ngecek apakah dia di menu utama fgo.
        #Dia nge try buat klik gambar yang ada di menu utama, kalau belum ada dia click tengah layar terus pass
        while True:
            try:
                #klik tombol chaldea gate
                p1,l1 = pyg.locateCenterOnScreen('AutoFGO\\Gate.jpg', region=(0,0,1856,1920), confidence = 0.7)
                click(p1,l1)
                break
            except:
                click(960,540)
                tungguGlobal()
                pass
        #kalo staminanya kurang dari 40 tambah staminanya
        if stamina < 40:
            staminup()
        #klik tombol daily quest, pake error handling takutnya terkahir kali main buka menu lain.
        while True:
            try:
                tungguGlobal()
                dailyX,dailyY = pyg.locateCenterOnScreen('AutoFGO\\Quest.jpg', region=(0,0,1856,1920), confidence = 0.7)
                click(dailyX,dailyY)
                break
            except:
                click(1761,222)
                tungguGlobal()
                pass
        #klik paling bawah scrollbar
        tungguGlobal()
        click(1763, 813)
        #klik yang ada tanda previous atau extreme atau required levelnya 60
        tungguGlobal()
        click(1344,333)

#Main Farming Loop
def mainLoop(repeat,ulang):
    while repeat != ulang:
        #balik ke window fgo
        print("Farming Dimulai")
        tungguGlobal()
        #tunggu loadignnya dulu :C
        tungguLoading()
        #klik icon mage
        while True:
            try:
                m1,m2 = pyg.locateCenterOnScreen('AutoFGO\\mage.jpg', region=(0,0,1856,1920), confidence = 0.8)
                tungguGlobal()
                tungguGlobal()
                tungguGlobal()
                click(m1,m2)
                break
            except:
                print("Belum ada icon mage")
                pass
    #cari gambar zhuge liang/waver kalau gak ada skrol ke bawah (cek terus sampe bawah, kalo gak ada klik update list)
        pyg.moveTo(1751,338)
        while True:
            try:
                #ngecek apakah ada waver di screenshot tersebut?
                tungguGlobal()
                cekWaver1X,cekWaver1Y = pyg.locateCenterOnScreen('AutoFGO\\Waver2.jpg', region=(0,0,1856,1920), confidence = 0.8)
                tungguGlobal()
                click(cekWaver1X,cekWaver1Y)
                #kalo dia gak ada waver
                break
            except:
                try:
                    tungguGlobal()
                    cekWaver2X,cekWaver2Y = pyg.locateCenterOnScreen('AutoFGO\\Waver1.jpg', region=(0,0,1856,1920), confidence = 0.8)
                    tungguGlobal()
                    click(cekWaver2X,cekWaver2Y)
                    break
                except:
                    turun(slider)
                    slider = slider + 42
                    #Kalo slider nya udah mentok
                    if slider > 1080:
                        click(1304,245)
                        click(1182,839)
                        slider = 338
                        tungguGlobal()
                pass
        slider = 72
        #klik start quest
        if repeat == 0:
            tungguGlobal()
            click(1621,998)
        #ngecek apakah dia udah di battle screen, jika udh lakuin hal berikut:
        tungguGlobal()
        while True:
            try:
                s1,s2 = pyg.locateCenterOnScreen('AutoFGO\\Utama.jpg', region=(0,0,1856,1920), confidence = 0.9)
                click(s1,s2)
                print("Gasskeun Bang!")
                break
            except:
                print("Masih Loading")
                pass
        #1. Klik skill 1 nya sessyoin, klik satu kali lagi biar cepet
        tungguGlobal()
        click(104,860)
        click(104,860)
        #2. Klik attack
        tungguGlobal()
        click(1594,896)
        #3. Klik ulti sessyoin
        tungguGlobal()
        click(583, 338)
        #4. Klik random dari 1 - 5
        tungguGlobal()
        pilihkartu()
        #4.5 tunggu buat np nya
        while True:
            try:
                a1,a2 = pyg.locateCenterOnScreen('AutoFGO\\Utama.jpg', region=(0,0,1856,1920), confidence = 0.9)
                click(a1,a2)
                print("Lanjutkeun!")
                break
            except:
                print("Masih NP Pertama")
                pass
        #5. Klik Skill 1,2,3 waver personal(dari kanan)
        tungguGlobal()
        click(1235,867)
        click(1235,867)
        tungguGlobal()
        click(1135,871)
        click(1135,871)
        tungguGlobal()
        click(1004,868)
        tungguGlobal()
        click(435, 659)
        click(435, 659)
        #5.5 klik skill 1 waver orang (dari kiri) terus sessyoin
        tungguGlobal()
        click(548,867)
        tungguGlobal()
        click(435, 659)
        click(435, 659)
        #6. Klik skill sessyoin yang ke 2
        tungguGlobal()
        click(215, 864)
        click(215, 864)
        #7. Klik attack
        tungguGlobal()
        click(1594,896)
        #8. Klik ulti sessyoin
        tungguGlobal()
        click(583, 338)
        #9. Klik random dari 1 - 5
        tungguGlobal()
        pilihkartu()
        #9.5. tunggu sampai NP selesai
        while True:
            try:
                a1,a2 = pyg.locateCenterOnScreen('AutoFGO\\Utama.jpg', region=(0,0,1856,1920), confidence = 0.8)
                click(a1,a2)
                print("Lanjutkeun!")
                break
            except:
                print("Masih NP Kedua")
                pass
        #10. Klik master skill, skill 3
        tungguGlobal()
        click(1681,499)
        tungguGlobal()
        click(1503,473)
        #11. Klik sessyoin, klik maid alter, klik replace
        tungguGlobal()
        click(242,521)
        tungguGlobal()
        click(1089,524)
        tungguGlobal()
        click(919,946)
        #12. Klik skill maid alter 1,3 waver 1, sama master skill 1,2
        tungguGlobal()
        tungguGlobal()
        click(122,845)
        click(122,845)
        tungguGlobal()
        click(338,871)
        click(338,871)
        tungguGlobal()
        click(791,863)
        click(791,863)
        tungguGlobal()
        click(681,866)
        click(681,866)
        tungguGlobal()
        click(1681,499)
        tungguGlobal()
        click(1285,501)
        tungguGlobal()
        click(1681,499)
        tungguGlobal()
        click(1395,492)
        #13. Klik attack
        tungguGlobal()
        click(1594,896)
        #14. Klik ult maid
        tungguGlobal()
        click(583, 338)
        #15. klik random 1 - 5
        tungguGlobal()
        pilihkartu()
        #16. tunggu np sampe selesai
        while True:
            try:
                x,y = pyg.locateCenterOnScreen('AutoFGO\\Done.jpg', region=(0,0,1856,1920), confidence = 0.8)
                click(x,y)
                print("Putaran ke", repeat+1, "sudah selsai.")
                #17. Klik sekali, klik 2 kali
                tungguGlobal()
                click(960,540)
                tungguGlobal()
                click(960,540)
                click(960,540)
                #18. Klik next
                tungguGlobal()
                click(1525,943)
                tungguGlobal()
                break
            except:
                print("Masih np")
                pass
    #19. repeat++
        repeat = repeat + 1
    #19.5 stamina ngurang 40 poin
        stamina = stamina - 40
    ## Jika supportnya bukan friend
        while True:
            try:
                #ngecek apakah dia friend atau bukan
                pyg.locateCenterOnScreen('AutoFGO\\Support.jpg', region=(0,0,1856,1920), confidence = 0.9)
                click(438,915)
                tungguGlobal()
                #klik repeat
                click(1165,852)
                if stamina < 40:
                    #21. Klik Golden Fruit
                    tungguGlobal()
                    click(545,500)
                    #22. Klik Ok
                    tungguGlobal()
                    click(1163,856)
                break
            except:
                #20. Klik Repeat
                if repeat != ulang:
                    tungguGlobal()
                    click(1168,846)
                ## jika kehabisan stamina:
                if stamina < 40 and repeat != ulang:
                    tungguGlobal()
                    #21. Klik Golden Fruit
                    click(1166,497)
                    #22. Klik Ok
                    tungguGlobal()
                    click(1134,835)    
                break

def mulaiMainLoop():
    threading.Thread(target= mainLoop, daemon = True, args = ((repeat,),(ulang,))).start()

def berhenti():
    print("Pencet key z kalau error atau udah selesai")
    while True:
        if key.is_pressed('z'):
            #kalo error ditengah jalan
            print("Ada error sehingga farming dilakukan sebanyak",repeat,"Kali")
            break
        elif repeat == ulang:
            #farming selesai
            print("Farming selesai dan sudah dilakukan sebanyak",repeat,"kali")
            break








