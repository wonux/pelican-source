Title: Gentoo解决windows txt文件中文乱码问题 -- 文件编码介绍
Date: 2015-12-10 09:30
Category: Gentoo
Tags: gentoo, bugs, i18n,
Slug: gentoo-file-encode
Authors: 孤逐王
Summary: 

[TOC]

### Linux与Windows系统语言编码区别

在Linux操作系统下，我们有时打开在windows下的txt文件，发现在windows下能正常显示的txt文件出现了中文乱码。
出现这种情况的原因为两种操作系统的中文字符编码方式（压缩方式）不同，在windows环境中中文字符编码一般为gbk，而在linux环境中为utf8，这就导致了在windows下能正常显示txt文件在linux环境下打开呈现了乱码状态。

### 系统编码设置

`locale.gen`文件

```
# /etc/locale.gen: list all of the locales you want to have on your system
#
# The format of each line:
# <locale> <charmap>
#
# Where <locale> is a locale located in /usr/share/i18n/locales/ and
# where <charmap> is a charmap located in /usr/share/i18n/charmaps/.
#
# All blank lines and lines starting with # are ignored.
#
# For the default list of supported combinations, see the file:
# /usr/share/i18n/SUPPORTED
#
# Whenever glibc is emerged, the locales listed here will be automatically
# rebuilt for you.  After updating this file, you can simply run `locale-gen`
# yourself instead of re-emerging glibc.
en_US.UTF-8 UTF-8
zh_CN.UTF-8 UTF-8
```

- 查看系统语言编码种类
` /usr/share/i18n/locales/`目录下包含系统支持的编码语言种类

```
gentoo ~ # ls /usr/share/i18n/locales/
en_US       en_GB     en_HK    
zh_CN       zh_TW     zh_HK
ja_JP       de_DE     ......
gentoo ~ #
```

- 查看字符编码压缩方式

`/usr/share/i18n/charmaps/`目录下包含系统支持的字符编码方式

```
ls /usr/share/i18n/charmaps/
ANSI_X3.110-1983.gz    IBM1026.gz         ISO-8859-16.gz
ANSI_X3.4-1968.gz      IBM1047.gz         ISO_8859-1,GL.gz
ARMSCII-8.gz           IBM1124.gz         ISO-8859-1.gz
ASMO_449.gz            IBM1129.gz         ISO-8859-2.gz
GB18030.gz             ISIRI-3342.gz      SAMI.gz
GB_1988-80.gz          ISO_10367-BOX.gz   SAMI-WS2.gz
GB2312.gz              ISO_10646.gz       SEN_850200_B.gz
GBK.gz                 ISO_11548-1.gz     SEN_850200_C.
HP-ROMAN9.gz           ISO_6937.gz        UTF-8.gz
......
```

- `enca`查看文件编码方式

```
enca -L zh_CN file    ###检查文件的编码
```

### 解决方案

#### iconv编码转换

使用`iconv`命令进行文件编码转换，如乱码文件名为hello.txt，那么在终端输入如下命令：

```
iconv -f gbk -t utf8 hello.txt > hello.utf8.txt
```

 #### enca编码转换

使用`enca`命令转换:

```
enca -L zh_CN -x UTF-8 hello.utf8.txt      ###将文件编码转换为"UTF-8"编码
enca -L zh_CN -x gbk hello.txt     ###将文件编码转换为"gbk"编码
```
> `enca`有一个好处,如果文件本来就是你要转换的那种编码，它不会报错，还是会print出结果来， 而”iconv”则会报错。


