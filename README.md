# Predicting Concrete Strength with Machine Learning

## Background

Kekuatan beton adalah salah satu faktor penting dalam industri konstruksi. Menentukan kekuatan beton dengan baik dapat membantu kontraktor dan konsultan pembangunan untuk membuat keputusan yang lebih baik dalam merancang struktur bangunan, memilih material, dan memastikan keamanan bangunan. Namun, menguji kekuatan beton secara langsung bisa memakan waktu dan biaya yang cukup besar. Oleh karena itu, dilakukan analisa prediksi kekuatan beton menggunakan Machine Learning.

## Objective

Memprediksi Kekuatan Beton dengan dataset yang disediakan.

## Machine Learning Models

Membuat model Regresi menggunakan Regresi Linear, SVR, Decision Tree Regression, dan Random Forest Regression. Adapun pencarian Model terbaik dilakukan dengan cara menggunakan Cross-Validation.

## Evaluation

**Random Forest**

|  Metric  |        Train        |        Test        |
|:---------|--------------------:|-------------------:|
| MAE      |  1.8557452380952377 |  4.534940547263683 |
| MSE      |   6.811458656581629 |  41.33908969723881 |
| RMSE     |  2.6098771343842277 |  6.429548172091007 |

## Deployment

https://concrete-strength-prediction.streamlit.app/
