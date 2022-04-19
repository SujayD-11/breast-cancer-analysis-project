# Breast Cancer Analysis
This is a beginner attempt at analysis of the breast cancer dataset, with datacleaning and pre-processing and basic classification model development (Logisitic Regression).

## Link
Link for the Dataset : https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data

## About Dataset and Problem Statement
Breast cancer is the most common malignancy among women, accounting for nearly 1 in 3 cancers diagnosed among women in the United States, and it is the second leading cause of cancer death among women. Breast Cancer occurs as a results of abnormal growth of cells in the breast tissue, commonly referred to as a Tumor. A tumor does not mean cancer - tumors can be benign (not cancerous), pre-malignant (pre-cancerous), or malignant (cancerous).

Our dataset is about breast cancer information gathered using fine needle aspirate - A procedure to check for breast cancer. They describe characteristics of the cell nuclei present in the image. The ultimate objective would be to predict if the cancer is benign or malignant. Benign stage is where the tumor (cell cluster) isnt a threat and invades other tissues. When it becomes abnormal and parasitic, its called malignant.

The 3-dimensional space is that described in: [K. P. Bennett and O. L. Mangasarian: "Robust Linear Programming Discrimination of Two Linearly Inseparable Sets", Optimization Methods and Software 1, 1992, 23-34].

This database is also available through the UW CS ftp server:
ftp ftp.cs.wisc.edu
cd math-prog/cpo-dataset/machine-learn/WDBC/

Also can be found on UCI Machine Learning Repository: https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+%28Diagnostic%29

## Attribute Information:

* ID number
* Diagnosis (M = malignant, B = benign)

Ten real-valued features are computed for each cell nucleus:

 * radius (mean of distances from center to points on the perimeter)
 * texture (standard deviation of gray-scale values)
 * perimeter
 * area
 * smoothness (local variation in radius lengths)
 * compactness (perimeter^2 / area - 1.0)
 * concavity (severity of concave portions of the contour)
 * concave points (number of concave portions of the contour)
 * symmetry
 * fractal dimension ("coastline approximation" - 1)

The mean, standard error and "worst" or largest (mean of the three
largest values) of these features were computed for each image,
resulting in 30 features. For instance, field 3 is Mean Radius, field
13 is Radius SE, field 23 is Worst Radius.

All feature values are recoded with four significant digits.

## Objective and About our Work
Scince the target attribute - "diagnosis" has discrete values & the predication falls into two categories this can be stated as a Binary Classification Problem and a normal classifier model can be used.
After analysis, Logistic regression has been used on this dataset.

## Contributions:
 * Ayan Mukherjee - https://github.com/atyhio9087
 * Akshat Chahuan - https://github.com/syneoxya
 * Sujay Doshi    - https://github.com/SujayD-11
