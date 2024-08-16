import torch 
print(torch.cuda.is_available())
print(f"Number of GPus: {torch.cuda.device_count()}")
print(f"GPU Name: {torch.cuda.get_device_name(0)}")
