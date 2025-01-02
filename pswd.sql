-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 02, 2025 at 06:57 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12


-- --------------------------------------------------------


SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

--
-- Database: `pswd`
--

-- --------------------------------------------------------

--
-- Table structure for table `pswd`
--

CREATE TABLE `pswd` (
  `Pswd_id` int(11) NOT NULL,
  `Title` varchar(100) NOT NULL,
  `Title_desc` text DEFAULT NULL,
  `Password` varchar(100) NOT NULL,
  `Desc` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `pswd`
--

INSERT INTO `pswd` (`Pswd_id`, `Title`, `Title_desc`, `Password`, `Desc`) VALUES
(34, 'Username1', 'Email id', 'password1', 'hint1'),
(35, 'Username2', 'Email id', 'password2', 'hint2');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `pswd`
--
ALTER TABLE `pswd`
  ADD PRIMARY KEY (`Pswd_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `pswd`
--
ALTER TABLE `pswd`
  MODIFY `Pswd_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=36;
COMMIT;
