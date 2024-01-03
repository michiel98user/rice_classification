import tensorflow as tf 
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense,Dropout
import scipy 

def train_model(train, valdata):
    """_summary_
    
    Args:
        arg_name (str): example variable

    Returns:
        type: description of return value
    """
    
    model = Sequential()
    model.add(Flatten(input_shape=(224, 224, 3)))  # Flatten the input images
    model.add(Dense(64, activation='relu'))
    model.add(Dropout(0.5))  # Dropout layer to reduce overfitting
    model.add(Dense(32, activation='relu'))
    model.add(Dense(5, activation='softmax')) 

    # Compile the model
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    
    # Train the model
    history = model.fit(train, epochs=3, validation_data=valdata)


    return history, model

