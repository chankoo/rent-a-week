import torch
import torch.nn as nn
from transformers import ViTModel, ViTConfig
from sklearn.model_selection import train_test_split
from utils.data import RentImgDataset, RentImgDataLoader


class ViTRegressionPredictor(object):
    train_dataset = None
    test_dataset = None
    dataset_class = RentImgDataset
    dataloader_class = RentImgDataLoader

    def __init__(self, data_file:str, image_dir:str, batch_size:int=32):
        # ViT 모델 정의
        config = ViTConfig.from_pretrained('google/vit-base-patch16-224-in21k')
        config.num_labels = 1  # 회귀 모델이므로 출력 레이블 수를 1로 설정합니다.
        self.model = ViTModel(config)
        self.regression_layer = nn.Linear(config.hidden_size, 1) # 회귀 레이어 추가
        self.model.add_module("regression", self.regression_layer)
        
        self.criterion = nn.MSELoss()
        self.optimizer = torch.optim.Adam(self.model.parameters(), lr=1e-4)
        self.batch_size = batch_size

        # data 세팅
        self.dataset = self.dataset_class(data_file, image_dir)
        
    def train(self, target_key:str, test_size:float, random_state:int=42, epochs:int=5):
        self.train_dataset, self.test_dataset = train_test_split(self.dataset, test_size=test_size, random_state=random_state)
        train_loader = self.dataloader_class(self.train_dataset, batch_size=self.batch_size, shuffle=True)

        self.model.train()
        for epoch in range(epochs):
            running_loss = 0.0
            for _, rent_infos, image_sets in train_loader:
                # 입력 이미지 세트의 평균값 계산
                image_sets = [torch.stack(image_set, dim=0) for image_set in image_sets]
                image_means = torch.stack([image_set.mean(dim=0) for image_set in image_sets], dim=0)

                # train
                self.optimizer.zero_grad()
                outputs = self.model(image_means).last_hidden_state.mean(dim=1)  # 이미지 임베딩의 평균을 사용합니다.
                predictions = self.regression_layer(outputs)
                targets = torch.Tensor([rent_info[target_key] for rent_info in rent_infos]).view(-1, 1)
                loss = self.criterion(predictions, targets)
                loss.backward()
                self.optimizer.step()
                running_loss += loss.item() * self.batch_size
            
            epoch_loss = running_loss / len(self.dataset)
            print(f"Epoch {epoch+1}/{epochs}, Loss: {epoch_loss:.4f}")
    
    def eval(self, target_key:str):    
        test_loader = self.dataloader_class(self.test_dataset, batch_size=self.batch_size, shuffle=False)
        self.model.eval()

        predictions_list = []
        real_list = []
        with torch.no_grad():
            for _, rent_infos, image_sets in test_loader:
                # 입력 이미지 세트의 평균값 계산
                image_means = torch.stack([torch.stack(image_set, dim=0).mean(dim=0) for image_set in image_sets], dim=0)

                # 모델에 입력 데이터를 전달하여 예측값 획득
                outputs = self.model(image_means).last_hidden_state.mean(dim=1)
                predictions = self.regression_layer(outputs)

                # 예측 결과를 리스트에 추가
                predictions_list.extend(predictions.tolist())
                real_list.extend([rent_info[target_key] for rent_info in rent_infos])
        
        print("Predictions:", predictions_list)
        print("real_list:", real_list)
