Title: ArchLinux安装详解
Date: 2014-10-10 13:18
Modified: 2014-12-26 16:01
Category: Arch
Tags: arch, handbook
Slug: arch-handbook
Authors: 孤逐王
Summary:

[TOC]

## 选择安装方式

### CD/USB Arch启动盘安装

使用Arch启动盘比较简单方便，没有额外设置，直接阅读下一步。
USB flash installation media

>启动盘制作： [USB flash installation media](https://wiki.archlinux.org/index.php/USB_flash_installation_media)

### 从已经存在的Linux系统中安装（非Arch类）

从已经存在的非Arch系统环境中安装arch，本质上是搭建引导过程中可以运行` arch-install-scripts` 脚本(包括`pacstrap`和`arch-chroot`命令) 的系统环境。

#### 创建Arch chroot环境
1、推荐使用`bootstrap`镜像

```
### Download the bootstrap image from a mirror：
 [root@GENTOO ~] curl -O http://mirrors.kernel.org/archlinux/iso/2015.10.01/archlinux-bootstrap-2015.10.01-x86_64.tar.gz
### Extract the tarball:
 [root@GENTOO ~] cd /tmp# tar xzf <path-to-bootstrap-image>/archlinux-bootstrap-2015.10.01-x86_64.tar.gz
```

2、编辑`/tmp/root.x86_64/etc/pacman.d/mirrorlist`本件，选择镜像源
3、进入chroot环境

```
/tmp/root.x86_64/bin/arch-chroot /tmp/root.x86_64/
```

#### 使用Arch chroot环境
1、初始化pacman keyring

```
# pacman-key --init
# pacman-key --populate archlinux
```

2、编辑`/etc/pacman.d/mirrorlist`本件，选择镜像源
3、更新软件列表

```
# pacman -Syyu
```

4、安装系统
Arch Chroot环境已经具备，继续下面的步骤，选择安装需要的系统`base`, `base-devel`, `parted`等.

> 参考：[https://wiki.archlinux.org/index.php/Install_from_existing_Linux](https://wiki.archlinux.org/index.php/Install_from_existing_Linux)

## 准备

### 准备磁盘分区

- 新建并格式化分区

至少准备一个足够大的/分区，如果磁盘容量足够，可以额外创建/home、/boot等。

- 创建挂载目录

```       
mkdir /mnt
mkdir /mnt/boot
mkdir /mnt/home
```

- 挂载根分区和swap

> Mount the root partition on /mnt. After that, create directories for and mount any other partitions (/mnt/boot, /mnt/home, ...) and activate your swap partition if you want them to be detected later by genfstab.

```
mount /dev/sdax /mnt
mount /dev/sdax/boot
mount /dev/sdax/home
```

### 准备连接

- 有线：

默认使用Dhcp，一般自动检测，无需设置

- 无线：
    
```
wifi-menu
```

-  编辑镜像列表

```
wget -O /etc/pacman.d/mirrorlist https://www.archlinux.org/mirrorlist/all/
```

> 取消注释中国的镜像

## 安装系统

```
pacstrap /mnt base
```

## 配置系统

### fstab文件

- Generate an fstab file (use -U or -L to define by UUID or labels):

```
genfstab -p /mnt >> /mnt/etc/fstab
```

### chroot

```
arch-chroot /mnt
```

### Hostname:

```
echo computer_name > /etc/hostname
```

### Time zone:

```
ln -sf /usr/share/zoneinfo/zone/subzone /etc/localtime
```

### Locale:

```
nano -w /etc/locale.gen
locale-gen
```

### Password:

```
passwd
```

### Initial RAM:

```
mkinitcpio -p linux
```

### Bootloader:

- 安装grub2:

```
pacman -S grub
grub-install --target=i386-pc --recheck  /dev/sda
```

- Dual-booting:

```
pacman -S os-prober
```

- 生成grub配置文件

```
grub-mkconfig -o /boot/grub/grub.cfg
```

### 重启

```
exit
reboot
```