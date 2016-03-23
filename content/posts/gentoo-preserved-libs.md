Title: Gentoo !!! existing preserved libs问题 
Date: 2014-11-20 12:21
Modified: 2014-11-20 14:01
Category: Gentoo
Tags: gentoo, bugs,
Slug: gentoo-preserved-libs
Authors: 孤逐王
Summary: 

[TOC]

## 问题描述

```
!!! existing preserved libs:
>>> package: media-libs/libmng-2.0.2-r1
 *  - /usr/lib/libmng.so.1
 *  - /usr/lib/libmng.so.1.0.0
 *      used by /opt/kingsoft/wps-office/office6/qt/plugins/imageformats/libqmng.so (app-office/wps-office-9.1.0.4751_alpha15)
>>> package: media-libs/lcms-1.19-r2
 *  - /usr/lib/liblcms.so.1
 *  - /usr/lib/liblcms.so.1.0.19
 *      used by /usr/lib/libmng.so.1 (preserved)
 *      used by /usr/lib/libmng.so.1.0.0 (preserved)
Use emerge @preserved-rebuild to rebuild packages using these libraries
```

## 解决方法

### 折腾过程：

1. emerge @preserved-rebuild 不起作用。

2. 重装wps-office，再@preserved-rebuild，不起作用。

3. 重装media-libs/libmng、package: media-libs/lcms不起作用。

```
emerge media-libs/libmng
emerge media-libs/lcms
emerge --depclean
revdep-rebuild
```

4.卸载wps-office（一直无法解决，想卸载暂时放弃使用），preserved libs提示消失：

```
emerge -C wps-office
emerge --depclean
emerge @preserved-rebuild
```

5.第二天安装wps-office，成功无preserved libs提示。

### 总结

- 先卸载引起preserved libs的软件包（记得--depclean）
- @preserved-rebuild
- 重新安装软件