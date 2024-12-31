# calendarコマンド
[![test](https://github.com/mooto2525/ROS2_2/actions/workflows/test.yml/badge.svg)](https://github.com/mooto2525/ROS2_2/actions/workflows/test.yml)
このコードは/calendarというトピックに２０２５年1月からのカレンダーのデータを一か月分ずつ放出し、同時に流れるメッセージを確認するものになります。  

##使用準備
* 以下のコマンドを順にターミナルで実行
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
* 以下のコマンドをターミナル上で実行
```
ros2 run mypkg calendar
```



