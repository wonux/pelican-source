Title: Arch下载官方镜像列表Official mirrors
Date: 2014-10-08 13:29
Modified: 2015-02-10 17:08
Category: Arch
Tags: arch, mirrors
Slug: arch-mirrors
Authors: 孤逐王
Summary:

[TOC]

### Official mirrors

The official Arch Linux mirror list is available from the `pacman-mirrorlist` package. To get an even more up-to-date list of mirrors, use the Pacman Mirror List Generator page on the main site.

#### 手动下载镜像列表

有时因为系统镜像列表丢失或可读性不强，我们需要从官方网站下载按地区分类的镜像列表，很简单，执行如下命令：

```
wget -O /etc/pacman.d/mirrorlist https://www.archlinux.org/mirrorlist/all/
```