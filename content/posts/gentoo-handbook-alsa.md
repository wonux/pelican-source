Title: Gentoo安装详解（五）--声卡设置
Date: 2014-05-05 15:40
Modified: 2015-02-11 11:54
Category: Gentoo
Tags: gentoo, handbook, alsa
Slug: gentoo-handbook-alsa
Authors: Ace King,孤逐王
Summary: 

[TOC]

### 硬件检测

To choose the right driver, first detect the used audio controller. You can use lspci for this task:

```
lspci | grep -i audio
```

### 内核配置

You need to activate the following kernel options:

```
Device Drivers --->
    Sound --->
        <*> Sound card Support
            <*> Advanced Linux Sound Architecture --->
                [*]   PCI sound devices  --->
 
                      Select the driver for your audio controller, e.g.:
                      <*>   Intel HD Audio  ---> (snd-hda-intel)
                            Select a codec or enable all and let the generic parse choose the right one:
                            [*] Build Realtek HD-audio codec support
                            [*] ...
                            [*] Build Silicon Labs 3054 HD-modem codec support
                            [*] Enable generic HD-audio codec parser
```

### 软件

You also want to install media-sound/alsa-utils, if it isn't already pulled in:

```
emerge --ask alsa-utils
```

### 配置

#### 权限

Add the user you want to be able to access the sound card to the audio group:

```
gpasswd -a larry audio
```

#### 服务

You can now start ALSA:

```
/etc/init.d/alsasound start
```

To start ALSA at boot time, add it your boot runlevel:

```
rc-update add alsasound boot
```

#### Mixer调节音量，取消静音

If you can't hear anything, the output channels may be muted. Unmute the channels with your desktop environment's mixer or with alsamixer by selecting the appropriate channels and hitting the m key to mute or unmute:

```
alsamixer
```

### 测试声音

If everything above is perfect, you should now be able to test your sound card and your speakers. We will use the speaker-test command line tool from package media-sound/alsa-utils (this should already be installed as per our previous recommendation).

```
speaker-test -t wav -c 2
```


