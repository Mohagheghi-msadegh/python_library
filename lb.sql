-- MySQL dump 10.13  Distrib 8.0.35, for Linux (x86_64)
--
-- Host: localhost    Database: library
-- ------------------------------------------------------
-- Server version	8.0.35-0ubuntu0.22.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Book`
--

DROP TABLE IF EXISTS `Book`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Book` (
  `ISBN` int NOT NULL,
  `Title` varchar(255) DEFAULT NULL,
  `Author` varchar(255) DEFAULT NULL,
  `publisher` varchar(255) DEFAULT NULL,
  `publication_year` int DEFAULT NULL,
  `number_of_instance` int DEFAULT NULL,
  `number_of_availible` int DEFAULT NULL,
  PRIMARY KEY (`ISBN`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Book`
--

LOCK TABLES `Book` WRITE;
/*!40000 ALTER TABLE `Book` DISABLE KEYS */;
INSERT INTO `Book` VALUES (171,'Computer Programming for Beginners','Natan Clark','Springer',2018,5,5),(978,'Introduction to Database Management System ','Satinder Bal Gupta','Laxmi Publications Pvt Ltd',2018,5,5),(2345,'Programmer avec Rust - pour une ','Jim  Blundya','First Interactive',2019,8,4),(9797,'C# & C++','Mark Reed',NULL,2023,2,2),(5435436,'sdfds',NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `Book` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Book_loan`
--

DROP TABLE IF EXISTS `Book_loan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Book_loan` (
  `ISBN` int DEFAULT NULL,
  `ID_e` int DEFAULT NULL,
  `ID` int DEFAULT NULL,
  `Browing_date` int DEFAULT NULL,
  `Delivery_data_set` int DEFAULT NULL,
  `Actual_delivery_date` int DEFAULT NULL,
  `Brrowing_date` int DEFAULT NULL,
  `penalty` int DEFAULT NULL,
  KEY `ISBN` (`ISBN`),
  KEY `ID` (`ID`),
  KEY `ID_e` (`ID_e`),
  CONSTRAINT `Book_loan_ibfk_1` FOREIGN KEY (`ISBN`) REFERENCES `Book` (`ISBN`),
  CONSTRAINT `Book_loan_ibfk_2` FOREIGN KEY (`ID`) REFERENCES `Person` (`ID`),
  CONSTRAINT `Book_loan_ibfk_3` FOREIGN KEY (`ID_e`) REFERENCES `Employee` (`ID_e`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Book_loan`
--

LOCK TABLES `Book_loan` WRITE;
/*!40000 ALTER TABLE `Book_loan` DISABLE KEYS */;
INSERT INTO `Book_loan` VALUES (171,30092,324,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `Book_loan` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Employee`
--

DROP TABLE IF EXISTS `Employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Employee` (
  `ID_e` int NOT NULL,
  `name` varchar(200) DEFAULT NULL,
  `family_name` varchar(200) DEFAULT NULL,
  `employment_year` int DEFAULT NULL,
  PRIMARY KEY (`ID_e`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Employee`
--

LOCK TABLES `Employee` WRITE;
/*!40000 ALTER TABLE `Employee` DISABLE KEYS */;
INSERT INTO `Employee` VALUES (30092,'e1','f1',2019),(32091,'e2','f2',2022);
/*!40000 ALTER TABLE `Employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Person`
--

DROP TABLE IF EXISTS `Person`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Person` (
  `ID` int NOT NULL,
  `Firstname` varchar(255) DEFAULT NULL,
  `Lastname` varchar(255) DEFAULT NULL,
  `Address` varchar(255) DEFAULT NULL,
  `Phone_number` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Person`
--

LOCK TABLES `Person` WRITE;
/*!40000 ALTER TABLE `Person` DISABLE KEYS */;
INSERT INTO `Person` VALUES (324,'Azita','Mokhtari','hghjkjk','09878676'),(1121,'zahra','Khameieeeeeee','kasnvdsknk','93874922'),(35203,'ALi','vreve','qwew','23532'),(324555,'jnwd','SLFSD','oksmd DS','92842'),(923423,'sname4','family4','cit82,street16','9989878676'),(993466,'sname1','famil14','cit27,street196','7865643'),(3243533,'jnwd','SLFSD','oksmd DS','92842');
/*!40000 ALTER TABLE `Person` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reserve`
--

DROP TABLE IF EXISTS `reserve`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reserve` (
  `ID` int DEFAULT NULL,
  `ISBN` int DEFAULT NULL,
  `reserve_date` int DEFAULT NULL,
  `expire_date` int DEFAULT NULL,
  KEY `ID` (`ID`),
  KEY `ISBN` (`ISBN`),
  CONSTRAINT `reserve_ibfk_1` FOREIGN KEY (`ID`) REFERENCES `Person` (`ID`),
  CONSTRAINT `reserve_ibfk_2` FOREIGN KEY (`ISBN`) REFERENCES `Book` (`ISBN`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reserve`
--

LOCK TABLES `reserve` WRITE;
/*!40000 ALTER TABLE `reserve` DISABLE KEYS */;
INSERT INTO `reserve` VALUES (324,171,NULL,NULL);
/*!40000 ALTER TABLE `reserve` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-01-08 17:14:56
