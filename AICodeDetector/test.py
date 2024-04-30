import torch

# GPUが利用可能かどうかを確認
if torch.cuda.is_available():
    # CUDAデバイスの初期化
    torch.cuda.init()
    print("CUDA is available and initialized.")
    # 利用可能なCUDAデバイスの数と、デフォルトデバイスを表示
    print(f"Number of CUDA devices: {torch.cuda.device_count()}")
    print(f"Current CUDA device: {torch.cuda.current_device()}")

    # CUDAデバイス情報の取得
    device = torch.device('cuda')
    print(torch.cuda.get_device_properties(device))
else:
    print("CUDA is not available.")
