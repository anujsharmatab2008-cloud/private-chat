[app]
# (str) Title of your application
title = Discord Clone

# (str) Package name
package.name = pythonchat

# (str) Package domain (needed for android packaging)
package.domain = org.anuj

# (str) Source code directory
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 0.1

# (list) Application requirements
# Crucial: Installs Python 3, core Kivy, and Material Design UI elements
requirements = python3, kivy, kivymd

# (str) Supported orientations (landscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# =============================================================================
# Android specific configuration
# =============================================================================

# (list) Permissions
# Crucial: Allows your mobile app to talk to your desktop room server
android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) If True, then skip trying to update the Android sdk
android.skip_update = 0

# (bool) If True, then automatically accept SDK licenses
android.accept_sdk_license = 1

# (str) The Android architectural format
android.archs = arm64-v8a

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root
warn_on_root = 1
