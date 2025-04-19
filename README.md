# Wind Turbine Predictive Maintenance System 🚀

![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8%2B-green.svg)
![Framework](https://img.shields.io/badge/framework-Flask-red.svg)
![ML](https://img.shields.io/badge/ML-LSTM-orange.svg)

## 🌬️ Real-Time Predictive Maintenance for Wind Turbines

A cutting-edge solution leveraging Apache Kafka, PySpark, and LSTM neural networks to predict wind turbine failures in real-time, reducing downtime and maintenance costs.

## 📌 Table of Contents
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Architecture](#-architecture)
- [Installation](#-installation)
- [Usage](#-usage)
- [Team](#-team)
- [License](#-license)

## ✨ Features
- **Real-time monitoring** of 5+ wind turbines
- **Predictive analytics** using LSTM neural networks
- **Interactive dashboard** with live visualizations
- **10-minute refresh cycle** for up-to-date insights
- **9 status codes** for comprehensive turbine health monitoring

## 🛠️ Tech Stack
| Component | Technology |
|-----------|------------|
| Streaming | Apache Kafka |
| Processing | PySpark |
| Machine Learning | TensorFlow/Keras (LSTM) |
| Visualization | Chart.js, Matplotlib |
| Web Framework | Flask |
| Data Analysis | Pandas, NumPy |

## 🏗️ Architecture
![System Architecture](https://github.com/user-attachments/assets/0f38f59a-aa43-4dea-aa37-8903c39d8aeb)

## 💻 Installation

### Prerequisites
- Python 3.8+
- Java 8+ (for Kafka)
- MySQL

### Setup
1. Clone the repository:
```bash
git clone https://github.com/BhanuPrakashNani/WindTurbine-PredictiveMaintenance.git
cd WindTurbine-PredictiveMaintenance
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up Kafka:
```bash
# Start Zookeeper
bin/zookeeper-server-start.sh config/zookeeper.properties

# Start Kafka server
bin/kafka-server-start.sh config/server.properties
```

## 🚀 Usage

1. Start the data producer:
```bash
python src/kafka_producer.py
```

2. Run the Spark streaming processor:
```bash
spark-submit src/spark_streaming.py
```

3. Launch the web dashboard:
```bash
python app.py
```

Access the dashboard at: `http://localhost:5000`

## 👥 Team
- Naveen Alampally ([@an4207](https://github.com/an4207))
- Anthony Nikhil Reddy Lingala ([@al8291](https://github.com/al8291))
- Bhanu Prakash Poluparthi ([@bp2507](https://github.com/bp2507))
- Kevin Vashinav ([@knv2014](https://github.com/knv2014))

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
