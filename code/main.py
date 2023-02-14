import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from tools.happy import happy 
from tools.hello_world import hello_world 

hello_world()
happy()

print(torch.__version__)

# check gpu
print(torch.cuda.is_available())

# check gpu name
print(torch.cuda.get_device_name(0))

# check gpu memory
print(torch.cuda.memory_allocated())

# create a linear regression model
class LinearRegression(nn.Module):
    def __init__(self):
        super(LinearRegression, self).__init__()
        self.linear = nn.Linear(1, 1)
    
    def forward(self, x):
        out = self.linear(x)
        return out
    
# create a dataset
x = torch.randn(100, 1)
y = 2*x + 3 + torch.randn(100, 1)

# create a model
model = LinearRegression()

# create a loss function
criterion = nn.MSELoss()

# create a optimizer
optimizer = optim.SGD(model.parameters(), lr=1e-3)

# train the model
for epoch in range(100):
    # forward
    out = model(x)
    loss = criterion(out, y)
    
    # backward
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    
    # print loss
    if (epoch+1) % 20 == 0:
        print('Epoch[{}/{}], loss: {:.6f}'.format(epoch+1, 100, loss.item()))

# save the model
torch.save(model.state_dict(), './model.pth')

