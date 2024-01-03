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

## 106.1: Customize and use shell environment
```bash
# Shell types
interactive     # user interaction, reads conf files
non-interactive # no user interaction, reads env vars
login           # reads configuration scripts
no-login        # does not read config scritps

# Open TTY
ctrl+alt+f1-6   # open TTY when using GUI
ctrl+alt+f7     # go back to GUI from TTY

# Launching shells with bash
bash --login         # invoke a login shell
bash -l              # invoke a login shell
bash -i              # invoke an interactive shell
bash --noprofile     # ignore config files
bash --norc          # ignore .bashrc files
bash --rcfile [file] # specify .bashrc file

# start interactive login shell with su
su - [user]
su -l [user]
su --login [user]
su - # root

# start interactive no-login shell with su
su [user]
su # root

# start interactive login shell with sudo
sudo su - [user]
sudo su -l [user]
sudo su --login [user]
sudo su - # root
sudo -i # root
sudo -i [comand] # run command and exit

# start interactive no-login shell with sudo
sudo su [user]
sudo -u [user] -s
sudo su # root
sudo -s # root

# find out what shell you're working at
echo $0
# results
-bash or -su      # interactive login
bash or /bin/bash # interactive no-login
name_of_script    # non-interactive no-login

# find out how many bash shells are running
ps aux | grep bash

# shell configuration files
/etc/profile # sets a number of variables such as PATH 
             # and PS1, sources /etc/bash.bashrc and 
             # files in /etc/profile.d/

/etc/profile.d/* # has scripts sourced by /etc/profile

~/.bash_profile # bash specific file used to configure
                # user environment, sources both
                # ~/.bash_login and ~/.profile

~/.bash_login # bash specific, only executed if there's
              # no ~/.bash_profile, run at login

~/.profile # not bash specific, sourced when neither
           # ~/.bash_profile nor ~/.bash_login exit
           # checks if bash shell is running and 
           # sources ~/.bashrc if it exists. Usually
           # sets PATH to include ~/bin if exists
  
~/.bash_logout # does clean-up operations on logoff

# bashrc files
/etc/bash.bashrc # customizes bash environment, makes
                 # sure bash is run interactively
                 # checks window size after each
                 # command and sets some variables

~/.bashrc # carries tasks of /etc/bash.bashrc at
          # user level, sets some history variables
          # sources ~/.bash_aliases if exists.
          # stores users' aliases and functions

# sourcing files
. [file]
source [file]

# SKEL - a home directory template
/etc/skel

# create a local variable
[var_name]=[value]
	# names may contain: a-z A-Z 0-9 _
	# values may contain: a-z A-Z 0-9, most other chars
	# values must be in quotes if contain spaces, 
	# redirection chars < > or pipe symbol |
	# single quotes '' -> literal string
	# double quotes "" -> variable substitution
	# exclamation marks ! must be last character
	# backslashes \ must be escaped with backslashes

# reference a variable
$[var_name]
"$[var_name]" # if contains initial/extra spaces

# create a readonly variable
readonly [var_name]=[value]

# make variable readonly
readonly [var_name]

# list readonly variables
readonly
readonly -p

# list all currently assigned vars and functions
set 

# check if variable is declared
set | grep [var_name]

# delete a variable
unset [var_name]

# create a global variable
export [var_name]=[value]

# make variable global
export [var_name]

# make global variable local
export -r [var_name]

# list global variables
export
export -p
declare -x
env
printenv

# view value of a variable
echo $[var_name]
printenv [var_name]

# run command with as empty environment as possible
env -i [comand]

# set particular variable for particular program
env [var_name]=[value] [script]
[var_name]=[value] [script]

env BASH_ENV=/root/.startup.sh ./script.sh # example

# common environment variables
DISPLAY      # X server info
HISTCONTROL  # controls commands saved into HISTFILE
	ignorespace # commands starting with space
	ignoredups  # commands the same as previous one
	ignoreboth  # any of the above
HISTSIZE     # number of commands stored in history
             # while session is running, in memory
HISTFILESIZE # number of commands stored in history
             # in the HISTFILE
HISTFILE     # name of file where history is stored
HOME         # absolute path to current user's home dir
HOSTNAME     # stores TCP/IP name of the system
HOSTTYPE     # stores architecture of the system
LANG         # stores the locale of the system
LD_LIBRARY_PATH # list of directories with libraries
MAIL         # file where bash searches for email
MAILCHECK    # mail check frequency in seconds
PATH         # list of dirs with executables
PS1          # value of bash prompt
PS2          # prompt for multiline commmands >
PS3          # prompt for the select command
PS4          # prompt for debugging +
SHELL        # absolute path to the current shell
USER         # name of the current user

# create an alias
alias [alias_name]=[command]
alis ls="ls --color=auto" # example

# create an alias containing multiple commands
alias [alias_name]=[command];[command];[...]
alias git_info="which git; git --version"

# remove an alias
unalias [alias_name]

# escape an alias
\[command]
\ls # example

# Dynamic expansion of variables in aliases
# the value read when executing an alias
alias [alias_name]='$var'

# Static expansion of variables in aliases
# the value read when creating an alias
alias [alias_name]="$var"

# alias declaration files
.bashrc
.bash_aliases

# create a function
function [function_name] { ... }
[function_name]() { ... }

# bash built-in variables
$?      # result of last command, 0 -> success
$$      # shell PID
$!      # PID of the last background job
$#      # number of args passed to a command
$_      # last arg or the name of the script
$@ $*   # args passed to the command
$0 - $9 # args passed to a function, $0 - function name

# positional parameters in function
[function] arg1 arg2 ...
$1 -> arg1
$2 -> arg2

# remove a function
unset -f [function_name]

```

