# İrem Selen, hafta 2, ödev sorusu 1

fiyat = {"muz": 4, "elma": 2, "portakal": 1.5, "armut": 3}
stok = {'muz': 6, 'elma': 8, 'portakal': 32, 'armut': 15}
print("fiyat", fiyat)
print("stok", stok)
for j in range(3):
    print("%d. MUSTERI" % (j+1))
    print("Alisverisiniz bittiginde son yaziniz")
    meyve = []
    miktar = []
    tutar = 0
    for i in range(5):
        y = input("almak isteginiz meyveyi giriniz")
        meyve.append(y)
        if meyve[i] == "son":
            break
        x = int(input("almak isteginiz meyveyinin miktarini giriniz"))
        miktar.append(x)
        if meyve[i] not in stok.keys():
            print("aradiginiz meyve stoklarda bulunmamaktadir")
            continue
        if (meyve[i] in stok.keys() and stok[meyve[i]] - miktar[i] < 0 and stok[meyve[i]] != 0):
            z = int(input("%s stoklari yetersiz daha az almayi deneyin" % meyve[i]))
            while (stok[meyve[i]] - z) < 0:
                z = int(input("%s stoklari yetersiz  daha az almayi deneyin" % meyve[i]))
            stok.update({(meyve[i], stok[meyve[i]] - z)})
            print("stok:", stok)
            tutar += fiyat[meyve[i]] * z
        elif (meyve[i] in stok.keys() and (stok[meyve[i]] - miktar[i]) > 0):
            stok.update({(meyve[i], stok[meyve[i]] - miktar[i])})
            print("stok:", stok)
            tutar += fiyat[meyve[i]] * miktar[i]
        elif (meyve[i] in stok.keys() and (stok[meyve[i]] - miktar[i]) == 0):
            stok.update({(meyve[i], stok[meyve[i]] - miktar[i])})
            print("stok:", stok)
            tutar += fiyat[meyve[i]] * miktar[i]
        if (stok[meyve[i]] == 0):
            print("%s stoklari bitmistir" % meyve[i])
        print("tutar=", tutar)