/*
 Navicat MySQL Data Transfer

 Source Server         : python_db
 Source Server Type    : MySQL
 Source Server Version : 50641
 Source Host           : 101.132.109.255:3306
 Source Schema         : eduSys

 Target Server Type    : MySQL
 Target Server Version : 50641
 File Encoding         : 65001

 Date: 11/03/2019 17:58:03
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for classes
-- ----------------------------
DROP TABLE IF EXISTS `classes`;
CREATE TABLE `classes` (
  `id` int(5) NOT NULL AUTO_INCREMENT,
  `class_name` varchar(255) NOT NULL,
  `class_code` varchar(255) NOT NULL,
  `school_code` varchar(255) NOT NULL,
  `addr` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for lesson
-- ----------------------------
DROP TABLE IF EXISTS `lesson`;
CREATE TABLE `lesson` (
  `id` int(5) NOT NULL AUTO_INCREMENT,
  `teacher_code` varchar(255) NOT NULL,
  `school_code` varchar(255) NOT NULL,
  `subject_code` varchar(255) DEFAULT NULL,
  `class_code` varchar(255) DEFAULT NULL,
  `student_code` varchar(255) DEFAULT NULL,
  `score` int(8) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for school
-- ----------------------------
DROP TABLE IF EXISTS `school`;
CREATE TABLE `school` (
  `id` int(5) NOT NULL AUTO_INCREMENT,
  `school_name` varchar(255) NOT NULL,
  `school_code` varchar(255) NOT NULL,
  `school_addr` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of school
-- ----------------------------
BEGIN;
INSERT INTO `school` VALUES (1, '清华大学', '003', '北京');
INSERT INTO `school` VALUES (2, '浙江大学', '004', '杭州');
INSERT INTO `school` VALUES (3, '大红鹰学院', '009', '宁波');
INSERT INTO `school` VALUES (4, '测试大学', '009', '测试地址');
INSERT INTO `school` VALUES (5, '测试大学', '009', '测试地址');
INSERT INTO `school` VALUES (6, '我的大学', '110', '我的大学地址');
COMMIT;

-- ----------------------------
-- Table structure for student
-- ----------------------------
DROP TABLE IF EXISTS `student`;
CREATE TABLE `student` (
  `id` int(5) NOT NULL AUTO_INCREMENT,
  `student_code` varchar(255) NOT NULL,
  `class_code` varchar(255) NOT NULL,
  `school_code` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `sex` varchar(8) NOT NULL,
  `age` int(4) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for subject
-- ----------------------------
DROP TABLE IF EXISTS `subject`;
CREATE TABLE `subject` (
  `id` int(5) NOT NULL AUTO_INCREMENT,
  `subject_code` varchar(255) NOT NULL,
  `subject_name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for teacher
-- ----------------------------
DROP TABLE IF EXISTS `teacher`;
CREATE TABLE `teacher` (
  `id` int(5) NOT NULL AUTO_INCREMENT,
  `teacher_code` varchar(255) NOT NULL,
  `school_code` varchar(255) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

SET FOREIGN_KEY_CHECKS = 1;
