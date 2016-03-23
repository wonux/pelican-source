Title: Gentoo Xorg:Failed to load module "……" 问题
Date: 2014-10-24 09:32
Modified: 2014-12-22 14:12
Category: Gentoo
Tags: gentoo, bugs, xorg,
Slug: gentoo-xorg-failed
Authors: 孤逐王
Summary: 

[TOC]

### 错误描述：

安装完xorg-server后，startx启动桌面环境，出现缺少模块错误。

> Xorg:Failed to load module "……"

查看log：

```
cat /var/log/Xorg.0.log | grep EE  
```

> [75.403] (EE) Failed to load module "modesetting" (module does not exist, 0)
[75.403] (EE) Failed to load module "fbdev" (module does not exist, 0)
[75.403] (EE) Failed to load module "vesa" (module does not exist, 0)

### 解决方法：

查看xorg-drivers中INPUT_DEVICES和VIDEO_CARDS变量,在make.conf中添加缺失的标记。

```
emerge -pv  xorg-drivers
```

> These are the packages that would be merged, in order:
Calculating dependencies  ... done!
[ebuild   R    ] x11-base/xorg-drivers-1.15  INPUT_DEVICES="evdev keyboard mouse -acecad -aiptek -elographics -fpit -hyperpen -joystick -mutouch -penmount -synaptics -tslib -vmmouse -void -wacom" VIDEO_CARDS="intel -apm -ast -chips -cirrus -dummy -epson -fbdev -fglrx (-freedreno) -geode -glint -i128 -i740 -mach64 -mga -modesetting -neomagic -nouveau -nv -nvidia (-omap) (-omapfb) -qxl -r128 -radeon -radeonsi -rendition -s3virge -savage -siliconmotion -sisusb (-sunbw2) (-suncg14) (-suncg3) (-suncg6) (-sunffb) (-sunleo) (-suntcx) -tdfx -tga -trident -tseng -v4l -vesa -via -virtualbox -vmware (-voodoo)" 0 kB

在VIDEO_CARDS中添加modesetting,fbdev,vesa即可。