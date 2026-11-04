import os 
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.dummy import DummyRegressor
from sklearn.linear_model import LinearRegression 
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score 

dossier = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(dossier, "..", "donnees", "voitures_nettoyees.csv"))

y = df["selling_price"]
X = df.drop(columns=["selling_price"])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
reference = DummyRegressor(strategy="mean")

reference.fit(X_train, y_train)   
pred_reference = reference.predict(X_test) 
print(pred_reference[:5])

model = LinearRegression()
model.fit(X_train,y_train )
pred_model = model.predict(X_test)

print(pred_model[:5])
print(y_test[:5].values)

mae_model = mean_absolute_error(y_test, pred_model)
mae_reference = mean_absolute_error(y_test, pred_reference)
r2_reference = r2_score(y_test, pred_reference)
mae_model = mean_absolute_error(y_test, pred_model)
r2_model = r2_score(y_test, pred_model)

print(f"Référence (moyenne)  : MAE = {mae_reference:,.0f} roupies, R² = {r2_reference:.3f}")
print(f"Régression linéaire  : MAE = {mae_model:,.0f} roupies, R² = {r2_model:.3f}")