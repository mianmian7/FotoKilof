[![PyPI](https://img.shields.io/pypi/v/fotokilof.svg)](https://pypi.org/project/FotoKilof/)
[![Python versions](https://img.shields.io/pypi/pyversions/fotokilof.svg)](https://pypi.org/project/FotoKilof/)
[![Test & publish](https://github.com/TeaM-TL/FotoKilof/workflows/Build%20and%20upload%20to%20PyPI%20when%20a%20Release%20is%20Created/badge.svg)](https://github.com/TeaM-TL/FotoKilof/actions/workflows/publish_to_pypi.yml?query=workflow%3A%22Build+and+upload+to+PyPI+when+a+Release+is+Created%22)

[English](README_EN.md)

# FotoKilof - ImageMagick 的图形用户界面

一个为我最常用的 ImageMagick 功能设计的图形用户界面，用于处理图片。
如果 ImageMagick 或 Wand 不可用，则使用 Pillow。虽然有一些小限制，但基本上可以正常工作。

## 屏幕截图

### Linux

![Screenshot](https://raw.githubusercontent.com/TeaM-TL/FotoKilof/master/screenshots/fotokilof_linux.png)

### Linux 深色模式

![Screenshot](https://raw.githubusercontent.com/TeaM-TL/FotoKilof/master/screenshots/fotokilof_linux_dark.png)

### Windows

![Screenshot Windows](https://raw.githubusercontent.com/TeaM-TL/FotoKilof/master/screenshots/fotokilof_windows.png)

### macOS 合成

![Screenshot Windows](https://raw.githubusercontent.com/TeaM-TL/FotoKilof/master/screenshots/fotokilof_compose.png)

## 图形转换

 - 缩放/调整大小，
 - 裁剪，
 - 在图片内外添加文本注释（表情包生成器），
 - 在图片周围添加边框，
 - 旋转，
 - 镜像（垂直或水平），
 - 黑白，
 - 棕褐色 - 仅适用于 Wand 和 ImageMagick，
 - 增加/减少对比度或标准化或直方图拉伸，
 - 颜色自动色阶或均衡，
 - 晕影 - 仅适用于 Wand 和 ImageMagick，
 - 在图片上添加徽标图像，
 - 将两张图片合成为一张，
 - 文件格式：JPG、PNG、TIFF、SVG，
 - 将格式转换为 JPG、PNG、TIFF。

## 功能：

 - 处理 JPG、PNG、SVG 和 TIFF 图像，
 - 即时处理图片，原始文件安全，
 - 处理单个文件或整个目录，
 - 从剪贴板获取图片并将其用作源图片，
 - 处理后，结果将复制到剪贴板，
 - 显示选定的工具，
 - 工具选择，
 - 预览原始和结果，
 - 预定义的旋转：90、180 和 270 度或自定义，
 - 通过单击预览或坐标选择裁剪区域，
 - 裁剪坐标：
   - 两个角（左上和右下），
   - 左上角以及宽度和高度，
   - 重心、宽度、高度和偏移量，
 - 文本：颜色、字体和大小选择、背景、旋转，
 - 文本位置：
   - 外部：底部、左/中/右
   - 内部：按重心或按位置和旋转
 - 自定义棕褐色 - 仅适用于 Wand 和 ImageMagick，
 - 按通道均衡，
 - 对比度在 -5 和 +5 之间，
 - 自定义对比度拉伸，
 - 晕影：
   - 可以是锐利或模糊的，
   - 角可以用选定的颜色填充，
   - 双向偏移
 - 按重心、大小和偏移量定位徽标，
 - 合成：
   - 在右侧添加图片
   - 在底部添加图片
   - 自动调整图片大小
   - 如果不自动调整大小，则填充颜色
 - 快速文件导航：第一张、上一张、下一张、最后一张或按键：Home、PgUp、PgDn、End，
 - 命令编辑器：可以使用 ImageMagick 命令进行转换：例如 *-gaussian-blur 10x10* 或 *-monochrome* 等。
- 深色和浅色模式

---

## 处理

可以运行一次转换或所有选定的转换。
所有选定转换的处理顺序：

- 裁剪，
- 镜像，
- 黑白，
- 棕褐色 - 仅适用于 Wand 和 ImageMagick，
- 对比度，
- 色彩标准化，
- 晕影 - 仅适用于 Wand 和 ImageMagick，
- 旋转，
- 边框，
- 调整大小，
- 文本，
- 将两张图片合成为一张，
- 徽标。

处理始终在内存中的图片克隆上进行。原始文件不会被触及。

## 用户手册（有点过时）

- [英语](doc/en/fotokilof.md)，
- [波兰语](doc/pl/fotokilof.md)。

## 可用翻译

可用：简体中文、保加利亚语、英语、德语、印度尼西亚语、波兰语和土耳其语。

---

## 安装和运行

### 要求

- Windows、Linux、MacOS X、BSD，
- 全高清屏幕以获得舒适的工作体验，
- [ImageMagick](https://imagemagick.org/)，请记住将路径添加到 `%PATH%` 环境变量中，并启用安装库！
- [Python3.10+](https://www.python.org/)，请记住将路径添加到 `%PATH%` 环境变量中。

### 安装

#### Linux

安装要求：
```bash
apt-get install python3-pip python3-tk python3-wand imagemagick xclip
```

通过 PIP 安装为 PyPi 包：
```bash
python3 -m pip install fotokilof
```

#### Windows
下载并安装要求：
- [Python3.10+](https://www.python.org/) - 将路径添加到 `%PATH%` 环境变量中，
- [ImageMagick](https://imagemagick.org/script/download.php#windows) - 将路径添加到 `%PATH%` 环境变量中，并启用安装库！

```bash
python -m pip install fotokilof
```

#### MacOS
安装要求：
```bash
brew install imagemagick python@3.13 python-tk@3.13
```

对于基于 Apple Silicon (M1, M2, M3) 的 Mac，默认的 Homebrew 安装目录与 Intel 安装的 Homebrew 不同。以下环境变量允许 FotoKilof 在 Apple Silicon Mac 上正确定位 Homebrew 安装的 ImageMagick：
```bash
export MAGICK_HOME=/opt/homebrew
```

通过 PIP 安装为 PyPi 包：
```bash
python3 -m pip install fotokilof
```

#### FreeBSD

FotoKilof 可通过 [ports](https://www.freshports.org/graphics/py-fotokilof/) 获得

```bash
pkg install py311-fotokilof
```

### 升级

```bash
python3 -m pip install --upgrade fotokilof
```

### 运行

```bash
fotokilof
```
或
```bash
python -m fotokilof
```

### 深色或浅色模式

按 F2 在浅色和深色模式之间切换。

---

## 感谢

 - 朋友们 - 一些想法和测试，
 - Max von Forell - 德语翻译，
 - Bozhidar Kirev - 保加利亚语翻译，
 - Alexander Ignatov - 保加利亚语翻译，
 - Afif Hendrawan - 印度尼西亚语翻译，
 - Sebastian Hiebl - python 打包，
 - Matt Sephton - 打包 gui 的想法，
 - emsspree - 更新德语翻译，jpeg，
 - Olm - 在 Windows 上测试，
 - Carbene Hu - 修复问题的想法
 - Mert Cobanov - 土耳其语翻译
 - Giancarlo Dessì - 意大利语翻译，Slackware 包
 - Danny (dchenz) - 正确的日志记录方式
 - Nicola Vitale - 支持调试和寻找解决方案

---

## Star 历史

[![Star History Chart](https://api.star-history.com/svg?repos=TeaM-TL/FotoKilof&type=Date)](https://star-history.com/#TeaM-TL/FotoKilof&Date)

---

## 技术支持

![Python powered](python-powered.png)
[Imagemagick](https://github.com/ImageMagick/ImageMagick)
[Wand](https://github.com/emcconville/wand)
[ttkbootstrap](https://github.com/israel-dryer/ttkbootstrap)
[Pillow](https://github.com/python-pillow/Pillow)
[FindSystemFontsFilename](https://github.com/moi15moi/FindSystemFontsFilename)
[pyperclipimg](https://github.com/asweigart/pyperclipimg)
