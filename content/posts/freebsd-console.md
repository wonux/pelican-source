Title: UNIX基础 -- 控制台和终端
Date: 2015-04-21 17:18
Modified: 2015-04-21 20:31
Category: FreeBSD
Tags: unix, console, tty, freebsd,
Slug: freebsd-console
Authors: 孤逐王
Summary:

[TOC]

## 虚拟控制台和终端
Virtual Consoles and Terminals:

FreeBSD 虚拟控制台的默认配置为8个，但并不是硬性设置， 您可以很容易设置虚拟控制台的个数增多或减少。 虚拟控制台的的编号和设置在 `/etc/ttys `文件里。

```
# name    getty                         type  status comments
#
ttyv0   "/usr/libexec/getty Pc"         xterm   on  secure
# Virtual terminals
ttyv1   "/usr/libexec/getty Pc"         xterm   on  secure
ttyv2   "/usr/libexec/getty Pc"         xterm   on  secure
ttyv3   "/usr/libexec/getty Pc"         xterm   on  secure
ttyv4   "/usr/libexec/getty Pc"         xterm   on  secure
ttyv5   "/usr/libexec/getty Pc"         xterm   on  secure
ttyv6   "/usr/libexec/getty Pc"         xterm   on  secure
ttyv7   "/usr/libexec/getty Pc"         xterm   on  secure
ttyv8   "/usr/X11R6/bin/xdm -nodaemon"  xterm   off secure
```

FreeBSD 默认系统控制台是system console（ttyv0）,8个虚拟控制台virtual consoles (ttyv1 ~ ttyv8),(ttyv8)用于进入桌面环境。

> FreeBSD使用 Alt+F1 ~  Alt+F9键，切换多个虚拟控制台。从图形界面切换至其他虚拟控制台要使用Ctrl+Alt。

### 单用户模式
Single User Mode

单用户模式主要用于修复系统启动失败，或者重新设置root密码。在单用户模式中，网络和虚拟控制台不能使用，但是可以提供完整的root权限，而不需要root密码。

单用户模式的控制台也可以在`/etc/ttys`文件中的设置。

```
# name  getty                           type  status  comments
#
# If console is marked "insecure", then init will ask for the root password
# when going to single-user mode.
console none                            unknown  off  secure
```

>  可编辑把 secure 改为 insecure。 这样， 当用单用户进入 FreeBSD 时， 它仍然要求提供 root 用户的密码。

### 改变控制台的显示模式
Changing Console Video Modes

FreeBSD 控制台默认的显示模式可以被调整为 1024x768， 1280x1024， 或者任何你的显卡芯片和显示器所支持的其他尺寸。 要使用一个不同的显示模式，加载vesa模块：
```
kldload vesa
```

使用`vidcontrol`工具来检测硬件支持的显示模式。
```
vidcontrol -i mode
```

这个命令的输出是一份你的硬件所支持的显示模式列表。使用`vidcontrol`命令来改变显示模式：
```
vidcontrol MODE_279
```

如果对于新的显示模式满意，那么可以把它加入到` /etc/rc.conf `使机器在每次启动的时候都能生效.
> allscreens_flags="MODE_279"

