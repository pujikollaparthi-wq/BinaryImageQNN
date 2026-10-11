# Binary Image Classification Using Machine Learning and Deep Quantum Neural Networks

An advanced image classification system integrating Classical Machine Learning and Deep Quantum Neural Networks (QNN) for binary classification on datasets like MNIST (e.g., distinguishing digit pairs such as 0 vs 1, 3 vs 7).

## 🚀 Overview

Quantum Neural Networks (QNNs) harness the principles of quantum computing—superposition and entanglement—to process high-dimensional visual information. This project features a full-stack Django application that provides:

- **Quantum Neural Network (QNN) Pipeline**: Variational Quantum Circuits (VQC) using PennyLane/PyTorch.
- **Classical ML Baseline**: Comparative evaluation against classical ML and CNN models.
- **Interactive Canvas UI**: Web-based digit drawing interface powered by HTML5 Canvas for real-time classification.
- **Admin & User Dashboards**: Management interface for training, dataset inspection, and performance evaluation.

---

## 🛠️ Technology Stack

- **Backend**: Python, Django
- **Quantum Computing**: PennyLane, PennyLane-Qiskit
- **Machine Learning / Deep Learning**: PyTorch, TensorFlow, Scikit-learn, NumPy
- **Frontend**: HTML5 Canvas, CSS3, JavaScript, Bootstrap
- **Database**: SQLite

---

## 📂 Project Structure

```text
├── 2.Binary Image Classification Using Machine Learning and Deep Quantum Neural Networks/
│   ├── Binary_Image_Classification_Using_Machine_Learning_and_Deep_Quantum_Neural_Networks/
│   │   └── BinaryImageQNN/
│   │       ├── BinaryImageQNN/        # Django project settings & routing
│   │       ├── users/                 # User app & interactive canvas
│   │       ├── admins/                # Admin portal & model training
│   │       ├── assets/                # Static assets & stylesheets
│   │       ├── mnist_data/            # MNIST dataset files
│   │       ├── manage.py              # Django execution entry point
│   │       └── requirements.txt       # Python dependencies
│   ├── abstract/                      # Project abstract and overview
│   ├── basepaper/                     # Research paper references
│   └── binory image documantes/       # Project documentation
├── .gitignore                         # Git ignore rules
└── README.md                          # Project documentation
```

---

## ⚙️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/pujikollaparthi-wq/BinaryImageQNN.git
   cd BinaryImageQNN
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   # macOS/Linux:
   source venv/bin/activate
   ```

3. **Install Dependencies:**
   ```bash
   cd "2.Binary Image Classification Using Machine Learning and Deep Quantum Neural Networks/Binary_Image_Classification_Using_Machine_Learning_and_Deep_Quantum_Neural_Networks/BinaryImageQNN"
   pip install -r requirements.txt
   ```

4. **Run Database Migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Start the Development Server:**
   ```bash
   python manage.py runserver
   ```

6. Open your browser and navigate to `http://127.0.0.1:8000/`.

---

## 📊 Features & Workflow

1. **User Registration & Login**: Authentication for accessing the prediction interface.
2. **Interactive Drawing Board**: Draw digits directly on the canvas and submit for real-time classification.
3. **QNN Inference**: Image preprocessing (downsampling/PCA) encoded into quantum states via angle embedding and measured through variational layers.
4. **Performance Metrics**: Comparative accuracy, loss curves, and confusion matrix against classical ML.

---

## 👤 Author
- **GitHub**: [@pujikollaparthi-wq](https://github.com/pujikollaparthi-wq)
