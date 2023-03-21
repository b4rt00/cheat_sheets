## 101.1: Determine and configure hardware settings [2]
```bash
# list PCI devices
lspci
-v # detailed
-s # select device by address
-k # list kernel modules of device

# list USB devices
lsusb
-v # detailed
-s # select device by bus and device number
-d # select device by vendor and device ID
-t # show device mappings in a tree

# list loaded kernel modules
lsmod

# load/unload kernel module
modprobe [module]
modprobe -r [module]

# display info about kernel module
modinfo [module]
-p # print only parameters

# view custom module parameters
cat /etc/modprobe.conf
cat /etc/modprobe.d/*

# prevent module from loading
echo "blacklist [module]" >> /etc/modprobe.d/blacklist.conf

# display cpu info
cat /proc/cpuinfo

# display numbers of interrupts
cat /proc/interrupts

# list currently registered I/O port regions in use
cat /proc/ioports

# list registered DMA channels in use
cat /proc/dma

# list sysfs file system
ls /sys

# list devices on the system
ls /dev

# view udev configuration
cat /etc/udev/rules.d/*

```

## 101.2: Boot the system [3]
```bash
## BIOS
# bootloader at the first 440 bytes of the first storege device
# relies on Master Boot Record

## UEFI
# bootloader is an EFI application stored on EFI System Partition
# relies on settings stored in NVRAM on motherboard, not MBR
# NVRAM points to the EFI application with the bootloader

## GRUB parameters
acpi         # turn acpi support on/off 
init         # set alternative system initiator
systemd.unit # set systemd target to be activated
mem          # set amount of RAM available to the system
maxcpus      # limit CPU cores visible to the system
quiet        # hide most boot messages
vga          # select a video mode
root         # set a root partition
rootflags    # set mount options for the root filesystem
ro           # mount root read only
rw           # mount root read-write

# permanently change GRUB parameters
vim /etc/default/grub # on line GRUB_CMDLINE_LINUX
grub-mkconfig -o /boot/grub/grub.cfg # generate new GRUB config

# view what GRUB parameters were used in the most recent boot
cat /proc/cmdline

## SysV
# the oldest init system
# uses shell scripts executed one after another
# uses runlevels to control system state

## systemd
# the modern init system used by most distros
# uses parallelization
# unit files devine system services and manage dependencies

## Upstart
# designed to replace SysV
# parallelizes the loading of system services

# display messages in the kernel ring buffer
dmesg
journalctl -b
journalctl -k
journalctl --boot
journalctl --dmesg

# clear kernel ring buffer
dmesg --clear

# list previous boots
journalctl --list-boots

# display events from previous boot
journactl -b [num] 

# read log messages from different directory
# the default is: /var/log/journal
journactl -D [directory]

```

## 101.3: Change runlevels/boot targets and shutdown or reboot system [3]
```bash
# SysVinit

# Runlevels
0 # system shutdown
1 # single user mode
2 # multi user mode
3 # multi user mode
4 # multi user mode
5 # multi user mode with GUI
6 # system restart

/sbin/init   # program managing runlevels
/etc/inittab # config file of the init process
/etc/init.d/ # 



```

## 102.1: Design hard disk layout [2]
```bash
# mount points
/mnt   # traditional directory to mount devices
/media # modern directory to mount devices

# automatic mounts
/media/[user]/[label]

# boot partition
/boot

# variable data partition
/var

# home dir partition
/home

# LVM devices
/dev/[vg]/[lv]

# mount a partition
mount [what] [where]

```

## 102.2: Install boot manager [2]
```bash

```

## 102.3: Manage shared libraries [1]
```bash
## Static libraries
#  library code embedded into the program
#  no dependencies at runtime
#  bigger file size

## Dynamic libraries
#  program only references library code
#  program has dependencies
#  smaller file size

# Library naming convention
[name][so][ver]
libpthread.so.0 # example

# common locations for shared libraries
/lib
/lib32
/lib64
/usr/lib
/usr/local/lib

# Dynamic linker
ld.so
ld-linux.so

# library path
/etc/ld.so.conf
/etc/ld.so.conf.d/*.conf

# work with shared library cache
ldconfig
-p # print cache
-v # verbose

# add new paths to shared libraries temporarily
export LD_LIBRARY_PATH=[path]

# search for dependencies of executable
ldd [file]
-u # print unused direct dependencies

# display information about the contents of ELF files
readelf [file]

# display information about the contents of object files
objdump [file]

```

