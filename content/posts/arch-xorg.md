Title: Arch最小化安装X
Date: 2014-06-10 14:42
Modified: 2015-01-04 13:56
Category: Arch
Tags: arch, xorg,
Slug: arch-xorg
Authors: 孤逐王
Summary:

[TOC]

## Xorg

### xorg-server

- 安装xorg-server

```
pacman -S xorg-server
```

- 可选：xorg-server-utils

```
pacman -S xorg-server-utils
```

>  Xorg-server-utils meta-package pulls in the most useful packages for certain configuration tasks, they are pointed out in the relevant sections.

### Driver installation

如果不知道显卡类型，请执行如下命令进行查询：

```
lspci | grep VGA
```

输入下面命令，查看所有开源驱动:

```
pacman -Ss xf86-video | less
```

安装显卡驱动:

- vesa：

```
pacman -S xf86-video-vesa
```

> vesa是一个支持大部分显卡的通用驱动，不提供任何 2D 和 3D 加速功能。
要充分发挥显卡性能，请按下表安装驱动程序。推荐先使用开源驱动，这些驱动出问题的可能性较小。

- AMD/ATI :

```
pacman -S xf86-video-ati
```

- Intel:

```
pacman -S xf86-video-intel
```

- Nvidia:

```
pacman -S xf86-video-nouveau     
```

### Running

- Display manager:
最简单的方法是使用登录管理器 例如 GDM, KDM or SLiM.

- Manually：
如果不用登陆管理器启动 X，需要安装软件包 xorg-xinit。

```
pacman -S xorg-xinit
pacman -S xorg-twm xorg-xclock xterm
```

> startx 和 xinit 命令将启动 X 服务器和客户端(startx 脚本是更通用命令 xinit 的前端)。为了确定要运行的客户端，startx/xinit 先在用户目录解析 ~/.xinitrc 文件，如果 ~/.xinitrc 不存在，使用默认的 /etc/X11/xinit/xinitrc, 其中默认会使用 Twm 窗口管理器，Xclock 和 Xterm（需安装 xorg-twm, xorg-xclock 和 xterm）.

- To launch the X server and clients:

```
startx
```