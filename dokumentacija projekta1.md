# Dokumentacija projekta gradiska_train_test

Cilj ovog projekta je predviđanje AverageWeight koristeći različite regresione modele, nakon što je obavljen preprocesing podataka. Modeli će biti evaluirani i upoređeni na osnovu njihovih performansi na test skupu podataka.
## Dataset:
Trening dataset: df_gradiska_train_inter.csv
Test dataset: df_gradiska_test_inter.csv
Ovi skupovi podataka sadrže kolone koje će se koristiti za predviđanje AverageWeight za svaku instancu.
Koriste se sledeće kolone za obuku modela:
- AvgPixelCount
- NumberOfDaysFromStart
- PreviousWeight
Ciljana promenljiva (target) za obučavanje i testiranje je:
- AverageWeight

Preprocesing pipeline se sastoji od dva glavna koraka:
PolynomialFeatures
MinMaxScaler

## Modeli i Parametri:
Linear Regression:
Parametri: fit_intercept (True/False)

Ridge:
Parametri: alpha (0.1, 1.0, 10.0), solver (auto, svd, cholesky, lsqr), fit_intercept (True/False)

Lasso:
Parametri: alpha (0.1, 1.0, 10.0), max_iter (1000, 2000, 3000), fit_intercept (True/False)

ElasticNet:
Parametri: alpha (0.1, 1.0, 10.0), l1_ratio (0.2, 0.5, 0.8), max_iter (1000, 2000, 3000), fit_intercept (True/False)

DecisionTreeRegressor:
Parametri: criterion (mse, friedman_mse, mae), max_depth (None, 5, 10, 15), min_samples_split (2, 5, 10), min_samples_leaf (1, 5, 10)

RandomForestRegressor:
Parametri: n_estimators (50, 100, 150), max_depth (None, 10, 20), min_samples_split (2, 5, 10), min_samples_leaf (1, 5, 10)

KNeighborsRegressor:
Parametri: n_neighbors (3, 5, 7, 9), weights (uniform, distance), algorithm (auto, ball_tree, kd_tree, brute)

AdaBoostRegressor:
Parametri: n_estimators (50, 100, 200), learning_rate (0.1, 0.05, 0.02), loss (linear, square, exponential)

GradientBoostingRegressor:
Parametri: learning_rate (0.1, 0.05, 0.02), n_estimators (50, 100, 150), max_depth (3, 5, 7, 10), min_samples_split (3, 5, 10), min_samples_leaf (2, 5, 10)

## Trening i Evaluacija:
Korišćen je GridSearchCV za izbor najboljih hiperparametara za svaki model. Na osnovu najbolje kombinacije hiperparametara, model je obučen na trening podacima, a zatim su njegove performanse evaluirane na test skupu podataka pomoću Mean Absolute Error (MAE) metrike.
Za svaki model, podaci su bili procesuirani korišćenjem preprocesing pipeline-a (polinomske karakteristike i MinMax skala).
Nakon toga, rezultati modela (najbolji parametri i MAE) su bili logovani u MLflow za praćenje modela.

## Analiza Rezultata:
Na osnovu testnog skupa podataka, najbolji performanse su pokazali Linear Regression sa MAE od 18.33, što znači da je ovaj model najslabije grešio u poređenju sa drugim modelima. Sa druge strane, ElasticNet je imao najlošiji rezultat sa MAE od 58.17, što sugeriše da ovaj model nije dobro obavio predviđanja na test skupu.
Gradient Boosting Regressor takođe ima dobar rezultat sa MAE od 22.66, što ga čini jednim od konkurentnih modela, zajedno sa Decision Tree Regressor i Random Forest Regressor, koji su imali MAE od 25.63 i 27.65, respektivno.


