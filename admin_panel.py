import tkinter as tk
from tkinter import simpledialog, messagebox
import sqlite3

def run_admin_panel():
    admin_window = tk.Tk()
    admin_window.title("Admin Panel")

    tk.Button(admin_window, text="View All Movies", command=view_all_movies).pack(pady=5)
    tk.Button(admin_window, text="Add Movie", command=add_movie).pack(pady=5)
    tk.Button(admin_window, text="Edit Movie", command=edit_movie).pack(pady=5)
    tk.Button(admin_window, text="Delete Movie", command=delete_movie).pack(pady=5)
    tk.Button(admin_window, text="Logout", command=admin_window.destroy).pack(pady=5)

    admin_window.mainloop()

def view_all_movies():
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()
    cursor.execute("SELECT movie_id, title, genre, release_year FROM Movie")
    movies = cursor.fetchall()
    conn.close()
    
    movie_list = "\n".join([f"ID: {m[0]}, Title: {m[1]}, Genre: {m[2]}, Year: {m[3]}" for m in movies])
    messagebox.showinfo("All Movies", movie_list or "No movies found.")

def add_movie():
    title = simpledialog.askstring("Add Movie", "Title:")
    genre = simpledialog.askstring("Add Movie", "Genre:")
    year = simpledialog.askstring("Add Movie", "Release Year:")
    director_id = simpledialog.askstring("Add Movie", "Director ID:")

    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Movie (title, genre, release_year, director_id) VALUES (?, ?, ?, ?)",
                   (title, genre, year, director_id))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Movie added.")

def edit_movie():
    movie_id = simpledialog.askstring("Edit Movie", "Movie ID to edit:")
    title = simpledialog.askstring("Edit Movie", "New Title:")
    genre = simpledialog.askstring("Edit Movie", "New Genre:")
    year = simpledialog.askstring("Edit Movie", "New Release Year:")
    director_id = simpledialog.askstring("Edit Movie", "New Director ID:")

    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE Movie SET title = ?, genre = ?, release_year = ?, director_id = ? WHERE movie_id = ?",
                   (title, genre, year, director_id, movie_id))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Movie updated.")

def delete_movie():
    movie_id = simpledialog.askstring("Delete Movie", "Movie ID to delete:")

    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Movie WHERE movie_id = ?", (movie_id,))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Movie deleted.")
