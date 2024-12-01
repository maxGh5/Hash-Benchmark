# Multi-Algorithm Hash Benchmark

🌟 **Multi-Algorithm Hash Benchmark** is a tool designed to measure your CPU’s performance when computing hashes using various algorithms.  
It supports **SHA-256**, **SHA-512**, and **Blake2b** and allows benchmarking for single or multiple algorithms.

---

## 🔧 Features

- **Supported Algorithms:**
  - SHA-256
  - SHA-512
  - Blake2b
- **Customizable Settings:**
  - Benchmark duration
  - Number of threads
  - Algorithm selection
- **Multi-Algorithm Benchmark:** Run benchmarks for all supported algorithms sequentially.
- **Progress Bar:** Visual representation of the benchmark progress.
- **Result Display:** Results are shown in a clear table format.

---

## 🚀 Installation

### 1. Install Python
Download and install Python 3.6 or higher from [python.org](https://www.python.org/downloads/).  
Make sure to enable the **"Add Python to PATH"** option during installation.

### 2. Clone the Project

git clone https://github.com/username/multi_algorithm_benchmark.git
cd multi_algorithm_benchmark

3. Install Dependencies
The tool works with Python's standard library, so no additional dependencies are required.

Optional: Install colorama for enhanced color display on Windows:

pip install colorama

🏁 Usage
1. Start the Benchmark
Run the script:

python benchmark.py

2. Main Menu
The tool offers several options to choose from:

1️⃣ Set Benchmark Duration: Set the benchmark duration in seconds.
2️⃣ Choose Hash Algorithm: Select one of the supported algorithms (SHA-256, SHA-512, Blake2b).
3️⃣ Set Number of Threads: Manually adjust the number of CPU threads.
4️⃣ Start Single Algorithm Benchmark: Run the benchmark for the selected algorithm.
5️⃣ Start Multi-Algorithm Benchmark: Benchmark all supported algorithms sequentially.
6️⃣ Exit: Quit the program.
3. Results
The results are displayed in a clear table format, such as:

Algorithm	Duration	Hashes	Hashrate
SHA-256	20.00 seconds	500000	25.00 MH/s
SHA-512	20.00 seconds	300000	15.00 MH/s
Blake2b	20.00 seconds	400000	20.00 MH/s


🖥️ Example Output

🏁 Benchmark started for Algorithm: sha256 (8 Threads)

Progress: |██████████████----------------| 50% Complete

✨ Benchmark Results ✨

Algorithm       Duration        Hashes          Hashrate        
------------------------------------------------------------
SHA-256         20.00 seconds  500000          25.00 MH/s      
SHA-512         20.00 seconds  300000          15.00 MH/s      
Blake2b         20.00 seconds  400000          20.00 MH/s


📂 Project Structure

multi_algorithm_benchmark/
│
├── benchmark.py          # Main script
├── requirements.txt      # Optional dependencies
└── README.md             # Project documentation


🛠️ Requirements
Python 3.6 or higher
Operating Systems:
Windows, Linux, macOS
Optional: colorama for enhanced terminal color support
💡 Future Enhancements
Add more hashing algorithms.
GPU support for selected algorithms.
Advanced statistics and visualizations for benchmarking results.


THIS PROJECT IS UNFINISHED!!!



