# VMPStudio

### Description

An arm/arm64/x86/x86_64 lightweight IDA for UraniumVM/PhoneVMP.

It's free to be used as a lightweight IDA tool.

||Local|Sample Android|Sample iOS|
|-|-|-|-|
|Windows|No|Yes|No|
|Intel Linux|No|Yes|No|
|ARM Linux|No|Yes|No|
|Intel macOS|Yes|Yes|Yes|
|ARM macOS|Yes|Yes|Yes|

 * GUI Runtime is based on [Qt](https://www.qt.io/); 
 * GUI Controls is based on [X64Dbg](https://github.com/vpand/X64Dbg/);
 * UraniumVM Engine is developed by [VPAND](https://vpand.com/);
 * Assembler/Disassembler is based on [LLVM](http://llvm.org/);
 * Analyze Engine is developed by [VPAND](https://vpand.com/);
 * Script is based on [Python](https://www.python.org/);

 ```
macOS user: use the Preference menu to configurate the remote machine instruction 
             and register context sampling.

Windows/Linux user: use the MainMenu/Options/Preference to configurate the remote 
             machine instruction and register context sampling.
```

Sample Server:

 * iOS user: install [uvm-server.deb](https://github.com/vpand/VMPStudio/blob/master/uvm-server.deb) to iDevice
```
scp VMPStudio/uvm-server.deb root@ip:/tmp/
ssh root@ip dpkg -i --force-overwrite /tmp/uvm-server.deb
```
 * iOS user: an extra step to install injection framework [Textobot.deb](https://github.com/vpand/VMPStudio/blob/master/Textobot.deb) to iDevice
```
scp VMPStudio/Textobot.deb root@ip:/tmp/
ssh root@ip dpkg -i --force-overwrite /tmp/Textobot.deb
```
 * Android user: push [uvm-server64](https://github.com/vpand/VMPStudio/tree/master/uvm-server64) to Android Device
```
adb push VMPStudio/uvm-server64 /data/local/tmp/
adb shell chmod -R 755 /data/local/tmp/uvm-server64
cd /data/local/tmp/uvm-server64; ./uvmserver&
```
 * Android user: an extra step to turn off SELinux
```
setenforce 0
```
 * On Android, if you want to launch APK using uvmfire, you should have Magisk root, and install [Riru UVMZygote](https://github.com/vpand/VMPStudio/tree/master/launch-apk)

### User Manual

For more details, see [VMPStudio User Manual](https://github.com/vpand/vsusermanual/).
