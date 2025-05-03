import sqlite3
import hashlib

DB_FILE = 'movies.db'
ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD_HASH = hashlib.sha256('admin123'.encode()).hexdigest()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(username, email, password):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO User (username, email, password) VALUES (?, ?, ?)",
                       (username, email, hash_password(password)))
        conn.commit()
        print(f"User '{username}' registered successfully.")
    except sqlite3.IntegrityError:
        print("Username or email already exists.")
    conn.close()

def login_user(username, password):
    if username == ADMIN_USERNAME and hash_password(password) == ADMIN_PASSWORD_HASH:
        print("Admin login successful.")
        return 'admin'
    
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM User WHERE username = ? AND password = ?",
                   (username, hash_password(password)))
    user = cursor.fetchone()
    conn.close()
    if user:
        print(f"User '{username}' login successful.")
        return 'user'
    else:
        print("Invalid username or password.")
        return None

if __name__ == "__main__":
    # For quick testing
    register_user('testuser', 'test@example.com', 'testpass')
    login_user('testuser', 'testpass')
    login_user('admin', 'admin123')
