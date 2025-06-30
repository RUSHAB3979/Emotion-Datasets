import os
import shutil

source_dir = 'jaffe'  # Path to extracted JAFFE
target_dir = 'jaffe_sorted'

emotion_map = {
    'AN': 'angry',
    'HA': 'happy',
    'SA': 'sad',
    'FE': 'fear',
    'DI': 'disgust',
    'SU': 'surprise',
    'NE': 'neutral'
}

os.makedirs(target_dir, exist_ok=True)

for file in os.listdir(source_dir):
    if file.endswith(".tiff"):
        for code, emotion in emotion_map.items():
            if f".{code}" in file:
                emotion_folder = os.path.join(target_dir, emotion)
                os.makedirs(emotion_folder, exist_ok=True)
                shutil.copy(os.path.join(source_dir, file), os.path.join(emotion_folder, file))
                break
