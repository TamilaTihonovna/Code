select city.city, 
count(case when customer.active = 1 then 1 end) as active_customer, 
count(case when customer.active = 0 then 1 end) as NOT_active_customer 
from city 
join address on address.city_id =city.city_id 
join customer on address.address_id = customer.address_id
group by city.city
order by NOT_active_customer desc