## 105.2: Customize and write simple scripts
```bash
# sheband
#![path_to_program]
#!/bin/bash # example

# execute a script with bash
bash [script]

# execute script as a program
chmod +x [script]
./[script]

# in scripts ; is the same as new line character so
[command1];[command2]
# is the same as 
[command1]
[command2]

# execute script in the current shell
# not in a sub-shell which is the default
. [script]
source [script]

# execute script or command and exit the shell
exec [script]

# declare a variable
[var_name]=[value]

# bash built-in variables
$* # all arguments passed to script
$@ # same as $*, if in "" all args will be in "" as well
$# # the number of args
$0 # the name of the script
$! # PID of the last executed program
$$ # PID of the current shell
$? # exit code of the last finished command

# positional parameters
$1 .. $9 ${10} ${11} ..

# read user input and store it in variable
read [variable]
read [var1] [var2]
read -p [prompt] [var]

# command substitution
`[command]`
$([command])

# get length of a variable
echo ${#[var_name]}
echo ${#name} # example

# declare an array
declare -a [arr_name]

# populate array with values
[arr_name]=( val1 val2 val3 ... )

# reference nth element of a variable
${[var_name][n]}
${numbers[0]} # first element of the 'numbers' variable

# assign array element
[var_name][n]=[val]
numbers[0]=1337 # example

# get length of nth element in an array
${#[var_name][n]}
${#names[0]} # example

# get number of elements in an array
${#[var_name][@]}
${#[var_name][*]}
${#names[@]} # example
${#names[*]} # example

# declare arrays using command substitution
[var_name]=( $([command]) )
FS=( $(cut -f 2 /proc/filesystems) ) # example

# arithmetic expressions
expr [value] [operator] [value]
SUM=`expr $val1 + $val2` # example

$(( [value] [operator] [value] ))
SUM=$(( $val1 + $val2 ))

# execute command only if the previous was successful
[command] && [command]

# execute command only if the previous failed
[command] || [command]

# if statements with test conditions
if test [param] [value] ; then
	[command]
fi

if [ [param] [value] ] ; then
	[command]
fi

# example - test if path is executable file
if [ -x /bin/bash ] ; then
	echo "hell yeah"
fi

# display messages with escaped sequences
echo -e [string]
echo -e "name\t$name\nsurname\t$surname" # example

# display messages using printf
printf [string]
printf "OS: %s, RAM: %d" $OS $FREE
# where %s is a placeholder for strings
# and %d is a placeholder for integers

# test
test [param] [value]
-a # if exits in filesystems and is a file
-b # if is a special block file
-c # if is a special character file
-d # if is a directory
-e # if exists in filesystem
-f # if exists and is a regular file
-g # if has SGID permission set
-h # if is a symbolic link
-L # if is a symbolic link (like -h)
-k # if has sticky bit permission set
-p # if is a pipe file
-r # if is readable by the current user
-s # if exists and is not empty
-S # if is a socket file
-t # if is open in terminal
-u # if has SUID permission set
-w # if is writable by the current user
-x # if is executable by the current user
-O # if is owned by the current user
-G # if belongs to the effective group of the current user
-N # if has been modified since the last time if was accessed

# comparing two variables
[var1] -nt [var2] # newer than according to modification dates
[var1] -ot [var2] # older than according to modification dates
[var1] -ef [var2] # one is a hard link to the other

# tests for arbitrary text variables
-z # if is empty
-n # if is not empty
[var1] = [var2]  # if variables are equal
[var1] == [var2] # if variables are equal
[var1] != [var2]  # if variables are not equal
[var1] < [var2]  # if var1 comes before var2 (alphabetical)
[var1] > [var2]  # if var1 comes after var2 (alphabetical)

# numerical comparisons
[num] [comparison] [num]
-lt # less than
-gt # greater than
-le # less than or equal
-ge # greater than or equal
-eq # equal
-ne # not equal

# test modifiers
! [expression]     # negation
[expr1] -a [expr2] # AND
[expr1] -o [expr2] # OR

# case
case [var] in [val1] | val2 | ... )
	[command]
	;; # ;; ;& or ;;&
	[val1] | [val2] | ... )
	[command]
	;; # ;; ;& or ;;&
esac

# toggle value settings controlling optional shell behavior
shopt -s # enable
shopt -u # disable

# nocasematch - case insensitive case pattern matching
shopt -s nocasematch # enable
shopt -u nocasematch # disable

# for loop
for [var_name] in [list]
do
	[command]
done

# for loop - C like parenthesis notation
for (( [init]; [condition]; [increment] ))
do
	[command]
done

# until loop
until [condition]
do
	[command]
done

# while loop
while [condition]
do
	[command]
done

```

## 106.1: Install and configure X11
```bash
# X server display name
hostname:displaynumber.screennumber
hostname # name of system where app will be displayed
displaynumber # collection of screens in use
screennumber  # number of the screen

# view display name of running X session
echo $DISPLAY

# start application on specific screen
DISPLAY=[host]:[display_num].[screen_num] [application] &
DISPLAY=:0.1 firefox & # example

# X server config files
/etc/X11/xorg.conf
/etc/X11/xorg.conf.d/*.conf
/usr/share/X11/xorg.conf.d/*.conf

# X server config file sections
InputDevice  # config specific model of keyboard or mouse
InputClass   # config a class of hardware devices, rather
			 # than a specific device
Monitor      # config physical monitor
Device       # describes physical PCI device
Screen       # ties Monitor and Device sections together
ServerLayout # groups all sections together

# Example /etc/X11/xorg.conf.d/00-keyboard.conf file:
Section "InputClass"
    Identifier "system-keyboard"
    MatchIsKeyboard "on"
    Option "XkbLayout" "us"    # keyboard layout
    Option "XkbModel" "pc105"  # keyboard type
EndSection

# Example Monitor section
Section "Monitor"
    Identifier "DP2"            # port where connected
    Option     "Primary" "true" # set to primary
EndSection

# Example Device section
Section "Device"
    Identifier  "Device0"    # ID
    Driver      "i915"       # kernel module
    BusID       "PCI:0:2:0"  # location on PCI bus
EndSection

# Example Screen section
Section "Screen"
    Identifier "Screen0"  # ID
    Device     "Device0"  # identifies Device
    Monitor    "DP2"      # identifies Monitor
EndSection

# Example ServerLayout section
Section "ServerLayout"
	Identifier   "Layout-1" # ID
	Screen       "Screen0" 0 0 # Screen
	InputDevice  "mouse1" "CorePointer" # Mouse
	InputDevice  "system-keyboard" "CoreKeyboard" # Keyboard
EndSection

# modify keyboard layout on running X session
setxkbmap -model [model] -layout [layout]
setxkbmap -model chromeboQwEtGbzxC312ok -layout "gr(polytonic)" # example

# modify keyboard layout using localectl
localectl --no-convert set-x11-keymap [layout] [model]
--no-convert # prevents modification of host's console keymap

# display info about running X server instance
xdpyinfo

# generate a xorg.conf file
Xorg -configure
Xorg :[N] -configure # specify display number
X -configure         # X is symlinc to Xorg

# Wayland - newer display protocol designed to replace X11.
# It's more efficient and more secure.
# no server instance between the client and kernel
# Wayland compositor handles dev input, windows management
# and composition. 
# XWayland - X server that runs within Wayland to render 
#            application that does not support Wayland yet

# view Wayland display variable
echo $WAYLAND_DISPLAY

```

## 106.2: Graphical Desktops
```bash
# Popular Desktop Environments
# Gnome:    Fedora, Debian, Ubuntu SLE, RHEL, CentOS
# KDE:      openSUSE, Mageia, Kubuntu
# Xfce:     aestically pleasing by lightweight DE
# LXDE:     focused on low resource consumption
# MATE:     fork of Gnome 2
# Cinnamon: fork of Gnome 3

# Desktop interoperability - shared specifications of DEs
# Directories locations
# Desktop entries
# Application autostart
# Drag and Drop
# Trash Can
# Icon themes

# Remote desktop sessions
# XDMCP (X Display Manager Control Protocol)
	# native to X11, high bandwidh usage, low security
# VNC (Virtual Network Computing)
	# platform independent
	# uses Remote Frame Buffer protocol (RFB)
	# dow not provide encryption and authentication natively
# RDP (Remote Desktop Protocol)
	# mainly used to access Windows systems
	# uses proprietary Microsoft's RDP protocol.
# SPICE
	# (Simple Protocol for Independent Computing Environments)
	# ability to integrate local and remote systems:
	# - access local devices
	# - file sharing between devices
```

