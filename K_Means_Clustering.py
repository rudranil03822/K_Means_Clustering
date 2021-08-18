import random
from scipy.spatial.distance import cityblock
import pandas as pd
import numpy as np

class Centroid:
    def __init__(self, location):
        self.location = location
        self.closest_users = set()


    def get_k_means(self,user_feature_map, num_features_per_user, k):
        # Don't change the following two lines of code.
        random.seed(42)
        # Gets the inital users, to be used as centroids.
        inital_centroid_users = random.sample(sorted(list(user_feature_map.keys())), k)

        # Write your code here.
        centroid_Corr=[]
        sls=list(user_feature_map.values())
        for i in range(k):
          x = user_feature_map[inital_centroid_users[i]]
          centroid_Corr.append(x)
        #centroid_corr gives the cordinates of randomly initialized centroids
        row=len(user_feature_map) #number of training data
        
        counter=0
        while counter<20:  #while loop to run 20 iterations
          #Creating a matrix of Manhattan Distance from centroids for each point  
          MD=[]
          
          for j in range(k):
            for l in range(row):
              tempDist=cityblock(centroid_Corr[j], sls[l])
              MD.append(tempDist)
          KD=np.asarray(MD).reshape(row,k) #matrix of Manhattan Distance 
          C=np.argmin(KD,axis=1)+1 #we found the minimum distance and stored the index of the column in a vector C
          Y={}
          centroid_Corr = np.asarray(centroid_Corr)
          for j in range(k):
            Y[j+1]=[]
          for j in range(row):
            Y[C[j]].append(x[j])
          for j in range(row):
            Y[C[j]]=np.asarray(Y[C[j]])  
          for j in range(k):
            Y[j+1]=Y[j+1].T  
          for j in range(k):
            # ky=np.mean(Y[j+1],axis=0)
            centroid_Corr[:,j]=np.mean(Y[j+1],axis=0)
          counter+=1
        return centroid_Corr
      
