import tkinter as tk
from tkinter import filedialog
import time

class TypingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Practice Game")
        self.root.geometry("800x400")
        self.text_data = ""
        self.current_index = 0
        self.typing_started = False
        self.start_time = None
        self.char_count = 0
        self.word_count = 0

        # 顯示文字框
        self.text_display = tk.Text(self.root, font=("Consolas", 16), wrap="word", state="disabled", bg="white")
        self.text_display.pack(fill="both", expand=True)

        # 統計顯示
        self.stats_label = tk.Label(self.root, text="CPS: 0.00 | WPS: 0.00", font=("Arial", 12))
        self.stats_label.place(x=10, y=10)

        # 綁定事件
        self.root.bind("<Key>", self.on_key_press)
        self.root.bind("<Return>", self.toggle_start)
        self.root.bind("<FocusIn>", self.resume_typing)
        self.root.bind("<FocusOut>", self.pause_typing)

        self.load_text()

    def load_text(self):
        filepath = filedialog.askopenfilename(title="選擇要練習的文章", filetypes=[("Text Files", "*.txt")])
        if not filepath:
            self.root.destroy()
            return
        with open(filepath, "r", encoding="utf-8") as file:
            self.text_data = file.read().strip()
        self.update_display()

    def update_display(self):
        self.text_display.config(state="normal")
        self.text_display.delete("1.0", "end")

        for i, char in enumerate(self.text_data):
            tag = ""
            if i < self.current_index:
                tag = "correct"  # 預設都當作正確輸入（後續會補紅色錯誤處理）
            elif i == self.current_index:
                tag = "current"
            self.text_display.insert("end", char, tag)

        # 標記樣式定義
        self.text_display.tag_config("correct", foreground="green")
        self.text_display.tag_config("wrong", foreground="red")
        self.text_display.tag_config("current", background="yellow")

        self.text_display.config(state="disabled")

    def on_key_press(self, event):
        if not self.typing_started or event.keysym == "Return":
            return

        expected_char = self.text_data[self.current_index]
        typed_char = event.char

        if typed_char == expected_char:
            tag = "correct"
            self.char_count += 1
            if typed_char == " ":
                self.word_count += 1
        else:
            tag = "wrong"

        self.current_index += 1
        if self.current_index >= len(self.text_data):
            self.typing_started = False

        self.update_display()
        self.update_stats()

    def toggle_start(self, event=None):
        if not self.typing_started:
            self.typing_started = True
            self.start_time = time.time()
            self.char_count = 0
            self.word_count = 0
        else:
            self.typing_started = False

    def update_stats(self):
        if not self.typing_started:
            return
        elapsed = max(time.time() - self.start_time, 0.01)
        cps = self.char_count / elapsed
        wps = self.word_count / elapsed
        self.stats_label.config(text=f"CPS: {cps:.2f} | WPS: {wps:.2f}")

    def pause_typing(self, event=None):
        self.typing_started = False

    def resume_typing(self, event=None):
        self.typing_started = False
        self.current_index = 0
        self.char_count = 0
        self.word_count = 0
        self.start_time = None
        self.update_display()
        self.stats_label.config(text="CPS: 0.00 | WPS: 0.00")


if __name__ == "__main__":
    root = tk.Tk()
    app = TypingGame(root)
    root.mainloop()
