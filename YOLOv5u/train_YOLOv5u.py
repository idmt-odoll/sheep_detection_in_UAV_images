from ultralytics import YOLO
import torch

epochs = 100
save_period = 10
# load and train models

print("\n\n####   n-Modell   ####\n\n")
model_n = YOLO("yolov5nu.pt")
model_n.train(data="config_v5u.yaml", epochs=epochs, name="v5_nu", save_period=save_period, patience=100, batch=16)
torch.cuda.empty_cache()

print("\n\n####   s-Modell   ####\n\n")
model_s = YOLO("yolov5su.pt")
model_s.train(data="config_v5u.yaml", epochs=epochs, name="v5_su", save_period=save_period, patience=100, batch=14)
torch.cuda.empty_cache()

print("\n\n####   m-Modell   ####\n\n")
model_m = YOLO("yolov5mu.pt")
model_m.train(data="config_v5u.yaml", epochs=epochs, name="v5_mu", save_period=save_period, patience=100, batch=12)
torch.cuda.empty_cache()

print("\n\n####   l-Modell   ####\n\n")
model_l = YOLO("yolov5lu.pt")
model_l.train(data="config_v5u.yaml", epochs=epochs, name="v5_lu", save_period=save_period, patience=100, batch=8)
torch.cuda.empty_cache()

print("\n\n####   x-Modell   ####\n\n")
model_x = YOLO("yolov5xu.pt")
model_x.train(data="config_v5u.yaml", epochs=epochs, name="v5_xu", save_period=save_period, patience=100, batch=6)
print("\nFinished")