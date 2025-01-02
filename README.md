# calendar
[![test](https://github.com/mooto2525/ROS2_2/actions/workflows/test.yml/badge.svg)](https://github.com/mooto2525/ROS2_2/actions/workflows/test.yml)
calendarというノードがcalendarというトピックを通じて２０２５年1月からのカレンダーのデータを一か月分ずつ放出し、同時に流れるメッセージを確認するものになります。  

## このリポジトリで使用可能なノード
* calendar  
## 使用準備
以下のコマンドを順にターミナルで実行  
Gitをインストール(Gitをインストールしていない方のみ)  
```sudo apt-get install git```  
リポジトリをクローン  
```git clone https://github.com/mooto2525/ROS2_2.git```  
リポジトリを移動  
```cd mypkg```  
移動できたか確認  
```ls```  
```__init__.py  calendar.py```  
と表示されたらOK  
## 使用方法
以下のコマンドをターミナル上で実行  
```
ros2 run mypkg calendar
```  
実行結果  
```
[INFO] [1735656940.436907959] [calender_talker]: Receive calemdar data:
    January 2025
Su Mo Tu We Th Fr Sa
          1  2  3  4
 5  6  7  8  9 10 11
12 13 14 15 16 17 18
19 20 21 22 23 24 25
26 27 28 29 30 31


[INFO] [1735656941.404341464] [calender_talker]: Receive calemdar data:
   February 2025
Su Mo Tu We Th Fr Sa
                   1
 2  3  4  5  6  7  8
 9 10 11 12 13 14 15
16 17 18 19 20 21 22
23 24 25 26 27 28
```
## テスト専用ディレクトリ
* launch  
* test  
## 動作環境
### 必要なソフトウェア
* python
  * テスト済み：3.7~3.11
###テスト環境
* ubuntu 22.04.2 LTS
  * ROS2 Humble

### テストに使用したコンテナ  
上田准教授の[コンテナ](https://hub.docker.com/repository/docker/ryuichiueda/ubuntu22.04-ros2)を使用させていただきました。

## ライセンス
  
- このソフトウェアパッケージは、３条項BSDライセンスの下、再頒布及び使用が許可されます
- このパッケージのコードの一部は、下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを、本人の許可を得て自身の著作としたものです。
  - [ryuichiueda/slides_marp/robosys2024](https://github.com/ryuichiueda/slides_marp/tree/master/robosys2024)
- © 2024 Ryusei Fujimura
