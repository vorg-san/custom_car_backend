drop database custom_car;

CREATE DATABASE if not exists custom_car CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `custom_car`.`car` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(400) NOT NULL,
  `price` DECIMAL(10,8) NULL,
  `transmission` VARCHAR(400) NULL,
  `engine` VARCHAR(400) NULL,
  `drivetrain` VARCHAR(400) NULL,
  `weight` VARCHAR(400) NULL,
  `needs_fixin` VARCHAR(2000) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;

use custom_car;
show tables;

select * from polls_question;
select * from polls_choice;

-> set MYSQL_PASS in system variables as password of root user for mysql on your machine
-> python manage.py makemigrations polls
-> python manage.py check
-> python manage.py migrate
-> python manage.py shell
-> superuser: admin 6AypCcg6!Py5
-> python manage.py runserver
-> 
-> 
-> 