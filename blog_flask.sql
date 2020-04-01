-- phpMyAdmin SQL Dump
-- version 4.9.3
-- https://www.phpmyadmin.net/
--
-- Host: localhost:8889
-- Generation Time: Apr 01, 2020 at 02:50 PM
-- Server version: 5.7.26
-- PHP Version: 7.4.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `blog_flask`
--

-- --------------------------------------------------------

--
-- Table structure for table `posts`
--

CREATE TABLE `posts` (
  `post_id` int(10) NOT NULL,
  `post_title` varchar(255) NOT NULL,
  `post_content` varchar(255) NOT NULL,
  `post_time` datetime DEFAULT NULL,
  `filename` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `posts`
--

INSERT INTO `posts` (`post_id`, `post_title`, `post_content`, `post_time`, `filename`) VALUES
(1, 'this is my post tile 1', 'post description comes here 1', NULL, 'filename1'),
(2, 'title2', 'description2', NULL, 'filename2'),
(3, 'title2', 'description2', '2020-03-30 06:09:33', 'filename2'),
(4, 'title2', 'description2', '2020-03-30 06:10:02', 'filename2'),
(5, 'title2', 'description2', '2020-03-30 06:10:43', 'filename2'),
(6, 'title 1', 'content 1', '2020-03-30 15:53:19', 'alok.txt');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `usr_id` int(10) NOT NULL,
  `usr_username` varchar(255) NOT NULL,
  `usr_password` varchar(255) NOT NULL,
  `usr_token` varchar(500) NOT NULL,
  `usr_status` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`usr_id`, `usr_username`, `usr_password`, `usr_token`, `usr_status`) VALUES
(11, 'alok', 'sha256$JPBiGVCE$7a74cca70e03fa8a03b1951514a454641260c02bf9702a8e4870f7421016635b', '', 1),
(12, 'alok1', 'sha256$2pkBSKdh$e50777b1f7609650be16b6585300ebb1651dbb159b54ef240179d459c121a226', '', 1),
(13, 'aloksingh', 'sha256$T6Pi1HVt$1ce0dbdec7b9439a2320bbc00c137b01964c5bd7af3ef4b1ee2e74d231082237', '', 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`post_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`usr_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `posts`
--
ALTER TABLE `posts`
  MODIFY `post_id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `usr_id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
