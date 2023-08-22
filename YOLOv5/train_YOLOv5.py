import train
import torch

epochs = 100
save_period = 10
# load and train models

print("\n\n####   n-Modell   ####\n\n")
train.run(data="config_v5.yaml", epochs=epochs, save_dir="v5_n", save_period=save_period, batch_size=64, weights="yolov5n.pt")
torch.cuda.empty_cache()

print("\n\n####   s-Modell   ####\n\n")
train.run(data="config_v5.yaml", epochs=epochs, save_dir="v5_s", save_period=save_period, batch_size=40, weights="yolov5s.pt")
torch.cuda.empty_cache()

print("\n\n####   m-Modell   ####\n\n")
train.run(data="config_v5.yaml", epochs=epochs, save_dir="v5_m", save_period=save_period, batch_size=24, weights="yolov5m.pt")
torch.cuda.empty_cache()

print("\n\n####   l-Modell   ####\n\n")
train.run(data="config_v5.yaml", epochs=epochs, save_dir="v5_l", save_period=save_period, batch_size=16, weights="yolov5l.pt")
torch.cuda.empty_cache()

print("\n\n####   x-Modell   ####\n\n")
train.run(data="config_v5.yaml", epochs=epochs, save_dir="v5_x", save_period=save_period, batch_size=10, weights="yolov5x.pt")
print("\nFinished")