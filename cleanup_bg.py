#!/usr/bin/env python3
"""Remove all background/gradient code from main.py"""
import re

p = r'C:\temp_app\main.py'
with open(p, 'r', encoding='utf-8') as f:
    c = f.read()

# Remove BackgroundWidget class entirely
c = re.sub(
    r'class BackgroundWidget\(FloatLayout\):.*?(?=class ContentBoxLayout)',
    '',
    c,
    flags=re.DOTALL
)

# Remove _get_bg_path method
c = re.sub(
    r'    def _get_bg_path.*?return None\n\n',
    '',
    c,
    flags=re.DOTALL
)

# Remove _check_backgrounds
c = c.replace('        self._check_backgrounds()\n', '')
c = re.sub(
    r'    def _check_backgrounds.*?pass\n\n',
    '',
    c,
    flags=re.DOTALL
)

# Remove bg_image: line
c = re.sub(
    r"\s+'bg_image': self\._get_bg_path\('我的背景\d'\),\n",
    '',
    c
)

# Remove bg_image line from theme
c = c.replace("'bg_image': self._get_bg_path('我的背景1'),\n", '')
c = c.replace("'bg_image': None,\n", '')

# Add bg_image: None fallback
c = c.replace(
    "def get_current_theme(self):\n        return self.themes[self.current_theme]",
    "def get_current_theme(self):\n        theme = dict(self.themes[self.current_theme])\n        return theme"
)

# Remove BackgroundWidget from all tabs
# RandomNumberTab
c = c.replace(
    '        self.background_widget = BackgroundWidget()\n        self.add_widget(self.background_widget)\n\n        scroll_view',
    '        scroll_view'
)
# TextRandomTab
c = c.replace(
    '        self.background_widget = BackgroundWidget()\n        self.add_widget(self.background_widget)\n\n        self.easter_egg_manager',
    '        self.easter_egg_manager'
)
# ListRandomTab
c = c.replace(
    '        self.background_widget = BackgroundWidget()\n        self.add_widget(self.background_widget)\n\n        scroll_view',
    '        scroll_view'
)
# SettingsTab
c = c.replace(
    '        self.background_widget = BackgroundWidget()\n        self.add_widget(self.background_widget)\n\n        scroll_view',
    '        scroll_view'
)

with open(p, 'w', encoding='utf-8') as f:
    f.write(c)
print('Cleanup done')
