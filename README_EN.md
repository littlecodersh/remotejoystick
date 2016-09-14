# remotejoystick

![py27][py27] ![py35][py35] [中文版][chinese-version]

Remote joysticks can be connected to local computers now.

So some interesting games without online version can be played through screen sharing.

This version turns remote joysticks into local keyboard. With a ordinary server, delay is about 100ms.

Also, this program provide local joystick to keyboard function.

## Install

You may install this program through the following script:

```bash
pip install remotejoystick
```

## Usage

This program provides two basic functions: local j2k & remote joystick connection.

More detailed help info is also available: `remotejoystick -h`

### remote joystick connection

First, you need to have an touchable public net ip, assume it is `114.114.114.114`.

Install this program on the server of the ip (three platfroms supported), and run this cmd: `remotejoystick -ep 2333`.

This will use 2333 port for this program.

Then run this cmd on the joystick pc: `remotejoystick -sd 114.114.114.114 -p 2333`. (-j option is for more than one joystick)

Finally, use this cmd on game pc: `remotejoystick -rd 114.114.114.114 -p 2333`. (order of the last two cmd does not matter)

### local joystick to keyboard

Use this cmd to turn joystick to keyboard locally: `remotejoystick --local`.

## Future features
* Visual version
* Simulate as joystick signal locally (**help wanted! If you have any idea please contact me.**)

## Author

Author: [LittleCoder][author]

Email: i7meavnktqegm1b@qq.com

Suggestion: [Issue #1][issue#1]

[py27]: https://img.shields.io/badge/python-2.7-ff69b4.svg "python27"
[py35]: https://img.shields.io/badge/python-3.5-red.svg "python35"
[author]: https://github.com/littlecodersh
[chinese-version]: https://github.com/littlecodersh/remotejoystick/blob/master/README.md
[issue#1]: https://github.com/littlecodersh/remotejoystick/issues/1
