from ultralytics import YOLO
import torch

epochs = 100
save_period = 10
# load and train models

print("\n\n####   n-Modell   ####\n\n")
model_n = YOLO("yolov8n.pt")
model_n.train(data="config_v8.yaml", epochs=epochs, name="v8_n", save_period=save_period, patience=100) # batch = 16
torch.cuda.empty_cache()

print("\n\n####   s-Modell   ####\n\n")
model_s = YOLO("yolov8s.pt")
model_s.train(data="config_v8.yaml", epochs=epochs, name="v8_s", save_period=save_period, patience=100) # batch=16
torch.cuda.empty_cache()

print("\n\n####   m-Modell   ####\n\n")
model_m = YOLO("yolov8m.pt")
model_m.train(data="config_v8.yaml", epochs=epochs, name="v8_m", save_period=save_period, patience=100, batch=12)
torch.cuda.empty_cache()

print("\n\n####   l-Modell   ####\n\n")
model_l = YOLO("yolov8l.pt")
model_l.train(data="config_v8.yaml", epochs=epochs, name="v8_l", save_period=save_period, patience=100, batch=8)
torch.cuda.empty_cache()

print("\n\n####   x-Modell   ####\n\n")
model_x = YOLO("yolov8x.pt")
model_x.train(data="config_v8.yaml", epochs=epochs, name="v8_x", save_period=save_period, patience=100, batch=6)
print("\nFinished")
