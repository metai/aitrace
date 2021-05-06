
import torch as th
from torch.utils.data import Dataset, DataLoader, TensorDataset
from torch.autograd import Variable


# ===data

x1 = th.randn((10, 3, 128, 128))
x2 = th.randn((10, 2, 128, 128))
y = th.randn((10, 128, 128))

epochs = 4

# ===DataSet

print("---Dataset")

class MyDataset(Dataset):

    def __init__(self, x1, x2, y):
        self.x1 = x1
        self.x2 = x2
        self.y = y
        self.len = y.shape[0]


    def __getitem__(self, index):
        return self.x1[index], self.x2[index], self.y[index]

    def __len__(self):
        return self.len

mydataset = MyDataset(x1, x2, y)

dataloader = DataLoader(dataset=mydataset,
    batch_size=3, shuffle=True, num_workers=2)

for epoch in range(epochs):
    print(epoch)
    for i, data in enumerate(dataloader):
        x1v, x2v, yv = data
        print(x1v.size(), x2v.size(), yv.size())


