Title: Linux BT下载软件 -- Rtorrent 配置使用
Date: 2015-12-16 16:40
Modified: 2015-12-18 16:13
Category: Applications
Tags: apps, torrent,
Slug: apps-rtorrent
Authors: 孤逐王
Summary:

[TOC]
### rtorrent介绍

rtorrent是Linux下的bt下载软件,由于支持DHT网络,可以很好的于迅雷和Bitcomet的用户进行资源共享,所以很适合国内网络环境,下载速度极快.

### 配置：

因安装过程不自动生成配置文件，要手动在用户根目录新建`~/.rtorrent.rc`文件。
其内容大体如下：

```
#最小允许peer数
min_peers = 3
#最大允许peer数
max_peers = 500
#最大同时上传用户数
max_uploads = 10
#最大下载950k/s  光纤用户使用,adsl请酌情修改
download_rate = 950
#最大上传200k/s  光纤用户使用,adsl请酌情修改
upload_rate = 200

#下载目录
directory = ~/Downloads
#下载历史目录（此目录中包括下载进度信息和DHT节点缓存）
session = ~/Downloads/session
#（配置自动监视,把bt种子扔进～/Downloads/torrents目录就自动下载）
schedule = watch_directory,5,5,load_start=~/Downloads/torrents/*.torrent
#（配置自动监视,把bt种子从～/Downloads/torrents目录拿走就自动停止下载）
schedule = untied_directory,5,5,stop_untied=
#硬盘空间低于100M就自动停止一切下载）
schedule = low_diskspace,5,60,close_low_diskspace=100M
#（在总上传量达到200M的情况下上传/下载率达到200%,或者在总上传量不足200M情况下上传/下载率达到2000%,则停止上传）
# schedule = ratio,60,60,"stop_on_ratio=200,200M,2000"

#bt监听端口
port_range = 9400-9500
#随机从上面范围内选择端口
port_random = yes
######开启DHT######
dht = on
#DHT所用的UDP端口
dht_port = 9501   
#种子交换功能
peer_exchange = yes

#（上传缓存,每个种子10M,小内存用户请酌情修改）
send_buffer_size = 10M
#（下载缓存,每个种子20M,小内存用户请酌情修改）
receive_buffer_size = 20M
#(修改编码以避免中文乱码）
encoding_list=UTF-8
```

### 使用：

- 启动：命令行输入rtorrent 即可

```
gentoo ~ # rtorrent
```

rtorrent就会自动下载~/Downloads/torrents目录下面的所有bt种子.

- 添加和删除 torrents：
`回退键`    用 URL 或者文件路径添加，采用 tab 键查看目录内容并自动完成，支持通配符，例如: ~/torrent/*
`回车键`     和回退键一样，但是添加的 torrent 保持非激活( inactive )状态 (用 ^s 激活)
`^o`     对选择的 torrent 设置新的下载目录，仅仅对还没有被激活过的 torrent
`^s`     开始下载，先运行 hash ，除非已经做过
`^d`     停止激活的下载，或者删除一个停止的下载
`^r`     初始化 torrent 的 hash 检查
`a/s/d`    增加上传带宽 1/5/50 KB.
`z/x/c`     降低上传带宽 1/5/50 KB.
`A/S/D`     增加下载带宽 1/5/50 KB.
`Z/X/C`     降低下载带宽 1/5/50 KB.

> 注意： ^s 和 ^q 在 shell 里面经常用来控制屏幕的暂停，这会和 rTorrent 发生冲突，用 stty -a 来检查是否已经被使用，删除的办法是：
`stty stop undef`
`stty start undef`
before running rTorrent (or reattaching to screen) to leave them undefined. You could also replace undef with some other code — ^p, say. ^d also usually sends end-of-file but ncurses passes this through to rTorrent. stty eof undef if you are worried.
To fix this, you may also toggle the flow control in screen with ^a ^f until screen displays “-flow” in the bottom left corner.

- 退出： `CTRL+q`

### Global Keys

- 主屏幕视图操作
`^q`             关闭 rTorrent，再按一次，强行关闭
`上下`      选择 torrent
`右键`     切换到下载视图
`左键`     回到前一个屏幕
`^r `    检查 hash
`+/-`     修改优先度
`l `    查看日志，空格退出
`1`     显示所有下载
`2`     显示所有下载，按文件名排序
`3`    显示开始的下载
`4`     显示停止的下载
`5`     显示完成的下载
`6`     显示未完成的下载
`7`     显示正在 hash 的下载
`8`     显示正在做种的下载

- 下载视图
`right`    Switch to selected view
`left`     Switch to view selection or back to main view
`1/2`     Adjust max uploads.
`3/4`     Adjust min peers.
`5/6`     Adjust max peers.
`p`             Display peer info
`o`             Display torrent info
`i`             Display file list
`u`             Display tracker list
`t/T`       Initiate tracker request. Use capital T to force the request, ignoring the “min interval” set by the tracker.

- Peer list View Keys
`left`     Switch to view selection
`right`     Show peer details
`*`     Snub peer (stop uploading to this peer)
`k`     Kick peer (disconnect from peer)

- File list View Keys
`left`     Switch to view selection
`right`     Show file details
`space`     Change the file priority; applies recursively when done on a directory
`*`     Change the priority of all files
`/ `    Collapse directories. While collapsed, press right to expand the selected directory.

- Tracker list View Keys
`left`     Switch to view selection
`*`             Enable/disable tracker
`space`     Rotate trackers in a group