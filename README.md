# otsuri.py
# 基本仕様
- プログラミング言語：Python
- GUIライブラリ:tkinter
  
# 環境
- Python3.9
- tkinter8.9

# 注意
- 安定版のCLIのみのコイン判定(簡易版).pyとGUIのコイン判定.pyがあります
# 使用方法(簡易版)
1. コイン判定(簡易版).pyを実行
1. 必要に応じてリストmaisuuの中を変更してください。[500円玉,100円玉,50円玉,10円玉]の枚数です
1. コマンドラインで購入するものの金額を聞かれるのでキーボードで入力してください
1. コマンドラインで投入金額を聞かれるのでキーボードで入力してください
1. コマンドラインに返却枚数が表示されます。釣り銭切れの場合"精算できません"と表示されます

# 使用方法(GUI版)
1. コイン判定.pyを起動します
1. ~~必要に応じてリストmaisuuの中を変更してください。[500円玉,100円玉,50円玉,10円玉]の枚数です~~  
  自販機内の釣り銭を変更したいときは「釣り銭残量」内のテキストボックスに任意の値を入力し、「更新」を押してください。釣り銭残量が変更されます
1. 「投入口」から任意のボタンを押して金銭を投入してください。一回押すごとに一枚投入されます
1. 投入金額は「投入口」右下の値から確認できます
1. 「商品ボタン」から任意の金額の商品を選択してください
1. お釣りが釣り銭口にお釣りの種類と枚数が表示されます
1. 釣り銭切れもしくは金額不足のときはウィンドウが表示され、投入金がクリアされます。金銭の投入から再開してください
1. 自販機内の釣り銭は「釣り銭残量」に表示されます


# 今後
- ~~GUIの実装~~
