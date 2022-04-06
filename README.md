# Breast Cancer Analysis
This is a beginner attempt at analysis of the breast cancer dataset, with datacleaning and pre-processing and eda.

## Link
Link for the Dataset : https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data

## About Dataset and Problem Statement
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

## Contributions:
 * Ayan Mukherjee - https://github.com/atyhio9087
 * Akshat Chahuan - https://github.com/syneoxya
 * Sujay Doshi    - https://github.com/SujayD-11
