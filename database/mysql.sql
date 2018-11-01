create table py_dept(
	id int primary key auto_increment,
	name varchar(50),
	addtime timestamp NULL default CURRENT_TIMESTAMP,
	description varchar(500)
)

create table py_user(
	id int primary key auto_increment,
	name varchar(50) not null,
	sex varchar(2) default'男' check(sex='男' or sex='女'),
	age int,
	address varchar(500),
	email varchar(100),
	addtime timestamp NULL default CURRENT_TIMESTAMP,
	dept_id int foreign key references py_dept(id)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;


sudo docker pull mysql:5.6
sudo docker run --name mysql -e MYSQL_ROOT_PASSWORD=admin -e MYSQL_DATABASE=inst1 -d -p 3066:3066 mysql:5.6

sudo docker run --name mysql -e MYSQL_ROOT_PASSWORD=root -d -p 3066:3066 mysql:5.6

sudo docker exec -it mysql bash
mysql -uroot -padmin

sudo docker cp mysql:/var/lib/mysql /wwwroot/docker/mysql/data
sudo docker stop mysql
sudo docker rm mysql

sudo docker run --name mysql -e MYSQL_ROOT_PASSWORD=root -d -p 3066:3066 -v $PWD/data:/var/lib/mysql -v $PWD/etc:/etc/mysql -v $PWD/log:/var/log/mysql mysql:5.6
sudo docker run --name mysql -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=pythonDb -d -p 3066:3066 -v $PWD/data:/var/lib/mysql mysql:5.6
sudo docker run --name mysql -e MYSQL_ROOT_PASSWORD=root -d -p 3066:3066 -v $PWD/data:/var/lib/mysql mysql:5.6
mysql -uroot -proot
create database pythonDb
sudo docker inspect mysql
docker network inspect wordpress_net 
docker network create --driver bridge --subnet 172.25.0.0/16 wordpress_net

sudo docker run -itd --name myredis -p 6379:6379 -v /wwwroot/docker/redis/data:/data redis:latest redis-server /data/etc/redis.conf