## 102.4: Use Debian package management [3]
```bash
# install package with dpkg
dpkg --install [package]
dpkg -i [package]

# remove package with dpkg
dpkg --remove [package]
dpkg -r [package]

# remove package and all its files
dpkg --purge [package]
dpkg -P [package]

# get info about a package
dpkg --info [package]
dpkg -I [package]

# get all installed packages
dpkg --get-selections

# list every file installed by a package
dpkg -L [package]

# find out which package created a specific file
dpkg-query -S [file]

# reconfigure already installed package 
dpkg-reconfigure [package]

# APT utilities
apt-get   # dowload, install, upgrade, remove
apt-cache # search etc.
apt-file  # search for files inside packages

# update package index
apt-get update

# install a package
apt-get install [package]

# remove a package
apt-get remove [package]

# remove a package and all its files
apt-get purge [package]
apt-get remove --purge [package]

# fix broken dependencies
apt-get install -f

# update installed packages
apt-get upgrade

# view local apt cache
ls /var/cache/apt/archives
ls /var/cache/apt/archives/partial

# clear local apt cache
apt-get clean

# search for keyword in packages
apt-cache search [keyword]

# show full information about the package
apt-cache show [package]

# view apt repositories
cat /etc/apt/sources.list

## APT repo syntax
# Archive type
deb     # binary files
deb-src # source code
# URL 
http://us.archive.ubuntu.com/ubuntu # example
# Distribution (code name)
disco # example: Ubuntu 19.04 Disco Dingo
# Components (Ubuntu)
main       # officially supported, open-source
restricted # officially supported, closed-source
universe   # community maintained, open-source
multiverse # unsupported, closed-source, patented
# Components (Debian)
main       # compliant with DFSG, don't rely on non-DFSG software
contrib    # compliant with DFSG, depend on non-DFSG packages
non-free   # not compliant with DFSG
security   # security updates
backports  # more recent versions of 'main' packages

# add additional repos
echo [repo] >> /etc/apt/sources.list
echo [repo] >> /etc/apt/sources.list.d/[file]

# update apt-file cache
apt-file update

# list contents of a package
apt-file list [package]

# search which package provides a given file
apt-file search [file]

```

## 102.5: Use RPM and YUM package management [3]
```bash
# install package with RPM
rpm --install [package]
rpm -i [package]

# upgrade pacage with RPM
rpm --upgrade [package]
rpm -U [package]
rpm -U -F [package] # don't install if not present
-v # verbose
-h # display progress

# delete package with RPM
rpm --erase [package]
rpm -e [package]

# list installed packages
rpm --query --all
rpm -qa

# get package info
rpm --query --info [package]
rpm -qi [package] 
rpm -qip [package_file] # if package is not installed

# list files of installed package 
rpm --query --list [package]
rpm -ql [package]
rpm -qlp [package_file] # if package is not installed

# find out what package owns a file
rpm --query --file [file]
rpm -qf [file]

# search for keyword using yum
yum search [keyword]

# install package
yum install [package]

# update package
yum update [package]

# remove a package
yum remove [package]

# update all packages
yum update

# find out which package provides a specific file
yum whatprovides [file]

# get info aobut a package
yum info [package]

# view yum repos
cat /etc/yum/repos.d/*.repo

# add yum repo
yum-config-manger --add-repo [url]

# list all available repos
yum repolist all

# enable/disable a repo
yum-config-manager --enable [repo]
yum-config-mangeer --disable [repo]

# search for keyword using DNF
dnf search [keyword]

# get info about the package
dnf info [package]

# install a package
dnf install [package]

# remove a package
dnf remove [package]

# upgrade a package
dnf upgrage [package]

# find out which package provices a specific file
dnf whatprovides [file]

# list packages installed on the system
dnf list --installed

# list contents of a package
dnf repoquery -l [package]

# display available repos
dnf repolist all
dnf repolist --enabled
dnf repolist --disabled

# add repo
dnf config-manager --add_repo [URL]

# enable/disable repo
dnf config-manager --set-enabled [repo_ID]
dnf config-manager --set-disabled [repo_ID]

# list dnf repos
cat /etc/yum.repos.d/*.repo

# update package index with zypper
zypper refresh

# search for package
zypper se [package]

# list all installed packages
zypper se -i

# search for keyword in installed packages
zypper se -i [keyword]

# search for keyword in not installed packages
zypper se -u [keyword]

# install package
zypper in [package]

# remove package
zypper rm [package]

# find out what package owns a specific file
zypper se --provides [file]

# get package info
zypper info [package]

# list repos
zypper repos

# enable/disable repo
zypper modifyrepo -d [repo]
zypper modifyrepo -e [repo]

# enable/disable repo autorefresh
zypper modifyrepo -f [repo]
zypper modifyrepo -F [repo]

# add repo
zypper addrepo [URL] [name]

# remove repo
zypper removerepo [name]

```

## 102.6: Linux as a virtualization guest [1]
```bash

```

## 103.1: Work on the command line [4]
```bash
# print working directory
pwd

# create a file
touch [file]

# retrieve basic system and kernel info
uname -a 

# get command man page
man [command]

# search a keyword in man pages
apropos [keyword]

# get the type of the command
type [command]

# display hashed commands
hash

# clear command hash table
hash -d

# locate a command
which [command]

# display command history
history
cat ~/.bash_history

# view environmental variable
env

# display $PATH variable value
echo $PATH

# create a varaible
variable=[value]

# create an environmental variable
export variable=[value]

# delete environmental variable
unset [variable]

# display all variables and functions
set

# create files with spaces
touch "file with spaces"
touch file\ with \spaces

```

