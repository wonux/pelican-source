Title: Gentoo本地化设置--时区、时钟、字体、中文环境
Date: 2014-06-30 11:21
Modified: 2015-01-05 16:05
Category: Gentoo
Tags: gentoo, locale,
Slug: gentoo-localization
Authors: 孤逐王
Summary: 

[TOC]

## 时区

你需要选择时区让系统知道你的地理位置，以保持正确的时间。在/usr/share/zoneinfo中查找你的时区。然后在/etc/conf.d/clock中设置时区。请忽略/usr/share/zoneinfo/Etc/GMT*时区，因为它们的名字并不表示所指的地区。比如，GMT-8实际上是GMT+8。
设置时区信息：

```
ls /usr/share/zoneinfo
echo "Asia/Shanghai" > /etc/timezone
emerge --config sys-libs/timezone-data
```

> 注意: 你可以做一个用户级的设置，在shell的rc文件（如bash的.bash_profile）中将TZ变量的值设为/usr/share/zoneinfo下的任何东西。本案例中TZ="Asia/Shanghai"。

## 硬件时钟

Gentoo Linux安装过程中，大多数情况下硬件时钟都是被设成UTC（或GMT，格林威治标准时间），而时区则定为实际的本地时间。如果出于某种原因，你需要将硬件时钟设为非UTC，那么你就要编辑/etc/conf.d/hwclock，将CLOCK的值由UTC改为local。

```
CLOCK="UTC"
或
CLOCK="local"
```

## 安装中文字体

推荐开源文泉驿自由字体

```
emerge wqy-zenhei （文泉驿正黑）
emerge wqy-microhei （文泉驿微米黑）
```

## 生成指定的Locale

可能你在系统中只要用到一个或者两个locale。你可以在/etc/locale.gen中指定所需的的locale。
中文有很多种编码，最流行的就是UTF8和GBK。我们推荐客户使用UTF8编码，因为这是国际标准，能兼容任何语言的编码。

添加locale到`/etc/locale.gen`

```
nano -w /etc/locale.gen
```

> en_US ISO-8859-1
en_US.UTF-8 UTF-8
zh_CB.UTF-8 UTF-8

下一步是执行`locale-gen`。它会生成/etc/locale.gen文件中指定的所有locale。

```
locale-gen
```

你可以通过执行locale -a来检验所选的locale是否可用。

```
locale -a
```

## 设置一个Locale显示中文

- 在`/etc/env.d/02locale`中设置全局默认的系统locale

> LANG="zh_CN.UTF-8"
LC_COLLATE="C"

- 在~/.bashrc中设置用户级的系统locale

> export LANG="zh_CN.UTF-8"
export LC_COLLATE="C"

- 更新系统全局默认的locale：

设置好正确的locale后，一定要更新环境变量使系统知道所做的更改：

```
env-update && source /etc/profile
```

- 更新特定用户的locale：

```
source ~/.bashrc
```

更新环境后，你需要按下Ctrl-Alt-Backspace杀死X服务器，登出，然后以用户身份登入。
现在，检验一下所做的更改是否已经生效了：

```
locale
```

> 注：*另一种系统配置方式是保留默认的C locale，同时要能够表现UTF-8字符。
这种选择可以通过使用下述设置来实现：LC_CTYPE=zh_CN.UTF-8*
