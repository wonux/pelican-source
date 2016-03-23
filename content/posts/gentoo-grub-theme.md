Title: Gentoo启动菜单设置：使用官方LiveDVD Grub主题
Date: 2014-11-20 15:21
Category: Gentoo
Tags: gentoo, grub,
Slug: gentoo-grub-theme
Authors: 孤逐王
Summary: 

[TOC]

### 设置Gentoo Grub启动主题

- 拷贝官方LiveDVD grub主题：

下载官方DVD，找到 /boot/grub/themes/GenGrub目录，并拷贝出来。

- 安装GenGrub主题：

将GenGrub主题拷贝到系统的 /boot/grub/themes目录，并编辑grub配置文件：

```
nano -w /etc/default/grub
```

> 将主题路径设置成/boot/grub/themes/GenGrub/theme.txt

- 更新grub配置文件（grub2）：

```
grub2-mkconfig -o /boot/grub/grub.cfg
```

系统自动检测存在的操作系统和主题。

- OK，重启系统