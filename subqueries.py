from database import DB

DB_name = 'imdb_nmz'

'''
The queries below all act as subqueries for the aggregate matrix query which will be 
fed to ML.

1.)Distinct count of movies by titles

2.)Distinct count of total genres present for movies

3.)Distinct count of total countries where movies were released

4.)Distinct count of total languages in which the movies were released.

5.)Gross Revenue per movie id.

6.)Budget of a movie per movie id.

7.)Number of languages the movie was released in per movie id.

8.)Number of genres the movie was tagged to per movie id.

9.)Number of countries where the movie was released in per movie id.
'''

title_count = 'select count(distinct(title)) from title;'

genre_count = 'select count(distinct(info)) from movie_info where info_type_id=3;'

country_count = 'select count(distinct(info)) from movie_info where info_type_id=8;'

language_count = 'select count(distinct(info)) from movie_info where info_type_id=4;'

gross_revenue = """select movie_id,info
from title m INNER JOIN movie_info
ON (m.id=movie_info.movie_id)
WHERE (info_type_id=107 AND info LIKE ('\$%') ) limit 10;"""

movie_budget = """select movie_id,info
from title p
INNER JOIN movie_info
ON (p.id=movie_info.movie_id)
WHERE (info_type_id=105 AND info LIKE ('\$%') ) limit 10;"""

movie_lang = """select movie_id,COUNT(info) from (
select t.title,t.id,m.movie_id,m.info_type_id,m.info
from title t
inner join movie_info m
on (t.id=m.movie_id)
where info_type_id=4 ) temp
group by movie_id order by count(info) DESC limit 10;"""

movie_genre = """select movie_id,COUNT(info) from (
select t.title,t.id,m.movie_id,m.info_type_id,m.info
from title t
inner join movie_info m
on (t.id=m.movie_id)
where info_type_id=3 ) temp
group by movie_id order by count(info) DESC limit 10;"""

movie_country = """select movie_id,COUNT(info) from (
select t.title,t.id,m.movie_id,m.info_type_id,m.info
from title t
inner join movie_info m
on (t.id=m.movie_id)
where info_type_id=8 ) temp
group by movie_id order by count(info) DESC limit 10;"""

#Main function
def main():
    db = DB('imdb_nmz')
    for line in db.query(title_count):
	print 'Distinct count of titles: '
	print line[0]
    
    
    for line in db.query(genre_count):
        print 'Distinct count of genres: '
        print line[0]


    for line in db.query(country_count):
        print 'Distinct count of countries: '
        print line[0]


    for line in db.query(language_count):
        print 'Distinct count of languages: '
        print line[0]

    print 'Gross Revenue by movie id: '
    for line in db.query(gross_revenue):
	print line

    print 'Movie Budget by movie id: '
    for line in db.query(movie_budget):
        print line

    print 'Number of languages per movie id: '
    for line in db.query(movie_lang):
        print line

    print 'Number of genres per movie id: '
    for line in db.query(movie_genre):
        print line

    print 'Number of countries by movie id: '
    for line in db.query(movie_country):
        print line

if __name__ == '__main__':
    main()
