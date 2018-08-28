-- MySQL dump 10.13  Distrib 5.7.22, for Linux (x86_64)
--
-- Host: localhost    Database: college
-- ------------------------------------------------------
-- Server version	5.7.22-0ubuntu0.16.04.1

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
-- Table structure for table `clazz`
--

DROP TABLE IF EXISTS `clazz`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `clazz` (
  `clazz_number` varchar(8) NOT NULL,
  `clazz_name` varchar(50) NOT NULL,
  `clazz_major` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`clazz_number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clazz`
--

LOCK TABLES `clazz` WRITE;
/*!40000 ALTER TABLE `clazz` DISABLE KEYS */;
INSERT INTO `clazz` VALUES ('00001','sx201801','sx2018'),('00002','sx201802','sx2018'),('00003','dl201801','dl2018'),('00004','dl201901','dl2019'),('00005','jj201801','jj2018'),('00006','sh201701','sh2017'),('00007','sh201801','sh2018'),('00009','tw201801','tw2018');
/*!40000 ALTER TABLE `clazz` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `course`
--

DROP TABLE IF EXISTS `course`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `course` (
  `major_number` varchar(3) DEFAULT NULL,
  `course_number` varchar(3) NOT NULL,
  `course_name` varchar(50) NOT NULL,
  PRIMARY KEY (`course_number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `course`
--

LOCK TABLES `course` WRITE;
/*!40000 ALTER TABLE `course` DISABLE KEYS */;
/*!40000 ALTER TABLE `course` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `exam`
--

DROP TABLE IF EXISTS `exam`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `exam` (
  `ID` tinyint(4) NOT NULL AUTO_INCREMENT,
  `term` varchar(20) NOT NULL,
  `major_number` varchar(50) NOT NULL,
  `class_number` varchar(50) NOT NULL,
  `course_name` varchar(30) NOT NULL,
  `exam_place` varchar(20) NOT NULL,
  `exam_day` varchar(20) NOT NULL,
  `exam_time` varchar(50) NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `class_number` (`class_number`),
  KEY `major_number` (`major_number`),
  KEY `course_name` (`course_name`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `exam`
--

LOCK TABLES `exam` WRITE;
/*!40000 ALTER TABLE `exam` DISABLE KEYS */;
INSERT INTO `exam` VALUES (1,'高等数学期末考试','sx2018','sx201801','高等数学','1','2018-08-02','考试时间为9:00-11:30'),(2,'数据结构期末考试','sx2018','sx201802','数据结构','1','2018-08-15','考试时间为9:00-10:30'),(3,'地理科学进展','dl2018','dl201801','地理科学进展','1','2018-08-15','考试时间为14:30-16:30'),(4,'色度学期末考试','dl2019','dl201901','色度学','1','2018-08-14','考试时间为14:30-16:30'),(5,'会计学期末考试','jj2018','jj201801','会计学','1','2018-08-14','考试时间为9:00-11:00'),(6,'经济社会学期末考试','sh2017','sh201701','经济社会学','1','2018-08-16','考试时间为9:00-11:30'),(7,'人类学导论期末考试','sh2018','sh201801','人类学导论','1','2018-08-20','考试时间为14:00-16:30');
/*!40000 ALTER TABLE `exam` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `major`
--

DROP TABLE IF EXISTS `major`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `major` (
  `major_number` varchar(3) NOT NULL,
  `major_name` varchar(50) NOT NULL,
  PRIMARY KEY (`major_number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `major`
--

LOCK TABLES `major` WRITE;
/*!40000 ALTER TABLE `major` DISABLE KEYS */;
INSERT INTO `major` VALUES ('001','sx2018'),('002','dl2018'),('003','dl2019'),('004','jj2018'),('005','sh2017'),('006','sh2018'),('007','tw2018');
/*!40000 ALTER TABLE `major` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `major_course`
--

DROP TABLE IF EXISTS `major_course`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `major_course` (
  `ID` tinyint(4) NOT NULL AUTO_INCREMENT,
  `major_number` varchar(20) DEFAULT NULL,
  `course_number` varchar(50) DEFAULT NULL,
  `class_number` varchar(20) NOT NULL,
  `tea_number` varchar(10) DEFAULT NULL,
  `course_place` varchar(20) NOT NULL,
  `course_day` varchar(20) NOT NULL,
  `course_time` varchar(50) NOT NULL,
  `course_week` varchar(10) NOT NULL,
  `course_date` varchar(50) NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `major_number` (`major_number`),
  KEY `class_number` (`class_number`),
  KEY `tea_number` (`tea_number`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `major_course`
--

LOCK TABLES `major_course` WRITE;
/*!40000 ALTER TABLE `major_course` DISABLE KEYS */;
INSERT INTO `major_course` VALUES (1,'sx2018','高等数学','sx201801','待定','课室1','07/03/2018','9.00','星期二','6'),(2,'sx2018','几何学','sx201801','待定','课室1','07/04/2018','10.30','星期三','8'),(3,'sx2018','实变函数','sx201802','待定','课室1','07/04/2018','9.30','星期三','8'),(4,'sx2018','数据结构','sx201802','待定','课室2','07/11/2018','9.30','星期三','6'),(5,'sx2018','解析数论','sx201802','待定','课室2','07/11/2018','11.00','星期三','9'),(6,'dl2018','地理科学进展','dl201801','待定','课室4','07/10/2018','9.00','星期二','7'),(7,'dl2018','遥感应用','dl201801','待定','课室5','07/12/2018','9.00','星期四','6'),(8,'dl2018','地图学','dl201801','待定','课室5','07/12/2018','11.00','星期四','5'),(10,'dl2019','地球灾害','dl201901','待定','课室3','07/04/2018','11.00','星期三','8'),(11,'jj2018','会计学','jj201801','待定','课室4','07/06/2018','9.00','星期五','8'),(12,'jj2018','美国经济','jj201801','待定','课室4','07/06/2018','11.00','星期五','6'),(13,'jj2018','审计学','jj201801','待定','课室3','07/16/2018','9.00','星期一','6'),(14,'jj2018','行为经济学','jj201801','待定','课室2','07/18/2018','9.00','星期三','7'),(15,'jj2018','公司财务','jj201801','待定','课室2','07/18/2018','11.00','星期三','7'),(16,'sh2017','中国社会','sh201701','待定','课室6','07/17/2018','9.00','星期二','4'),(17,'sh2017','经济社会学','sh201701','待定','课室6','07/17/2018','19.00','星期二','8'),(18,'sh2017','家庭社会学','sh201701','待定','课室6','07/17/2018','11.00','星期二','6'),(19,'sh2017','社会性别研究','sh201701','待定','课室5','07/18/2018','19.00','星期三','9'),(20,'sh2018','人类学导论','sh201801','待定','课室8','07/12/2018','9.00','星期四','15'),(21,'sx2018','高等数学2','sx201802','待定','课室3','07/12/2018','9:00','星期四','8'),(22,'sh2018','人类进化学','sh201801','待定','课室7','07/12/2018','9:00','星期四','9');
/*!40000 ALTER TABLE `major_course` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `notice`
--

DROP TABLE IF EXISTS `notice`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `notice` (
  `schoolname` varchar(50) DEFAULT NULL,
  `teacherBulletin` text,
  `studentBulletin` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `notice`
--

LOCK TABLES `notice` WRITE;
/*!40000 ALTER TABLE `notice` DISABLE KEYS */;
INSERT INTO `notice` VALUES ('达内','明天不上课','五月天8.10在本校操场进行室外演唱会，要报名临时工的同学前往青志队报名！ ');
/*!40000 ALTER TABLE `notice` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `score`
--

DROP TABLE IF EXISTS `score`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `score` (
  `ID` tinyint(4) NOT NULL AUTO_INCREMENT,
  `term` varchar(10) NOT NULL,
  `major_number` varchar(10) NOT NULL,
  `class_number` varchar(20) NOT NULL,
  `stu_number` varchar(20) NOT NULL,
  `course_number` varchar(10) NOT NULL,
  `score` tinyint(4) NOT NULL,
  `major_name` varchar(50) NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `major_number` (`major_number`),
  KEY `class_number` (`class_number`),
  KEY `stu_number` (`stu_number`)
) ENGINE=InnoDB AUTO_INCREMENT=44 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `score`
--

LOCK TABLES `score` WRITE;
/*!40000 ALTER TABLE `score` DISABLE KEYS */;
INSERT INTO `score` VALUES (4,'张雨绮','1','sx201801','sx20180101','高等数学',95,'sx2018'),(5,'金汉文','1','sx201801','sx20180102','高等数学',100,'sx2018'),(6,'吕剑人','1','sx201801','sx20180103','高等数学',85,'sx2018'),(7,'张静初','1','sx201801','sx20180104','高等数学',76,'sx2018'),(8,'朱开轩','1','sx201801','sx20180105','高等数学',88,'sx2018'),(9,'苏婴','4','sx201802','sx20180201','数据结构',89,'sx2018'),(10,'秦观','4','sx201802','sx20180202','数据结构',84,'sx2018'),(11,'朱远利','4','sx201802','sx20180203','数据结构',96,'sx2018'),(12,'张也','4','sx201802','sx20180204','数据结构',94,'sx2018'),(13,'水新元','4','sx201802','sx20180205','数据结构',83,'sx2018'),(14,'金星','6','dl201801','dl20180101','地理科学进展',95,'dl2018'),(15,'秦仁昌','6','dl201801','dl20180102','地理科学进展',88,'dl2018'),(16,'张太展','6','dl201801','dl20180103','地理科学进展',80,'dl2018'),(17,'金波','6','dl201801','dl20180104','地理科学进展',79,'dl2018'),(18,'吕应中','6','dl201801','dl20180105','地理科学进展',90,'dl2018'),(19,'秦淮书','9','dl201901','dl20190101','色度学',100,'dl2019'),(20,'张永珍','9','dl201901','dl20190102','色度学',95,'dl2019'),(21,'云保英','9','dl201901','dl20190103','色度学',88,'dl2019'),(22,'秦玉琴','9','dl201901','dl20190104','色度学',97,'dl2019'),(23,'朱昌权','9','dl201901','dl20190105','色度学',87,'dl2019'),(24,'金润宇','11','jj201801','jj20180101','会计学',99,'jj2018'),(25,'水天一','11','jj201801','jj20180102','会计学',85,'jj2018'),(26,'姜鉴','11','jj201801','jj20180103','会计学',77,'jj2018'),(27,'张鲁大','11','jj201801','jj20180104','会计学',92,'jj2018'),(28,'曲春妍','11','jj201801','jj20180105','会计学',90,'jj2018'),(29,'朱乃正','11','jj201801','jj20180106','会计学',80,'jj2018'),(30,'胡定欣','11','jj201801','jj20180107','会计学',86,'jj2018'),(31,'曲长钢','11','jj201801','jj20180108','会计学',79,'jj2018'),(32,'云广英','11','jj201801','jj20180109','会计学',84,'jj2018'),(33,'宫新勇','11','jj201801','jj20180110','会计学',90,'jj2018'),(34,'吕飞','17','sh201701','sh20170101','经济社会学',95,'sh2017'),(35,'钱贵','17','sh201701','sh20170102','经济社会学',94,'sh2017'),(36,'王时悦','17','sh201701','sh20170103','经济社会学',90,'sh2017'),(37,'丁涟云','17','sh201701','sh20170104','经济社会学',80,'sh2017'),(38,'曲小路','17','sh201701','sh20170105','经济社会学',99,'sh2017'),(39,'苏文举','20','sh201801','sh20180101','人类学导论',99,'sh2018'),(40,'水金土','20','sh201801','sh20180102','人类学导论',79,'sh2018'),(41,'丁雪锋','20','sh201801','sh20180103','人类学导论',85,'sh2018'),(42,'王进喜','20','sh201801','sh20180104','人类学导论',80,'sh2018'),(43,'房光斗','20','sh201801','sh20180105','人类学导论',86,'sh2018');
/*!40000 ALTER TABLE `score` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `student` (
  `stu_number` varchar(20) DEFAULT NULL,
  `name` varchar(20) DEFAULT NULL,
  `gender` char(1) NOT NULL,
  `major_number` varchar(3) NOT NULL,
  `class_number` varchar(20) NOT NULL,
  `instructor` varchar(10) DEFAULT NULL,
  `phone` varchar(20) DEFAULT NULL,
  `QQ` varchar(20) DEFAULT NULL,
  KEY `major_number` (`major_number`),
  KEY `class_number` (`class_number`),
  KEY `instructor` (`instructor`),
  KEY `stu_number` (`stu_number`),
  KEY `name` (`name`),
  CONSTRAINT `student_ibfk_1` FOREIGN KEY (`stu_number`) REFERENCES `user` (`user_number`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `student_ibfk_2` FOREIGN KEY (`name`) REFERENCES `user` (`name`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` VALUES ('dl20180101','金星','1','002','dl201801','Null','',''),('sx20180101','张雨绮','1','001','sx201801','Null','','6857861'),('sx20180102','金汉文','0','001','sx201801','Null','15987123475','9815615'),('sx20180103','吕剑人','1','001','sx201801','Null','15987412494','1654987'),('sx20180104','张静初','1','001','sx201801','Null','13598745614','66511234'),('sx20180105','朱开轩','0','001','sx201801','Null','15789516535','15678999'),('sx20180201','苏婴','1','001','sx201802','Null','19994564647','9845647'),('sx20180202','秦观','0','001','sx201802','Null','14879641654','885123456'),('sx20180203','朱远利','0','001','sx201802','Null','13549687156','8745163'),('sx20180204','张也','0','001','sx201802','Null','13598794116','548975165'),('sx20180205','水新元','0','001','sx201802','Null','14567894161','66549871'),('dl20180102','秦仁昌','0','002','dl201801','Null','13549687144',''),('dl20180103','张太展','0','002','dl201801','Null','15667895121',''),('dl20180104','金波','0','002','dl201801','Null','','489798416'),('dl20180105','吕应中','1','002','dl201801','Null','','65789798'),('dl20190101','秦淮书','0','003','dl201901','Null','13459789156','56798213'),('dl20190102','张永珍','1','003','dl201901','Null','','597981'),('dl20190103','云保英','1','003','dl201901','Null','13579845744','1897981'),('dl20190104','秦玉琴','1','003','dl201901','Null','15789515647','1564987'),('dl20190105','朱昌权','0','003','dl201901','Null','19515648741','81521320'),('jj20180101','金润宇','0','004','jj201801','Null','',''),('jj20180102','水天一','0','004','jj201801','Null','13546857981','89210'),('jj20180103','姜鉴','0','004','jj201801','Null','15784615647','5648979'),('jj20180104','张鲁大','0','004','jj201801','Null','15487156448','99515640'),('jj20180105','曲春妍','1','004','jj201801','Null','14892023465','22654877'),('jj20180106','朱乃正','0','004','jj201801','Null','15674894161','1115678941'),('jj20180107','胡定欣','0','004','jj201801','Null','13546874136','8851564654'),('jj20180108','曲长钢','0','004','jj201801','Null','15489751102','20056789'),('jj20180109','云广英','1','004','jj201801','Null','13549874654','98751651'),('jj20180110','宫新勇','0','004','jj201801','Null','','5945161'),('sh20170101','吕飞','0','005','sh201701','Null','','981203'),('sh20170102','钱贵','0','005','sh201701','Null','13235479871','3257132'),('sh20170103','王时悦','0','005','sh201701','Null','13574971564',''),('sh20170104','丁涟云','0','005','sh201701','Null','','12341212'),('sh20170105','曲小路','1','005','sh201701','Null','','1859871001'),('sh20180101','苏文举','0','006','sh201801','Null','13578971454','564897'),('sh20180102','水金土','0','006','sh201801','Null','13579871154','1657987'),('sh20180103','丁雪锋','0','006','sh201801','Null','15798452164','90324657'),('sh20180104','王进喜','0','006','sh201801','Null','','910548484'),('sh20180105','房光斗','0','006','sh201801','Null','15798135471','156791521');
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `teacher`
--

DROP TABLE IF EXISTS `teacher`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `teacher` (
  `tea_number` varchar(20) DEFAULT NULL,
  `name` varchar(20) DEFAULT NULL,
  `gender` char(1) NOT NULL,
  `data_birth` varchar(20) NOT NULL,
  `major_number` varchar(20) DEFAULT NULL,
  `phone` varchar(20) DEFAULT NULL,
  `QQ` varchar(20) DEFAULT NULL,
  KEY `major_number` (`major_number`),
  KEY `tea_number` (`tea_number`),
  KEY `name` (`name`),
  CONSTRAINT `teacher_ibfk_1` FOREIGN KEY (`tea_number`) REFERENCES `user` (`user_number`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `teacher_ibfk_2` FOREIGN KEY (`name`) REFERENCES `user` (`name`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teacher`
--

LOCK TABLES `teacher` WRITE;
/*!40000 ALTER TABLE `teacher` DISABLE KEYS */;
INSERT INTO `teacher` VALUES ('zhangheng','张衡','男','07/02/1996','Null','13597894168','6546565'),('zuchongzhi','祖冲之','男','07/05/1888','Null','',''),('zouboqi','邹伯奇','女','02/06/2006','Null','13800138000','654657'),('xuguanqi','徐光启','男','07/05/2000','Null','15874541234','234567'),('qinjiushao','秦九韶','男','07/03/1850','Null','19511549810',''),('lidaoyuan','郦道元','男','07/18/1888','Null','15800244456',''),('shenkuo','沈括','女','07/05/2000','Null','','5645612'),('gelunbu','哥伦布','男','01/25/1855','Null','15023156487',''),('zhangxiangwen','张相文','男','02/07/1995','Null','',''),('wangfang','王凡','女','07/09/1985','Null','','1893453'),('linyifu','林毅夫','男','02/09/2000','Null','',''),('zhangweiying','张维迎','男','07/05/1989','Null','15850214564','98456164'),('langxianping','郎咸平','男','02/25/1998','Null','',''),('zhangwuchang','张五常','女','03/05/1890','Null','15647821654','156789'),('tianguoqiang','田国强','男','02/05/1985','Null','','64567498'),('makesi','马克思','男','07/16/1890','Null','',''),('liyinhe','李银河','女','06/30/1993','Null','',''),('feixiaotong','费孝通','男','06/25/2018','Null','15156415647',''),('bolatu','柏拉图','男','07/03/2018','Null','15987123456','1564798'),('zhanmusi','詹姆斯','女','02/07/1984','Null','15687516347','55949899');
/*!40000 ALTER TABLE `teacher` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `user_number` varchar(20) NOT NULL,
  `name` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL DEFAULT '000000',
  `type` char(1) NOT NULL,
  `isActive` varchar(1) DEFAULT '1',
  PRIMARY KEY (`user_number`),
  KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES ('00001','具良鑫','111111','2','1'),('00002','徐海龙','222222','2','1'),('00003','罗仕龙','333333','2','1'),('00004','陈舒升','444444','2','1'),('00005','徐剑杰','555555','2','1'),('20180000','superadmin','abcdef','2','1'),('bolatu','柏拉图','000000','1','1'),('dl20180101','金星','000000','0','1'),('dl20180102','秦仁昌','000000','0','1'),('dl20180103','张太展','000000','0','1'),('dl20180104','金波','000000','0','1'),('dl20180105','吕应中','000000','0','1'),('dl20190101','秦淮书','000000','0','1'),('dl20190102','张永珍','000000','0','1'),('dl20190103','云保英','000000','0','1'),('dl20190104','秦玉琴','000000','0','1'),('dl20190105','朱昌权','000000','0','1'),('feixiaotong','费孝通','000000','1','1'),('gelunbu','哥伦布','000000','1','1'),('jj20180101','金润宇','000000','0','1'),('jj20180102','水天一','000000','0','1'),('jj20180103','姜鉴','000000','0','1'),('jj20180104','张鲁大','000000','0','1'),('jj20180105','曲春妍','000000','0','1'),('jj20180106','朱乃正','000000','0','1'),('jj20180107','胡定欣','000000','0','1'),('jj20180108','曲长钢','000000','0','1'),('jj20180109','云广英','000000','0','1'),('jj20180110','宫新勇','000000','0','1'),('langxianping','郎咸平','000000','1','1'),('lidaoyuan','郦道元','000000','1','1'),('linyifu','林毅夫','000000','1','1'),('liyinhe','李银河','000000','1','1'),('makesi','马克思','000000','1','1'),('qinjiushao','秦九韶','000000','1','1'),('sh20170101','吕飞','000000','0','1'),('sh20170102','钱贵','000000','0','1'),('sh20170103','王时悦','000000','0','1'),('sh20170104','丁涟云','000000','0','1'),('sh20170105','曲小路','000000','0','1'),('sh20180101','苏文举','111111','0','1'),('sh20180102','水金土','000000','0','1'),('sh20180103','丁雪锋','000000','0','1'),('sh20180104','王进喜','000000','0','1'),('sh20180105','房光斗','000000','0','1'),('shenkuo','沈括','000000','1','1'),('sx20180101','张雨绮','000000','0','1'),('sx20180102','金汉文','000000','0','1'),('sx20180103','吕剑人','000000','0','1'),('sx20180104','张静初','000000','0','1'),('sx20180105','朱开轩','000000','0','1'),('sx20180201','苏婴','000000','0','1'),('sx20180202','秦观','000000','0','1'),('sx20180203','朱远利','000000','0','1'),('sx20180204','张也','000000','0','1'),('sx20180205','水新元','000000','0','1'),('tianguoqiang','田国强','000000','1','1'),('wangfang','王凡','000000','1','1'),('xuguanqi','徐光启','000000','1','1'),('zhangheng','张衡','000000','1','1'),('zhangweiying','张维迎','000000','1','1'),('zhangwuchang','张五常','000000','1','1'),('zhangxiangwen','张相文','000000','1','1'),('zhanmusi','詹姆斯','000000','1','1'),('zouboqi','邹伯奇','000000','1','1'),('zuchongzhi','祖冲之','000000','1','1');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-07-29 20:55:51