## 103.2: Process text streams using filters [2]
```bash
# redirect stdout
echo "hello" > hello.txt

# redirect stdin
echo < hello.txt

# compare two files
diff [file1] [file2]

# append to a file
echo "hello" >> hello.txt

# redirect stdout of one command to stdin of another 
[command] | [command]

# read contents of a gziped file
zcat [file]

# read contents of a file compressed with bzip2
bzcat [file]

# view file content in a pager
more [file]
less [file]

# view a portion of a file
head [file]
tail [file]

# display line numbers
cat [file] | nl

# count number of lines 
cat [file] | wc -l

# search for a string in a file using sed
sed -n /string/p < [file]

# delete lines containing a string using sed
sed /string/d < [file]

# replace text using sed
sed s/string1/string2/ < [file]

# replace text in place using sed
sed -i s/string1/string2/ [file]

# extract two fields of a comma separated file
cut -d "," -f 1,2 file.txt

# extract first 10 characters of a file
cut -c 1-10 file.txt

# calcualte a sha256 checksum of a file
sha256 [file]

# verify checksums provided in a file
sha256 -c [file]

# print file contents in octal format
od [file]

# print file contents in hex
od -x [file]

# print all characters in a file
od -c [file]

# print all characters in a file without offset into
od -An -c [file]
``` 

## 103.3: Perform basic file management [4]
```bash
# list files
ls
ls -l # long
ls -a # all
ls -h # human-readable
ls -R # recurse

# create a file
touch [file]

# copy a file
cp [file] [dir]
cp [file] [file]
cp -r [dir] [dir]

# move a file
mv [file] [dir]
mv [file] [file]
mv -r [dir] [dir]
mv -i # ask to override
mv -f # forcefully override

# remove a file
rm [file]
rm -i [file] # ask
rm -f [file] # force
rm -r [dir] # recursively

# create a directory
mkdir [dir]
mkdir -p [path] # create parents

# remove directory
rmdir [dir]
rmdir -p [path] # remove structure

# wildcards
* # any number of characters
? # a single character
[] # a range or list of characters

# find command
find [where] [what]
-type [fdl] # file, directory, link
-name # search based on name
-iname # search based on name case insensitive
-not # return results that do NOT match the test case
-maxdepth # search N levels deep
-size # search based on size

# execute command on the results
find [where] [what] -exec [command] {} \;

# delete all files that match the condition
find [where] [what] -delete

# tar command
tar [options] [archive] [files]
--create -c  # create new archive
--extract -x # extract an archive
--list -t    # display files in an archive
--verbose -v # show files being processed
--file -f    # specify file
--gzip -z    # gzip the archive
--bzip2 -j   # bzip2 the archive

# create an archive
tar -cvf [archive] [dir]
tar -cvf [archive] [file1] [file2]

# extract an archive 
tar -xvf [archive]
tar -xvf [archive] -C [dir] # to specific dir

# compress archive with tar
tar -czvf [archive] [dir] # gzip
tar -cjvf [archive] [dir] # bzip2

# gzip
gzip [dir]
gunzip [archive]

# bzip2
bzip2 [dir]
bunzip2 [archive]

# create at archive based on ls command output
ls | cpio -o > [archive]

# extract cpio archive 
cpio -id < [archive]
-i # extract
-d # create destination folder

# copy data from one location to another
dd if=[source] of=[destination]

# display dd progress
dd status=progress if=[source] of=[destination]

```

## 103.4: Use streams, pipes and redirects [4]
```bash
# file descriptors
0 /dev/stdin  # stdin
1 /dev/stdout # stdout
2 /dev/stderr # stderr

# redirect stdin
[command] > [destination]
[command] 1> [destination]
cat /proc/cpu_info > cpu.txt # example

# redirect stderr
[command] 2> [destination]
cat /proc/cpu_info 2> err.txt # example

# redirect stderr to stdin and vice versa
[command] 2>&1
[command] 1>&2

# get rid of error messages
[command] 2>/dev/null

# set noclobber parameter (no override existing files)
set -o noclobber

# redirect stdin to command
[command] < [file]
[command] 0< [file]
uniq -c < error.txt # example

# write text to file using heredoc
cat > [file] << EOF
line 1
line 2
EOF

# write text to file using herestring
cat > [file] <<<"string"

# redirect output to file and display it 
[command] | tee [file]
grep "model name" /proc/cpu_info | tee cpu_model.txt # example

# reditect both stdout and stderr to tee
[command] 2>&1 | tee [file]
make 2>&1 | tee log.txt # example

# command substitution
`[command]`
$([command])
mkdir `date +%Y-%m-%d` # example
mkdir $(date +%Y-%m-%d) # example

# xargs
[command] | xargs [command]
find . -name "*.iso" | xargs du -h # example 
find . -name "*.iso" -print0 | xargs -0 du -h # example
cat names.txt | xargs -I {} echo "hello {}!" # example
```

