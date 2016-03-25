Title: RSync实现文件备份同步
Date: 2016-01-27 15:07
Modified: 2016-02-03 17:19
Category: Applications
Tags: apps, sync,
Slug: apps-rsync
Authors: 孤逐王
Summary:

[TOC]

## rsync介绍

`rsync` , Remote Synchronize 顾名思意它是一款实现远程同步功能的软件，可通过LAN/WAN快速同步多台主机间的文件。它在同步文件的同时，可以保持原来文件的权限、时间、软硬链接等附加信息。Rsync使用所谓的 “Rsync算法”来使本地和远程两个主机之间的文件达到同步，这个算法只传送两个文件的不同部分，而不是每次都整份传送，因此速度相当快，而且可以通过ssh方式来传输文件，这样其保密性也非常好，另外它还是免费的软件。
Rsync是一款通过网络备份重要数据的工具/软件。它同样是一个在类Unix和Window系统上通过网络在系统间同步文件夹和文件的网络协议。Rsync可以复制或者显示目录并复制文件。Rsync默认监听TCP 873端口，通过远程shell如rsh和ssh复制文件。Rsync必须在远程和本地系统上都安装。

### rsync优点

- 速度：最初会在本地和远程之间拷贝所有内容。下次，只会传输发生改变的块或者字节。
- 安全：传输可以通过ssh协议加密数据。
- 低带宽：rsync可以在两端压缩和解压数据块。

### 缺点

- 单向同步，不支持双向传输

### 特性

- 可以镜像更新整个目录树和文件系统。
- 有选择性的保持符号链链、硬链接、文件属于、权限、设备以及时间等；
- 对于安装来说，无任何特殊权限要求；
- 对于多个文件来说，内部流水线减少文件等待的延时；
- 用rsh、ssh 或直接端口做为传输入端口；
- 支持匿名rsync 同步文件，是理想的镜像工具；

## 使用

- 语法

````
rsync [OPTION] SRC_PATH/[SRC_FILE] DEST_PATH
```

- 选项

```
-a 以archive模式操作、复制目录、符号连接 相当于-rlptgoD,是保留了所有人和所属组、时间戳、软链接、权限，并以递归模式运行。
-l 是链接文件，意思是拷贝链接文件；-p 表示保持文件原有权限；-t 保持文件原有时间；-g 保持文件原有用户组；-o 保持文件原有属主；-D 相当于块设备文件；
-r 是递归
-z 传输时压缩；
-P 传输进度；
-v 传输时的进度等信息，和-P有点关系，自己试试。可以看文档；
-e ssh的参数建立起加密的连接。
-n,--dry-run预览操作，不实际改变文件。
-u, --update仅仅进行更新，也就是跳过所有已经存在于DST，并且文件时间晚于要备份的文件。(不覆盖更新的文件)，注意两者机器的时钟的不同.
--progress是指显示出详细的进度情况
--existing 仅仅更新那些已经存在于DST的文件，而不备份那些新创建的文件
--delete 删除那些DST中SRC没有的文件
--password-file=/password/path/file来指定密码文件，这样就可以在脚本中使用而无需交互式地输入验证密码了，这里需要注意的是这份密码文件权限属性要设得只有属主可读。
```

### 常用实例

- 启用压缩

```
rsync -zvr /home/aceking/ /backupdir
```

- 保留文件和文件夹的属性

```
rsync -zva /home/aceking/ /backupdir
```

- 模拟运行查看结果，不实际操作

```
rsync -zvan /home/aceking/ /backupdir
```

- 找出文件间的不同

```
rsync -avzi /backupdir /home/aceking/ 
```

### 排除文件和目录列表

有时候，当我们做大量同步的时候，我们可能想要从同步的文件和目录中排除一个文件和目录的列表。一般来说，像设备文件和某些系统文件，或者像临时文件或者缓存文件这类占据不必要磁盘空间的文件是不合适同步的，这类文件是我们需要排除的。

- 创建排除文件
`--exclude-from`参数,创建一个名为`excluded`的文件（当然，你想取什么名都可以），将想要排除的文件夹或文件写入该文件，一行一个。例如，如果你想要对根分区进行完整的备份，你应该排除一些在启动时创建的设备目录和放置临时文件的目录：

```
# cat exclude

/dev/*
/proc/*
/sys/*
/tmp/*
/run/*
/mnt/*
/media/*
/lost+found

# rsync -aAXhv --exclude-from=excluded / /mnt/backup
```

- 从命令行排除文件
`--exclude`参数,目录列表`{"/var/cache","/var/tmp"}`

```
rsync -aAXhv --exclude={"/var/cache","/var/tmp"} /var /home/adrian/var
```
