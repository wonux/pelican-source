Title: Gentoo解决Windows双系统时间不同步的问题
Date: 2014-05-06 17:21
Modified: 2014-11-20 14:05
Category: Gentoo
Tags: gentoo, clock,
Slug: gentoo-handbook-clock
Authors: 孤逐王
Summary: 

[TOC]

> 升级后的gentoo不再使用/etc/conf.d/clock，而是使用/etc/conf.d/hwclock来设置和时间相关了。

- 在/etc/conf.d/hwclock文件中设置系统时间为本地时间而不是UTC时间:

```   
clock="local"     #default: UTC
```

- 然后用date命令设置正确的系统时间，格式如下：

```
date [MMDDhhmm[YY][.ss］
```

其他的不用解释了，其中的YY表示年份的前２位数。

- 然后再把系统时间同步到硬件时间就可以了：

```
 hwclock --systohc
```

> 使用hwclock命令也可以把硬件时间同步到系统时间：

```
 hwclock --hctosys
```

显示硬件时间则是：

```
hwclock --show
```
