# 专业随机工具

一个基于 Kivy 的移动端随机工具 App，支持随机数生成、随机选择器和列表随机化功能。

## 从 GitHub Actions 下载 APK

1. 打开 https://github.com/你的用户名/random-tool-app/actions
2. 点击 **"构建 Android APK"** 工作流
3. 点击 **"Run workflow"** 按钮
4. 等待 20-40 分钟，构建完成后点击运行记录
5. 在 **Artifacts** 部分下载 `专业随机工具-APK.zip`
6. 解压后得到 `.apk` 文件，传到手机安装

## 本地运行

```bash
pip install kivy
python main.py
```

## 功能

- **随机数生成**：设置范围，生成 1-10 个随机数
- **随机选择器**：输入多个候选项，随机选一个
- **列表随机化**：输入列表，随机打乱顺序
- **彩蛋**：连续点击 5 次"随机选择"有惊喜

## 技术栈

- Python 3 + Kivy 2.3
- Buildozer + Python-for-Android（打包）
- GitHub Actions（CI/CD）
