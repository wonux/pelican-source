Title: MPD+MPC+Conky 听音乐
Date: 2014-09-09 11:07
Modified: 2015-05-25 10:19
Category: Applications
Tags: apps, music
Slug: apps-mpd
Authors: 孤逐王
Summary:

[TOC]

## MPD、MPC介绍：

- 为何选用MPD+MPC？
在Linux下有很多不错的音乐播放器，强大的如amarok，简单的如bmp，而我更喜欢mpc（需要安装MPD），简洁是我选择它的理由。每次开机自动打开守护程序MusicPD（简称mpd），这如同一个潜在的点歌器，终端下用mpc就能选听自己喜欢的歌曲，不需要任何界面，也不必为音乐播放器单开一个桌面。
mpc和conky结合，可以做出开机音乐；mpc和remind结合用音乐来提醒某些事情。守护程序mpd就像一个功能强大的点歌器，你可以轻松地选择你喜爱的歌手、专辑，毫不逊于GUI的音乐播放器。
我们还可以用conky在桌面上显示mpd的情况，显示歌曲名，显示歌手名，显示播放进程等，设计我们自己的音乐播放器，够酷吧。
- MPD
MPD (Music Player Daemon) ：它跟常见的大多数播放器都很不同，是一个C／S结构的音乐播放器。MPD 作为一个守护程序运行于后台, 通过各种各样的client软件来控制播放动作、播放列表等， 占用很少的资源，从一开始使用我便喜欢上了这种方式。
这是一个可以在后台播放音乐的东东，非常节省资源，而且和X无关，在终端下一样能播放。而且可以用过各种各样的MPC前端来进行控制。
MPD的优点很多，配置简单但是功能丰富。比如，可以选择音频设备，选择mixer设备，选择ID3编码等等。最大的好处就是音乐播放和管理前台分离，这样既可以使用mpc这个最简单的MPD客户端控制播放，也可以用GMPC和QMPDClient这样的强大MPD客户端进行音乐管理。
- MPC
一个命令行下的Mpd客户端。

### 安装MPD

````    
emerge mpd
````

### 配置MPD

mpd的系统级配置文件是`/etc/mpd.conf`;用户级配置文件是`~/.config/mpd/mpd.conf` 或 `~/.mpdconf`.

编辑`mpd.conf`：
MPD设置有几个地方：
1、MPD的音乐目录和进程需要存放一些数据库等文件的目录；
2、MPD的执行用户；
3、MPD的输出和混音器选择；
4、MPD的ID3编码.

````
music_directory "/var/lib/mpd/music" 
playlist_directory "/var/lib/mpd/playlists" 
db_file "/var/lib/mpd/database" 
log_file "/var/lib/mpd/log" 
state_file "/var/lib/mpd/state" 
user "mpd" 
bind_to_address "localhost" 
bind_to_address "/var/lib/mpd/socket" 
input { plugin "curl" }
````

>mpd默认配置使用mpd用户，默认的`~`目录是`/var/lib/mpd/`.要添加mpd用户对`/var/lib/mpd/`目录相应的权限。

### 使用MPD

- 启动mpd守护进程

````
/etc/init.d/mpd start
````
- 开机启动

````
rc-update add mpd default
````

### MPD Clients
- mpc
- vimpc
- gmpc
- glurp
- ario

### MPC

mpc的常用参数：

```
mpc add 添加歌曲到播放列表
mpc listall|mpc add 可以把所有歌曲都添加到当前的播放列表
mpc listall 可以列出所有的歌曲
mpc playlist 查看当前播放列表
mpc 查看当前播放歌曲的信息
mpc play 播放
mpc pause 暂停
mpc stop 停止
mpc next 播放下一首
mpc prev 播放前一首
mpc repeat on 启用重复播放
mpc random on 启用随机播放
mpc play 18 播放列表中第18首
mpc search filename 可以按文件名查找
mpc search artist 可以按歌手查找
mpc search title 可以按歌曲名查找
音量调节：
mpc volume +20
mpc volume -20
mpc的更多选项可以看mpc的帮助。
```

## Conky

强大的Linux系统监控及桌面美化应用，在这里不详细介绍，自己Google，Wiki。