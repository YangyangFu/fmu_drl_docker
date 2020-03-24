from __future__ import print_function

def test_torch():
    import torch
    x = torch.rand(5, 3)
    print(x)
    print("PyTorch is available and successfully working.")


if __name__ == '__main__':
    test_torch()
