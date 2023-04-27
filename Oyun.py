import random #random sayı üretir.
can = 3 
puan = 0

oyun = ["Tas","kagit","makas"]

while(can!=0):
  x = random.randint(0,2)  #o ile 2 arasında random int sayılar üretmemize yardımcı olur.
  PcHamle = oyun[x]
  Hamle= input("tas,kagit,makas???\n") #\ bu işaret için option+? tuşuna basıcan.
  if(PcHamle == Hamle):
      print("Berabere")
  elif(Hamle == "tas"):
      if(PcHamle == "kagit"):
         can-=1
         print("Kaybettiniz", can, "caniniz kaldi")
      else:
         puan +=10
         print("tebrikler! 10 puan kazandiniz!")   
  elif(Hamle =="kagit"):
      if(PcHamle == "makas"):
         can-=1
         print("Kaybettiniz!", can, "caniniz kaldi")
      else:
         
         puan +=10
         print("tebrikler! 10 puan kazandiniz!")
  elif(Hamle == "makas"):
      if(PcHamle == "tas"):
         can-=1
         print("Kaybettiniz!", can, "caniniz kaldi")
      else:
         puan+=10
         print("tebrikler! 10 puan kazandiniz!")
print("Oyun bitti", puan, "puan kazandiniz!")





