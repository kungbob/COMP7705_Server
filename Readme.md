# Backend Server For Cat2Anime

The server is based on Flask.

## Setup

If there is no database setup, please change the branch to non-sql branch. DB connection and functions are removed in the non-sql branch.

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

7. Install flask
```
pip install flask
```

8. Install flask cors
```
pip install flask-cors
```

9. Install Flask SQLALCHEMY
```
pip install Flask-SQLAlchemy
```

10. Install Python dotenv
```
pip install python-dotenv
```

7. Run Flask
```
flask run
```
