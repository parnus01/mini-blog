CREATE DATABASE homework;
use homework;

CREATE TABLE user (
  id int(11) NOT NULL AUTO_INCREMENT,
  username VARCHAR(20) NOT NULL,
  password CHAR(32) NOT NULL,
  primary key (id)
);

INSERT INTO user(id, username, password) values
(1, 'john', MD5('john123!')),
(2, 'emmy', MD5('emmy123!')),
(3, 'robert', MD5('robert123!'));


CREATE TABLE blog (
  id int(11) unsigned NOT NULL AUTO_INCREMENT,
  name VARCHAR(20) NOT NULL,
  category VARCHAR(10) NOT NULL,
  status TINYINT(2) NOT NULL,
  content MEDIUMTEXT NOT NULL,
  author_id int(11) NOT NULL,
  primary key (id)
);
