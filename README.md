
 ## 内容
**メイン機能**：  
- 1週間のスケジュールの自動で作成、可視化できる(matplotlibを使用)     

**サブ機能**：  
- リーダーはチームメンバーが仕事に対してどのような心境であるのか把握できる  

**開発経緯**：  
- 毎週１週間の予定を組み立てる作業を自動化し、最適な順番を示すことでマルチタスク状態になってしまうのを避けたいと考えたから。  

**工夫した点**:   
- 「7つの習慣」の緊急重要マトリクスを用いて、人生にとって大切である「重要であり緊急でないもの」を実行できる予定の組み方にした点。  
- 作成した1週間のスケジュールをpdfでダウンロードできるようにした点。  


## アプリの使用方法
1. このリポジトリをclone
2. 以下を実行
以下を実行
```
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsurperuser
python3 manage.py runserver
```




# 社会人1年目のスケジュール最適化アプリ

1週間のスケジュールの生成&可視化アプリ

# DEMO

1. ホーム画面で「新メンバー追加」をクリックして下さい。  
![スクリーンショット 0003-08-17 午後3 51 08](https://user-images.githubusercontent.com/66200485/129677581-092644f7-91bf-41a7-82aa-1d2a4cf09fcb.png)  
ホーム画面
<br>

2. 名前と所属部署を入力した後、「曜日ごとのスケジュール」と「1週間のうちにやるべきタスク」を入力し、「新メンバー追加」をクリックして下さい。    
![スクリーンショット 0003-08-17 午後3 51 58](https://user-images.githubusercontent.com/66200485/129677684-8a9f66b6-880a-40f3-8610-3021cf19ef6a.png)  
入力ページ
<br>  

3. Mypageボタンをクリックすると、「曜日ごとのスケジュール」と「1週間のうちにやるべきタスク」が表示されます。  
ページ下にある「アクションプランを確認する(緑ボタン)」をクリックして下さい。  
![スクリーンショット 0003-08-17 午後3 52 39](https://user-images.githubusercontent.com/66200485/129677783-0c8b88ad-ae5f-45be-9784-54a7b1f2dc83.png)  
Mypage
<br>  
 
4. タスク毎の緊急度、重要度、モチベーション、難易度のスコアを元に1週間のスケジュールが作成されます。  
Mypageに戻り、「アクションプランのDL(赤ボタン)」をクリックして下さい。  
![スクリーンショット 0003-08-17 午後3 52 53](https://user-images.githubusercontent.com/66200485/129677819-3b6bf278-3dc4-4f60-bf1e-604f8e3d51f0.png)  
アクションプラン確認ページ
<br>  
 
5. 作成された1週間のスケジュールがPDF形式でダウンロードできます。    
![スクリーンショット 0003-08-17 午後3 53 51](https://user-images.githubusercontent.com/66200485/129677987-4072b099-b4c7-4c34-83d2-66da00345e89.png)  
PDF

# Features

"hoge"のセールスポイントや差別化などを説明する

# Requirement

**ページのリンク**：http://45.76.98.152/list/  
**言語**：Python 3.9.4  
**フレームワーク**：Django 3.1.7  
**開発期間**:3週間  
**開発環境**：MacOS  
**外部サーバー(OS)**：vultur(ubuntu)  
**DB**：外部サーバー上ではPostgreSQLを使用 

"hoge"を動かすのに必要なライブラリなどを列挙する

* huga 3.5.2
* hogehuga 1.0.2

# Installation

Requirementで列挙したライブラリなどのインストール方法を説明する

```bash
pip install huga_package
```

# Usage

DEMOの実行方法など、"hoge"の基本的な使い方を説明する

```bash
git clone https://github.com/hoge/~
cd examples
python demo.py
```

# Note

注意点などがあれば書く

# Author

作成情報を列挙する

* 作成者
* 所属
* E-mail

# License
ライセンスを明示する

"hoge" is under [MIT license](https://en.wikipedia.org/wiki/MIT_License).

社内向けなら社外秘であることを明示してる

"hoge" is Confidential.

