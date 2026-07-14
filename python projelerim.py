import random 
gizli_sayi = random.randint(1, 100)
deneme=0
while True:
    deneme += 1
    tahmin = int(input("1 ile 100 arasında bir sayı tahmin edin: "))
    if tahmin < gizli_sayi:
        print("Daha büyük bir sayı söyleyin.")
    elif tahmin > gizli_sayi:
        print("Daha küçük bir sayı söyleyin.")
    else:
        print("Tebrikler! Doğru sayıyı buldunuz.")
        print("Deneme sayısı:", deneme)
        break