## 103.5: Create, monitor and kill processes [4]
```bash
# display jobs
jobs
jobs -l # PID
jobs -p # PID
jobs -r # running
jobs -s # suspended
jobs -n # status changed

# select job
jobs %[n]    # by id
jobs %[str]  # starts with string
jobs %?[str] # contains string
jobs %+      # current job
jobs %%      # currten job
jobs %-      # previous job

# background, foreground and kill jobs
fg %[n]      # foreground by id
bg %[n]      # background by id
[command] &  # run command in the background
kill %[n]    # kill job by id

# detached jobs
nohup [command] &

# execute a program periodically
watch -n [sec] [command]
watch -n 5 free   # example 
watch -n 2 uptime # example

# find process by name
pgrep [str]

# kill process by name
pkill [str]

# kill all instances of the same process by name
killall [str]

# kill a process by ID
kill [signal] [ID]
kill -SIGHUP 1337   # example 
kill -1 1337        # example 
kill -s SIGHUP 1337 # example

# SIGHUP (15) - instructs the process to terminate gracefully
# SIGKILL (9) - instructs the kernel to terminate the process
# SIGTERM (1) - sent when termianl session that started the
#               process is terminated or hung up, up to the
#               process what to do, usually reload config

# top
top
# M - sort by memory usage
# N - sort by PID number
# T - sort by running time
# P - sort by percentage of CPU usage
# R - switche between descending and ascending order

# h - display help
# ? - display help
# k - kill a process
# r - renice a process
# u - list process of a particular user
# c - show programs' absolute path, indicate user/kernel space
# V - hierarchy view of processes
# t - display CPU usage bars, hide, bring back
# m - display MEM usage bars, hide, bring back
# W - save configuration settings

# ps
ps
# p - show process by PID
# u - user-oriented format
# a - processes attached to a tty or terminal
# x - processes not attached to a tty or terminal

# BSD format : no dashes [ps aux]
# UNIX format: dashes [ps -u user]
# GNU format : double dashes [ps --pid 1337]

# Screen
screen           # start screen
screen -t [name] # create a windows with a name
screen -ls       # list sessions
screen -S [name] # create a new session
screen -S [PID | name] -X quit # kill a session
screen -r [PID | name] # reattach a session

ctrl+a w   # view all windows
ctrl+a c   # create a new window
ctrl+a A   # rename window
ctrl+a n   # go to next window
ctrl+a p   # go to previous window
ctrl+a [N] # go to window number N
ctrl+a \"  # see the list of all windows
ctrl+a k   # kill window
ctrl+a S   # split horizontally
ctrl+a |   # split vertically
ctrl+a tab # move between regions
ctrl+a Q   # terminate all regions except current one
ctrl+a X   # terminate current region
ctrl+a d   # detach session
ctrl+a [   # enter copy mode
ctrl+a ]   # paste

/etc/screenrc # system-wide screen config file
~/.screenrc   # user-level screen config file

# screenrc sections
SCREEN SETTINGS    # general settings
SCREEN KEYBINDINGS # keybindings
TERMINAL SETTINGS  # terminal windows sizes and buffers
STARTUP SCREENS    # define starup screens

# TMUX
tmux # start tmux session

# create new named session with named window
tmux new -s [session_name] -n [window_name]

# view sessions
tmux ls

# kill session
tmux kill-session -t [name]

# attach session
tmux a -t [name]

# supply config file to start tmux with
tmux -f [config_file]

ctrl+b c   # create new window
ctrl+b ,   # rename window
ctrl+b w   # display all windows
ctrl+b n   # go to next window
ctrl+b p   # go to previous window
ctrl+b [N] # go to windows number N
ctrl+b &   # kill window
ctrl+b f   # find window by name
ctrl+b .   # change window index number
ctrl+b \"  # split window horizontally
ctrl+b %   # split window vertically
ctrl+b x   # destroy current pane
ctrl+b ;   # move to last active pane
ctrl+b {   # swap panes (current to previous)
ctrl+b }   # swap panes (current to next)
ctrl+b z   # zoom in/out panel
ctrl+b t   # display a fancy clock
ctrl+b !   # turn pane into window
ctrl+b s   # list sessions
ctrl+b $   # rename session
ctrl+b D   # select what client to detach
ctrl+b r   # refresh client's terminal
ctrl+b [   # enter copy mode
ctrl+b ?   # view key bingings
ctrl+b [arrow] # move between panes
ctrl+b ctrl+[arrow] # resize pane by one line
ctrl+b alt+[arrow]  # resize pane by 5 lines

/etc/tmux.conf # system-wide tmux config file
~/.tmux.conf   # user-level tmux config file

```

