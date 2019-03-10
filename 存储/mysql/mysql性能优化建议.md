# mysql性能优化建议

- 作者：codehackfox@gmail.com
- 时间：2015-12-28 12:23:00

>## 0x00、优化建议

- 1.为查询缓存优化你的查询(curdata(),rand(),no()无法进行优化)；
- 2.explain你的查询；
- 3.当只要一行数据时使用limit 1；
- 4.为搜索字段建立索引；
- 5.在join表的时候使用相当类型的列，并将其索引
- 6.千万不要order by rand();
- 7.避免select *；
- 8.用于为每张表设置一个id，尽量为unsigned int类型；
- 9.使用enum而不是varchar;
- 10.从procedure  analyse()取得建议；
- 11.尽可能的使用not null;
- 12.Prepared  Statements;
- 13.把ip地址存成UNSIGNED INT
- 14.固定长度表会更快；
- 15.垂直分割；
- 16.拆分大的delete或insert语句；
- 17.越小的列会越快；
- 18.选择正确的存储引擎；
- 19.使用一个对象关系映射器（ORM）；
- 20.小心“永久链接”；
