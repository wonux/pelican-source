Title: Arch安装fcitx
Date: 2014-10-11 13:04
Modified: 2015-12-11 16:03
Category: Arch
Tags: arch, fcitx
Slug: arch-fcitx
Authors: 孤逐王
Summary:

[TOC]

### 安装fcitx,安装gtk、qt模块。

```
[root@Arctux ~]# pacman -S fcitx-im
:: There are 4 members in group fcitx-im:
:: Repository community
   1) fcitx  2) fcitx-gtk2  3) fcitx-gtk3  4) fcitx-qt4
Enter a selection (default=all):
```

### 安装fcitx配置工具

```
[root@ARCH ~]# pacman -S fcitx-configtool
```

### `.xinitrc`文件添加gtk、qt支持

```
export GTK_IM_MODULE=fcitx
export QT_IM_MODULE=fcitx
export XMODIFIERS=@im=fcitx
```