import os

# 检测是否为 Android 环境
IS_ANDROID = False
STORAGE_PATH = os.getcwd()

# 在导入 Kivy 之前设置 Config
from kivy.config import Config
Config.set('graphics', 'resizable', True)
# 不设置固定宽高，让 Android 自动适配屏幕

try:
    # 优先尝试 android_config 模块检测
    from android_config import setup_android, get_android_storage_path
    IS_ANDROID = setup_android()
    STORAGE_PATH = get_android_storage_path()
except ImportError:
    # android_config 不存在时，通过环境变量检测
    if os.environ.get('KIVY_BUILD') == 'android':
        IS_ANDROID = True
        try:
            from android.permissions import request_permissions, Permission
            request_permissions([Permission.INTERNET, Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])
            from android.storage import primary_external_storage_path
            STORAGE_PATH = primary_external_storage_path()
        except ImportError:
            pass

# 桌面环境设置
if not IS_ANDROID:
    from kivy.core.window import Window
    Window.size = (360, 640)
    os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

import kivy

kivy.require('2.3.0')

from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.core.text import LabelBase
from kivy.graphics import Color, Rectangle, RoundedRectangle
from kivy.clock import Clock
from kivy.metrics import dp, sp
import random
from datetime import datetime
import time


# ============================================
# 字体设置
# ============================================

def setup_fonts():
    """设置中文字体"""
    import sys
    if hasattr(sys, 'getandroidapilevel') or os.environ.get('KIVY_BUILD') == 'android':
        from kivy.core.text import LabelBase
        LabelBase.register(name='ChineseFont', fn_regular='')
        return

    for font in ['C:/Windows/Fonts/msyh.ttc', 'C:/Windows/Fonts/simhei.ttf', 'C:/Windows/Fonts/simsun.ttc']:
        if os.path.exists(font):
            try:
                from kivy.core.text import LabelBase
                LabelBase.register(name='ChineseFont', fn_regular=font)
                return
            except:
                continue
