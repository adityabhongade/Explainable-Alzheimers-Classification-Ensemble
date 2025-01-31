# Check versions

import numpy as np
import pandas as pd
import matplotlib
import torch
import torchvision
import timm
from PIL import Image
import tqdm
import sklearn
import joblib
import shap

versions = {
    'numpy': np.__version__,
    'pandas': pd.__version__,
    'matplotlib': matplotlib.__version__,
    'torch': torch.__version__,
    'torchvision': torchvision.__version__,
    'timm': timm.__version__,
    'Pillow': Image.__version__,
    'tqdm': tqdm.__version__,
    'scikit-learn': sklearn.__version__,
    'joblib': joblib.__version__,
    'shap' : shap.__version__
}

print(versions)

'''
Expected (or newer): 
{'numpy': '1.26.4', 'pandas': '2.2.2', 'matplotlib': '3.7.5', 'torch': '2.5.1+cu121', 'torchvision': '0.20.1+cu121', 'timm': '1.0.12', 'Pillow': '11.0.0', 'tqdm': '4.67.1', 'scikit-learn': '1.2.2', 'joblib': '1.4.2', 'shap': '0.44.1'}
'''
