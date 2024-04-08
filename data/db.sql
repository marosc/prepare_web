alter user 'root'@'localhost' identified with mysql_native_password by 'password';
CREATE USER 'portal'@'%' IDENTIFIED BY 'password';
GRANT ALL ON *.* TO 'portal'@'%';

CREATE DATABASE IF NOT EXISTS `portal` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;

use portal;

CREATE TABLE upload_user (
  `code` VARCHAR(50) PRIMARY KEY,
  `password` VARCHAR(80)
);