import tkinter as tk
import tkinter.messagebox as tkmg

class Aplication(tk.Frame):
    def __init__(self,root=None):
        super().__init__(root,width=300,height=400,
                         borderwidth=4,relief='groove')
        self.root = root
        self.pack()
        self.nyuukin = 0
        self.pack_propagate(0)
        self.create_widgets()

    def create_widgets(self):#GUI部分
        #投入口
        input_coin = tk.LabelFrame(self,text="投入口",padx=10,pady=10)
        coin_btn_1000 =tk.Button(input_coin,text = 1000,command = lambda:self.total_coin(4),padx=5)#1000はあとから付け足したため4
        coin_btn_500 =tk.Button(input_coin,text = 500,command = lambda:self.total_coin(0),padx=5)
        coin_btn_100 =tk.Button(input_coin,text = 100,command = lambda:self.total_coin(1),padx=5)
        coin_btn_50 =tk.Button(input_coin,text = 50,command = lambda:self.total_coin(2),padx=5)
        coin_btn_10 =tk.Button(input_coin,text = 10,command = lambda:self.total_coin(3),padx=5)
        coin_btn_reset =tk.Button(input_coin,text = "リセット",command = self.coin_reset,)
        self.total_Text = tk.StringVar()
        self.total_Text.set(0)
        total_label = tk.Label(input_coin,textvariable=self.total_Text)

        #商品ボタン
        btn_sp = tk.LabelFrame(self,text="商品ボタン",padx=10,pady=10)
        btn_100 = tk.Button(btn_sp,text ="100",command = lambda:self.sentaku_click(100))#押されたとき引数100を渡す
        btn_110 = tk.Button(btn_sp,text ="110",command = lambda:self.sentaku_click(110))
        btn_120 = tk.Button(btn_sp,text ="120",command = lambda:self.sentaku_click(120))
        btn_130 = tk.Button(btn_sp,text ="130",command = lambda:self.sentaku_click(130))
        btn_140 = tk.Button(btn_sp,text ="140",command = lambda:self.sentaku_click(140))
        btn_150 = tk.Button(btn_sp,text ="150",command = lambda:self.sentaku_click(150))
        btn_160 = tk.Button(btn_sp,text ="160",command = lambda:self.sentaku_click(160))
        btn_170 = tk.Button(btn_sp,text ="170",command = lambda:self.sentaku_click(170))
        btn_180 = tk.Button(btn_sp,text ="180",command = lambda:self.sentaku_click(180))
        btn_190 = tk.Button(btn_sp,text ="190",command = lambda:self.sentaku_click(190))
        btn_200 = tk.Button(btn_sp,text ="200",command = lambda:self.sentaku_click(200))

        #釣り銭残量
        turi_in_sp = tk.LabelFrame(self,text ="釣り銭残量",padx=10,pady=10)
        turi_in500_sp = tk.Label(turi_in_sp,text="500円玉:",width=7)
        self.turi_in500_Text = tk.StringVar()
        self.turi_in500_Text.set(maisuu[0])
        self.turi_in500_entry = tk.Entry(turi_in_sp,textvariable=self.turi_in500_Text,width=4)
        turi_in100_sp = tk.Label(turi_in_sp,text="100円玉:",width=7)
        self.turi_in100_Text = tk.StringVar()
        self.turi_in100_Text.set(maisuu[1])
        self.turi_in100_entry = tk.Entry(turi_in_sp,textvariable=self.turi_in100_Text,width=4)
        turi_in50_sp = tk.Label(turi_in_sp,text="50円玉:",width=7)
        self.turi_in50_Text = tk.StringVar()
        self.turi_in50_Text.set(maisuu[2])
        self.turi_in50_entry = tk.Entry(turi_in_sp,textvariable=self.turi_in50_Text,width=4)
        turi_in10_sp = tk.Label(turi_in_sp,text="10円玉:",width=7)
        self.turi_in10_Text = tk.StringVar()
        self.turi_in10_Text.set(maisuu[3])
        self.turi_in10_entry = tk.Entry(turi_in_sp,textvariable=self.turi_in10_Text,width=4)
        turi_rescan_btn = tk.Button(turi_in_sp,text="更新",width=3,command = self.turi_in_entry_scan)

        #釣り銭表示
        turi_sp = tk.LabelFrame(self,text ="釣り銭口",padx=10,pady=10)
        turi_500_sp = tk.Label(turi_sp,text="500円玉:",width=7)
        self.turi_500_Text = tk.StringVar()
        self.turi_500_Text.set(0)
        turi_500_label = tk.Label(turi_sp,textvariable=self.turi_500_Text)
        turi_100_sp = tk.Label(turi_sp,text="100円玉:",width=7)
        self.turi_100_Text = tk.StringVar()
        self.turi_100_Text.set(0)
        turi_100_label = tk.Label(turi_sp,textvariable=self.turi_100_Text)
        turi_50_sp = tk.Label(turi_sp,text="50円玉:",width=7)
        self.turi_50_Text = tk.StringVar()
        self.turi_50_Text.set(0)
        turi_50_label = tk.Label(turi_sp,textvariable=self.turi_50_Text)
        turi_10_sp = tk.Label(turi_sp,text="10円玉:",width=7)
        self.turi_10_Text = tk.StringVar()
        self.turi_10_Text.set(0)
        turi_10_label = tk.Label(turi_sp,textvariable=self.turi_10_Text)
        self.totalChangesText = tk.StringVar()
        self.totalChangesText.set(0)
        totalChangeslabel = tk.Label(turi_sp,textvariable=self.totalChangesText)

        #ウィジェット配置
        line1 = 45
        line2 = 45
        line3 = 150
        line4 = 230
        line5 = 230

        #投入口
        input_coin.place(relx=0.5,y=line1,anchor=tk.CENTER)
        coin_btn_1000.grid(in_ =input_coin,row=0,column=0)
        coin_btn_500.grid(in_ =input_coin,row=0,column=1)
        coin_btn_100.grid(in_ =input_coin,row=0,column=2)
        coin_btn_50.grid(in_ =input_coin,row=0,column=3)
        coin_btn_10.grid(in_ =input_coin,row=0,column=4)
        coin_btn_reset.grid(in_ =input_coin,row=1,column=0)
        total_label.grid(in_ =input_coin,row=1,column=3)

        #商品ボタン
        btn_sp.place(relx = 0.5,y=line3,anchor=tk.CENTER)
        btn_100.grid(in_ =btn_sp,row=0,column=0)
        btn_110.grid(in_ =btn_sp,row=0,column=1)
        btn_120.grid(in_ =btn_sp,row=0,column=2)
        btn_130.grid(in_ =btn_sp,row=0,column=3)
        btn_140.grid(in_ =btn_sp,row=0,column=4)
        btn_150.grid(in_ =btn_sp,row=1,column=0)
        btn_160.grid(in_ =btn_sp,row=1,column=1)
        btn_170.grid(in_ =btn_sp,row=1,column=2)
        btn_180.grid(in_ =btn_sp,row=1,column=3)
        btn_190.grid(in_ =btn_sp,row=1,column=4)
        btn_200.grid(in_ =btn_sp,row=2,column=0)

        #釣り銭残量
        turi_in_sp.place(relx=0.1,y=line4)
        turi_in500_sp.grid(in_ = turi_in_sp,row=0,column = 0)
        self.turi_in500_entry.grid(in_ = turi_in_sp,row=0,column = 1)
        turi_in100_sp.grid(in_ = turi_in_sp,row=1,column = 0)
        self.turi_in100_entry.grid(in_ = turi_in_sp,row=1,column = 1)
        turi_in50_sp.grid(in_ = turi_in_sp,row=2,column = 0)
        self.turi_in50_entry.grid(in_ = turi_in_sp,row=2,column = 1)
        turi_in10_sp.grid(in_ = turi_in_sp,row=3,column = 0)
        self.turi_in10_entry.grid(in_ = turi_in_sp,row=3,column = 1)
        turi_rescan_btn.grid(in_ = turi_in_sp,row = 4,column=1)

        #釣り銭部分
        turi_sp.place(relx=0.6,y=line5)
        turi_500_sp.grid(in_ = turi_sp,row=0,column = 0)
        turi_500_label.grid(in_ = turi_sp,row=0,column = 1)
        turi_100_sp.grid(in_ = turi_sp,row=1,column = 0)
        turi_100_label.grid(in_ = turi_sp,row=1,column = 1)
        turi_50_sp.grid(in_ = turi_sp,row=2,column = 0)
        turi_50_label.grid(in_ = turi_sp,row=2,column = 1)
        turi_10_sp.grid(in_ = turi_sp,row=3,column = 0)
        turi_10_label.grid(in_ = turi_sp,row=3,column = 1)
        totalChangeslabel.grid(in_ = turi_sp ,row = 5, column= 0,columnspan=2,sticky = tk.E)
        #GUI部分終了

    #処理部分
    #投入された合計金額
    def total_coin(self,kingaku): 
        in_coin[kingaku] += 1
        self.nyuukin += coin[kingaku]#押されるたびに処理なので種類を足すだけで済む
        self.total_Text.set(self.nyuukin)

    #商品ボタン押されたあとの枚数の計算から出力まで
    def sentaku_click(self,i):
        ryoukin = int(i)
        nyuukin = self.nyuukin - ryoukin
        self.totalChanges = nyuukin 
        for i in range (0,4):
            nyuukin = self.maisuu_keisan(i,nyuukin)
            if otr[i] < 0:#入金金額が足りない時にマイナスになる
                break
            else:
                pass
        self.output_window(nyuukin)
        self.turi_in_set()

    #枚数の計算
    def maisuu_keisan(self,i,nyuukin):
        otr_kari = nyuukin // coin[i]
        #必要な数と用意のある数の比較
        if otr_kari <= maisuu[i]:
            otr[i] = otr_kari
            return nyuukin % coin[i]
        else:
            otr[i] = maisuu[i]#あるだけいれる
            return nyuukin - (coin[i] * otr[i])

    #精算できたか判定。できてなければinfoで知らせる
    def output_window(self,nyuukin):
        if nyuukin == 0:
            for i in range (0,4):
                maisuu[i] -= otr[i]#使ったお金を引いて
                maisuu[i] += in_coin[i]#入ったお金をいれる。精算前に追加すると精算できないとき処理増える
            self.turi_set()
        else:
            tkmg.showinfo("精算できません","釣り銭切れもしくは金額不足")
        self.stats_reset()

    #釣り銭の表示更新
    def turi_set(self):
        self.turi_500_Text.set(otr[0])
        self.turi_100_Text.set(otr[1])
        self.turi_50_Text.set(otr[2])
        self.turi_10_Text.set(otr[3])
        self.totalChangesText.set(self.totalChanges)

    #指定された値の取得と格納
    def turi_in_entry_scan(self):
        maisuu[0] = int(self.turi_in500_entry.get())
        maisuu[1] = int(self.turi_in100_entry.get())
        maisuu[2] = int(self.turi_in50_entry.get())
        maisuu[3] = int(self.turi_in10_entry.get())
        self.turi_in_set()

    #残りの釣り銭を更新
    def turi_in_set(self):
        self.turi_in500_Text.set(maisuu[0])
        self.turi_in100_Text.set(maisuu[1])
        self.turi_in50_Text.set(maisuu[2])
        self.turi_in10_Text.set(maisuu[3])

    #投入額のリセット
    def coin_reset(self):
        self.nyuukin = 0
        for i in range (0,5):#clear()すると次の精算時参照ができなくてエラー
            in_coin[i] = 0
        self.total_Text.set(self.nyuukin)

    #継承する要素以外のリセット
    def stats_reset(self):
        for i in range (0,4):#clear()すると次の精算時参照ができなくてエラー
            otr[i] = 0
        self.nyuukin = 0
        for i in range (0,5):
            in_coin[i] = 0
        self.total_Text.set(self.nyuukin)
    #処理部分終了


maisuu = [1 , 10 , 10 , 10]
coin = [500 , 100 , 50 ,10 , 1000]
in_coin = [0 , 0 , 0 , 0 , 0]
otr = [0 , 0 , 0, 0]

root = tk.Tk()
root.title("Vending Machine")#title
app = Aplication(root=root)
app.mainloop()