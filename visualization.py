import seaborn as sns

# Apply the default theme
sns.set_theme()

# Load dataset
data = sns.load_dataset("/data/mandi_dataset.csv")

sns.relplot(
	data = data,
	x = 'date', y = 'price', col = 'time',
	hue='smoker', style='smoker', size='size',
)
