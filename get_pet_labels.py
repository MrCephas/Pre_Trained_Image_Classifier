#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Nnaemeka Cephas Okeke
# DATE CREATED: 02-12-2022                                  
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Retrieve the filenames from folder pet_images/
    filename_list = listdir(image_dir)
    results_dic = {}
    #populate the dictionary with keys from list, assign values for each zero
    for element in filename_list:
        results_dic[element] = results_dic.get(element, 0)
    
    
#create initial results_dic dict
    for key in results_dic:
        results_dic[key] = key
    
#create initial values list that will be modified, its in lowercase already
    values = list(results_dic.values())

    for word in values:
    #get index of word, an integer
        index_of_word = values.index(word) 
    #split word into a list of only two at last underscore
        word = word.rsplit("_", 1) 
    #discard second part of list which is at word[1],by updating word variable to word[0], thus making it a string again
        word = word[0]  
    #update word to replace "_" with " "
        word = word.replace("_", " ").strip().lower()
    #filename_list[index_of_word] returns the word with that index. results_dic
        results_dic[filename_list[index_of_word]] = [word]
    # Replace None with the results_dic dictionary that you created with this
    # function
    print(results_dic)
    return results_dic