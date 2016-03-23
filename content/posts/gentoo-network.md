Title: Gentoo网络配置
Date: 2014-11-20 10:07
Category: Gentoo
Tags: gentoo, network,
Slug: gentoo-network
Authors: 孤逐王
Summary: 

[TOC]

## 网卡识别配置

要开始配置你的网卡，你首先需要告诉Gentoo RC系统你的网卡。
可以用ifconfig命令查看自己网卡名字：

```
ifconfig -a
```
> 网卡名字（如eth0）的识别是通过在/etc/init.d目录里建立一个指向net.lo的符号链接来实现。

```
cd /etc/init.d
ln -s net.lo net.eth0
```

## 启动和停止网络脚本

```
/etc/init.d/net.eth0 start
/etc/init.d/net.eth0 stop
rc-update add net.eth0 default  #设置开机启动eth0
```

## 网络配置

### 命令方式（临时配置，重启后失效）：

设置网络包括了三个步骤：

- 使用ifconfig配置ip地址：

```
ifconfig eth0 192.168.1.10 broadcast 192.168.1.255 netmask 255.255.255.0 up
```

- 使用route来设定路由的网关：

```
route add default gw 192.168.1.1
```

- 创建/etc/resolv.conf配置DNS：

```
nano -w /etc/resolv.conf
```

> nameserver $202.99.166.4
nameserver $202.99.160.68

### 配置文件方式：

编辑网络配置文件/etc/conf.d/net和/etc/resolv.conf。

- 编辑/etc/conf.d/net配置主机IP地址、子网掩码和网关:

```
nano -w /etc/conf.d/net
```    

> 使用CIDR形式表示的静态IP：

```     
config_eth0="192.168.1.7/24"
routes_eth0="default via 192.168.1.1"
```

> 使用netmask形式表示的静态IP

```
config_eth0="192.168.1.7 broadcast 192.168.1.255 netmask 255.255.255.0"
routes_eth0="default via 192.168.1.1"
```

注意: 如果你没有指定，DHCP是默认选项。

### 测试：

- 测试是否能ping的通网关：

```
ping 192.168.1.1
```
如果能ping通，ip设置没错误。

- 测试DNS：
 
编辑/etc/resolv.conf配置DNS：

```
nano /etc/resolv.conf
```

在其中加入以下两行内容：

```
nameserver 202.99.160.68
nameserver 202.99.166.4
```

测试DNS解析是否正常：

```
ping www.baidu.com
```
如果能ping通，DNS设置无误。
