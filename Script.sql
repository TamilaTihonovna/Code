select category.name, count(film.film_id) as film_count from category 
join film_category on film_category.category_id=category.category_id 
join film on film_category.film_id=film.film_id 
group by category.name
order by film_count desc
