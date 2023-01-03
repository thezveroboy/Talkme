# talkme is a first attempt to talk with stable diffusion

from ldm.modules.encoders.modules import FrozenCLIPEmbedder, FrozenOpenCLIPEmbedder
from modules import script_callbacks, shared
import open_clip.tokenizer

import gradio as gr

css = """
.tokenizer-token{
    cursor: pointer;
}
.tokenizer-token-0 {background: rgba(255, 0, 0, 0.05);}
.tokenizer-token-0:hover {background: rgba(255, 0, 0, 0.15);}
.tokenizer-token-1 {background: rgba(0, 255, 0, 0.05);}
.tokenizer-token-1:hover {background: rgba(0, 255, 0, 0.15);}
.tokenizer-token-2 {background: rgba(0, 0, 255, 0.05);}
.tokenizer-token-2:hover {background: rgba(0, 0, 255, 0.15);}
.tokenizer-token-3 {background: rgba(255, 156, 0, 0.05);}
.tokenizer-token-3:hover {background: rgba(255, 156, 0, 0.15);}
"""


def add_tab():
    with gr.Blocks(analytics_enabled=False, css=css) as ui:
        gr.HTML(f"""
<style>{css}</style>
<p>
Just say something
</p>
""")

#########################################


#########################################

    return [(ui, "Talkme", "talkme")]


script_callbacks.on_ui_tabs(add_tab)
