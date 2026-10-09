[app]

# =====================================================================
#  (str) Title of your application
# =====================================================================
title = Showroom DZ

# =====================================================================
#  (str) Package name
# =====================================================================
package.name = showroomdz

# =====================================================================
#  (str) Package domain (needed for android/ios packaging)
# =====================================================================
package.domain = org.samirpyth

# =====================================================================
#  (str) Source code where the main.py live
# =====================================================================
source.dir = .

# =====================================================================
#  (list) Source files to include (let empty to include all the files)
# =====================================================================
source.include_exts = py,png,jpg,jpeg,kv,atlas,ttf,otf,json,txt,db

# =====================================================================
#  (list) Source files to exclude (let empty to not exclude anything)
# =====================================================================
source.exclude_exts = spec,md,gitignore

# =====================================================================
#  (list) List of directory to exclude (let empty to not exclude anything)
# =====================================================================
source.exclude_dirs = __pycache__, .git, .idea, bin, build, tests

# =====================================================================
#  (list) List of exclusions using pattern matching
# =====================================================================
source.exclude_patterns = license,images/*/*.jpg,*.pyc,__pycache__/*,*.log,crash_log.txt,startup_error.txt

# =====================================================================
#  (str) Application versioning (method 1)
# =====================================================================
version = 1.1.1

# =====================================================================
#  (list) Application requirements
# =====================================================================
requirements = python3,kivy==2.3.0,kivymd==1.1.1,pillow,arabic-reshaper,python-bidi,reportlab,cryptography,pypdf,pyjnius,android

# =====================================================================
#  (str) Custom source folders for requirements
# =====================================================================
# requirements.source.kivy = ../../kivy

# =====================================================================
#  (list) Garden requirements
# =====================================================================
# garden_requirements = 

# =====================================================================
#  (str) Presplash of the application
# =====================================================================
presplash.filename = %(source.dir)s/splash.png

# =====================================================================
#  (str) Icon of the application
# =====================================================================
icon.filename = %(source.dir)s/icon.png

# =====================================================================
#  (str) Supported orientation
# =====================================================================
orientation = portrait

# =====================================================================
#  (list) List of service to declare
# =====================================================================
# services = NAME:ENTRYPOINT_TO_PY,NAME2:ENTRYPOINT2_TO_PY

# =====================================================================
#  OSX specific
# =====================================================================
# osx.python_version = 3
# osx.kivy_version = 1.9.1

# =====================================================================
#  Android specific
# =====================================================================
# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (string) Presplash background color (for new android toolchain)
android.presplash_color = #0B5394

# (list) Permissions
android.permissions = INTERNET,ACCESS_NETWORK_STATE,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,READ_MEDIA_IMAGES,READ_MEDIA_VIDEO,READ_MEDIA_AUDIO,MANAGE_EXTERNAL_STORAGE

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK / AAB will support.
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 33

# (str) Android NDK version to use
android.ndk = 25b

# (int) Android NDK API to use. This is the minimum API your app will support, it should usually match android.minapi.
android.ndk_api = 21

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# (str) Android NDK directory (if empty, it will be automatically downloaded.)
# android.ndk_path =

# (str) Android SDK directory (if empty, it will be automatically downloaded.)
# android.sdk_path =

# (str) ANT directory (if empty, it will be automatically downloaded.)
# android.ant_path =

# (bool) If True, then skip trying to update the Android sdk
# This can be useful to avoid excess Internet downloads or save time
# when an update is due and you just want to test/build your package
android.skip_update = False

# (bool) If True, then automatically accept SDK license
# agreements. This is intended for automation only. If set to False,
# the default, you will be shown the license when first running
# buildozer.
android.accept_sdk_license = True

# (str) Android entry point, default is ok for Kivy-based app
# android.entrypoint = org.kivy.android.PythonActivity

# (str) Full name including package path of the Java class that implements Android Activity
# use that parameter together with android.entrypoint to set custom Java class instead of PythonActivity
# android.activity_class_name = org.kivy.android.PythonActivity

# (str) Extra xml to write directly inside the <manifest> element of AndroidManifest.xml
# use that parameter to provide a filename from where to load your custom XML code
# android.extra_manifest_xml = ./src/android/extra_manifest.xml

# (str) Extra xml to write directly inside the <manifest><application> tag of AndroidManifest.xml
# use that parameter to provide a filename from where to load your custom XML code
# android.extra_manifest_application_xml = ./src/android/extra_manifest.xml

# (str) Full name including package path of the Java class that implements Android Service
# android.service_class_name = org.kivy.android.PythonService

# (str) Android app theme, default is ok for Kivy-based app
# android.apptheme = "@android:style/Theme.NoTitleBar"

# (list) Pattern to whitelist for the whole project
# android.whitelist =

# (str) Path to a custom whitelist file
# android.whitelist_src =

# (str) Path to a custom blacklist file
# android.blacklist_src =

# (list) List of Java .jar files to add to the libs so that pyjnius can access
# their classes. Don't add jars that you do not need, since extra jars can slow
# down the build process. Allows wildcards matching, for example:
# OUYA-ODK/libs/*.jar
# android.add_jars = foo.jar,bar.jar,path/to/more/*.jar

# (list) List of Java files to add to the android project (can be java or a
# directory containing the files)
# android.add_src =

# (list) Android AAR archives to add
# android.add_aars =

# (list) Put these files or directories in the apk assets directory.
# android.add_assets =

# (list) Gradle dependencies to add
android.gradle_dependencies = 

# (bool) Enable AndroidX support. Enable when 'android.gradle_dependencies'
# contains an 'androidx' package, or any package that requires AndroidX
android.enable_androidx = True

# (list) add java compile options
# android.add_compile_options = "sourceCompatibility = 1.8", "targetCompatibility = 1.8"

# (list) NDK projections
# android.ndk_projectcflags =

# (list) Android application meta-data to set (key=value format)
# android.meta_data =

# (list) Android library project to add (will be added in the
# project.properties automatically.)
# android.library_references =

# (list) Android shared libraries which will be added to AndroidManifest.xml using <uses-library> tag
# android.uses_library =

# (str) Android logcat filters to use
android.logcat_filters = *:S python:D

# (bool) Copy library instead of making a libpymodules.so
android.copy_libs = 1

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.archs = arm64-v8a, armeabi-v7a

# (int) overrides automatic versionCode computation (used in build.gradle)
# android.numeric_version = 1

# (bool) enables Android auto backup feature (Android API >=23)
android.allow_backup = True

# (str) XML file to include as an intent filters in <activity> tag
# android.manifest.intent_filters =

# (str) launchMode to set for the main activity
# android.manifest.launch_mode = standard

# (list) Android additionnal libraries to copy into libs/armeabi
# android.add_libs_armeabi = libs/android/*.so
# android.add_libs_armeabi_v7a = libs/android-v7/*.so
# android.add_libs_x86 = libs/android-x86/*.so
# android.add_libs_mips = libs/android-mips/*.so

# (bool) Indicate whether the screen should stay on
# android.wakelock = False

# (list) List of Java classes that should be in "android:name" attribute of
# <uses-library> tags
# android.uses_library =

# =====================================================================
#  iOS specific
# =====================================================================
# (str) Title of your application
# ios.title = Showroom DZ
# ios.icon.filename = icon.png
# ios.presplash.filename = splash.png

# =====================================================================
#  Kivy specific
# =====================================================================
# (bool) If True, all the KV files are saved as bytecode
# kivy.kv_files_bytecode = True

# (list) List of directories to exclude from being compiled to bytecode
# kivy.kv_files_exclude_dirs =

# (str) Presplash of the application (PNG or JPG)
# presplash.filename = %(source.dir)s/splash.png

# =====================================================================
#  Buildozer specific
# =====================================================================
# (str) Path to build artifact storage, absolute or relative to spec file
# build_dir = ./.buildozer

# (str) Path to build output (i.e. .apk, .ipa) storage
bin_dir = ./bin

# (bool) Store the build in an AAB
# android.release_artifact = aab

# (list) List of keystores and their associated signing credentials
# android.keystore = 
# android.keystore_passwd = 
# android.keystore_alias = 
# android.keystore_alias_passwd = 