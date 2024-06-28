# HealthInsuranceCostPrediction

It is extremely important to predict the health insurance cost for every individual so in this project, I have used several features of a person to predict their insurance cost.

About Dataset: This dataset is taken from Kaggle: https://www.kaggle.com/datasets/mirichoi0218/insurance

This dataset has following columns:
> - **age:** age of primary beneficiary
> - **sex:** insurance contractor gender, female, male
> - **bmi:** Body mass index, providing an understanding of body, weights that are relatively high or low relative to height, objective index of body weight (kg / m ^ 2) using the ratio of height to weight, ideally 18.5 to 24.9
> - **children:** Number of children covered by health insurance / Number of dependents
> - **smoker:** Smoking
> - **region:** the beneficiary's residential area in the US, northeast, southeast, southwest, northwest.
> - **charges:** Individual medical costs billed by health insurance

Since the objective of this project is to predict the insurance cost, it is a Regression problem so I tried Linear Regression, Support Vector Regressor, Random Forest Regressor, and Gradient Boosting Regressor. Out of them, Gradient Boosting Regressor performed the best with the least mean absolute error.
