# 社会人1年目のスケジュール最適化アプリ

1週間のスケジュールが①作成, ②可視化, ③pdf形式でダウンロードできるアプリ

# DEMO

1. ホーム画面で「新メンバー追加」をクリックして下さい。  
![スクリーンショット 0003-08-17 午後3 51 08](https://user-images.githubusercontent.com/66200485/129677581-092644f7-91bf-41a7-82aa-1d2a4cf09fcb.png)  
*ホーム画面*
<br>

2. 名前と所属部署を入力した後、「曜日ごとのスケジュール」と「1週間のうちにやるべきタスク」を入力し、「新メンバー追加(緑ボタン)」をクリックして下さい。    
![スクリーンショット 0003-08-17 午後3 51 58](https://user-images.githubusercontent.com/66200485/129677684-8a9f66b6-880a-40f3-8610-3021cf19ef6a.png)  
*入力ページ*
<br>  

3. 「Mypageボタン(青ボタン)」をクリックすると、「曜日ごとのスケジュール」と「1週間のうちにやるべきタスク」が表示されます。  
ページ下にある「アクションプランを確認する(緑ボタン)」をクリックして下さい。  
![スクリーンショット 0003-08-17 午後3 52 39](https://user-images.githubusercontent.com/66200485/129677783-0c8b88ad-ae5f-45be-9784-54a7b1f2dc83.png)  
*Mypage*
<br>  
 
4. タスク毎の緊急度、重要度、モチベーション、難易度のスコアを元に1週間のスケジュールが作成されます。  
Mypageに戻り、「アクションプランのDL(赤ボタン)」をクリックして下さい。  
![スクリーンショット 0003-08-17 午後3 52 53](https://user-images.githubusercontent.com/66200485/129677819-3b6bf278-3dc4-4f60-bf1e-604f8e3d51f0.png)  
*アクションプラン確認ページ*
<br>  
 
5. 作成された1週間のスケジュールがPDF形式でダウンロードできます。    
![スクリーンショット 0003-08-17 午後3 53 51](https://user-images.githubusercontent.com/66200485/129677987-4072b099-b4c7-4c34-83d2-66da00345e89.png)  
*PDF*

# Features
- スケジュールが作成、可視化、ダウンロードできます。
- 作成した1週間のスケジュールをpdfでダウンロードできるようにしました。
- 毎週１週間の予定を組み立てる作業を自動化し、最適な順番を示すことでマルチタスク状態になってしまうことを避けることができます。  
- また、リーダーはチームメンバーが仕事に対してどのような心境であるのか把握することができます。

## Scheduling Algorithm
自分が最適だと考える作業順をアルゴリズムにしました。

1. 「重要であり緊急でもあるもの」の次は「重要であり緊急でないもの」を行う。

2. スケジュールが多い日はタスクを減らす。

3. 週の後半にバッファを残す。

4. 午前中には難易度の高い仕事を行う。

5. １番目にやることには、難易度が低く達成できるものを配置する。

# DB
![スクリーンショット 0003-09-07 午前0 36 28](https://user-images.githubusercontent.com/66200485/132239922-2145e408-8b89-4ab3-a9a4-b806afb6db45.png)
![スクリーンショット 0003-09-07 午前0 36 53](https://user-images.githubusercontent.com/66200485/132239964-fdf015ac-dfbd-4a4b-b205-ca43441621bd.png)

# Requirement

**ページのリンク**：http://45.76.98.152/list/  
**言語**：Python 3.9.4  
**フレームワーク**：Django 3.1.7  
**開発期間**:3週間  
**開発環境**：MacOS  
**外部サーバー(OS)**：vultur(ubuntu)  
**DB**：外部サーバー上ではPostgreSQLを使用  
**ライブラリ**:  
matplotlib 3.4.2  
pandas 1.3.0  
numpy 1.20.0  
json  
io  
copy  
csv  
japanize_matplotlib  

# Installation

```bash
pip install python3
pip install Django
pip install matplotlib
pip install pandas
pip install numpy
pip install json
pip install io
pip install copy
pip install csv
pip install japanize_matplotlib
```

# Usage
このリポジトリの利用方法
1. 以下をターミナルで実行して下さい。
```bash
git clone https://github.com/tomohiko9090/ScheduleRevolution.git
cd ScheduleRevolution/
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver
```
2. http://127.0.0.1:8000/list
へアクセスして下さい。
3. http://127.0.0.1:8000/admin
では、管理画面を使用できます。
<img width="280" alt="スクリーンショット 0003-08-23 午後11 02 11" src="https://user-images.githubusercontent.com/66200485/130460801-97b02801-03a1-433c-ad1f-ceff97be8fd0.png">

# Author

* 作成者 Hikotomo!