## 106.3: Accessibility
```bash
# Accessibility settings
# Gnome: Universal Access
# KDE: System Settings -> Personalization -> Accessibility
# Xfce: Accessibility

# Keyboard accessibility settings
# Sticky keys: type keyboard shortcuts one key at a time
# Bounce keys: new key press accepted after specified time
# Slow keys: hold key for specified time before accepted
# Mouse keys: control mouse cursor using numpad

# Configure slow, sticky, bounce and mouse keys from CLI
xkbset

# Screen keyboard: allows typing with a mouse
# KDE screen keyboard package is "onboard"

# Mouse accessibility settings
# double-click interval
# click events simulation

# Visual accessibility
# High contrast
# Large text
# Cursor size
# Screen magnifier (Zoom, KMagnifier)

# Screen reader (Orca)
# Refreshable Braille displays

```

## 107.1: Manage user and group accounts and related system files
```bash
# add user
useradd [user]
-c # comment
-d # home directory
-e # expiration date
-f # number of days after which password expires
-g # primary group
-G # secondary groups
-k # custom skel
-m # create home directory
-M # do not create home directory
-s # login shell
-u # custom UID

# modify user
usermod [option] [user]
-c # comment
-d # home directory
-e # expiration date
-f # number of days after which password expires
-g # primary group
-G # secondary groups
-l # login name
-L # lock
-s # login shell
-u # UID
-U # unlock

# change password of a user
passwd [user]

# delete user account
userdel [user]
userdel -r [user] # remove homedir

# add group
groupadd [group]
groupadd -g [ID] [group] # specify GID

# rename group
groupmod -n [new_name] [group]

# change group GID
groupmod -g [ID] [group]

# delete group
groupdel [group]

# skeleton directory
/etc/skel

# login definitions
/etc/login.defs
UID_MIN         # min UID number
UID_MAX         # max UID number
GID_MIN         # min GID number
GID_MAX         # max GID number
CREATE_HOME     # whether to create home dir by default
USERGROUPS_ENAB # if create new groups for each new user
MAIL_DIR        # mail spool directory
PASS_MAX_DAYS   # max number of days password can be used
PASS_MIN_DAYS   # min number of days between password changes
PASS_MIN_LEN    # min acceptable password length
PASS_WARN_AGE   # warning days before password expires

# passwd
passwd
-d # delete user password
-e # expire user password
-i # number of inactive days
-l # lock user account
-n # minimum password lifetime
-S # show password status
-u # unlock user account
-x # maximum password lifetime
-w # warn days before password expires 

# chage
chage
-d # last password change
-E # expiration date
-I # number of inactive days
-m # minimum password lifetime
-M # maximum password lifetime
-W # warn days before password expires

```

## 107.2: Automate system administration tasks by scheduling jobs
```bash
# user contabs location
/var/spool/cron/

# system crontabslocation
/etc/crontab
/etc/cron.d/*
/etc/cron.hourly
/etc/cron.daily
/etc/cron.weekly
/etc/cron.monthly

# .---------------- minute (0 - 59)
# |  .------------- hour (0 - 23)
# |  |  .---------- day of month (1 - 31)
# |  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ..
# |  |  |  |  .---- day of week (0 - 6) OR mon,tue,wed ..
# |  |  |  |  |
# *  *  *  *  * user-name command to be executed

* # any value
, # list of specific values
- # range of possible values
/ # stepped values

# time specifications
@reboot
@hourly
@daily
@midnight
@weekly
@monthly
@yearly
@annually

# crontab variables
HOME   # dir where cron invokes commands
MAILTO # username or address where errors will be emailed
PATH   # path where commands can be found
SHELL  # shell to use

# manage crontab as a user
crontab -e # edit
crontab -l # list
crontab -r # remove

# manage other user's crontab
crontab -u [user]

# manage system crontab
vim /etc/crontab

# restrict access to job scheduling 
vim /etc/cron.allow
vim /etc/cron.deny

# schedule a job with systemd
# 1. create a .service unit
vim /etc/systemd/system/[name].service

[Unit]
Description=[description]

[Service]
Type=oneshot
ExecStart=[path]

[Install]
WantedBy=multi-user.target

# 2. create a timer unit
vim /etc/systemd/system/[name].timer

[Unit]
Description=[description]

[Timer]
OnCalendar=[DayOfWeek Year-Month-Day Hour:Minute:Second]

[Install]
WantedBy=timers.target

# 3. enable the timer
systemctl enable --now [timer]

# list all timers
systemctl list-timers
systemctl list-timemrs --all # include inactive

# special time expressions
hourly
daily
weekly
monthly
yearly

# schedule a one time job - interactive prompt
at [when]
-c # print commands of specific job ID
-d # delete job based on job ID
-f # read job from file
-l # list pending jobs of the user
-m # send mail to user at the end of the job
-q # specify queue
-v # show time at which job will be run

# list scheduled jobs
atq
at -l

# delete jobs
atrm [ID]
at -d [ID]

# restrict access to at
/etc/at.allow
/etc/at.deny

# time specifications
HH:MM                         # 09:15
month-name day-of-month       # january 20
month-name day-of-month year  # january 20 2025
MMDDYY                        # 012025
MM/DD/YY                      # 01/20/25
DD.MM.YY                      # 20.01.25
YYYY-MM-DD                    # 2025-01-20

# one-time jobs with systemd
systemd-run --on-calendar=[date] [command]
systemd-run --on-active=[time_passsed] [command]


```

## 107.3: Localization and internationalization
```bash
# display time
date
timedatectl

# timezone info file
/etc/timezone

# select timezone
tzselect

# timezone settings file
/etc/localtime

# all timezone settings files
/usr/share/zoneinfo/*

# check system locale
echo $LANG
cat /etc/locale.conf

# locale variables
LC_COLLATE  # alphabetical ordering
LC_CTYPE    # how to treat sets of characters
LC_MESSAGES # language of program messages
LC_MONETARY # money unit and currency format
LC_NUMERIC  # numerical format for non-monetary values
LC_TIME     # time and date format
LC_PAPER    # standard paper size
LC_ALL      # overrides all variables, including LANG

# show defined variables and their values
locale

# encoding convertion
iconv -f [encoding] -t [encoding] [file] > [outfile]

```


