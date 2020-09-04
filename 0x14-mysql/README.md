# Database administration

>Database administrators use specialized software to store and organize data. The role 
>may include capacity planning, installation, configuration, database design, 
>migration, performance monitoring, security, troubleshooting, as well as backup and 
>data recovery.

## SQL Replication
Replication is a set of technologies for copying and distributing 
data and database objects from one database to another and then 
synchronizing between databases to maintain consistency. 
Use replication to distribute data to different locations and to remote or mobile users 
over local and wide area networks, dial-up connections, wireless connections, and the Internet.

Transactional replication is typically used in server-to-server scenarios that require 
high throughput, including: improving scalability and availability; data warehousing 
and reporting; integrating data from multiple sites; integrating heterogeneous data; 
and offloading batch processing. Merge replication is primarily designed for mobile applications 
or distributed server applications that have possible data conflicts

## Master-Slave Replication
The most basic kind of SQL replication is a Master-Slave configuration. In this scenario, you have 
a main database server, which is referred to as the “master” server. 
This server is responsible for performing all writes and updates. 
The data from this server is copied continuously to a “slave” server. 
This server can be be read from, but not written to.

![alt text](https://www.researchgate.net/profile/Raju_Shrestha3/publication/317299391/figure/fig1/AS:540208529670144@1505807158195/Master-slave-architecture.png)
