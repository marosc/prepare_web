FROM ubuntu:22.04
RUN apt-get -y update
RUN apt -y install apache2
ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/Bratislava
RUN apt-get install -y tzdata
RUN apt -y install php mysql-server libapache2-mod-php php-mysql
RUN rm /var/www/html/index.html
RUN sed -i 's/upload_max_filesize = 2M/upload_max_filesize = 20M/g' /etc/php/8.1/apache2/php.ini
RUN sed -i 's/post_max_size = 8M/post_max_size = 200M/g' /etc/php/8.1/apache2/php.ini
RUN sed -i 's/max_execution_time = 30/max_execution_time = 120/g' /etc/php/8.1/apache2/php.ini
RUN chmod -R 777 /run/mysqld
RUN apt-get -y install software-properties-common
RUN add-apt-repository -y ppa:deadsnakes/ppa
RUN apt-get -y update
RUN apt -y install python3.8
RUN apt -y install python3-pip
RUN pip3 install pandas==2.1.4
RUN pip3 install matplotlib==3.8.2
RUN mkdir /var/www/html/results
RUN mkdir /var/www/html/uploads
RUN chmod 777 /var/www/html/results
RUN chmod 777 /var/www/html/uploads

# docker build -t simulation_web_image .
# docker run -dit -v path.to.html:/var/www/html/ -v path.to.data:/home/data/ -v path.to.code:/home/code/ --name simulation_web -p 8085:80 simulation_web_image
# docker container exec -it simulation_web /bin/bash
#  service apache2 start
#  service mysql start
#  mysql -u root < /home/data/db.sql     # copy db.sql from import/db/ to data/

