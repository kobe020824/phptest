import tkinter as tk
import random

class LotteryApp:
    def __init__(self, master):
        self.master = master
        master.title("로또 번호 자동 생성기")
        master.geometry("400x400")
        
        self.label = tk.Label(master, text="이번주 로또 번호는 과연:")
        self.label.pack()
        
        self.result = tk.Label(master, font=("Arial", 20))
        self.result.pack(pady=20)
        
        self.button = tk.Button(master, text="Generate", command=self.generate)
        self.button.pack()
        
        self.quit_button = tk.Button(master, text="Quit", command=master.quit)
        self.quit_button.pack(pady=20)
        
    def generate(self):
        numbers = random.sample(range(1, 47), 6)
        self.result.config(text=str(numbers))
        
root = tk.Tk()
app = LotteryApp(root)
root.mainloop()
