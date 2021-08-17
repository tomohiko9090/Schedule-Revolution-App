# 制作物名：「社会人1年目のスケジュール最適化アプリ」  

## 詳細
**ページのリンク**：http://45.76.98.152/list/  
**言語**：Python 3.9.4  
**フレームワーク**：Django 3.1.7  
**開発期間**:3週間  
**開発環境**：MacOS  
**外部サーバー(OS)**：vultur(ubuntu)  
**DB**：外部サーバー上ではPostgreSQLを使用  


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

"hoge"の魅力が直感的に伝えわるデモ動画や図解を載せる

# Features

"hoge"のセールスポイントや差別化などを説明する

# Requirement

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

