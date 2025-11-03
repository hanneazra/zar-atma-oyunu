import random
print ("Zar Atma Oyununa Hoş Geldiniz!")

zar_yüzleri = {
    1: "⚀",
    2: "⚁",
    3: "⚂",
    4: "⚃",
    5: "⚄",
    6: "⚅"
}
while True:
    input("Zar atmak için Enter’a bas...")
    zar = random.randint(1, 6)
    print(f"Zarın sonucu: {zar} {zar_yüzleri[zar]}")
    
    devam = input("Tekrar atmak ister misin? (e/h): ").lower()
    if devam != "e":
        print("Oyun bitti! 👋")
        break