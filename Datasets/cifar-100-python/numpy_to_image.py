from PIL import Image
import pickle
import numpy as np


with open('trees_train_data_CIFAR_100.pickle', 'rb') as file:
    imageCount = 1
    for data in pickle.load(file):

        img_R = data[0:1024].reshape((32, 32))
        img_G = data[1024:2048].reshape((32, 32))
        img_B = data[2048:3072].reshape((32, 32))
        img = np.dstack((img_R, img_G, img_B))

        # imsave(os.path.join(PIXELS_DIR, fname), img)

        save_img = Image.fromarray(img, 'RGB')
        save_img.save('tree' + str(imageCount) + '.png')
        imageCount += 1
        # img.show()
