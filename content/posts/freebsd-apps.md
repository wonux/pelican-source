Title: UNIX基础 -- 安装应用程序: Packages 和 Ports
Date: 2015-05-04 09:37
Modified: 2015-05-05 08:52
Category: FreeBSD
Tags: unix, ports, package, freebsd,
Slug: freebsd-apps
Authors: 孤逐王
Summary:

[TOC]

## Packages and Ports

### 概述

FreeBSD 将许多系统工具捆绑作为基本系统的一部分。另外，FreeBSD 提供了两种补充的技术来安装第三方软件：FreeBSD Ports Collection，从源代码安装； packages，从预编译的二进制版本安装。这两种方法都可以用于从本地介质， 或从网上直接安装您喜欢的应用程序的最新版本。

UNIX®系统典型的安装第三方软件的步骤包括：

```
1、下载这个软件，软件的发布可能是源代码格式，或是一个二进制包。
2、从默认的发行格式解压软件，通常是用compress, gzip,或bzip2压缩过tar包。
3、阅读相关文档，了解如何安装。 (通常文件名是INSTALL或README， 或在doc/ 目录下的一些文档)
4、如果软件是以源代码形式发布的，那就需要编译它。可能需要编辑一个 Makefile文件, 或运行 configure脚本。
5、测试和安装软件。
```

FreeBSD的package是包含了一个应用的所有命令、全部的配置文件和文档的预编译好的副本 。package可以使用pkg命令来操作。
FreeBSD的port是一个可以自动从源代码编译成应用程序的文件集合。这些文件包含了自动下载、解开、打补丁、编译、安装应用的所有必要的信息。

pots系统也可以用于生成被包管理命令维护的packages。
packages 和 ports 都可以自动处理依赖库。

这两种技术是很相似，packages 和 ports有各自的强项，根据需要选择哪种方法安装一个特定的软件。

Package优点
- 一个压缩的 package 通常要比一个压缩的包含源代码的应用程序小得多。
- package 不需要进行额外的编译时间。 对于大型应用程序如 Mozilla， KDE 或 GNOME 来说这显得尤为重要， 特别是在您的系统资源比较差的情况下。
- package不需要理解任何在FreeBSD上编译软件的详细过程。

Port优点：
- package 在编译时通常使用比较保守的选项，这是为了保证它们能够运行在大多数的系统上。通过从 port 安装，可以细微调整编译选项来产生适合于处理器的代码。
- 一些软件包已经把与它们相关的能做和不能做的事情的选项都编译进去了。从 port 中安装时，不一定要接受默认的选项， 可以自己来设置。
- 一些软件的许可条件禁止采用二进制形式发行。 它们必须以源代码形式发布，终端用户编译。
- 一些人不信任二进制发行形式。 至少有了源代码， (理论上) 可以亲自阅读它，寻找潜在的问题。
- 如果要自己对软件打补丁，您就需要有源代码。

### 查找软件

