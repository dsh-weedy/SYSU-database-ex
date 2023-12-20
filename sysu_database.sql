/*
 Navicat Premium Data Transfer

 Source Server         : MySql80
 Source Server Type    : MySQL
 Source Server Version : 80030
 Source Host           : localhost:3306
 Source Schema         : sysu_database

 Target Server Type    : MySQL
 Target Server Version : 80030
 File Encoding         : 65001

 Date: 20/12/2023 17:01:30
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for car
-- ----------------------------
DROP TABLE IF EXISTS `car`;
CREATE TABLE `car`  (
  `image` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `car_id` int NOT NULL,
  `price` int NOT NULL,
  `rent` int NOT NULL,
  `model` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `state` int NOT NULL,
  `description` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `deposit` int NULL DEFAULT NULL,
  PRIMARY KEY (`car_id`) USING BTREE,
  INDEX `dept_no_Btree`(`model` ASC) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of car
-- ----------------------------
INSERT INTO `car` VALUES ('./img/CarImage2.png', 2, 250000, 3500, ' ZR-125', 2, ' a sleek car for city driving', NULL);
INSERT INTO `car` VALUES ('./img/CarImage3.png', 3, 150000, 2000, ' A1-900', 2, ' a compact car for daily commute', NULL);
INSERT INTO `car` VALUES ('./img/CarImage4.png', 4, 300000, 4000, ' Q7-2000', 2, ' a luxury SUV for family trips', NULL);
INSERT INTO `car` VALUES ('./img/CarImage5.png', 5, 200000, 3000, ' Civic-X', 2, ' a sporty car for dynamic driving', NULL);
INSERT INTO `car` VALUES ('./img/CarImage6.png', 6, 280000, 3800, ' Model3-E', 2, ' an electric car for eco-friendly driving', NULL);
INSERT INTO `car` VALUES ('./img/CarImage7.png', 7, 220000, 3200, ' Mustang-GT', 2, ' a classic car for a thrilling experience', NULL);
INSERT INTO `car` VALUES ('./img/CarImage8.png', 8, 190000, 2700, ' Altima-SV', 2, ' a comfortable sedan for daily use', NULL);
INSERT INTO `car` VALUES ('./img/CarImage9.png', 9, 260000, 3600, ' Camaro-SS', 2, ' a powerful car for speed enthusiasts', NULL);
INSERT INTO `car` VALUES ('./img/CarImage10.png', 10, 170000, 2400, ' Elantra-L', 2, ' a modern car for urban adventures', NULL);
INSERT INTO `car` VALUES ('./img/CarImage11.png', 11, 310000, 4200, ' XC90-T8', 2, ' a luxurious SUV for family travels', NULL);
INSERT INTO `car` VALUES ('./img/CarImage12.png', 12, 240000, 3300, ' Outback-X', 2, ' a rugged car for off-road enthusiasts', NULL);
INSERT INTO `car` VALUES ('./img/CarImage13.png', 13, 200000, 2900, ' Sportage-GT', 2, ' a sporty car for dynamic driving', NULL);
INSERT INTO `car` VALUES ('./img/CarImage14.png', 14, 280000, 3700, ' 911-Carrera', 2, ' an iconic car for a luxurious experience', NULL);
INSERT INTO `car` VALUES ('./img/CarImage15.png', 15, 180000, 2600, ' Golf-R', 2, ' a versatile car for any occasion', NULL);
INSERT INTO `car` VALUES ('./img/CarImage16.png', 16, 250000, 3400, ' RX350-L', 2, ' an elegant SUV for a smooth ride', NULL);
INSERT INTO `car` VALUES ('./img/CarImage2.png', 17, 150000, 2100, ' CX5-Sport', 2, ' a stylish SUV for a comfortable journey', NULL);
INSERT INTO `car` VALUES ('./img/CarImage3.png', 18, 300000, 4100, ' F-PACE-400', 2, ' a sophisticated SUV for a classy ride', NULL);
INSERT INTO `car` VALUES ('./img/CarImage4.png', 19, 220000, 3000, ' Yukon-Denali', 2, ' a spacious SUV for family adventures', NULL);
INSERT INTO `car` VALUES ('./img/CarImage5.png', 20, 190000, 2700, ' 500-Lounge', 2, ' a compact car for city exploration', NULL);
INSERT INTO `car` VALUES ('./img/CarImage6.png', 21, 260000, 3500, ' MDX-Advance', 2, ' a luxurious SUV for a premium experience', NULL);
INSERT INTO `car` VALUES ('./img/CarImage7.png', 22, 170000, 2300, ' Encore-GX', 2, ' a stylish and compact car', NULL);
INSERT INTO `car` VALUES ('./img/CarImage8.png', 23, 310000, 4000, ' Aviator-Prestige', 2, ' an elegant SUV for a grand ride', NULL);
INSERT INTO `car` VALUES ('./img/CarImage9.png', 24, 240000, 3200, ' QX60-Luxe', 2, ' a sleek SUV for a sophisticated journey', NULL);
INSERT INTO `car` VALUES ('./img/CarImage10.png', 25, 200000, 2800, ' Outlander-SE', 2, ' a versatile SUV for various terrains', NULL);
INSERT INTO `car` VALUES ('./img/CarImage11.png', 26, 280000, 3700, ' XT5-Luxury', 2, ' a Cadillac for a luxurious and comfortable ride', NULL);
INSERT INTO `car` VALUES ('./img/CarImage12.png', 27, 220000, 3100, ' Wrangler-Rubicon', 2, ' a rugged Jeep for off-road adventures', NULL);
INSERT INTO `car` VALUES ('./img/CarImage13.png', 28, 190000, 2600, ' Ram-1500-Classic', 2, ' a powerful Ram for heavy-duty tasks', NULL);
INSERT INTO `car` VALUES ('./img/CarImage14.png', 29, 260000, 3500, ' Discovery-HSE', 2, ' a Land Rover for an adventurous journey', NULL);
INSERT INTO `car` VALUES ('./img/CarImage15.png', 30, 180000, 2400, ' Cooper-S', 2, ' an iconic Mini for a fun and compact ride', NULL);
INSERT INTO `car` VALUES ('./img/CarImage16.png', 31, 300000, 4100, ' Stelvio-Ti', 2, ' an Alfa Romeo for a sporty and stylish drive', NULL);
INSERT INTO `car` VALUES ('./img/CarImage2.png', 32, 240000, 3300, ' G80-Elite', 2, ' a luxurious Genesis for a smooth and comfortable ride', NULL);
INSERT INTO `car` VALUES ('./img/CarImage3.png', 33, 200000, 2900, ' Fortwo-Passion', 2, ' a compact and efficient Smart for city driving', NULL);
INSERT INTO `car` VALUES ('./img/CarImage4.png', 34, 280000, 3800, ' Continental-Flying-Spur', 2, ' a Bentley for a truly luxurious experience', NULL);
INSERT INTO `car` VALUES ('./img/CarImage5.png', 35, 220000, 3100, ' Impreza-Limited', 2, ' a reliable Subaru for all-weather driving', NULL);
INSERT INTO `car` VALUES ('./img/CarImage6.png', 36, 190000, 2600, ' Explorer-XLT', 2, ' a versatile Ford for family travels', NULL);
INSERT INTO `car` VALUES ('./img/CarImage7.png', 37, 260000, 3500, ' ModelX-Performance', 2, ' an electric Tesla for a sustainable journey', NULL);
INSERT INTO `car` VALUES ('./img/CarImage8.png', 38, 170000, 2300, ' Rav4-XLE', 2, ' a popular Toyota for adventure seekers', NULL);
INSERT INTO `car` VALUES ('./img/CarImage9.png', 39, 310000, 4000, ' GLC-300', 2, ' an elegant Mercedes for a luxurious drive', NULL);
INSERT INTO `car` VALUES ('./img/CarImage10.png', 40, 240000, 3200, ' Rogue-SV', 2, ' a comfortable Nissan for a smooth journey', NULL);
INSERT INTO `car` VALUES ('./img/CarImage11.png', 41, 200000, 2800, ' Equinox-Premier', 2, ' a modern Chevrolet for urban adventures', NULL);
INSERT INTO `car` VALUES ('./img/CarImage12.png', 42, 280000, 3700, ' XE-P300', 2, ' a stylish Jaguar for a classy and dynamic drive', NULL);
INSERT INTO `car` VALUES ('./img/CarImage13.png', 43, 220000, 3000, ' Accord-EX', 2, ' a reliable Honda for daily commuting', NULL);
INSERT INTO `car` VALUES ('./img/CarImage14.png', 44, 190000, 2700, ' Soul-Exclaim', 2, ' a compact and funky Kia for city exploration', NULL);
INSERT INTO `car` VALUES ('./img/CarImage15.png', 45, 260000, 3500, ' Tiguan-SEL', 2, ' a versatile Volkswagen for any occasion', NULL);
INSERT INTO `car` VALUES ('./img/CarImage16.png', 46, 170000, 2400, ' ES-350', 2, ' an elegant Lexus for a luxurious and smooth ride', NULL);
INSERT INTO `car` VALUES ('./img/CarImage2.png', 47, 310000, 4100, ' Acadia-Denali', 2, ' a spacious GMC for family adventures', NULL);
INSERT INTO `car` VALUES ('./img/CarImage3.png', 48, 240000, 3200, ' SantaFe-Limited', 2, ' a modern Hyundai for a comfortable journey', NULL);
INSERT INTO `car` VALUES ('./img/CarImage4.png', 49, 200000, 2800, ' Forester-Premium', 2, ' a rugged Subaru for off-road enthusiasts', NULL);
INSERT INTO `car` VALUES ('./img/CarImage5.png', 50, 280000, 3700, ' Cayenne-S', 2, ' an iconic Porsche for a luxurious experience', NULL);
INSERT INTO `car` VALUES ('./img/CarImage6.png', 51, 220000, 3000, ' 3-Series-M340i', 2, ' a sporty BMW for dynamic driving', NULL);
INSERT INTO `car` VALUES ('./img/CarImage7.png', 52, 190000, 2600, ' Camry-XSE', 2, ' a reliable Toyota for a smooth ride', NULL);
INSERT INTO `car` VALUES ('./img/CarImage8.png', 53, 260000, 3500, ' A4-Premium', 2, ' a sophisticated Audi for a stylish journey', NULL);
INSERT INTO `car` VALUES ('./img/CarImage9.png', 54, 170000, 2300, ' CR-V-EX', 2, ' a popular Honda for versatile adventures', NULL);
INSERT INTO `car` VALUES ('./img/CarImage10.png', 55, 310000, 4000, ' CLA-250', 2, ' a luxurious Mercedes for a premium experience', NULL);
INSERT INTO `car` VALUES ('./img/CarImage11.png', 56, 240000, 3200, ' Fusion-SE', 2, ' a modern Ford for urban driving', NULL);
INSERT INTO `car` VALUES ('./img/CarImage12.png', 57, 200000, 2800, ' Sentra-SR', 2, ' a fuel-efficient Nissan for daily commuting', NULL);
INSERT INTO `car` VALUES ('./img/CarImage13.png', 58, 280000, 3700, ' Model-S-Long-Range', 2, ' an electric Tesla for a sustainable ride', NULL);
INSERT INTO `car` VALUES ('./img/CarImage14.png', 59, 220000, 3100, ' Silverado-LT', 2, ' a powerful Chevrolet for tough tasks', NULL);
INSERT INTO `car` VALUES ('./img/CarImage15.png', 60, 190000, 2600, ' Kona-SEL', 2, ' a compact Hyundai for city exploration', NULL);
INSERT INTO `car` VALUES ('./img/CarImage16.png', 61, 260000, 3500, ' Macan-S', 2, ' a sporty Porsche for a thrilling drive', NULL);
INSERT INTO `car` VALUES ('./img/CarImage2.png', 62, 170000, 2300, ' Optima-EX', 2, ' a stylish Kia for a dynamic journey', NULL);
INSERT INTO `car` VALUES ('./img/CarImage3.png', 63, 310000, 4000, ' S60-Inscription', 2, ' a sleek Volvo for a comfortable and luxurious ride', NULL);
INSERT INTO `car` VALUES ('./img/CarImage4.png', 64, 240000, 3200, ' Crosstrek-Limited', 2, ' an adventurous Subaru for off-road enthusiasts', NULL);
INSERT INTO `car` VALUES ('./img/CarImage5.png', 65, 200000, 2800, ' Grand-Cherokee-Overland', 2, ' a rugged Jeep for outdoor adventures', NULL);
INSERT INTO `car` VALUES ('./img/CarImage6.png', 66, 280000, 3700, ' CT5-Luxury', 2, ' a Cadillac for a luxurious and smooth ride', NULL);
INSERT INTO `car` VALUES ('./img/CarImage7.png', 67, 220000, 3100, ' 2500-Tradesman', 2, ' a powerful Ram for heavy-duty tasks', NULL);
INSERT INTO `car` VALUES ('./img/CarImage8.png', 68, 190000, 2600, ' Range-Rover-HSE', 2, ' an iconic Land Rover for a grand experience', NULL);
INSERT INTO `car` VALUES ('./img/CarImage9.png', 69, 260000, 3500, ' Countryman-Cooper-S', 2, ' a Mini for a fun and compact drive', NULL);
INSERT INTO `car` VALUES ('./img/CarImage10.png', 70, 180000, 2400, ' Giulia-Ti', 2, ' an Alfa Romeo for a sporty and stylish journey', NULL);

-- ----------------------------
-- Table structure for employees
-- ----------------------------
DROP TABLE IF EXISTS `employees`;
CREATE TABLE `employees`  (
  `emp_id` int NOT NULL,
  `name` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `age` int NOT NULL,
  `email` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`emp_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of employees
-- ----------------------------
INSERT INTO `employees` VALUES (1, 'Mike', 30, 'mike11213@gmail.com');
INSERT INTO `employees` VALUES (2, 'Jack', 32, 'Jack313@qq.com');
INSERT INTO `employees` VALUES (3, 'Rose', 20, 'Rose3321@yahoo.com');
INSERT INTO `employees` VALUES (4, 'Chaos', 40, 'Chaos2321@outlook.com');
INSERT INTO `employees` VALUES (5, 'Joker', 30, 'Joker2313@mail2.sysu.edu.cn');

-- ----------------------------
-- Table structure for fine
-- ----------------------------
DROP TABLE IF EXISTS `fine`;
CREATE TABLE `fine`  (
  `lease_id` int NOT NULL,
  `fine_value` int NOT NULL,
  PRIMARY KEY (`lease_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of fine
-- ----------------------------

-- ----------------------------
-- Table structure for global_time
-- ----------------------------
DROP TABLE IF EXISTS `global_time`;
CREATE TABLE `global_time`  (
  `time_global` int NOT NULL,
  `global_year` int NOT NULL,
  `global_month` int NOT NULL,
  `global_day` int NOT NULL,
  PRIMARY KEY (`time_global`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of global_time
-- ----------------------------
INSERT INTO `global_time` VALUES (0, 2023, 12, 30);

-- ----------------------------
-- Table structure for lease
-- ----------------------------
DROP TABLE IF EXISTS `lease`;
CREATE TABLE `lease`  (
  `lease_id` int NOT NULL,
  `usr_id` int NOT NULL,
  `car_id` int NOT NULL,
  `emp_id` int NOT NULL,
  `rent_tot` int NOT NULL,
  `begin_date` int NOT NULL,
  `end_date` int NOT NULL,
  `return_date` int NULL DEFAULT NULL,
  `state` int NOT NULL,
  PRIMARY KEY (`lease_id`) USING BTREE,
  INDEX `usr_id_Btree`(`usr_id` ASC) USING BTREE,
  INDEX `car_id_Btree`(`car_id` ASC) USING BTREE,
  INDEX `emp_id_Btree`(`emp_id` ASC) USING BTREE,
  CONSTRAINT `lease_car` FOREIGN KEY (`car_id`) REFERENCES `car` (`car_id`) ON DELETE CASCADE ON UPDATE RESTRICT,
  CONSTRAINT `lease_emp` FOREIGN KEY (`emp_id`) REFERENCES `employees` (`emp_id`) ON DELETE CASCADE ON UPDATE RESTRICT,
  CONSTRAINT `lease_usr` FOREIGN KEY (`usr_id`) REFERENCES `user` (`usr_id`) ON DELETE CASCADE ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of lease
-- ----------------------------

-- ----------------------------
-- Table structure for purchase
-- ----------------------------
DROP TABLE IF EXISTS `purchase`;
CREATE TABLE `purchase`  (
  `purchase_id` int NOT NULL,
  `usr_id` int NOT NULL,
  `car_id` int NOT NULL,
  `emp_id` int NOT NULL,
  `price` int NOT NULL,
  `purchase_date` int NOT NULL,
  PRIMARY KEY (`purchase_id`) USING BTREE,
  INDEX `usr_id_Btree`(`usr_id` ASC) USING BTREE,
  INDEX `car_id_Btree`(`car_id` ASC) USING BTREE,
  INDEX `emp_id_Btree`(`emp_id` ASC) USING BTREE,
  CONSTRAINT `purchase_car` FOREIGN KEY (`car_id`) REFERENCES `car` (`car_id`) ON DELETE CASCADE ON UPDATE RESTRICT,
  CONSTRAINT `purchase_emp` FOREIGN KEY (`emp_id`) REFERENCES `employees` (`emp_id`) ON DELETE CASCADE ON UPDATE RESTRICT,
  CONSTRAINT `purchase_usr` FOREIGN KEY (`usr_id`) REFERENCES `user` (`usr_id`) ON DELETE CASCADE ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of purchase
-- ----------------------------

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user`  (
  `usr_id` int NOT NULL,
  `name` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `age` int NOT NULL,
  `email` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `password` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `creditcard` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`usr_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES (2, 'Alice', 35, 'alice.smith@gmail.com', 'SecurePwd!', '9876-5432-1098-7654');
INSERT INTO `user` VALUES (3, 'Bob', 22, 'bob.jones@yahoo.com', 'Passw0rd#', '5678-1234-5678-9012');
INSERT INTO `user` VALUES (4, 'Sarah', 30, 'sarah.brown@hotmail.com', 'ComplexPwd', '4321-8765-4321-0987');
INSERT INTO `user` VALUES (5, 'Mike', 25, 'mike.jenkins@gmail.com', 'StrongPwd@', '8765-4321-0987-6543');
INSERT INTO `user` VALUES (6, 'Emily', 31, 'emily.wilson@yahoo.com', 'P@ssw0rd!', '3456-7890-1234-5678');
INSERT INTO `user` VALUES (7, 'David', 29, 'david.miller@gmail.com', 'RandomPwd!', '2109-8765-4321-0987');
INSERT INTO `user` VALUES (8, 'Sophia', 26, 'sophia.clark@hotmail.com', 'SecurePwd@', '6543-2109-8765-4321');
INSERT INTO `user` VALUES (9, 'Ethan', 32, 'ethan.cooper@yahoo.com', 'ComplicatedPwd', '7890-1234-5678-9012');
INSERT INTO `user` VALUES (10, 'Olivia', 27, 'olivia.hill@gmail.com', 'StrongPwd!', '5432-1098-7654-3210');
INSERT INTO `user` VALUES (11, 'Liam', 23, 'liam.roberts@gmail.com', 'UniquePwd@', '1234-5678-9012-3456');
INSERT INTO `user` VALUES (12, 'Ava', 33, 'ava.perez@yahoo.com', 'DifficultPwd#', '8765-4321-0987-6543');
INSERT INTO `user` VALUES (13, 'Mason', 28, 'mason.baker@hotmail.com', '123456789', '4321-8765-4321-0987');
INSERT INTO `user` VALUES (14, 'Harper', 36, 'harper.ross@gmail.com', 'HarperPwd!', '9876-5432-1098-7654');
INSERT INTO `user` VALUES (15, 'Elijah', 24, 'elijah.evans@yahoo.com', 'SecurePwd@', '5678-1234-5678-9012');
INSERT INTO `user` VALUES (16, 'Grace', 29, 'grace.ward@gmail.com', 'StrongPwd!', '4321-8765-4321-0987');
INSERT INTO `user` VALUES (17, 'Logan', 34, 'logan.carter@hotmail.com', 'ComplexPwd#', '8765-4321-0987-6543');
INSERT INTO `user` VALUES (18, 'Lily', 25, 'lily.alexander@yahoo.com', 'P@ssw0rd!', '3456-7890-1234-5678');
INSERT INTO `user` VALUES (19, 'Aiden', 31, 'aiden.foster@gmail.com', 'RandomPwd!', '2109-8765-4321-0987');
INSERT INTO `user` VALUES (20, 'Chloe', 30, 'chloe.long@yahoo.com', 'SecurePwd@', '6543-2109-8765-4321');
INSERT INTO `user` VALUES (21, 'Noah', 22, 'noah.bryant@hotmail.com', '789012345', '7890-1234-5678-9012');
INSERT INTO `user` VALUES (22, 'Zoey', 28, 'zoey.reid@gmail.com', 'StrongPwd!', '5432-1098-7654-3210');
INSERT INTO `user` VALUES (23, 'Jackson', 26, 'jackson.mason@yahoo.com', 'UniquePwd@', '1234-5678-9012-3456');
INSERT INTO `user` VALUES (24, 'Ava', 33, 'ava.perez@hotmail.com', 'DifficultPwd#', '8765-4321-0987-6543');
INSERT INTO `user` VALUES (25, 'Benjamin', 35, 'benjamin.fisher@gmail.com', '123456789', '4321-8765-4321-0987');
INSERT INTO `user` VALUES (26, 'Mia', 29, 'mia.griffith@yahoo.com', 'HarperPwd!', '9876-5432-1098-7654');
INSERT INTO `user` VALUES (27, 'Oliver', 27, 'oliver.hayes@gmail.com', 'SecurePwd@', '5678-1234-5678-9012');
INSERT INTO `user` VALUES (28, 'Amelia', 34, 'amelia.kelly@hotmail.com', 'StrongPwd!', '4321-8765-4321-0987');
INSERT INTO `user` VALUES (29, 'Lucas', 32, 'lucas.harrison@gmail.com', 'ComplexPwd#', '8765-4321-0987-6543');
INSERT INTO `user` VALUES (30, 'Emma', 26, 'emma.perry@yahoo.com', 'P@ssw0rd!', '3456-7890-1234-5678');
INSERT INTO `user` VALUES (31, 'Liam', 23, 'liam.roberts@hotmail.com', 'UniquePwd@', '1234-5678-9012-3456');
INSERT INTO `user` VALUES (32, 'Ava', 33, 'ava.perez@gmail.com', 'DifficultPwd#', '8765-4321-0987-6543');
INSERT INTO `user` VALUES (33, 'Mason', 28, 'mason.baker@yahoo.com', '123456789', '4321-8765-4321-0987');
INSERT INTO `user` VALUES (34, 'Harper', 36, 'harper.ross@hotmail.com', 'HarperPwd!', '9876-5432-1098-7654');
INSERT INTO `user` VALUES (35, 'Elijah', 24, 'elijah.evans@gmail.com', 'SecurePwd@', '5678-1234-5678-9012');
INSERT INTO `user` VALUES (36, 'Grace', 29, 'grace.ward@yahoo.com', 'StrongPwd!', '4321-8765-4321-0987');
INSERT INTO `user` VALUES (37, 'Logan', 34, 'logan.carter@gmail.com', 'ComplexPwd#', '8765-4321-0987-6543');
INSERT INTO `user` VALUES (38, 'Lily', 25, 'lily.alexander@hotmail.com', 'P@ssw0rd!', '3456-7890-1234-5678');
INSERT INTO `user` VALUES (39, 'Aiden', 31, 'aiden.foster@yahoo.com', 'RandomPwd!', '2109-8765-4321-0987');
INSERT INTO `user` VALUES (40, 'Chloe', 30, 'chloe.long@gmail.com', 'SecurePwd@', '6543-2109-8765-4321');
INSERT INTO `user` VALUES (41, 'Noah', 22, 'noah.bryant@gmail.com', '789012345', '7890-1234-5678-9012');
INSERT INTO `user` VALUES (42, 'Zoey', 28, 'zoey.reid@yahoo.com', 'StrongPwd!', '5432-1098-7654-3210');
INSERT INTO `user` VALUES (43, 'Jackson', 26, 'jackson.mason@gmail.com', 'UniquePwd@', '1234-5678-9012-3456');
INSERT INTO `user` VALUES (44, 'Ava', 33, 'ava.perez@hotmail.com', 'DifficultPwd#', '8765-4321-0987-6543');
INSERT INTO `user` VALUES (45, 'Benjamin', 35, 'benjamin.fisher@yahoo.com', '123456789', '4321-8765-4321-0987');
INSERT INTO `user` VALUES (46, 'Mia', 29, 'mia.griffith@gmail.com', 'HarperPwd!', '9876-5432-1098-7654');
INSERT INTO `user` VALUES (47, 'Oliver', 27, 'oliver.hayes@yahoo.com', 'SecurePwd@', '5678-1234-5678-9012');
INSERT INTO `user` VALUES (48, 'Amelia', 34, 'amelia.kelly@gmail.com', 'StrongPwd!', '4321-8765-4321-0987');
INSERT INTO `user` VALUES (49, 'Lucas', 32, 'lucas.harrison@yahoo.com', 'ComplexPwd#', '8765-4321-0987-6543');
INSERT INTO `user` VALUES (50, 'Emma', 26, 'emma.perry@gmail.com', 'P@ssw0rd!', '3456-7890-1234-5678');
INSERT INTO `user` VALUES (51, 'Liam', 23, 'liam.roberts@yahoo.com', 'UniquePwd@', '1234-5678-9012-3456');
INSERT INTO `user` VALUES (52, 'Ava', 33, 'ava.perez@gmail.com', 'DifficultPwd#', '8765-4321-0987-6543');
INSERT INTO `user` VALUES (53, 'Mason', 28, 'mason.baker@yahoo.com', '123456789', '4321-8765-4321-0987');
INSERT INTO `user` VALUES (54, 'Harper', 36, 'harper.ross@hotmail.com', 'HarperPwd!', '9876-5432-1098-7654');
INSERT INTO `user` VALUES (55, 'Elijah', 24, 'elijah.evans@gmail.com', 'SecurePwd@', '5678-1234-5678-9012');
INSERT INTO `user` VALUES (56, 'Grace', 29, 'grace.ward@yahoo.com', 'StrongPwd!', '4321-8765-4321-0987');
INSERT INTO `user` VALUES (57, 'Logan', 34, 'logan.carter@gmail.com', 'ComplexPwd#', '8765-4321-0987-6543');
INSERT INTO `user` VALUES (58, 'Lily', 25, 'lily.alexander@hotmail.com', 'P@ssw0rd!', '3456-7890-1234-5678');
INSERT INTO `user` VALUES (59, 'Aiden', 31, 'aiden.foster@yahoo.com', 'RandomPwd!', '2109-8765-4321-0987');
INSERT INTO `user` VALUES (60, 'Chloe', 30, 'chloe.long@gmail.com', 'SecurePwd@', '6543-2109-8765-4321');
INSERT INTO `user` VALUES (61, 'Noah', 22, 'noah.bryant@gmail.com', '789012345', '7890-1234-5678-9012');
INSERT INTO `user` VALUES (62, 'Zoey', 28, 'zoey.reid@yahoo.com', 'StrongPwd!', '5432-1098-7654-3210');
INSERT INTO `user` VALUES (63, 'Jackson', 26, 'jackson.mason@gmail.com', 'UniquePwd@', '1234-5678-9012-3456');
INSERT INTO `user` VALUES (64, 'Ava', 33, 'ava.perez@hotmail.com', 'DifficultPwd#', '8765-4321-0987-6543');
INSERT INTO `user` VALUES (65, 'Benjamin', 35, 'benjamin.fisher@gmail.com', '123456789', '4321-8765-4321-0987');
INSERT INTO `user` VALUES (66, 'Mia', 29, 'mia.griffith@yahoo.com', 'HarperPwd!', '9876-5432-1098-7654');
INSERT INTO `user` VALUES (67, 'Oliver', 27, 'oliver.hayes@gmail.com', 'SecurePwd@', '5678-1234-5678-9012');
INSERT INTO `user` VALUES (68, 'Amelia', 34, 'amelia.kelly@hotmail.com', 'StrongPwd!', '4321-8765-4321-0987');
INSERT INTO `user` VALUES (69, 'Lucas', 32, 'lucas.harrison@gmail.com', 'ComplexPwd#', '8765-4321-0987-6543');
INSERT INTO `user` VALUES (70, 'Emma', 26, 'emma.perry@yahoo.com', 'P@ssw0rd!', '3456-7890-1234-5678');
INSERT INTO `user` VALUES (71, 'Liam', 23, 'liam.roberts@hotmail.com', 'UniquePwd@', '1234-5678-9012-3456');
INSERT INTO `user` VALUES (72, 'Ava', 33, 'ava.perez@gmail.com', 'DifficultPwd#', '8765-4321-0987-6543');
INSERT INTO `user` VALUES (73, 'Mason', 28, 'mason.baker@yahoo.com', '123456789', '4321-8765-4321-0987');
INSERT INTO `user` VALUES (74, 'Harper', 36, 'harper.ross@hotmail.com', 'HarperPwd!', '9876-5432-1098-7654');
INSERT INTO `user` VALUES (75, 'Elijah', 24, 'elijah.evans@gmail.com', 'SecurePwd@', '5678-1234-5678-9012');
INSERT INTO `user` VALUES (76, 'Grace', 29, 'grace.ward@yahoo.com', 'StrongPwd!', '4321-8765-4321-0987');
INSERT INTO `user` VALUES (77, 'Logan', 34, 'logan.carter@gmail.com', 'ComplexPwd#', '8765-4321-0987-6543');
INSERT INTO `user` VALUES (78, 'Lily', 25, 'lily.alexander@hotmail.com', 'P@ssw0rd!', '3456-7890-1234-5678');
INSERT INTO `user` VALUES (79, 'Aiden', 31, 'aiden.foster@yahoo.com', 'RandomPwd!', '2109-8765-4321-0987');
INSERT INTO `user` VALUES (80, 'Chloe', 30, 'chloe.long@gmail.com', 'SecurePwd@', '6543-2109-8765-4321');
INSERT INTO `user` VALUES (81, 'Noah', 22, 'noah.bryant@gmail.com', '789012345', '7890-1234-5678-9012');
INSERT INTO `user` VALUES (82, 'Zoey', 28, 'zoey.reid@yahoo.com', 'StrongPwd!', '5432-1098-7654-3210');
INSERT INTO `user` VALUES (83, 'Jackson', 26, 'jackson.mason@gmail.com', 'UniquePwd@', '1234-5678-9012-3456');
INSERT INTO `user` VALUES (84, 'Ava', 33, 'ava.perez@hotmail.com', 'DifficultPwd#', '8765-4321-0987-6543');
INSERT INTO `user` VALUES (85, 'Benjamin', 35, 'benjamin.fisher@gmail.com', '123456789', '4321-8765-4321-0987');
INSERT INTO `user` VALUES (86, 'Mia', 29, 'mia.griffith@yahoo.com', 'HarperPwd!', '9876-5432-1098-7654');
INSERT INTO `user` VALUES (87, 'Oliver', 27, 'oliver.hayes@gmail.com', 'SecurePwd@', '5678-1234-5678-9012');
INSERT INTO `user` VALUES (88, 'Amelia', 34, 'amelia.kelly@hotmail.com', 'StrongPwd!', '4321-8765-4321-0987');
INSERT INTO `user` VALUES (89, 'Lucas', 32, 'lucas.harrison@gmail.com', 'ComplexPwd#', '8765-4321-0987-6543');
INSERT INTO `user` VALUES (90, 'Emma', 26, 'emma.perry@yahoo.com', 'P@ssw0rd!', '3456-7890-1234-5678');
INSERT INTO `user` VALUES (91, 'Liam', 23, 'liam.roberts@yahoo.com', 'UniquePwd@', '1234-5678-9012-3456');
INSERT INTO `user` VALUES (92, 'Ava', 33, 'ava.perez@gmail.com', 'DifficultPwd#', '8765-4321-0987-6543');
INSERT INTO `user` VALUES (93, 'Mason', 28, 'mason.baker@yahoo.com', '123456789', '4321-8765-4321-0987');
INSERT INTO `user` VALUES (94, 'Harper', 36, 'harper.ross@hotmail.com', 'HarperPwd!', '9876-5432-1098-7654');
INSERT INTO `user` VALUES (95, 'Elijah', 24, 'elijah.evans@gmail.com', 'SecurePwd@', '5678-1234-5678-9012');
INSERT INTO `user` VALUES (96, 'Grace', 29, 'grace.ward@yahoo.com', 'StrongPwd!', '4321-8765-4321-0987');
INSERT INTO `user` VALUES (97, 'Logan', 34, 'logan.carter@gmail.com', 'ComplexPwd#', '8765-4321-0987-6543');
INSERT INTO `user` VALUES (98, 'Lily', 25, 'lily.alexander@hotmail.com', 'P@ssw0rd!', '3456-7890-0987-6543');

-- ----------------------------
-- Triggers structure for table global_time
-- ----------------------------
DROP TRIGGER IF EXISTS `update_lease_trigger`;
delimiter ;;
CREATE TRIGGER `update_lease_trigger` BEFORE UPDATE ON `global_time` FOR EACH ROW BEGIN
            DECLARE carState INT;
            DECLARE leaseCarId INT;
        
            -- 获取车辆状态和lease表对应的car_id
            SELECT car.state, lease.car_id INTO carState, leaseCarId
            FROM car
            JOIN lease ON car.car_id = lease.car_id
            WHERE lease.begin_date = CONCAT(NEW.global_year, NEW.global_month, NEW.global_day) AND lease.state = 0
            LIMIT 1;
        
            -- 根据车辆状态更新lease表
            UPDATE lease
            SET state = CASE 
                WHEN carState = 2 THEN 1  -- 车辆处于空闲状态，订单进行中
                ELSE 4                     -- 车辆不处于空闲状态，订单取消
            END
            WHERE begin_date = CONCAT(NEW.global_year, NEW.global_month, NEW.global_day) AND state = 0;
        
            -- 更新car表
            IF carState = 2 THEN
                -- 车辆处于空闲状态，将车辆状态置为被租用
                UPDATE car
                SET state = 1
                WHERE car_id = leaseCarId;
            END IF;
        END
;;
delimiter ;

-- ----------------------------
-- Triggers structure for table global_time
-- ----------------------------
DROP TRIGGER IF EXISTS `update_lease_status_trigger`;
delimiter ;;
CREATE TRIGGER `update_lease_status_trigger` AFTER UPDATE ON `global_time` FOR EACH ROW BEGIN
            UPDATE lease
            SET state = 3
            WHERE state = 1
            AND NEW.global_year * 10000 + NEW.global_month * 100 + NEW.global_day > lease.end_date;
        END
;;
delimiter ;

-- ----------------------------
-- Triggers structure for table lease
-- ----------------------------
DROP TRIGGER IF EXISTS `check_return_date_trigger`;
delimiter ;;
CREATE TRIGGER `check_return_date_trigger` AFTER UPDATE ON `lease` FOR EACH ROW BEGIN
            DECLARE fineValue INT;
            DECLARE rentPerDay INT;
            DECLARE overDueDay INT;
			DECLARE tempOverDue INT;
            IF OLD.return_date IS NULL AND NEW.return_date IS NOT NULL THEN
                -- 获取租赁车辆的rent值
                SELECT rent INTO rentPerDay
                FROM car
                WHERE car_id = NEW.car_id;

                -- 计算逾期的天数
                SET tempOverDue = (NEW.return_date - NEW.end_date) / 10000 * 365 + (((NEW.return_date - NEW.end_date) / 100) % 100) * 30 + (NEW.return_date - NEW.end_date) % 100;
--                 -- 计算罚款值,每天租金的1.5倍率
				SET overDueDay = GREATEST(0, tempOverDue);
                SET fineValue = overDueDay * rentPerDay * 1.5;
                -- 如果是逾期还车，插入fine表中
                IF fineValue > 0 THEN
                  INSERT INTO fine (lease_id, fine_value)
                  VALUES (NEW.lease_id, fineValue);
                END IF;
            END IF;
        END
;;
delimiter ;

SET FOREIGN_KEY_CHECKS = 1;
