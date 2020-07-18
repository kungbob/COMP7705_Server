# Backend Server For Cat2Anime

The server is based on Flask.

## Setup

### For Windows

1. Install Python (Ensure version is above 3.6)

2. Install venv
'''Python
py -m pip install --user virtualenv
'''

3. Enter Virtual Enviornment
```Script
.\venv\Scripts\activate
```

4. Install Pytorch
```
pip install torch===1.5.1 torchvision===0.6.1 -f https://download.pytorch.org/whl/torch_stable.html
```

5. Install Scipy
```
pip install numpy scipy matplotlib ipython jupyter pandas sympy nose
```

6. Install Opencv-python
```
pip install opencv-python
```

7. Run Flask
```
flask run
```