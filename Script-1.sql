select actor.first_name, actor.last_name, 
count(film.rental_duration) AS rental_count
from actor
join film_actor on film_actor.actor_id = actor.actor_id
join film on film_actor.film_id = film.film_id
group by actor.actor_id, actor.first_name, actor.last_name
order by rental_count desc
limit 10

