CREATE DATABASE dlproject;
Use dlproject;

create table students(
  student_id varchar(20) PRIMARY KEY,
  name varchar(100) NOT NULL,
  email varchar(100),
  phone varchar(20),
  course varchar(100),
  created_at timestamp Default current_timestamp);
  
  create table attendance(
  id INT auto_increment Primary Key,
  student_id varchar(20) not null,
  attendance_date date not null,
  attendance_time time not null,
  status varchar(20) default 'Present',
  Foreign key (student_id)
  references students(student_id),
  Unique(student_id,attendance_date)
  );
  
  create table users(
  id int auto_increment Primary Key,
  username varchar(50) unique not null,
  password_hash varchar(255) not null,
  role varchar(20) default 'admin'
  );
  
  create table face_encodings(
  id int auto_increment primary key,
  student_id varchar(20) not null,
  encoding_reference varchar(255),
  created_at timestamp default current_timestamp,
  foreign key(student_id)
  references students(student_id)
  );
  

  
