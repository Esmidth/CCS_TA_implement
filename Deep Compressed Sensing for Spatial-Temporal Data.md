# Deep Compressed Sensing for Spatial-Temporal Data

## Traditional Compressed Sensing

- More with less
  - Data Structure Conversion (Data Martix)
  - Base Training (learning)
    - K-SVD
  - Sampling
    - Passively
    - Pro-Actively
  - Reconstruction
    - OMP
    - L1-norm minimization
- CCS-TA
  - Salient
  - LOOSI

## Deep Compressed Sensing for CV
- Bora 2017 Compressed Sensing with Generative Model (CSGM)
- DCS
  - Compressed Sensing with Meta-Learning
  - Deep Compressed Sensing with Learned Mesurement Function
    - Learning Mesurement Function
      - Generator Model: latent representation z, G(z) = x
      - Mesurement Matrix: F(G(z)) = m
      - G, F 都是NN（准确来说都是 MLP
    - CS-GAN
      - GAN: latent representation z, G(z) = x
    - CS-SGAN (Semi-Supervised GANs)

## Progress

- Python Library
  - Tensorflow
    - CS-GAN implemented by DeepMind
  - Pytorch
    - fundemental reconstruction
  - CVXPY
    - a python library for convex optimization problem
- Dataset
  - Rat Infestion
  - Noise Heatmap
- Progess
  - Rat infestion
    - Read csv file
    - Data Structure Conversion
      - Divide NYC map into 100 cells
      - count rat infestion number in each cell for each month
    - Attempt to train measurement matrix
      - Pytorch Gradient Des
        - Loss -> ((pred-real)**2).sum()
        - Loss -> l1_loss(pred,real)
      - CVX convex optim
        - Measurement Matrix -> DCT(random)


## Confusion

- Model-Agnostic Meta Learning ？？

- Python Convex Library -> Deep Learning Library or others

- Data Structure Conversion -> Construction Method

- Data Reconstruction Precision -> for faking data usage`

- 量化相关性

  

