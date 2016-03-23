Title: Gentoo/Arch常用软件列表
Date: 2016-02-24 14:30
Category: Gentoo
Tags: gentoo, arch, apps,
Slug: gentoo-arch-apps
Authors: 孤逐王
Summary: 

[TOC]

```
## Desktop Environment
### GNOME
### KDE
### LXDE
### Xfce

## Window Managers
### dwm
[x11-wm/dwm]  [dmenu]    
euse --enable savedconfig
ln -s /etc/portage/savedconfig/x11-wm/dwm-6.1 /etc/portage/savedconfig/x11-wm/dwm-6.1.h
### Awesome
### openbox
x11-wm/openbox
[obconf]  [obmenu]  [tint2]  [dmenu_run]
.config/openbox/
autostart  menu.xml  rc.xml

## Taskbars/Panels
### lxpanel
### tint2
[tint2]  [volumeicon]
.config/tint2/tint2rc
### wbar

## Desktop Utilities
### File Managers
#### vifm
#### xfe
#### dolphin
#### thunar
#### pcmanfm

### Clipboard Managers

### Terminal Emulators
#### rxvt-unicode
[x11-terms/rxvt-unicode]  [xorg-xrdb]  [x11-misc/xsel]  [x11-misc/xclip]  [x11-misc/urxvt-perls]
.Xresources  
.xinitrc == [[ -f ~/.Xresources ]] && xrdb -merge ~/.Xresources  
urxvtd --quiet --opendisplay --fork  ==  urxvtc
#### tilda
#### sakura
#### xfce4-terminal
#### konsole
#### yakuake
#### lxterminal

## Network Management
### dhcpcd
### wpa_supplicant
### networkmanager
### netctl

## Internet
### Email Clients
### P2P
#### rtorrent

### Web Browsers
#### firefox
#### chromium
#### midori

## Multimedia
### Audio
#### MPD
#### moc

### Video
#### mplayer

### Image Viewers
#### xfe
#### xfi

## Documents
### Editors
#### vim

### Document Readers
#### zathura
#### apvlv
#### mupdf

### Office Suites
#### wps-office

```


参考：
[https://wiki.gentoo.org/wiki/Rxvt-unicode](https://wiki.gentoo.org/wiki/Rxvt-unicode)
[https://wiki.archlinux.org/index.php/Rxvt-unicode](https://wiki.archlinux.org/index.php/Rxvt-unicode)
