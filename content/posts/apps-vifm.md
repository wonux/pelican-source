Title: vi风格控制台文件管理器 -- vifm 配置使用
Date: 2015-12-22 08:40
Modified: 2015-12-23 08:54
Category: Applications
Tags: apps, vi, file-manager,
Slug: apps-vifm
Authors: 孤逐王
Summary:

[TOC]

## 介绍

vifm是Linux下一个基于ncurses的控制台文件管理器，我很少使用文件管理器，要用一下，就拿出vifm来。图形界面的文件管理器我不喜欢用，控制台下有人叫做mc的，功能很强大，但快捷键实在用不习惯，还经常和Terminal下的快捷键冲突，找来找去也只找到vifm这个还勉强可用，快捷键模拟vi，符合我的习惯。
vifm最主要的特点是模拟vi的快捷键，例如要复制某个文件，按yy，然后到目的文件夹，按p。要移动文件，将yy换成dd就可以了。直接重命名，则按cw。另外，删除文件并不是直接删除，而是移到分区根目录的`.vifm-Trash/`中，所以不小心删错了，还可以找回来。比较常用的命令有：

```
j,k     上下移动
h,l     在父/子目录之间移动
gg     移动到文件列表首行
G      移动到文件列表末行
M     移动到窗口中间
H,L   移动到窗口首末文件
gh     返回上级目录
gl,Enter     进入目录或打开文件
[count]dd,d[count]d     删除文件(放入回收站)
[count]DD,D[count]D   删除文件(不放回收站)
[count]yy,[count]Y,y[count]y     复制文件
p       粘贴文件
u       undo last change
Space,Tab     在两个panel之间切换
/     查找文件
m[a-zA-Z0-9]     标记文件
'[a-zA-Z0-9]     移到标记所在文件
za     切换隐藏文件显隐
zo     显示隐藏文件
zm     不显示隐藏文件
:fil regex     隐藏匹配regex的文件
zO     显示被:fil命令过滤的文件
zM     隐藏被:fil命令过滤的文件
cp     更改文件属性权限
cw    文件/文件夹重命名
cW   文件/文件夹重命名,不包含扩展名
ga     计算文件夹大小
!prog     执行系统命令, %f可以用来当前选中文件名
```

## 配置vifm

### 配置文件

Vifm creates and populates a `.vifm/` folder in your home directory containing the following:
`vifmrc` - a well commented configuration file that can be edited to suit your working style.
 `vifm-help.txt` - the help text
`vifminfo` - bookmarks and trash contents - it is not recommended to edit this file by hand
`Trash/ directory` - self explanatory
`colors/ directory` - color schemes
`Default` - well commented default color scheme - can be copied to create user-created color schemes

> To get started, read the information avaliable in:

```
/usr/share/vifm/vifm.txt
/usr/share/vifm/vifm-help.txt
```

### 用户自定命令

用户可以根据自己习惯配置自定义命令,如创建cp, mv命令用于将一个面板中选中的文件复制/移动到另一个面板中去。

```
command! cp cp -r %f %D
command! mv mv -r %f %D
```

```
" :com[mand][!] command_name action
" The following macros can be used in a command
" %a is replaced with the user arguments.
" %c the current file under the cursor.
" %C the current file under the cursor in the other directory.
" %f the current selected file, or files.
" %F the current selected file, or files in the other directory.
" %b same as %f %F.
" %d the current directory name.
" %D the other window directory name.
" %m run the command in a menu window

command! df df -h %m 2> /dev/null
command! diff vim -d %f %F
command! zip zip -r %f.zip %f
command! run !! ./%f
command! make !!make %a
command! mkcd :mkdir %a | cd %a
command! vgrep vim "+grep %a"
command! reload :write | restart
```

> 其中%a是一个特殊值，表示输入的参数，类似的%f表示当前选中的文件, %F表示在另一个面板中选中的文件，%d表示当前目录，%D表示另一个面板的当前目录。

### 集成命令:`mkcd` `move` `copy`

### 文件默认打开方式

vifm可以定义文件默认打开方式，这些都在`~/.vifm/vifmrc`中配置。使用`file[x]type`定义文件的默认打开方式：

```
 " Pdf
filextype *.pdf zathura %c %i &, apvlv %c, xpdf %c
fileviewer *.pdf pdftotext -nopgbrk %c -
" Image
filextype *.bmp,*.jpg,*.jpeg,*.png,*.gif,*.xpm
        \ {View in feh}
        \ feh -FZ %d --start-at %d/%c 2>/dev/null
        \ {View in sxiv}
        \ sxiv,
        \ {View in gpicview}
        \ gpicview %c,
        \ {View in shotwell}
        \ shotwell,
fileviewer *.bmp,*.jpg,*.jpeg,*.png,*.gif,*.xpm convert -identify %f -verbose /dev/null
" Office files
" filextype *.odt,*.doc,*.docx,*.xls,*.xlsx,*.odp,*.pptx libreoffice %f &
fileviewer *.doc catdoc %c
fileviewer *.docx, docx2txt.pl %f -
filextype *.doc,*.docx wps %f &
filextype *.xls,*.xlsx et %f &
```

参考:[https://wiki.archlinux.org/index.php/Vifm](https://wiki.archlinux.org/index.php/Vifm)