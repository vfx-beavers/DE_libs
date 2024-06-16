-- позволяет получить реальные последовательные периоды действия цены, 
-- вместо условных, которые не поддаются последующему анализу



--select md5(concat(a,b,c,d)) from tablename_ref;

--select * into tablename_v3 from tablename_v2;

--${DEFAULT_DATE_TO}=(9999-12-31 23:59:59.000)::timestamp(3);

update tableName_v3 sat
   set date_to=tt.date_close
  from (
        select gid
              ,hashsum
              ,date_from
              ,max(date_close) over (partition by gid, date_from) date_close
         from (
               select gidName gid
                     ,hashsum
                     ,date_from
                     ,lead(date_from) over(partition by gidName order by date_from) date_close
                 from tableName_v2
                where date_to = '9999-12-31 23:59:59.000'::timestamp(3)
              )t
	      )tt
 where sat.date_to = '9999-12-31 23:59:59.000'::timestamp(3)
   and sat.gidName = tt.gid
   and sat.date_from = tt.date_from
   and sat.hashsum = tt.hashsum
   and sat.date_from!=tt.date_close;