#library
import os
import datetime
import string
import random
import pytz


#system
x=''.join(random.choices(string.digits, k=3))
y=''.join(random.choices(string.ascii_uppercase, k=3))
asia = pytz.timezone('Asia/Jakarta')
waktu = datetime.datetime.now(asia)
nafile = ''.join(random.choices(string.ascii_uppercase, k=3))

#Storage
Namabarang = []
Hargabarang = []
totalharga = []
dapatdiskon = []
jumlah=[]
subtotal = 0
urutan = 0

os.system('cls') #clear session 'cls' for windosw

#Proses Input Data
namakasir = str(input('Nama Kasir?\nJawab: '))
f = open(f"Write By {namakasir}.txt", "w") #disini soalnya variabelnya baru
print('-------------------------------------------')
Banyakbeli = int(input('Berapa banyak barang yang dibeli?\nJawab: '))

while urutan < Banyakbeli :
    os.system('cls') 
    print(f'Barang ke {urutan+1} / {Banyakbeli}')
    Namabarang.append(input('Nama Barang yang dibeli?\nJawab: '))
    print('-------------------------------------------')
    Hargabarang.append(int(input('Berapa harganya?\nJawab: ')))
    print('-------------------------------------------')
    jumlah.append(int(input('Jumlah yang diambil?\nJawab: ')))
    totalharga.append(Hargabarang[urutan]*jumlah[urutan])
    urutan = urutan + 1

os.system('cls') #clear session 'cls' for windosw

bayar = int(input('Bayar pakai uang berapa?\nJawab:'))

os.system('cls') #clear session 'cls' for windosw

#Proses Nulis d txt
f.write('''\nJl. Prof Dr. Sudar 68, Jagalah,
   Baharaju, Kota Namakota.
       Jawa Tenggara, 53239
          081232449437''') #masih bermasalah
f.write('\n-------------------------------------')
f.write(waktu.strftime("\n%d %b %Y               %X"))
f.write(f'''\nReceipet Number           {x}{y}
Collected By              {namakasir}
------------------------------------
Nama Menu                 Total''')

urutan2 = 0
while urutan2 < Banyakbeli:
    subtotal = subtotal + totalharga[urutan2]
    f.write('\n '+str(Namabarang[urutan2]))
    f.write(f'\n {jumlah[urutan2]}    x Rp.{Hargabarang[urutan2]}          Rp.{totalharga[urutan2]}')
    f.write('')
    urutan2 = urutan2 + 1
f.write('\n-------------------------------------')    
  
f.write(f'\nSubtotal                   Rp.{subtotal:<10}')
f.write(f'\nBayar                      Rp.{bayar:<10}')
f.write(f'\nKembalian                  Rp.{bayar-subtotal:<10}')
f.write('\n-------------------------------------')
f.write('\nNotes')
f.write( '''\nWifi: CAFEE-CAFFEAN
Password:  EVERYDAYNGOPI
"Jangan Lupa ulasan & reviewnya
ya kak" :D''') 

