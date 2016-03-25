Title: Vim常用技巧
Date: 2016-01-07 08:07
Modified: 2016-01-07 16:19
Category: Applications
Tags: apps, vi, vim
Slug: apps-vim
Authors: 孤逐王
Summary:

[TOC]

## 使用vim教程

```
vimtutor
```

它会复制一份教程文件,你可以放心练习,不用担心破坏原来的内容.

## 求助

`:help`
`:help + 相关内容`

## vim三种工作模式

- Normal模式: `Esc`
- Insert模式: `i` `a` `o` 
i:光标前 I:光标行首
a:光标后 A:光标行末
o:光标下新行 O:光标上新行
- 末行模式: `:`

### 定位

`h` `j` `k` `l`
`0` `^`  ^行首非空字符  0行首字符
`$` 末字符
`w` `W` `b` `B` `e` `E`
`Enter` 移至下行首
`gg` `G` `8G` 
`50%`
`H` `M` `L`
`zz` `zt` `zb`
`f`
`F`
`/`
`?`

`Ctrl + d`  下滚半页
`Ctrl + u`  上滚半页
`Ctrl + f`   下滚一页
`Ctrl + b`  上滚一页

`x`
`dw` `de`  `db`  `d$`
`dd` `D` `3dd`
`: 5,10d`
J

`u` `U` `Ctrl + R`

`yy`
`p`
`P`

`:wq` `:x` `zz`
`:q` `:q!`

### 查询信息

- 当前位围置
`Ctrl + G`
`:set number`  `:set nonumber`
`:set ruler`