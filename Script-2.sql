select category.name, sum(payment.amount) as total_spent from category
join film_category on film_category.category_id = category.category_id 
join inventory on inventory.film_id = film_category.film_id 
join rental on rental.inventory_id = inventory.inventory_id 
join payment on payment.rental_id = rental.rental_id
group by category.name
order by total_spent desc 
limit 1