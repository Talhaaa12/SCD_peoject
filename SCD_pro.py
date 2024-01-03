import tkinter as tk
import random
import time
import requests

class TypingSpeedTest:
    def __init__(self, master):
        self.master = master
        self.master.title("Typing Speed Test")
        self.master.geometry("800x500")
        self.master.configure(bg="aqua")

        self.paragraphs = [
            "Python is a versatile programming language...",
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit...",
            "The quick brown fox jumps over the lazy dog...",
            "Programming is the art of telling a computer what to do..."
        ]
        self.current_paragraph = ""
        self.start_time = 0

        self.label_heading = tk.Label(master, text="Welcome to Typing Speed Test", font=("Helvetica", 20), bg="aqua")
        self.label_heading.pack(pady=10)

        self.label_instruction = tk.Label(master, text="Type the paragraph below:", font=("Helvetica", 14), bg="aqua")
        self.label_instruction.pack(pady=10)

        self.label_paragraph = tk.Label(master, text=self.get_new_paragraph(), wraplength=700, justify=tk.LEFT, font=("Helvetica", 12), bg="aqua")
        self.label_paragraph.pack(pady=10)

        self.entry = tk.Entry(master, bg="white", font=("Helvetica", 14))
        self.entry.pack(pady=10, ipady=5)  # Increase the internal padding (ipady) for a larger field

        # Move check_paragraph method definition above this line
        self.entry.bind("<Return>", self.check_paragraph)

        self.label_result = tk.Label(master, text="", font=("Helvetica", 14), bg="aqua")
        self.label_result.pack(pady=10)

        self.label_statistics = tk.Label(master, text="", font=("Helvetica", 14), bg="aqua")
        self.label_statistics.pack(pady=10)

        self.button_restart = tk.Button(master, text="Restart", command=self.restart_test, font=("Helvetica", 14))
        self.button_restart.pack(pady=10)

        self.correct_words = 0
        self.total_words = 0
        self.total_time = 0

    def get_new_paragraph(self):
        self.current_paragraph = random.choice(self.paragraphs)
        return self.current_paragraph

    # Move this method definition above the entry.bind line
    def check_paragraph(self, event):
        user_input = self.entry.get().strip()
        self.total_words += len(self.current_paragraph.split())

        if user_input == self.current_paragraph:
            self.correct_words += len(self.current_paragraph.split())
            elapsed_time = time.time() - self.start_time
            self.total_time += elapsed_time
            accuracy_percentage = int((self.correct_words / self.total_words) * 100)

            # Move the result label update here
            self.label_result.config(text=f"Correct! Accuracy: {accuracy_percentage}%")

            # Display additional statistics
            total_correct_words = self.correct_words
            total_time_taken = round(self.total_time, 2)

            # Handle division by zero
            if total_time_taken != 0:
                words_per_minute = int(total_correct_words / (total_time_taken / 60))
            else:
                words_per_minute = 0

            self.label_statistics.config(text=f"Total Correct Words: {total_correct_words}, Words Per Minute: {words_per_minute}")
        else:
            accuracy_percentage = int((self.correct_words / self.total_words) * 100)
            self.label_result.config(text=f"Incorrect! Accuracy: {accuracy_percentage}%")

        # Move these operations here
        self.entry.delete(0, tk.END)
        self.label_paragraph.config(text=self.get_new_paragraph())
        self.start_time = time.time()

    def submit_result(self, correct_words, incorrect_words, time_taken):
        api_url = 'http://localhost:5000/submit_result' 
        data = {
            'correct_words': correct_words,
            'incorrect_words': incorrect_words,
            'time_taken': time_taken
        }

        try:
            response = requests.post(api_url, json=data)
            if response.status_code == 200:
                print('Result submitted successfully')
            else:
                print(f'Error: {response.status_code}')
        except Exception as e:
            print(f'Error: {e}')

    def restart_test(self):
        self.label_result.config(text="")
        self.label_paragraph.config(text=self.get_new_paragraph())
        self.start_time = time.time()
        self.entry.delete(0, tk.END)
        self.correct_words = 0
        self.total_words = 0
        self.total_time = 0
        self.label_statistics.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTest(root)

    # Move check_paragraph method definition above this line
    app.check_paragraph = app.check_paragraph  # Redefine the method here
    app.entry.bind("<Return>", app.check_paragraph)

    root.mainloop()
