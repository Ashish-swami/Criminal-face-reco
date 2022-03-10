import os
from random import shuffle
from tqdm import tqdm
def my_data():
    data = []
    for img in tqdm(os.listdir("/datasets")):
        path=os.path.join("/datasets",img)
        img_data = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        img_data = cv2.resize(img_data, (50,50))
        data.append([np.array(img_data), my_label(img)])
    shuffle(data)  
    return data
