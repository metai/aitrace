import torch as th
from torch.utils.data import Dataset, DataLoader, TensorDataset
from torch.autograd import Variable


# ===data

x1 = th.randn((10, 3, 128, 128))
x2 = th.randn((10, 2, 128, 128))
y = th.randn((10, 128, 128))

epochs = 4

# ===TensorDataSet

print("---TensorDataset")
mydataset = TensorDataset(x1, x2, y)

dataloader = DataLoader(dataset=mydataset,
                        batch_size=3, shuffle=True, num_workers=2)

# epoch = 0
for epoch in range(epochs):
    print(epoch)
    for i, data in enumerate(dataloader):
        x1v, x2v, yv = data
        print(x1v.size(), x2v.size(), yv.size())
