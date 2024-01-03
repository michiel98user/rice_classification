from src.data.make_dataset import make_dataset
from src.models.train_model import train_model
from src.models.predict_model import predict_model


"""
Main script of the project to run the entire pipeline. Example of docstring in Google style.
"""


def main(arg: bool = True) -> bool:
    """Summary line.

    Extended description of function.

    Args:
        arg (bool): Description of arg

    Returns:
        bool: Description of return value
    """
    train, valdata = make_dataset()
    
    history, model = train_model(train, valdata)
    
    predict_model(history, model, valdata)
    
    return arg


if __name__ == "__main__":
    main()
