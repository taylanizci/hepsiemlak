-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Anamakine: 127.0.0.1:3306
-- Üretim Zamanı: 30 Mar 2022, 11:55:56
-- Sunucu sürümü: 5.7.36
-- PHP Sürümü: 7.4.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Veritabanı: `hepsiemlak`
--

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `fotograf`
--

DROP TABLE IF EXISTS `fotograf`;
CREATE TABLE IF NOT EXISTS `fotograf` (
  `foto_id` int(11) NOT NULL AUTO_INCREMENT,
  `ilan_id` int(11) NOT NULL,
  `foto_ad` varchar(50) NOT NULL,
  PRIMARY KEY (`foto_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `hepsiemlak`
--

DROP TABLE IF EXISTS `hepsiemlak`;
CREATE TABLE IF NOT EXISTS `hepsiemlak` (
  `ilan_id` int(11) NOT NULL AUTO_INCREMENT,
  `emlakisim` varchar(100) NOT NULL,
  `ilanad` varchar(200) NOT NULL,
  `ilanfiyat` varchar(20) NOT NULL,
  PRIMARY KEY (`ilan_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
