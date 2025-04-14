import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1. Import data
df = pd.read_csv("medical_examination.csv")

# 2. Add 'overweight' column
df['BMI'] = df['weight'] / ((df['height'] / 100) ** 2)
df['overweight'] = (df['BMI'] > 25).astype(int)
df.drop(columns='BMI', inplace=True)

# 3. Normalize data by making 0 good and 1 bad
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# 4. Draw Categorical Plot
def draw_cat_plot():
    # 5. Create DataFrame for cat plot using `pd.melt`
    df_cat = pd.melt(df, 
                     id_vars=['cardio'],
                     value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # 6. Group and reformat data
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']) \
                   .size().reset_index(name='total')

    # 7. Draw the catplot
    fig = sns.catplot(data=df_cat, kind='bar',
                      x='variable', y='total', hue='value',
                      col='cardio').fig

    return fig

# 8. Draw Heat Map
def draw_heat_map():
    # 9. Clean the data
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # 10. Calculate the correlation matrix
    corr = df_heat.corr()

    # 11. Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 12. Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 10))

    # 13. Draw the heatmap
    sns.heatmap(corr, mask=mask, annot=True, fmt=".1f", center=0,
                square=True, linewidths=.5, cbar_kws={"shrink": .5})

    return fig