import matplotlib.pyplot as plt

def predict_model(history, model, valdata):
    """_summary_
    
    Args:
        arg_name (str): example variable

    Returns:
        type: description of return value
    """
    # Evaluate the model on the validation set
    val_loss, val_accuracy = model.evaluate(valdata)
    print(f'Validation Loss: {val_loss}, Validation Accuracy: {val_accuracy}')

    # Plot training and validation accuracy
    plt.plot(history.history['accuracy'], label='Training Accuracy')
    plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
    plt.xlabel('Epochs')
    plt.ylabel('Accuracy')
    plt.legend()
    plt.show()
    
    return 0
