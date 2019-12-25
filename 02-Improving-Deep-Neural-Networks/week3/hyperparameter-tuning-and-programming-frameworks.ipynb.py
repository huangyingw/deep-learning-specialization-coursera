# coding: utf-8

# # Table of Contents
#  <p><div class="lev1 toc-item"><a href="#Hyperparameter-tuning,-Batch-Normalization-and-Programming-Frameworks" data-toc-modified-id="Hyperparameter-tuning,-Batch-Normalization-and-Programming-Frameworks-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Hyperparameter tuning, Batch Normalization and Programming Frameworks</a></div><div class="lev2 toc-item"><a href="#Hyperparameter-Tuning" data-toc-modified-id="Hyperparameter-Tuning-11"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Hyperparameter Tuning</a></div><div class="lev3 toc-item"><a href="#Tuning-Process" data-toc-modified-id="Tuning-Process-111"><span class="toc-item-num">1.1.1&nbsp;&nbsp;</span>Tuning Process</a></div><div class="lev3 toc-item"><a href="#Using-an-appropriate-scale-to-pick-hyperparameters" data-toc-modified-id="Using-an-appropriate-scale-to-pick-hyperparameters-112"><span class="toc-item-num">1.1.2&nbsp;&nbsp;</span>Using an appropriate scale to pick hyperparameters</a></div><div class="lev3 toc-item"><a href="#Hyperparameters-tuning-in-practice:-Pandas-vs.-Caviar" data-toc-modified-id="Hyperparameters-tuning-in-practice:-Pandas-vs.-Caviar-113"><span class="toc-item-num">1.1.3&nbsp;&nbsp;</span>Hyperparameters tuning in practice: Pandas vs. Caviar</a></div><div class="lev2 toc-item"><a href="#Batch-Normalization" data-toc-modified-id="Batch-Normalization-12"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Batch Normalization</a></div><div class="lev3 toc-item"><a href="#Normalizing-activations-in-a-network" data-toc-modified-id="Normalizing-activations-in-a-network-121"><span class="toc-item-num">1.2.1&nbsp;&nbsp;</span>Normalizing activations in a network</a></div><div class="lev3 toc-item"><a href="#Fitting-Batch-Norm-into-a-neural-network" data-toc-modified-id="Fitting-Batch-Norm-into-a-neural-network-122"><span class="toc-item-num">1.2.2&nbsp;&nbsp;</span>Fitting Batch Norm into a neural network</a></div><div class="lev3 toc-item"><a href="#Why-does-Batch-Norm-work?" data-toc-modified-id="Why-does-Batch-Norm-work?-123"><span class="toc-item-num">1.2.3&nbsp;&nbsp;</span>Why does Batch Norm work?</a></div><div class="lev3 toc-item"><a href="#Batch-Norm-at-test-time" data-toc-modified-id="Batch-Norm-at-test-time-124"><span class="toc-item-num">1.2.4&nbsp;&nbsp;</span>Batch Norm at test time</a></div><div class="lev2 toc-item"><a href="#Multi-class-classificiation" data-toc-modified-id="Multi-class-classificiation-13"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>Multi-class classificiation</a></div><div class="lev3 toc-item"><a href="#Softmax-Regression" data-toc-modified-id="Softmax-Regression-131"><span class="toc-item-num">1.3.1&nbsp;&nbsp;</span>Softmax Regression</a></div><div class="lev3 toc-item"><a href="#Training-a-softmax-classifier" data-toc-modified-id="Training-a-softmax-classifier-132"><span class="toc-item-num">1.3.2&nbsp;&nbsp;</span>Training a softmax classifier</a></div><div class="lev2 toc-item"><a href="#Introduction-to-programming-frameworks" data-toc-modified-id="Introduction-to-programming-frameworks-14"><span class="toc-item-num">1.4&nbsp;&nbsp;</span>Introduction to programming frameworks</a></div><div class="lev3 toc-item"><a href="#Deep-Learning-Frameworks" data-toc-modified-id="Deep-Learning-Frameworks-141"><span class="toc-item-num">1.4.1&nbsp;&nbsp;</span>Deep Learning Frameworks</a></div><div class="lev3 toc-item"><a href="#TensorFlow" data-toc-modified-id="TensorFlow-142"><span class="toc-item-num">1.4.2&nbsp;&nbsp;</span>TensorFlow</a></div>

# # Hyperparameter tuning, Batch Normalization and Programming Frameworks

# ## Hyperparameter Tuning

# ### Tuning Process

# ![](https://i.imgur.com/2O0mJ8T.png)
# ![](https://i.imgur.com/lEofSyy.png)
# ![](https://i.imgur.com/7v591Bh.png)

# ### Using an appropriate scale to pick hyperparameters

# ![](https://i.imgur.com/hMkBqQN.png)

# ![](https://i.imgur.com/7WWzABh.png)

# ### Hyperparameters tuning in practice: Pandas vs. Caviar
#

# ![](https://i.imgur.com/gZC1piD.png)

# ## Batch Normalization

# ### Normalizing activations in a network

# ![](https://i.imgur.com/rO2u0HS.png)
# ![](https://i.imgur.com/YH9xVsw.png)

# ### Fitting Batch Norm into a neural network

# ![](https://i.imgur.com/ydulxtV.png)

# ![](https://i.imgur.com/Wg5nU2o.png)

# ![](https://i.imgur.com/Bs9ccPQ.png)

# ### Why does Batch Norm work?

# ![](https://i.imgur.com/BOR7g8y.png)
# ![](https://i.imgur.com/OZRyg65.png)
# ![](https://i.imgur.com/VSx8NnH.png)

# ### Batch Norm at test time

# ![](https://i.imgur.com/ygXa3oQ.png)

# ## Multi-class classificiation

# ### Softmax Regression

# ![](https://i.imgur.com/caXsKOu.png)
# ![](https://i.imgur.com/7FQzzin.png)
# ![](https://i.imgur.com/TJJMNH4.png)

# ### Training a softmax classifier

# ![](https://i.imgur.com/AVGvLhZ.png)
# ![](https://i.imgur.com/B1sXWXh.png)
# ![](https://i.imgur.com/B1sXWXh.png)

# ## Introduction to programming frameworks

# ### Deep Learning Frameworks

# ![](https://i.imgur.com/96m8cmt.png)

# ### TensorFlow

import tensorflow as tf
import numpy as np


w = tf.Variable(0, dtype=tf.float32)
cost = tf.add(tf.add(w**2, tf.multiply(-10., w)), 25)


train = tf.train.GradientDescentOptimizer(0.01).minimize(cost)


init = tf.global_variables_initializer()


session = tf.Session()


get_ipython().run_line_magic('time', 'session.run(init)')


print(session.run(w))


get_ipython().run_line_magic('time', 'session.run(train)')


get_ipython().run_line_magic('time', 'print(session.run(w))')


get_ipython().run_line_magic('load_ext', 'version_information')
get_ipython().run_line_magic('version_information', 'tensorflow, numpy')
