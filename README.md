# Alexer

An AI-powered smart home assistant that connects a local LLM (Ollama) with IoT devices using MQTT.  
The system allows natural language commands like “turn on the light” to control real hardware. This example project controlls the lamps called kitchen, desk, and cupboard.

## 🚀 Features

- 🧠 Natural language control using local LLM (Ollama)
- 📡 MQTT-based communication with IoT devices
- 💡 Smart home automation (lights, sensors, etc.)
- 🐳 Fully Dockerized setup

## 🧰 Tech Stack

- Python
- Ollama (LLM runtime)
- MQTT (Mosquitto)
- Docker / Docker Compose
- IoT

## 🏗️ Architecture

User → [NLP Model (Ollama) → Python Agent → MQTT Broker] → IoT Devices


## Usage

```bash
##Start the Docker Container with Mosquitto and Ollama
sh scripts\start_ollama.sh
```

```bash
##Start the Homeautomation Controller
python ollama_mqtt\mqtt.py
```