FreeBSD中可用的应用程序正在不断地增长着。有很多方法可以查找需要安装的软件。
- FreeBSD站点上维护着一个最新的的可搜索当前所有可用应用程序的列表，在 [http://www.FreeBSD.org/ports/](http://www.freebsd.org/ports/index.html)。ports可以通过程序名称或软件分类来搜索。
- Dan Langille维护着网站 FreshPorts，[http://www.FreshPorts.org/](http://www.FreshPorts.org/)。 FreshPort提供综合搜索工具，追踪ports中应用的变化。注册用户可以创建自定义检视列表，当有任何程序被升级时，他们就会发 email 提醒您。
- 如果不确定想要的应用程序的名字，可以尝试在 [SourceForge.net](http://www.sourceforge.net/) or [GitHub.com](http://www.github.com/)这些网站中查找，然后回到 [FreeBSD site](http://www.freebsd.org/ports/index.html)主站查看应用是否被port进去了（ be ported）。
- 查找二进制包仓库（binary package repository）
pkg search xxx
pkg search -o xxx
- Ports集（Ports Collection）安装后，有几种方法可以查询本地ports树。查找一个port属于哪个category：
`whereis lsof`
lsof: /usr/ports/sysutils/lsof
`echo /usr/ports/*/*lsof*`
/usr/ports/sysutils/lsof
- 另外一个查找软件的方法是用Ports Collection内嵌的搜索机制。要使用这个搜索机制, 需要先cd到/usr/ports目录下面，然后运行`make search name=program-name`，program-name是要查找的软件名。例如：

```
# cd /usr/ports
# make search name=lsof
Port:   lsof-4.88.d,8
Path:   /usr/ports/sysutils/lsof
Info:   Lists information about open files (similar to fstat(1))
Maint:  ler@lerctr.org
Index:  sysutils
B-deps:
R-deps: 
```

> 注意：内嵌搜索机制使用索引信息文件. 如果显示消息：the INDEX is required, 执行`make fetchindex`下载最新的索引文件. 

显示精简信息，使用quicksearch特性：

```
# cd /usr/ports
# make quicksearch name=lsof
Port:   lsof-4.88.d,8
Path:   /usr/ports/sysutils/lsof
Info:   Lists information about open files (similar to fstat(1))
```

为了更深入的搜索，还可以用 `make search key=string`， string就是想搜索的部分内容。 它将搜索port的名字、 注释， 描述和从属关系， 如果不知道您想搜索的程序名字， 可以利用它搜索一些关键主题来找到需要的。
当使用search或quicksearch时，搜索的关键字不区分大小写。

### 使用pkg进行二进制包管理

pkg是FreeBSD传统的包管理工具的下一代替代者。它提供了很多特性，使处理二进制包更快，更简单。
pkg不是替代像 [ports-mgmt/portmaster](http://www.freebsd.org/cgi/url.cgi?ports/ports-mgmt/portmaster/pkg-descr) 或 [ports-mgmt/portupgrade](http://www.freebsd.org/cgi/url.cgi?ports/ports-mgmt/portupgrade/pkg-descr)这样的port管理工具，这些工具既可以使用二进制方式又可以通过ports集方式安装第三方软件，而pkg只安装二进制包。

#### 安装pkg

从FreeBSD 8.4之后的版本包括了一个用于下载安装pkg（包括使用手册）的引导程序。（bootstrap utility）
- To bootstrap the system, run:

```
/usr/sbin/pkg
```

#### pkg常用命令
- 查看已安装软件包信息
`pkg info`
- 安装和移除软件包
`pkg install`和`pkg delete` 
- 更新已安装软件包
`pkg version` 
`pkg upgrade`
- 审核已安装软件包
`pkg audit -F`
- 自动移除孤立依赖
`pkg autoremove`
- 移除陈旧package包
`pkg clean`  

> pkg默认在一个缓存目录（PKG_CACHEDIR）存储二进制包，当使用pkg upgrade更新包时，旧的版本不会自动移除。

### 使用Ports Collection

Ports Collection ── 本质上是 /usr/ports 目录下的一堆 Makefile、 Patches（补丁）和描述文件，这些文件用于在FreeBSD系统中编译和安装应用。

#### 安装Ports Collection

- Portsnap Method
FreeBSD的base system包含Portsnap. 这是一个获得Ports Collection的快速易用的工具也是对大多数用户推荐的方法。
1、下载压缩的 Ports 套件快照到 /var/db/portsnap：

```
portsnap fetch
```

2、如果是首次运行 Portsnap，则需要将快照释放到 /usr/ports： 

```
portsnap extract
```

3、更新 /usr/ports：

```
portsnap fetch
portsnap update
```

> 当使用fetch选项时，extract、update选项可以连续运行：
`portsnap fetch update`

- Subversion Method
如果需要更多的控制ports tree或者本地更改需要维护，	Subversion可以用于获得Ports Collection。
1、在检测ports tree之前Subversion必须安装。如果ports tree已经存在：

```
cd /usr/ports/devel/subversion
make install clean
```

如果ports tree不可用：

```
pkg install subversion
```

2、Check out a copy of the ports tree. 使用离你最近的Subversion mirror替换`svn0.us-east.FreeBSD.org`

```
svn checkout https://svn0.us-east.FreeBSD.org/ports/head /usr/ports
```

3、As needed, update /usr/ports after the initial Subversion checkout:

```
svn update /usr/ports
```

#### Port Skeleton

port skeleton 是让一个程序在 FreeBSD 上简洁地编译并安装的所需文件的最小组合。 每个 port skeleton 包含：

```
Makefile:  Makefile 包括好几个部分， 指出应用程序是如何编译以及将被安装在系统的哪些地方。 
distinfo: 这个文件包括这些信息：这些文件用来对下载后的文件校验和进行检查	，来确保在下载过程中文件没有被破坏。	
files/: 这个目录包括在FreeBSD系统上编译和安装程序需要用到的补丁。这些补丁基本上都是些小文件，指出特定文件作了哪些修正。它们都是纯文本的的格式，基本上是这样的 “删除第 10 行” 或 “将第 26 行改为这样 ...”，补丁文件也被称作 “diffs”，他们由diff程序生成。
这个目录也包含了在编译 port 时要用到的其它文件。
pkg-descr:这是一个提供更多细节，有软件的多行描述。
pkg-plist: 这是即将被安装的所有文件的列表。它告诉 ports 系统在卸载时需要删除哪些文件。
```

port里面包含着如何编译源代码的指令，但不包含真正的源代码。ports中这个程序源代码标示文件叫 “distfile”,构建port的过程中会自动存储已经下载的源码到/usr/ports/distfiles.

#### 安装Ports

使用Ports Collection编译安装port，需要连接网络和超级用户特权。如果没有网络，则需要将 distfile 手工放到 /usr/ports/distfiles 中。
- 首先进入要安装 port 的目录：
`cd /usr/ports/sysutils/lsof`
- `make install`
- `make clean`

> 编译port的时候可以使用`make install clean`节省步骤。

#### 移除已安装的Ports

已经安装的ports可以使用`pkg delete`命令卸载。
也可以在ports目录，使用`make deinstall`命令

#### 升级Ports

列出可以更新版本的ports：

```
pkg version -l "<"
```

> Important:
Before attempting an upgrade, read /usr/ports/UPDATING from the top of the file to the date closest to the last time ports were upgraded or the system was installed. This file describes various issues and additional steps users may encounter and need to perform when updating a port, including such things as file format changes, changes in locations of configuration files, or any incompatibilities with previous versions. Make note of any instructions which match any of the ports that need upgrading and follow these instructions when performing the upgrade.

执行Ports升级，使用Portmaster或者Portupgrade.
- Upgrading Ports Using Portmaster
[ports-mgmt/portmaster](http://www.freebsd.org/cgi/url.cgi?ports/ports-mgmt/portmaster/pkg-descr)package（或称port），是推荐的升级已安装Ports的工具，它被设计为随FreeBSD系统使用而不需要依赖其他ports的工具。它用/var/db/pkg/中的信息决定哪些ports需要升级。

```
cd /usr/ports/ports-mgmt/portmaster
make install clean
```

Portmaster 把 ports 分成4类：

```
Root ports (不依赖其他的 ports，也不被依赖)
Trunk ports (不依赖其他的 ports，但是被其他的 ports 依赖)
Branch ports (依赖于其他的 ports，同时也被依赖)
Leaf ports (依赖于其他的 ports，但不被依赖)
```

可以使用 -L 选项列出所有已安装的 ports 和查找存在更新的 ports：

```
portmaster -L
===>>> Root ports (No dependencies, not depended on)
===>>> ispell-3.2.06_18
===>>> screen-4.0.3
        ===>>> New version available: screen-4.0.3_1
===>>> tcpflow-0.21_1
===>>> 7 root ports
...
===>>> Branch ports (Have dependencies, are depended on)
===>>> apache22-2.2.3
        ===>>> New version available: apache22-2.2.8
...
===>>> Leaf ports (Have dependencies, not depended on)
===>>> automake-1.9.6_2
===>>> bash-3.1.17
        ===>>> New version available: bash-3.2.33
...
===>>> 32 leaf ports
===>>> 137 total installed ports
        ===>>> 83 have new versions available
```

可以使用这个简单的命令升级所有已安装的 ports：

```
portmaster -a
```

如果你在升级的过程中发现了错误，你可以使用 -f 选项升级/重新编译所有的 ports：

```
portmaster -af
```

同样你也可以使用 Portmaster 往系统里安装新的 ports，升级所有的依赖关系之后并安装新的 port：

```
portmaster shells/bash
```

> 注意:
Portmaster 默认在删除一个现有的 port 前会做一个备份包。如果新的版本能够被成功安装， Portmaster 将删除备份。 使用 -b 后 Portmaster 便不会自动删除备份。加上 -i 选项之后 Portmaster 将进入互动模式， 在升级每个 port 以前提示你给予确认。

-  Upgrading Ports Using Portupgrade
portupgrade 工具是设计来简化升级已安装的 port 的操作的。 它通过 [ports-mgmt/portupgrade](http://www.freebsd.org/cgi/url.cgi?ports/ports-mgmt/portupgrade/pkg-descr) port 来提供。它安装一系列用于ports管理的应用。然而，它依赖于ruby。

```
cd /usr/ports/ports-mgmt/portupgrade
make install clean
```

在每次升级之前，推荐使用 `pkgdb -F` 命令来扫描已安装的 port 的列表， 并修正其所报告的不一致。
运行portupgrade -a升级系统中所安装的所有过时的 ports。 如果您希望在每个升级操作时得到确认， 应指定 -i 参数。

```
portupgrade -ai
```

如果您只希望升级某个特定的应用程序， 而非全部可用的 port，应使用portupgrade pkgname。 指定 -R 参数非常重要，portupgrade将首先升级指定程序所需要的所有ports。

```
portupgrade -R firefox
```

要使用预编译的 package 而不是 ports 来进行安装， 需要指定 -P。 如果指定了这个选项， portupgrade 会搜索 PKG_PATH 中指定的本地目录， 如果没有找到， 则从远程站点下载。 如果本地没有找到， 而且远程站点也没有成功地下载预编译包， 则 portupgrade 将使用 ports。 要禁止使用 port， 可以指定 -PP。

```
portupgrade -PP gnome2
```

#### Ports and Disk Space

在通过 ports 编译和安装软件之后，您应记得清理临时的 work 目录， 其方法是使用 make clean 命令。 
- If Portmaster is used to install a port, it will automatically remove this directory unless -K is specified. 
- If Portupgrade is installed, this command will remove all work directories found within the local copy of the Ports Collection:
`portsclean -C`

另外,许多过时的源码文件被收集在目录 /usr/ports/distfiles 中. 如果安装了Portupgrade, 下列命令将删除那些不被其他port引用的过时的distfiles。

```
portsclean -D
```

使用Portupgrade移除所有的不被系统其他port引用的distfiles:

```
portsclean -DD
```

如果安装了Portmaster,使用:

```
portmaster --clean-distfiles
```

除了这些命令之外,  [ports-mgmt/pkg_cutleaves]() package（or port）自动完成移除已安装但不再使用的ports的任务。