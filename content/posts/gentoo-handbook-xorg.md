Title: Gentoo安装详解（四）-- 安装X桌面环境
Date: 2014-05-05 10:20
Modified: 2015-05-14 11:03
Category: Gentoo
Tags: gentoo, handbook, xorg
Slug: gentoo-handbook-xorg
Authors: 孤逐王
Summary: 

[TOC]

## 安装X桌面环境：

### 安装Xorg：

- 检测显卡信息：

```
dmesg | grep video
lspci  | grep -i VGA
```

- 配置INPUT_DEVICE、VIDEO_CARDS变量：
在安装Xorg之前，你需要在/etc/portage/make.conf文件中设置两个重要的变量。

```
    (For mouse, keyboard, and Synaptics touchpad support)
    INPUT_DEVICE="evdev  synaptics"   
    （对nVidia显卡）
    VIDEO_CARDS="nvidia"
    （或，对ATI Radeon显卡）
    VIDEO_CARDS="radeon"
    （VMware虚拟机）
    VIDEO_CARDS="vmware"
    （VirtualBox虚拟机）
    VIDEO_CARDS="virtualbox"
```

- 安装xorg-server“

```
emerge -pv xorg-drivers
```

First of all, make sure udev is in your USE flags:

```
echo "x11-base/xorg-server udev" >> /etc/portage/package.use
```

Next, install Xorg:

```
emerge -av xorg-server
```

>注：现在比较新的版本的Xorg（大概是 1.5 以后的吧） 使用 evdev 替换了 keyboard 和 mouse ，确保 udev 标记在安装 xorg-server 时被启用。

- 更新环境变量：

```
env-update
source /etc/profile
```

- 使用startx：
安装 twm 和 xterm 之后 执行 startx 测试 X 是否正常。
测试正常之后可以删除 twm 和 xterm。

```
emerge -v twm xterm
startx
```

### 安装桌面环境：

这里选择轻量快速的 awesome 和 openbox （严格上不算完整的桌面环境，称为wm窗口管理器）配置介绍。它们自定义性比较强，可以根据自己喜好配置成各种效果。为了兼顾部署速度，我大多数选择默认配置，只做微量调整。

#### awesome

- 安装awesome：
awesome3.5.5以上版本,支持使用dmenu类似[Mod4+P]的命令补全。

```
emerge --ask awesome
```

- 配置awesome：
配置文件位于`~/.config/awesome/rc.lua`
主题文件在`/usr/share/awesome/theme/default/theme.lua`

```
mkdir -p ~/.config/awesome/
cp /etc/xdg/awesome/rc.lua ~/.config/awesome/rc.lua
```

- 检测：
更改配置文件后可以用下面的命令检测是否正确。

```
awesome -k
✔ Configuration file syntax OK
```

- 使用startx启动：
编辑`~/.xinitrc`文件

```
exec ck-launch-session dbus-launch --sh-syntax --exit-with-session awesome
```

- 常用配置

```
-- {{{ Variable definitions
-- Themes define colours, icons, font and wallpapers.
beautiful.init("/usr/share/awesome/themes/default/theme.lua")
-- This is used later as the default terminal and editor to run.
terminal = "tilda"
editor = os.getenv("EDITOR") or "nano"
editor_cmd = terminal .. " -e " .. editor
-- Autostart
awful.util.spawn_with_shell("fcitx &")
-- awful.util.spawn_with_shell("feh --bg-scale /usr/share/wallpaper/gentoo-gold.jpg")
-- }}}
```

- 音量控制：
后台启动`volumeicon &`

```
emerge --ask volumeicon
```

- 设置壁纸：
feh设置壁纸 `feh --bg-tile /path/to/image.jpg` --bg-scale --bg-center --bg-fill --bg-max

```
emerge --ask feh
```

> 除了在rc.lua中添加自启动应用命令，还可以添加`/etc/xdg/awesome/autostart`脚本。
在awesome中，terminal推荐tilda、sakura。

#### openbox

- 安装openbox：

```
emerge --ask x11-wm/openbox
```

- 配置openbox：
配置文件位于`/etc/xdg/openbox`

```
mkdir -p ~/.config/openbox/
cp /etc/xdg/openbox/* ~/.config/openbox/
```

- 使用startx启动：
编辑`~/.xinitrc`文件

```
exec ck-launch-session dbus-launch --sh-syntax --exit-with-session openbox-session
```

- Autostart脚本：

```
vim ~/.config/openbox/autostart
```

- 右键菜单配置：
1、安装Gentoo特有包`x11-misc/openbox-menu`，自动生成menu，不依赖`etc/xdg/menus`文件夹下的信息。

```
emerge --ask x11-misc/openbox-menu
openbox-menu
```

2、使用MenuMaker更新menu。

```
emerge menumaker
mmaker -v OpenBox3
```

```
cp .config/openbox/menu.xml /etc/xdg/openbox/menu.xml
```

> 或使用-f参数覆盖

- 配置主题：
GUI工具obconf

```
emerge obconf
obconf
```

- openbox去边框
Openbox 在匹配窗口的 name、class 及 role 时，可以使用通配符 * 和 ?。其中，* 用来匹配任意多个字符，而 ? 仅能匹配单个字符。例如：

```
<application name="*">
 <decor>no</decor>
</application>
```

这样就去掉了所有窗口的边框。

- Feh设置壁纸

- Panels：tint2

- 配置透明效果
参考另一篇文章: [openbox设置透明效果]()

#### dwm



