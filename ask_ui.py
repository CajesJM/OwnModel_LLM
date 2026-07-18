import gradio as gr
from ask import answer_question

custom_css = """
@import url('https://fonts.googleapis.com/css2?family=Segoe+UI&display=swap');

.gradio-container {
    max-width: 800px !important;
    margin: auto !important;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.header {
    text-align: center;
    padding: 20px;
    background: linear-gradient(135deg, #a1c4fd, #c2e9fb);
    color: #1e3c72;
    border-radius: 15px 15px 0 0;
}
.header h1 { margin: 0; font-size: 2.2em; }
.header p { margin: 5px 0 0 0; font-size: 1.1em; opacity: 0.9; }

.chat-container {
    background: #f9f9f9;
    padding: 20px;
    border-left: 1px solid #ddd;
    border-right: 1px solid #ddd;
}

.footer {
    text-align: center;
    padding: 10px;
    background: #e0e0e0;
    border-radius: 0 0 15px 15px;
    color: #555;
    font-size: 0.9em;
}

.input-row { display: flex; gap: 10px; align-items: center; margin-top: 10px; }
.input-row .textbox { flex: 1; }
.send-btn {
    background: #2a5298;
    color: white;
    border: none;
    border-radius: 8px;
    padding: 10px 20px;
    font-weight: bold;
    cursor: pointer;
}
.send-btn:hover { background: #1e3c72; }

.output-box textarea {
    font-size: 1em;
    line-height: 1.5;
    border-radius: 10px;
    background: white;
    border: 1px solid #ccc;
}
"""

with gr.Blocks(css=custom_css, title="Cypher Tech") as demo:
    gr.HTML("""
        <div class="header">
            <h1>Cypher Tech</h1>
            <p>Your AI guide to Trinidad Municipal College</p>
        </div>
    """)

    with gr.Column(elem_classes="chat-container"):
        output = gr.Textbox(
            label="Cypher's answer",
            interactive=False,
            lines=5,
            elem_classes="output-box"
        )
        with gr.Row(elem_classes="input-row"):
            input_text = gr.Textbox(
                label="Your question",
                placeholder="e.g. What is the mission of TMC?",
                scale=4,
                elem_classes="textbox"
            )
            send_btn = gr.Button("Send", variant="primary", elem_classes="send-btn")

    gr.HTML("""
        <div class="footer">
            Powered by <strong>CajesJM</strong> - Custom from-scratch mini-LLM - Runs 100% offline
        </div>
    """)

    send_btn.click(fn=answer_question, inputs=input_text, outputs=output)
    input_text.submit(fn=answer_question, inputs=input_text, outputs=output)

if __name__ == "__main__":
    demo.launch(server_name="127.0.0.1", server_port=7860, share=False)