import sqlite3
def setup_database():
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()

    # Create Director table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Director (
            director_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            birth_year INTEGER
        )
    ''')

    # Create Actor table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Actor (
            actor_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            birth_year INTEGER
        )
    ''')

    # Create Movie table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Movie (
            movie_id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            genre TEXT,
            release_year INTEGER,
            director_id INTEGER,
            FOREIGN KEY (director_id) REFERENCES Director(director_id)
        )
    ''')

    # Create User table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS User (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            email TEXT UNIQUE,
            password TEXT
        )
    ''')

    # Create Movie_Actor table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Movie_Actor (
            movie_id INTEGER,
            actor_id INTEGER,
            PRIMARY KEY (movie_id, actor_id),
            FOREIGN KEY (movie_id) REFERENCES Movie(movie_id),
            FOREIGN KEY (actor_id) REFERENCES Actor(actor_id)
        )
    ''')

    # Create Review table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Review (
            review_id INTEGER PRIMARY KEY AUTOINCREMENT,
            movie_id INTEGER,
            user_id INTEGER,
            rating INTEGER,
            comment TEXT,
            FOREIGN KEY (movie_id) REFERENCES Movie(movie_id),
            FOREIGN KEY (user_id) REFERENCES User(user_id)
        )
    ''')

    conn.commit()
    conn.close()
    print("Database and tables created successfully.")

if __name__ == "__main__":
    setup_database()
