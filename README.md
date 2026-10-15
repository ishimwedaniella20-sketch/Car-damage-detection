# Car Damage Detection

## 1. The Project
This project finds damage on car photos. A user uploads a photo and the app draws boxes on the damage and names it (broken, dent or scratch). I built it for my Machine Learning course.

Steps I followed: collect the data, split it, train a CNN model, deploy with Flask on Render, and show the results with graphs.

## 2. The Model
I trained a YOLOv8 OBB model (`yolov8n-obb`). It looks at a photo and finds damage in one pass. "OBB" means it draws tilted boxes that fit the damage better than straight boxes. The final model is saved as `best.pt`.

## 3. The Dataset
- Source: Car Damage Detection dataset from Roboflow (YOLOv8-OBB format)
- Classes: broken, dent, scratch
- Images: train [ ], valid 404, test [ ]
- Each image has a label file that tells the model where the damage is.

## 4. Splitting, Training and Evaluation
**Splitting:** The data came already split into three folders:
- train: the model learns from these
- valid: checks the model while it learns
- test: new photos used at the end

**Training:** I used transfer learning. I started with a model that was already trained on many images, then trained it on my car damage photos.
- Epochs: 30
- Image size: 640
- Hardware: free T4 GPU on Google Colab

**Feature engineering and extraction:** The CNN does this by itself. Its first layers find edges and textures, and its deeper layers find shapes like dents and scratches.

**Evaluation:** I used precision, recall, mAP50, the loss graphs and the confusion matrix. The model was also tested on the test photos.
**Results (on the validation set, 404 images):**
- Precision: 0.51
- Recall: 0.42
- mAP50: 0.43
- mAP50-95: 0.21

| Damage | Precision | Recall | mAP50 |
|---|---|---|---|
| broken | 0.60 | 0.55 | 0.58 |
| dent | 0.46 | 0.36 | 0.36 |
| scratch | 0.47 | 0.36 | 0.36 |

Speed: about 5 ms per image.

## 5. The Algorithm
I used YOLOv8 OBB. It is a CNN (Convolutional Neural Network). YOLO means "You Only Look Once": it finds and names all the damage in one pass, so it is fast.

## 6. How I Deployed It
1. Saved the trained model (`best.pt`).
2. Wrote a Flask app (`app.py`) with a page to upload a photo.
3. Put the files on GitHub.
4. Connected the repo to Render, which runs the app with gunicorn and gives a public link.

Live link: [add your Render link]

## 7. Limitations
- The dataset is small, so the model can miss damage or make mistakes.
- It only knows 3 types of damage.
- It does not tell how bad the damage is or how much the repair costs.
- Bad light, dirty cars, reflections and odd angles lower accuracy.
- The free Render plan is slow and sleeps when not used.

## 8. How It Helps the Community
- Gives a fast, cheap first check of car damage.
- Helps buyers of used cars see damage before they pay.
- Helps insurance companies and garages check claims faster.
- Reduces fights over damage on rental cars and in accidents.

## 9. How It Can Make Money
- Charge garages, insurers and car rental companies a monthly fee.
- Charge per photo checked.
- Sell it as an API that other apps can use.
- Partner with garages: the app finds the damage, and the garage gets the repair job.
- Later, add repair cost estimates as a paid feature.

## Files
- `app.py`: the Flask website
- `best.pt`: the trained model
- `requirements.txt`: the libraries needed
- `notebook.ipynb`: my Colab training notebook

## Author
Ishimwe Mwambutsa Daniella
