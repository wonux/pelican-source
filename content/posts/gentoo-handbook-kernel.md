Title: Gentoo安装详解（二）-- 编译内核
Date: 2014-05-04 17:10
Modified: 2015-05-08 10:44
Category: Gentoo
Tags: gentoo, handbook, kernel
Slug: gentoo-handbook-kernel
Authors: 孤逐王
Summary: 

[TOC]

## 编译内核：

- 安装内核源码：

选择内核：如gentoo-sources

```
emerge gentoo-sources
ls -l /usr/src/linux
```

### 手动编译内核：

```
cd /usr/src/linux
make menuconfig
```

- 必须启用的选项：

Most information can be gathered by emerging [sys-apps/pciutils]() which contains the `lspci` command:
显卡：[Xorg/Configuration](https://wiki.gentoo.org/wiki/Xorg/Configuration)
声卡：[ALSA](https://wiki.gentoo.org/wiki/ALSA)
网卡：根据具体网卡芯片型号，查看wiki。
无线网卡芯片驱动查询：[Linux Wireless](http://wireless.kernel.org/en/users/Devices/PCI)

>其他选项根据需要添加，不了解保持默认即可.

- 编译内核与模块：

```
make && make modules_install
```

- 拷贝内核到启动分区：

```
cp arch/x86_64/boot/bzImage /boot/kernel-3.10.10-gentoo
或
make install  #使用make install
```

> This will copy the kernel image into /boot together with the System.map file and the kernel configuration file.

### 使用genkernel编译内核：

```
emerge genkernel
```

- 可选：复制安装光盘上的内核配置文件：

```
zcat /proc/config.gz > /usr/share/genkernel/arch/x86_64/kernel-config
```

- 编译：

```
genkernel --menuconfig all
```

一旦genkernel运行完成，一个包括全部模块和initrd的内核将被建立。在后面配置引导程序时我们将会用到这个内核和initrd。请记下内核和initrd的名字，因为您将在配置引导程序的时候用到他们(Grub Legacy使用)。initrd将会在启动真正的系统前自动识别硬件（如同安装光盘一样）。

```
ls /boot/kernel* /boot/initramfs*
```
