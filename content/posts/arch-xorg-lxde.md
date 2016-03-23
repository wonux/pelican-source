Title: ArchLinux最小化安装LXDE桌面环境
Date: 2014-06-10 15:00
Modified: 2015-01-04 14:02
Category: Arch
Tags: arch, xorg, lxde,
Slug: arch-xorg-lxde
Authors: 孤逐王
Summary:

[TOC]

### 安装最小化的LXDE桌面环境：

```
pacman -S lxde-common
```

### 安装LXDE Session：

```
pacman -S lxsession

```

> 不安装这个没法登录进桌面环境

### 安装LXDE面板：

```
pacman -S lxpanel
```

> 不安装这个，进入LXDE桌面环境后什么都没有

### 安装窗口管理器:

```
pacman -S openbox
```

> 不安装这个，既不能移动窗口，也不能最大、最小化窗口

### 安装LXDE环境下的终端程序:

```
pacman -S lxterminal
```

### 安装LXDE环境下的文件管理器:

```
pacman -S pcmanfm
```

### 总结

根据自己需要取舍上述组件，现在我仅仅使用`openbox`，DIY配合其他工具，超精简流畅。