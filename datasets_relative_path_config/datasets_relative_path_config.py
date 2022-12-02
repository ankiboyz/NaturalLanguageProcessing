# The dictionary containing the key and value of the path identifier 
# and the relative path of the dataset to the main repository.
# This config is used in the get_dataset method to navigate to the actual dataset passing in the ID for the dataset.

id_dataset_dict = {'NLP_VOCAB_BUILDER' : {'PATH': "datasets/EAWE01.csv", # The path relative to the main repository, not including the starting slash.
                                          'NAME': "Educational Attainment and Wage Equations (EAWE)",
                                          'DESCR': "A tagged dataset taken from the Wall Street Journal for Educational purposes. \
                                                   "
                              },
                   
                  }
