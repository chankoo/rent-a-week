import os
from PIL import Image

from torch.utils.data import Dataset, DataLoader
import torchvision.transforms as transforms
import pandas as pd


rent_transform = transforms.Compose(
    [
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
    ]
)


class RentImgDataset(Dataset):
    id_col_name = "rid"

    def __init__(self, data_file: str, image_dir: str, transform=rent_transform):
        super(RentImgDataset, self).__init__()
        self.data = pd.read_excel(data_file, engine="openpyxl")
        self.image_dir = image_dir
        self.transform = transform

        mask = (self.data["sigungu"] == "서울특별시 강남구") & (self.data["건물 유형"] == "오피스텔")
        self.room_ids = self.data.loc[mask][self.id_col_name].to_list()
        # self.room_ids = sorted(os.listdir(image_dir)) # 모든 이미지 사용

    def __len__(self):
        return len(self.room_ids)

    def __getitem__(self, idx):
        room_id = self.room_ids[idx]
        rent_info = self.data.loc[self.data[self.id_col_name] == int(room_id)]

        room_dir = os.path.join(self.image_dir, str(room_id))
        image_files = sorted(os.listdir(room_dir))
        images = []
        for image_file in image_files:
            img_path = os.path.join(room_dir, image_file)
            image = Image.open(img_path)
            if self.transform:
                image = self.transform(image)
            images.append(image)
        return {
            self.id_col_name: room_id,
            "images": images,
            "rent_info": rent_info.iloc[0].to_dict() if not rent_info.empty else {},
        }


class RentImgDataLoader(DataLoader):
    def __init__(self, *args, **kwargs):
        super(RentImgDataLoader, self).__init__(*args, **kwargs)
        self.collate_fn = image_collate_fn


def image_collate_fn(batch):
    rids = [item["rid"] for item in batch]
    rent_infos = [item["rent_info"] for item in batch]
    images = [item["images"] for item in batch]
    return rids, rent_infos, images
