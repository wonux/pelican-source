Title: gcc-config:Active gcc profile is invalid 解决办法
Date: 2014-09-02 16:32
Modified: 2014-11-14 17:36
Category: Gentoo
Tags: gentoo, bugs, gcc,
Slug: gentoo-gcc-invalid
Authors: 孤逐王
Summary: 

[TOC]

### 错误描述

Gentoo软件安装错误,提示：

> gcc-config: Active gcc profile is invalid

### 解决方法：

- 列出可用的profile

```
gcc-config -l
```

> gcc-config: Active gcc profile is invalid!
  [1] i686-pc-linux-gnu-4.6.3

- 显示当前使用的profile

```
gcc-config -c
```

> gcc-config: Active gcc profile is invalid!
[1] i686-pc-linux-gnu-4.6.3

- 设置profile

```
gcc-config i686-pc-linux-gnu-4.6.3
```

> Switching native-compiler to i686-pc-linux-gnu-4.6.3 ...
Regenerating /etc/ld.so.cache...                                      [ ok ]
