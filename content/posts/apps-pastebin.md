Title: 直接粘贴代码到网络上:command-line pastebins
Date: 2014-09-16 10:08
Modified: 2015-05-22 17:29
Category: Applications
Tags: apps, pastebin,
Slug: apps-pastebin
Authors: 孤逐王
Summary:

[TOC]

### 软件作用

直接把管道里面的文字内容传到网站上面，然后反馈一个地址可以读取内容。

### 同类软件

- wgetpaste
- dpaste
- pastebin
- pasteie

### 用法

介绍wgetpaste为例：

```
GENTOO ~ # cat /etc/portage/make.conf | wgetpaste
Your paste can be seen here: https://bpaste.net/show/bf4077579512
```

### 常见问题

#### pastebin服务源无法访问

解决办法：

- 列出可用的pastebin服务

```
GENTOO ~ # wgetpaste -S
Services supported: (case sensitive):
   Name:        | Url:
   =============|=================
   *bpaste      | https://bpaste.net/
    ca          | http://pastebin.ca/
    codepad     | http://codepad.org/
    dpaste      | http://dpaste.com/
    gists       | https://api.github.com/gists
    lugons      | https://paste.lugons.org/
    poundpython | http://paste.pound-python.org/
```

> 默认使用bpate

- 切换可用的pastebin服务，如dpaste

```
cat /etc /portage/make.conf | wgetpaste  -s dpaste
```