
# coding: utf-8

# In[3]:


import numpy as np
import random
import os


# In[2]:


DATA_PATH = 'data/prepared_data/'


# In[37]:


class Data:
    def __init__(self):
        self.X_counter = 0
        self.file_counter = 0
        
        self.files = [file for file in os.listdir(DATA_PATH) if file.endswith('.npy')]
        random.shuffle(self.files)
        
        self._load_data()            ## store in self.X at starting
        
    def _load_data(self):
        self.X = []
        datas = np.load(os.path.join(DATA_PATH, self.files[self.file_counter]))
        for data in datas:
            self.X.append(data)
        random.shuffle(self.X)
        self.X = np.asarray(self.X)
        self.file_counter += 1
        
#     def get_data(self, batch_size):             # don't support batch_size > len(X)
#         if self.X_counter >= len(self.X):
#             if self.file_counter > len(self.files) - 1:
#                 print("Data exhausted, Re Initialize")
#                 self.__init__()
#                 return None
#             else:
#                 self._load_data()
#                 self.X_counter = 0
        
#         if self.X_counter + batch_size <= len(self.X):
#             X = self.X[self.X_counter : self.X_counter + batch_size]
#         else:
#             X = self.X[self.X_counter : ]
        
#         self.X_counter += batch_size
        
#         return X
    
    def get_data(self, batch_size):               # supports batch_size > len(X)
        X = []
        while(batch_size):
            if self.X_counter >= len(self.X):
                if self.file_counter > len(self.files) - 1:
                    print("Data exhausted, Re Initialize")
                    self.__init__()
                    return None
                else:
                    self._load_data()
                    self.X_counter = 0

            if self.X_counter + batch_size <= len(self.X):
                X.extend(self.X[self.X_counter : self.X_counter + batch_size])
                self.X_counter += batch_size
                break
            else:
                X.extend(self.X[self.X_counter : ])

            self.X_counter += batch_size
            batch_size = self.X_counter - len(self.X)

        X = np.asarray(X)
        return X

