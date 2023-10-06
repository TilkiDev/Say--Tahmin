from random import randint

sayi=randint(1,10)
sayi=str(sayi)

can=3


print("Merhaba yarışmacı bugün 1-10 arası sayı belirleyeceğiz ve o sayıyı tahmin etmeye çalışacaksın \n eğer doğru tahmin yaparsan oyunu kazanacaksın fakat 3 yanlış yaparsan yarışmadan eleneceksin hazırmısın?")
print("Hazır olduğunda tahminini yapabilirsin")



while can>0:
		cevap=(input("TAHMİN: " ))
		
		

		if sayi not in cevap:
			can-=1
			print(f"Yanlış tahmin geriye {can} canın kaldı")
		else:
			print("DOĞRU TAHMİN OYUNU KAZANDIN")
			break
		if can==0:
			print(f"KAYBETTİNİZ DOĞRU CEVAP {sayi}")