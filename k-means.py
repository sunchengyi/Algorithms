import numpy as np

class cKMeans:

         def __init__(self, K, random_state=None, maxI=1000):
                  self.K = K
                  self.random_state = random_state
                  self.maxI = maxI

         def get_dis_cluster(self, cs, data):
                  dis = None
                  for c_i in cs:
                           tempD = np.sum((data-c_i)**2, axis=1)
                           if dis is None:
                                    dis = tempD.reshape(-1, 1)
                           else:
                                    dis = np.c_[dis, tempD]

                  sum_dis = np.sum(np.min(dis, axis=1))
                  clusterIDs = np.argmin(dis, axis=1)

                  return sum_dis, clusterIDs

         def fit(self, data):
                  data = np.array(data)
                  n = data.shape[0]

                  # inital centroids
                  if self.random_state:
                           np.random.seed(self.random_state)
                  cs = data[np.random.choice(n,self.K)]
                  total_dis, clusterIDs = self.get_dis_cluster(cs, data)

                  i = 0
                  maxI = self.maxI

                  while i < maxI:
                           
                           # new centroids
                           new_cs = []
                           for i in range(self.K):
                                    data_ID = data[clusterIDs == i]
                                    new_cs.append(np.average(data_ID, axis=0))
                           new_cs = np.array(new_cs)
                           
                           new_total_dis, new_clusterIDs = self.get_dis_cluster(new_cs, data)

                           # update
                           if new_total_dis < total_dis:
                                    total_dis, clusterIDs = new_total_dis, new_clusterIDs
                                    cs = new_cs
                           else:
                                    break
                           i += 1

                  self.clusterIDs=clusterIDs
                  self.cs = cs
                  self.data = data

         def predict(self, x):
                  x = np.array(x).reshape(-1,2)
                  _, clusterIDs = self.get_dis_cluster(self.cs, x)
                  return clusterIDs
                  
                  

if __name__ == "__main__":
         a = -1
         b = 1
         data = (b-a)*np.random.rand(500,2) + a
         
         mykmeans = cKMeans(4, 0)
         mykmeans.fit(data)
         pre1 = mykmeans.predict([1,1])
         pre2 = mykmeans.predict([[1,1], [-1,1], [-1,-1], [1,-1]])
                  
                           
         
         
