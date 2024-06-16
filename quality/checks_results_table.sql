Select datetime, table_name, dq_check_name, dq_check_result  From stage.dq_checks_results where dq_check_result = 1
order by datetime DESC
limit 1;