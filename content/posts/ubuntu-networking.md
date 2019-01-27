Title: Ubuntu networking issues
Date: 2017-10-01
Summary: A post about issues with network drivers on Ubuntu, that lead to a discovery of lvm partition magic, learning chroot and reasoning about Ubuntu and hardware.

A post about issues with network drivers on Ubuntu, that lead to a discovery of lvm partition magic, learning chroot and reasoning about Ubuntu and hardware.

This was one of that day when suddenly things go wild south. It started with a frozen system and fall down all way to missing drivers for network hardware. Debugging problem was hard, with intense use of `lshw`, `lspci`, `nmcli`, `ifconfig`, grepping through `dmesg`. Finally, I found out that it was a network driver issue, download it and like in old times `make clean modules && make install`.

Also, it is not obvious but ethernet and wireless networks have different drivers thus it can be easy that only wireless or only ethernet network can be unreachable.

But what really helped me was the ability to connect to broken system from live-cd with working internet connection.

```console
sudo mkdir /mnt/ubuntu
sudo mount /dev/ubuntu-vg/root /mnt/ubuntu

sudo mount --bind /dev /mnt/ubuntu/dev
sudo mount --bind /dev/pts /mnt/ubuntu/dev/pts
sudo mount --bind /proc /mnt/ubuntu/proc
sudo mount --bind /sys /mnt/ubuntu/proc

sudo chroot /mnt/ubuntu
```

And that's how you can try to fix broken ubuntu system. For example, if you **accidentally** put your system in an infinity booting loop or system won't boot.

In my case, it was that I was not able to install anything without an internet connection. I could download package on the flash drive, put it into working notebook and install with `dpkg`, but any program packages have dependencies, the more packages you want to install the more dependencies you get. And once apt manager sees unmet dependency it blocks purging, installing etc.

So, while this all was good, and I fixed my network connection, there was still a thought about what if ubuntu brokes again, and I will be downloading, installing and loading live-cd to fix it, maybe I better off installing another Linux distro on the same device.

I must say that modern ubuntu installation is suggesting the use of lvm. It is like a local volume instead of managing real physical volumes. And advantages of this approach is that you can have multiple HDD's but can manage space in them as a whole. But I best like it's `disadvantage` 😈.

> When you broke one local volume, you lost data on all physical volumes that local volume managed

So, as I understand for today there is not much of a GUI interface for working with lvm. There is a `system-config-lvm`, a relatively old package, but its disadvantage is that it will not install easily on modern Ubuntu 17+, you have to add package repo to apt and some users on StackOverflow are saying that this GUI program can be a reason for data loss, where console way with `lvresize` and `lvcreate` is a safer way.

In order to split lv partition you need to issue only two commands:

```console
sudo lvresize -L 800G /dev/ubuntu-vg/root
sudo lvcreate -L 200G -n kali ubuntu-vg
```

Here `ubuntu-vg` is local volume group, `kali` is new local volume partition name, `-L` stands for limit and sets the new size of the partition.

Also, there is a handy command `lvdisplay` for getting info about local volumes, they're name and group and `lvextend` for extending local volume size.

After these manipulations installing secondary os is not a problem. Only remember, if the installer will be complaining about root partition, select desired local volume, hit "change", format to any Ext file format and set the mount point to `/`.
