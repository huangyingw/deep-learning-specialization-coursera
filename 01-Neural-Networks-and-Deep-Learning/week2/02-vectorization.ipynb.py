# coding: utf-8

# # Table of Contents
#  <p><div class="lev1 toc-item"><a href="#Vectorization" data-toc-modified-id="Vectorization-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Vectorization</a></div><div class="lev1 toc-item"><a href="#Vectorizing-Logistic-Regression" data-toc-modified-id="Vectorizing-Logistic-Regression-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Vectorizing Logistic Regression</a></div><div class="lev1 toc-item"><a href="#Vectorizing-Logistic-Regression's-Gradient-Output" data-toc-modified-id="Vectorizing-Logistic-Regression's-Gradient-Output-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Vectorizing Logistic Regression's Gradient Output</a></div><div class="lev1 toc-item"><a href="#A-note-on-python/numpy-vectors" data-toc-modified-id="A-note-on-python/numpy-vectors-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>A note on python/numpy vectors</a></div>

# # Vectorization
# ![](https://i.imgur.com/yz60bns.png)

import numpy as np


a = np.random.rand(1000000)
b = np.random.rand(1000000)


get_ipython().run_line_magic('time', 'c = np.dot(a, b)')


def loop():
    c = 0
    for i in range(1000000):
        c += a[i] * b[i]


get_ipython().run_line_magic('time', 'loop()')


# ![](https://i.imgur.com/p94lp3F.png)

# ![](https://i.imgur.com/62FCVzX.png)

# ![](https://i.imgur.com/lQnsLDn.png)

# # Vectorizing Logistic Regression
#

# ![](https://i.imgur.com/3NO1maQ.png)

# # Vectorizing Logistic Regression's Gradient Output

# ![](https://i.imgur.com/5HLkUab.png)

# # A note on python/numpy vectors

a = np.random.randn(5)
a


a.shape


a.T


np.dot(a, a.T)


a = np.random.randn(5, 1)
a


a.shape


a.T


np.dot(a, a.T)


# ![](https://i.imgur.com/RWHkYsw.png)

get_ipython().run_line_magic('load_ext', 'version_information')
get_ipython().run_line_magic('version_information', 'numpy')
