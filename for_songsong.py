# -*- coding: utf-8 -*-
"""
Created on Fri May 17 19:20:36 2024

@author: Lenovo
"""
#      ******       ******      
#    **      **   **      **    
#  **          ** **          **
# **             **             **
# **                            **
# **                            **
#  **                          **
#   **                        **
#    **                      **
#      **                  **
#        **              **
#          **          **
#            **      **
#              **  **
#                **
#                
#                **
#              **  **
#            **      **
#          **          **
#        **              **
#      **                  **
#    **                      **
#   **                        **
#  **                          **
# **                            **
# **                            **
# **             **             **
#  **          ** **          **
#    **      **   **      **    
#      ******       ******      
#      ******       ******      
#    **      **   **      **    
#  **          ** **          **
# **             **             **
# **                            **
# **                            **
#  **                          **
#   **                        **
#    **                      **
#      **                  **
#        **              **
#          **          **
#            **      **
#              **  **
#                **
#                
#                **
#              **  **
#            **      **
#          **          **
#        **              **
#      **                  **
#    **                      **
#   **                        **
#  **                          **
# **                            **
# **                            **
# **             **             **
#  **          ** **          **
#    **      **   **      **    
#      ******       ******      
#      ******       ******      
#    **      **   **      **    
#  **          ** **          **
# **             **             **
# **                            **
# **                            **
#  **                          **
#   **                        **
#    **                      **
#      **                  **
#        **              **
#          **          **
#            **      **
#              **  **
#                **
#                
#                **
#              **  **
#            **      **
#          **          **
#        **              **
#      **                  **
#    **                      **
#   **                        **
#  **                          **
# **                            **
# **                            **
# **             **             **
#  **          ** **          **
#    **      **   **      **    
#      ******       ******      

import random
import tkinter as tk
from ttkbootstrap import Style


items = ['songsong对待小动物很友好',
         'songsong的怀抱很温暖',
         'songsong英语说得很好',
         'songsong还会日语和希伯来语，好厉害',
         'songsong有钢铁般的肌肉',
         'songsong的大眼睛可爱极了',
         'songsong撒娇的时候让人想要搂住',
         'songsong吃饭吃得香还几乎不剩饭',
         'songsong穿五颜六色的可爱衣服',
         'songsong闻起来香香的',
         '和songsong谈完心我总能感到安慰',
         '和songsong待在一起我总能感到平静',
         'songsong很擅长亲亲让人亲不够',
         'songsong总能控制好脾气',
         'songsong做事很有耐心',
         'songsong is so well-organized',
         'songsong是暖暖的人肉床垫',
         'songsong喜欢鸭鸭',
         'songsong会读心术',
         'songsong会走私',
         'songsong唱皮卡丘之歌唱得好听',
         'songsong is a decent human being',
         'songsong的手臂看上去很好吃',
         'songsong是一位好老师',
         '觉得songsong如果当导师会是好老师',
         '喜欢和songsong一起看书学习',
         '喜欢和songsong一起聊天',
         '喜欢和songsong一起讨论哲学',
         '喜欢和songsong一起读书并分享读后感',
         'songsong的butt is so mine',
         '喜欢摸摸songsong的肚皮',
         'songsong是会跳水的美人鱼',
         '看到songsong我就猫瘾犯了',
         '和songsong一起刷题很开心',
         '喜欢和songsong一起出去玩',
         '喜欢和songsong一起健身变壮',
         '喜欢和songsong一起吃饭',
         '感觉什么事都可以和songsong说',
         '喜欢和songsong一起傻笑']

def lottery():
    winners = random.sample(items, 1)
    result_label.config(text="因为\n" + "\n".join(winners)) 

def create_heart(canvas, x, y, size, color):
    points = [
        x, y,
        x - size, y - size,
        x - size*2, y,
        x, y + size*2,
        x + size*2, y,
        x + size, y - size
    ]
    return canvas.create_polygon(points, fill=color, outline='')

def animate_hearts():
    for heart in hearts:
        canvas.move(heart, 0, 5)
        pos = canvas.coords(heart)
        if pos[1] > canvas.winfo_height():
            canvas.coords(heart, pos[0], 0, pos[2], -size, pos[4], 0, pos[6], size*2, pos[8], 0, pos[10], -size)

    root.after(50, animate_hearts)

style = Style(theme='united')
root = tk.Tk()
root.title("Refreshment")

result_label = tk.Label(root, text="为什么喜欢songsong？", font=("Arial", 15), justify=tk.LEFT)
result_label.pack(pady=10)

lottery_button = tk.Button(root, text="Click Me", font=("Arial", 15), command=lottery)
lottery_button.pack()

canvas = tk.Canvas(root, width=400, height=400, bg='white')
canvas.pack()

hearts = []
num_hearts = 20
size = 10
for _ in range(num_hearts):
    x = random.randint(0, 400)
    y = random.randint(-400, 0)
    heart = create_heart(canvas, x, y, size, 'orange')
    hearts.append(heart)


animate_hearts()
root.mainloop()
