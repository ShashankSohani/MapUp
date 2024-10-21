with recursivedistance as(
    select id, source, destination, distance from toll_location
    union all
    select r1.id, r1.source, r2.destination, r.distance + r2.distance
    from recursiveDistance r1
    join toll_location r2 on r1.destination = r2.source

)

select r1.source, r2.source, coaesce(r1.distance, r2.distance) as distance
from recursiveDistance r1
join recursiveDistance r2
join recursiveDistance r2 on r1.destination = r2.source
group by r1.source, r2.source3