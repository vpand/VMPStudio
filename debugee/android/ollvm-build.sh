rm -f ./libs/arm64-v8a/* ./libs/armeabi-v7a/* ./libs/x86_64/* ./libs/x86/*
rm -f ./libs/arm64-v8a/gdbserver ./libs/armeabi-v7a/gdbserver ./libs/x86_64/gdbserver ./libs/x86/gdbserver
rm -f ./libs/arm64-v8a/gdb.setup ./libs/armeabi-v7a/gdb.setup ./libs/x86_64/gdb.setup ./libs/x86/gdb.setup
mkdir -p obj/local/arm64-v8a/objs/ollvmdebug/__/__
echo [arm64-v8a] "Compile++      ": "ollvmdebug <= antidebug.cpp"
rm -f ./obj/local/arm64-v8a/objs/ollvmdebug/__/__/antidebug.o
${clang_vmp}++ -MMD -MP -MF ./obj/local/arm64-v8a/objs/ollvmdebug/__/__/antidebug.o.d -target aarch64-none-linux-android24 -fdata-sections -ffunction-sections -fstack-protector-strong -funwind-tables -no-canonical-prefixes  --sysroot ${NDK_HOME}/toolchains/llvm/prebuilt/darwin-x86_64/sysroot -g -Wno-invalid-command-line-argument -Wno-unused-command-line-argument  -D_FORTIFY_SOURCE=2 -fno-exceptions -fno-rtti -fpic -O2 -DNDEBUG  -I${NDK_HOME}/sources/cxx-stl/llvm-libc++/include -I${NDK_HOME}/sources/cxx-stl/llvm-libc++abi/include -Ijni    -DANDROID -fvisibility=hidden -nostdinc++ -Wformat -Werror=format-security -std=gnu++17  -c  jni/../../antidebug.cpp -o ./obj/local/arm64-v8a/objs/ollvmdebug/__/__/antidebug.o
mkdir -p obj/local/arm64-v8a
mkdir -p ${NDK_HOME}/sources/cxx-stl/llvm-libc++/libs/arm64-v8a
mkdir -p ${NDK_HOME}/sources/cxx-stl/llvm-libc++abi/../llvm-libc++/libs/arm64-v8a
mkdir -p ${NDK_HOME}/toolchains/llvm/prebuilt/darwin-x86_64/lib64/clang/12.0.8/lib/linux/aarch64
echo [arm64-v8a] "Executable     ": "ollvmdebug"
${NDK_HOME}/toolchains/llvm/prebuilt/darwin-x86_64/bin/clang++ -Wl,--gc-sections -Wl,-rpath-link=${NDK_HOME}/toolchains/llvm/prebuilt/darwin-x86_64/sysroot/usr/lib/aarch64-linux-android/24 -Wl,-rpath-link=./obj/local/arm64-v8a ./obj/local/arm64-v8a/objs/ollvmdebug/__/__/antidebug.o ${NDK_HOME}/sources/cxx-stl/llvm-libc++/libs/arm64-v8a/libc++_static.a ${NDK_HOME}/sources/cxx-stl/llvm-libc++abi/../llvm-libc++/libs/arm64-v8a/libc++abi.a ${NDK_HOME}/toolchains/llvm/prebuilt/darwin-x86_64/lib64/clang/12.0.8/lib/linux/aarch64/libunwind.a -latomic -target aarch64-none-linux-android24 -no-canonical-prefixes   -Wl,--build-id=sha1 -Wl,--no-rosegment  -nostdlib++ -Wl,--no-undefined -Wl,--fatal-warnings -llog -lc -lm -o ./obj/local/arm64-v8a/ollvmdebug
mkdir -p libs/arm64-v8a
echo [arm64-v8a] "Install        ": "ollvmdebug => libs/arm64-v8a/ollvmdebug"
install -p ./obj/local/arm64-v8a/ollvmdebug ./libs/arm64-v8a/ollvmdebug
${NDK_HOME}/toolchains/llvm/prebuilt/darwin-x86_64/bin/llvm-strip --strip-unneeded  ./libs/arm64-v8a/ollvmdebug
mkdir -p obj/local/armeabi-v7a/objs/ollvmdebug/__/__
echo [armeabi-v7a] "Compile++ thumb": "ollvmdebug <= antidebug.cpp"
rm -f ./obj/local/armeabi-v7a/objs/ollvmdebug/__/__/antidebug.o
${clang_vmp}++ -MMD -MP -MF ./obj/local/armeabi-v7a/objs/ollvmdebug/__/__/antidebug.o.d -target armv7-none-linux-androideabi24 -fdata-sections -ffunction-sections -fstack-protector-strong -funwind-tables -no-canonical-prefixes  --sysroot ${NDK_HOME}/toolchains/llvm/prebuilt/darwin-x86_64/sysroot -g -Wno-invalid-command-line-argument -Wno-unused-command-line-argument  -D_FORTIFY_SOURCE=2 -fno-exceptions -fno-rtti -fpic -march=armv7-a -mthumb -Oz -DNDEBUG  -I${NDK_HOME}/sources/cxx-stl/llvm-libc++/include -I${NDK_HOME}/sources/cxx-stl/llvm-libc++abi/include -Ijni    -DANDROID -fvisibility=hidden -nostdinc++ -Wformat -Werror=format-security -std=gnu++17  -c  jni/../../antidebug.cpp -o ./obj/local/armeabi-v7a/objs/ollvmdebug/__/__/antidebug.o
mkdir -p obj/local/armeabi-v7a
mkdir -p ${NDK_HOME}/sources/cxx-stl/llvm-libc++/libs/armeabi-v7a
mkdir -p ${NDK_HOME}/sources/cxx-stl/llvm-libc++abi/../llvm-libc++/libs/armeabi-v7a
mkdir -p ${NDK_HOME}/toolchains/llvm/prebuilt/darwin-x86_64/lib64/clang/12.0.8/lib/linux/arm
echo [armeabi-v7a] "Executable     ": "ollvmdebug"
${NDK_HOME}/toolchains/llvm/prebuilt/darwin-x86_64/bin/clang++ -Wl,--gc-sections -Wl,-rpath-link=${NDK_HOME}/toolchains/llvm/prebuilt/darwin-x86_64/sysroot/usr/lib/arm-linux-androideabi/24 -Wl,-rpath-link=./obj/local/armeabi-v7a ./obj/local/armeabi-v7a/objs/ollvmdebug/__/__/antidebug.o ${NDK_HOME}/sources/cxx-stl/llvm-libc++/libs/armeabi-v7a/libc++_static.a ${NDK_HOME}/sources/cxx-stl/llvm-libc++abi/../llvm-libc++/libs/armeabi-v7a/libc++abi.a ${NDK_HOME}/toolchains/llvm/prebuilt/darwin-x86_64/lib64/clang/12.0.8/lib/linux/arm/libunwind.a -latomic -target armv7-none-linux-androideabi24 -no-canonical-prefixes   -Wl,--build-id=sha1 -Wl,--no-rosegment  -nostdlib++ -Wl,--no-undefined -Wl,--fatal-warnings -llog -lc -lm -o ./obj/local/armeabi-v7a/ollvmdebug
mkdir -p libs/armeabi-v7a
echo [armeabi-v7a] "Install        ": "ollvmdebug => libs/armeabi-v7a/ollvmdebug"
install -p ./obj/local/armeabi-v7a/ollvmdebug ./libs/armeabi-v7a/ollvmdebug
${NDK_HOME}/toolchains/llvm/prebuilt/darwin-x86_64/bin/llvm-strip --strip-unneeded  ./libs/armeabi-v7a/ollvmdebug
mkdir -p obj/local/x86_64/objs/ollvmdebug/__/__
echo [x86_64] "Compile++      ": "ollvmdebug <= antidebug.cpp"
rm -f ./obj/local/x86_64/objs/ollvmdebug/__/__/antidebug.o
${clang_vmp}++ -MMD -MP -MF ./obj/local/x86_64/objs/ollvmdebug/__/__/antidebug.o.d -target x86_64-none-linux-android24 -fdata-sections -ffunction-sections -fstack-protector-strong -funwind-tables -no-canonical-prefixes  --sysroot ${NDK_HOME}/toolchains/llvm/prebuilt/darwin-x86_64/sysroot -g -Wno-invalid-command-line-argument -Wno-unused-command-line-argument  -D_FORTIFY_SOURCE=2 -fno-exceptions -fno-rtti -fPIC -O2 -DNDEBUG  -I${NDK_HOME}/sources/cxx-stl/llvm-libc++/include -I${NDK_HOME}/sources/cxx-stl/llvm-libc++abi/include -Ijni    -DANDROID -fvisibility=hidden -nostdinc++ -Wformat -Werror=format-security -std=gnu++17  -c  jni/../../antidebug.cpp -o ./obj/local/x86_64/objs/ollvmdebug/__/__/antidebug.o
mkdir -p obj/local/x86_64
mkdir -p ${NDK_HOME}/sources/cxx-stl/llvm-libc++/libs/x86_64
mkdir -p ${NDK_HOME}/sources/cxx-stl/llvm-libc++abi/../llvm-libc++/libs/x86_64
mkdir -p ${NDK_HOME}/toolchains/llvm/prebuilt/darwin-x86_64/lib64/clang/12.0.8/lib/linux/x86_64
echo [x86_64] "Executable     ": "ollvmdebug"
${NDK_HOME}/toolchains/llvm/prebuilt/darwin-x86_64/bin/clang++ -Wl,--gc-sections -Wl,-rpath-link=${NDK_HOME}/toolchains/llvm/prebuilt/darwin-x86_64/sysroot/usr/lib/x86_64-linux-android/24 -Wl,-rpath-link=./obj/local/x86_64 ./obj/local/x86_64/objs/ollvmdebug/__/__/antidebug.o ${NDK_HOME}/sources/cxx-stl/llvm-libc++/libs/x86_64/libc++_static.a ${NDK_HOME}/sources/cxx-stl/llvm-libc++abi/../llvm-libc++/libs/x86_64/libc++abi.a ${NDK_HOME}/toolchains/llvm/prebuilt/darwin-x86_64/lib64/clang/12.0.8/lib/linux/x86_64/libunwind.a -latomic -target x86_64-none-linux-android24 -no-canonical-prefixes   -Wl,--build-id=sha1 -Wl,--no-rosegment  -nostdlib++ -Wl,--no-undefined -Wl,--fatal-warnings -llog -lc -lm -o ./obj/local/x86_64/ollvmdebug
mkdir -p libs/x86_64
echo [x86_64] "Install        ": "ollvmdebug => libs/x86_64/ollvmdebug"
install -p ./obj/local/x86_64/ollvmdebug ./libs/x86_64/ollvmdebug
${NDK_HOME}/toolchains/llvm/prebuilt/darwin-x86_64/bin/llvm-strip --strip-unneeded  ./libs/x86_64/ollvmdebug
mkdir -p obj/local/x86/objs/ollvmdebug/__/__
echo [x86] "Compile++      ": "ollvmdebug <= antidebug.cpp"
rm -f ./obj/local/x86/objs/ollvmdebug/__/__/antidebug.o
${clang_vmp}++ -MMD -MP -MF ./obj/local/x86/objs/ollvmdebug/__/__/antidebug.o.d -target i686-none-linux-android24 -fdata-sections -ffunction-sections -fstack-protector-strong -funwind-tables -no-canonical-prefixes  --sysroot ${NDK_HOME}/toolchains/llvm/prebuilt/darwin-x86_64/sysroot -g -Wno-invalid-command-line-argument -Wno-unused-command-line-argument  -D_FORTIFY_SOURCE=2 -fno-exceptions -fno-rtti -fPIC -O2 -DNDEBUG  -I${NDK_HOME}/sources/cxx-stl/llvm-libc++/include -I${NDK_HOME}/sources/cxx-stl/llvm-libc++abi/include -Ijni    -DANDROID -fvisibility=hidden -nostdinc++ -Wformat -Werror=format-security -std=gnu++17  -c  jni/../../antidebug.cpp -o ./obj/local/x86/objs/ollvmdebug/__/__/antidebug.o
mkdir -p obj/local/x86
mkdir -p ${NDK_HOME}/sources/cxx-stl/llvm-libc++/libs/x86
mkdir -p ${NDK_HOME}/sources/cxx-stl/llvm-libc++abi/../llvm-libc++/libs/x86
mkdir -p ${NDK_HOME}/toolchains/llvm/prebuilt/darwin-x86_64/lib64/clang/12.0.8/lib/linux/i386
echo [x86] "Executable     ": "ollvmdebug"
${NDK_HOME}/toolchains/llvm/prebuilt/darwin-x86_64/bin/clang++ -Wl,--gc-sections -Wl,-rpath-link=${NDK_HOME}/toolchains/llvm/prebuilt/darwin-x86_64/sysroot/usr/lib/i686-linux-android/24 -Wl,-rpath-link=./obj/local/x86 ./obj/local/x86/objs/ollvmdebug/__/__/antidebug.o ${NDK_HOME}/sources/cxx-stl/llvm-libc++/libs/x86/libc++_static.a ${NDK_HOME}/sources/cxx-stl/llvm-libc++abi/../llvm-libc++/libs/x86/libc++abi.a ${NDK_HOME}/toolchains/llvm/prebuilt/darwin-x86_64/lib64/clang/12.0.8/lib/linux/i386/libunwind.a -latomic -target i686-none-linux-android24 -no-canonical-prefixes   -Wl,--build-id=sha1 -Wl,--no-rosegment  -nostdlib++ -Wl,--no-undefined -Wl,--fatal-warnings -llog -lc -lm -o ./obj/local/x86/ollvmdebug
mkdir -p libs/x86
echo [x86] "Install        ": "ollvmdebug => libs/x86/ollvmdebug"
install -p ./obj/local/x86/ollvmdebug ./libs/x86/ollvmdebug
${NDK_HOME}/toolchains/llvm/prebuilt/darwin-x86_64/bin/llvm-strip --strip-unneeded  ./libs/x86/ollvmdebug
