--Есть таблица test:
--id	date	value
--1	2020-03-05	100
--2	2020-03-10	200
--3	2020-02-01	50
--4	2020-01-05	60
--5	2020-03-06	80
--6	2020-01-10	110
--7	2020-01-08	100
--8	2020-02-08	70
--9	2020-04-18	105
--10	2020-02-02	40

--Подсчитать подытог по сумме valueдля каждой строки. Т.е. получить следующую таблицу. Сделать двумя способами.
--date	value	sum
--05.01.2020	60	60
--08.01.2020	100	160
--10.01.2020	110	270
--01.02.2020	50	320
--02.02.2020	40	360
--08.02.2020	70	430
--05.03.2020	100	530
--06.03.2020	80	610
--10.03.2020	200	810
--18.04.2020	105	915

-- v1
SELECT
	TO_CHAR(date, 'DD.MM.YYYY') as "date",
	value,
	SUM(value) OVER (ORDER BY date asc) as "sum"
FROM test 
ORDER BY date::date;

-- v2
select TO_CHAR(t1.date, 'DD.MM.YYYY') as "date", 
       t1.value, 
       t1.value + (select coalesce(sum(t2.value), 0)
	        from test t2
	        where t2.date < t1.date) as sum
from test t1
order by t1.date;