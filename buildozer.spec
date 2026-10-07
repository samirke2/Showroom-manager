[app]
title = ShowroomManager
package.name = ShowroomManager
package.domain = org.ShowroomManager
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,xml
source.exclude_dirs = bin, .buildozer, venv, __pycache__, .git
source.exclude_patterns = *.db, startup_error.txt, *.pdf, *.log

version = 1.1.1

icon.filename = %(source.dir)s/icon.png
presplash.filename = %(source.dir)s/splash.png
presplash.color = #020B1E

requirements = python3==3.10.11,hostpython3==3.10.11,kivy==2.3.0,kivymd==1.1.1,sqlite3,pillow,reportlab,cryptography,arabic-reshaper,python-bidi==0.4.2,pypdf

orientation = portrait
fullscreen = 0

android.api = 33
android.minapi = 24
android.ndk = 25b
android.ndk_api = 24
android.archs = arm64-v8a
android.accept_sdk_license = True

android.permissions = INTERNET, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, READ_MEDIA_IMAGES

android.enable_androidx = True
android.gradle_dependencies = androidx.core:core:1.9.0
android.extra_manifest_application_arguments = ./manifest_app_extra.xml
android.add_resources = ./xml/file_paths.xml:xml

android.allow_backup = True
android.logcat_filters = *:S python:D

p4a.branch = v2024.01.21

[buildozer]
log_level = 2
warn_on_root = 0