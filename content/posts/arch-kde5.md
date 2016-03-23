Title: Arch安装KDE5
Date: 2016-01-25 15:04
Modified: 2016-02-02 11:22
Category: Arch
Tags: arch, xorg, kde,
Slug: arch-kde
Authors: 孤逐王
Summary:

[TOC]

## plasma desktop

Install the `plasma-meta` meta-package or the `plasma` group. Alternatively, for a more minimal Plasma installation, install the `plasma-desktop` package.

## sddm
The Simple Desktop Display Manager (SDDM) is the preferred [display manager](https://wiki.archlinux.org/index.php/Display_manager) for [KDE](https://wiki.archlinux.org/index.php/KDE) Plasma desktop.

### Install sddm

```
pacman -S sddm
```
### Configuration

SDDM defaults to using systemd-logind for session management.

```
sddm --example-config > /etc/sddm.conf
```

### Loading sddm

```
systemctl start sddm
systemctl enable sddm
```