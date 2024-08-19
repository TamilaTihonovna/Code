select category.name, sum(film.rental_duration) as time from category
join film_category ON category.category_id = film_category.category_id
join film on film.film_id = film_category.film_id
join inventory on film.film_id = inventory.film_id
join rental on inventory.inventory_id = rental.inventory_id
join customer on rental.customer_id = customer.customer_id
join address on customer.address_id = address.address_id
join city on address.city_id = city.city_id
where city.city like 'a%' or city.city like '%-%'
group by category.name
order by time desc 
limit 1