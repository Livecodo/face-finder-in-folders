import os
import face_recognition
import cv2
import numpy as np


your_image_path = 'D:\\Livecodo\\Face-recognization\\IMG_1153.jpg'  # Replace with your image path
your_image = face_recognition.load_image_file(your_image_path)
your_face_encodings = face_recognition.face_encodings(your_image)

if not your_face_encodings:
    print("❌ No face found in your known image. Please use a clearer photo.")
    exit()

your_face_encoding = your_face_encodings[0]


output_dir = 'found_faces'
os.makedirs(output_dir, exist_ok=True)
print("✅ Output folder:", os.path.abspath(output_dir))

# Path to the folder containing photos
photos_folder = 'D:\\Livecodo\\memories'  # Change if needed

for root, dirs, files in os.walk(photos_folder):
    for filename in files:
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            photo_path = os.path.join(root, filename)
            print(f"🔍 Processing: {photo_path}")


            try:
                image = face_recognition.load_image_file(photo_path)
                face_encodings = face_recognition.face_encodings(image)
            except Exception as e:
                print(f"⚠️ Error loading {filename}: {e}")
                continue

            if not face_encodings:
                print("   ⚠️ No faces found.")
                continue

            for face_encoding in face_encodings:
                distance = face_recognition.face_distance([your_face_encoding], face_encoding)[0]
                print(f"   ➤ Face distance: {distance:.4f}")

                if distance < 0.6:  # Adjust tolerance if needed
                    output_path = os.path.join(output_dir, filename)
                    cv2.imwrite(output_path, cv2.cvtColor(image, cv2.COLOR_RGB2BGR))
                    print(f"   ✅ Match found! Saved: {output_path}")
                    break

print("🎉 Face detection complete. Check the 'found_faces' folder.")
