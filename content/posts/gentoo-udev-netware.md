Title: Gentoo解决Udev升级的网卡重命名问题 
Date: 2014-06-30 10:40
Category: Gentoo
Tags: gentoo, bugs, network,
Slug: gentoo-udev-netware
Authors: 孤逐王
Summary: 

[TOC]

## 问题描述：

配置网络时，很多新手运行ifconfig命令查看网卡时，会发现我们熟悉的eth0网卡没有了，或是发现一些不规则命名的东东，不错，那就是你的网卡。

> 因为内核升级（忘记具体哪个版本了）从udev-197将自动分配更好的接口,网卡的命名改变了。

参考资料：[http://www.freedesktop.org/wiki/Software/systemd/PredictableNetworkInterfaceNames](http://www.freedesktop.org/wiki/Software/systemd/PredictableNetworkInterfaceNames)

从开机信息中可以看到提示：

```
dmesg |grep network
```

> [   74.261872] systemd-udevd[14259]: renamed network interface wlan0 to wlp2s0
[   74.391865] systemd-udevd[14259]: renamed network interface eth0 to enp0s4

## 解决方法：

- 使用老的命名方式（eth×）：
    
使用原来的网卡名字eth0,重置udev的rules：

> 方法一： 在kernel命令行选项里使用net.ifnames=0 ;
方法二：新建空文件文件/etc/udev/rules.d/80-net-name-slot.rules或注释掉里面内容

```
ln -s /dev/null /etc/udev/rules.d/80-net-name-slot.rules
或
touch /etc/udev/rules.d/80-net-name-slot.rules
```

- 使用新的网卡名字：

```
rm /etc/udev/rules.d/80-net-name-slot.rules
rm /etc/init.d/net.eth0 #删除不存在的引用
rc-update delete net.eth0 default #删除不存在的开机启动
cd /etc/init.d
ln -s net.lo net.enp0s3
rc-update add net.enp0s3 default #使用新名字
```
