import torch
import torch.nn as nn
import numpy as np

batch_size = 128
n_z = 62

z = torch.randn(batch_size, n_z, 1, 1)

print(z)