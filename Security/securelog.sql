SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

CREATE DATABASE security;

CREATE TABLE `securelog` (
  `quater` int(11) NOT NULL,
  `position` varchar(33) NOT NULL,
  `fname` varchar(33) NOT NULL,
  `sname` varchar(33) NOT NULL,
  `onduty` int(11) NOT NULL,
  `outduty` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `securelog` (`quater`, `position`, `fname`, `sname`, `onduty`, `outduty`) VALUES
(1, '1', 'AAA', 'AAA', 1, 0),
(1, '2', 'BBB', 'BBB', 1, 0),
(1, '3', 'CCC', 'CCC', 1, 0),
(1, '4', 'DDD', 'DDD', 1, 0),
(1, '5', 'EEE', 'EEE', 1, 0),
(1, '6', 'FFF', 'FFF', 1, 0),
(1, '7', 'ZZZ', 'ZZZ', 1, 0);
COMMIT;
