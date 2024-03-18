from vit import ViTRegressionPredictor


def eval_vit():
    vit = ViTRegressionPredictor(data_file='./data/24-03-17.xlsx', image_dir='./data/room_images/', batch_size=16)
    y = 'rate_76d'
    vit.train(target_key=y, test_size=0.1, epochs=5)
    vit.eval(target_key=y)

if __name__ == "__main__":
    eval_vit()
