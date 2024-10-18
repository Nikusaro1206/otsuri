def maisuu_keisan(i,nyuukin):
    otkr = nyuukin // coin[i]
    print(otkr)
    if maisuu[i] >= otkr:
        ot[i] = otkr
        return nyuukin % coin[i]
    else:
        ot[i] = maisuu[i]
        return nyuukin - (coin[i] * ot[i])

nyuukin = int(input("いくら入れましたか？"))
ryoukin = int(input("いくらのものを買いますか"))

maisuu = [1 , 10 , 10 , 10]
coin = [500 , 100 , 50 ,10]
ot = [0 , 0 , 0, 0]

nyuukin = nyuukin - ryoukin

for i in range (0,4):
    print(ot)
    nyuukin = maisuu_keisan(i,nyuukin)

if nyuukin == 0:
    print(f"500円玉:{ot[0]}")
    print(f"100円玉:{ot[1]}")
    print(f"50円玉:{ot[2]}")
    print(f"10円玉:{ot[3]}")
else:
    print("精算できません")