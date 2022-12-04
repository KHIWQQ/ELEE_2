-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 04, 2022 at 05:36 PM
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
(1, '1', 'q', 'q', 1, 0),
(1, '1', 'a', 'a', 0, 1),
(1, '1', 'a', 'a', 1, 0),
(1, '1', 'a', 'a', 1, 0),
(0, '', '', '', 1, 0),
(1, '1', 'bb', 'bb', 1, 0),
(1, '1', 'bb', 'bb', 1, 0),
(1, '1', 'bb', 'bb', 1, 0),
(1, '1', 'bb', 'bb', 1, 0),
(1, '1', 'aa', 'aa', 1, 0),
(1, '1', 'bb', '', 1, 0),
(1, '1', 'aa', 'aa', 1, 0),
(1, '1', 'aa', 'aa', 1, 0),
(1, '1', 'bb', 'bb', 1, 0),
(1, '1', 'bb', 'bb', 1, 0),
(0, '1', 'q', '', 1, 0),
(0, '2', 'b', '', 1, 0),
(0, '2', 'c', '', 1, 0),
(0, '2', 'c', '', 1, 0),
(0, '1', 'a', '', 1, 0),
(0, '2', 'b', '', 1, 0),
(0, '2', 'd', '', 1, 0),
(0, '1', 'z', '', 1, 0),
(0, '1', 'z', '', 1, 0),
(1, '1', 'z', 'z', 1, 0),
(0, '1', 'z', '', 1, 0),
(0, '1', 'z', '', 1, 0),
(0, '2', 'dd', '', 1, 0),
(0, '2', 'dd', '', 1, 0),
(0, '2', 'dd', '', 0, 1);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
