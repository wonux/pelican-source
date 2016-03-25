Title: firefox神器：vimperator插件
Date: 2015-12-26 15:58
Modified: 2015-12-27 14:19
Category: Applications
Tags: apps, vi, firefox
Slug: apps-firefox-vimperator
Authors: 孤逐王
Summary:

[TOC]

## 介绍
Vimperator是一个Firefox浏览器扩展，能够使Firefox浏览器像Vim一样高效工作。在安装上 Vimperator之后，无论是 Firefox 的外观，还是 Firefox 的行为，都像极Vim。Vimperator还具有类似键盘绑定的功能，这使你能够灵活地使用热键来完成各种操作。不过，如果你想使用好它，必须确认你要有使用vim的经验，如同vim一样，vimperator也有多种模式，它也是致力于抛弃鼠标，使手指不用离开键盘就能完成大部分工作，事实也证明这样做确实很高效，但前提是你要习惯这种工作方式。

## HINT模式

这个模式算是用于极度的命令行爱好者或者鼠标坏掉的用户，hint模式就是为当前页面所有的链接标上序号，然后只要敲击键盘选择对应的链接即可，你的手完全不需要离开键盘去摸鼠标——我个人很喜欢这种方式。
最基本的用法就是在页面按`f/F`，然后根据显示的数字来选择一下，链接就打开了。f会原页面打开，F则会在新页面打开。
当然，还可以用‘;{mode}{hint}’来实现更多复杂的操作，但是对我来讲前面的就已经足够了，细节可以参考帮助文档。

## firefox系统功能

vimperator命令提供了firefox各种功能入口,常用的如下:

```
:dialog – To access some of Firefox's many dialog windows
:bmarks – Vimperator provides a new interface to bookmarks
:history – display a colorized, scrollable and clickable list of the locations in history.
:emenu – Access the Firefox menus through the Vimperator command line.
```

### 打开网页

```
-- o :o :open
:o[pen] [arg1], [arg2], …
o
O    Show an :open prompt containing the current URL.
:tabopen[!] [arg1], [arg2], …       [!], 后台打开,不切换到新标签
-- t :t :tabopen :tabnew
t
T    Show a :tabopen prompt containing the current URL.
-- w :winopen :wopen
:wino[pen][!] [arg1], [arg2], …
w
W
p    Open (put) a URL based on the current clipboard contents in the current buffer.
P
gP    Works like P but inverts the 'activate' option.

y    Yank current location to the clipboard. 
```

- 使用搜索引擎关键字搜索
` :open baidu keywords`

> 设置搜索引擎关键字:`dialog searchengines`.

###  历史导航

```
-- H <C-o> CTRL-O :ba :back
:[count]ba[ck] [url]
:ba[ck][!]    [!] goes to the beginning of the browser history.
-- L <C-i> CTRL-i :fo :fw :forward
:[count]fo[rward] [url]
:fo[rward]!
----------
:ju[mps]    List all jumps aka current tab's history aka session history.
gh    Go home. Opens the homepage in the current tab.
gH
```

### 标签页操作

我个人是非常喜欢使用VIM的Buffer操作的，简单快捷，精准。
而vimperator则是非常忠实的再现了这一特性，唯一不同的就是，这里的Buffer就相当于Tab。

```
-- B :tabs :ls :files :buffers
:buffers [filter]    Show a list of buffers.    %当前标签 #上一个标签
-- b :b :buffer    
[count]b    Go to the specified buffer from the buffer list.
[count]gb    Repeat last :buffer! command.
[count]gt    Go to the next tab.
[count]gT    Go to the previous tab.
[count]d    Delete current buffer tab.
:tabo[nly]    Close all other tabs.
-- u :u :undo
[count]u    Undo closing of a tab.
-- :undoa :undoall
:undoa[ll]    Undo closing of all closed tabs. Firefox存储10个最近关闭的标签(包括重启firefox).
d – close the active tab (delete the buffer)
```

### 刷新网页

```
r    Force reloading of the current web page.
R   Force reloading of the current web page skipping the cache.
:re[load][!]    Reload current web page.If [!] is given, skip the cache.
```

### 退出

```
-- :q :quit
:q[uit]    Quit current tab. The session is not stored.
-- :qa :qall :quita :quitall
:quita[ll]    Quit Vimperator. Quit Vimperator, no matter how many tabs/windows are open. The session is not stored.
-- :wc :wclose :winc :winclose
:winc[lose]    Close window.
-- :winon :winonly
:winon[ly]    Close all other windows.
--:xa : xall  :wq :wqa :wqall
:xa[ll]     Save the session and quit. 
ZQ    Quit and don't save the session. Works like :qall.
ZZ    Quit and save the session.Works like :xall.
```

### Buffer

#### Motion commands
```
-- <Home> gg
[count]gg    Go to the top.   [count] scrolls to [count]%.
-- <End> G
[count]G    Go to the end.   [count] scrolls to [count]%. 
{count}%    Scroll to {count} percent of the document.
-- <Left> h
[count]h    Scroll to the left.   [count], times to move to the left.
-- <Right> l
[count]l    Scroll to the right. [count], times to move to the right.
-- <C-e> <Down> j
[count]j    Scroll document down.  [count], times to move to the down.
-- <C-y> <Up> k
[count]k    Scroll document up.  [count], times to move to the up.

-- <C-d>    Scroll window down to half a page in the buffer. 
-- <C-u>    Scroll window up to half a page in the buffer. 
-- <S-Space> <PageUp> <C-b>
[count]<C-b>    Scroll up a full page. Scroll window [count] pages upwards.
-- <Space> <PageDown> <C-f>
[count]<C-f>    Scroll down a full page. Scroll window [count] pages downwards.

[count]gi    Focus last used input field or first input field. 
```

#### Zooming

```
[count]zi    Enlarge text zoom of current web page. Mnemonic: zoom in.
[count]zI    Enlarge full zoom of current web page. Mnemonic: zoom in.
[count]zo    Reduce text zoom of current web page. Mnemonic: zoom out.
[count]zO    Reduce full zoom of current web page. Mnemonic: zoom out.
[count]zm    Enlarge text zoom by a larger amount. Mnemonic: zoom more.
[count]zM    Enlarge full zoom by a larger amount. Mnemonic: zoom more.
[count]zr    Reduce text zoom by a larger amount. Mnemonic: zoom reduce.
[count]zR    Reduce full zoom by a larger amount. Mnemonic: zoom reduce.
[count]zz    Set text zoom value of current web page. [count] 30% to 300% default 100%.
[count]zZ    Set full zoom value of current web page. [count] 30% to 300% default 100%.
```

#### Copying text

```
y    Yank current location to the clipboard. 
Y    Copy currently selected text to the system clipboard
```