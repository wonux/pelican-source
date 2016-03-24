Title: Mplayer使用及快捷键
Date: 2014-10-29 14:08
Modified: 2015-12-16 11:13
Category: Applications
Tags: apps, video,
Slug: apps-mplayer
Authors: 孤逐王
Summary:

[TOC]

MPlayer 是我在 Linux 系统中用到的相当好的媒体播放程序，它因支持播放广泛的音／视频文件格式而著称。本文所要探讨的，除却一般的使用方法之外，更包括一些鲜为人知的提示和诀窍。相信在阅读此文后，你的多媒体播放体验将会增色不少。

### 配置文件

配置文件是`/etc/mplayer/mplayer.conf`和`~/.mplayer/config`
常用配置:

```
#subcp=cp936
#font=/usr/share/fonts/wqy-zenhei/wqy-zenhei.ttc
slang = "chs,eng"
sub-fuzziness=1
```

### 使用方法

简单实例:

```
mplayer -sub subtitle.srt -subcp cp936 -font /usr/share/fonts/wqy-zenhei/wqy-zenhei.ttc movie.avi
```

- 播放文件
使用 MPlayer 播放媒体文件最简单的方式是：
`mplayer <somefile>`
MPlayer 会自动检测文件的类型并加以播放，如果是音频文件，则会在命令行中显示该播放文件的状态信息；而假如是视频文件的话，则会打开一个新的播放窗口。

- 选择播放进度
`−ss <时间>` 参数指定的时间位置.示例:

```
mplayer <somefile> −ss 56    ###搜索到56秒处
mplayer <somefile> −ss 01:10:00    ###搜索到1小时10分钟处
```

- 倒退与快进
在播放文件的时候，你可以通过以下三组快捷键来对播放进程进行倒退与快进操作：
左方向键和右方向键：分别执行倒退 10 秒和快进 10 秒操作
下方向键和上方向键：分别执行倒退 1 分钟和快进 1 分钟操作
下翻页键和上翻页键：分别执行倒退 10 分钟和快进 10 分钟操作

- 播放 DVD
虽然 MPlayer 不支持 DVD 菜单，但是却能够播放 DVD。你可以这样播放 DVD：
`mplayer dvd://<titlenumber>`
你需要使用实际的数字来替换 <titlenumber>，如 1、2、3 等。

### 使用字幕
当播放电影文件时，你可以指定字幕文件(idx,sub字幕文件)：
`mplayer -sub <somesubtitlefile> <somefile>`
`mplayer -sub-paths <somesubpaths> <somefile>`

- 中文字幕乱码问题
使用ass文件字幕需要加`-ass`
参数:−ass (仅适用于FreeType)打开SSA/ASS字幕提供。 通过此选项, libass 将用于 SSA/ASS 外部字幕和 Matroska 轨迹。
`mplayer <somefile> -sub-paths <somesubpaths> -ass`

> 一般网上下载的字幕文件都是cp936的编码格式。如果不是，可以用iconv转换。比如utf8的转换成cp936的，命令如下：
`iconv -f utf8 -t cp936 -o name_of_movie.cp936.srt name_of_movie.utf8.srt`

- 让mplayer自动识别字幕文件并加载
最简单的就是修改字幕文件，使其与电影同名（不包括最后的扩展名）。
其实我们可以用下面的方法让mplayer更智能的。在配置文件`~/.mplayer/config`中加入下面两行：

```
slang = "chs,cht,eng"
sub-fuzziness=1
```

> −sub-fuzziness <模式>
搜寻字幕时调整匹配模糊度:
0 精确匹配;1 装载所有包含电影名称的字幕;2 装载当前目录的所有字幕。

### 有用的快捷键

以下是 MPlayer 中一些有用的快捷键：

```
f－当播放视频时，在全屏和窗口模式之间切换。你也可以在命令行中使用 -fs 选项，以便让 MPlayer 开始在全屏模式中播放。
o－在播放视频时切换 OSD（OnScreen Display）模式。
p 或 Space－暂停／继续播放。
q 或 Esc－退出 MPlayer。在 GUI 模式时，Esc 不会退出，仅停止播放。
/ 和 * 或 9 和 0－减小或增大音量。
m－静音切换。
T（通常是 Shift + t）－播放窗口置顶切换。
b 和 j－在可用的字幕间循环。
x 和 z－调整字幕的延迟时间。
I（Shift + i）－显示播放电影的文件名称。
1 和 2－调整对比度。
3 和 4－调整亮度。
5 和 6－调整色度。
7 和 8－调整饱和度。
```