create database todolist;
create table todolist.todolist (id int NOT NULL AUTO_INCREMENT PRIMARY KEY, checked bool, task varchar(256)) ENGINE=InnoDB DEFAULT CHARSET=utf8;
