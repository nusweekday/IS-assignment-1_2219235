import tkinter as tk
from tkinter import messagebox
import random

class HomeScreen:
    def __init__(self, master):
        self.master = master
        self.master.title("Faith Quest: Journey through the Pillars of Islam")
        self.master.geometry("1000x500")
        self.master.configure(bg="#B0C5A4")

        self.title_label = tk.Label(self.master, text="Faith Quest: Journey through the Pillars of Islam", font=("Comfortaa", 16), bg="#B0C5A4")
        self.title_label.pack(pady=20)
        self.title_label = tk.Label(self.master, text="How to Play : Guess the pillars of Islam related to each question. You have 3 attempts per question. Use the hint if needed.", font=("Comfortaa", 10), bg="#B0C5A4")
        self.title_label.pack(pady=20, anchor="center")

        self.play_button = tk.Button(self.master, text="Play", command=self.play_game, width=20, pady=10, bg="white", borderwidth=2, relief=tk.RAISED, font=("Comfortaa", 10))
        self.play_button.pack(pady=10, padx=10)


    def play_game(self):
        self.master.withdraw()
        play_screen = tk.Toplevel(self.master)
        play_screen.configure(bg="#B0C5A4")
        PlayScreen(play_screen)


    def quit_game(self):
        self.master.quit()

class PlayScreen:
    def __init__(self, master):
        self.master = master
        self.master.title("Faith Quest: Journey through the Pillars of Islam")
        self.master.geometry("700x500")
        self.master.configure(bg="#B0C5A4")

        self.questions = [
            "What is the first pillar of Islam?",
            "What religious practice do Muslims engage in five times a day?",
            "What do Muslims do during the month of Ramadan?",
            "What is the obligatory charity called in Islam?",
            "What is the last pillar of Islam?"
        ]

        random.shuffle(self.questions)

        self.answer_dict = {
            "What is the first pillar of Islam?": "Syahadah",
            "What religious practice do Muslims engage in five times a day?": "Pray",
            "What do Muslims do during the month of Ramadan?": "Fasting",
            "What is the obligatory charity called in Islam?": "Zakat",
            "What is the last pillar of Islam?": "Hajj"
        }

        self.hint_dict = {
            "What is the first pillar of Islam?": "The declaration of faith in Islam.",
            "What religious practice do Muslims engage in five times a day?": "Involves facing towards the Kaaba during its performance.",
            "What do Muslims do during the month of Ramadan?": "They refrain from eating and drinking from dawn until sunset.",
            "What is the obligatory charity called in Islam?": "It is a form of almsgiving.",
            "What is the last pillar of Islam?": "The pilgrimage to Mecca."
        }

        self.current_question_index = -1
        self.next_question()

    def next_question(self):
        self.current_question_index += 1
        if self.current_question_index < len(self.questions):
            self.current_question = self.questions[self.current_question_index]
            self.word_to_guess = self.answer_dict[self.current_question]
            self.hint = self.hint_dict[self.current_question]
            self.guess = ['_'] * len(self.word_to_guess)
            self.attempts_left = 3

            self.word_label = tk.Label(self.master, text=' '.join(self.guess), bg="#B0C5A4", font=("Comfortaa", 12))
            self.word_label.pack()

            self.question_label = tk.Label(self.master, text="Question: " + self.current_question, bg="#B0C5A4", font=("Comfortaa", 12))
            self.question_label.pack()

            self.attempts_label = tk.Label(self.master, text=f"Attempts Left: {self.attempts_left}", bg="#B0C5A4", font=("Comfortaa", 12))
            self.attempts_label.pack()

            self.entry = tk.Entry(self.master)
            self.entry.pack()

            self.guess_button = tk.Button(self.master, text='Guess', command=self.submit_guess, width=20, pady=10, bg="white", borderwidth=2, relief=tk.RAISED, font=("Comfortaa", 10))
            self.guess_button.pack(pady=10, padx=10)

            self.hint_button = tk.Button(self.master, text='Take Hint', command=self.show_hint, width=20, pady=10, bg="white", borderwidth=2, relief=tk.RAISED, font=("Comfortaa", 10))
            self.hint_button.pack(pady=10, padx=10)

            self.return_button = tk.Button(self.master, text='Return to Home Screen', command=self.return_to_home, width=20, pady=10, bg="white", borderwidth=2, relief=tk.RAISED, font=("Comfortaa", 10))
            self.return_button.pack(pady=10, padx=10)

            self.quit_button = tk.Button(self.master, text='Quit the Game', command=self.quit_game, width=20, pady=10, bg="white", borderwidth=2, relief=tk.RAISED, font=("Comfortaa", 10))
            self.quit_button.pack(pady=10, padx=10)
        else:
            messagebox.showinfo("Congratulations", "You have completed all questions! Masyallah brother you are a true Muslim!")
            self.master.quit()

    def submit_guess(self):
        guess = self.entry.get().lower()
        if guess == self.word_to_guess.lower():
            messagebox.showinfo("Correct", f"Alhamdulillah! Your guess '{guess}' is correct!")
            self.word_label.destroy()
            self.question_label.destroy()
            self.attempts_label.destroy()
            self.entry.destroy()
            self.guess_button.destroy()
            self.hint_button.destroy()
            self.return_button.destroy()
            self.quit_button.destroy()
            self.next_question()
        else:
            self.attempts_left -= 1
            if self.attempts_left == 0:
                messagebox.showinfo("Out of Attempts. Redirecting to Home Screen...", "Astaghfirullah brother, how can you not know the answer!")
                self.return_to_home()
            else:
                messagebox.showinfo("Incorrect", f"Nuh uh wrong answer! Attempts left: {self.attempts_left}")
                self.attempts_label.config(text=f"Attempts Left: {self.attempts_left}")
                self.entry.delete(0, tk.END)

    def show_hint(self):
        messagebox.showinfo("Hint", self.hint)

    def return_to_home(self):
        self.master.destroy()
        root.deiconify()

    def quit_game(self):
        root.quit()

def main():
    global root
    root = tk.Tk()
    home_screen = HomeScreen(root)
    root.mainloop()

if __name__ == "__main__":
    main()
