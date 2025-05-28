# 普通的一个交互式UI，问候他人
# import gradio as gr
#
# def greet(name,intensity):
#     return "Hello" + name + "!" * int(intensity)/ 
#
# demo = gr.Interface(
#     fn=greet,
#     inputs=["text", "slider"],
#     outputs=["text"],
# )
#
# demo.launch(share = True)

"""我们看到 Interface 类使用三个必需参数进行初始化：
fn：用于包装用户界面（UI）的函数
inputs：用于输入的 Gradio 组件。组件数量应与函数参数数量相匹配。
outputs：用于输出的 Gradio 组件。组件数量应与函数返回值数量相匹配。"""

# 假设你想将滑块自定义为范围从1到10，默认值为2。
# 你还想自定义输出文本框——你希望它更大，并带有标签。
import gradio as gr
from numpy.ma.core import minimum, maximum

from Lib.email.policy import default


def greet(name, intensity):
    return "Hello " + name + "!" * int(intensity)

demo = gr.Interface(
    fn=greet,
    inputs=["text",gr.Slider(minimum=1,maximum=10,value=2,step=1)],
    outputs=[gr.Textbox(label='greeting',lines=3)]
)

demo.launch()
