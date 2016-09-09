remote-joystick
===============

|py2| `Chinese Version <chinese_version_>`_

**目前该程序还在开发阶段。**

将远程手柄连接到本地电脑上。

这样一些没有联网版本的游戏也可以通过屏幕共享实现多人联网。

**Current process**

通过将手柄信号读取并传送，在本地转化为键盘消息。

在有公网的服务器运行`server.py`，并将config中的ip改为公网服务器的ip。

在手柄端运行`sender.py`，在接收端运行`receiver.py`即可。（先后无所谓）

如果要开启多个receiver，需要多个命令行窗口。

**Future features**

* 可视化界面
* 一个receiver接收多个sender
* 本地也模拟为手柄信号（**需要帮助，如果你有想法请务必联系我**）

.. |py2| image:: https://img.shields.io/badge/python-2.7-ff69b4.svg
.. |py3| image:: https://img.shields.io/badge/python-3.5-red.svg
.. _chinese_version: https://github.com/littlecodersh/RemoteJoystick/blob/master/README.md
.. _document: https://danmu.readthedocs.org/zh/latest/
.. _issue#1: https://github.com/littlecodersh/RemoteJoystick/issues/1
.. |gitter| image:: https://badges.gitter.im/littlecodersh/danmu.svg
.. _gitter: https://gitter.im/littlecodersh/danmu?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge
