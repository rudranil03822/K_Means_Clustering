import random

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
        #Creating a matrix of Manhattan Distance from centroids for each point
        counter=0
        while counter<20:
            
          MD=[[0 for i in range(k)] for j in range(row)]
          for j in range(k):
            for l in range(row):
              z=centroid_Corr[j]
              y=sls[l]
              n=len(x)
              sum = 0
              for i in range(n):
                sum += abs(z[i]-y[i])
              tempDist=sum
              MD[l][j]=(tempDist)
          C=[0 for i in range(row)]
          for i in range(row):
            C[i]=MD[i].index(min(MD[i]))#we found the minimum distance and stored the index of the column in a vector C

          Y={}
          centroid_Corr = np.asarray(centroid_Corr)
          for j in range(k):
            Y[j]=[]
          for j in range(row):
            Y[C[j]].append(sls[j]) 
          for j in range(k):
            q=len(Y[j])
            for m in range(num_features_per_user):
              Sum=0
              for i in range(q):
                Sum+=Y[j][i][m]
              avg=round(Sum/q,4)
              centroid_Corr[j][m]=avg 
          counter+=1
        return centroid_Corr
      
