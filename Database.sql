# Creating the database for the NLP project
CREATE DATABASE cv_attendance;

USE cv_attendance;

# CREATING THE TABLES For the project

# STUDENT TABLE->store student information
CREATE TABLE STUDENTS(
	student_id VARCHAR(20) PRIMARY KEY ,
    name VARCHAR(30) ,
    email VARCHAR(30),
    phone VARCHAR(20) ,
    COURSE VARCHAR(100),
    created_at TIMESTAMP  DEFAULT CURRENT_TIMESTAMP
    );
    SHOW TABLES;
    DROP TABLES STUDENTS;
    
    
# Attendance Table-> Store attendance records
CREATE TABLE attendance(
	id INT PRIMARY KEY AUTO_INCREMENT,
    student_id VARCHAR(20) NOT NULL,
    attendance_date DATE  NOT NULL,
    attendance_time TIME NOT NULL,
    status VARCHAR(20) DEFAULT 'PRESENT',
    FOREIGN KEY (student_id)  REFERENCES STUDENTS(student_id),
    UNIQUE (student_id,attendance_date)
    );
    
# USER-Store application users
    CREATE TABLE users(
		id INT PRIMARY KEy AUTO_INCREMENT,
        username VARCHAR(50)  UNIQUE NOT NULL,
        password_hash VARCHAR(30) NOT NULL,
        role VARCHAR(20) DEFAULT 'admin'
        );
        
# Face encoding ->stores refernces/metadata  associated with facial representation
CREATE TABLE face_encodings( 
		id INT PRIMARY KEY AUTO_INCREMENT,
        student_id varchar(20) NOT NULL,
        encoding_reference  VARCHAR(255),
        CREATED_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (student_id)  REFERENCES students(student_id)
        );
        
        show tables;

        
    
    