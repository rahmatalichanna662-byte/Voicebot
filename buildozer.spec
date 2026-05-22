[app]

# (str) Title of your application
title = Voicebot

# (str) Package name
package.name = offlinevoicebot

# (str) Package domain (needed for android packaging)
package.domain = org.rahmats

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning (method 1)
version = 1.0

# (list) Application requirements
# Vosk aur PyAudio ko bina internet processing ke liye add kiya hai
requirements = python3,kivy==2.1.0,vosk,pyaudio,setuptools

# (str) Supported orientations (valid options are: landscape, portrait, all)
orientation = portrait

# -----------------------------------------------------------------------------
# Android specific configuration

# (list) Permissions required by the app (Microphone recording sabse zaroori hai)
android.permissions = INTERNET, RECORD_AUDIO, MODIFY_AUDIO_SETTINGS

# (int) Target Android API
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Use architectures like armeabi-v7a or arm64-v8a (Aapke phone ke mutabiq)
android.archs = arm64-v8a, armeabi-v7a

# (bool) Allow backup
android.allow_backup = True

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root
warn_on_root = 1
