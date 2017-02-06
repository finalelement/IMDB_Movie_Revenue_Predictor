import psycopg2


class DB:
    def __init__(self, db_name):
        try:
            self.conn = psycopg2.connect("dbname='%s'" % db_name)
        except:
            print "I am unable to connect to the database"
            exit()
        self.cur = self.conn.cursor()

    def cursor(self):
        return self.cur

    def getNewCursor(self):
        return self.conn.cursor()

    def connection(self):
        return self.conn

    def query(self, q):
        self.cur.execute(q)
        return self.cur.fetchall()


def main():
    db = DB('imdb_nmz')
    q = 'select * from title limit 10'
    for line in db.query(q):
	print line
    print 'IMDB_NMZ !'
    print 'Successfully works ! Now go ahead write the code !'


if __name__ == '__main__':
    main()
