# iterm2配置lzrz

- 作者：codehackfox@gmail.com
- 时间：2019-03-09 12:11:30

>## 0x00、安装lzrz

- 1.远程连接的服务器端必须要有sz、rz这两个工具，如果没有，可以执行安装。如在CentOS上安装的命令为：
```
sudo yum install lrzsz
```
- 2.本地安装lzrz工具。

```
brew install lrzsz
```

>## 0x01、本地下载脚本

- 1.由于sz,rz是基于ZMODEM/YMODEM/XMODEM协议的，所以安装iterm2-zmodem
```
cd /usr/local/bin
sudo wget https://raw.github.com/mmastrac/iterm2-zmodem/master/iterm2-send-zmodem.sh
sudo wget https://raw.github.com/mmastrac/iterm2-zmodem/master/iterm2-recv-zmodem.sh
sudo chmod 777 /usr/local/bin/iterm2-*
```

>## 0x02、配置iterm2

- 1.打开Item2，点击preferences → profiles，选择某个profile，如Default，之后继续选择advanced → triggers，添加编辑添加如下triggers：
(Profiles -> Open Profiles -> Edit Profies -> Advanced -> Triggers -> Edit )
- 2.rz配置
```
Regular Expression: \*\*B0100
Action: Run Silent Coprocess
Parameters: /usr/local/bin/iterm2-send-zmodem.sh
```
- 3.sz配置
```
Regular Expression: \*\*B00000000000000
Action: Run Silent Coprocess
Parameters: /usr/local/bin/iterm2-recv-zmodem.sh
```

>## 0x03、配置完毕，进行尝试。