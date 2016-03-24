Title: Linux系统维护 -- chroot
Date: 2014-11-25 16:08
Modified: 2015-01-04 14:29
Category: Applications
Tags: apps, chroot,
Slug: apps-chroot
Authors: 孤逐王
Summary:

[TOC]

## chroot简介

chroot，即 change root directory (更改 root 目录)。在 linux 系统中，系统默认的目录结构都是以 `/`，即是以根 (root) 开始的。而在使用 chroot 之后，系统的目录结构将以指定的位置作为 `/` 位置。
chroot是在unix系统的一个操作，针对正在运作的软件进程和它的子进程，改变它外显的根目录。一个运行在这个环境下，经由chroot设置根目录的程序，它不能够对这个指定根目录之外的文件进行访问动作，不能读取，也不能更改它的内容。
由chroot创造出的那个根目录，叫做“chroot监狱”（chroot jail，或chroot prison）。

## 为何使用 chroot

在经过 chroot 之后，系统读取到的目录和文件将不在是旧系统根下的而是新根下(即被指定的新的位置)的目录结构和文件，因此它带来的好处大致有以下3个：

- 增加了系统的安全性，限制了用户的权力；
在经过 chroot 之后，在新根下将访问不到旧系统的根目录结构和文件，这样就增强了系统的安全性。这个一般是在登录 (login) 前使用 chroot，以此达到用户不能访问一些特定的文件。
- 建立一个与原系统隔离的系统目录结构，方便用户的开发；
使用 chroot 后，系统读取的是新根下的目录和文件，这是一个与原系统根下文件不相关的目录结构。在这个新的环境中，可以用来测试软件的静态编译以及一些与系统不相关的独立开发。
- 切换系统的根目录位置，引导 Linux 系统启动以及急救系统等。
chroot 的作用就是切换系统的根位置，而这个作用最为明显的是在系统初始引导磁盘的处理过程中使用，从初始 RAM 磁盘 (initrd) 切换系统的根位置并执行真正的 init。另外，当系统出现一些问题时，我们也可以使用 chroot 来切换到一个临时的系统。

## chroot 的使用

下面以Gentoo、Arch为例，说明chroot过程：

- 确定chroot的目标目录：

如果LiveCD环境，挂载系统所在根分区

```
mount  /dev/sdx /mnt/gentoo
```

- 挂载/proc

```
mount -t proc none /mnt/gentoo/proc/
或
mount -t proc proc /mnt/gentoo/proc/
```

- 挂载/sys,/dev/

```
mount --rbind /sys /mnt/gentoo/sys/
mount --rbind /dev /mnt/gentoo/dev/
```

- 可选：

```
mount --rbind /tmp /mnt/gentoo/tmp   (gentoo)
mount  --rbind  /run /mnt/arch/run (arch)
```

- 复制DNS信息：

```
cp /etc/resolv.conf etc/resolv.conf
```

- chroot

```
chroot /mnt/gentoo /bin/bash
```

- 更新环境变量：

```
env-update     (gentoo)
source /etc/profile
```

- Optionally, create a unique prompt to be able to differentiate your chroot environment:
   
```
export PS1="(chroot) $PS1"
```


## 结束语

在 Linux 系统初始引导的过程中，通常都有使用 chroot。但是 chroot 的好处不仅于此，它还增加了系统的安全性等。