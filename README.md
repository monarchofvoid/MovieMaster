# Movie Management System

This project is a movie database management system with a Python UI and SQLite backend.

## Features
- User registration and login
- Admin login (fixed: username `admin`, password `admin123`)
- Admin can:
  - View all movies
  - Add, edit, delete movies
- Users can:
  - View all movies
  - Search movies by genre, director, or actor

## Project Structure
```
movie_db/
├── main.py              # Main Python launcher with UI
├── db_setup.py          # Sets up the SQLite database
├── auth.py              # Handles registration and login
├── admin_panel.py       # Admin features
├── user_panel.py        # User features
├── utils.py             # Helper functions
├── movies.db            # SQLite database file (created after running setup)
└── README.md            # This file
```

## Setup Instructions

1️⃣ Install Python 3.

2️⃣ Install required modules (only `tkinter`, which is standard in most Python installs).

3️⃣ Set up the database:
```bash
python db_setup.py
```

4️⃣ Launch the application:
```bash
python main.py
```

5️⃣ Use admin account (username: `admin`, password: `admin123`) for full control.

## Notes
- All user passwords are stored as SHA-256 hashes.
- Movies, actors, and directors are managed through the admin panel.
- Regular users can browse and search but not modify data.

Enjoy managing your movie collection!