class ThemeManager:
    """主题管理器"""
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ThemeManager, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if hasattr(self, '_initialized') and self._initialized:
            return

        self._initialized = True

        # 经典智慧名言
        self.wisdom_quotes = [
            "你陪了我多少年，花开花落，一路上起起跌跌。",
            "每个人生来都是孤独的，这是人之宿命。但我总想着，或许有那么一个人……能让我不再孤独。",
            "命运这种东西，生来就是要被踏于足下的。",
            "没有什么会永远存在，但有些东西却可以永远留在心里。",
            "如果我能早点长大，是不是就不会失去你了。",
            "活着的人都是戴着枷锁前行，因为心里装着逝去的人。",
            "不是忘记，而是想不起来。",
            "我们走过的每一步不一定是完美的，但每一步都有值得深思的意义。",
            "无法舍弃任何东西的人，什么也改变不了。",
            "我们总是在注意错过太多，却不注意自己拥有多少。",
            "真正痛苦的事不是不能向人求助，而是没有一个可以求助的人。",
            "死亡不是生命的终点，遗忘才是。",
            "世界不会因为你而改变，但你能改变自己的世界。",
            "酷酷哥哥周的温馨提示：要珍惜当下。",
            "再见。",
            "少年之所以无忧无虑，是因为有人为其撑伞。",
            "不用为某些人的离开而难过，要知道人生有这么长，绝大部分人不过只是属于你故事里的过客。",
            "我们注定走向分离，就像河流终将入海。",
            "人并不能完全记住过去发生的事情，所谓记忆，其实是在不断被当下修改和重构的。",
            "谢谢。",
            "something for nothing。",
        ]

        self.current_quote = random.choice(self.wisdom_quotes)

        self.settings = {
            'last_min_value': '0',
            'last_max_value': '100'
        }

        # 适配浅黄背景的配色方案
        self.themes = {
            'mobile': {  # 移动端主题
                'name': '移动端',
                'bg_image': self._get_bg_path('我的背景1'),
                'bg_opacity': 0.9,
                'colors': {
                    # 字体颜色 - 适配浅黄背景的深色调
                    'text_primary': (0.25, 0.2, 0.1, 1),  # 深棕黄色
                    'text_secondary': (0.4, 0.35, 0.2, 1),  # 中棕黄色
                    'text_highlight': (0.6, 0.45, 0.1, 1),  # 金棕色
                    'text_button': (0.95, 0.95, 0.9, 1),  # 浅黄色

                    # 按钮颜色 - 温暖色调，适配浅黄背景
                    'button_primary': (0.85, 0.65, 0.2, 1),  # 金色
                    'button_secondary': (0.75, 0.55, 0.15, 1),  # 深金色
                    'button_accent': (0.9, 0.75, 0.3, 1),  # 浅金色
                    'button_error': (0.8, 0.4, 0.3, 1),  # 暖红色
                    'button_history': (0.8, 0.7, 0.4, 0.95),  # 米黄色

                    # 输入框 - 半透明白色，适配背景
                    'input_bg': (1, 1, 0.98, 0.9),  # 浅黄色
                    'input_text': (0.3, 0.25, 0.15, 1),  # 深棕
                    'input_hint': (0.65, 0.6, 0.4, 0.9),  # 中棕色
                    'input_border': (0.9, 0.85, 0.7, 0.8),  # 浅金边框

                    # 内容区域 - 半透明白色
                    'content_bg': (1, 1, 0.98, 0.9),  # 浅黄色

                    # 标签页
                    'tab_bg': (0.97, 0.95, 0.9, 0.95),  # 浅黄色
                    'tab_text': (0.4, 0.35, 0.2, 1),  # 棕黄色
                }
            }
        }

        self.current_theme = 'mobile'
        self._check_backgrounds()

    def _get_bg_path(self, bg_name):
        """获取背景图片路径"""
        search_dirs = ['backgrounds', '.']
        extensions = ['.jpg', '.jpeg', '.png', '.gif']
        for sd in search_dirs:
            for ext in extensions:
                path = f"{sd}/{bg_name}{ext}"
                if os.path.exists(path):
                    return path
        if os.path.exists('backgrounds'):
            try:
                for file in os.listdir('backgrounds'):
                    if bg_name in file:
                        return os.path.join('backgrounds', file)
            except:
                pass
        return None

    def _check_backgrounds(self):
        """检查背景图片"""
        pass

    def get_current_theme(self):
        return self.themes[self.current_theme]

    def get_color(self, color_name):
        theme = self.get_current_theme()
        return theme['colors'].get(color_name, (1, 1, 1, 1))

    def get_setting(self, key):
        return self.settings.get(key, None)

    def set_setting(self, key, value):
        self.settings[key] = value

    def get_random_quote(self):
        return self.current_quote


# ============================================
# 彩蛋管理器
# ============================================

