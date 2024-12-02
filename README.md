THIS PROJEKT IS NOT FINISHED!!!


🌟 Multi-Algorithm Hash Benchmark 🌟

A powerful tool to benchmark various hashing algorithms on both CPU and GPU! It automatically detects available system resources (CPU cores and GPUs) and utilizes them efficiently to compute and analyze hash rates.


---

🚀 Features

Supported Algorithms:

CPU: sha256, sha512, blake2b, sha3_256, md5

GPU (if available): cuda_sha256, cuda_sha512


Automatic Thread Detection:

Automatically optimizes the number of threads based on available CPU cores and GPU capabilities.


System Information:

Displays detailed information about the operating system, CPU, RAM, and available GPUs.


Progress Bar:

An animated progress bar during benchmarks for better visualization.


Colorful Layout:

A user-friendly interface with colorful frames and emojis.


Multi-Algorithm Benchmarking:

Tests multiple algorithms automatically and displays detailed results.




---

📋 Requirements

1. Python Version: Python 3.7 or higher


2. Dependencies:

Install the required libraries using:

pip install psutil GPUtil





---

📂 Installation

1. Clone this

2. Install dependencies:

pip install -r requirements.txt



---

🖥️ Usage

1. Run the program:

python Benchmark.py


2. Follow the on-screen menu:

Set Benchmark Duration: Configure the time for the benchmark in seconds.

Choose Hash Algorithm: Select from supported algorithms.

Start Single Algorithm Benchmark: Run a benchmark for a specific algorithm.

Start Multi-Algorithm Benchmark: Run benchmarks for all available algorithms.

Show Benchmark History: View previous results.

Show System Info: Display system hardware information.

Exit: Exit the program.




---

🧪 Example Output

System Information

Operating System: Windows 10 (10.0.22631)
CPU: Intel Core i9-12900K
CPU Cores: 24
Python Version: 3.10.9
Total Memory: 32.0 GB
GPU(s): NVIDIA GeForce RTX 3080

Benchmark Results

Algorithm: SHA256
Duration: 20.00 seconds
Total Hashes: 12,345,678
Hashrate: 617.28 MH/s


---

📜 License

This project is licensed under the MIT License.


---

💡 Contributions

Contributions are welcome! Feel free to fork this repository, submit pull requests, or open issues to improve the project.


