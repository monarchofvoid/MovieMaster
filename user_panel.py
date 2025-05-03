import tkinter as tk
from tkinter import simpledialog, messagebox
import sqlite3

def run_user_panel():
    user_window = tk.Tk()
    user_window.title("User Panel")

    tk.Button(user_window, text="View All Movies", command=view_all_movies).pack(pady=5)
    tk.Button(user_window, text="Search Movies", command=search_movies).pack(pady=5)
    tk.Button(user_window, text="Logout", command=user_window.destroy).pack(pady=5)

    user_window.mainloop()

def view_all_movies():
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()
    cursor.execute("SELECT movie_id, title, genre, release_year FROM Movie")
    movies = cursor.fetchall()
    conn.close()

    movie_list = "\n".join([f"ID: {m[0]}, Title: {m[1]}, Genre: {m[2]}, Year: {m[3]}" for m in movies])
    messagebox.showinfo("All Movies", movie_list or "No movies found.")

def search_movies():
    search_window = tk.Toplevel()
    search_window.title("Search Movies")

    def search_by(criteria):
        value = simpledialog.askstring("Search", f"Enter {criteria}:")
        conn = sqlite3.connect('movies.db')
        cursor = conn.cursor()

        if criteria == 'Genre':
            cursor.execute("SELECT movie_id, title FROM Movie WHERE genre LIKE ?", (f"%{value}%",))
        elif criteria == 'Director':
            cursor.execute("SELECT m.movie_id, m.title FROM Movie m JOIN Director d ON m.director_id = d.director_id WHERE d.name LIKE ?", (f"%{value}%",))
        elif criteria == 'Actor':
            cursor.execute("SELECT m.movie_id, m.title FROM Movie m JOIN Movie_Actor ma ON m.movie_id = ma.movie_id JOIN Actor a ON ma.actor_id = a.actor_id WHERE a.name LIKE ?", (f"%{value}%",))

        results = cursor.fetchall()
        conn.close()

        result_text = "\n".join([f"ID: {r[0]}, Title: {r[1]}" for r in results])
        messagebox.showinfo("Search Results", result_text or "No matching movies found.")

    tk.Button(search_window, text="By Genre", command=lambda: search_by('Genre')).pack(pady=5)
    tk.Button(search_window, text="By Director", command=lambda: search_by('Director')).pack(pady=5)
    tk.Button(search_window, text="By Actor", command=lambda: search_by('Actor')).pack(pady=5)
