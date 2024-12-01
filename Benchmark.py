import os
import time
import hashlib
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed

# Globale Variablen
progress = 0
stop_animation = False

# Unterstützte CPU-Algorithmen
CPU_ALGORITHMS = ["sha256", "sha512", "blake2b"]

def display_ascii_menu():
    """Zeigt das farbige ASCII-Hauptmenü an und gibt die Benutzerauswahl zurück."""
    print("\n")
    print("\033[94m╔════════════════════════════════════════╗")
    print("║     🌟 \033[96mMulti-Algorithm Hash Benchmark\033[94m 🌟    ║")
    print("╚════════════════════════════════════════╝")
    print("\033[93m1️⃣  Set Benchmark Duration (in seconds)")
    print("2️⃣  Choose Hash Algorithm (SHA256/SHA512/Blake2b)")
    print("3️⃣  Set Number of Threads")
    print("4️⃣  🚀 Start Single Algorithm Benchmark")
    print("5️⃣  🌍 Start Multi-Algorithm Benchmark")
    print("6️⃣  ❌ Exit")
    print("\033[94m══════════════════════════════════════════\033[0m")
    return input("\033[96m👉 Please choose an option (1-6): \033[0m")

def get_input_ascii(prompt, default_value):
    """Nimmt eine Eingabe vom Benutzer entgegen und gibt den Standardwert zurück, falls keine Eingabe erfolgt."""
    user_input = input(f"{prompt} (Default: {default_value}): ")
    return user_input if user_input else default_value

def print_progress_bar(total_duration, start_time):
    """Zeigt eine farbige ASCII-Progress-Bar an, die den Fortschritt des Benchmarks verfolgt."""
    while not stop_animation:
        elapsed_time = time.time() - start_time
        progress_percentage = min(100, int((elapsed_time / total_duration) * 100))
        bar_length = 30  # Länge der Progress-Bar
        filled_length = int(bar_length * progress_percentage // 100)
        bar = '\033[92m' + '█' * filled_length + '\033[91m' + '-' * (bar_length - filled_length) + '\033[0m'
        print(f"\r\033[93mProgress: |{bar}| {progress_percentage}% Complete\033[0m", end="", flush=True)
        time.sleep(0.2)

def format_hashrate(hashrate):
    """Formatiert die Hashrate in eine geeignete Einheit (H/s, kH/s, MH/s, etc.)."""
    units = ["H/s", "kH/s", "MH/s", "GH/s", "TH/s", "PH/s", "EH/s"]
    power = 0
    while hashrate >= 1000 and power < len(units) - 1:
        hashrate /= 1000
        power += 1
    return f"{hashrate:.2f} {units[power]}"

def display_results(results):
    """Zeigt die Benchmark-Ergebnisse übersichtlich in mehreren Zeilen an."""
    print("\n\033[96m✨ Benchmark Results ✨\033[0m\n")
    headers = ["Algorithm", "Duration", "Hashes", "Hashrate"]
    row_format = "{:<15} {:<15} {:<15} {:<15}"  # Formatierung der Tabelle

    # Tabellenkopf
    print("\033[94m" + row_format.format(*headers) + "\033[0m")
    print("\033[94m" + "-" * 60 + "\033[0m")

    # Ergebnisse zeilenweise ausgeben
    for result in results:
        row = row_format.format(
            result["algorithm"],
            result["duration"],
            result["hashes"],
            result["hashrate"]
        )
        print(row)
    print("\n")

def hash_worker(duration, algorithm="sha256"):
    """Berechnet Hashes für die angegebene Zeit."""
    global progress
    start_time = time.time()
    
    hasher = getattr(hashlib, algorithm)
    while time.time() - start_time < duration:
        data = str(progress).encode()
        hasher(data).hexdigest()
        progress += 1

def run_benchmark(algorithm, duration=20, threads=None):
    """Startet den Benchmark für einen bestimmten Algorithmus."""
    global progress, stop_animation
    progress = 0
    stop_animation = False

    if threads is None:
        threads = os.cpu_count()

    # Starte die Progress-Bar in einem separaten Thread
    start_time = time.time()
    progress_thread = threading.Thread(target=print_progress_bar, args=(duration, start_time))
    progress_thread.start()

    print(f"\n\033[94m🏁 Benchmark started for Algorithm: {algorithm} ({threads} Threads) 🏁\033[0m")

    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures = [executor.submit(hash_worker, duration, algorithm) for _ in range(threads)]
        for future in as_completed(futures):
            pass

    elapsed = time.time() - start_time
    hashrate = progress / elapsed
    stop_animation = True  # Stoppe die Progress-Bar nach Abschluss des Benchmarks
    progress_thread.join()  # Warten, bis der Progress-Thread beendet ist

    results = {
        "algorithm": algorithm,
        "duration": f"{elapsed:.2f} seconds",
        "hashes": progress,
        "hashrate": format_hashrate(progress / elapsed)
    }

    return results

def run_multi_algorithm_benchmark():
    """Startet den Multi-Algorithm Benchmark für die unterstützten CPU-Algorithmen."""
    results = []

    print("\033[92m🖥️ Running CPU benchmarks...\033[0m")
    for algorithm in CPU_ALGORITHMS:
        results.append(run_benchmark(algorithm, duration=20, threads=os.cpu_count()))

    display_results(results)

if __name__ == "__main__":
    # Standardwerte
    duration = 20  # Standarddauer für jeden Benchmark in Sekunden
    algorithm = "sha256"  # Standardalgorithmus
    threads = os.cpu_count()  # Automatische Erkennung der optimalen Anzahl von CPU-Kernen

    while True:
        choice = display_ascii_menu()

        if choice == "1":
            duration = int(get_input_ascii("⏳ Enter benchmark duration (in seconds)", duration))
        elif choice == "2":
            algorithm = get_input_ascii("🔑 Choose hash algorithm (sha256/sha512/blake2b)", algorithm).lower()
            if algorithm not in CPU_ALGORITHMS:
                print("\033[91m❌ Invalid algorithm selected. Default (sha256) will be used.\033[0m")
                algorithm = "sha256"
        elif choice == "3":
            threads = int(get_input_ascii("🔧 Enter the number of threads", threads))
            if threads <= 0:
                print("\033[91m❌ Invalid number of threads. Default will be used.\033[0m")
                threads = os.cpu_count()
        elif choice == "4":
            # Einzelner Algorithmus-Benchmark
            results = [run_benchmark(algorithm, duration, threads)]
            display_results(results)
        elif choice == "5":
            # Multi-Algorithmus Benchmark
            run_multi_algorithm_benchmark()
        elif choice == "6":
            print("\033[91m👋 Exiting program. Goodbye!\033[0m")
            break
        else:
            print("\033[91m❌ Invalid choice. Please try again.\033[0m")
