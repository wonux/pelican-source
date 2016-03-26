Title: UNIX基础 -- Manual Pages
Date: 2015-04-30 16:37
Modified: 2015-04-30 16:59
Category: FreeBSD
Tags: unix, man, freebsd,
Slug: freebsd-man
Authors: 孤逐王
Summary:

[TOC]

## 联机手册
Manual Pages

最详细的使用说明文档莫过于 FreeBSD 里的联机手册了。 几乎每一个程序都会附上一份简短说明， 以介绍这个程序的的基本功能以及参数的用法。 我们能通过 man 命令来阅读这些说明。
联机手册根据主题，分成下列章节:
```
1、    用户命令。
2、    系统调用以及错误代码。
3、    C 库文件里的函数说明。
4、    设备驱动程序。
5、    文件格式。
6、    游戏以及其他娱乐。
7、    各种资讯。
8、    系统维护以及命令。
9、    内核开发情况。
```

### `man`命令使用

- 加章节数字
例如查看chmod用户命令

```
man 1 chmod
```

- 搜索功能
`-k`选项加关键字,或使用`/`搜索

```
man -k mail
```

## GNU Info 文件

FreeBSD许多应用软件以及实用工具来自Free软件基金会(FSF)。 作为手册的扩充，这些程序提供了一种更具有活力的超文档说明info， 您可用info命令来阅读他们。