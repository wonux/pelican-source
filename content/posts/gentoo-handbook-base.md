Title: Gentoo安装详解（一）-- 安装基本系统
Date: 2014-05-04 16:48
Modified: 2015-02-11 11:24
Category: Gentoo
Tags: gentoo, handbook,
Slug: gentoo-handbook-base
Authors: 孤逐王
Summary: 

[TOC]

## 前期准备

### 远程登录：

- 开启ssh服务：
```
/etc/init.d/sshd start
```

- 设置密码：
 ```
passwd
```

以便使用putty、ssh client远程登录上传stage等（有时在线下载很慢，而局域网上传很快）

### 准备磁盘：

- 分区：
```
fdisk /dev/sda
```
> /dev/sda1 : /boot 100M(32-100M)  设启动笔记-a
/dev/sda2 : / 20G
/dev/sda3 : /home 20G
 /dev/sda5 : /swap 1G (内存< 512 MB,分区分配2倍内存大小的空间;> 1024 MB，可以分配较少的空间甚至不需要swap 分区。)-t 82

- 创建文件系统：
```
mkfs.ext4 /dev/sda1
mkfs.ext4 /dev/sda2
mkfs.ext4 /dev/sda3
mkswap /dev/sda5
```

- 挂载分区：
```
mount /dev/sda2 /mnt/gentoo
mkdir /mnt/gentoo/boot
mount /dev/sda1 /mnt/gentoo/boot
mkdir /mnt/gentoo/home
mount /dev/sda3 /mnt/gentoo/home
swapon /dev/sda5
```

## 安装系统

### 安装stage及portage：

- 正确设置日期／时间：
```
date
```
> 如果显示的日期／时间不正确，可以使用date MMDDhhmmYYYY命令

- 下载Stage3 Tarbll：
```
cd /mnt/gentoo
links http://www.gentoo.org/main/en/mirrors.xml
```
选择国内速度较快的镜像，进入releases/x86/autobuilds/目录里。你将会看到所有适合你的计算机体系结构的stage文件（它们也可能放在各个独立的子体系名称的子目录里）。选择一个，然后按D来下载。下载完以后，再按Q退出浏览器。
> 或使用SSH Secure Shell登录上传stage3文件

- 解开Stage3 Tarball：
```
tar xvjpf stage3-*.tar.bz2
```

- 下载Portage：
打开links（或者lynx）然后到我们的Gentoo镜像列表。选择一个离你最近的镜像，打开snapshots/目录。然后选择最新的Portage快照（portage-latest.tar.bz2）并按D来下载它。
```
links http://www.gentoo.org/main/en/mirrors.xml
```
> 或使用SSH Secure Shell登录上传portage文件

- 解压Portage：
```
tar -xvjf /mnt/gentoo/portage-latest.tar.bz2 -C /mnt/gentoo/usr （install a Portage snapshot）
```

### 编译前准备：

- 配置编译选项：
```
nano -w /mnt/gentoo/etc/portage/make.conf
```
> CFLAGS="-march=native -O2 -pipe"  
CXXFLAGS="${CFLAGS}"  # 两个变量使用相同的设置
MAKEOPTS="-j3"  #MAKEOPTS定义在安装软件的时候同时可以产生并行编译的数目，CPU数目加一是个不错的选择

查看cpu信息：
```
cat proc/cpuinfo
```

- 选择镜像站点：
 ```
mirrorselect -i -o >> /mnt/gentoo/etc/portage/make.conf
mirrorselect -i -r -o >> /mnt/gentoo/etc/portage/make.conf
```
> **Warning:**[app-portage/mirrorselect]() has not been updated to handle modifying the target chrootsrepos.conf/gentoo.conf file yet. Also, the SYNC variable in make.conf is deprecated and no longer used by portage. This section needs to be updated, please skip for the time being...

- 拷贝DNS信息：
```
cp -L /etc/resolv.conf /mnt/gentoo/etc/
```

## Chroot进入新系统环境：

### Chroot：

- 挂载 /proc, /dev, /sys文件系统：
```
mount -t proc none /mnt/gentoo/proc
mount --rbind /dev /mnt/gentoo/dev
mount --rbind /sys /mnt/gentoo/sys
```

- 进入新的系统环境：
```
chroot /mnt/gentoo /bin/bash
source /etc/profile
export PS1="(chroot) $PS1"
```

### 新环境配置：

- 更新portage树：
```
emerge --sync （Updating the Portage tree）
或
emerge-webrsync（fetch the latest portage snapshot）
```

- 选择Profile：
```
eselect profile list
eselect profile set ×
```

- 设置时区：
```
ls /usr/share/zoneinfo
echo "Europe/Brussels" > /etc/timezone
emerge --config sys-libs/timezone-data
```

- 设置locale：
```
nano -w /etc/locale.gen
locale-gen
eselect locale list
eselect locale set x
```

- 更新环境变量：
```
env-update && source /etc/profile
```

