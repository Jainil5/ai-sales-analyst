import numpy as np
import json
import torch
from torch import nn  # Import nn from torch directly
from torch.utils.data import Dataset, DataLoader
from spacy_utils import bag_of_words, tokenize, lemmatize
from model import NeuralNet

# Load intents from JSON
with open('backend/product_model/product_intents.json', 'r') as f:
    intents = json.load(f)

# Preprocess data
all_words = []
tags = []
xy = []

for intent in intents['intents']:
    tag = intent['tag']
    tags.append(tag)
    for pattern in intent['patterns']:
        w = tokenize(pattern)
        all_words.extend(w)
        xy.append((w, tag))

ignore_words = ['?', '.', '!']
all_words = [lemmatize(w) for w in all_words if w not in ignore_words]
all_words = sorted(set(all_words))
tags = sorted(set(tags))

# Convert words to PyTorch tensors (ensure consistent data type)
X_train = []
y_train = []
for (pattern_sentence, tag) in xy:
    bag = bag_of_words(pattern_sentence, all_words)

    # Convert bag to a NumPy array with float32 dtype (assuming bag elements are numerical)
    bag = np.array(bag, dtype=np.float32)

    X_train.append(torch.tensor(bag))
    label = tags.index(tag)
    y_train.append(label)

X_train = torch.stack(X_train)  # Stack tensors into a single tensor
y_train = torch.tensor(y_train)  # Convert labels to PyTorch tensor

# Hyperparameters
num_epochs = 3000
batch_size = 8
learning_rate = 0.001
input_size = len(X_train[0])
hidden_size = 8
output_size = len(tags)


class ChatDataset(Dataset):
    def __init__(self):
        self.x_data = X_train
        self.y_data = y_train

    def __getitem__(self, index):
        return self.x_data[index], self.y_data[index]

    def __len__(self):
        return len(self.x_data)


dataset = ChatDataset()
train_loader = DataLoader(dataset=dataset,
                          batch_size=batch_size,
                          shuffle=True,
                          num_workers=0)

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

model = NeuralNet(input_size, hidden_size, output_size).to(device)

# Loss and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

# Train the model
for epoch in range(num_epochs):
    for (words, labels) in train_loader:
        words = words.to(device)
        labels = labels.to(device)

        # Forward pass
        outputs = model(words)
        loss = criterion(outputs, labels)

        # Backward and optimize
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    if (epoch + 1) % 100 == 0:
        print(f'Epoch [{epoch + 1}/{num_epochs}], Loss: {loss.item():.4f}')

# Save the model
data = {
    "model_state": model.state_dict(),
    "input_size": input_size,
    "output_size": output_size,
    "hidden_size": hidden_size,
    "all_words": all_words,
    "tags": tags
}

FILE = "backend/product_model/product_model.pth"
torch.save(data, FILE)

print(f"Training complete. File saved to {FILE}")