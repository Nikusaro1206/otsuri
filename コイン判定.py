def maisuu_keisan(i,nyuukin):
    otr_kari = nyuukin // coin[i]
    if maisuu[i] >= otr_kari:
        otr[i] = otr_kari
        return nyuukin % coin[i]
    else:
        otr[i] = maisuu[i]
        return nyuukin - (coin[i] * otr[i])
    
ryoukin = int(input("いくらのものを買いますか"))
nyuukin = int(input("いくら入れましたか？"))

maisuu = [1 , 10 , 10 , 10]
coin = [500 , 100 , 50 ,10]
otr = [0 , 0 , 0, 0]

nyuukin = nyuukin - ryoukin

for i in range (0,4):
    nyuukin = maisuu_keisan(i,nyuukin)

if nyuukin == 0:
    print(f"500円玉:{otr[0]}")
    print(f"100円玉:{otr[1]}")
    print(f"50円玉:{otr[2]}")
    print(f"10円玉:{otr[3]}")
else:
    print("精算できません")