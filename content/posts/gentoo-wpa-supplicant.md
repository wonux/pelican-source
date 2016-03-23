Title: Gentoo无线网络配置 -- wpa_supplicant
Date: 2015-01-04 15:06
Modified: 2015-02-10 13:39
Category: Gentoo
Tags: gentoo, network, wireless, wpa2,
Slug: gentoo-wpa-supplicant
Authors: 孤逐王
Summary: 

[TOC]

### 安装

安装`net-wireless/wpa_supplicant`包

```
emerge --ask wpa_supplicant
```

### 启动网络

- 为wpa_supplicant添加无线接口
在`wpa_supplicant.conf`文件中添加

```
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=wheel
```

- 初始化wpa_supplicant环境

```
wpa_supplicant -d -Dnl80211 -iwlan0 -c /etc/wpa_supplicant/wpa_supplicant.conf
```

参数：

```
-B - Fork into background.
-c filename - Path to configuration file.
-d increase debugging verbosity
-i interface - Interface to listen on.
-D driver - Optionally specify the driver to be used.
```

For a list of supported drivers see the output of `wpa_supplicant -h`.

> ` nl80211` is the current standard, but not all wireless chip's modules support it.`wext` is currently deprecated, but still widely supported.

- 查看wpa_supplicant进程

```
ps -aux | grep wpa
root      1841  0.0  0.2   6168  2920 ?        Ss   09:10   0:00 wpa_supplicant -B -c/etc/wpa_supplicant/wpa_supplicant.conf -iwlan0
root      2122  0.0  0.0   2780   728 pts/0    S+   09:25   0:00 grep --colour=auto wpa
```

### 配置

- Set for Gentoo net.* scrips，tell the network script to use wpa_supplicant.
`File/etc/conf.d/net`

```
modules_wlan0="wpa_supplicant"
# 因为wpa_supplicant还不能很好的自动侦测驱动，所以需要我们为其指定正在使用的驱动。
wpa_supplicant_wlan0="-Dnl80211"
config_wlan0="dhcp"
```

- Set for dhcpcd,no special setup is needed.Do not add wpa_supplicant to any runlevel. It will be controlled by dhcpcd.

配置文件`/etc/wpa_supplicant/wpa_supplicant.conf`

```
# Allow users in the 'wheel' group to control wpa_supplicant
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=wheel
# Make this file writable for wpa_gui
update_config=1
#自动扫描AP（也就是可以上的无线网络热点）
ap_scan=1   
# 简单的情形：WPA-PSk密码验证方式，PSK是ASCII密码短语，所有合法的加密方式都允许连接
network={
  ssid="simple"
  psk="very secret passphrase"
  # 优先级越高，就能越早匹配到。
  priority=5
}
```

> To allow unprivileged users to control the connection using wpa_gui / wpa_cli, make sure `GROUP=wheel` and `update_config=1`.

#### 也可以使用`wpa_passphrase `命令添加无线热点

```
wpa_passphrase [ ssid ] [ passphrase ] >> /etc/wpa_supplicant/wpa_supplicant.conf
```

上面这条命令可以自动生成一段配置，我们将它输出添加到 wpa_supplicant 的默认配置文件里面。

#### wpa_cli

运行wpa_cli时可能会出现如下的错误：
`Could not connect to wpa_supplicant - re-trying`
这个错误可能是因为你的wpa_supplicant进程没有启动起来造成的。

```
wpa_cli
> scan
> scan_results
> add_network
0
> set_network 0 ssid "MYSSID"
> set_network 0 psk "passphrase"
> enable_network 0
> save_config
OK
dhcpcd interface
```

### 设置、获取IP

自动获取
```
dhcpcd wlan0
```
手动设置
```
ifconfig wlan0 192.168.1.11 broadcast 192.168.1.255 netmask 255.255.255.0
```

### 告知Gentoo RC系统网卡名字

```
cd /etc/init.d
ln -s net.lo net.wlan0
#start and stop it using the following commands:
/etc/init.d/net.eth0 start
/etc/init.d/net.eth0 stop
#开机启动
rc-update add wlan0 default
```