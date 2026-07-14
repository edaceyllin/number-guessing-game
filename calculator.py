print("===========HESAP MAKİNESİ============")
a=int(input("bir a sayisi giriniz: "))
b=int(input("ikinci b sayisi giriniz: "))
seçim=int(input("bir işlem seçiniz: 1-toplama 2-çıkarma 3-çarpma 4-bölme  "))
toplama=a+b
çıkarma=a-b
çarpma=a*b
bölme=a/b

if seçim==1:
    print("toplama sonucu:",toplama)
elif seçim==2:
    print("çıkarma sonucu:",çıkarma)
elif seçim==3:
        print("çarpma sonucu:",çarpma)
elif seçim==4:
             print("bölme sonucu:",bölme) 
else:
               print("geçersiz işlem seçtiniz")

