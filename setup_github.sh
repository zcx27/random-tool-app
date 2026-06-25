#!/bin/bash
cd /c/temp_app

# 配置 git 用户
git config user.email "zcx@example.com"
git config user.name "zcx"

# 提交代码
git commit -m "初版：专业随机工具 - Kivy Android App

功能：随机数生成、随机选择器、列表随机化
配置：buildozer + GitHub Actions 自动构建 APK
修复：字体注册、Android 检测、Python 3.14 兼容补丁"

echo "✅ 代码已提交"
echo ""
echo "============================================"
echo "现在需要登录 GitHub 并创建仓库"
echo "============================================"
echo ""
echo "请打开浏览器登录 GitHub，然后按回车继续..."
