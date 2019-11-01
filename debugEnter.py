from src.bin.train import run

if __name__ == '__main__':
    run(
        model_name="Transformer",
        reload=True,
        config_path="./configs/d2d-small_tvsub_zh2en.yaml",
        log_path="./log/",
        saveto="./save/"
    )