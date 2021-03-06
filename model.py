import torch
import torch.nn as nn
import torch.nn.functional as F

nclasses = 43 # GTSRB as 43 classes

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(3, 32, kernel_size=5,padding=2)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=5,padding=2)
        self.conv2_drop = nn.Dropout2d(p=0.1)
        self.conv2_bn=nn.BatchNorm2d(64)
        self.conv3 = nn.Conv2d(64, 128, kernel_size=5,padding=2)
        self.conv3_drop = nn.Dropout2d(p=0.3)
        self.conv3_bn=nn.BatchNorm2d(128)
        self.fc1 = nn.Linear(2048, 128)
        self.fc2 = nn.Linear(128, nclasses)

    def forward(self, x):
        x = F.relu(F.max_pool2d(self.conv1(x),2))
        x = F.relu(F.max_pool2d(self.conv2_drop(self.conv2_bn(self.conv2(x))), 2))
        x = F.relu(F.max_pool2d(self.conv3_drop(self.conv3_bn(self.conv3(x))), 2))
        x = x.view(-1, 128*4*4)
        x = F.relu(self.fc1(x))
        x = F.dropout(x, training=self.training)
        x = self.fc2(x)
        
        return F.log_softmax(x)