## 103.6: Modify process execution policies [2]
```bash
# display process priority
grep ^prio /proc/[ID]/sched

# display process priorities using ps
ps -el
ps -Al

# run a process specifying its priority
nice [command] # default nice value 10
nice -n [num] [command]

# change the nice value of a process
renice [num] -p [PID]
renice -g [group] # all processes of a group
renice -u [user]  # all processes of a user
```

## 103.7: Search text files using regular expressions [3]
```bash

```

## 103.8: Basic file editing [3]
```bash
# open vi and go to line
vi +[num] [file]

# Normal mode commands
0, $  # go to beginning/end of the line
1G, G # go to beginning/end of document
(,)   # go to beginning/end of the sentence
{,}   # go to beginning/end of the paragraph
w,W   # jump word, jump word including punctuation
e,E   # go to end of current word
/,?   # search forward/backward
i,I   # insert mode before cursor, at the beginning of line
a,A   # intert mode after cursor, at the end of line
o,O   # add new line below/above
s,S   # erase character/line and enter insert mode
c     # change character(s) under cursor
r     # replace character under cursor
x     # delete character under cursor
v,V   # start new selection with current character/line
y,yy  # yank character/line
p,P   # paste after/before
u     # undo last action
^-R   # redo last action
ZZ    # close and save
ZQ    # close and not save

# execute command number of times
[num][command]
3yy  # yank 3 lines
99dd # delete 99 lines

# record a macro
q[key] # start recording macro
q      # stop recording macro
qa     # record macro in register "a"

@[key] # play macro stored at register
@a     # play macro stared at register "a"

# store macro in .vimrc
echo "let @[key] = '[macro]'" >> .vimrc

# colon commands
:s/REGEX/TEXT/g # replace all occurences of REGEX with TEXT
:!              # run a shell command
:quit  :q       # exit the program
:quit! :q!      # exit the program without saving
:wq             # save and quit
:exit :x :e     # save and exit
:visual         # go back to navigation mode

```

## 104.1: Create partitions and filesystems [2]
```bash
# MBR - old partitioning style, partition table stored on the
#       first sector of a disk (Boot Sector), with bootloader
#       no disks larger than 2TB, max 4 primary partitions
#       extented partition can be used as a container to 
#       store logical partitions

# GPT - modern partitioning style, no practical limit to the
#       disk size, number of partitions limited by OS

# fdisk
fdisk [device]
p # print current partition table
n # create new partition
F # show unallocated space
d # delete a partition
t # change partition type
l # list all partition types
w # write changes to disk

# gdisk
gdisk [device]
p # print current partition table
n # create new partition
d # delete a partition
t # change partition type
l # list all partition types
w # write changes to disk
s # sort partitions
r # enter recovery mode
  b # rebuild main GPT header using backup
  c # load backup partition table from disk
  d # rebuild backup GPT header using main
  e # load main partition table from disk
  f # convert MBR to GPT
  g # convert GPT to MBR

# create a file system
mkfs.[filesystem] [target]
mkfs.ext4 /dev/sda # example

mk2fs -t [filesystem] [target]
mk2fs -t ext4 /dev/sda

# mk2fs command line parameters
-b [size]      # size of data blocks, 1024, 2048 or 4096
-c -c          # check target device for bad blocks, thourough
-d [directory] # copy contents of a dir to root of new FS
-F -F          # force, force on mounted or in use device
-L [label]     # set label, max 16 chars
-n             # simulate, print parameters of FS
-q             # do not produce output
-U [ID]        # set UUID
-V             # verbose

# XFS
xfsprogs # tools for managing XFS

# create XFS file system
mkfs.xfs [target]

# mkfs.xfs options
-b size=[value] # set block size, 4KB-64KB
-m crc=[value]  # enable/disable CRC32c checks
-m uuid=[value] # set partition UUID
-f              # force creation of FS even if other FS present
-l logdev=[dev] # put log section on specified device
-l size=[value] # set size of log section
-q              # do not print parameters of FS being created
-L [label]      # set label, max 12 chars long
-N              # simulate, print parameters of FS 

# FAT16 - 4GB vol, 2GB file 
# FAT32 - 2PB vol, 4GB file
# VFAT  - support file names up to 255 chars

# create FAT file system
mkfs.fat [target]
mkfs.vfat [target]

# mkfs.fat options
-c        # check target device for bad blocks
-F [size] # set size of FAT, 12, 16 or 32 bit
-n [name] # set name of the FS, up to 11 chars
-v        # verbose
-C [filename] [block_count]
          # create file and then create FAT FS on it
	      # effectively create en empty disk image

# exFAT - addresses vol/file limitations of FAT32
#       - vol up to 128 PB, file up to 16 exabytes

# create exFAT filesystem
mkfs.exfat [target]
mkexfatfs [target]

# mkfs.exfat options
-i [vol_id]  # set volume ID
-n [name]    # set volume label
-p [sector]  # specify first sector of the first partition
-s [sectors] # num of sectors per cluster of allocation

# Btrfs - modern FS, including multiple device support
#         (striping, mirroring, striping+mirroring)
#         and many features like transparent compression,
#         SSD optimizations, incremental backups, snapshots,
#         online defragmentation, offline checks, subvolumes
#         with quotas, deduplication and much more.
#         as a copy-on-write FS it is very resilient

# create a btrfs FS
mkfs.btrfs [device] [...]

# mkbtrfs options
-L [label]  # set FS label
-m [option] # specify type of storage array, options are:
            # raid1, raid5, raid6, raid10, single, dup

# create a btrfs subvolume
btrfs subvolume create [path]
# creates "backup" subvolume on FS mounted under /mnt/disk
btrfs subvolume create /mnt/disk/backup # example

# show subvolime information
btrfs subvolume show [path]

# mount a subvolume
mount -t btrfs -o subvol=[name] [device] [mountpoint]
mount -t btrfs -o subvol=backup /dev/sda1 /mnt/backup

# snapshots - just like subvolumes but with contents
#             from the snapshotted volume

# Create snapshot
btrfs subvolume snapshot [vol_path] [snap_path]
btrfs subvolume snapshot /mnt/disk /mnt/disk/snap

# create read-only snapshot
btrfs subvolume snapshot -r [vol_path] [snap_path]

# compression - btrfs supports transparent compression
#   which is done automatically on per-file basis,
#   as long as the file system is mounted with 
#   -o compress option. Compression algorithms available:
#   ZLIB - default
#   LZO  - faster, worse compression ratio
#   ZSTD - faster than ZLIB, comparable compression ratio

# GNU Parted - modern, robust partition editor
parted [device]

# parted commands
select [device] # switch to a different device
print           # print disk/partition information
print devices   # list all block devices on the system
print all       # print info about each device
print free      # print free space on device
mklabel [type]  # create partition table

# Create partition with parted
mkpart [part_type] [fs_type] [start] [end]
part_type # primary, logical, extended
fs_type   # specify FS type
start     # point on the device where partition begins
end       # point on the device where partition ends

mkpart primary ext4 1m 100m # example

# remove partition
rm [num]

# recover deleted partition
rescue [start] [end]
rescue 90m 210m # example
# note: FS must be present, empty partitions are not detected

# resize partitions
resizepart [part_num] [end]
resizepart 3 350m # example

# resize file system
resize2fs [device] [size]
resize2fs /dev/sda 150M # example
resize2fs /dev/sda      # takes all available space
resize2fs /dev/sda -M   # size just enough for stored files

# Swap partitions
# fdisk: t -> 82
# gdisk: t -> 8200
# parted:
mkpart primary linux-swap [start] [end]

# make swap partition
mkswap [device]
mksawp /dev/sda1 # example

# enable swap on partition
swapon [device]
swapon /dev/sda1 # example

# disable swap on partition
swapoff [device]
swapoff /dev/sda/1 # example

# Create a swap file
dd if=/dev/zero of=[file_path] bs=[size] count=[num]
dd if=/dev/zero of=swapfile bs=1M count=1024 # example

mkswap [swap_file]
swapon [swap_file]

```