```

## 108.1: Maintain system time
```bash
# system time
date               # local
date -u            # UTC
date -I            # ISO 8601 format
date -R            # RFC 5322 format
date --rfc-3339    # RFC 3339 format
date +%s           # UNIX time
date --date=[date] # specify date to display
date --debug --date=[date] # debug date parsing

# hardware clock
hwclock            # display hardware clock time
hwclock --verbose  # verbose output

# get time info using timedatectl
timedatectl

# set system and hardware time
timedatectl set-time "YYYY-MM-DD HH:MM:SS"

# list timezones
timedatectl list-timezones

# set timezone
timedatectl set-timezone [timezone]

# disable NTP
timedatectl set-ntp no

# enable NTP
timedatectl set-ntp yes

# set timezone manually
/usr/share/zoneinfo # list of timezones
/etc/localtime      # link to timezone conf file
/etc/timezone       # text file with current timezone
ln -s /usr/share/zoneinfo/[timezone] /etc/localtime

# set hardware clock to system time
hwclock --systohc

# set system time to hardware clock
hwclock --hctosys

# set date and time manually
date --set=[date_str]
date [format] -s [date_str]
date +%Y%m%d -s "20111125" # example
date +%T -s "13:11:00" # example

# set hardware clock time
hwclock --set --date [date_str]

# NTP servers
Stratum 0 # the clocks themselves
Stratum 1 # servers connected to Stratum 0
Stratum 2 # servers connected to Stratum 1

# NTP terminology
Offset      # difference between system time and NTP time
Step        # if time offset between NTP provider and consumer
            # is greater than 128ms, a single significant
            # change will be performed, as opposed to 
            # slowing down or speedingthe system time.
Slew        # if the offset is below 128ms the changes 
			# are made gradually - as opposed to stepping.
Insane Time # Offset between system time and NTP time greater
			# than 17 minutes. NTP will not produce any changes
			# to the system time. Special steps are taken
			# to bring system time below 17 minute offset
Drift       # two clocks becoming out of sync over time
Jitter      # measure of variation in time between NTP
			# server responses to client requests

# timedatectl
systemd-timesyncd # service responsible for NTP time sync

# show SNTP sync status
timedatectl show-timesync --all

# check NTP daemon status
systemctl status ntpd # RHEL
systemctl status ntp  # Debian

# enable and start NTP daemon
systemctl enable ntpd && systemctl start ntpd
systemctl enable --now ntpd

# NTP configuration
/etc/ntp.conf

# manual one-time NTP sync
systemctl stop ntpd
ntpdate [ntp_server]

# monitor NTP status - ntpq
ntpq -p

remote # hostname of NTP provider
refid  # reference ID of NTP provider
st     # stratum of the provider
when   # number of seconds since last query
poll   # numer of seconds between queries
reach  # status ID indicating if server was reached
delay  # time in ms between query and response
offset # time in ms system time and NTP time
jitter # offset (ms) between system time and NTP in last query

# chrony - another way to implement NTP
chronyd # daemon
chronyc # CLI

# display info about NTP and system time
chronyc tracking

Reference ID  # ID and name to which computer is synced
Stratum       # number of hops to attached reference clock
Ref time      # UTC time at which last measurement was made
System time   # delay of system clock from sync time
Last offset   # estimated offset of the last clock update
RMS offset    # long term average of the offset value
Frequency     # rate of error if not corrrected
Residual freq # difference between the measurements from
			  # reference source and the frequency being used
Skew          # estimated error bound of the frequency
Root delay    # total of network delay to stratum computer
Leap status   # normal, insert second, delete second, not sync

# view detailed info about last valid NTP update
chrony ntpdata

# get info about NTP servers used to sync time
chronyc sources

# chrony configuration file
/etc/chrony.conf

# manual one-time NTP step update
chronyc makestep

