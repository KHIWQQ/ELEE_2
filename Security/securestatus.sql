SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

CREATE DATABASE security;

CREATE TABLE `securestatus` (
  `quater` int(11) NOT NULL,
  `fname` varchar(33) NOT NULL,
  `sname` varchar(33) NOT NULL,
  `company` int(11) NOT NULL,
  `platoon` int(11) NOT NULL,
  `position` varchar(22) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `securestatus` (`quater`, `fname`, `sname`, `company`, `platoon`, `position`) VALUES
(1, 'AAA', 'AAA', 1, 1, '1'),
(1, 'BBB', 'BBB', 1, 1, '2'),
(1, 'CCC', 'CCC', 1, 1, '3'),
(1, 'DDD', 'DDD', 2, 1, '4'),
(1, 'EEE', 'EEE', 2, 1, '5'),
(1, 'FFF', 'FFF', 3, 1, '6'),
(1, 'ZZZ', 'ZZZ', 3, 1, '7');
COMMIT;