## 104.2: Maintain the integrity of filesystems [2]
```bash
# Disk Usage - du
du        # count 1KB blocks in current dir, recursively
du -h     # human readable
du -ah    # view files too, not only dirs
du -S     # count total excluding subdirs
du -Sc    # count total excluding subdirs, show grand total
du -d [N] # specify how deep to look
--exclude=[pattern] # exclude pattern when counting

# Disk Free - df
df        # show summany of mounted filesystems
df -h     # human readable
df -i     # show inodes instead of blocks
df -T     # display type of each filesystem
df -x [fs_type] # exclude filesystem of specified type
df -t [fs_type] # show only specified filesystems
--output=[fields] # customize output by selecting fields
source # device corresponding to filesystem
fstype # filesystem type
size   # total size of filesystem
used   # used space
avail  # available space
pcent  # usage percentage
target # mountpoint of filesystem
itotal # total number of inodes in the filesystem
iused  # number of used inodes in the filesystem
iavail # number of available inodes in the filesystem
ipcent # percentage of used inodes in the filesystem

# Filesystem Check - fsck
fsck [device] # perform fs check, fix errors
fsck -t # specify filesystem type
fsck -A # check all filesystems in /etc/fstab
fsck -C # display progress bar, ext2/3/4 only
fsck -N # print what would be done
fsck -R # skip root filesystem, used with -A
fsck -V # verbose
fsck -p # attempt to fix found erros, don't ask
fsck -y # answer yes to every question
fsck -n # answer no to every question
fsck -f # check FS even if its's marked as clean

# Fine tuning filesystems - tune2fs
tune2fs -l [path]  # list filesystem parameters
tune2fs -l /dev/sda1 # example
tune2fs -c [N]     # set max mount count
tune2fs -C [N]     # set mount count value
tune2fs -i [x]     # set FS check interval , d,m or y
tune2fs -L [label] # set label of filesystem
tune2fs -U [ID]    # set UUID of filesystem
tune2fs -e [behavior] # set behavior when errors detected
	continue       # continue execution normally
	remount-ro     # remount filesystem as read-only
	panic          # cause a kernal panic
tune2fs -j [path]  # convert ext2 to ext3 (add journal)
tune2fs -J [param] # set journal options
	size=[value]   # set journal size (MB)
	location=[loc] # set journal location
	device=[dev]   # store journal on different device
tune2fs -f         # force, complete despite errors

# Maintaining XFS filesystems - xfsprogs
xfs_repair [device]    # scan and repair filesystem
xfs_repair -n          # scan but do not repair
xfs_repair -l [logdev] # specify log device of FS
xfs_repair -r [rtdev]  # specify realtime section device
xfs_repair -m [N]      # set max MB of memory used
xfs_repair -d          # enable repair of FS mounted RO
xfs_repair -v          # verbose
xfs_repair -L          # zero-out corrupt log

xfs_db [path]          # debug XFS filesystem
xfs_db                 # interactive mode

xfs_fsr                # reorganize XFS filesystem
                       # all listed in /etc/mtab

```

