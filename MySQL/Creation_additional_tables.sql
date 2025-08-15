USE consumer_spending;

CREATE TABLE `avg_ consumption_cat_15_19` (
  `cons_15_19_ID` varchar(8),
  `country_ID` varchar(2),
  `category_ID` varchar(3),
  `avg_consumption_MEUR` int,
  PRIMARY KEY (`cons_15_19_ID`),
  FOREIGN KEY (`country_ID`) REFERENCES `country`(`country_ID`),
  FOREIGN KEY (`category_ID`) REFERENCES `category`(`category_ID`)
);

CREATE TABLE `inflation_cat` (
  `inflation_cat_ID` varchar(8),
  `country_ID` varchar(2),
  `year_ID` int,
  `category_ID` varchar(3),
  `inflation_%` dec(20,2),
  PRIMARY KEY (`inflation_cat_ID`),
  FOREIGN KEY (`country_ID`) REFERENCES `country`(`country_ID`),
  FOREIGN KEY (`year_ID`) REFERENCES `year`(`year_ID`),
  FOREIGN KEY (`category_ID`) REFERENCES `category`(`category_ID`)
);