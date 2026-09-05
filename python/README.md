# 🐍 Python for Data Analysis

## Standard Workflow

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('data.csv')

# Inspect
print(df.shape)
print(df.head())
print(df.info())
print(df.isna().sum())
print(df.duplicated().sum())

# Basic statistics
print(df.describe(include='all'))

# Example aggregation
summary = (
    df.groupby('category', as_index=False)['sales']
      .sum()
      .sort_values('sales', ascending=False)
)
```

## EDA Checklist
1. Understand the business question.
2. Inspect rows, columns and data types.
3. Check missing values.
4. Check duplicates.
5. Validate ranges and categorical values.
6. Identify outliers.
7. Explore distributions.
8. Compare important segments.
9. Analyze correlations carefully.
10. Translate findings into business insights.

## Good Practices
- Keep raw data unchanged.
- Create a cleaned dataset when appropriate.
- Use meaningful variable names.
- Avoid hard-coded assumptions.
- Add comments where business logic is not obvious.
- Make notebooks readable from top to bottom.
- Save important charts and tables for project documentation.
