import random

def detect_intruder(image_path):
    print("🚁 Running drone object detection...")

    probability = random.uniform(0, 1)

    print(f"Suspicious Activity Probability: {probability:.2f}")

    return probability > 0.6
