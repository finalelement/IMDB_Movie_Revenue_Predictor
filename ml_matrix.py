import scipy
import numpy as np
from sklearn import linear_model
from sklearn.metrics import roc_auc_score
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import StratifiedKFold
import cPickle as pickle


#Loading matrix from pickle 


def load_matrix():
    aggregate_matrix = pickle.load( open( "agg_matrix.p", "rb" ) )
    return aggregate_matrix


def prnt_matrix():
    for each in aggregate_matrix:
        print each

def create_input(matrix):
    #Excluding data points (movie_id) and gross_revenue
    skip = 2
    #width = len(matrix[0]) - skip
    width = len(matrix[0])
    X = scipy.zeros((len(matrix),width))
    for i in range(0, len(matrix)):
        for j in range(skip,width):
	    X[i, j-skip] = matrix[i][j] if matrix[i][j] != '' else 0
    return X

def create_output(matrix):
    Y = scipy.zeros(len(matrix))
    Y_log = scipy.zeros(len(matrix))
    # N as times of the budget whether GR will be N times greater than the budget or not
    N = 8
    for i in range(0, len(matrix)):
	Y[i] = matrix[i][1]
        if Y[i] > (N * matrix[i][2]):
	    Y_log[i] = 1
        else:
	    Y_log[i] = 0
    return Y,Y_log

def test_classifier(clf, X, Y, data_points):
    val = 0.10
    for i in range(0,7):
        interval = int(data_points * val)
        X_train = X[:-interval]
        X_test = X[-interval:]

        Y_train = Y[:-interval]
        Y_test = Y[-interval:]
        print ' ****************************** \n'
        print 'Slice of test set: \n'
        print val
        clf.fit(X_train, Y_train)
        print 'Linear Regression: \n \n'
        #The Coefficients
        #print('Coefficients: \n', clf.coef_)
        #Mean Square Error
        print("Residual sum of squares: %.2f \n" % np.mean((clf.predict(X_test) - Y_test) ** 2))
        #Variance
        print('Determination Coefficient score: %.2f \n' % clf.score(X_test, Y_test))

        lasso = linear_model.Lasso()
        lasso.fit(X_train, Y_train)
        print 'Lasso Regression: \n \n'
        #The Coefficients
        #print('Coefficients: \n', lasso.coef_)
        #Mean Square Error
        print("Residual sum of squares: %.2f \n" % np.mean((lasso.predict(X_test) - Y_test) ** 2))
        #Variance
        print('Determination Coefficient score: %.2f \n' % lasso.score(X_test, Y_test))
        val = val + 0.05
    print ' ****************************** \n'
 
def log_classifier(X, Y_log, data_points):
    interval = int(data_points * 0.20)
    X_train = X[:-interval]
    X_test = X[-interval:]

    Y_train = Y_log[:-interval]
    Y_test = Y_log[-interval:]
    
    logreg = linear_model.LogisticRegression()
    logreg.fit(X_train, Y_train)
    print 'Logistic Regression: \n \n'
    #The Coefficients
    #print('Coefficients: \n', logreg.coef_)
    #Mean Square Error
    print("Residual sum of squares: %.2f \n" % np.mean((logreg.predict(X_test) - Y_test) ** 2))
    #Accuracy
    print('Accuracy score: %.2f \n' % logreg.score(X_test, Y_test))

    gauss = GaussianNB()
    gauss.fit(X_train, Y_train)
    print 'Gaussian Naive Bayes: \n \n'
    #Mean Square Error
    print("Residual sum of squares: %.2f \n" % np.mean((gauss.predict(X_test) - Y_test) ** 2))
    #Accuracy
    print('Accuracy score: %.2f \n' % gauss.score(X_test, Y_test))


def count_points(matrix):
    count = 0
    for each in matrix:
	count = count + 1
    return count

def main():
    matrix = load_matrix()
    data_points = count_points(matrix)
    print 'Total Data points in the matrix: '
    print data_points
    print ' ******************************* '
    print 'Input Matrix: '
    X = create_input(matrix)
    print X
    print ' ******************************* '
    print 'Output Matrix: '
    Y,Y_log = create_output(matrix)
    print Y
    print ' ******************************* '
    print 'Output log matrix: '
    print Y_log
    clf = linear_model.LinearRegression()
    test_classifier(clf, X, Y, data_points)
    
    log_classifier(X, Y_log, data_points)

if __name__ == '__main__':
    main()
