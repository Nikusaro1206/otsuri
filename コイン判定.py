import tkinter as tk
import tkinter.messagebox as tkmg

class Aplication(tk.Frame):
    def __init__(self,root=None):
        super().__init__(root,width=380,height=480,
                         borderwidth=4,relief='groove')
        self.root = root
        self.pack()
        self.pack_propagate(0)
        self.create_widgets()

    def create_widgets(self):
        lbl_1000 = tk.Label(self,text="1000")
        lbl_500 = tk.Label(self,text="500")
        lbl_100 = tk.Label(self,text="100")
        lbl_50 = tk.Label(self,text="50")
        lbl_10 = tk.Label(self,text="10")
        self.text_1000 = tk.Entry(self,width=2)
        self.text_500 = tk.Entry(self,width=2)
        self.text_100 = tk.Entry(self,width=2)
        self.text_50 = tk.Entry(self,width=2)
        self.text_10 = tk.Entry(self,width=2)

        btn_100 = tk.Button(self,text ="100",command = lambda:self.sentaku_click(100))
        btn_110 = tk.Button(self,text ="110",command = lambda:self.sentaku_click(110))
        btn_120 = tk.Button(self,text ="120",command = lambda:self.sentaku_click(120))
        btn_130 = tk.Button(self,text ="130",command = lambda:self.sentaku_click(130))
        btn_140 = tk.Button(self,text ="140",command = lambda:self.sentaku_click(140))

        lbl_1000.pack()
        self.text_1000.pack()
        lbl_500.pack()
        self.text_500.pack()
        lbl_100.pack()
        self.text_100.pack()
        lbl_50.pack()
        self.text_50.pack()
        lbl_10.pack()
        self.text_10.pack()

        btn_100.pack()
        btn_110.pack()
        btn_120.pack()
        btn_130.pack()
        btn_140.pack()


    def sentaku_click(self,i):
        in_1000 = int(self.text_1000.get())
        in_coin[0] = int(self.text_500.get())
        in_coin[1] = int(self.text_100.get())
        in_coin[2] = int(self.text_50.get())
        in_coin[3] = int(self.text_10.get())
        #print(in_coin[0])
        #print(in_coin[1])
        #print(in_coin[2])
        #print(in_coin[3])
        nyuukin = int(1000*in_1000+500*in_coin[0] + 100*in_coin[1] + 50*in_coin[2] +10*in_coin[3])
        #print(nyuukin)

        ryoukin = int(i)
        nyuukin = nyuukin - ryoukin
        #print(nyuukin)

        for i in range (0,4):
            nyuukin = self.maisuu_keisan(i,nyuukin)
            #print(nyuukin)
        self.output_window(nyuukin)

    def maisuu_keisan(self,i,nyuukin):
        otr_kari = nyuukin // coin[i]
        if maisuu[i] >= otr_kari:
            otr[i] = otr_kari
            return nyuukin % coin[i]
        else:
            otr[i] = maisuu[i]
            return nyuukin - (coin[i] * otr[i])
        
    def output_window(self,nyuukin):
        if nyuukin == 0:
            print(f"500円玉:{otr[0]}")
            print(f"100円玉:{otr[1]}")
            print(f"50円玉:{otr[2]}")
            print(f"10円玉:{otr[3]}")
            for i in range (0,4):
                maisuu[i] = maisuu[i] - otr[i]
                maisuu[i] = maisuu[i] + in_coin[i]
            print(maisuu)
        else:
            print("精算できません")
            print(maisuu)
        self.stats_reset()

    def stats_reset(self):
        otr = [0 , 0 , 0, 0]

maisuu = [1 , 10 , 10 , 10]
coin = [500 , 100 , 50 ,10]
in_coin = [0 , 0 , 0 , 0]
otr = [0 , 0 , 0, 0]

root = tk.Tk()
root.title("Vending Machine")#title
app = Aplication(root=root)
app.mainloop()