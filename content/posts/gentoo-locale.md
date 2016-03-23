Title: Gentoo本地化中文设置--Locale系统介绍
Date: 2014-11-20 16:21
Modified: 2015-01-05 16:35
Category: Gentoo
Tags: gentoo, locale,
Slug: gentoo-locale
Authors: 孤逐王
Summary: 

[TOC]

### locale是什么？

一份Locale是一组信息的集合，大多数程序利用它来确定特定的国家和语言设置。这些locale以及它们包含的数据是系统库的一部分，可以在大多数系统中的/usr/share/locale目录下找到。locale的名称通常命名为ab_CD的形式，其中ab是两个（或三个）字母的语言代号（在ISO-639中指定），CD是两个字母的国家代号（在ISO-3166中指定）。一些变量常常附加在locale名称的后面，例如en_GB.UTF-8或de_DE@euro。

### locale环境变量

Locale的设置保存在环境变量中。典型情况下设置在`/etc/env.d/02locale`（系统全局设置）和 `~/.bashrc`（特定用户设置）文件中。这些变量分别决定locale各方面的设置，下面的表格给出了具体说明。所有变量都会取一个前述ab_CD格式的locale名称作为值。
locale把按照所涉及到的文化传统的各个方面分成12个大类，这12个大类分别是：
```
    语言符号及其分类(LC_CTYPE)  
    数字(LC_NUMERIC)  
    比较和排序习惯(LC_COLLATE)  
    时间显示格式(LC_TIME)  
    货币单位(LC_MONETARY)  
    信息主要是提示信息,错误信息, 状态信息, 标题, 标签, 按钮和菜单等(LC_MESSAGES)  
    姓名书写方式(LC_NAME)  
    地址书写方式(LC_ADDRESS)  
    电话号码书写方式(LC_TELEPHONE)  
    度量衡表达方式(LC_MEASUREMENT)  
    默认纸张尺寸大小(LC_PAPER)  
    对locale自身包含信息的概述(LC_IDENTIFICATION)。  
```

其中，与中文输入关系最密切的就是**LC_CTYPE,LC_CTYPE**规定了系统内有效的字符以及这些字符的分类，诸如什么是大写字母，小写字母，大小写转换，标点符号、可打印字符和其他的字符属性等方面。而locale定义zh_CN中最最重要的一项就是定义了汉字(Class “hanzi”)这一个大类，当然也是用Unicode描述的，这就让中文字符在Linux系统中成为合法的有效字符，而且不论它们是用什么字符集编码的。
在en_US的locale定义中，并没有定义汉字，所以汉字不是有效字符。所以如果要输入中文必须使用支持中文的locale，也就是zh_XX，如zh_CN，zh_TW，zh_HK等等。
另外非常重要的一点就是这些分类是彼此独立的，也就是说LC_CTYPE，LC_COLLATE和 LC_MESSAGES等等分类彼此之间是独立的，可以根据用户的需要设定成不同的值。这一点对很多用户是有利的，甚至是必须的。例如，我就需要一个能够输入中文的英文环境，所以我可以把LC_CTYPE设定成。

### 怎样设定locale呢？

设定locale就是设定12大类的locale分类属性，即 12个`LC_*`。除了这12个变量可以设定以外，为了简便起见，还有两个变量：`LC_ALL`和`LANG`。它们之间有一个优先级的关系：

> `LC_ALL` > `LC_*` > `LANG`

可以这么说，LC_ALL是最上级设定或者强制设定，而LANG是默认设定值。

```
1.如果你设定了LC_ALL＝zh_CN.UTF-8，那么不管LC_*和LANG设定成什么值，它们都会被强制服从LC_ALL的设定，成为 zh_CN.UTF-8。  
2.假如你设定了LANG＝zh_CN.UTF-8，而其他的LC_*=en_US.UTF-8，并且没有设定LC_ALL的话，那么系统的locale设定以LC_*=en_US.UTF-8。  
3.假如你设定了LANG＝zh_CN.UTF-8，而其他的LC_*，和LC_ALL均未设定的话，系统会将LC_*设定成默认值，也就是LANG的值 zh_CN.UTF-8 。  
4.假如你设定了LANG＝zh_CN.UTF-8，而其他的LC_CTYPE=en_US.UTF-8，其他的LC_*，和LC_ALL均未设定的话，那么系统的locale设定将是：LC_CTYPE=en_US.UTF-8，其余的 LC_COLLATE，LC_MESSAGES等等均会采用默认值，也就是LANG的值，也就是LC_COLLATE＝LC_MESSAGES＝……＝ LC_PAPER＝LANG＝zh_CN.UTF-8。  
```

所以，locale是这样设定的：

```
1.如果你需要一个纯中文的系统的话，设定LC_ALL= zh_CN.XXXX，或者LANG= zh_CN.XXXX都可以，当然你可以两个都设定，但正如上面所讲，LC_ALL的值将复盖所有其他的locale设定，不要作无用功。  
2.如果你只想要一个可以输入中文的环境，而保持菜单、标题，系统信息等等为英文界面，那么只需要设定LC_CTYPE＝zh_CN.XXXX，LANG= en_US.XXXX就可以了。这样LC_CTYPE＝zh_CN.XXXX，而LC_COLLATE＝LC_MESSAGES＝……＝ LC_PAPER＝LANG＝en_US.XXXX。  
3.假如你高兴的话，可以把12个LC_*一一设定成你需要的值，打造一个古灵精怪的系统：LC_CTYPE＝zh_CN.GBK/GBK(使用中文编码内码GBK字符集)；LC_NUMERIC=en_GB.ISO-8859-1(使用大不列颠的数字系统)LC_MEASUREMEN=de_DE.ISO-8859-15@euro(德国的度量衡使用ISO-8859-15字符集)罗马的地址书写方式，美国的纸张设定……。估计没人这么干吧。  
4.假如你什么也不做的话，也就是LC_ALL，LANG和LC_*均不指定特定值的话，系统将采用POSIX作为lcoale，  
```

> 警告: LC_ALL设置之后不可被覆写，因此强烈反对使用。除非作测试请不要使用它，并且决不要把它设置在启动文件中。
