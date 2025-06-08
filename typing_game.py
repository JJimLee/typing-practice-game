import tkinter as tk
import os
import time

class TypingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Practice Game")
        self.root.geometry("800x400")

        self.text_data = "This is a typing test. Please type this line correctly."  # <-- DEBUG HARDCODED
        self.current_index = 0
        self.typing_started = False
        self.start_time = None
        self.char_count = 0
        self.word_count = 0
        self.wrong_indices = set()

        self.info_label = tk.Label(root, text="", anchor="w", font=("Arial", 10))
        self.info_label.pack(fill="x")

        self.separator = tk.Label(root, text="─" * 200, font=("Courier", 8))
        self.separator.pack(fill="x")

        self.text_display = tk.Text(
            root, font=("Consolas", 16), wrap="word",
            state="disabled", bg="white", fg="black", insertbackground="black"
        )
        self.text_display.pack(fill="both", expand=True)

        root.bind("<Key>", self.on_key_press)
        root.bind("<Return>", self.toggle_start)
        root.bind("<FocusIn>", self.resume_typing)
        root.bind("<FocusOut>", self.pause_typing)

        self.update_info()
        self.update_display()

    def update_info(self, wpm=0.0, cpm=0.0, accuracy=100.0):
        total_chars = len(self.text_data)
        total_words = len(self.text_data.split())
        self.info_label.config(
            text=f"Words: {total_words}  Chars: {total_chars}    WPM: {wpm:.2f}  CPM: {cpm:.2f}  Accuracy: {accuracy:.2f}%"
        )

    def update_display(self):
        self.text_display.config(state="normal")
        self.text_display.delete("1.0", "end")

        for i, char in enumerate(self.text_data):
            tag = ""
            if i in self.wrong_indices:
                tag = "wrong"
            elif i < self.current_index:
                tag = "correct"
            elif i == self.current_index:
                tag = "current"
            self.text_display.insert("end", char, tag)

        self.text_display.tag_config("correct", foreground="green")
        self.text_display.tag_config("wrong", foreground="red")
        self.text_display.tag_config("current", background="yellow", foreground="black")
        self.text_display.config(state="disabled")

    def on_key_press(self, event):
        if not self.typing_started or event.keysym == "Return":
            return
        if self.current_index >= len(self.text_data):
            return

        expected_char = self.text_data[self.current_index]
        typed_char = event.char

        if typed_char == expected_char:
            self.char_count += 1
            if typed_char == " ":
                self.word_count += 1
        else:
            self.wrong_indices.add(self.current_index)

        self.current_index += 1
        self.update_display()
        self.update_stats()

    def toggle_start(self, event=None):
        if not self.typing_started:
            self.typing_started = True
            self.start_time = time.time()
            self.char_count = 0
            self.word_count = 0
            self.wrong_indices.clear()
        else:
            self.typing_started = False

    def update_stats(self):
        if not self.typing_started:
            return
        elapsed = max(time.time() - self.start_time, 1)
        cpm = self.char_count / elapsed * 60
        wpm = self.word_count / elapsed * 60
        total_typed = self.char_count + len(self.wrong_indices)
        accuracy = (self.char_count / total_typed) * 100 if total_typed else 100.0
        self.update_info(wpm, cpm, accuracy)

    def pause_typing(self, event=None):
        self.typing_started = False

    def resume_typing(self, event=None):
        self.typing_started = False
        self.current_index = 0
        self.char_count = 0
        self.word_count = 0
        self.wrong_indices.clear()
        self.start_time = None
        self.update_display()
        self.update_info()

if __name__ == "__main__":
    os.environ["TK_STYLE"] = "light"
    root = tk.Tk()
    app = TypingGame(root)
    root.mainloop()
