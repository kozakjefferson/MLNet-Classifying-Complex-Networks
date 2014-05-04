#!/usr/bin/python
# marina von steinkirch @2014
# steinkirch at gmail

''' This program shows the application of svm for sampled '''


import sklearn.svm  as sklsvm
import numpy as np
from constants import  SAMPLINGS_SETS, PERCENTAGE
import bio
import tech 
import info 
import social



INPUT_FILE = ['all_neat', 'all_neat_n1500', 'all_neat_n2000', "entire_net"]#,  'all_neat_n500', 'all_neat_n3000',"sampled"]



def save_result_final(final, output_file):
    ''' Save in a file the final result '''

    with open(output_file, "w") as f:
        for i in range(len(final)):
            f.write(str(final[i]) + ',' + str(i+1) + "\n")


def fit_model(data, truth):
    #model = sklsvm.LinearSVC() # better
    model = sklsvm.SVC()

    model = model.fit(data, truth) 
    return model


def probability(model, data):
    print model.predict_proba(data)


def classify_data(model, data, truth):
    guesses = model.predict(data)
    right = np.sum(guesses == truth)
    return float(right) / truth.shape[0]
    


def main():
   
    '''
        INFO networks
    '''
    OUT = '../output/INFO'

    print 'Starting info nets...'


    for net_type in INPUT_FILE:
        for NUM_SETS  in SAMPLINGS_SETS:
	    aver_error_train = []
            aver_error_test = []

            # run  for all datasets
            for i in range(NUM_SETS):

                print 'Calculating for nsets ', i

                DATA_TRAIN = '../data/' + net_type + '/' + str(NUM_SETS) + '/train_' + str(i) + "_.data"
                DATA_TEST  = '../data/' + net_type + '/' + str(NUM_SETS) +'/test_' + str(i) + "_.data"

                # HERE IS THE DIFFERENCE FOR EACH NET
                learn_data_X, learn_data_Y = info.load_data(DATA_TRAIN)
                predict_data_X, predict_data_Y = info.load_data(DATA_TEST)

                # classifier
                model = fit_model(learn_data_X, learn_data_Y)
                accuracy_train  = classify_data(model, learn_data_X, learn_data_Y) 
                accuracy_test = classify_data(model, predict_data_X, predict_data_Y)
                                       
                aver_error_train.append(accuracy_train)    
                aver_error_test.append(accuracy_test)    

            # save to file to plot
            print 'Saving final files ...'  
            OUTPUT_FILE_TRAIN = OUT + '_train_' + net_type + str(NUM_SETS) + '_.data' 
            OUTPUT_FILE_TEST =  OUT + '_test_'   + net_type + str(NUM_SETS) + '_.data' 
            
            save_result_final(aver_error_train, OUTPUT_FILE_TRAIN)
            save_result_final(aver_error_test, OUTPUT_FILE_TEST)



    '''
        tech networks
    '''
    OUT = '../output/TECH'

    print 'Starting tech nets...'


    for net_type in INPUT_FILE:
        for NUM_SETS  in SAMPLINGS_SETS:
	    aver_error_train = []
    	    aver_error_test = []

            # run  for all datasets
            for i in range(NUM_SETS):

                print 'Calculating for nsets ', i

                DATA_TRAIN = '../data/' + net_type + '/' + str(NUM_SETS) + '/train_' + str(i) + "_.data"
                DATA_TEST  = '../data/' + net_type + '/' + str(NUM_SETS) +'/test_' + str(i) + "_.data"

                # HERE IS THE DIFFERENCE FOR EACH NET
                learn_data_X, learn_data_Y = tech.load_data(DATA_TRAIN)
                predict_data_X, predict_data_Y = tech.load_data(DATA_TEST)

                # classifier
                model = fit_model(learn_data_X, learn_data_Y)
                accuracy_train = classify_data(model, learn_data_X, learn_data_Y) 
                accuracy_test = classify_data(model, predict_data_X, predict_data_Y)
                                       
                aver_error_train.append(accuracy_train)    
                aver_error_test.append(accuracy_test)    

            # save to file to plot
            print 'Saving final files ...'  
            OUTPUT_FILE_TRAIN = OUT + '_train_' + net_type + str(NUM_SETS) + '_.data' 
            OUTPUT_FILE_TEST =  OUT + '_test_'   + net_type + str(NUM_SETS) + '_.data' 
            
            save_result_final(aver_error_train, OUTPUT_FILE_TRAIN)
            save_result_final(aver_error_test, OUTPUT_FILE_TEST)


    '''
        SOCIAL networks
    '''
    OUT = '../output/SOCIAL'

    print 'Starting social nets...'



    for net_type in INPUT_FILE:
        for NUM_SETS  in SAMPLINGS_SETS:
	    aver_error_train = []
            aver_error_test = []

            # run  for all datasets
            for i in range(NUM_SETS):

                print 'Calculating for nsets ', i

                DATA_TRAIN = '../data/' + net_type + '/' + str(NUM_SETS) + '/train_' + str(i) + "_.data"
                DATA_TEST  = '../data/' + net_type + '/' + str(NUM_SETS) +'/test_' + str(i) + "_.data"

                # HERE IS THE DIFFERENCE FOR EACH NET
                learn_data_X, learn_data_Y = social.load_data(DATA_TRAIN)
                predict_data_X, predict_data_Y = social.load_data(DATA_TEST)

                # classifier
                model = fit_model(learn_data_X, learn_data_Y)
                accuracy_train = classify_data(model, learn_data_X, learn_data_Y) 
                accuracy_test = classify_data(model, predict_data_X, predict_data_Y)
                                       
                aver_error_train.append(accuracy_train)    
                aver_error_test.append(accuracy_test)    

            # save to file to plot
            print 'Saving final files ...'  
            OUTPUT_FILE_TRAIN = OUT + '_train_' + net_type + str(NUM_SETS) + '_.data' 
            OUTPUT_FILE_TEST =  OUT + '_test_'   + net_type + str(NUM_SETS) + '_.data' 
            
            save_result_final(aver_error_train, OUTPUT_FILE_TRAIN)
            save_result_final(aver_error_test, OUTPUT_FILE_TEST)





    '''
        BIO networks
    '''
    OUT = '../output/BIO'

    print 'Starting bio nets...'

 
    for net_type in INPUT_FILE[:-2]:
        for NUM_SETS  in SAMPLINGS_SETS:
	    aver_error_train = []
            aver_error_test = []

            # run  for all datasets
            for i in range(NUM_SETS):

                print 'Calculating for nsets ', i

                DATA_TRAIN = '../data/' + net_type + '/' + str(NUM_SETS) + '/train_' + str(i) + "_.data"
                DATA_TEST  = '../data/' + net_type + '/' + str(NUM_SETS) +'/test_' + str(i) + "_.data"

                # HERE IS THE DIFFERENCE FOR EACH NET
                learn_data_X, learn_data_Y = bio.load_data(DATA_TRAIN)
                predict_data_X, predict_data_Y = bio.load_data(DATA_TEST)

                # classifier
                model = fit_model(learn_data_X, learn_data_Y)
                accuracy_train = classify_data(model, learn_data_X, learn_data_Y) 
                accuracy_test = classify_data(model, predict_data_X, predict_data_Y)
                                       
                aver_error_train.append(accuracy_train)    
                aver_error_test.append(accuracy_test)    

            # save to file to plot
            print 'Saving final files ...'  
            OUTPUT_FILE_TRAIN = OUT + '_train_' + net_type + str(NUM_SETS) + '_.data' 
            OUTPUT_FILE_TEST =  OUT + '_test_'   + net_type + str(NUM_SETS) + '_.data' 
            
            save_result_final(aver_error_train, OUTPUT_FILE_TRAIN)
            save_result_final(aver_error_test, OUTPUT_FILE_TEST)




    print 'Done!!!'




if __name__ == '__main__':
    main()
