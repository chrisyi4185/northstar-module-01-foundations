# generate northwoodfresh_data.py 
# Module 1 Project
# Author: A. Chris Yi
# Date: 2024-10-05
#
# Generates a synthetic dataset of 48 monthly sales results (4 regions x 12 months)

import numpy as np
import pandas as pd

np.random.seed(42)

baselines = {
    "Northeast": {"before": 520000, "after": 520000},
    "Midwest": {"before": 510000, "after": 510000},
    "Southeast": {"before": 480000, "after": 370000},
    "West": {"before": 590000, "after": 590000},
}

data = []

for region, periods in baselines.items():
    for month in range(1, 13):

        if month <= 6:
            current_baseline = periods["before"]
        else:
            current_baseline = periods["after"]

        std_dev = current_baseline * 0.05

        revenue = np.random.normal(
            loc=current_baseline,
            scale=std_dev
        )

        data.append({
            "region": region,
            "month": month,
            "revenue": revenue
        })

northwoodfresh_data = pd.DataFrame(data)

northwoodfresh_data["revenue"] = pd.to_numeric(
    northwoodfresh_data["revenue"],
    errors="coerce"
)

northwoodfresh_data["revenue"] = northwoodfresh_data["revenue"].round(2)

print(northwoodfresh_data.head(13))

print("\nData types:")
print(northwoodfresh_data.dtypes)

output_path = "northwoodfresh_data.csv"
northwoodfresh_data.to_csv(output_path, index=False)

print(f"\nDataset saved to {output_path}")