```

## 108.2: System logging
```bash
# rsyslog config files
/etc/rsyslog.conf
/etc/rsyslog.d/*.conf

# log directory
/var/log

# auth processes: logons, sudo, cron jobs, failed logins etc.
/var/log/auth.log

# centralized file for all logs captured by rsyslogd
/var/log/syslog

# debug information from programs
/var/log/debug

# kernel messages
/var/log/kern.log

# informative messages not related to kernel but other
# services, default client log destination for centralized
# log server implementation
/var/log/messages

# info related to daemons and background services
/var/log/daemon.log

# info related to mail server
/var/log/mail.log

# info related to graphics card
/var/log/Xorg.0.log

# successful logins
/var/run/utmp
/var/log/wtmp

# failed logins
/var/log/faillog

# date and time of recent user logins
/var/log/lastlog

# Example service logs
/var/log/cups/
	error_log
	page_log
	access_log

/var/log/apache2/
/var/log/httpd/
	access.log
	error_log
	other_vhosts_access.log

/var/log/mysql
	error_log
	mysql.log
	mysql-slow.log
 
/var/log/samba
	log.
	log.nmbd
	log.smbd

# Reading logs
less
more
head
tail

# reading logs compressed with gzip
zless
zmore

# searching for stuff in logs
grep

# Log format
# timestamp
# hostname from which log originated
# name of program/service that generated the log
# the PID of the program that generated the log
# Description of the action that took place

# Examples of binary logs that require commands to parse them
/var/log/wtmp
who

/var/log/btmp
utmpdump /var/log/btmp

/var/log/faillog
faillog

/var/log/lastlog
lastlog

# The process of turning messages into logs
# 1. apps, services and kernell write messages in special
#    files (sockets and memory buffers) such as
/dev/log
/dev/kmsg

# 2. rsyslogd gets information from those special files
# 3. rsyslogd moves the info to corresponding log files
#    based on fules found in 
/etc/rsyslog.conf # and or
/etc/rsyslog.d/

# rsyslog config file sections
MODULES
GLOBAL DIRECTIVES
RULES

# rsyslog facilities
0  # kern - linux kernel messages
1  # user - user-level messages
2  # mail - mail system messages
3  # daemon - system daemon messages
4  # auth, authpriv - security/auth messages
5  # syslog - syslogd messages
6  # lpr - line printer subsystem
7  # news - network news subsystem
8  # uucp - unix-to-unix copy protocol subsystem
9  # cron - clock daemon
10 # auth, authpriv - security/auth messages
11 # ftp - file transfer protocol daemon
12 # ntp - network time protocol daemon
13 # security - log audit
14 # console - log alert
15 # cron - clockdaemon
16-23 # local0-local7 - local use 0-7

# rsyslog priorities
0 # Emergency [emerg, panic] - system is unusable
1 # Alert [alert] - action must be taken immediately
2 # Critital [crit] - Critical conditions
3 # Error [err, error] - Error conditions
4 # Warning [warn, warning] - warning conditions
5 # Notice [notice] - normal but significant condition
6 # informational [info] - informational messages
7 # Debug [debug] - Debug-level messages

# rule format
[facility].[priority] [action]

# Example rules
auth,authpriv.*                 /var/log/auth.log
*.*;auth,authpriv.none          -/var/log/syslog

mail.info                       -/var/log/mail.info

*.=debug;\
        auth,authpriv.none;\
	news.none;mail.none     -/var/log/debug

*.=info;*.=notice;*.=warn;\
	auth,authpriv.none;\
	cron,daemon.none;\
	mail,news.none          -/var/log/messages

# create manual entries in rsyslog
logger [message]

# implement rsyslog as central log server - server config
# 1. Edit remote logging config file
vim /etc/rsyslog.d/remote.conf
# uncomment the following line
$InputTCPServerRun 514  # Starts a TCP server on selected port

# 2. Restart rsyslog daemon
systemctl restart rsyslog

# 3. add a firewall rule to allow traffic on port 514
firewall-cmd --permanent --add-port 514/tcp
firewall-cmd --reload

# 4. Create a template specifying where to write remote logs
$template [template_name], "/var/log/remotehosts/%HOSTNAME%/%$NOW%.%syslogseverity-text%.log"

# 5. Add filter contorl the flow of logs
if $FROMHOST-IP=='[IP]' then ?[template_name]
& stop

# implement rsyslog as central log server - client config
# 1. Edit /etc/rsyslog.conf
vim /etc/rsyslog.conf
# add the following line at the end of the file
*.* @@[IP]:514

# 2. restart rsyslog
systemctl restart rsyslog

# Log rotation mechanism
logrotate

# logrotate config file
/etc/logrotate.conf

# logrotate config options
rotate [N] # retail N days/weeks/months of logs
daily # rotate logs daily
weekly # rotate logs weekly
monthly # rotate logs monthly
missingok # do not issue error message if log file missing
notifempty # do not rotate log if it is empty
compress # compress log files with gzip
delaycompress # postpone compression of previous log file
			  # to the next rotation cycle
sharedscripts # runs scripts only once regardless of how
			  # many log files mach given pattern
prerotate # indicate the beginning of prerotate script
postrotate # indicate the beginning of postrotate script

# Kernel Ring Buffer - registers logs before rsyslogd starts
dmesg

# systemd logging service - systemd-journald
systemctl status systemd-journald

# read journald logs
journalctl
-r # print messages in reverse order
-f # follow, print most recent and keep printing new entries
-e # view last entries within the pager
-n [N]       # print N most recent lines
--lines [N]  
-k           # print logs from Kernel Ring Buffer
--dmesg      

# search for patterns in logs
/ # forward search
? # backward search
N # go to next occurente
shift+N # go to previous occurence

# list boots
journalctl --list-boots

# show messages from current boot
journalctl --boot
journalctl -b 

# show messages from specified boot
journajctl --boot [N]
journajctl -b [N]

# show messages of given priority
journalctl -p [priority]
journalctl -p err # example

# show messages in given timeframe
journalctl --since [time] --until [time]
journalctl --since "19:00:00" "19:02:00" # example
journalctl --since "2 minutes ago" # example
journalctl --since "today" --until "19:00:00" # example

# show messages generated by a given program
journalctl [path_to_program]
journalctl /usr/sbin/sshd # example

# show messages generated by a given unit
journalctl -u [unit]
journalctl -u ssh.service # example

# filter logs by specific fields
journalctl PRIORITY=[N]
journalctl SYSLOG_FACILITY=[N]
journalctl _PID=[N]
journalctl _BOOT_ID=[ID]
journalctl _TRANSPORT=[transport_method]

# combining fields
journalctl [field1] [field2]   # AND
journalctl [field1] + [field2] # OR
journalctl [field1] [field1]   # OR

# manual entries in journal
systemd-cat
command | systemd-cat
systemd-cat [command]
systemd-cat -p [priority] [command]

# journald storage
/var/log/journal # persistent
/run/log/journal # volatile

# change storage configuration options
vim /etc/systemd/journald.conf
Storage=volatile   # store logs in /run/log/journal
Storage=persistent # store logs in /var/log/journal
Storage=auto       # default behaviour
Storage=none       # all log data is discarded

# check how much disk space do logs take
journalctl --disk-usage

# configure log retention
vim /etc/systemd/journald.conf

# amount of disk space that can be taken by a journal
SystemMaxUse=
RuntimeMaxUse=

# amount of disk space that should be left free
SystemKeepFree=
RuntimeKeepFree=

# maximum file size of each individual journal file
SystemMaxFileSize=
RuntimeMaxFileSize=

# maximum number of journal files to store
SystemMaxFiles=
RuntimeMaxFiles=

# time-based retention criterial examples
MaxRetentionSec=
MaxFileSec=

# manually clean archived journal files
journalctl --vacuum-time=[time]
journalctl --vacuum-size=[size]
journalctl --vacuum-files=[N]

# clean all journal files - not onlu archived
journalctl --rotate [vacuum_option]

# make journal persistent
journalctl --flush

# write all unwritten log data to disk
journalctl --sync

# verify consistency of a journal file
journalctl --verify

# reading logs in rescue mode - read from alternative dir
journalctl -D [path]
-m # merge entries from all journals to /var/log/journal
--file [path]    # show entries in specific file
--root [fs_root] # root of FS to search logs in 

# forward journald logs to syslog
ForwardToSyslog=yes

```

## 108.3: Mail Transfer Agent (MTA) basics
```bash
open relay # MTA that blindly forwards emails

# Common unix MTAs
sendmail
Postfix
qmail
Exim

# sendmail config file
/etc/mail/sendmail.mc

# sendmail - allow non-local connections
DAEMON_OPTIONS(\`Port=smtp,Addr=[IP], Name=MTA\')dnl

# connect to MTA using netcat
nc [MTA_name | MTA_IP] [port]
nc lab2.campus 25 # example

# interact with MTA using commands
HELO [initiator]     # indicate exchange initiator
MAIL FROM: [address] # FROM
RCPT TO: [address]   # TO
DATA                 # indicate start of email data
QUIT                 # finish connection with 

# example email data
Subject: hello there

This is my message.
.

# default email location
/var/spool/mail/[username]

# send an email using sendmail
sendmail [receiver_address]
From: [sender_address]
To: [receiver_address]
Subject: [subject]

[Body]
.

# view non-delievered messages
mailq
sendmail -bp

# outbox queue default location
/var/spool/mqueue

# Postfix outbox queue default location
/var/spool/postfix/[directory_tree]

# immediately attempt to deliever messages
sendmail -q

# MUA - Mail User Agent
mail
mailx
Mozilla Thunderbird
Gnome Evolution
webmail

# send email using mail
mail -s [subject] [reveiver_address] <<< [message]

# example
mail -s "Maintenance fail" henry@lab3.campus <<<"The maintenance script failed at `date`"

# aliases 
/etc/aliases

# example aliases
postmaster: root
root: bob

# update MTA's aliases database
newaliases
sendmail -bi
sendmail -I

# alias destinations
# 1. full path to a file
/home/bob/all_my_fucking_emails.txt

# 2. a command to process the message
|mail_processor.sh

# 3. an include file - forward to multiple places
:include:/var/local/destinations

# 4. an external address
greg@external.inc

# 5. other alias
[alias]

# forwarding configuration on user level
echo [destination] >> .forward

```

## 108.4: Manage printers and printing
```bash
# install CUPS
apt install cups
dnf install cups

# start CUPS service
systemctl start cups.service

# check status of CUPS service
systemctl status CUPS

# CUPS service config file
/etc/cups/cupsd.conf

# Legacy config file used with LDP before advent of CUPS
/etc/printcap

# config file with all configured printers
/etc/cups/printers.conf

# dir that holds PPD files for printers that use them
/etc/cups/ppd/

# CUPS log files
/var/log/cups/access_log
/var/log/cups/page_log
/var/log/cups/error_log

# config file stanza restricting access to admin tasks in CUPS
<Limit CUPS-Add-Modify-Printer CUPS-Delete-Printer CUPS-Add-Modify-Class CUPS-Delete-Class CUPS-Set-Default>
  AuthType Default     # basic auth prompt will be used
  Require user @SYSTEM # user with admin privs is required
  Order deny,allow     # deny, unless user is authenticated
</Limit

# Install a printer using web interface
http://localhost:631
Administration -> Add Printer

# Install a printer using CLI
lpadmin -p [name] -L [location] -v [device_URI] -m [model]

# example
lpadmin -p "printer" -L "office" -v socket://10.1.1.2 -m everywhere

# query locally installed PPD files
lpinfo --make-and-model [model] -m
lpingo --make-and-model "HP Envy 4510" -m # example

# select a default printer
lpoptions -d [printer]
lpoptions -d "ENVY-4510" # example

# share printer on the network
lpadmin -p [printer] -o printer-is-shared=true

# config print queue to only access jobs from specific user
lpadmin -p [printer] -u allow:[user], ...

# config print queue to deny print jobs from specific user
lpadmin -p [printer] -u deny:[user], ...

# allow/deny a group to use a print queue
lpadmin -p [printer] -u deny:@[group], ...
lpadmin -p [printer] -u allow:@[group], ...

# set printer error policy 
lpadmin -p [printer] -o printer-error-policy=[policy]
abort-job          # abort job
retry-job          # retry job at a later time
stop-printer       # stop printer immediately
retry-current-job  # retry job immediately

# send a print job to default printer
lpr [file]

# list available printers
lpstat -p -d

# send a print job to selected printer
lpr -P [printer] [file]

# send a print job and specify print options
lpr -o [options] [file]

# print options
landscape            # print document rotated 90 degrees
two-sided-long-edge  # print in portrait mode on both sides
two-sided-short-edge # print in landscape mode on both sides
media                # specify media size:
					 # A4, Letter, Legal, DL, COM10
collate              # collate printed document
page-ranges          # select page range to print
fit-to-page          # scale file to fit the paper
outputorder          # print in normal or reverse order

# example
lpr -P ACCOUNTING-LASERJET -o landscape -o media=A4 -o two-sided-short-edge finance-report.pdf

# print multiple pages
lpr -\#[N] [file]

lpr -\#7 -o collate=true status-report.pdf # example

# lp command - equivalent to lpr
lp -d [printer] -n [N] [file

# lp - example
lp -d SALES-LASERJET -n 7 -o collate=true status-report.pdf

# view submitted print jobs
lpq

# all queues of all printers
lpq -a 
lp -o

# remove print job
lprm [ID]

# delete all print jobs
lprm -

# stop current print job as user - using CUPS command
cancel

# stop specific print job
cancel [printer]-[ID]
cancel ACCCOUNTING-LASERJET-20 # example

# move print job from one queue to anoher
lpmove [printer]-[ID] [printer]
lpmove ACCOUNTING-LASERJET-20 FRONT-DESK # example

# list all printers managed by CUPS service
lpstat -v

# set printer to remove new print jobs
cupsreject -r [message] [printer]
cupsreject -r "To be removed" FRONT-DESK # example

# remove printer from cups
lpadmin -x [printer] # example

```

##  109.1: Fundamentals of internet protocols
```bash
# IP address classes
A 1.0.0.0 - 126.255.255.255
B 128.0.0.0 - 191.255.255.255
C 192.0.0.0 - 223.255.255.255

# Public and private IPs
A 10.0.0.0 - 10.255.255.255
B 172.16.0.0 - 172.31.255.255
C 192.168.0.0 - 192.168.255.255

# Netmask
255.0.0.0     11111111.00000000.00000000.00000000 /8
255.255.0.0   11111111.11111111.00000000.00000000 /16
255.255.255.0 11111111.11111111.11111111.00000000 /24

# Common ports
20  # FTP (data)
21  # FTP (control)
22  # SSH
23  # Telnet
25  # SMTP
53  # DNS
80  # HTTP
110 # POP3
123 # NTP
139 # Netbios
143 # IMAP
161 # SNMP
162 # SNMPTRAP, SNMP notifications
389 # LDAP
443 # HTTPS
465 # SMTPS
514 # RSH (remote shell)
636 # LDAPS
993 # IMAPS
995 # POP3S

# TCP  - connection oriented
# UDP  - connectionless
# ICMP - used to analyze and control network elements
#      - traffic volume control
#      - detection of unreachable destinations
#      - route redirection
#      - checking the status of remote hosts

# list ofstandard service ports
/etc/services

# IPv6 address types
unicast   # identifies single network interface
multicast # identifies a set of network interfaces
anycast   # set of NICs, packets delievered to only one

# IPv4 vs IPv6
# service ports follow the same standards and protocols
# IPv6 does not implement broadcast
# using SLAAC, IPv6 hosts are able to self-configure
# TTL field is replaced by Hop Limit
# all IPv6 interfaces have link-local addresses fe80::/10
# IPv6 implements NDP, something like ARP but more robust

```

## 109.2: Persistent network configuration
```bash
# show ip configuration
ip link show

# show network devices info
nmcli device

# interface names
en # Ethernet
ib # InfiniBand
sl # Serial line IP (slip)
wl # Wireless local area network (WLAN)
ww # Wireless wide area network (WWAN)

# interface naming rules
# 1. index provided by BIOS or firmware of embedded device [eno1]
# 2. PCI express slow index, as given by BIOS or firmware [ens1]
# 3. device address at the corresponding bus [enp3s5]
# 4. interface's MAC address [enx78e7d1ea46da]
# 5. legacy naming convention [eth1]

# NIC management commands
ifconfig # deprecated
ip       # current

# configure NICs based on interface definitions
# stored in /etc/network/interfaces or in case of CentOS
# in /etc/sysconfig/network-scripts
ifup [interface]
ifdown [interface]

# sample DHCP configuration
auto enp3s5
iface enp3s5 inet dhcp

# sample static configuration
iface enp3s5 inet static
	address 192.168.1.2/24
	gateway 192.168.1.1

# set static hostname of the system
echo [hostname] > /etc/hostname
hostnamectl set-hostname [hostname]

# set pretty hostname of the system
hostnamectl --pretty set-hostname [hostname]

# set transient hostname of the system
hostnamectl --transient set-hostname [hostname]

# show hostname details
hostnamectl status

# configure how to resolve network names of IPs and
# user and group names to their numeric IDs
vim /etc/nsswitch.conf

# ---- nsswitch.conf ---- #
hosts: files dns
# ----------------------- #
# resolve DNS names using /etc/hosts first then DNS servers

# edit /etc/hosts
vim /etc/hosts

# set system dns servers
vim /etc/resolv.conf

# ---- /etc/resolv.conf ---- #
nameserver 10.1.1.254    # DNS server entry
nameserver 1.1.1.1       # DNS server entry
domain home.local        # local domain name
search home.inc home.io  # list of local domain names
# -------------------------- #

# NetworkManager CLI
nmcli [object] [command]

# nmcli objects
general    # general status and operations
networking # overall networking control
radio      # radio switches
connection # connections
device     # devices managed by NetworkManager
agent      # secret agent or polkit agent
monitor    # monitor NetworkManager changes

# show overall connectivity status
nmcli general

# show list of wifi networks
nmcli device wifi list

# connect to wifi network
nmcli device wifi connect [net_name]

# connect to wifi network specifying the password
nmcli device wifi connect [net_name] password [pass]

# connect to wifi network with hidden SSID
nmcli device wifi connect [net_name] hidden yes

# connect to wifi network using specified interface
nmcli device wifi connect [net_name] ifname [interface]

# view saved network connections
nmcli connection show

# disable network connection
nmcli connection down [net_name]

# disconnect device
nmcli device disconnect [dev_name]

# connect device
nmcli device connect [dev_name]

# turn off wifi radio
nmcli radio wifi off

# systemd-networkd configuration files
/lib/systemd/network
/run/systemd/network
/etc/systemd/network

# systemd-networkd file types
.netdev  # virtual network devices
.link    # low-level config for corresponding network interface
.network # network addresses and routes

# sample .network file - static configuration
[Match]
Name=enp3s5

[Network]
Address=10.0.0.2/24
Gateway=10.0.0.1/24

# sample .network file - DHCP
[Match]
MACAddress=00:16:3e:8d:2b:5b

[Network]
DHCP=yes

# create WPA credentials
wpa_passphrase [net_name] > 
/etc/wpa_supplicant/wpa_supplicant-[interface].conf

```

## 109.3: Basic network troubleshooting
```bash
# ip command
man ip
ip address help

# list available interfaces
ifconfig -a
ip link
ls /sys/class/net

# configure interface - ifconfig
ifconfig [interface] [ip_address]
ifconfig enp1s0 192.168.50.50/24 # example
ifconfig eth1 10.1.1.1 netmask 255.255.255.0 # example
ifconfig eth1 10.1.1.1 netmask 0xffffff00 # example
ifconfig eth1 add 2001:db8::10/64

# configure interface - ip
ip addr add [ip_address] dev [interface]
ip addr add 10.1.1.1/24 dev eth1
ip addr add 2001:db8::10/64 dev eth1

# disable/enable interface
ip link set dev [interface] down
ip link set dev [interface] up

# show interface status
ip link show dev [interface]

# set interface MTU
ip link set [interface] mtu [value]

# view routing table
netstat -r
ip route
route

# view IPv6 routing table
netstat -6r
ip -6 route
route -6

# add IPv6 route
route -6 add [net_address] gw [gateway]
route -6 add 2001:db8:1::/64 gw 2001:db8::3 # example

# remove IPv6 route
ip route del [net_address] via [gateway]
ip route del 2001:db8:1::/64 via 2001:db8::3 # example

# send N ICMP echo packets to IP
ping -c [N] [IP]
ping6 -c [N] [IPv6]

# trace route to host - UDP
traceroute [host]

# trace route to host - ICMP
traceroute -I [host]

# trace route to host - TCP
traceroute -T -p [port] [host]

# trace route to host - find out MTU
tracepath [host]
tracepath6 [host]

# start listener on port
nc -l [port]

# start a UDP listener, pass to stdin of executable
nc -u -e [executable] -l [port]
nc -u -e /bin/bash -l 1337 # example

# create an arbitrary connection
nc [host] [port]

# view connections and listeners - netstat & ss
netstat
ss
-a # show all sockets
-l # show listening sockets
-p # show process associated with connection
-n # prevent name lookups for ports and addresses
-t # show TCP connections
-u # show UPD connections

```

## 109.4: Configure client side DNS
```bash
# name lookup configuration file
/etc/nsswitch.conf

# DNS configuration file
/etc/resolv.conf
nameserver [IP]
search [domain]
domain [domain]
option [option]:[value]

# the hosts file
/etc/hosts

# systemd-resolved
# listend for queries on 127.0.0.53
# queries DNS in /etc/systemd/resolve.conf or /etc/resolv.conf

# retrieve info from sources defined in nsswitch.conf
getent [datebase] [query]

# use specific data source
getent -s [source] [database] [query]

# host - simple DNS name lookup
host [query]

# host - find specific record type
host -t [record_type] [query]

# host - query specific DNS
host [query] [dns_server]

# dig - advanced DNS lookups
dig [query]

# dig - find specific record type
dig -t [record_type] [query]

# dig - shortened results
dig +short [query]

# dig - turn of cookie EDNS extension
dig +nocookie [query]

```

## 110.1: Perform security administration tasks
```bash
# find files with SUID set (exclusively) 
find / -perm u+s
find / -perm 4000

# find files with SUID (irrespective of other perms)
find / -perm -u+s
find / -perm -4000

# find files with GUID set (exclusively)
find / -perm g+s
find / -perm 2000

# find files with GUID set (irrespective of other perms)
find / -perm -g+s
find / -perm -2000

# both SUID and GUID set (exclusively)
find / -perm ug+s
find / -perm 6000

# both SUID and GUID set (irrespective of other perms)
find / -perm -ug+s
find / -perm -6000

# both SUID/ GUID (or either one, irrespective or other perms)
find / -perm /ug+s
find / -perm /6000

# get status information about an account
passwd -S 
bob P 12/07/2019 0 99999 7 -1
# fields:
username
password status # password P, locked L, no password NP 
minimum age
maximum age
warning period # user notified prior to password expiration
inactivity period # account inactive after password expiration

# other passwd options
-l # lock account
-u # unlock account
-e # expire password
-d # delete password

# lock/unlock account - usermod
usermod --lock [username]
usermod -L [username]
usermod --unlock [username]
usermod -U [username]

# print password info
chage -l [username]

# modify account with chage
chage [option] [param] [user]
--mindays    -m [N]    # minimum password age
--maxdays    -M [N]    # maximum password age
--lastday    -d [N]    # days since password last changed
--warndays   -W [N]    # remainder N days before expiration
--inactive   -I [N]    # inactive days (account lock)
--expiredate -E [date] # date of account expiration

# discover open ports - lsof
lsof -i
lsof -i @[IP] # specify host
lsof -i4      # IPv4 only
lsof -i6      # IPv6 only
lsof -i :[port] # filter by port

# discover open ports - fuser
fuser -vn [protocol] [port]
fuser -vn tcp 80 # example

# discover open ports - netstat
netstat
--listening -l  # listening ports only
--tcp       -t  # TCP only
--udp       -u  # UDP only
--extend    -e  # show additional info 

# discover open ports - nmap
nmap [host]
-p [ports] # port or port range
-F         # fast scan of top 100 ports
-v         # verbose

# limit available resources - ulimit
ulimit [option]         # display
ulimit [option] [value] # set
-S # display/change soft limit
-H # display/change hard limit
-b # socket buffer size
-f # size of files written
-l # size that may be locked into memory
-m # resident set size (RSS)
-v # virtual memory
-u # number of processes

# make limits persistent across reboots
/etc/security/limits.conf

# display last logged users
last

# display logons of specified user
last [user]

# display last unsuccessful logon attempts
lastb

# list currently logged on users - who
who
--boot     -b # display time of last system boot
--runlevel -r # display current runlevel
--heading  -H # print column headings

# list currently logged on users - w
w
USER   # login name of the user 
TTY    # name of terminal the user is on
FROM   # remote host from which user logged on
LOGIN@ # login time
IDLE   # idle time
JCPU   # CPU time of all processes on the tty
PCPU   # CPU time of the current process
WHAT   # the current process

# display only specified user
w [user]

# switch user
su [user]   # just open a shell as user
su - [user] # load configuration scripts

# switch context to root for one command
sudo [command]

# switch context to other user for one command
sudo -u [user] [command]

# configure sudo
vim /etc/sudoers

# example sudoers file entries
root    ALL=(ALL:ALL) ALL # user
%sudo   ALL=(ALL:ALL) ALL # group

[user] [host]=([user]:[group]) [commands]
# from all hosts, as all users and groups, exec all commands

# further examples
carol   ALL=(ALL:ALL) /usr/bin/systemctl status apache2
carol   ALL=(ALL:ALL) NOPASSWD: systemctl status apache2
carol   192.168.1.7=(mimi) /usr/bin/systemctl status apache2

# sudo groups
sudo
wheel

# aliases in sudoers
Host_Alias    # list of hostnames, IPs, networks
User_Alias    # list of users, groups
Cmnd_Alias    # list of commands

# alias examples
Host_Alias SERVERS = 192.168.1.7, server1, server2
User_Alias ADMINS = carol, %sudo, PRIV_USERS, !REGULAR_USERS
Cmnd_Alias SERVICES = /usr/bin/systemctl *

```

## 110.2: Setup host security
```bash
# change user's password
passwd [user]

# display info about user's password
chage -l [user]

# expire user's password
chage -E [date] [user]

# lock user account
passwd -l [user]

# tell users why they cannot log in
echo [message] > /etc/nologin

# set nologin shell for a user
usermod -s /bin/nologin [user]

# xinetd config files
/etc/xinetd.conf
/etc/xinetd.d/*

# example xinetd service config file
service ssh
{
	disable		= no 
	socket_type	= stream
	protocol	= tcp
	wait		= no
	user		= root
	server		= /usr/sbin/sshd
	server_args = -i
	flags		= IPv4
	interface	= 192.168.178.1
}

disable      # no - activates settings, yes disables them
socket_type  # stream for TCP sockets, dgram for UDP
protocol     # TCP or UDP
wait         # wait for the deamon to complete it's
			 # operation before closing the socket 
user         # service owner
server       # full path to service that should be started
server_args  # pass options to the service
flags        # socket options, like listen on IPv4 only
interface    # network interface to control


# systemd socket units
systemctl start [service].socket

# view all running services - SysV
service --status--all

# disable unnecessary service - SysV debian
update-rc.d [service] remove

# disable unnecessary service - SysV RHEL
chkconfig [service] off

# view all running services - systemd
systemctl list-units --state active --type service

# disable unnecesary service - systemd
systemctl disable [unit] --now

# view listening network services - netstat / ss
netstat -ltu
ss -ltu

# TCP wrappers
/etc/hosts.allow
/etc/hosts.deny

```

## 110.3: Securing data with encryption
```bash
# connect via ssh
ssh [user]@[host]
ssh [host]

# SSH known hosts
~/.ssh/known_hosts

# remove known host when host fingerprint changes
ssh-keygen -f ~/.ssh/known_hosts -R [host]

# delete all keys belonging to host
ssh-keygen -R [host]

# generate a set of asymetric keys
ssh-keygen -t [type]
-b # size in bytes

# SSH authorized keys
~/.ssh/authorized_keys

# open shell using ssh-agent and add private key
ssh-agent /bin/bash
ssh-add

# public-key algorithms
RSA     # secure, min key length 1024 bits (default)
DSA     # not secure, keys exactly 1024 bits long
ecdsa   # secure, key sizes of 256, 384 or 521
ed25519 # most secure, key size of 256 bits

# view key fingerprint
ssh-keygen -l -f [path]
ssh-keygen -lv -f [path] # display random art

# create a local port forward
ssh -L [local_port]:[host]:[local_port] localhost

# create a local tunnel to remote machine
ssh -L [local_port]:[host]:[remote_port] -Nf [user]@[host]
-N # do not execute commands
-f # run in the background

# create a remote tunnel to localhost (reverse port forward)
ssh -R [remote_port]:localhost:[local_port] -Nf [user]@[host]

# establish an ssh tunnel with X11 forwarding
ssh -X [user]@[host]

# generate GPG keys
gpg --gen-key

# GPG files and directories
openpgp-revocs.d   # revocation certificate dir
private-keys-v1.d  # private keys dir
pubring.kbx        # public keyring
trustdb.gpg        # trust database

# view public keys
gpg --list-keys

# export GPG key
gpg --export [user] > [outfile]

# send public key to remote server using scp
scp [file] [user]@[host]:[path]

# create GPG revocation certificate
gpg --output [outfile] --gen-revoke [user]

# import certificate into keyring
gpg --import [cert]

# import public key
gpg --import [key]

# encrypt file with GPG
gpg --output [outfile] --recipient [user] --encrypt [file]
--armor # output ASCII armor format (safe to send via email)

# decrypt file with GPG
gpg --decrypt [file]
--output # specify output file

# sign file using GPG
gpg --output [outfile] --sign [file]

# verify file with GPG
gpg --verify [file]

```
