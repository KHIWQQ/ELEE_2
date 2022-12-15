-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 06, 2022 at 03:48 AM
-- Server version: 10.4.25-MariaDB
-- PHP Version: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `security`
--

-- --------------------------------------------------------

--
-- Table structure for table `securelog`
--

CREATE TABLE `securelog` (
  `quater` int(11) NOT NULL,
  `position` varchar(33) NOT NULL,
  `fname` varchar(33) NOT NULL,
  `sname` varchar(33) NOT NULL,
  `onduty` int(11) NOT NULL,
  `outduty` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `securelog`
--

INSERT INTO `securelog` (`quater`, `position`, `fname`, `sname`, `onduty`, `outduty`) VALUES
(1, '1', 'AAA', 'AAA', 1, 0),
(1, '2', 'BBB', 'BBB', 1, 0),
(1, '3', 'CCC', 'CCC', 1, 0),
(1, '4', 'DDD', 'DDD', 1, 0),
(1, '5', 'EEE', 'EEE', 1, 0),
(1, '6', 'FFF', 'FFF', 1, 0),
(1, '7', 'ZZZ', 'ZZZ', 1, 0);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