class EasterEggManager:
    """彩蛋管理器"""

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(EasterEggManager, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if hasattr(self, '_initialized') and self._initialized:
            return

        self._initialized = True
        self.selection_count = 0  # 随机选择器的点击次数
        self.last_selection_time = 0  # 上次选择时间
        self.cooldown_seconds = 5  # 冷却时间（秒）

    def record_selection(self):
        """记录随机选择器的使用"""
        current_time = time.time()

        # 检查是否在冷却时间内
        if current_time - self.last_selection_time > self.cooldown_seconds:
            self.selection_count = 0  # 重置计数

        self.selection_count += 1
        self.last_selection_time = current_time

        # 检查是否触发彩蛋
        if self.selection_count >= 5:
            self.trigger_easter_egg()
            self.selection_count = 0  # 触发后重置

    def trigger_easter_egg(self):
        """触发彩蛋"""
        # 创建彩蛋弹窗
        egg_content = BoxLayout(orientation='vertical', spacing=10, padding=[20, 20], size_hint=(1, 1))

        # 彩蛋内容 - 使用ThemeLabel确保居中
        egg_text = ThemeLabel(
            text='遵从内心的想法，\n\n你的选择往往就是最好的选择。',
            text_type='primary',
            font_size=16,
            halign='center',
            valign='middle'
        )
        egg_text.bind(size=egg_text.setter('text_size'))
        egg_content.add_widget(egg_text)

        # 创建弹窗
        popup = Popup(
            title='',
            title_size=0,
            content=egg_content,
            size_hint=(0.65, 0.4),  # 更小的弹窗
            separator_height=0,
            background=''
        )

        # 为背景添加圆角和浅黄色背景
        with popup.canvas.before:
            Color(1, 0.98, 0.9, 0.98)  # 浅黄色背景
            popup.bg_rect = RoundedRectangle(radius=[15])

        def update_bg(instance, value):
            popup.bg_rect.pos = instance.pos
            popup.bg_rect.size = instance.size

        popup.bind(pos=update_bg, size=update_bg)

        # 自动关闭弹窗（3秒后）
        Clock.schedule_once(lambda dt: popup.dismiss(), 3)
        popup.open()


# ============================================
# 主题化控件
# ============================================

class ThemeLabel(Label):
    def __init__(self, text_type='primary', **kwargs):
        super().__init__(**kwargs)
        self.font_name = 'ChineseFont'
        self.text_type = text_type
        self.theme_manager = ThemeManager()

        if 'text_size' not in kwargs:
            self.bind(size=self._update_text_size)

        Clock.schedule_once(self.apply_theme, 0.1)

    def _update_text_size(self, instance, value):
        self.text_size = self.size

    def apply_theme(self, dt=0):
        theme = self.theme_manager.get_current_theme()
        colors = theme['colors']

        if self.text_type == 'primary':
            self.color = colors['text_primary']
        elif self.text_type == 'secondary':
            self.color = colors['text_secondary']
        elif self.text_type == 'highlight':
            self.color = colors['text_highlight']
        else:
            self.color = colors['text_primary']


class ThemeButton(Button):
    def __init__(self, button_type='primary', **kwargs):
        super().__init__(**kwargs)
        self.font_name = 'ChineseFont'
        self.button_type = button_type

        self.background_normal = ''
        self.background_down = ''
        self.background_color = (1, 1, 1, 0)

        # 移动端按钮更大，方便触摸
        self.size_hint = (None, None) if 'size_hint' not in kwargs else kwargs['size_hint']
        self.height = 50 if 'height' not in kwargs else kwargs['height']

        Clock.schedule_once(self.apply_theme, 0.1)
        self.bind(size=self._update_rect, pos=self._update_rect)

    def apply_theme(self, dt=0):
        theme_manager = ThemeManager()
        theme = theme_manager.get_current_theme()
        colors = theme['colors']

        if self.button_type == 'primary':
            bg_color = colors['button_primary']
        elif self.button_type == 'secondary':
            bg_color = colors['button_secondary']
        elif self.button_type == 'accent':
            bg_color = colors['button_accent']
        elif self.button_type == 'error':
            bg_color = colors['button_error']
        elif self.button_type == 'history':
            bg_color = colors['button_history']
        else:
            bg_color = colors['button_primary']

        with self.canvas.before:
            # 底部阴影
            Color(0, 0, 0, 0.12)
            self.shadow_rect = RoundedRectangle(radius=[10])
            # 按钮主体
            Color(*bg_color)
            self.bg_rect = RoundedRectangle(radius=[10])

        self.color = colors['text_button']
        self._update_rect()

    def _update_rect(self, *args):
        if hasattr(self, 'shadow_rect'):
            self.shadow_rect.pos = (self.pos[0] + 4, self.pos[1] - 2)
            self.shadow_rect.size = (self.size[0] - 2, self.size[1] - 2)
        if hasattr(self, 'bg_rect'):
            self.bg_rect.pos = (self.pos[0] + 1, self.pos[1] + 1)
            self.bg_rect.size = (self.size[0] - 2, self.size[1] - 2)


class ThemeTextInput(TextInput):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.font_name = 'ChineseFont'
        self.background_normal = ''
        self.background_active = ''
        self.halign = 'center'
        self.padding = [15, 15]

        Clock.schedule_once(self.apply_theme, 0.1)
        self.bind(text=self._center_text)

    def _center_text(self, instance, value):
        self.halign = 'center'

    def apply_theme(self, dt=0):
        theme_manager = ThemeManager()
        theme = theme_manager.get_current_theme()
        colors = theme['colors']

        self.background_color = colors['input_bg']
        self.foreground_color = colors['input_text']
        self.hint_text_color = colors['input_hint']
        self.cursor_color = colors['input_text']
        self.cursor_width = 2


# ============================================
# 背景和内容布局
# ============================================

class BackgroundWidget(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_manager = ThemeManager()

        self.bg_image = Image(
            size=self.size,
            pos=self.pos,
            keep_ratio=False,
            allow_stretch=True,
        )

        self.add_widget(self.bg_image)

        Clock.schedule_once(self.update_background, 0.1)
        self.bind(size=self._update_size, pos=self._update_size)

    def update_background(self, dt=0):
        theme = self.theme_manager.get_current_theme()
        bg_path = theme['bg_image']

        if bg_path:
            self.bg_image.source = bg_path
            self.bg_image.opacity = theme['bg_opacity']
            self.bg_image.reload()
        else:
            self.bg_image.source = ''
            self._draw_gradient()

    def _draw_gradient(self):
        self.canvas.before.clear()
        with self.canvas.before:
            colors = [
                (1.0, 0.85, 0.90),
                (0.95, 0.82, 0.92),
                (0.90, 0.80, 0.95),
                (0.85, 0.82, 0.98),
                (0.80, 0.85, 1.0),
            ]
            bands = 60
            for i in range(bands):
                t = i / bands
                idx = min(int(t * len(colors)), len(colors) - 1)
                c = colors[idx]
                Color(c[0], c[1], c[2], 1)
                Rectangle(pos=(self.x, self.y + i * (self.height / bands)), size=(self.width, self.height / bands + 1))

    def _update_size(self, *args):
        self.bg_image.size = self.size
        self.bg_image.pos = self.pos


class ContentBoxLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.apply_theme, 0.1)

    def apply_theme(self, dt=0):
        theme_manager = ThemeManager()
        theme = theme_manager.get_current_theme()

        with self.canvas.before:
            Color(0, 0, 0, 0.08)
            self.shadow_rect = RoundedRectangle(radius=[15])
            Color(1, 1, 1, 0.88)
            self.bg_rect = RoundedRectangle(radius=[15])

        self.bind(size=self._update_bg, pos=self._update_bg)
        self._update_bg()

    def _update_bg(self, *args):
        if hasattr(self, 'shadow_rect'):
            self.shadow_rect.pos = (self.x + 2, self.y - 3)
            self.shadow_rect.size = self.size
        if hasattr(self, 'bg_rect'):
            self.bg_rect.pos = self.pos
            self.bg_rect.size = self.size


# ============================================
# 标签页
# ============================================

class RandomNumberTab(FloatLayout):
    """随机数生成 - 移动端优化布局（全屏适配版）"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.background_widget = BackgroundWidget()
        self.add_widget(self.background_widget)

        # ScrollView 填满全屏
        scroll_view = ScrollView(size_hint=(1, 1))
        content = ContentBoxLayout(
            orientation='vertical',
            padding=[dp(32), dp(25), dp(32), dp(25)],  # 左右留边 ~85% 宽度
            spacing=dp(18),
            size_hint_y=None,
            size_hint_x=1
        )
        content.bind(minimum_height=content.setter('height'))
        scroll_view.add_widget(content)

        # 标题
        title = ThemeLabel(
            text='随机数生成',
            text_type='primary',
            font_size=sp(30),
            size_hint=(1, None),
            height=dp(58),
            bold=True,
            halign='center'
        )
        content.add_widget(title)

        # 范围设置区域
        range_section = BoxLayout(
            orientation='vertical',
            spacing=dp(14),
            size_hint=(1, None),
            height=dp(160)
        )

        # 最小值行
        min_layout = BoxLayout(
            orientation='horizontal',
            spacing=dp(12),
            size_hint=(1, None),
            height=dp(68)
        )
        min_label = ThemeLabel(
            text='最小值:',
            font_size=sp(20),
            halign='left',
            size_hint_x=0.35
        )
        min_layout.add_widget(min_label)

        self.min_input = ThemeTextInput(
            text='0',
            font_size=sp(24),
            multiline=False,
            size_hint_x=0.65,
            input_filter='int',
            padding=[dp(18), dp(14)],
            halign='center',
            write_tab=False
        )
        min_layout.add_widget(self.min_input)
        range_section.add_widget(min_layout)

        # 最大值行
        max_layout = BoxLayout(
            orientation='horizontal',
            spacing=dp(12),
            size_hint=(1, None),
            height=dp(68)
        )
        max_label = ThemeLabel(
            text='最大值:',
            font_size=sp(20),
            halign='left',
            size_hint_x=0.35
        )
        max_layout.add_widget(max_label)

        self.max_input = ThemeTextInput(
            text='100',
            font_size=sp(24),
            multiline=False,
            size_hint_x=0.65,
            input_filter='int',
            padding=[dp(18), dp(14)],
            halign='center',
            write_tab=False
        )
        max_layout.add_widget(self.max_input)
        range_section.add_widget(max_layout)

        content.add_widget(range_section)

        # 数量控制区域
        count_section = BoxLayout(
            orientation='vertical',
            spacing=dp(10),
            size_hint=(1, None),
            height=dp(110)
        )

        count_title = ThemeLabel(
            text='生成数量 (1-10):',
            text_type='secondary',
            font_size=sp(18),
            size_hint=(1, None),
            height=dp(34),
            halign='center'
        )
        count_section.add_widget(count_title)

        count_slider_layout = BoxLayout(
            orientation='horizontal',
            spacing=dp(18),
            size_hint=(1, None),
            height=dp(64)
        )

        count_slider_layout.add_widget(ThemeLabel(
            text='1',
            font_size=sp(18),
            size_hint_x=0.2,
            halign='center'
        ))

        self.count_input = ThemeTextInput(
            text='1',
            font_size=sp(24),
            multiline=False,
            size_hint_x=0.6,
            input_filter='int',
            padding=[dp(18), dp(14)],
            halign='center'
        )
        count_slider_layout.add_widget(self.count_input)

        count_slider_layout.add_widget(ThemeLabel(
            text='10',
            font_size=sp(18),
            size_hint_x=0.2,
            halign='center'
        ))

        count_section.add_widget(count_slider_layout)
        content.add_widget(count_section)

        # 生成按钮
        gen_btn = ThemeButton(
            text='生成随机数',
            button_type='primary',
            size_hint=(1, None),
            height=dp(52),
            font_size=sp(20)
        )
        gen_btn.bind(on_press=self.generate_random)
        content.add_widget(gen_btn)

        # 结果区域
        self.result_label = ThemeLabel(
            text='点击上方按钮生成随机数',
            text_type='highlight',
            font_size=sp(22),
            size_hint=(1, None),
            height=dp(110),
            halign='center',
            valign='middle',
            bold=True
        )
        self.result_label.bind(size=self.result_label.setter('text_size'))
        content.add_widget(self.result_label)

        # 历史记录按钮
        history_btn = ThemeButton(
            text='查看历史记录',
            button_type='history',
            size_hint=(1, None),
            height=dp(48),
            font_size=sp(18)
        )
        history_btn.bind(on_press=self.show_history)
        content.add_widget(history_btn)

        self.add_widget(scroll_view)
        self.history = []

        # 恢复上次设置
        Clock.schedule_once(self.restore_settings, 0.2)

    def restore_settings(self, dt=0):
        theme_manager = ThemeManager()
        min_val = theme_manager.get_setting('last_min_value')
        max_val = theme_manager.get_setting('last_max_value')

        if min_val:
            self.min_input.text = min_val
        if max_val:
            self.max_input.text = max_val

    def generate_random(self, instance):
        try:
            min_val = int(self.min_input.text) if self.min_input.text else 0
            max_val = int(self.max_input.text) if self.max_input.text else 100

            if min_val > max_val:
                min_val, max_val = max_val, min_val

            count = int(self.count_input.text) if self.count_input.text else 1
            if count < 1:
                count = 1
            if count > 10:
                count = 10
                self.count_input.text = '10'

            results = []
            for i in range(count):
                result = random.randint(min_val, max_val)
                results.append(str(result))

            # 显示结果
            if count == 1:
                self.result_label.text = f'生成的随机数: {results[0]}'
            else:
                self.result_label.text = f'生成的随机数:\n' + ' | '.join(results)

            # 保存设置
            theme_manager = ThemeManager()
            theme_manager.set_setting('last_min_value', str(min_val))
            theme_manager.set_setting('last_max_value', str(max_val))

            # 添加到历史记录
            timestamp = datetime.now().strftime("%H:%M:%S")
            if count == 1:
                history_item = f'{timestamp} - 生成随机数: {results[0]} ({min_val}-{max_val})'
            else:
                history_item = f'{timestamp} - 生成多个随机数: [{", ".join(results)}] ({min_val}-{max_val})'
            self.history.append(history_item)
            if len(self.history) > 20:
                self.history = self.history[-20:]

        except ValueError:
            self.result_label.text = '请输入有效的数字！'

    def show_history(self, instance):
        content = BoxLayout(orientation='vertical', spacing=8, padding=[10, 10])
        history_title = ThemeLabel(
            text='生成历史记录',
            text_type='primary',
            font_size=22,
            size_hint=(1, 0.15),
            halign='center',
            bold=True
        )
        content.add_widget(history_title)

        scroll = ScrollView()
        grid = GridLayout(cols=1, size_hint_y=None, spacing=4)
        grid.bind(minimum_height=grid.setter('height'))

        for item in reversed(self.history):
            label = ThemeLabel(text=item, text_type='secondary', size_hint_y=None, height=32)
            grid.add_widget(label)

        if not self.history:
            label = ThemeLabel(text='暂无生成记录', text_type='secondary', size_hint_y=None, height=32)
            grid.add_widget(label)

        scroll.add_widget(grid)
        content.add_widget(scroll)

        close_btn = ThemeButton(text='关闭', button_type='accent', size_hint_y=0.15)
        content.add_widget(close_btn)

        popup = Popup(
            title='历史记录',
            content=content,
            size_hint=(0.9, 0.8),
            background=''
        )

        close_btn.bind(on_release=popup.dismiss)
        popup.open()


class TextRandomTab(FloatLayout):
    """文本随机选择器 - 全屏适配版"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.background_widget = BackgroundWidget()
        self.add_widget(self.background_widget)

        self.easter_egg_manager = EasterEggManager()

        scroll_view = ScrollView(size_hint=(1, 1))
        content = ContentBoxLayout(
            orientation='vertical',
            padding=[dp(32), dp(25), dp(32), dp(25)],
            spacing=dp(18),
            size_hint_y=None,
            size_hint_x=1
        )
        content.bind(minimum_height=content.setter('height'))
        scroll_view.add_widget(content)

        title = ThemeLabel(
            text='随机选择器',
            text_type='primary',
            font_size=sp(30),
            size_hint=(1, None),
            height=dp(58),
            bold=True,
            halign='center'
        )
        content.add_widget(title)

        desc = ThemeLabel(
            text='输入多个选项（每行一个），系统将随机选择其中一个：',
            text_type='secondary',
            font_size=sp(17),
            size_hint=(1, None),
            height=dp(46),
            halign='center'
        )
        content.add_widget(desc)

        # 文本输入框
        self.text_input = TextInput(
            hint_text='例如:\n选项一\n选项二\n选项三\n选项四\n选项五',
            font_size=sp(18),
            size_hint=(1, None),
            height=dp(200),
            multiline=True,
            background_color=(1, 1, 0.98, 0.96),
            foreground_color=(0.25, 0.2, 0.1, 1),
            hint_text_color=(0.5, 0.45, 0.35, 0.9),
            padding=[dp(15), dp(15)],
            cursor_color=(0.6, 0.45, 0.1, 1),
            halign='left'
        )
        content.add_widget(self.text_input)

        select_btn = ThemeButton(
            text='随机选择',
            button_type='primary',
            size_hint=(1, None),
            height=dp(52),
            font_size=sp(20)
        )
        select_btn.bind(on_press=self.select_random)
        content.add_widget(select_btn)

        self.result_label = ThemeLabel(
            text='等待随机选择...',
            text_type='highlight',
            font_size=sp(22),
            size_hint=(1, None),
            height=dp(110),
            halign='center',
            bold=True
        )
        self.result_label.bind(size=self.result_label.setter('text_size'))
        content.add_widget(self.result_label)

        clear_btn = ThemeButton(
            text='清空所有选项',
            button_type='error',
            size_hint=(1, None),
            height=dp(48),
            font_size=sp(18)
        )
        clear_btn.bind(on_press=self.clear_text)
        content.add_widget(clear_btn)

        hint_label = ThemeLabel(
            text='提示：连续快速点击5次"随机选择"按钮有惊喜',
            text_type='secondary',
            font_size=sp(14),
            size_hint=(1, None),
            height=dp(34),
            halign='center'
        )
        content.add_widget(hint_label)

        self.add_widget(scroll_view)

    def select_random(self, instance):
        lines = self.text_input.text.strip().split('\n')
        lines = [line.strip() for line in lines if line.strip()]

        if lines:
            result = random.choice(lines)
            self.result_label.text = f'随机选择的结果:\n{result}'

            # 记录点击，可能触发彩蛋
            self.easter_egg_manager.record_selection()
        else:
            self.result_label.text = '请输入至少一个选项！'

    def clear_text(self, instance):
        self.text_input.text = ''
        self.result_label.text = '等待随机选择...'


class ListRandomTab(FloatLayout):
    """列表随机功能 - 全屏适配版"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.background_widget = BackgroundWidget()
        self.add_widget(self.background_widget)

        scroll_view = ScrollView(size_hint=(1, 1))
        content = ContentBoxLayout(
            orientation='vertical',
            padding=[dp(32), dp(25), dp(32), dp(25)],
            spacing=dp(18),
            size_hint_y=None,
            size_hint_x=1
        )
        content.bind(minimum_height=content.setter('height'))
        scroll_view.add_widget(content)

        title = ThemeLabel(
            text='列表随机化',
            text_type='primary',
            font_size=sp(30),
            size_hint=(1, None),
            height=dp(58),
            bold=True,
            halign='center'
        )
        content.add_widget(title)

        desc = ThemeLabel(
            text='输入多个项目（每行一个），系统将随机打乱顺序：',
            text_type='secondary',
            font_size=sp(17),
            size_hint=(1, None),
            height=dp(46),
            halign='center'
        )
        content.add_widget(desc)

        self.text_input = TextInput(
            hint_text='例如:\n项目一\n项目二\n项目三\n项目四\n项目五',
            font_size=sp(18),
            size_hint=(1, None),
            height=dp(180),
            multiline=True,
            background_color=(1, 1, 0.98, 0.96),
            foreground_color=(0.25, 0.2, 0.1, 1),
            hint_text_color=(0.5, 0.45, 0.35, 0.9),
            padding=[dp(15), dp(15)],
            cursor_color=(0.6, 0.45, 0.1, 1),
            halign='left'
        )
        content.add_widget(self.text_input)

        randomize_btn = ThemeButton(
            text='随机打乱列表',
            button_type='primary',
            size_hint=(1, None),
            height=dp(52),
            font_size=sp(20)
        )
        randomize_btn.bind(on_press=self.randomize_list)
        content.add_widget(randomize_btn)

        self.result_label = ThemeLabel(
            text='随机化结果将显示在这里...',
            text_type='highlight',
            font_size=sp(20),
            size_hint=(1, None),
            height=180,
            halign='center',
            valign='top'
        )
        self.result_label.bind(size=self.result_label.setter('text_size'))
        content.add_widget(self.result_label)

        clear_btn = ThemeButton(
            text='清空列表',
            button_type='error',
            size_hint=(1, None),
            height=dp(48),
            font_size=sp(18)
        )
        clear_btn.bind(on_press=self.clear_text)
        content.add_widget(clear_btn)

        self.add_widget(scroll_view)

    def randomize_list(self, instance):
        lines = self.text_input.text.strip().split('\n')
        lines = [line.strip() for line in lines if line.strip()]

        if lines:
            shuffled = lines.copy()
            random.shuffle(shuffled)

            # 显示结果
            result_text = '随机化后的顺序:\n'
            for i, item in enumerate(shuffled, 1):
                result_text += f'{i}. {item}\n'

            self.result_label.text = result_text.strip()
        else:
            self.result_label.text = '请输入至少一个项目！'

    def clear_text(self, instance):
        self.text_input.text = ''
        self.result_label.text = '随机化结果将显示在这里...'


class SettingsTab(FloatLayout):
    """设置和关于页面 - 全屏适配版"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.background_widget = BackgroundWidget()
        self.add_widget(self.background_widget)

        scroll_view = ScrollView(size_hint=(1, 1))
        content = ContentBoxLayout(
            orientation='vertical',
            padding=[dp(32), dp(25), dp(32), dp(25)],
            spacing=dp(18),
            size_hint_y=None,
            size_hint_x=1
        )
        content.bind(minimum_height=content.setter('height'))
        scroll_view.add_widget(content)

        title = ThemeLabel(
            text='关于与设置',
            text_type='primary',
            font_size=sp(30),
            size_hint=(1, None),
            height=dp(58),
            bold=True,
            halign='center'
        )
        content.add_widget(title)

        quote_layout = BoxLayout(
            orientation='vertical',
            spacing=dp(12),
            size_hint=(1, None),
            height=dp(120)
        )
        theme_manager = ThemeManager()
        quote = theme_manager.get_random_quote()
        quote_text = ThemeLabel(
            text=f'"{quote}"',
            text_type='secondary',
            font_size=sp(17),
            size_hint=(1, 1),
            halign='center',
            valign='middle'
        )
        quote_text.bind(size=quote_text.setter('text_size'))
        quote_layout.add_widget(quote_text)
        content.add_widget(quote_layout)

        usage_layout = BoxLayout(
            orientation='vertical',
            spacing=dp(10),
            size_hint=(1, None),
            height=dp(420)
        )
        usage_title = ThemeLabel(
            text='功能说明',
            text_type='primary',
            font_size=sp(24),
            size_hint=(1, None),
            height=dp(44),
            halign='center',
            bold=True
        )
        usage_layout.add_widget(usage_title)
        usage_text = """随机数生成器:
• 设定任意范围的整数区间
• 支持一次生成多个随机数
• 自动保存生成历史记录

随机选择器:
• 输入多个候选项
• 系统随机选择其中一个
• 适合决策困难时使用

列表随机化:
• 输入项目列表
• 系统随机打乱顺序
• 适合抽签、排序等场景

数据管理:
• 自动保存最近设置
• 生成历史记录查看
• 简洁直观的操作界面
• 移动端优化设计"""
        usage_label = ThemeLabel(
            text=usage_text,
            text_type='secondary',
            font_size=sp(15),
            size_hint=(1, 1),
            halign='left',
            valign='top'
        )
        usage_label.bind(size=usage_label.setter('text_size'))
        usage_layout.add_widget(usage_label)
        content.add_widget(usage_layout)

        info_layout = BoxLayout(
            orientation='vertical',
            spacing=dp(8),
            size_hint=(1, None),
            height=dp(90)
        )
        version_label = ThemeLabel(
            text='版本: 1.1 (移动端优化版)',
            text_type='primary',
            font_size=sp(18),
            size_hint=(1, None),
            height=dp(36),
            halign='center',
            bold=True
        )
        info_layout.add_widget(version_label)
        date_label = ThemeLabel(
            text='© 2026 专业随机工具',
            text_type='secondary',
            font_size=sp(16),
            size_hint=(1, None),
            height=dp(36),
            halign='center'
        )
        info_layout.add_widget(date_label)
        content.add_widget(info_layout)
        self.add_widget(scroll_view)


# ============================================
# 主应用
# ============================================

class RandomToolApp(App):
    def build(self):
        self.title = '专业随机工具 v1.1'

        # Android 全屏适配：自动填满屏幕并按 DPI 缩放
        if IS_ANDROID:
            from kivy.core.window import Window
            Window.fullscreen = 'auto'

        theme_manager = ThemeManager()
        theme = theme_manager.get_current_theme()

        panel = TabbedPanel(
            do_default_tab=False,
            tab_pos='top_mid',
            tab_height=120,
            background_color=theme['colors']['tab_bg']
        )

        tabs = [
            ('随机数', RandomNumberTab()),
            ('选择器', TextRandomTab()),
            ('列表', ListRandomTab()),
            ('关于', SettingsTab())
        ]

        for tab_text, tab_content in tabs:
            tab = TabbedPanelItem(text=tab_text)
            tab.font_size = 32
            tab.size_hint_x = 0.25
            tab.size_hint_y = None
            tab.height = 120
            tab.color = theme['colors']['tab_text']
            tab.background_color = theme['colors']['tab_bg']
            tab.add_widget(tab_content)
            panel.add_widget(tab)

        return panel


if __name__ == '__main__':
    # 先注册中文字体，再启动应用
    setup_fonts()
    RandomToolApp().run()