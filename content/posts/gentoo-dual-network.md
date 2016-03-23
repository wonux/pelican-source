Title: Gentoo双网卡同时启用上内外网
Date: 2015-06-16 07:30
Category: Gentoo
Tags: gentoo, network,
Slug: gentoo-dual-network
Authors: 孤逐王
Summary: 

[TOC]

>引言：本文配置网络通过 [OpenRC/netifrc]() 方法（net.*scritps）配置。

```
外网网卡：enp3s4
内网网卡：enp2s0
- 外网地址（通过路由器）
IP： 192.168.1.10
掩码： 255.255.255.0
网关： 192.168.1.1
- 内网地址
IP： 172.14.255.27
掩码： 255.255.0.0
网关： 172.14.0.1
```

1、分别设置网卡IP，默认网关设置外网网关。
编辑`/etc/conf.d/net`文件

```
config_enp3s4="192.168.1.10/24"
routes_enp3s4="default via 192.168.1.1"
config_enp2s0="172.14.255.27/16"
```
