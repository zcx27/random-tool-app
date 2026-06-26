[app]

# 应用信息
title = 专业随机工具
package.name = professionalrandomtool
package.domain = org.zcx24
source.dir = .
source.include_exts = py,png,jpg,kv,ttf

# 版本信息
version = 1.0
requirements = python3,kivy==2.3.0

# 主程序入口
orientation = portrait
fullscreen = 0

# Android配置
android.archs = arm64-v8a
android.api = 33
android.minapi = 21
android.ndk = 25b

# 权限设置
android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

# 接受SDK许可
android.accept_sdk_license = True

[buildozer]

# 构建目录
log_level = 2

# 在线模式（GitHub Actions 需要联网下载 p4a）
# p4a.offline = True
