# Machine learning expert

## Summary

| Criteria                  | Supervised Learning                                                         | Unsupervised Learning                                                      | Deep Learning                                                                                           |
| ------------------------- | --------------------------------------------------------------------------- | -------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| **Definition**            | Algorithms trained on labeled data to predict outcomes based on input data. | Algorithms trained on unlabeled data to find patterns or structures.       | A subset of machine learning using neural networks with many layers to analyze various factors of data. |
| **Training Data**         | Requires labeled data.                                                      | Works with unlabeled data.                                                 | Can work with both labeled and unlabeled data, but often requires large datasets.                       |
| **Goal**                  | Prediction or classification based on known outputs.                        | Data clustering, dimensionality reduction, or association.                 | Hierarchical feature extraction and pattern recognition.                                                |
| **Examples**              | Linear Regression, Decision Trees, Support Vector Machines.                 | K-means clustering, Hierarchical clustering, Principal Component Analysis. | Convolutional Neural Networks (CNN), Recurrent Neural Networks (RNN), Autoencoders.                     |
| **Use Cases**             | Image classification, stock price prediction, spam detection.               | Market segmentation, anomaly detection, topic modeling.                    | Image and speech recognition, machine translation, game playing (e.g., AlphaGo).                        |
| **Complexity**            | Typically less complex than deep learning models.                           | Varies from simple clustering to more complex hierarchical models.         | Highly complex due to multiple layers in neural networks.                                               |
| **Data Volume**           | Can work with smaller datasets.                                             | Can work with moderate-sized datasets.                                     | Typically requires large amounts of data for effective training.                                        |
| **Interpretability**      | Often more interpretable, especially with simpler models.                   | Varies, but some methods like clustering can be interpretable.             | Often considered a "black box" due to its complexity, making it less interpretable.                     |
| **Hardware Requirements** | Standard computing resources for most models.                               | Standard computing resources for most models.                              | Often requires specialized hardware (e.g., GPUs) for training, especially for large models.             |

This table provides a concise overview of the key differences and characteristics of supervised, unsupervised, and deep learning methods.

## Crash course

### Supervised learning

Naive Bayes
Naive Bayes Optimized
Performance techniques
K-nearest Neighbors
Decision Tree
Linear Regression
Logistics regression
Support Vector Machine

This table provides a concise overview of each topic's principles and features in the context of supervised learning.

| Topic                      | Essential Principles                                                                              | Key Features                                                                                    |
| -------------------------- | ------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| **Naive Bayes**            | Based on Bayes' theorem with the assumption of independence between features.                     | - Probabilistic classification. <br> - Works well with high-dimensional datasets.               |
| **Naive Bayes Optimized**  | Improvements on the basic Naive Bayes to enhance performance or accuracy.                         | - Feature selection. <br> - Parameter tuning.                                                   |
| **Performance Techniques** | Methods to evaluate and improve the accuracy and efficiency of models.                            | - Cross-validation. <br> - Precision, Recall, F1 Score. <br> - ROC curve, AUC.                  |
| **K-nearest Neighbors**    | Classify based on the majority class of 'k' closest data points.                                  | - Non-parametric. <br> - Lazy learner (no explicit training phase).                             |
| **Decision Tree**          | Tree-like model of decisions. Nodes represent tests on attributes; leaves represent class labels. | - Can handle both categorical & numerical data. <br> - Prone to overfitting.                    |
| **Linear Regression**      | Predict continuous values based on linear relationships between variables.                        | - Assumes linear relationship. <br> - Coefficient determination (R^2) measures goodness of fit. |
| **Logistic Regression**    | Predict probabilities of categorical outcomes using a logistic function.                          | - Binary or multinomial classification. <br> - Outputs probabilities.                           |
| **Support Vector Machine** | Find the hyperplane that best divides a dataset into classes.                                     | - Effective in high-dimensional spaces. <br> - Uses kernel trick for non-linear data.           |

### Unsupervised Learning

K-Means
Singular Value Decomposition

| Topic                                  | Essential Principles                                                                               | Key Features                                                                                                                                                           |
| -------------------------------------- | -------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **K-means**                            | Partitioning method that divides a dataset into K distinct, non-overlapping subsets (or clusters). | - Iterative algorithm. <br> - Minimizes within-cluster variance. <br> - Requires specifying the number of clusters (K) beforehand.                                     |
| **Singular Value Decomposition (SVD)** | Factorization technique that decomposes a matrix into three other matrices.                        | - Used for dimensionality reduction. <br> - Commonly used in recommendation systems (e.g., collaborative filtering). <br> - Captures the underlying structure in data. |

### Deep Learning

Neural Networks
Convolutional Neural Networks
Recurrent Neural Networks
Generative Adversarial Networks

### Recommender Systems

### Ranking
