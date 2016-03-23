Title: Gentoo挂载Windowntfs的NTFS分区
Date: 2014-11-20 10:20
Modified: 2014-11-21 13:56
Category: Gentoo
Tags: gentoo, ntfs, 
Slug: gentoo-ntfs
Authors: 孤逐王
Summary: 

[TOC]

### 内核需要开启的选项

```
File systems --->
    <*> FUSE (Filesystem in Userspace) support
```

### 使用NTFS-3G

NTFS-3G是一个由Tuxera公司开发并维护的开源项目，目的是为Linux提供NTFS分区的的驱动程序。它可以安全且快速地读写 Windows 系统的 NTFS 分区，而不用担心数据丢失。

- 安装软件包：

```
emerge -pv sys-fs/ntfs3g
```

- 临时挂载NTFS分区

可以使用下面的命令以读写方式临时装载一个NTFS分区到装载点

```
mount  -t ntfs-3g <NTFS Partition>  <Mount Point>
```

- 系统启动时挂载NTFS分区

编辑`/etc/fstab`

```
vi /etc/fstab
```

在文件最后增加如下格式的行

> <NTFS Partition>  <Mount Point>  ntfs-3g  defaults  0  0
   
保存文件后重启系统或简单的执行下面的命令，即可装载NTFS分区到指定的装载点

```
mount  -a
```