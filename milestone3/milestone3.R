library('rJava')
library('DBI')
library('RJDBC')

drv<-JDBC("org.apache.hive.jdbc.HiveDriver", list.files("/Users/liuhongyang/Desktop/hive/RProject",pattern="jar$", full.names=T, recursive=TRUE))

conn<-dbConnect(drv, sprintf('jdbc:hive2://http://10.242.135.104:10000/WQD7005'), 'root', 'password') 

dbGetQuery(conn, "show databases")

dbGetQuery(conn, "select * from oilcrawldata")