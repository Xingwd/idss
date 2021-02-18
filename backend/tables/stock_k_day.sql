
DROP TABLE IF EXISTS stock_k_day;
CREATE TABLE IF NOT EXISTS stock_k_day(
   code VARCHAR(10) NOT NULL COMMENT '股票代码',
   date VARCHAR(10) COMMENT '交易日期',
   open FLOAT COMMENT '开盘价',
   high FLOAT COMMENT '最高价',
   low FLOAT COMMENT '最低价',
   close FLOAT COMMENT '收盘价',
   preclose FLOAT COMMENT '昨日收盘价',
   volume BIGINT COMMENT '成交量',
   amount BIGINT COMMENT '成交额',
   adjustflag INT COMMENT '复权状态(1=后复权,2=前复权,3=不复权)',
   turn FLOAT COMMENT '换手率',
   tradestatus INT COMMENT '交易状态',
   pctChg FLOAT COMMENT '涨跌幅',
   peTTM FLOAT COMMENT '滚动市盈率',
   psTTM FLOAT COMMENT '滚动市销率',
   pcfNcfTTM FLOAT COMMENT '滚动市现率',
   pbMRQ FLOAT COMMENT '市净率',
   isST INT COMMENT '是否ST(1是0否)',
   PRIMARY KEY ( code,date )
) COMMENT='股票详情' ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
