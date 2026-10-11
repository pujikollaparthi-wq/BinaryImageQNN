import pennylane as qml
import torch
from torch import nn
import numpy as np
import cv2
import os

# =============================
# Quantum Parameters
# =============================

n_qubits = 64
n_layers = 2

dev = qml.device("default.qubit", wires=n_qubits)

# =============================
# Quantum Circuit
# =============================

def circuit(inputs, weights):

    qml.templates.AngleEmbedding(inputs, wires=range(n_qubits))
    qml.templates.BasicEntanglerLayers(weights, wires=range(n_qubits))

    return [qml.expval(qml.PauliZ(i)) for i in range(n_qubits)]


qnode = qml.QNode(circuit, dev, interface="torch", diff_method="backprop")

# =============================
# QNN MODEL
# =============================

class QNN(nn.Module):

    def __init__(self):

        super().__init__()

        weight_shapes = {"weights": (n_layers, n_qubits)}

        self.qlayer = qml.qnn.TorchLayer(qnode, weight_shapes)

        self.fc = nn.Linear(n_qubits, 10)

    def forward(self, x):

        x = self.qlayer(x)
        x = self.fc(x)

        return torch.log_softmax(x, dim=1)

# =============================
# MODEL PATH
# =============================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "mnist_qnn_model.pth")

# =============================
# LOAD MODEL
# =============================

model = QNN()

if os.path.exists(MODEL_PATH):

    model.load_state_dict(torch.load(MODEL_PATH, map_location="cpu"))
    model.eval()

    print("Model Loaded Successfully")

else:

    print("Model not found. Please run training first.")

# =============================
# PREDICT FUNCTION
# =============================

def predict_digit(image):

    try:

        # PIL image → resize to 8x8
        image = image.resize((8,8))

        # convert to numpy
        img = np.array(image)

        # invert colors
        img = 255 - img

        # normalize
        img = img / 255.0

        # reshape for model
        img = img.reshape(1,64)

        # convert to tensor
        img = torch.tensor(img).float()

        with torch.no_grad():

            output = model(img)

            _, predicted = torch.max(output,1)

        return int(predicted.item())

    except Exception as e:

        print("Prediction Error:", e)
        return -1