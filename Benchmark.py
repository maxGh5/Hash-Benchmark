import os
import platform
import time
import psutil
import threading
import hashlib
from concurrent.futures import ThreadPoolExecutor, as_completed
import csv
import shutil

try:
    import GPUtil  # Zum Erkennen echter GPUs
except ImportError:
    GPUtil = None

# Farbverlauf-Generator für RGB-Farben
def rgb_color(r, g, b):
    return f"\033[38;2;{r};{g};{b}m"

RESET = "\033[0m"

# Farben
CYAN = rgb_color(0, 255, 255)
GREEN = rgb_color(0, 255, 0)
YELLOW = rgb_color(255, 255, 0)
RED = rgb_color(255, 0, 0)
BLUE = rgb_color(0, 0, 255)

# Unterstützte CPU-Algorithmen
CPU_ALGORITHMS = ["sha256", "sha512", "blake2b", "sha3_256", "md5"]

# GPU-Unterstützung
def detect_gpus():
    """Erkennt verfügbare GPUs mit GPUtil."""
    if GPUtil is None:
        return []
    gpus = GPUtil.getGPUs()
    return [gpu.name for gpu in gpus]

GPU_LIST = detect_gpus()
GPU_ALGORITHMS = ["cuda_sha256", "cuda_sha512"] if GPU_LIST else []

# Globale Variablen
progress = 0
progress_lock = threading.Lock()
stop_animation = threading.Event()

def display_startup_message():
    """Zeigt die Startnachricht mit Farben und Rahmen."""
    text = "🌟 Multi-Algorithm Hash Benchmark 🌟"
    terminal_width = shutil.get_terminal_size().columns
    border = "═" * (len(text) + 4)
    padding = (terminal_width - len(border)) // 2

    for _ in range(3):  # Animation für 3 Wiederholungen
        os.system("cls" if platform.system() == "Windows" else "clear")
        print(f"{CYAN}{' ' * padding}╔{border}╗{RESET}")
        print(f"{CYAN}{' ' * padding}║  {text}  ║{RESET}")
        print(f"{CYAN}{' ' * padding}╚{border}╝{RESET}")
        time.sleep(0.5)

def print_normal_border(text):
    """Zeigt den Text mit einem normalen Rahmen an."""
    terminal_width = shutil.get_terminal_size().columns
    border = "═" * (len(text) + 4)
    padding = (terminal_width - len(border)) // 2

    print(f"{GREEN}{' ' * padding}╔{border}╗{RESET}")
    print(f"{GREEN}{' ' * padding}║  {text}  ║{RESET}")
    print(f"{GREEN}{' ' * padding}╚{border}╝{RESET}")

