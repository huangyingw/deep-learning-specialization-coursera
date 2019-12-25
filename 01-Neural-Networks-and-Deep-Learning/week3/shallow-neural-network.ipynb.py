# coding: utf-8

# # Table of Contents
#  <p><div class="lev1 toc-item"><a href="#Neural-Networks-Overview" data-toc-modified-id="Neural-Networks-Overview-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Neural Networks Overview</a></div><div class="lev1 toc-item"><a href="#Neural-Network-Representation" data-toc-modified-id="Neural-Network-Representation-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Neural Network Representation</a></div><div class="lev1 toc-item"><a href="#Computing-a-Neural-Network's-Output" data-toc-modified-id="Computing-a-Neural-Network's-Output-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Computing a Neural Network's Output</a></div><div class="lev1 toc-item"><a href="#Vectorizing-across-multiple-examples" data-toc-modified-id="Vectorizing-across-multiple-examples-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Vectorizing across multiple examples</a></div><div class="lev1 toc-item"><a href="#Explanation-for-Vectorized-Implementation" data-toc-modified-id="Explanation-for-Vectorized-Implementation-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Explanation for Vectorized Implementation</a></div><div class="lev1 toc-item"><a href="#Activation-functions" data-toc-modified-id="Activation-functions-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Activation functions</a></div><div class="lev1 toc-item"><a href="#Why-do-you-need-non-linear-activation-functions?" data-toc-modified-id="Why-do-you-need-non-linear-activation-functions?-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>Why do you need non-linear activation functions?</a></div><div class="lev1 toc-item"><a href="#Derivatives-of-activation-functions" data-toc-modified-id="Derivatives-of-activation-functions-8"><span class="toc-item-num">8&nbsp;&nbsp;</span>Derivatives of activation functions</a></div><div class="lev2 toc-item"><a href="#Sigmoid-activation-Function" data-toc-modified-id="Sigmoid-activation-Function-81"><span class="toc-item-num">8.1&nbsp;&nbsp;</span>Sigmoid activation Function</a></div><div class="lev2 toc-item"><a href="#Tanh-activation-Function" data-toc-modified-id="Tanh-activation-Function-82"><span class="toc-item-num">8.2&nbsp;&nbsp;</span>Tanh activation Function</a></div><div class="lev2 toc-item"><a href="#Relu-and-Leaky-Relu-activation-Functions" data-toc-modified-id="Relu-and-Leaky-Relu-activation-Functions-83"><span class="toc-item-num">8.3&nbsp;&nbsp;</span>Relu and Leaky Relu activation Functions</a></div><div class="lev1 toc-item"><a href="#Gradient-descent-for-Neural-Networks" data-toc-modified-id="Gradient-descent-for-Neural-Networks-9"><span class="toc-item-num">9&nbsp;&nbsp;</span>Gradient descent for Neural Networks</a></div><div class="lev1 toc-item"><a href="#Backpropagation-intuition" data-toc-modified-id="Backpropagation-intuition-10"><span class="toc-item-num">10&nbsp;&nbsp;</span>Backpropagation intuition</a></div><div class="lev1 toc-item"><a href="#Random-Initialization" data-toc-modified-id="Random-Initialization-11"><span class="toc-item-num">11&nbsp;&nbsp;</span>Random Initialization</a></div>

# # Neural Networks Overview
#

# ![](https://i.imgur.com/4yfM07L.png)

# # Neural Network Representation
#

# ![](https://i.imgur.com/kyl6x26.png)

# # Computing a Neural Network's Output

# ![](https://i.imgur.com/wQlhl87.png)

# ![](https://i.imgur.com/ihsKJ4Z.png)

# ![](https://i.imgur.com/KAatjCr.png)

# # Vectorizing across multiple examples

# ![](https://i.imgur.com/0iDEAN7.png)

# ![](https://i.imgur.com/InoZItP.png)

# # Explanation for Vectorized Implementation

# ![](https://i.imgur.com/JgIaS9c.png)

# ![](https://i.imgur.com/xhgzY4B.png)

# # Activation functions

# ![](https://i.imgur.com/aGQaUie.png)
#
# **some rules of thumb for choosing activation functions:**
# - if your output is 0 1 value if you're I'm using binary classification then the sigmoid activation function is very natural for the upper layer and then for all other units on varalu or the rectified linear unit is increasingly the default choice of activation function so if you're not sure what to use, I would just use the relu activation function that's what you see most people using these days although sometimes people also use the tannish activation function once this advantage of the value is that the derivative is equal to zero when V is negative in practice this works just fine but there is another version of the value called the least G value will give you.
#
# ![](https://i.imgur.com/DDpGVCh.png)

# # Why do you need non-linear activation functions?

# ![](https://i.imgur.com/fpn6NdA.png)

# # Derivatives of activation functions

# - when you implement back-propagation for your neural network you need to really compute the slope or the derivative of the activation functions. so
#     - let's take a look at our choices of activation functions and
#     - how you can compute the slope of these functions
#

# ## Sigmoid activation Function
# ![](https://i.imgur.com/hnNpKAk.png)

# ## Tanh activation Function
# ![](https://i.imgur.com/6j7Q5FO.png)

# ## Relu and Leaky Relu activation Functions
# ![](https://i.imgur.com/Uuj8XzK.png)

# # Gradient descent for Neural Networks

# ![](https://i.imgur.com/OI08zkX.png)
#
# ![](https://i.imgur.com/GrayIZ0.png)

# # Backpropagation intuition

# ![](https://i.imgur.com/7v0bsl8.png)
# ![](https://i.imgur.com/5sRIZ0N.png)
# ![](https://i.imgur.com/gJtMEjF.png)
# ![](https://i.imgur.com/J4y00XB.png)

# # Random Initialization

# ![](https://i.imgur.com/cxIjPvj.png)

# ![](https://i.imgur.com/Y1GNtUj.png)
