-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 01, 2024 at 12:51 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `equiseat`
--

-- --------------------------------------------------------

--
-- Table structure for table `exams`
--

CREATE TABLE `exams` (
  `regd_no` varchar(100) DEFAULT NULL,
  `sub_code` varchar(8) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `exams`
--

INSERT INTO `exams` (`regd_no`, `sub_code`) VALUES
('21331A1201', 'A3CIT101'),
('21331A1202', 'A3CIT101'),
('21331A1203', 'A3CIT101'),
('21331A1204', 'A3CIT101'),
('21331A1205', 'A3CIT101'),
('21331A1206', 'A3CIT101'),
('21331A1207', 'A3CIT101'),
('21331A1208', 'A3CIT101'),
('21331A1209', 'A3CIT101'),
('21331A1210', 'A3CIT101'),
('21331A1211', 'A3CIT101'),
('21331A1212', 'A3CIT101'),
('21331A1213', 'A3CIT101'),
('21331A1214', 'A3CIT101'),
('21331A1215', 'A3CIT101'),
('21331A1216', 'A3CIT101'),
('21331A1217', 'A3CIT101'),
('21331A1218', 'A3CIT101'),
('21331A1219', 'A3CIT101'),
('21331A1220', 'A3CIT101'),
('21331A1221', 'A3CIT101');

-- --------------------------------------------------------

--
-- Table structure for table `rooms`
--

CREATE TABLE `rooms` (
  `rid` int(11) NOT NULL,
  `room_name` varchar(5) DEFAULT NULL,
  `num_rows` int(3) DEFAULT NULL,
  `num_cols` int(3) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `rooms`
--

INSERT INTO `rooms` (`rid`, `room_name`, `num_rows`, `num_cols`) VALUES
(1, 'IT-1', 7, 3),
(2, 'IT-2', 7, 3),
(3, 'IT-3', 7, 3),
(4, 'IT-4', 7, 3);

-- --------------------------------------------------------

--
-- Table structure for table `student_data`
--

CREATE TABLE `student_data` (
  `id` int(11) NOT NULL,
  `regd_no` varchar(30) DEFAULT NULL,
  `name` varchar(30) DEFAULT NULL,
  `section` varchar(40) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `student_data`
--

INSERT INTO `student_data` (`id`, `regd_no`, `name`, `section`) VALUES
(1, '21331A1201', 'name1', 'IT3a'),
(2, '21331A1202', 'name2', 'IT3a'),
(3, '21331A1203', 'name3', 'IT3a'),
(4, '21331A1204', 'name4', 'IT3a'),
(5, '21331A1205', 'name5', 'IT3a'),
(6, '21331A1206', 'name6', 'IT3a'),
(7, '21331A1207', 'name7', 'IT3a'),
(8, '21331A1208', 'name8', 'IT3a'),
(9, '21331A1209', 'name9', 'IT3a'),
(10, '21331A1210', 'name10', 'IT3a'),
(11, '21331A1211', 'name11', 'IT3a'),
(12, '21331A1212', 'name12', 'IT3a'),
(13, '21331A1213', 'name13', 'IT3a'),
(14, '21331A1214', 'name14', 'IT3a'),
(15, '21331A1215', 'name15', 'IT3a'),
(16, '21331A1216', 'name16', 'IT3a'),
(17, '21331A1217', 'name17', 'IT3a'),
(18, '21331A1218', 'name18', 'IT3a'),
(19, '21331A1219', 'name19', 'IT3a'),
(20, '21331A1220', 'name20', 'IT3a'),
(21, '21331A1221', 'name21', 'IT3a'),
(27, '21331A1227', 'name27', 'IT3a'),
(28, '21331A1228', 'name28', 'IT3a'),
(29, '21331A1229', 'name29', 'IT3a'),
(30, '21331A1230', 'name30', 'IT3a'),
(31, '21331A1231', 'name31', 'IT3a'),
(32, '21331A1232', 'name32', 'IT3a'),
(33, '21331A1233', 'name33', 'IT3a'),
(34, '21331A1234', 'name34', 'IT3a'),
(35, '21331A1235', 'name35', 'IT3a'),
(36, '21331A1236', 'name36', 'IT3a'),
(37, '21331A1237', 'name37', 'IT3a'),
(38, '21331A1238', 'name38', 'IT3a'),
(39, '21331A1239', 'name39', 'IT3a'),
(40, '21331A1240', 'name40', 'IT3a'),
(41, '21331A1241', 'name41', 'IT3a'),
(42, '21331A1242', 'name42', 'IT3a'),
(43, '21331A1243', 'name43', 'IT3a'),
(44, '21331A1244', 'name44', 'IT3a'),
(45, '21331A1245', 'name45', 'IT3a'),
(46, '21331A1246', 'name46', 'IT3a'),
(47, '21331A1247', 'name47', 'IT3a'),
(48, '21331A1248', 'name48', 'IT3a'),
(49, '21331A1249', 'name49', 'IT3a'),
(50, '21331A1250', 'name50', 'IT3a'),
(51, '21331A1251', 'name51', 'IT3a'),
(52, '21331A1252', 'name52', 'IT3a'),
(53, '21331A1253', 'name53', 'IT3a'),
(54, '21331A1254', 'name54', 'IT3a'),
(55, '21331A1255', 'name55', 'IT3a'),
(56, '21331A1256', 'name56', 'IT3a'),
(57, '21331A1257', 'name57', 'IT3a'),
(58, '21331A1258', 'name58', 'IT3a'),
(59, '21331A1259', 'name59', 'IT3a'),
(60, '21331A1260', 'name60', 'IT3a'),
(61, '21331A1261', 'name61', 'IT3a'),
(62, '21331A1262', 'name62', 'IT3a'),
(63, '21331A1263', 'name63', 'IT3a'),
(64, '21331A1264', 'name64', 'IT3a'),
(65, '21331A1265', 'name65', 'IT3a'),
(66, '21331A1266', 'name66', 'IT3a'),
(67, '21331A1267', 'name67', 'it3b'),
(68, '21331A1268', 'name68', 'it3b'),
(69, '21331A1269', 'name69', 'it3b'),
(70, '21331A1270', 'name70', 'it3b'),
(71, '21331A1271', 'name71', 'it3b'),
(72, '21331A1272', 'name72', 'it3b'),
(73, '21331A1273', 'name73', 'it3b'),
(74, '21331A1274', 'name74', 'it3b'),
(75, '21331A1275', 'name75', 'it3b'),
(76, '21331A1276', 'name76', 'it3b'),
(77, '21331A1277', 'name77', 'it3b'),
(78, '21331A1278', 'name78', 'it3b'),
(79, '21331A1279', 'name79', 'it3b'),
(80, '21331A1280', 'name80', 'it3b'),
(81, '21331A1281', 'name81', 'it3b'),
(82, '21331A1282', 'name82', 'it3b'),
(83, '21331A1283', 'name83', 'it3b'),
(84, '21331A1284', 'name84', 'it3b'),
(85, '21331A1285', 'name85', 'it3b'),
(86, '21331A1286', 'name86', 'it3b'),
(87, '21331A1287', 'name87', 'it3b'),
(88, '21331A1288', 'name88', 'it3b'),
(89, '21331A1289', 'name89', 'it3b'),
(90, '21331A1290', 'name90', 'it3b'),
(91, '21331A1291', 'name91', 'it3b'),
(92, '21331A1292', 'name92', 'it3b'),
(93, '21331A1293', 'name93', 'it3b'),
(94, '21331A1294', 'name94', 'it3b'),
(95, '21331A1295', 'name95', 'it3b'),
(96, '21331A1296', 'name96', 'it3b'),
(97, '21331A1297', 'name97', 'it3b'),
(98, '21331A1298', 'name98', 'it3b'),
(99, '21331A1299', 'name99', 'it3b'),
(100, '21331A1300', 'name100', 'it3b'),
(101, '21331A1301', 'name101', 'it3b'),
(102, '21331A1302', 'name102', 'it3b'),
(103, '21331A1303', 'name103', 'it3b'),
(104, '21331A1304', 'name104', 'it3b'),
(105, '21331A1305', 'name105', 'it3b'),
(106, '21331A1306', 'name106', 'it3b'),
(107, '21331A1307', 'name107', 'it3b'),
(108, '21331A1308', 'name108', 'it3b'),
(109, '21331A1309', 'name109', 'it3b'),
(110, '21331A1310', 'name110', 'it3b'),
(111, '21331A1311', 'name111', 'it3b'),
(112, '21331A1312', 'name112', 'it3b'),
(113, '21331A1313', 'name113', 'it3b'),
(114, '21331A1314', 'name114', 'it3b'),
(115, '21331A1315', 'name115', 'it3b'),
(116, '21331A1316', 'name116', 'it3b'),
(117, '21331A1317', 'name117', 'it3b'),
(118, '21331A1318', 'name118', 'it3b'),
(119, '21331A1319', 'name119', 'it3b'),
(120, '21331A1320', 'name120', 'it3b'),
(121, '21331A1321', 'name121', 'it3b'),
(122, '21331A1322', 'name122', 'it3b'),
(123, '21331A1323', 'name123', 'it3b'),
(124, '21331A1324', 'name124', 'it3b'),
(125, '21331A1325', 'name125', 'it3b'),
(126, '21331A1326', 'name126', 'it3b'),
(127, '21331A1327', 'name127', 'it3b'),
(128, '21331A1328', 'name128', 'it3b');

-- --------------------------------------------------------

--
-- Table structure for table `subjects`
--

CREATE TABLE `subjects` (
  `subid` int(3) NOT NULL,
  `sub_name` varchar(30) DEFAULT NULL,
  `sub_code` varchar(8) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `subjects`
--

INSERT INTO `subjects` (`subid`, `sub_name`, `sub_code`) VALUES
(1, 'Etc', 'A3CIT101'),
(2, 'SPA', 'A3IT607');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `rooms`
--
ALTER TABLE `rooms`
  ADD PRIMARY KEY (`rid`),
  ADD UNIQUE KEY `unique_room_name` (`room_name`);

--
-- Indexes for table `student_data`
--
ALTER TABLE `student_data`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `subjects`
--
ALTER TABLE `subjects`
  ADD PRIMARY KEY (`subid`),
  ADD UNIQUE KEY `sub_code` (`sub_code`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `rooms`
--
ALTER TABLE `rooms`
  MODIFY `rid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `student_data`
--
ALTER TABLE `student_data`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=129;

--
-- AUTO_INCREMENT for table `subjects`
--
ALTER TABLE `subjects`
  MODIFY `subid` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
