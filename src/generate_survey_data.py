import pandas as pd
import numpy as np

np.random.seed(42)

n = 1000

data = pd.DataFrame({
    "customer_id": np.arange(1, n+1),
    "nps_score": np.random.randint(0, 11, n),
    "customer_effort_score": np.random.randint(1, 6, n),
    "satisfaction_score": np.random.randint(1, 6, n),
    "interaction_channel": np.random.choice(
        ["web", "mobile_app", "call_center", "branch"],
        n
    ),
    "complaint_flag": np.random.choice([0,1], n, p=[0.8,0.2])
})

data.to_csv("data/raw/customer_survey.csv", index=False)

print("Survey dataset created")