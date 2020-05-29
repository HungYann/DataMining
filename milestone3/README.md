WQD 7005 - Data Mining Continue Assessment



##### Participants



- 17201091/1 LIU,HONGYANG

- 17043640/1 Gunasegarran



___



##### Milestone 3



Milestone 3: https://github.com/LIU-HONGYANG/DataMining/tree/master/milestone3



Video: https://www.youtube.com/watch?v=YcFxfNfkmqM





---



##### R code:



```R
library('rJava')
library('DBI')
library('RJDBC')

drv<-JDBC("org.apache.hive.jdbc.HiveDriver", list.files("/Users/liuhongyang/Desktop/hive/RProject",pattern="jar$", full.names=T, recursive=TRUE))

conn<-dbConnect(drv, sprintf('jdbc:hive2://http://10.242.135.104:10000/WQD7005'), 'root', 'password') 

dbGetQuery(conn, "show databases")

dbGetQuery(conn, "select * from oilcrawldata")
```



##### Resutls:



![image-20200520171120090](https://tva1.sinaimg.cn/large/007S8ZIlgy1gez1otow3uj30si106gtn.jpg)





