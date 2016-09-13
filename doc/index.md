# remotejoystick

![version][py27] [English Version][english-version]

将远程手柄连接到本地电脑上。

这样一些没有联网版本的游戏也可以通过屏幕共享实现多人联网。

目前的效果为本地电脑将远程手柄视为键盘，使用正常的主机延时一般在100ms。

当然，同样的顺手就提供了本地手柄转为键盘的功能。

## Install

通过如下命令可以安装本项目：

```bash
pip install remotejoystick
```

## Usage

该程序提供两个基础的功能，本地手柄转键盘与远程手柄连接。

详细的帮助可以使用该命令：`remotejoystick -h`

### 远程手柄连接

首先，你需要有一个可以访问的公网ip，假设该ip为`114.114.114.114`。

在该ip对应的主机上安装好该项目（平台不限），在命令行中运行：`remotejoystick -ep 2333`。

即可将2333端口用于该项目。

之后，在手柄所在主机使用该命令：`remotejoystick -sd 114.114.114.114 -p 2333`。（多个手柄可以使用-j指定）

最后，在游戏所在主机使用该命令：`remotejoystick -rd 114.114.114.114 -p 2333`。（这两个命令不分先后）

### 本地手柄转键盘

使用该命令可以在本地将手柄转为键盘：`remotejoystick --local`

## Future features
* 可视化界面
* 本地也模拟为手柄信号（**需要帮助，如果你有想法请务必联系我**）

## Author

软件作者：[LittleCoder][author]

联系方式：i7meavnktqegm1b@qq.com

意见收集：[Issue #1][issue#1]

[py27]: https://img.shields.io/badge/python-2.7-ff69b4.svg
[author]: https://github.com/littlecodersh
[english-version]: https://github.com/littlecodersh/remotejoystick/blob/master/README_EN.md
[issue#1]: https://github.com/littlecodersh/remotejoystick/issues/1
