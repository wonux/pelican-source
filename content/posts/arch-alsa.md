Title: Arch声卡配置
Date: 2014-10-11 15:04
Modified: 2016-02-03 15:03
Category: Arch
Tags: arch, alsa
Slug: arch-alsa
Authors: 孤逐王
Summary:

[TOC]

### ALSA Utilities
Install the `alsa-utils` package. This contains (among other utilities) the `alsamixer` and `amixer` utilities.

```
pacman -S alsa-utils
```

### Unmuting the channels
ALSA by default has all channels muted, all of which will need to be unmuted manually. This can be done using amixer:

```
amixer sset Master unmute
```

This can alternatively be done using alsamixer:

```
alsamixer
```

### Test your changes

```
speaker-test -c 2
```

### User privileges

Usually, local users have permission to play audio and change mixer levels.
To allow remote users to use ALSA, you need to [add](https://wiki.archlinux.org/index.php/Users_and_groups#Group_management) those users to the audio
group.

参考：[https://wiki.archlinux.org/index.php/Advanced_Linux_Sound_Architecture](https://wiki.archlinux.org/index.php/Advanced_Linux_Sound_Architecture)