Title: UNIX基础--Shells
Date: 2015-04-26 14:26
Modified: 2015-04-27 21:21
Category: FreeBSD
Tags: unix, shell, freebsd,
Slug: freebsd-shells
Authors: 孤逐王
Summary:

[TOC]

## Shells

Shell提供了一个和操作系统交互的命令行接口。shell的主要功能就是从输入取得命令然后去执行。FreeBSD内含了一些shell，包括:Bourne shell（sh）、 extended C shell（tcsh）。 其他shell也可在FreeBSD的Ports得到，例如:zsh和bash。 

### Shell的特点：

- 文件名补全
- 使用环境变量
Common Environment Variables

```
Variable	Description
USER	Current logged in user's name.
PATH	Colon-separated list of directories to search for binaries.
DISPLAY	Network name of the Xorg display to connect to, if available.
SHELL	The current shell.
TERM	The name of the user's type of terminal. Used to determine the capabilities of the terminal.
TERMCAP	Database entry of the terminal escape codes to perform various terminal functions.
OSTYPE	Type of operating system.
MACHTYPE	The system's CPU architecture.
EDITOR	The user's preferred text editor.
PAGER	The user's preferred utility for viewing text one page at a time.
MANPATH	Colon-separated list of directories to search for manual pages.
```

怎样设置环境变量：不同的shell有不同的方法。
- 在tcsh和csh这样的C-Style shell，使用`setenv`设置环境变量
- 在sh和bash这样的Bourne shell，使用, `export`设置环境变量

例如：设置或改变EDITOR环境变量，将EDITOR设为/usr/local/bin/vim.
在csh或tcsh下

```
setenv EDITOR /usr/local/bin/vim
```

在sh或bash下

```
export EDITOR="/usr/local/bin/vim"
```

命令行中在环境变量前加一个$字符，可以取得环境变量查看当前设置。
shell里有许多特别的字符代表着特别的内容，我们把叫做meta-characters。最常用的就是`*`字符，它可代表文件名的任何字符。为了防止shell去分析这些特别字符， 我们可在它之前加一个` \`字符去说明它只是普通字符。

### 改变Shell

改变Shell的最简单方法是使用 chsh 命令。 
- 执行 chsh 将根据EDITOR 环境变量进入到那个编辑器，假如没有设定，就会进入vi编辑器。 请改变“Shell:”这行对应值。
- 可使用chsh 的-s选项， 这样就能设置您的shell却又不用编辑器。假如想把shell改为bash:

```
chsh -s /usr/local/bin/bash
```

> 注意:新的shell必须在`/etc/shells`文件里列出。 如果从ports里安装一个shell，应该默认自动添加到这个文件了。如果没有添加，用下面的命令添加：`echo "/usr/local/bin/bash" >> /etc/shells` ，然后从新运行`chsh`.

### Shell高级技巧

Advanced Shell Techniques

- 重定向：`>` `<`
- 管道：`|`
