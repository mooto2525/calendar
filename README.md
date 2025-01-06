# calendar_data
[![test](https://github.com/mooto2525/ROS2_2/actions/workflows/test.yml/badge.svg)](https://github.com/mooto2525/ROS2_2/actions/workflows/test.yml)  
- これはROS2のパッケージです
- カレンダーのデータをトピックから出力する
## ノード概要
* calendar  
  * calコマンドを使用して2025年1月からのカレンダーのデータを一か月分ずつ1秒ごとにトピックにパブリッシュする  
* listener  
  * テスト用  
  * トピックからのメッセージをサブスクライブする  
## トピック概要  
* トピック名:`calendar`  
* メッセージの型:`String`  
## 実行方法  
- 実行方法1  
2つの端末で実行  
  - 端末1  
`ros2 run calendar_data calendar`  
  - 端末2  
`ros2 run calendar_data listener`  
- 実行方法2  
launchファイルを使用して1つの端末で実行  
`ros2 launch calendar_data talk_listen.launch.py`  
## 動作環境
### 必要なソフトウェア
* python  
### テスト環境
* ubuntu 22.04.2 LTS
  * ROS2 Humble
#### テストに使用したコンテナ  
上田教授の[コンテナ](https://hub.docker.com/repository/docker/ryuichiueda/ubuntu22.04-ros2)を使用させていただきました。
## ライセンス  
- このソフトウェアパッケージは、３条項BSDライセンスの下、再頒布及び使用が許可されます
- このパッケージのコードの一部は、下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを、本人の許可を得て自身の著作としたものです。
  - [ryuichiueda/slides_marp/robosys2024](https://github.com/ryuichiueda/slides_marp/tree/master/robosys2024)
- © 2024 Ryusei Fujimura
