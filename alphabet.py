import os
import tkinter as tk
from pygame import mixer

# 初始化 pygame 的音频模块
mixer.init()

# 藏文字母与其对应音频文件名的映射
tibetan_letters = {
    "ཀ": "ka.mp3", "ཁ": "kha.mp3", "ག": "ga.mp3", "ང": "nga.mp3",
    "ཅ": "ca.mp3", "ཆ": "cha.mp3", "ཇ": "ja.mp3", "ཉ": "nya.mp3",
    "ཏ": "ta.mp3", "ཐ": "tha.mp3", "ད": "da.mp3", "ན": "na.mp3",
    "པ": "pa.mp3", "ཕ": "pha.mp3", "བ": "ba.mp3", "མ": "ma.mp3",
    "ཙ": "tsa.mp3", "ཚ": "tsha.mp3", "ཛ": "dza.mp3", "ཝ": "wa.mp3",
    "ཞ": "zha.mp3", "ཟ": "za.mp3", "འ": "a.mp3", "ཡ": "ya.mp3",
    "ར": "ra.mp3", "ལ": "la.mp3", "ཤ": "sha.mp3", "ས": "sa.mp3",
    "ཧ": "ha.mp3", "ཨ": "a1.mp3"
}


# 定义播放音频的函数
def play_audio(letter):
    audio_file = os.path.join('audio', tibetan_letters[letter])
    if os.path.exists(audio_file):
        mixer.music.load(audio_file)
        mixer.music.play()
    else:
        print(f"音频文件 {audio_file} 不存在")


# 创建 Tkinter 窗口
root = tk.Tk()
root.title("藏文字母发音")

# 使用 Grid 布局排列按钮
row = 0
col = 0
for index, letter in enumerate(tibetan_letters):
    button = tk.Button(root, text=letter, font=("Arial", 20), width=5, command=lambda l=letter: play_audio(l))
    button.grid(row=row, column=col, padx=10, pady=10)

    col += 1
    if (index + 1) % 4 == 0:  # 每行放置6个按钮
        row += 1
        col = 0

# 启动 Tkinter 主循环
root.mainloop()
