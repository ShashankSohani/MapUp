select id, id_2,
case when timestampdiff(hour, concat(startday, ' ' , starttime), concat(endday, ' ' , endtime)) = 24
and count(distinct startday) = 7
then 'complete'
else 'incomplete'
end as completeness
from timestamps
group by id, id_2