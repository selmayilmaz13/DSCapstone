import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import r2_score, mean_absolute_error
import torch
import torch.nn as nn
import torch.optim as optim
import os

base_dir = os.path.dirname(__file__)
data_path = os.path.join(base_dir, "..", "..", "Datasets", "ai_job_trends_dataset.csv")

df = pd.read_csv(data_path)

for col in df.select_dtypes(include=["object", "string"]).columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])

X = df.drop("Automation Risk (%)", axis=1)
y = df["Automation Risk (%)"]

X_train_full, X_test, y_train_full, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
X_train, X_val, y_train, y_val = train_test_split(X_train_full, y_train_full, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_val = scaler.transform(X_val)

X_train = torch.tensor(X_train, dtype=torch.float32)
y_train = torch.tensor(y_train.values, dtype=torch.float32).view(-1,1)

X_val = torch.tensor(X_val, dtype=torch.float32)
y_val = torch.tensor(y_val.values, dtype=torch.float32).view(-1,1)

model = nn.Sequential(
    nn.Linear(X_train.shape[1], 128),
    nn.ReLU(),
    nn.Dropout(0.3),
    nn.Linear(128, 64),
    nn.ReLU(),
    nn.Dropout(0.3),
    nn.Linear(64, 1)
)

criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001, weight_decay=1e-4)

train_losses = []
val_losses = []
train_acc = []
val_acc = []

for epoch in range(200):
    model.train()
    optimizer.zero_grad()
    outputs = model(X_train)
    loss = criterion(outputs, y_train)
    loss.backward()
    optimizer.step()

    with torch.no_grad():
        model.eval()
        val_outputs = model(X_val)
        val_loss = criterion(val_outputs, y_val)

        train_losses.append(loss.item())
        val_losses.append(val_loss.item())

        train_accuracy = (torch.abs(outputs - y_train) <= 10).float().mean().item()
        val_accuracy = (torch.abs(val_outputs - y_val) <= 10).float().mean().item()

        train_acc.append(train_accuracy)
        val_acc.append(val_accuracy)

        val_r2 = r2_score(y_val.numpy(), val_outputs.numpy())
        val_mae = mean_absolute_error(y_val.numpy(), val_outputs.numpy())

        print("Epoch:", epoch,
              "| Train Acc:", train_accuracy,
              "| Val Acc:", val_accuracy,
              "| Val R2:", val_r2,
              "| Val MAE:", val_mae)

baseline_pred = torch.full_like(y_val, y_train.mean())
baseline_mae = mean_absolute_error(y_val.numpy(), baseline_pred.numpy())
print("Baseline MAE:", baseline_mae)


# plt.figure()
# plt.plot(train_losses)
# plt.plot(val_losses)
# plt.xlabel("Epoch")
# plt.ylabel("Loss")
# plt.legend(["Train", "Validation"])
# plt.savefig('Code/Deep Learning/Loss.png')

# plt.figure()
# plt.plot(train_acc)
# plt.plot(val_acc)
# plt.xlabel("Epoch")
# plt.ylabel("Accuracy (±10)")
# plt.legend(["Train", "Validation"])
# plt.savefig('Code/Deep Learning/Accuracy.png')

df.groupby("Job Title")["Automation Risk (%)"].nunique().sort_values(ascending=False).head()
print(df.corr(numeric_only=True)["Automation Risk (%)"].sort_values(ascending=False))
