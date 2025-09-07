-- Clinic Booking System Database

CREATE DATABASE IF NOT EXISTS clinic_booking;
USE clinic_booking;

CREATE TABLE IF NOT EXISTS Patients (
    patient_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(15) UNIQUE NOT NULL,
    date_of_birth DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS Doctors (
    doctor_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    specialization VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(15) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS Appointments (
    appointment_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT NOT NULL,
    doctor_id INT NOT NULL,
    appointment_date DATETIME NOT NULL,
    reason TEXT,
    status VARCHAR(50) DEFAULT 'Scheduled',
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id) ON DELETE CASCADE,
    FOREIGN KEY (doctor_id) REFERENCES Doctors(doctor_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Prescriptions (
    prescription_id INT AUTO_INCREMENT PRIMARY KEY,
    appointment_id INT NOT NULL,
    medication VARCHAR(200) NOT NULL,
    dosage VARCHAR(100) NOT NULL,
    instructions TEXT,
    FOREIGN KEY (appointment_id) REFERENCES Appointments(appointment_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Bills (
    bill_id INT AUTO_INCREMENT PRIMARY KEY,
    appointment_id INT NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    status VARCHAR(50) DEFAULT 'Unpaid',
    FOREIGN KEY (appointment_id) REFERENCES Appointments(appointment_id) ON DELETE CASCADE
);

-- Sample Data
INSERT INTO Patients (first_name, last_name, email, phone, date_of_birth) VALUES
('John', 'Doe', 'johndoe@example.com', '0712345678', '1990-05-15'),
('Jane', 'Smith', 'janesmith@example.com', '0723456789', '1985-09-22');

INSERT INTO Doctors (first_name, last_name, specialization, email, phone) VALUES
('Alice', 'Brown', 'Cardiologist', 'alicebrown@clinic.com', '0734567890'),
('Bob', 'Johnson', 'Dermatologist', 'bobjohnson@clinic.com', '0745678901');

INSERT INTO Appointments (patient_id, doctor_id, appointment_date, reason, status) VALUES
(1, 1, '2025-09-10 10:00:00', 'Routine Checkup', 'Scheduled'),
(2, 2, '2025-09-11 14:30:00', 'Skin Rash', 'Scheduled');

INSERT INTO Prescriptions (appointment_id, medication, dosage, instructions) VALUES
(1, 'Aspirin', '100mg', 'Take one tablet daily'),
(2, 'Hydrocortisone Cream', 'Apply twice daily', 'Apply to affected area');

INSERT INTO Bills (appointment_id, amount, status) VALUES
(1, 2000.00, 'Unpaid'),
(2, 1500.00, 'Paid');