def print_progress_bar(total_duration, start_time):
    """Zeigt eine farbige Fortschrittsanzeige an."""
    bar_length = 50
    while not stop_animation.is_set():
        elapsed_time = time.perf_counter() - start_time
        progress_percentage = min(100, int((elapsed_time / total_duration) * 100))
        filled_length = int(bar_length * progress_percentage // 100)
        bar = f"{GREEN}{'█' * filled_length}{RESET}{'-' * (bar_length - filled_length)}"
        print(f"\r{CYAN}Progress: |{bar}| {progress_percentage}% Complete{RESET}", end="", flush=True)
        time.sleep(0.1)
    print("\n")

def format_hashrate(hashrate):
    """Formatiert die Hashrate in eine geeignete Einheit."""
    units = ["H/s", "kH/s", "MH/s", "GH/s", "TH/s", "PH/s"]
    power = 0
    while hashrate >= 1000 and power < len(units) - 1:
        hashrate /= 1000
        power += 1
    return f"{hashrate:.2f} {units[power]}"

def show_system_info():
    """Zeigt Informationen über das System an."""
    gpu_info = ", ".join(GPU_LIST) if GPU_LIST else "No GPU detected"
    system_info = (
        f"{YELLOW}Operating System:{RESET} {platform.system()} {platform.release()} ({platform.version()})\n"
        f"{YELLOW}CPU:{RESET} {platform.processor()}\n"
        f"{YELLOW}CPU Cores:{RESET} {os.cpu_count()}\n"
        f"{YELLOW}Python Version:{RESET} {platform.python_version()}\n"
        f"{YELLOW}Total Memory:{RESET} {psutil.virtual_memory().total / (1024 ** 3):.2f} GB\n"
        f"{YELLOW}GPU(s):{RESET} {gpu_info}"
    )
    print_normal_border("System Information")
    print(system_info)

def display_ascii_menu():
    """Zeigt das Hauptmenü an."""
    menu = f"""
    {CYAN}🌟 Main Menu 🌟{RESET}
    {YELLOW}1️⃣  Set Benchmark Duration
    2️⃣  Choose Hash Algorithm
    3️⃣  Set Number of Threads
    4️⃣  🚀 Start Single Algorithm Benchmark
    5️⃣  🌍 Start Multi-Algorithm Benchmark
    6️⃣  📊 Show Benchmark History
    7️⃣  💻 Show System Info
    8️⃣  ❌ Exit{RESET}
    """
    print(menu)

def hash_worker(duration, algorithm="sha256"):
    """Berechnet Hashes für die angegebene Zeit."""
    global progress
    start_time = time.perf_counter()
    hasher = getattr(hashlib, algorithm)()
    local_progress = 0
    data = b"0" * 4096

    while time.perf_counter() - start_time < duration:
        hasher.update(data)
        hasher.digest()
        local_progress += 1

    with progress_lock:
        progress += local_progress

def run_benchmark(algorithm, duration=20, threads=None):
    """Startet einen Benchmark für einen Algorithmus."""
    global progress, stop_animation
    progress = 0
    stop_animation.clear()

    if threads is None:
        threads = os.cpu_count()

    start_time = time.perf_counter()
    progress_thread = threading.Thread(target=print_progress_bar, args=(duration, start_time))
    progress_thread.start()

    print_normal_border(f"Benchmark: {algorithm.upper()} ({threads} Threads)")
    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures = [executor.submit(hash_worker, duration, algorithm) for _ in range(threads)]
        for future in as_completed(futures):
            future.result()

    elapsed = time.perf_counter() - start_time
    hashrate = format_hashrate(progress / elapsed)
    stop_animation.set()
    progress_thread.join()

    return {
        "Algorithm": algorithm.upper(),
        "Duration": f"{elapsed:.2f} seconds",
        "Total Hashes": progress,
        "Hashrate": hashrate
    }

def run_multi_algorithm_benchmark():
    """Startet einen Benchmark für alle unterstützten Algorithmen."""
    results = []
    all_algorithms = CPU_ALGORITHMS + GPU_ALGORITHMS
    for algorithm in all_algorithms:
        result = run_benchmark(algorithm)
        results.append(result)

    print_normal_border("Benchmark Results")
    for res in results:
        print(f"{YELLOW}{res}{RESET}")

def main():
    """Hauptfunktion des Programms."""
    display_startup_message()  # Zeigt die Startanimation

    benchmark_duration = 20
    selected_algorithm = "sha256"
    number_of_threads = os.cpu_count()

    while True:
        display_ascii_menu()
        choice = input(f"{BLUE}👉 Please choose an option (1-8): {RESET}")

        if choice == "1":
            benchmark_duration = int(input("Enter benchmark duration (seconds): "))
        elif choice == "2":
            all_algorithms = CPU_ALGORITHMS + GPU_ALGORITHMS
            selected_algorithm = input(f"Enter hash algorithm ({', '.join(all_algorithms)}): ").lower()
            if selected_algorithm not in all_algorithms:
                print(f"{RED}Invalid algorithm! Defaulting to sha256.{RESET}")
                selected_algorithm = "sha256"
        elif choice == "3":
            number_of_threads = int(input("Enter number of threads: "))
        elif choice == "4":
            result = run_benchmark(selected_algorithm, benchmark_duration, number_of_threads)
            print(f"{GREEN}Result:{RESET} {result}")
        elif choice == "5":
            run_multi_algorithm_benchmark()
        elif choice == "6":
            print("Feature coming soon.")
        elif choice == "7":
            show_system_info()
        elif choice == "8":
            print_normal_border("Goodbye!")
            break
        else:
            print(f"{RED}Invalid choice! Please select a valid option.{RESET}")

if __name__ == "__main__":
    main()
