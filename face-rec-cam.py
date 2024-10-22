# terminal to activate the profile
source ~/.bash_profile

# Crop face from an input image
python src/align_dataset_mtcnn.py  Dataset/FaceData/raw Dataset/FaceData/processed --image_size 160 --margin 32  --random_order --gpu_memory_fraction 0.25

# Train model
python src/classifier.py TRAIN Dataset/FaceData/processed Models/20180402-114759.pb Models/facemodel.pkl --batch_size 1000

# Face verification
python src/face_verification.py  Models/20180402-114759.pb 'Dataset/FaceData/processed/Nhat/idcard_front.png' 'Dataset/FaceData/processed/Nhat/nhat4.png'

