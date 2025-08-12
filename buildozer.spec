[app]

# (str) Title of your application
title = F2C Weather App

# (str) Package name
package.name = f2cweatherapp

# (str) Package domain (needed for android/ios packaging)
package.domain = net.idux.f2cweatherapp

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let buildozer find them)
source.include_exts = py,png,jpg,kv,atlas

# (list) List of inclusions using pattern matching
#source.include_patterns = assets/*,images/*.png

# (list) List of exclusions using pattern matching
#source.exclude_patterns = tests/*

# (str) Application versioning (method 1)
version = 1.0

# (str) Application versioning (method 2)
# version.regex = __version__ = ['"](.*)['"]
# version.filename = %(source.dir)s/main.py

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy,bleak

# (str) Custom source folders for requirements
# requirements.source.kivymd = ../../kivymd

# (str) Presplash background color (for new android toolchain)
# Supported formats are: #RRGGBB #AARRGGBB or one of the following names:
# red, blue, green, black, white, fuchsia, lime, maroon, navy, olive,
# purple, silver, teal, yellow.
#android.presplash_color = #FFFFFF

# (str) Presplash animation using Lottie format.
# see https://lottiefiles.com/
# android.presplash_lottie = "path/to/lottie/file.json"

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (str) Presplash image
#presplash.filename = %(source.dir)s/data/presplash.png

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = BLUETOOTH, BLUETOOTH_ADMIN, BLUETOOTH_SCAN, BLUETOOTH_CONNECT

# (int) Android API to use
#android.api = 27

# (int) Minimum API required
#android.minapi = 21

# (int) Android SDK version to use
#android.sdk = 20

# (str) Android NDK version to use
#android.ndk = 19b

# (int) Android NDK API to use
#android.ndk_api = 21

# (bool) Use --private data storage (True) or --dir public storage (False)
#android.private_storage = True

# (str) Android entry point, default is ok for Kivy applications
#android.entrypoint = org.kivy.android.PythonActivity

# (str) Android app theme, default is ok for Kivy applications
#android.apptheme = "@android:style/Theme.NoTitleBar"

# (list) Pattern to whitelist for the whole project
#android.whitelist =

# (str) Path to a custom whitelist file
#android.whitelist_src =

# (str) Path to a custom blacklist file
#android.blacklist_src =

# (list) List of Java files to add to the android project
#android.add_src =

# (list) List of Java files to add to the android project
#android.add_libs_armeabi_v7a = libs/android/*.so
#android.add_libs_arm64_v8a = libs/android-arm64/*.so
#android.add_libs_x86 = libs/android-x86/*.so
#android.add_libs_x86_64 = libs/android-x86_64/*.so

# (bool) Bomb out if inspect fails
#android.allow_backup = True

# (str) XML file to include as an intent filter
#android.manifest.intent_filters =

# (str) Launch mode for activity
#android.manifest.launch_mode = standard

# (list) Android additional libraries to copy into libs/armeabi
#android.add_jars = foo.jar,bar.jar,path/to/more/jars/*.jar

# (list) Android hardware features to require
#android.hardware_features = android.hardware.usb.host

# (list) copy files in case of big app
#android.big_app_files =

[buildozer]

# (int) Log level (0 = error, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

android.build_tools_version = 36.0.0