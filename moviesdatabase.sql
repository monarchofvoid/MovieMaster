CREATE DATABASE movie_db;
USE movie_db;
-- Create table: Director
CREATE TABLE Director (
    director_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    name TEXT,
    birth_year INTEGER
);

-- Create table: Actor
CREATE TABLE Actor (
    actor_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    name TEXT,
    birth_year INTEGER
);

-- Create table: Movie
CREATE TABLE Movie (
    movie_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    title TEXT,
    genre TEXT,
    release_year INTEGER,
    director_id INTEGER,
    FOREIGN KEY (director_id) REFERENCES Director(director_id)
);

-- Create table: User
CREATE TABLE User (
    user_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    username TEXT UNIQUE,
    email TEXT UNIQUE
);

-- Create table: Movie_Actor
CREATE TABLE Movie_Actor (
    movie_id INTEGER,
    actor_id INTEGER,
    PRIMARY KEY (movie_id, actor_id),
    FOREIGN KEY (movie_id) REFERENCES Movie(movie_id),
    FOREIGN KEY (actor_id) REFERENCES Actor(actor_id)
);

-- Create table: Review
CREATE TABLE Review (
    review_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    user_id INTEGER,
    movie_id INTEGER,
    rating REAL CHECK (rating BETWEEN 0 AND 10),
    comment TEXT,
    review_date TEXT,
    FOREIGN KEY (user_id) REFERENCES User(user_id),
    FOREIGN KEY (movie_id) REFERENCES Movie(movie_id)
);

-- Insert Directors
INSERT INTO Director (name, birth_year) VALUES
('Frank Darabont', 1959),
('Francis Ford Coppola', 1939),
('Christopher Nolan', 1970),
('Sidney Lumet', 1924),
('Steven Spielberg', 1946),
('Peter Jackson', 1961),
('Quentin Tarantino', 1963),
('Sergio Leone', 1929),
('David Fincher', 1962),
('Robert Zemeckis', 1951);

-- Insert Actors
INSERT INTO Actor (name, birth_year) VALUES
('Tim Robbins', 1958),
('Morgan Freeman', 1937),
('Marlon Brando', 1924),
('Al Pacino', 1940),
('Christian Bale', 1974),
('Heath Ledger', 1979),
('Liam Neeson', 1952),
('Ben Kingsley', 1943),
('Elijah Wood', 1981),
('Brad Pitt', 1963);

-- Insert Movies
INSERT INTO Movie (title, genre, release_year, director_id) VALUES
('The Shawshank Redemption', 'Drama', 1994, 1),
('The Godfather', 'Crime', 1972, 2),
('The Dark Knight', 'Action', 2008, 3),
('12 Angry Men', 'Drama', 1957, 4),
('Schindler\'s List', 'Biography', 1993, 5),
('The Lord of the Rings: The Return of the King', 'Adventure', 2003, 6),
('Pulp Fiction', 'Crime', 1994, 7),
('The Good, the Bad and the Ugly', 'Western', 1966, 8),
('Fight Club', 'Drama', 1999, 9),
('Forrest Gump', 'Drama', 1994, 10);

-- Insert Movie_Actor relationships
INSERT INTO Movie_Actor (movie_id, actor_id) VALUES
(1,1),(1,2),
(2,3),(2,4),
(3,5),(3,6),
(4,4),
(5,7),(5,8),
(6,9),
(7,4),
(8,3),
(9,10),
(10,10);

-- Insert Users
INSERT INTO User (username, email) VALUES
('moviebuff1', 'moviebuff1@example.com'),
('cinemalover', 'cinemalover@example.com'),
('critic101', 'critic101@example.com');

-- Insert Reviews
INSERT INTO Review (user_id, movie_id, rating, comment, review_date) VALUES
(1,1,9.5,'Masterpiece of hope and friendship.','2025-05-01'),
(2,2,9.0,'A legendary crime saga.','2025-05-01'),
(3,3,9.7,'Dark, thrilling, unforgettable.','2025-05-01'),
(1,4,9.0,'A classic courtroom drama.','2025-05-02'),
(2,5,9.2,'Heart-wrenching and beautifully made.','2025-05-02'),
(3,6,9.5,'Epic fantasy at its best.','2025-05-02'),
(1,7,9.4,'Stylish, violent, and brilliant.','2025-05-03'),
(2,8,9.3,'Iconic spaghetti western.','2025-05-03'),
(3,9,9.1,'Psychological mind-bender.','2025-05-03'),
(1,10,9.4,'Life is like a box of chocolates.','2025-05-03');
