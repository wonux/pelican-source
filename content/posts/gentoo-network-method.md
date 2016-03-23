Title: Gentoo网络管理方法总结
Date: 2015-06-15 15:30
Category: Gentoo
Tags: gentoo, network,
Slug: gentoo-network-method
Authors: 孤逐王
Summary: 

[TOC]

### OpenRC/netifrc

Netifrc is a collection of modules created to configure and manage network interfaces via individual, per-interface scripts located in the /etc/init.d/ directory.
Enable Gentoo's network stack ([net.* scripts](https://wiki.gentoo.org/wiki/Netifrc)).

#### 检测网卡名字

```
ifconfig -a
or
ls /sys/class/net
```

#### 添加网卡

通过`net.lo`链接

```
ln -s /etc/init.d/net.lo /etc/init.d/net.ifname
/etc/init.d/net.ifname start
rc-update add net.ifname default
```

#### 配置网络IP

编辑`/etc/conf.d/net`文件
```
config_ifname="192.168.1.10/24"    #ip、掩码
routes_ifname="default via 192.168.1.1"    #网关
```

#### 添加DNS

编辑`/etc/resolv.conf文件
```
nameserver 202.99.166.4
nameserver 202.99.160.68
```

###  Newnet
enable the [new network]() stack (experimental)

### DHCPCD

**D**ynamic **H**ost **C**onfiguration **P**rotocol **C**lient **D**aemon (**[DHCPCD]()**) is a popular DHCP client for Gentoo Linux users.
使用dhcpcd自动获取IP，需要将net.*scripts标本停用，并设置`/etc/conf.d/net`中`config_ifname="dhcp"`或留空。

#### dhcpcd-ui
[https://wiki.gentoo.org/wiki/Dhcpcd-ui#Usage](https://wiki.gentoo.org/wiki/Dhcpcd-ui#Usage)
- dhcpcd-gtk

### NetworkManager

**NetworkManager** is a [network management software](https://wiki.gentoo.org/wiki/Network_management) for Ethernet, Wifi, DSL, dialup, VPN, [WiMAX](https://wiki.gentoo.org/wiki/WiMAX) and mobile broadband network connections.
It's a good idea to use dhclient from [net-misc/dhcp]() instead of [net-misc/dhcpcd]().

#### NetworkManager GUI
- GTK:
 [gnome-extra/nm-applet]()
- KDE Frontend:
[kde-misc/plasma-nm]()
[kde-misc/networkmanagement]()

参考：
[Network management ](https://wiki.gentoo.org/wiki/Network_management)
[Network_management_using_DHCPCD/OpenRC_message](https://wiki.gentoo.org/wiki/Network_management_using_DHCPCD/OpenRC_message)
[Netifrc ](https://wiki.gentoo.org/wiki/Netifrc)
[Network management using DHCPCD ](https://wiki.gentoo.org/wiki/Network_management_using_DHCPCD)
[NetworkManager](https://wiki.gentoo.org/wiki/NetworkManager)
