import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# CSV File Loading
df = pd.read_csv("Car_sales.csv")

# Grouping Data
model_sales = df.groupby(
    "Model")["Sales_in_thousands"].sum().sort_values(ascending=False)

# Matplotlib Bar Chart
plt.figure(figsize=(10, 6))
model_sales.head(10).plot(kind="bar", color="skyblue")
plt.title("Top 10 Best-Selling Car Models")
plt.xlabel("Car Model")
plt.ylabel("Sales (in thousands)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Plotly Pie Chart
fig = px.pie(
    values=model_sales.head(10),
    names=model_sales.head(10).index,
    title="Sales Distribution of Top 10 Car Models",
    hole=0.3
)
fig.show()
