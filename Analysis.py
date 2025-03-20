import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import chi2_contingency, f_oneway
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report

# Load data
observations = pd.read_csv("data/observations.csv")
species = pd.read_csv("data/species_info.csv")

# Merge datasets
biodiversity = observations.merge(species, on="scientific_name", how="left")
biodiversity["conservation_status"].fillna("Not Listed", inplace=True)

# Chi-Square Test
contingency = pd.crosstab(biodiversity["category"], biodiversity["conservation_status"])
chi2, p, _, _ = chi2_contingency(contingency)
print(f"Chi-Square Test: chi2={chi2}, p-value={p}")

# ANOVA Test
parks = biodiversity["park_name"].unique()
observations_per_park = [biodiversity[biodiversity["park_name"] == park]["observations"] for park in parks]
anova_stat, anova_p = f_oneway(*observations_per_park)
print(f"ANOVA Test: F-stat={anova_stat}, p-value={anova_p}")

# Visualization
plt.figure(figsize=(10,5))
sns.countplot(data=biodiversity, x="category", order=biodiversity["category"].value_counts().index)
plt.xticks(rotation=45)
plt.title("Species Count by Category")
plt.show()

# Machine Learning Model
biodiversity["is_endangered"] = biodiversity["conservation_status"].apply(lambda x: 1 if x in ["Endangered", "Threatened", "Species Of Concern", "In Recovery"] else 0)
label_encoders = {}
for col in ["category", "park_name"]:
    le = LabelEncoder()
    biodiversity[col] = le.fit_transform(biodiversity[col])
    label_encoders[col] = le

X = biodiversity[["category", "park_name", "observations"]]
y = biodiversity["is_endangered"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

print("Model Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))
