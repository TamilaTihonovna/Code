select film.title from film 
left join inventory on inventory.film_id = film.film_id
where inventory.film_id is null