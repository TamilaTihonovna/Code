select actor.first_name, actor.last_name, count(*) as film_count
from actor
join film_actor on actor.actor_id = film_actor.actor_id
join film_category on film_actor.film_id = film_category.film_id
join category on film_category.category_id = category.category_id
where category.name = 'Children'
group by actor.actor_id, actor.first_name, actor.last_name
having count(*) >= (
select min(film_count) from (
select count(*) as film_count from actor
join film_actor on actor.actor_id = film_actor.actor_id
join film_category on film_actor.film_id = film_category.film_id
join category on film_category.category_id = category.category_id
where category.name = 'Children'
group by actor.actor_id
order by film_count desc 
limit 3
        ) as TopFilmCounts
    )
order by film_count DESC, actor.last_name, actor.first_name;
