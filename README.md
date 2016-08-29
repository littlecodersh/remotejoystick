# RemoteJoystick

![version][py27]

**目前该程序还在开发阶段。**

将远程手柄连接到本地电脑上。

这样一些没有联网版本的游戏也可以通过屏幕共享实现多人联网。

## Current process

通过将手柄信号读取并传送，在本地转化为键盘消息。

在有公网的服务器运行`server.py`，并将config中的ip改为公网服务器的ip。

在手柄端运行`sender.py`，在接收端运行`receiver.py`即可。（先后无所谓）

如果要开启多个receiver，需要多个命令行窗口。

## Future features
* 可视化界面
* 一个receiver接收多个sender
* 本地也模拟为手柄信号（**需要帮助，如果你有想法请务必联系我**）

## Author

软件作者：[LittleCoder](https://github.com/littlecodersh/)

联系方式：i7meavnktqegm1b@qq.com

[py27]: https://img.shields.io/badge/python-2.7-ff69b4.svg
