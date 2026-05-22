[app]
title = Voicebot
package.name = offlinevoicebot
package.domain = org.rahmats
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,gstyle,wav,model
version = 1.0

# Vosk compilation ko bypass karne aur static load ke liye requirements
requirements = python3, kivy==2.1.0, android, jnius

orientation = portrait
fullscreen = 1

android.permissions = INTERNET, RECORD_AUDIO, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE
android.api = 33
android.minapi = 21
android.ndk_api = 21
android.archs = arm64-v8a
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1
