from database import DB
import cPickle as pickle

DB_name = 'imdb_nmz'

'''
Amalgamating all the subqueries into a monster query to create an aggregate matrix.
'''

matrix = """select grblg.movie_id,grblg.gross,grblg.buget,grblg.languages,grblg.genres,country.count countries from (
select grbl.movie_id,grbl.gross,grbl.buget,grbl.languages,genre.count genres from (
select grb.movie_id,grb.gross,grb.buget,lang.count languages from (
select gr.movie_id,gr.info gross,budget.info buget from (
select movie_id,info
from title m INNER JOIN movie_info
ON (m.id=movie_info.movie_id)
WHERE (info_type_id=107 AND info LIKE ('\$%') )
) gr inner join (
select movie_id,info
from title p
INNER JOIN movie_info
ON (p.id=movie_info.movie_id)
WHERE (info_type_id=105 AND info LIKE ('\$%') )
) budget
ON (gr.movie_id=budget.movie_id)
) grb inner join (
select movie_id,COUNT(info) from (
select t.title,t.id,m.movie_id,m.info_type_id,m.info
from title t
inner join movie_info m
ON (t.id=m.movie_id)
where info_type_id=4 ) temp1
group by movie_id
) lang
ON (grb.movie_id=lang.movie_id)
) grbl inner join (
select movie_id,COUNT(info) from (
select t.title,t.id,m.movie_id,m.info_type_id,m.info
from title t
inner join movie_info m
ON (t.id=m.movie_id)
where info_type_id=3 ) temp2
group by movie_id
) genre
ON (grbl.movie_id=genre.movie_id)
) grblg inner join (
select movie_id,COUNT(info) from (
select t.title,t.id,m.movie_id,m.info_type_id,m.info
from title t
inner join movie_info m
ON (t.id=m.movie_id)
where info_type_id=8 ) temp3
group by movie_id
) country
ON (grblg.movie_id=country.movie_id);
"""

#Main function
def main():
    db = DB('imdb_nmz')
    print 'Movie_id, Gross Revenue, Budget, Language, Genre, Country'
    t = db.query(matrix)
    aggregate_matrix = []
    for line in t:
	t = line[1]
        k = line[2]
        result1 = []
        result2 = []
        f = []
        l = []
        output = [0,0,0,0,0,0]
        result1.append(t.split(' ')[0])
        for each in result1[0]:
            if each.isdigit():
                f.append(each)
        s = int(''.join(map(str,f)))

        result2.append(k.split(' ')[0])
        for each in result2[0]:
            if each.isdigit():
                l.append(each)
        p = int(''.join(map(str,l)))
        output[0] = line[0]
        output[1] = s
        output[2] = p
        output[3] = int(line[3])
        output[4] = int(line[4])
        output[5] = int(line[5])
        #You can uncomment this statement to ensure the order and see on the terminal if you would like to  
        #print output
        aggregate_matrix.append(output)
    
    #Dumping data through pickle
    pickle.dump( aggregate_matrix, open("agg_matrix.p", "wb" ) )

if __name__ == '__main__':
    main()
