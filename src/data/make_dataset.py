import os, sys
sys.path.insert(1, 'C:/Users/MichielWelling/rice classification')

from configs.paths import FILE_PATH_RAW, FOLDER_DATA_RAW
from tensorflow.keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array

def make_dataset():
    """Execute data preprocessing pipeline

    Runs data processing scripts to turn raw data from (../raw) into
    cleaned data ready to be analyzed (saved in ../processed).

    Args:
        arg_name (str): example variable

    Returns:
        type: description of return value
    """
    # # Get a list of subdirectories (each subdirectory corresponds to a class)
    # class_folders = [f.name for f in os.scandir(FOLDER_DATA_RAW) if f.is_dir()]

    # img_size = 224
    batch_size =64
    # fpath = "/kaggle/input/rice-image-dataset/Rice_Image_Dataset"
    datagen = ImageDataGenerator(rescale=1/255.,
                                zoom_range=0.2,
                                validation_split = 0.2,
                                rotation_range=30,
                                horizontal_flip=True)

    # splitting to train and test
    train = datagen.flow_from_directory(FILE_PATH_RAW,
                                    target_size=(224,224),
                                    subset="training",
                                    class_mode='categorical',
                                    batch_size=batch_size)
    valdata = datagen.flow_from_directory(FILE_PATH_RAW,
                                    target_size=(224,224),
                                    batch_size=64,
                                    subset='validation',
                                    class_mode='categorical')   
    
    
    return train, valdata
