python code:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = "small_sided_games_dataset.csv"
df = pd.read_csv(file_path)

def classify_scene(row):
    scene_type = "Indoor" if row['Game_Setting'].lower() == 'indoor' else "Outdoor"
    people_present = "With People" if row['Number_of_Players'] > 0 or row['Crowd_Presence'] > 0 else "Without People"
    return f"{scene_type} - {people_present}"

df['Scene_Category'] = df.apply(classify_scene, axis=1)

plt.figure(figsize=(8,3))
sns.countplot(x='Scene_Category', data=df, palette='viridis')
plt.xticks(rotation=45)
plt.title('Scene-Based Video Segmentation Categories')
plt.xlabel('Scene Category')
plt.ylabel('Count')
plt.show()

df.to_csv("categorized_scenes.csv", index=False)
df_filtered = df[['Game_Setting', 'Crowd_Presence']]

df_filtered['Indoor'] = df_filtered['Game_Setting'].apply(lambda x: 1 if x == 'Indoor' else 0)
df_filtered['People_Present'] = df_filtered['Crowd_Presence'].apply(lambda x: 1 if x > 0 else 0)

df_filtered.head()

indoor_scenes = df_filtered[df_filtered['Indoor'] == 1]
print("Indoor Scenes:")
print(indoor_scenes.head())

outdoor_scenes = df_filtered[df_filtered['Indoor'] == 0]
print("Outdoor Scenes:")
print(outdoor_scenes.head())

people_present_scenes = df_filtered[df_filtered['People_Present'] == 1]
print("Scenes with People Present:")
print(people_present_scenes.head())

no_people_scenes = df_filtered[df_filtered['People_Present'] == 0]
print("Scenes without People Present:")
print(no_people_scenes.head())

data = {
    "Game_Setting": ["Indoor", "Indoor", "Indoor", "Indoor", "Outdoor"],
    "Number_of_Players": [6, 6, 8, 8, 6],
    "Crowd_Presence": [50, 50, 100, 10, 10]
}

df = pd.DataFrame(data)

def classify_scene(row):
    scene_type = "Indoor" if row['Game_Setting'].lower() == 'indoor' else "Outdoor"
    
    people_present = "With People" if row['Number_of_Players'] > 0 or row['Crowd_Presence'] > 0 else "Without People"
    
    return f"{scene_type} - {people_present}"

df['Scene_Category'] = df.apply(classify_scene, axis=1)

print(df)

data = {
    "Game_Setting": ["Indoor", "Indoor", "Indoor", "Indoor", "Outdoor", "Outdoor"],
    "Number_of_Players": [6, 0, 8, 0, 6, 0],
    "Crowd_Presence": [50, 0, 100, 0, 10, 0]
}

df = pd.DataFrame(data)

def classify_scene_without_people(row):
    scene_type = "Indoor" if row['Game_Setting'].lower() == 'indoor' else "Outdoor"
    people_present = "Without People" if row['Number_of_Players'] == 0 and row['Crowd_Presence'] == 0 else None
    return f"{scene_type} - {people_present}" if people_present else None

df['Scene_Category'] = df.apply(classify_scene_without_people, axis=1)

df_without_people = df.dropna()

print(df_without_people)

df_filtered.to_csv("processed_data.csv", index=False)
