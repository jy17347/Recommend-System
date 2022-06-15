import pandas as pd
import numpy as np

def load_dataset(data):
    dataset_dir = "C:/project/kwix/curation/dataset/movielens"
    loaded_dataset = pd.read_csv(dataset_dir +'/' + data + '.csv')
    
    if data in ['user', 'test/user']:
        loaded_user = loaded_dataset.to_numpy()
        return loaded_user
    
    else:
        exercise_list = np.array(loaded_dataset.columns[1:],dtype = int)
        loaded_dataset = loaded_dataset.to_numpy()[:,1:]
        return exercise_list, loaded_dataset


def get_trainset(user_profile, exercise, labeling):
    user_input, item_input, labels = [],[],[]
        
    for i in range(len(user_profile[:,0])):
        for j in range(len(exercise)):
            user_input.append(user_profile[i,:])
            item_input.append(exercise[j])
            if labeling[i,j]>2.5:
                labels.append(1)
            else:
                labels.append(0)
    
    return np.array(user_input), np.array(item_input), np.array(labels)


def scaler_user(user_dataset):

    user_dataset = user_dataset[:,1:].astype(np.float64)

    return user_dataset