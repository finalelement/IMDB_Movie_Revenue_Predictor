# finalelement_final_project
Predictive Movie Analytics

1.) Run the sanity test database.py to ensure that there is connectivity to the imdb_nmz (this is the database that I created).
Usage: python database.py

2.) subqueries.py is a list of all the queries that I made in bits and pieces. Running it will give output of multiple queries that have 
also been described in that file. However I have limited the output of the queries there to 10 so as not to clog the terminal.

************This was only used to create all queries and all of them were used for a final query
not related in generation of matrix directly !**************

Usage: python subqueries.py

3.)  matrix.py will generate the final matrix by running the monster query -> cleaning it up -> forming a list of lists. This script will
output a file 'agg_matrix.p'. This is a pickle file and it is a hard-coded name and the same is read by the machine learning model script
ml_matrix.py.

Usage: python matrix.py
Output: agg_matrix.p
Note - It will take a couple of minutes to run. Worst case scenario five (It never went there, but just saying)

4.) Once we have the agg_matrix.p. ml_matrix.py has to be executed. It will output the results of the machine learning models implemented
for the linear and lasso regression. However for GaussianNB and Logistic if you wish to verify the values from the report. 'N' will
have to changed manually.
Usage: python ml_matrix.py

5.) mat_out.txt is a log file of the matrix that i generated from printing the output in matrix.py by redirecting the output.

And thats all folks !!

Thanks,
Vish
