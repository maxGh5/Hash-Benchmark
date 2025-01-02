# Hashing Benchmark with Easter Egg Cracker

Welcome to the **Hashing Benchmark Tool**! This fun project allows you to test your computer's hashing performance, compare the results with real-world distances, and discover a hidden Easter Egg by cracking its MD5 hash.

---

## Features

- **Hashing Benchmark:**
  - Measure how many hashes your computer can compute in a set duration using algorithms like MD5, SHA1, SHA256, or SHA512.
  - Results are compared to real-world distances (e.g., "If each hash was 1 meter, you traveled X kilometers").

- **Easter Egg Challenge:**
  - Guess the 6-character uppercase password for the hidden Easter Egg.
  - Use manual guessing or an automatic dictionary attack.

- **Fun Facts:**
  - Learn random fun facts about hashing, cryptography, and computing.

- **Settings Menu:**
  - Customize the benchmark duration and hashing algorithm.

---

## Getting Started

### Requirements

- Python 3.x

No additional libraries are required as the script uses only Python's built-in modules.

### Running the Script

1. Clone or download the repository.
2. Open a terminal and navigate to the project directory.
3. Run the script using:
   ```bash
   python3 benchmark.py
   ```

### Menu Options

- **1) Start Hash Benchmark:** Run the benchmark and see how many hashes your PC can compute.
- **2) Show Fun Fact:** Learn something fun about hashing or computing.
- **3) System Info:** View details about your system and Python environment.
- **4) Settings:** Adjust the benchmark duration or hashing algorithm.
- **5) Crack Easter Egg:** Try to guess or crack the Easter Egg password.
- **6) Exit:** Quit the program.

---

## Easter Egg Challenge

The Easter Egg is hidden behind an MD5 hash. You can access it in two ways:

1. **Manual Guess:** Enter your guess for the 6-character password. Hint: It is a word often associated with a holiday.
2. **Dictionary Attack:** Use the built-in dictionary to automatically find the password.

---

## Customization

Feel free to customize the script to suit your preferences:

- **Add More Algorithms:** Extend the `ALGO_FUNCTIONS` dictionary with additional hashing algorithms.
- **Expand the Dictionary:** Add more words to the `DICTIONARY` list for the dictionary attack.
- **Update Distances:** Modify or add entries in the `DISTANCE_REFERENCES` list for comparison.
- **Change the Easter Egg:** Replace the `EASTER_EGG_HASH` with a new MD5 hash and adjust the hints.

---

## Example Output

```plaintext
╔════════════════════════════════════════╗
║               MAIN MENU               ║
╠════════════════════════════════════════╣
║ 1) Start Hash Benchmark  ⚙️           ║
║ 2) Show Fun Fact         🤯           ║
║ 3) System Info           💻           ║
║ 4) Settings              ⚒️           ║
║ 5) Crack Easter Egg      🥚           ║
║ 6) Exit                  🚪           ║
╚════════════════════════════════════════╝

Select an option: 1
Starting SHA256 hash benchmark for 3 second(s)... ⚙️⏱️
Completed 300,000 SHA256 hashes in 3.00 seconds.
That’s about 100,000 hashes per second!

If each hash was 1 meter, you traveled 300.00 km.
You've gone beyond:
 - the height of the ISS orbit (~400 km)

---
```

---

## License

This project is open-source and available under the MIT License. Feel free to modify and share it!

---

## Contributing

If you have suggestions for improvements or additional features, feel free to fork the repository and submit a pull request.