## 104.3: Control mounting and unmounting of filesystems [3]
```bash
# Mount filesystem 
mount -t [type] [device] [mountpoint]
mount -t ext4 /dev/sda1 /mnt/disk

# list all mounted filesystems
mount

# list all mounted filesystems of specified type
mount -t [type]
mount -t exfat     # exmaple
mount -t ext2,ext3 # example
# output: SOURCE on TARGET type TYPE OPTIONS

mount -a # mount all filesystems in /etc/fstab
mount -o # specify mount options
mount -r # mount FS as read-only
mount -w # mount FS as writable

# Unmount filesystem
umount [device] or [mountpoint]
umount /dev/sda1 # example
umount /mnt/disk # example

umount -a # unmount all filesystems listed in /etc/fstab
umount -f # force unmounting of filesystem
umount -r # if FS cannot be unmounted, make it read-only

# view open files on filesystem
lsof [device]
lsof /dev/sda1 # example

# /etc/fstab - contains descriptions of FS mounted on boot
FILESYSTEM # device containing FS to be mounted
MOUNTPOINT # where the filesystem will be mounted
TYPE       # the filesystem type
OPTIONS    # mount options for the filesystem
DUMP       # if should be backed up by dump command
PASS       # order in which will be checked on bootup

# boot options
atime    # update access time on read
noatime  # do no update access time on read
auto     # can be mounted automatically with mount -a
noauto   # cannot be mounted automatically with mount -a
defaults # rw, suid, dev, exec, auto, nouser, async, mount
dev      # interpret character and block devices
nodev    # do not interpret character and block devices
exec     # allow execution of binaries in FS
noexec   # disallow execution of binaries in FS
user     # allow ordinary user to mount FS
nouser   # disallow ordinary user to mount fS
group    # user can mount if member of group which owns device
owner    # user can mount if he owns the device
suid     # allow SETUID and SETGID bits to take effect
nosuid   # disallow SETUID and SETGID bits to take effect
ro       # mount read-only
rw       # mount read-write
remount  # attempt to remount already mounted FS
sync     # do I/O operations synchronously
async    # do I/O operations asynchronously

# view device UUID
lsblk -f [device]

# create /etc/fstab entry with UUID
UUID=[ID]  /  ext4  defaults 0 0

# create /etc/fstab entry with label
LABEL=[label] / ext4 defaults 0 0 

# mount FS by UUID using mount
mount -t [type] UUID=[ID] [mountpoint]

# Mounting disks with systemd
# systemd can be used to mount filesystems by creating
# a mount unit and placing it in /etc/systemd/system/

# .mount file example:
# ------- external.mount -------- #
[Unit]
Description=External data disk

[Mount]
What=/dev/disk/by-uuid/56C11DCC5D2E1334
Where=/mnt/external
Type=ntfs
Options=defaults

[Install]
WantedBy=multi-user.target
# -------------------------------- #
Description # description of mount unit
What        # volume to be mounted
Where       # mountpoint
Type        # filesystem type
Options     # mount options to pass
WantedBy    # target to mount the disk with

# NOTE: The .mount file must have the same name as mountpoint
#       /mnt/external --> mnt-external.mount

# check mounting status
systemctl status mnt-external.mount

# mount the disk for current session
systemctl start mnt-external.mount

# mount the disk on bootup
systemctl enable mnt-external.mount

# automount mount unit whenever mount point is accessed
# create an .automount file alongside the .mount one
# --------- etc-external.automount ---------- #
[Unit]
Description=Automount the external data disk

[Automount]
Where=/mnt/external

[Install]
WantedBy=multi-user.target
# ------------------------------------------- #
Description # description of automount
Where       # mountpoint
WantedBy    # target to mount the disk with

# reload systemd
systemctl daemon-reload

# start the .automount unit
systemctl start mnt-external.automount

# enable the .automount unit
systemctl enable mnt-external.automount

```

