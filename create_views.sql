CREATE VIEW Days_Rate AS
	 SELECT time::date AS day, count(*) AS num 
	 FROM log 
	 GROUP BY day;
	 
CREATE VIEW Error_Rate AS
     SELECT time::date AS day, count(*) AS num
	 FROM log 
	 WHERE status='404 NOT FOUND'
	 GROUP BY day 
	 ORDER BY day;
	 
CREATE VIEW All_Rate AS	
	 SELECT Days_Rate.day, Days_Rate.num AS Rate, Error_Rate.num AS Error
	 FROM Days_Rate, Error_Rate
	 WHERE Days_Rate.day = Error_Rate.day
	 GROUP BY Days_Rate.day, Days_Rate.num, Error_Rate.num; 
