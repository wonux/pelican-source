Title: UNIX基础 -- 磁盘组织
Date: 2015-04-23 17:19
Modified: 2015-04-23 17:36
Category: FreeBSD
Tags: unix, disk, slice, freebsd,
Slug: freebsd-disk
Authors: 孤逐王
Summary:

[TOC]

## 磁盘组织

FreeBSD 查找文件的最小单位是文件名。 而文件名区分大小写，不凭文件扩展名去识别这个文件是 程序、 文档， 或是其他格式的数据。
在文件系统里目录和文件的作用是存储数据。 每一个文件系统都有且只有一个顶级目录 根目录， 这个根目录则可以容纳其他目录。

### Slice
FreeBSD将硬盘分成slices（片段），对应Windows系统的“分区”，Slices 有其编号， 从1到4，最多四个。Slices再分成分区（partitions）。Slice 编号在设备名后面， 并有一个 s 前缀， 从 1 开始。 每个磁盘上只能有四个物理的 slices， 但您可以在物理 slice 中使用适当的类型来创建逻辑 slice。 这些扩展 slice 编号从 5 开始。

- 分区的术语   
FreeBSD将硬盘分成最多四个slice（片段），FreeBSD的开机区必须在这些slice其中之一。每一个slice上又可以分成最多8个 partition（分区）,分别称为a,b,c,d,e,f,g,h，传统上a,b,c,d分区有特殊的意义，a表示root分区，b表示swap分 区，c表示整个slice，d表示整个硬盘。
- 分区的顺序
文件系统是和分区一一对应的。因为FreeBSD的UNIX传统，每一个分区使用一个从 a 到 h 的字母来表示。

```
a分区：通常指定为根文件系统。
b分区：通常指定为交换分区。
c分区：通常它和所在的 slice 大小相同。 c 分区上工作时必定会影响到事整个 slice (举个例子，坏块扫描器)。 您通常不愿意在这个partition建立文件系统。
d分区：d曾经有特殊的含义，不过这种意义在现时的系统上已不再适用，因此 d 可以和任何其它普通的分区一样使用了。
```

> 只有c内定位整个slice，其他都可自由使用，但一般还是遵循传统观念，即a:root，b:swap，efgh:其他使用。

- 磁盘设备的代码
一个磁盘名字是用磁盘类型代码和编号来标识的， 它不像slices，磁盘的编号是由0开始的。

```
SATA 和 IDE 磁盘    ada或ad
SCSI磁盘和USB存储设备    da 
SATA and IDE CD-ROM光驱   cd或acd
SCSI CD-ROM光驱    cd
软驱    fd
```

在安装FreeBSD时，您首先要配置好磁盘slices， 然后在FreeBSD使用的slice上建立partitions。 并在每个partition上建立一个文件系统(或交换分区)， 和指定文件系统的挂接位置。
