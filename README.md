# BE-Project - API 
## Image Caption Generation and Refinement for Intelligent Tutoring Systems

#### Basic System Prerequisites:
```
Python >= 3.6
virtualenv >= 16.0.0
```

#### Fork this repo and run these commands after cloning the project and go inside the directory:
```
wget http://nlp.stanford.edu/data/wordvecs/glove.6B.zip
mkdir glove_models && mv ./glove.6B.zip ./glove_models
unzip ./glove_models/glove.6B.zip
virtualenv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 -m gensim.scripts.glove2word2vec --input  ./glove_models/glove.6B.50d.txt --output ./glove_models/glove.6B.50d.w2vformat.txt
python3 app.py
```

The API is up at [http://localhost:5000](http://localhost:5000)

#### In case of any issues with the installation of `glove_python` follow the below steps:
```
git clone https://github.com/maciejkula/glove-python.git
cd ./glove-python/glove
cython **.pyx
cython --cplus corpus_cython.pyx
cythonize **.pyx
cython ./metrics/accuracy_cython.pyx
cythonize ./metrics/accuracy_cython.pyx
cd ..
python3 setup.py cythonize
pip3 install -e .
cd ..
pip3 install -r requirements.txt
```

