# Dokumentacija opsti model
Ovaj kod implementira proces treniranja i evaluacije različitih regresionih modela koristeći više datasetova. Takođe, uključuje optimizaciju hiperparametara pomoću GridSearchCV, kao i procenu performansi modela pomoću mean absolute error (MAE) metrike. 

## Datasetovi:
Kanada Dataset (df_kanada.csv)
Gradiška Training Dataset (df_gradiska_train_inter.csv)
Portugal Dataset (df_portugal.csv)
Podaci iz različitih datasetova učitavaju se u jedan DataFrame kako bi se stvorio zajednički trening skup. Koriste se sledeće kolone za obuku modela:
- AvgPixelCount
- NumberOfDaysFromStart
- PreviousWeight
Ciljana promenljiva (target) za obučavanje i testiranje je:
- AverageWeight
Ovde je gradiskatest DataFrame koji sadrži test podatke. Kolone training_columns (AvgPixelCount, NumberOfDaysFromStart, PreviousWeight) se koriste kao ulazne karakteristike za testiranje, a AverageWeight se koristi kao ciljna promenljiva.
## Preprocessing Podataka:
Podaci se transformišu pomoću PolynomialFeatures (stepen 2) i MinMaxScaler

## Trening Modela i Optimizacija Hiperparametara:
Kod koristi različite regresione modele za predikciju ciljne promenljive AverageWeight. Za svaki model, hiperparametri se optimizuju pomoću GridSearchCV, što omogućava pretragu različitih kombinacija parametara kako bi se našla najbolja konfiguracija.

Lista korišćenih modela:
- Linear Regression
- Ridge Regression
- Lasso Regression
- ElasticNet
- Decision Tree Regressor
- Random Forest Regressor
- K-Nearest Neighbors
- AdaBoost Regressor
- Gradient Boosting Regressor

## Evaluacija Modela:
Nakon što su modeli trenirani, koristi se mean absolute error (MAE) kao metriku za evaluaciju performansi na test skupu. MAE meri prosečnu apsolutnu grešku između predikcija i stvarnih vrednosti.

## Rezultat:
Najbolji rezultati imaju RandomForestRegressor i GradientBoostingRegressor sa MAE vrednostima od 16.62 i 16.78, respektivno. Ovi modeli su najbolji u ovoj analizi na osnovu MAE.
Najgori rezultati imaju ElasticNet i AdaBoostRegressor, sa znatno višim MAE vrednostima.