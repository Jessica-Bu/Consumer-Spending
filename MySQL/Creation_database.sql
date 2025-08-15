
CREATE DATABASE IF NOT EXISTS consumer_spending;

USE consumer_spending;

CREATE TABLE `country` (
  `country_ID` varchar(2),
  `country` varchar(30),
  PRIMARY KEY (`country_ID`)
);

CREATE TABLE `year` (
  `year_ID` int,
  `year` year,
  PRIMARY KEY (`year_ID`)
);

CREATE TABLE `KPIs_total` (
  `indicator_ID` varchar(4),
  `country_ID` varchar(2),
  `year_ID` int,
  `consumption_MEUR` dec(20,2),
  `net_income_MEUR` dec(20,2),
  `hvpi_2015` int,
  `inflation` dec(20,1),
  `saving_net` int,
  `saving_ratio` dec(20,2),
  PRIMARY KEY (`indicator_ID`),
  FOREIGN KEY (`country_ID`) REFERENCES `country`(`country_ID`),
  FOREIGN KEY (`year_ID`) REFERENCES `year`(`year_ID`)
);

CREATE TABLE `category` (
  `category_ID` varchar(3),
  `category` varchar(200),
  PRIMARY KEY (`category_ID`)
);

CREATE TABLE `consumption_cat` (
  `consumption_ID` varchar(8),
  `country_ID` varchar(2),
  `year_ID` int,
  `category_ID` varchar(3),
  `consumption_MEUR` int,
  PRIMARY KEY (`consumption_ID`),
  FOREIGN KEY (`country_ID`) REFERENCES `country`(`country_ID`),
  FOREIGN KEY (`year_ID`) REFERENCES `year`(`year_ID`),
  FOREIGN KEY (`category_ID`) REFERENCES `category`(`category_ID`)
);

CREATE TABLE `gender` (
  `gender_ID` varchar(2),
  `gender` varchar(20),
  PRIMARY KEY (`gender_ID`)
);

CREATE TABLE `age` (
  `age_ID` varchar(4),
  `age_group` varchar(20),
  PRIMARY KEY (`age_ID`)
);

CREATE TABLE `income_age_gender` (
  `income_ID` varchar(10),
  `country_ID` varchar(2),
  `year_ID` int,
  `age_ID` varchar(3),
  `gender_ID` varchar(1),
  `median_income_MEUR` dec(20,2),
  PRIMARY KEY (`income_ID`),
  FOREIGN KEY (`country_ID`) REFERENCES `country`(`country_ID`),
  FOREIGN KEY (`year_ID`) REFERENCES `year`(`year_ID`),
  FOREIGN KEY (`age_ID`) REFERENCES `age`(`age_ID`),
  FOREIGN KEY (`gender_ID`) REFERENCES `gender`(`gender_ID`)
);







