# Machine Learning and AI

## Overview

Supervised and Unsupervised learning remains foundational in many domains:

- Where data is limited
- Interpretability is crucial
- Deep learning is not needed

These models are quicker to develop and deploy and can serve as baselines.

For applications where performance is paramount and ample data is available deep learning is the go-to method.

The choice of method should be dictated by the problem, the data, and the specific requirements of the task.

| Criteria                  | Supervised Learning                                                         | Unsupervised Learning                                                      | Deep Learning                                                                                                 |
| ------------------------- | --------------------------------------------------------------------------- | -------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| **Definition**            | Algorithms trained on labeled data to predict outcomes based on input data. | Algorithms trained on unlabeled data to find patterns or structures.       | A subset of machine learning using neural networks with many layers to analyze various factors of data.       |
| **Training Data**         | Requires labeled data.                                                      | Works with unlabeled data.                                                 | Can work with both labeled and unlabeled data, but often requires large datasets.                             |
| **Goal**                  | Prediction or classification based on known outputs.                        | Data clustering, dimensionality reduction, or association.                 | Hierarchical feature extraction and pattern recognition.                                                      |
| **Examples**              | Linear Regression, Decision Trees, Support Vector Machines.                 | K-means clustering, Hierarchical clustering, Principal Component Analysis. | Convolutional Neural Networks (CNN), Recurrent Neural Networks (RNN), **Transformers** (e.g., BERT, GPT).     |
| **Use Cases**             | Image classification, stock price prediction, spam detection.               | Market segmentation, anomaly detection, topic modeling.                    | Image and speech recognition, machine translation, text generation, and more.                                 |
| **Complexity**            | Typically less complex than deep learning models.                           | Varies from simple clustering to more complex hierarchical models.         | Highly complex due to multiple layers in neural networks.                                                     |
| **Data Volume**           | Can work with smaller datasets.                                             | Can work with moderate-sized datasets.                                     | Typically requires large amounts of data for effective training.                                              |
| **Interpretability**      | Often more interpretable, especially with simpler models.                   | Varies, but some methods like clustering can be interpretable.             | Often considered a "black box" due to its complexity, making it less interpretable.                           |
| **Hardware Requirements** | Standard computing resources for most models.                               | Standard computing resources for most models.                              | Often requires specialized hardware (e.g., GPUs) for training, especially for large models like transformers. |

## Technology examples

| Criteria                            | Supervised Learning                                   | Unsupervised Learning                          | Deep Learning                                                       |
| ----------------------------------- | ----------------------------------------------------- | ---------------------------------------------- | ------------------------------------------------------------------- |
| **Technologies/Concepts**           |                                                       |                                                |                                                                     |
| Python (scikit-learn)               | ✓ (Classification, Regression, etc.)                  | ✓ (Clustering, Dimensionality Reduction, etc.) |                                                                     |
| Python (TensorFlow, PyTorch)        | ✓ (With labeled data)                                 | ✓ (With unlabeled data)                        | ✓ (CNN, RNN, Transformers, etc.)                                    |
| R                                   | ✓ (Various packages for supervised tasks)             | ✓ (Various packages for unsupervised tasks)    | Limited (Some deep learning support with packages like Keras)       |
| Spark MLlib                         | ✓ (Classification, Regression, etc.)                  | ✓ (Clustering, Dimensionality Reduction, etc.) | Limited (Basic neural networks)                                     |
| Generative AI                       |                                                       |                                                | ✓ (Generative Adversarial Networks, Variational Autoencoders, etc.) |
| AutoML Tools                        | ✓ (Automated model selection & hyperparameter tuning) | ✓ (Automated clustering, association, etc.)    | ✓ (Automated deep model selection & tuning)                         |
| Large Language Models (GPT-3, BERT) |                                                       |                                                | ✓ (Transformers-based architectures)                                |

## Neural Network characteristics

Of course! Here's the table with the characteristics as rows and the neural network types as columns:

| Central Characteristics                                                            | Convolutional Neural Networks (CNN)    | Recurrent Neural Networks (RNN) | Generative Adversarial Networks (GAN) | Transformers                                 |
| ---------------------------------------------------------------------------------- | -------------------------------------- | ------------------------------- | ------------------------------------- | -------------------------------------------- |
| Designed for specific data structure (e.g., grid-structured, sequential)           | Grid-structured data (e.g., images)    | Sequential data (e.g., text)    | Any data structure (often images)     | Sequential data                              |
| Contains specific layers or mechanisms (e.g., convolutional, recurrent, attention) | Convolutional layers                   | Recurrent loops                 | Generator & Discriminator             | Self-attention mechanism                     |
| Common challenges or issues (e.g., vanishing gradient)                             | -                                      | Vanishing/exploding gradient    | Mode collapse, training instability   | Potential for high computational cost        |
| Variants or notable subtypes                                                       | -                                      | LSTM, GRU                       | DCGAN, CycleGAN, etc.                 | BERT, GPT, T5                                |
| Common applications                                                                | Image classification, object detection | Time series, text processing    | Image generation, style transfer      | Text classification, translation, generation |
| Introduced or foundational references                                              | -                                      | -                               | -                                     | "Attention Is All You Need" paper            |

This table provides a flipped perspective, focusing on the characteristics and how they manifest or relate to each major type of neural network.
