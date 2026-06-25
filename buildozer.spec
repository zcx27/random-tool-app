[app]

# 应用信息
title = 专业随机工具
package.name = professionalrandomtool
package.domain = org.zcx24
source.dir = .
source.include_exts = py,png,jpg,kv,ttf

# 版本信息
version = 1.0
requirements = python3==3.12,kivy==2.3.0,hostpython3==3.12

# 主程序入口
orientation = portrait
fullscreen = 0

# Android配置 - 仅构建 arm64-v8a（兼容最新手机）
android.archs = arm64-v8a
android.api = 33
android.minapi = 21
android.ndk = 25b

# 权限设置
android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

# 接受SDK许可（线上构建自动下载 SDK/NDK）
android.accept_sdk_license = True

[buildozer]

# 日志级别
log_level = 2

# 允许自动下载 SDK/NDK（只在 GitHub Actions 等有网络的 CI 中使用）
# 本地构建建议设置 p4a.offline = True
# p4a.offline = True
