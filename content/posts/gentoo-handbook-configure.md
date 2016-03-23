Title: Gentoo安装详解（三）-- 配置系统
Date: 2014-05-04 17:40
Modified: 2015-05-08 11:54
Category: Gentoo
Tags: gentoo, handbook, 
Slug: gentoo-handbook-configure
Authors: 孤逐王
Summary: 

[TOC]

## 配置系统

### 系统信息：

- 文件系统信息：

创建/etc/fstab

```
nano -w /etc/fstab
```

- 网络信息：

Host name, Domainname, etc

```
nano -w /etc/conf.d/hostname
```

Configuring Network

```
nano -w /etc/conf.d/net
```

- 系统信息：

Gentoo uses /etc/rc.conf to configure the services, startup, and shutdown of your system.

```
nano -w /etc/rc.conf
```

Root Password

```
passwd
```

Gentoo uses /etc/conf.d/hwclock to set clock options.

```
nano -w /etc/conf.d/hwclock
```

### 安装系统工具软件：

- 可选：PCMCIA使用lspci查看硬件信息：

```
emerge pcmciautils
```

- System Logger：

```
emerge syslog-ng
rc-update add syslog-ng default
```

- 可选：File Indexing：

```
emerge mlocate
```

- 可选：Remote Access：

```
rc-update add sshd default
```

- 可选：DHCP Client：

```
emerge dhcpcd
```

### 配置启动项：

- Using GRUB2：

```
emerge sys-boot/grub
grub2-install /dev/sda
```

> Optionally, install theos-prober utility (provided through the [sys-boot/os-prober]() package) to have GRUB2 probe for other operating systems when running thegrub2-mkconfig command. In most instances, this will enable GRUB2 to automatically detect other operating systems (Windows 7, Windows 8.1, etc.).

Generating GRUB2 configuration：

```
grub2-mkconfig -o /boot/grub/grub.cfg
```

- 可选：Using GRUB Legacy：

```
emerge sys-boot/grub:0
```

编辑配置文件：

```
nano -w /boot/grub/grub.conf
```

Example grub.conf：

```
# 默认选择哪个列表来引导。0表示第一个， 1表示第二个，以此类推。
default 0
# 引导默认列表前等待多少秒
timeout 30
# 使用漂亮、“臃肿”的spalsh图像来增加一点趣味:)
# 如果您没有安装显卡，请将这行注释掉
splashimage=(hd0,0)/boot/grub/splash.xpm.gz

title Gentoo Linux 3.10.10
# 内核镜像（或者操作系统）所在分区
root (hd0,0)
kernel /boot/kernel-3.10.10-gentoo root=/dev/sda2

title Gentoo Linux 3.10.10 (rescue)
# 内核镜像（或者操作系统）所在分区
root (hd0,0)
kernel /boot/kernel-3.10.10-gentoo root=/dev/sda2 init=/bin/bb

# 接下来的四行只有在您与Windows系统进行双启动的情况下才需要。
# 本例中，windows系统位于/dev/sda6。
title Windows XP
rootnoverify (hd0,5)
makeactive
chainloader +1

#win7下注释掉makeactive
```

Setting up GRUB Legacy using grub-install:
Creating /etc/mtab:

```
grep -v rootfs /proc/mounts > /etc/mtab
```

Install GRUB Legacy:

```
grub-install --no-floppy /dev/sda
```

### 重启系统:

```
exit
cd
umount -l /mnt/gentoo/dev{/shm,/pts,}
umount -l /mnt/gentoo{/boot,/proc,}
reboot
```
