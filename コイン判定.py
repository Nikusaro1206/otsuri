nyuukin = int(input("いくら入れましたか？"))
ryoukin = int(input("いくらのものを買いますか"))

nyuukin = nyuukin - ryoukin
maisuu = [1 , 10 , 10 , 10]
if maisuu[0] > 0:
    otsuri_500 = nyuukin // 500
    nyuukin = nyuukin % 500
else:
    otsuri_500 = 0

otsuri_100_kari = nyuukin // 100 
if maisuu[1] > otsuri_100_kari:
    otsuri_100 = nyuukin // 100
    nyuukin = nyuukin % 100
else:
    otsuri_100 = maisuu[1]
    nyuukin = nyuukin - 100 * maisuu[1]

otsuri_50_kari = nyuukin // 50 
if maisuu[2] > otsuri_50_kari:
    otsuri_50 = nyuukin // 50
    nyuukin = nyuukin % 50
else:
    otsuri_50 = maisuu[2]
    nyuukin = nyuukin - 50 * maisuu[2]

otsuri_10_kari = nyuukin // 10
if maisuu[3] > otsuri_10_kari:
    otsuri_10 = nyuukin // 10
    nyuukin = nyuukin % 10

    print(f"500円玉:{otsuri_500}")
    print(f"100円玉:{otsuri_100}")
    print(f"50円玉:{otsuri_50}")
    print(f"10円玉:{otsuri_10}")
else:
    print("精算できません")