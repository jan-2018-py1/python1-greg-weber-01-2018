CREATE DATABASE  IF NOT EXISTS `the_wall` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `the_wall`;
-- MySQL dump 10.13  Distrib 5.7.17, for macos10.12 (x86_64)
--
-- Host: localhost    Database: the_wall
-- ------------------------------------------------------
-- Server version	5.7.21

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `comments`
--

DROP TABLE IF EXISTS `comments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `comments` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `post_id` int(11) NOT NULL,
  `comment` text NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_comments_users1_idx` (`user_id`),
  KEY `fk_comments_posts1_idx` (`post_id`),
  CONSTRAINT `fk_comments_posts1` FOREIGN KEY (`post_id`) REFERENCES `posts` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_comments_users1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comments`
--

LOCK TABLES `comments` WRITE;
/*!40000 ALTER TABLE `comments` DISABLE KEYS */;
INSERT INTO `comments` VALUES (3,1,5,'Cool! This is my first comment!!!','2018-02-02 19:48:49','2018-02-02 19:48:49'),(5,1,2,'Nice Tanner!! COMMENT COMMENT  COMMENT COMMENT COMMENT COMMENT COMMENT COMMENT COMMENT COMMENT COMMENT COMMENT COMMENT COMMENT COMMENT COMMENT COMMENT COMMENT','2018-02-02 19:49:35','2018-02-02 19:49:35'),(6,2,2,'hey man right back at you! hey man right back at you! hey man right back at you! hey man right back at you! hey man right back at you! hey man right back at you! hey man right back at you! ','2018-02-02 19:51:46','2018-02-02 19:51:46'),(8,2,6,'hahah it all good hahah it all good hahah it all good hahah it all good hahah it all good hahah it all good hahah it all good hahah it all good hahah it all good hahah it all good hahah it all good hahah it all good hahah it all good hahah it all good hahah it all good !','2018-02-02 19:53:19','2018-02-02 19:53:19'),(9,2,5,'What up Johnny?!?!?! Glad you\'re stoked Glad you\'re stoked Glad you\'re stoked Glad you\'re stoked Glad you\'re stoked Glad you\'re stoked Glad you\'re stoked !!!!','2018-02-02 19:54:14','2018-02-02 19:54:14'),(10,1,5,'I\'m gonna leave another comment as a test this should be the third comment on Johnny\'s post by me - user Greg','2018-02-02 21:46:11','2018-02-02 21:46:11'),(11,1,2,'yeeeeeeeehaaaaaa!!!!!! yeeeeeeeehaaaaaa!!!!!! yeeeeeeeehaaaaaa!!!!!! yeeeeeeeehaaaaaa!!!!!! yeeeeeeeehaaaaaa!!!!!! yeeeeeeeehaaaaaa!!!!!! yeeeeeeeehaaaaaa!!!!!! yeeeeeeeehaaaaaa!!!!!! yeeeeeeeehaaaaaa!!!!!! yeeeeeeeehaaaaaa!!!!!! yeeeeeeeehaaaaaa!!!!!! yeeeeeeeehaaaaaa!!!!!! yeeeeeeeehaaaaaa!!!!!! yeeeeeeeehaaaaaa!!!!!! yeeeeeeeehaaaaaa!!!!!! yeeeeeeeehaaaaaa!!!!!! ','2018-02-02 22:11:53','2018-02-02 22:11:53'),(12,1,7,'opppssssyyyy I hit post before I wrote anything - better figure the delete part out now....','2018-02-02 22:13:26','2018-02-02 22:13:26'),(13,3,7,'way to go!! way to go!! way to go!! way to go!! way to go!! way to go!! way to go!! way to go!! way to go!! way to go!! way to go!! way to go!! way to go!! way to go!! way to go!! way to go!! way to go!! way to go!! way to go!! way to go!! way to go!! way to go!! way to go!! way to go!! way to go!! way to go!! way to go!! way to go!! way to go!! way to go!! way to go!! ','2018-02-02 22:19:57','2018-02-02 22:19:57'),(14,3,5,'get over it Johnny! hahaha!! get over it Johnny! hahaha!! get over it Johnny! hahaha!! get over it Johnny! hahaha!! get over it Johnny! hahaha!! get over it Johnny! hahaha!! get over it Johnny! hahaha!! get over it Johnny! hahaha!! get over it Johnny! hahaha!! get over it Johnny! hahaha!! get over it Johnny! hahaha!! get over it Johnny! hahaha!! get over it Johnny! hahaha!! get over it Johnny! hahaha!! get over it Johnny! hahaha!! get over it Johnny! hahaha!! get over it Johnny! hahaha!! get over it Johnny! hahaha!! ','2018-02-02 22:21:00','2018-02-02 22:21:00'),(15,6,7,'bummer!','2018-02-02 22:35:04','2018-02-02 22:35:04'),(16,6,5,'Yes!!!! Yes!!!! Yes!!!! Yes!!!! Yes!!!! Yes!!!! Yes!!!! Yes!!!! Yes!!!! Yes!!!! Yes!!!! Yes!!!! Yes!!!! Yes!!!! Yes!!!! Yes!!!! Yes!!!! Yes!!!! Yes!!!! Yes!!!! Yes!!!! Yes!!!! Yes!!!! Yes!!!! Yes!!!! Yes!!!! Yes!!!! Yes!!!! Yes!!!! Yes!!!! Yes!!!! Yes!!!! Yes!!!! Yes!!!! Yes!!!! Yes!!!! Yes!!!! Yes!!!! Yes!!!! Yes!!!! ','2018-02-02 22:35:41','2018-02-02 22:35:41'),(17,6,6,'','2018-02-02 22:36:07','2018-02-02 22:36:07'),(18,6,8,'','2018-02-02 22:36:13','2018-02-02 22:36:13'),(19,6,8,'','2018-02-02 22:36:15','2018-02-02 22:36:15'),(20,6,8,'','2018-02-02 22:36:16','2018-02-02 22:36:16'),(21,6,8,'empty words....','2018-02-02 22:36:27','2018-02-02 22:36:27'),(22,6,4,'numero tres!','2018-02-02 22:39:26','2018-02-02 22:39:26'),(23,6,8,'hahah - I fixed it so you cant leave an empty comment now - I will do the same for posts','2018-02-02 22:40:26','2018-02-02 22:40:26'),(24,1,3,'hi tanner!!','2018-02-02 22:45:27','2018-02-02 22:45:27'),(25,1,9,'maybe not though...','2018-02-02 22:52:07','2018-02-02 22:52:07');
/*!40000 ALTER TABLE `comments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `posts`
--

