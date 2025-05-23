import torch
import torch.nn as nn

class StudentUNet_MultiResUNet(nn.Module):
    def __init__(self, in_channels=3, out_channels=2):
        super(StudentUNet_MultiResUNet, self).__init__()
        self.encoder = nn.Sequential(
            nn.Conv2d(in_channels, 32, 3, padding=1), nn.ReLU(),
            nn.Conv2d(32, 64, 3, padding=1), nn.ReLU()
        )
        self.pool = nn.MaxPool2d(2)
        self.decoder = nn.Sequential(
            nn.Conv2d(64, 64, 3, padding=1), nn.ReLU(),
            nn.ConvTranspose2d(64, out_channels, 2, stride=2)
        )

    def forward(self, x):
        x = self.encoder(x)
        x = self.pool(x)
        x = self.decoder(x)
        return x
