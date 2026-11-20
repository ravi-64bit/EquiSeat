-- Fresh EquiSeat database schema (MySQL / MariaDB)
CREATE DATABASE IF NOT EXISTS equiseat
  CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE equiseat;

CREATE TABLE IF NOT EXISTS rooms (
  rid INT NOT NULL AUTO_INCREMENT,
  room_name VARCHAR(5) NOT NULL,
  num_rows INT NOT NULL,
  num_cols INT NOT NULL,
  PRIMARY KEY (rid),
  UNIQUE KEY uq_rooms_name (room_name),
  CONSTRAINT chk_rooms_rows CHECK (num_rows > 0),
  CONSTRAINT chk_rooms_cols CHECK (num_cols > 0)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS student_data (
  id INT NOT NULL AUTO_INCREMENT,
  regd_no VARCHAR(30) NOT NULL,
  name VARCHAR(100) NOT NULL,
  section VARCHAR(40) NOT NULL,
  PRIMARY KEY (id),
  UNIQUE KEY uq_student_regd_no (regd_no),
  KEY idx_student_section (section)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS subjects (
  subid INT NOT NULL AUTO_INCREMENT,
  sub_name VARCHAR(100) NOT NULL,
  sub_code VARCHAR(8) NOT NULL,
  PRIMARY KEY (subid),
  UNIQUE KEY uq_subject_code (sub_code)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS exams (
  regd_no VARCHAR(30) NOT NULL,
  sub_code VARCHAR(8) NOT NULL,
  PRIMARY KEY (regd_no, sub_code),
  KEY idx_exams_subject (sub_code),
  CONSTRAINT fk_exams_student
    FOREIGN KEY (regd_no) REFERENCES student_data (regd_no)
    ON UPDATE CASCADE ON DELETE CASCADE,
  CONSTRAINT fk_exams_subject
    FOREIGN KEY (sub_code) REFERENCES subjects (sub_code)
    ON UPDATE CASCADE ON DELETE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
