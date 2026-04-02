# CSE Advanced AI & Deep Learning Lab - Student Guide

## General Lab Information

- **Department:** Computer Science and Engineering (CSE)
- **Lab Name:** Advanced AI & Deep Learning Lab
- **Lab Room Number:** Room 304, Block B
- **Lab Timings:** Monday to Friday, 9:00 AM to 4:00 PM
- **Primary Instructor:** Assistant Professor Arun
- **Contact Email:** arun.cse@university.edu
- **Mentored Projects Hub:** Base for the "Creadeat" hackathon-winning student project.
- **Lab Network SSID (Wi-Fi):** CSE_AI_LAB_5G
- **Lab Wi-Fi Password:** DeepLearn2026!
- **Emergency Contact / Lab Technician:** Technical Staff, Ext. 402

## Hardware and Software Infrastructure

### Workstation Specifications
- 32GB RAM
- Intel i9 Processor
- 1TB NVMe SSD

### GPU Availability
- 10x NVIDIA RTX 3090
- 2x RTX 4090

### Operating System
- Ubuntu 22.04 LTS

### Primary Programming Language
- Python 3.10+

### Key Installed Frameworks
- PyTorch 2.2+
- TensorFlow 2.15+
- HuggingFace Transformers
- LangChain / LlamaIndex
- JupyterLab / VS Code

### Server Access Protocol
Students must use SSH to connect to the main GPU cluster at IP 192.168.1.150 using port 2222.

### GPU Cluster Password/Key Policy
SSH keys must be generated and submitted to the TA by Week 2. Password authentication is disabled.

## Coursework and Practical Outlines

### Machine Learning (B.Tech CSE)
- **Lab 1:** Introduction to Scikit-Learn, Pandas, and Data Preprocessing.
- **Lab 2:** Implementing Linear and Logistic Regression from scratch.
- **Lab 3:** Decision Trees, Random Forests, and Hyperparameter tuning.
- **Dataset Repository:** All local datasets for ML labs are stored on the shared drive at /mnt/data/ml_datasets.

### Deep Learning (B.Tech CSE)
- **Lab 1:** Building a basic Multilayer Perceptron (MLP) using PyTorch.
- **Lab 2:** Convolutional Neural Networks (CNNs) for Image Classification (CIFAR-10).
- **Lab 3:** Recurrent Neural Networks (RNNs) and LSTMs for Time-Series forecasting.
- **Compute Quota:** Students are limited to 10 hours of GPU compute time per week for DL model training.

### Generative AI (B.Tech CSE)
- **Lab 1:** Introduction to LLM APIs and prompt engineering techniques.
- **Lab 2:** Implementing a Retrieval-Augmented Generation (RAG) pipeline using LangChain.
- **Lab 3:** Fine-tuning open-source models (e.g., Llama-3, Mistral) using LoRA/QLoRA.
- **API Keys:** Departmental OpenAI/Anthropic API keys are strictly confidential. Students must request access via the local proxy server at http://proxy.cse.local:8080.

## Lab Policies and Grading Rubric

### Attendance Policy
75% mandatory attendance required to appear for the final lab viva.

### Submission Guidelines
All lab records and Jupyter Notebooks (.ipynb) must be pushed to the student's assigned GitHub classroom repository by Friday 11:59 PM each week.

### Plagiarism Policy
Automated code similarity checks are run using MOSS. Matches above 30% will result in a zero for that specific practical.

### Evaluation Breakdown
- **Weekly Lab Executions:** 40%
- **Lab Record Maintenance:** 20%
- **Mini-Project Implementation:** 20%
- **Final Viva-Voce:** 20%

## Troubleshooting FAQs

### Q: What do I do if my Jupyter kernel crashes during model training?
**A:** Clear the GPU memory by running `nvidia-smi` to find the zombie process PID, then use `kill -9 [PID]`. Restart the kernel and reduce your batch size.

### Q: How do I request additional GPU hours for my B.Tech final year project or the Creadeat project?
**A:** Send a formal request outlining your model architecture and estimated compute requirements to Assistant Professor Arun via email at least 48 hours in advance.

### Q: The proxy server for huggingface.co is blocked. How do I download models?
**A:** Use the departmental mirror at http://huggingface-mirror.cse.local or execute the lab script `download_weights.sh` to bypass the firewall for model weights.
