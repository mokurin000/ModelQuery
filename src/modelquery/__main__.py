import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttkb
import polars as pl
import random

# 读取数据
data = pl.read_excel("data.xlsx")
model_to_config = dict(zip(map(lambda s: s.lower(), data["型号"]), data["推荐配置"]))

# 初始化主窗口
app = ttkb.Window(themename="superhero")
app.title("配置推荐软件")

# 设置字体
font_style = ("Microsoft Yahei", 20)

# 创建框架来组织布局
frame = ttk.Frame(app, padding="10")

# 标签和输入框
title_model = ttk.Entry(frame, font=font_style)
title_model.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

# 标签和输入框
label_model = ttk.Label(frame, text="手机型号：", font=font_style)
label_model.grid(row=1, column=0, padx=10, pady=10, sticky="e")

entry_model = ttk.Entry(frame, font=font_style)
entry_model.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

label_config = ttk.Label(frame, text="推荐配置：", font=font_style)
label_config.grid(row=2, column=0, padx=10, pady=10, sticky="e")

# 使用不可编辑的 Entry 以保持一致的高度
text_config = ttk.Entry(frame, font=font_style, state="readonly")
text_config.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

# 使entry和text宽度一致
frame.grid_columnconfigure(1, weight=1)

# 将框架添加到主窗口并居中对齐
frame.pack(expand=True, fill="both")


# 查询函数
def search_config(event):
    model = entry_model.get().lower()
    config = model_to_config.get(model)

    if not config:
        config = random.choice(["换铁盆", "砸核桃"])

    text_config.configure(state="normal")
    text_config.delete(0, tk.END)
    text_config.insert(0, config)
    text_config.configure(state="readonly")


# 绑定回车事件
entry_model.bind("<Return>", search_config)

# 运行主循环
app.mainloop()
