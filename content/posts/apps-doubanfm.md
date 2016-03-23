Title: Shell终端收听音乐--豆瓣FM命令行版
Date: 2016-02-29 12:04
Modified: 2016-02-29 12:32
Category: Applications
Tags: apps, music, python
Slug: apps-doubanfm
Authors: 孤逐王
Summary:

[TOC]

## douban.fm

Terminal-based douban.fm inspired by [douban.fm](https://github.com/turingou/douban.fm).该版本版基于Python2.*

### 安装Python2.*

````
pacman -S python2
pacman -S python2-pip
````

### 安装douban.fm

```
pip2 install douban.fm
```

###需要mplayer播放器依赖,如未安装:

```
pacman -S mplayer
```

### Update

````
pip2 install --upgrade douban.fm
````

### Usage
在终端下直接输入

````
douban.fm
````

> 第一次登陆需要输入账号,密码,程序不会保留密码,而是保存返回的token存储在~/.douban_token.txt,下次登陆无需输入密码.

### Keys
支持vim按键

```
移动
[j] --> 下
[k] --> 上
[g] --> 移到最顶
[G] --> 移到最底
音乐
[space] --> 播放
[w] --> 打开歌曲专辑豆瓣主页
[n] --> 下一首
[r] --> 喜欢/取消喜欢
[b] --> 不再播放
[q] --> 退出
[p] --> 暂停
[l] --> 单曲循环
音量
[=] --> 增
[-] --> 减
[m] --> 静音
[e] --> 播放/历史/红心列表
歌词
[o] --> 显示歌词
[q] --> 退出歌词
帮助
 [h] --> 查看快捷键
主题
[1]
[2]
[3]
[4]
```

github主页： [douban.fm](https://github.com/turingou/douban.fm)