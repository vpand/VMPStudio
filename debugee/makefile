armmac: antidebug.cpp
	$(clang_vmp)++ -isysroot /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk -arch arm64 -Os -o armmac/ollvmdebug.o -c antidebug.cpp
	clang++ -arch arm64 -Os -o armmac/ollvmdebug armmac/ollvmdebug.o

ios: antidebug.cpp
	$(clang_vmp)++ -target arm64-apple-ios10.0 -isysroot /Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS.sdk -Os -o ios/ollvmdebug.o -c antidebug.cpp
	clang++ -target arm64-apple-ios10.0 -isysroot /Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS.sdk -o ios/ollvmdebug ios/ollvmdebug.o

mac: antidebug.cpp
	$(clang_vmp)++ -isysroot /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk -arch x86_64 -Os -o mac/ollvmdebug.o -c antidebug.cpp
	clang++ -arch x86_64 -Os -o mac/ollvmdebug mac/ollvmdebug.o
