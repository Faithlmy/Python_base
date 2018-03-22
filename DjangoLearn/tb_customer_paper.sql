/*
Navicat MySQL Data Transfer

Source Server         : 10.167.197.12
Source Server Version : 50621
Source Host           : 10.167.197.12:3306
Source Database       : st

Target Server Type    : MYSQL
Target Server Version : 50621
File Encoding         : 65001

Date: 2018-03-23 14:33:32
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for tb_customer_paper
-- ----------------------------
DROP TABLE IF EXISTS `tb_customer_paper`;
CREATE TABLE `tb_customer_paper` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `ECN_NO` varchar(255) DEFAULT NULL COMMENT 'ECN编号',
  `version` varchar(255) DEFAULT NULL COMMENT '图纸版次',
  `p_name` varchar(255) DEFAULT NULL COMMENT '图纸制定人',
  `ST_site` varchar(255) DEFAULT NULL COMMENT 'ST厂区',
  `drawing_type` varchar(255) DEFAULT NULL COMMENT '图纸类别',
  `definer_name` varchar(255) DEFAULT NULL COMMENT '图纸制定人',
  `c_name` varchar(255) DEFAULT NULL COMMENT '客户名称',
  `c_type` varchar(255) DEFAULT NULL COMMENT '客户类别',
  `c_site` varchar(255) DEFAULT NULL COMMENT '客户厂区',
  `uploader` varchar(255) DEFAULT NULL COMMENT '文件上传者',
  `custters_spec` varchar(255) DEFAULT NULL COMMENT '刀具规格',
  `case_name` varchar(255) DEFAULT NULL COMMENT '专案名称',
  `priority` int(11) DEFAULT NULL COMMENT '优先级',
  `alter_cause` text COMMENT '变更说明',
  `alter_front` text COMMENT '变更前说明',
  `alter_later` text COMMENT '变更后说明',
  `desc_file` text COMMENT '文件描述',
  `create_time` datetime DEFAULT NULL COMMENT '创建时间',
  `modify_time` datetime DEFAULT NULL COMMENT '修改时间',
  `upload_time` datetime DEFAULT NULL COMMENT '文件创建时间',
  `c_confirm` int(11) DEFAULT NULL COMMENT '0草稿，1已发行未签核，2签核完未分发，3已发完',
  `customer_info` int(11) DEFAULT NULL,
  `copy_id` int(11) DEFAULT NULL COMMENT '复制id',
  `drawingtype` int(11) DEFAULT NULL,
  `modify_draft` int(11) DEFAULT NULL,
  `valid` int(11) DEFAULT NULL COMMENT '0代表失效，1代表有效',
  `create_people` varchar(255) DEFAULT NULL,
  `current` int(11) DEFAULT '0' COMMENT '0失效，1有效',
  `enabled` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `customer_id` (`customer_info`),
  CONSTRAINT `tb_customer_paper_ibfk_1` FOREIGN KEY (`customer_info`) REFERENCES `tb_custom_info` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of tb_customer_paper
-- ----------------------------
INSERT INTO `tb_customer_paper` VALUES ('1', null, 'version', 'p_name', null, null, null, 'c_name', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `tb_customer_paper` VALUES ('2', null, 'version', 'p_name', null, null, null, 'c_name', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `tb_customer_paper` VALUES ('3', null, 'version', 'p_name', null, null, null, 'c_name', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `tb_customer_paper` VALUES ('4', null, 'version', 'p_name', null, null, null, 'c_name', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `tb_customer_paper` VALUES ('5', null, null, null, 'faithfaith', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, '22', null);
INSERT INTO `tb_customer_paper` VALUES ('6', 'ddd', null, null, 'dd', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, '11', null);
INSERT INTO `tb_customer_paper` VALUES ('7', 'fff', null, null, 'fff', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, '12', null);
INSERT INTO `tb_customer_paper` VALUES ('8', 'sss', null, null, 'ss', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, '11', null);
