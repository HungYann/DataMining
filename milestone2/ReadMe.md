1. Create table in hive



```mysql
create table oilCrawl(Index STRING,Year STRING,AverageClosingPrice STRING,YearOpen STRING,YearHigh STRING,YearLow STRING,YearClose STRING,AnnualChange STRING)row format delimited fields terminated by ',' stored as textfile; 
```



2. check the table 



```mysql
describe oilCrawl
```



3. load data into hdfs



```mysql
hdfs dfs -copyFromLoacl ~/Desktop/oilCrawl.txt /usr/oilCrawl
```



4. Load data from hdfs

```mysql
LOAD data inpath '/usr/oilCrawl' into table oilCrawl;
```



5. check the data in hive

```mysql
select * from oilCrawl
```





![results-screenshot](https://tva1.sinaimg.cn/large/00831rSTgy1gd2w96zc4ij30wk0lq43g.jpg)