## 104.5: Manage file permissions and ownership [3]
```bash
# view file permissions
ls -l [file]

# view directory permissions
ls -l -d [directory]

# view permissions of hidden files
ls -la

## Filetypes
- # normal file
d # directory
l # symbolic link
b # block device
c # character device
s # socket

# permissions
r (4) # read
w (2) # write
x (1) # execute

# modify file permissions
chmod [ugo][+-=][rwx] [file]
chmod [octal] [file]

# modify permissions recursively
chmod -R [perms] [directory]

# modify file ownership
chown [user] [file]
chown [user]: [file]
chown [user]:[group] [file]
chown :[group] [file]
chgrp [group] [file]

# view groups on the system
getend group

# view groups of a user
groups [user]

# view users in a group
groupmems -g [group] -l

# view umask value
umask

# temporarily change umask value
umask [perms]

# set sticky bit
chmod +t [directory]
chmod 1[perms] [directory]

# unset sticky bit
chmod -t [directory]
chmod 0[perms] [directory]

# set/unset SGID
chmod g+s [file]
chmod g-s [file]

# set/unset SUID
chmod u+s [file]
chmod u-s [file]

```

## 104.6: Create and change hard and symbolic links [2]
```bash
## Symbolic link
#  point to path of another file
#  when file is deleted the link break as it points to nothing

## Hard link
#  additional entry in FS poiting to the same inode
#  deleting the original entry does not break a hard link

# Create hard link
ln [target] [link_name]

# Create symbolic link
ln -s [target] [link_name]

# delete hard/soft links
rm [link]

# move hard/soft links
mv [link]

# Note that moving soft links may break them if they use
# a relative path to point to the target
ln -s target.txt link.txt # bad
ln -s /home/user/target.txt link.txt # good

```

## 104.7: Find system files and place file in the correct location [2]
```bash
# Filesystem Hierarchy Standard (FHS)
/      # topmost directory in the hierarchy
/bin   # essential binaries, for all users
/boot  # files needed by the boot process
/dev   # device files
/etc   # host-specific configuration files
/home  # users' home directories
/lib   # shared libraries
/media # user-mountable removable media
/mnt   # mount point for temporarily mounted FS
/opt   # application software packages
/root  # home directory of root user
/run   # run-time variable data
/sbin  # system binaries
/srv   # data served by the system, ex. webpage
/tmp   # temporary files
/usr   # read-only user data
/proc  # virtual FS with data of running processes
/var   # variable data written during system operation

# Temporary file locations
/tmp     # cleared on each boot
/var/tmp # not cleared on bootup
/run     # must be cleared on bootup

# Finding files - find
find [where] [what]

# find programs by name
find [where] -name [pattern]
find . -name "*.jpg" # example

# find programs by name - case insensitive
find [where] -iname [pattern]
find . -iname "*.iso" # example

# specify max depth of search
find [where] [what] -maxdepth [N]
find . '*.txt' -maxdepth 1 # example

# specify min depth of search 
find [where] [what] -mixdepth [N]
find . '*.txt' -mindepth 3 # example

# Specify filesystem type to search
find [where] [what] -fstype [type]
find . '*.txt' -fstype exfat # example

# Do not search mounted filesystems
find [where] [what] -mount
find . '*.txt' -mount # example

# Search for attributes
find [where] [attr]
-user [username]   # files owned by user
-group [groupname] # files owned by group
-readable          # readable by current user
-writable          # writable by current user
-executable        # executable by current user
-perm [-]XXXX      # files with specified permissions
                   # - at least specified permissions
-empty             # empty files and directories
-size [+-][N]      # files of specified size
                   # - smaller files, + bigger files

# Search by time
find [where] [time]
-amin [+-][N]  # accessed N minutes ago
-cmin [+-][N]  # attributes changed N minutes ago
-mmin [+-][N]  # modified N minutes ago
-atime [+-][N] # accessed N days ago
-ctime [+-][N] # attributes changed N days ago
-mtime [+-][N] # modified N days ago

# locate and updatedb
updatedb             # update locate database
locate [pattern]     # search for pattern
locate -i [pattern]  # search for pattern, case-insensitive
locate -A [patterns] # match multiple patterns
locate -c [pattern]  # count files
locate -e [pattern]  # verify file exist before printing it
locate jpg    # example
locate -i iso # example

/var/lib/mlocate.db # location of locate database
/etc/updatedb.conf  # locate database config

# updatedb configuration options
PRUNEFS=           # FS types not to scan 
PRUNENAMES=        # dir names not to scan
PRUNEPATHS=        # paths not to scan
PRUNE_BIND_MOUNTS= # yes/no - ignore mount --bind dirs

# Find full path to executable - which
which [query]
which -a [query] # show all pathnames

# Show information about a binary - type
type [query]
type -a [query] # show all pathnames
type -t [query] # show just the type

# Find binaries, man pages, source code - whereis
whereis [query]
whereis -b [query] # show only binaries
whereis -m [query] # show only man pages
whereis -s [query] # show only source code

```