DROP TABLE IF EXISTS `posts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `posts` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `content` text NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_posts_users_idx` (`user_id`),
  CONSTRAINT `fk_posts_users` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `posts`
--

LOCK TABLES `posts` WRITE;
/*!40000 ALTER TABLE `posts` DISABLE KEYS */;
INSERT INTO `posts` VALUES (1,1,'Hey all this is my first post!  Hey all this is my first post!  Hey all this is my first post!  Hey all this is my first post!  Hey all this is my first post!  Hey all this is my first post!  Hey all this is my first post!  Hey all this is my first post!  Hey all this is my first post!  Hey all this is my first post!  Hey all this is my first post!  Hey all this is my first post!  Hey all this is my first post!  Hey all this is my first post!  Hey all this is my first post!  Hey all this is my first post!  Hey all this is my first post!  Hey all this is my first post!  ','2018-02-02 16:18:15','2018-02-02 16:18:15'),(2,2,'meee toooo!  Hey all this is my first post!  Hey all this is my first post!  Hey all this is my first post!  Hey all this is my first post!  Hey all this is my first post!  Hey all this is my first post!  Hey all this is my first post!  Hey all this is my first post!  Hey all this is my first post!  Hey all this is my first post!  ','2018-02-02 16:19:14','2018-02-02 16:19:14'),(3,2,'Ill post again for good measure!  Ill post again for good measure!Ill post again for good measure!Ill post again for good measure!Ill post again for good measure!Ill post again for good measure!Ill post again for good measure!Ill post again for good measure!Ill post again for good measure!Ill post again for good measure!Ill post again for good measure!Ill post again for good measure!Ill post again for good measure!Ill post again for good measure!Ill post again for good measure!Ill post again for good measure!Ill post again for good measure!','2018-02-02 16:19:45','2018-02-02 16:19:45'),(4,1,'this is going to be my 3rd post now.  this is going to be my 3rd post now.this is going to be my 3rd post now.this is going to be my 3rd post now.this is going to be my 3rd post now.this is going to be my 3rd post now.this is going to be my 3rd post now.this is going to be my 3rd post now.this is going to be my 3rd post now.','2018-02-02 17:04:44','2018-02-02 17:04:44'),(5,5,'Man this is cool! I\'m Johnny - what up y\'all!!','2018-02-02 17:12:06','2018-02-02 17:12:06'),(6,2,'arrggggg!!!!!!!!','2018-02-02 17:59:06','2018-02-02 17:59:06'),(7,1,'','2018-02-02 22:12:11','2018-02-02 22:12:11'),(8,6,'Whats up y\'ll - new here! 1\'s post Whats up y\'ll - new here! 1\'s post Whats up y\'ll - new here! 1\'s post Whats up y\'ll - new here! 1\'s post Whats up y\'ll - new here! 1\'s post Whats up y\'ll - new here! 1\'s post Whats up y\'ll - new here! 1\'s post Whats up y\'ll - new here! 1\'s post Whats up y\'ll - new here! 1\'s post Whats up y\'ll - new here! 1\'s post Whats up y\'ll - new here! 1\'s post Whats up y\'ll - new here! 1\'s post Whats up y\'ll - new here! 1\'s post Whats up y\'ll - new here! 1\'s post Whats up y\'ll - new here! 1\'s post Whats up y\'ll - new here! 1\'s post Whats up y\'ll - new here! 1\'s post ','2018-02-02 22:34:51','2018-02-02 22:34:51'),(9,1,'last post of the day....... last post of the day....... last post of the day....... last post of the day....... last post of the day....... last post of the day....... last post of the day....... last post of the day....... last post of the day....... last post of the day....... last post of the day....... last post of the day....... last post of the day....... last post of the day....... last post of the day....... last post of the day....... last post of the day....... last post of the day....... last post of the day....... last post of the day....... last post of the day....... last post of the day....... last post of the day.......  ','2018-02-02 22:51:56','2018-02-02 22:51:56');
/*!40000 ALTER TABLE `posts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Greg','Weber','gregoryweberguitars@gmail.com','1bbd886460827015e5d605ed44252251','2018-02-02 12:35:38','2018-02-02 12:35:38'),(2,'tanner','dog','t@dog.net','1bbd886460827015e5d605ed44252251','2018-02-02 12:37:51','2018-02-02 12:37:51'),(3,'Kay','Peterson','k@peterson.com','1bbd886460827015e5d605ed44252251','2018-02-02 13:38:46','2018-02-02 13:38:46'),(4,'Hailey','Lewis','h@lewis.com','1bbd886460827015e5d605ed44252251','2018-02-02 17:09:30','2018-02-02 17:09:30'),(5,'Johnny','Appleseed','j@apple.com','1bbd886460827015e5d605ed44252251','2018-02-02 17:11:28','2018-02-02 17:11:28'),(6,'Amber','Wilson','a@wilson.com','1bbd886460827015e5d605ed44252251','2018-02-02 22:34:14','2018-02-02 22:34:14');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-02-02 23:18:38
