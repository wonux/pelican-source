Title: Gentoo/Funtoo USE标记介绍
Date: 2014-11-20 09:47
Modified: 2015-02-10 17:27
Category: Gentoo
Tags: gentoo, portage, use,
Slug: gentoo-use
Authors: 孤逐王
Summary: 

[TOC]

### Gentoo/Funtoo USE标记

USE的简单理解如下：一个软件不只包含软件本身，还包括其组件，如，文档，插件，GUI支持等。USE就是用来标记是否要安装软件的同时安装这些组件。

### 声明USE标记

所有USE标记都声明在USE变量里面。默认的USE设定，在make.defaults文件（你的profile的一部分）里声明。

#### 全局USE标记

不要通过修改make.defaults文件里的USE变量来满足你的需要：在升级Portage的时候，这个文件将会被破坏（被覆盖）。
要改变这个默认设置，你需要在USE变量里添加或移去关键字。这是通过在`/etc/make.conf`里定义USE全局变量来实现的。
全局USE标记适用范围是整个系统，保存在 /etc/portage/make.conf 文件中。
比如，如果使用GNOME而不想使用KDE，就希望所有软件都要默认支持GNOME，KDE的支持就不要装，那么写上 USE＝“gnome -kde"。前面加 - 表示移除。
当前可用的全局USE标记列表可以在网上或者本机的/usr/portage/profiles/use.desc文件里找到。

#### 局部USE标记

局部USE标记只被单个包用来做该包特有的决定，保存在 `/etc/portage/package.use` 中。
比如，某个软件需要安装帮助文档，加上doc。
当前可用的局部USE标记列表可以在网上或本机的/usr/portage/profiles/use.local.desc 文件里找到。

#### 临时USE标记

仅仅把USE变量声明成一个`环境变量`设定临时USE。比如，在安装 xxx 的时候不要装 jj 就声明：
`USE ＝ "-jj" emerge xxx`

#### USE标记优先级

USE标记这么多地方可以定义，有的加有的减，听谁的，需要有优先级来判断。USE优先级顺序如下（由低到高）：

> make.defaults（这个文件不要去修改）里面的USE默认设定 < 用户在/etc/make.conf里面的USE设定 < 用户在/etc/portage/package.use里面的USE设定 < 作为环境变量的USE设定

#### USE标记颜色

emerge命令显示时，不同**颜色**USE标记的意义:

```
*红色* 代表这次emerge用到的USE标记
*黄色* 表示从上次更新后该标记被增加、删除或者Masked
*蓝色* 前面带-表示这次emerge屏蔽掉的USE标记
*绿色* 的是你本次编译添加的新USE标记，或者去掉的USE标记。
```

#### 包特有的USE标记

查看特定包可用USE标记

```
emerge -pv xxx
```

#### 系统上应用新的USE标记

如果你已经修改了你的USE标记，而且你想用新USE标记更新你的系统，可以使用emerge 的 `--newuse`。

```
emerge --update --deep --newuse world  （重新构建你的系统）
```

参考：
http://en.gentoo-wiki.com/wiki/Portage
http://www.gentoo.org/doc/en/handbook/handbook-x86.xml?part=2&chap=1
http://www.gentoo.org/dyn/use-index.xml