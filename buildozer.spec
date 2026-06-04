[app]

title = Discord Clone
package.name = pythonchat
package.domain = org.anuj

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas

version = 0.1

requirements = python3,kivy==2.3.0,kivymd==1.2.0

orientation = portrait

fullscreen = 0

android.permissions = INTERNET

android.api = 33
android.minapi = 24
android.ndk = 25b

android.archs = arm64-v8a

android.accept_sdk_license = 1

# Main file
source.main = main.py

[buildozer]

log_level = 2
warn_on_root = 1
