/*
    Title: whatabook.init.sql
    Shannon Russell-Phipps
    12/14/2021
    Description: WhatABook database initialization script.
*/

-- drop test user if exists 
DROP USER IF EXISTS 'whatabook_user'@'localhost';

-- create whatabook_user and grant them all privileges to the whatabook database 
CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

-- grant all privileges to the whatabook database to user whatabook_user on localhost 
GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';

-- drop contstraints if they exist
ALTER TABLE wishlist DROP FOREIGN KEY fk_book;
ALTER TABLE wishlist DROP FOREIGN KEY fk_user;

-- drop tables if they exist
DROP TABLE IF EXISTS store;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS user;

/*
    Create table(s)
*/
CREATE TABLE store (
    store_id    INT             NOT NULL    AUTO_INCREMENT,
    locale      VARCHAR(500)    NOT NULL,
    PRIMARY KEY(store_id)
);

CREATE TABLE book (
    book_id     INT             NOT NULL    AUTO_INCREMENT,
    book_name   VARCHAR(200)    NOT NULL,
    author      VARCHAR(200)    NOT NULL,
    details     VARCHAR(500),
    PRIMARY KEY(book_id)
);

CREATE TABLE user (
    user_id         INT         NOT NULL    AUTO_INCREMENT,
    first_name      VARCHAR(75) NOT NULL,
    last_name       VARCHAR(75) NOT NULL,
    PRIMARY KEY(user_id) 
);

CREATE TABLE wishlist (
    wishlist_id     INT         NOT NULL    AUTO_INCREMENT,
    user_id         INT         NOT NULL,
    book_id         INT         NOT NULL,
    PRIMARY KEY (wishlist_id),
    CONSTRAINT fk_book
    FOREIGN KEY (book_id)
        REFERENCES book(book_id),
    CONSTRAINT fk_user
    FOREIGN KEY (user_id)
        REFERENCES user(user_Id)
);

/*
    insert store record 
*/
INSERT INTO store(locale)
    VALUES('2625 W Grandview Rd, Phoenix, AZ 85023');

/*
    insert book records 
*/
INSERT INTO book(book_name, author)
	VALUES('Silent Spring', 'Rachel Carson');
INSERT INTO book(book_name, author)
	VALUES('Mean Girls Club', 'Ryan Heska');
INSERT INTO book(book_name, author, details)
	VALUES('Captain Marvel', 'Kelly Sue DeConnicha and Christopher Sebela', 'Earth’s mightiest hero');
INSERT INTO book(book_name, author, details)
	VALUES('Moon Knight', 'Doug Moench', 'Bad moon rising');
INSERT INTO book(book_name, author)
	VALUES('Embrace Your Weird', 'Felicia Day');
INSERT INTO book(book_name, author)
	VALUES('Every Tool’s A Hammer', 'Adam Savage');
INSERT INTO book(book_name, author)
	VALUES('Welcome to the Universe', 'Neil deGrasse Tyson');
INSERT INTO book(book_name, author)
	VALUES('Just Jackie', 'Edward Klein');
INSERT INTO book(book_name, author)
	VALUES('Peanuts Treasury', 'Charles Schulz');

/*
    insert user
*/ 
INSERT INTO user(first_name, last_name)
VALUES('Natasha', 'Romanov');
INSERT INTO user(first_name, last_name)
	VALUES('Scott', 'Lang');
INSERT INTO user(first_name, last_name)
	VALUES('Sam', 'Wilson');

/*
    insert wishlist records 
*/
INSERT INTO wishlist(user_id, book_id) 
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Natasha'), 
        (SELECT book_id FROM book WHERE book_name = 'Mean Girls Club')
    );
INSERT INTO wishlist(user_id, book_id) 
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Scott'), 
        (SELECT book_id FROM book WHERE book_name = 'Welcome to the Universe')
    );
INSERT INTO wishlist(user_id, book_id) 
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Sam'), 
        (SELECT book_id FROM book WHERE book_name = 'Embrace Your Weird')
    );

