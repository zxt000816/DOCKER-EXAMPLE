import torch

def happy():
    if torch.cuda.is_available():
        print("Happy!")