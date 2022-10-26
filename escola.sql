CREATE DATABASE  IF NOT EXISTS `escola` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `escola`;
-- MySQL dump 10.13  Distrib 8.0.30, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: escola
-- ------------------------------------------------------
-- Server version	8.0.30

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `aluno`
--

DROP TABLE IF EXISTS `aluno`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `aluno` (
  `id_aluno` int NOT NULL AUTO_INCREMENT,
  `nome_aluno` varchar(45) NOT NULL,
  `cpf_aluno` varchar(11) NOT NULL,
  `nome_responsavel_aluno` varchar(144) NOT NULL,
  `cpf_responsavel_aluno` varchar(11) NOT NULL,
  PRIMARY KEY (`id_aluno`),
  UNIQUE KEY `cpf_aluno_UNIQUE` (`cpf_aluno`),
  UNIQUE KEY `cpf_responsavel_aluno_UNIQUE` (`cpf_responsavel_aluno`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `aluno`
--

LOCK TABLES `aluno` WRITE;
/*!40000 ALTER TABLE `aluno` DISABLE KEYS */;
INSERT INTO `aluno` VALUES (17,'rafael','22875433091','roger','22875433591'),(18,'renan','28875433091','cadu','22875663091'),(19,'fabio','22875466691','paulo','22875433097'),(20,'tulio','12345678912','del','12345678913'),(21,'ricardinho','14725836978','marcelo catatau','15935875360');
/*!40000 ALTER TABLE `aluno` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `avaliacoes`
--

DROP TABLE IF EXISTS `avaliacoes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `avaliacoes` (
  `id_avaliacoes` int NOT NULL AUTO_INCREMENT,
  `nome_aluno` varchar(45) NOT NULL,
  `disciplina` varchar(45) NOT NULL,
  `tipo_avaliacao` varchar(45) NOT NULL,
  `nota` int NOT NULL,
  `cpf_aluno` varchar(45) NOT NULL,
  PRIMARY KEY (`id_avaliacoes`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `avaliacoes`
--

LOCK TABLES `avaliacoes` WRITE;
/*!40000 ALTER TABLE `avaliacoes` DISABLE KEYS */;
INSERT INTO `avaliacoes` VALUES (12,'((\'fabio\',),)','((\'portugues\',),)','prova',10,'((\'22875466691\',),)'),(13,'((\'fabio\',),)','((\'portugues\',),)','trabalho',6,'((\'22875466691\',),)'),(14,'((\'rafael\',),)','((\'portugues\',),)','prova',10,'((\'22875433091\',),)'),(15,'(\'renan\',)','((\'portugues\',),)','trabalho',2,'((\'28875433091\',),)'),(16,'(\'fabio\',)','((\'portugues\',),)','teste',10,'((\'22875466691\',),)'),(17,'tulio','portugues','teste',10,'12345678912'),(18,'ricardinho','((\'ingles\',),)','prova',10,'14725836978'),(19,'ricardinho','portugues','prova',20,'14725836978');
/*!40000 ALTER TABLE `avaliacoes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `professor`
--

DROP TABLE IF EXISTS `professor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `professor` (
  `idprofessor` int NOT NULL AUTO_INCREMENT,
  `nome_professor` varchar(45) NOT NULL,
  `senha_professor` varchar(45) NOT NULL,
  `disciplina` varchar(45) NOT NULL,
  `recados_professor` varchar(144) DEFAULT NULL,
  PRIMARY KEY (`idprofessor`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `professor`
--

LOCK TABLES `professor` WRITE;
/*!40000 ALTER TABLE `professor` DISABLE KEYS */;
INSERT INTO `professor` VALUES (1,'revoredo','123','portugues',NULL),(2,'carlo','321','matematica',NULL),(3,'marcelo','147','historia',NULL),(4,'luiz','258','filosofia',NULL),(5,'inacio','369','sociologia',NULL),(6,'simone','456','geografia',NULL),(7,'marilia','789','fisica',NULL),(8,'raquel','159','quimica',NULL),(9,'obama','777','ingles',NULL);
/*!40000 ALTER TABLE `professor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `recado`
--

DROP TABLE IF EXISTS `recado`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `recado` (
  `idrecado` int NOT NULL AUTO_INCREMENT,
  `nome_aluno` varchar(45) NOT NULL,
  `nome_professor` varchar(45) NOT NULL,
  `titulo_recado` varchar(45) NOT NULL,
  `recado` varchar(144) NOT NULL,
  `cpf_receptor` varchar(45) NOT NULL,
  PRIMARY KEY (`idrecado`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recado`
--

LOCK TABLES `recado` WRITE;
/*!40000 ALTER TABLE `recado` DISABLE KEYS */;
INSERT INTO `recado` VALUES (1,'((\'tulio\',),)','diretor','teste5','esse teste5','((\'12345678912\',),)');
/*!40000 ALTER TABLE `recado` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `responsavel`
--

DROP TABLE IF EXISTS `responsavel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `responsavel` (
  `idresponsavel` int NOT NULL AUTO_INCREMENT,
  `nome_responsavel` varchar(45) NOT NULL,
  `cpf_responsavel` varchar(11) NOT NULL,
  `aluno_responsavel` varchar(45) NOT NULL,
  `recado` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idresponsavel`),
  UNIQUE KEY `senha_responsavel_UNIQUE` (`cpf_responsavel`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `responsavel`
--

LOCK TABLES `responsavel` WRITE;
/*!40000 ALTER TABLE `responsavel` DISABLE KEYS */;
INSERT INTO `responsavel` VALUES (6,'roger','22875433591','rafael',NULL),(7,'cadu','22875663091','renan',NULL),(8,'paulo','22875433097','fabio',NULL),(9,'del','12345678913','tulio',NULL),(10,'marcelo catatau','15935875360','ricardinho',NULL);
/*!40000 ALTER TABLE `responsavel` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-10-26  0:50:49
