#!/usr/bin/env python3

import hashlib
import time
import random
import platform

# ---------------------------
#         GLOBAL SETTINGS
# ---------------------------

# Default benchmark duration (seconds)
benchmark_duration = 3  

# Default hashing algorithm (choose from "MD5", "SHA1", "SHA256", "SHA512")
hash_algorithm = "SHA256"

# Mapping from a string name to the actual hashlib constructor
ALGO_FUNCTIONS = {
    "MD5": hashlib.md5,
    "SHA1": hashlib.sha1,
    "SHA256": hashlib.sha256,
    "SHA512": hashlib.sha512,
}

# Distances for “If each hash was 1 meter” analogy (in kilometers)
DISTANCE_REFERENCES = [
    {"name": "the height of the ISS orbit (~400 km)",             "distance_km": 400},
    {"name": "the length of Germany N-S (~876 km)",               "distance_km": 876},
    {"name": "Berlin to Istanbul (~1,738 km)",                    "distance_km": 1738},
    {"name": "the length of Africa N-S (~8,000 km)",              "distance_km": 8000},
    {"name": "Earth's equator (~40,075 km)",                      "distance_km": 40075},
    {"name": "Earth to Moon (~384,400 km)",                       "distance_km": 384400},
    {"name": "Earth to Sun (~150 million km)",                    "distance_km": 150_000_000},
    {"name": "Earth to Jupiter (~588 million km)",               "distance_km": 588_000_000},
    {"name": "Earth to Pluto (~5.9 billion km)",                  "distance_km": 5_900_000_000},
]

# Some random fun facts
FUN_FACTS = [
    "SHA-256 is used by Bitcoin for proof-of-work. ⛏️",
    "MD5 is old but still widely used for checksums. 🔑",
    "SHA-1 was once considered secure, but collisions have been found. ⚠️",
    "Python was named after Monty Python, not the snake. 🐍",
    "The Earth’s circumference is about 40,075 km at the equator! 🌍",
    "Distance to the Moon is around 384,400 km – quite a hike! 🌕",
    "The first computer ‘bug’ was an actual moth found in a relay. 🦋",
]

# ----------------------------------------------------------------
# EASTER EGG HASH (MD5). The actual password is a 6-letter UPPERCASE word.
# ----------------------------------------------------------------
EASTER_EGG_HASH = "454f3567bdf5b94e0f421deac30c5e2d"

# A small wordlist for the "auto-cracker"

DICTIONARY = [
    "BUNNY",  
    "SPRING",
    "WINTER",
    "HOLIDAY",
    "EASTER", 
    "SUMMER",
    "AUTUMN",
    "FLOWER",
    "PLANET",
    "ROCKET",
    "CANDY",
]

# An ASCII banner for show
ASCII_BANNER = r"""
   ___                _           _                  _        
  / _ \ _ __ ___  ___| |__   ___ | |_   _ _ __   ___| |_ ___  
 | | | | '__/ _ \/ __| '_ \ / _ \| | | | | '_ \ / __| __/ __| 
 | |_| | | |  __/\__ \ | | | (_) | | |_| | | | | (__| |_\__ \ 
  \___/|_|  \___||___/_| |_|\___/|_|\__,_|_| |_|\___|\__|___/ 

  ~ A very good Hashing Benchmark Tool 🙃🙃🙃🙃 ~
"""

# ---------------------------
#       CORE BENCHMARK
# ---------------------------

def hash_benchmark(algo: str, duration: int):
    """
    Perform a hashing benchmark for a given duration using the specified algorithm.
    :param algo: Algorithm name ("MD5", "SHA1", "SHA256", "SHA512").
    :param duration: Time in seconds to run the benchmark.
    :return: (total_hashes, total_time_seconds)
    """
    if algo not in ALGO_FUNCTIONS:
        raise ValueError(f"Unsupported algorithm: {algo}")

    print(f"Starting {algo} hash benchmark for {duration} second(s)... ⚙️⏱️")
    start_time = time.time()
    count = 0
    
    # Get the hashlib constructor
    hash_func = ALGO_FUNCTIONS[algo]

    while (time.time() - start_time) < duration:
        # Just a small piece of data to hash, slightly varied
        data = b"BenchmarkTestData" + count.to_bytes(4, 'little')
        _ = hash_func(data).hexdigest()
        count += 1

    elapsed = time.time() - start_time
    hps = count / elapsed if elapsed else 0
    print(f"Completed {count} {algo} hashes in {elapsed:.2f} seconds.")
    print(f"That’s about {hps:,.0f} hashes per second!\n")
    return count, elapsed

# ---------------------------
#    DISTANCE COMPARISON
# ---------------------------

def distance_analogy(num_hashes: int):
    """
    Given the total number of hashes, treat each hash as if it were 1 meter traveled.
    Convert to kilometers and compare against known distances for a fun analogy.
    :param num_hashes: total number of hashes performed
    :return: A string with the distance analogy report
    """
    km = num_hashes / 1000.0  # 1 meter per hash => num_hashes / 1000 = kilometers

    message = f"If each hash was 1 meter, you traveled {km:,.2f} km.\n"
    
    # Check which milestones we surpassed
    reached_milestones = []
    for ref in DISTANCE_REFERENCES:
        if km >= ref["distance_km"]:
            reached_milestones.append(ref["name"])
    
    if not reached_milestones:
        message += "🚶 You haven’t reached the first milestone yet. Keep hashing to go further!\n"
    else:
        message += "You've gone beyond:\n"
        for milestone in reached_milestones:
            message += f" - {milestone}\n"
        
        # If you surpassed the last known reference, add a special message
        if reached_milestones[-1] == DISTANCE_REFERENCES[-1]["name"]:
            message += "You’ve even surpassed our largest reference! You're unstoppable! 🚀\n"

    return message

# ---------------------------
#        FUN EXTRAS
# ---------------------------

def show_fun_fact():
    """Print out a random fun fact."""
    fact = random.choice(FUN_FACTS)
    print("Here’s a fun fact! 🤓")
    print(f"➡️ {fact}\n")


def show_system_info():
    """Show some basic system information."""
    print("System Info 🖥️")
    print(f"Python Version : {platform.python_version()}")
    print(f"System         : {platform.system()}")
    print(f"Node           : {platform.node()}")
    print(f"Release        : {platform.release()}")
    print(f"Processor      : {platform.processor()}\n")

# ---------------------------
#      SETTINGS MENU
# ---------------------------

def print_settings_menu():
    print("""
╔══════════════════════════════════════════╗
║             SETTINGS MENU               ║
╠══════════════════════════════════════════╣
║ 1) Change Benchmark Duration            ║
║ 2) Change Hash Algorithm                ║
║ 3) Back to Main Menu                    ║
╚══════════════════════════════════════════╝
""")


def settings_menu():
    """
    Allows user to change global benchmark parameters:
      - benchmark_duration
      - hash_algorithm
    """
    global benchmark_duration, hash_algorithm

    while True:
        print_settings_menu()
        choice = input("Select an option: ").strip()

        if choice == '1':
            # Change benchmark duration
            new_duration = input("Enter new benchmark duration (in seconds): ").strip()
            if new_duration.isdigit():
                benchmark_duration = int(new_duration)
                print(f"Benchmark duration set to {benchmark_duration} second(s).\n")
            else:
                print("Invalid input! Please enter an integer.\n")

        elif choice == '2':
            # Change hashing algorithm
            print("Available algorithms:", ", ".join(ALGO_FUNCTIONS.keys()))
            new_algo = input(f"Enter new hash algorithm (e.g. {hash_algorithm}): ").upper().strip()
            if new_algo in ALGO_FUNCTIONS:
                hash_algorithm = new_algo
                print(f"Hash algorithm set to {hash_algorithm}.\n")
            else:
                print(f"Invalid algorithm! Please choose from {', '.join(ALGO_FUNCTIONS.keys())}.\n")

        elif choice == '3':
            # Return to main menu
            break
        else:
            print("Invalid option! Please try again.\n")

# ---------------------------
#       EASTER EGG
# ---------------------------

def manual_crack_easter_egg():
    """
    Ask the user for an Easter Egg password guess. Compare the MD5 hash of
    their guess with the stored hash. If it matches, reveal the secret message.
    """
    print("\n🔒 EASTER EGG: Manual Guess 🔒")
    print("Hint: It's a 6-letter UPPERCASE word often associated with a holiday!\n")
    user_guess = input("Enter your guess: ").strip().upper()

    hashed_guess = hashlib.md5(user_guess.encode("utf-8")).hexdigest()
    if hashed_guess == EASTER_EGG_HASH:
        print("\n✅ Congratulations! You cracked the Easter Egg password!")
        print("Secret message: 'Can i try o3 please' 🥳\n")
    else:
        print("\n❌ Sorry, that's not correct. Keep trying!\n")

def dictionary_crack_easter_egg():
    """
    Use a small built-in dictionary to attempt to find the Easter Egg password
    by comparing MD5 hashes of each word with EASTER_EGG_HASH.
    """
    print("\n🔍 EASTER EGG: Dictionary Attack 🔍")
    print(f"Trying {len(DICTIONARY)} words in our tiny dictionary...\n")

    for word in DICTIONARY:
        # Convert to uppercase just in case
        candidate = word.upper()
        hashed_candidate = hashlib.md5(candidate.encode("utf-8")).hexdigest()
        if hashed_candidate == EASTER_EGG_HASH:
            print(f"✅ Found a match! The password is '{candidate}'")
            print("Secret message: 'Pls can i try o3' 🥳\n")
            return
    print("❌ Sorry, no match found in the dictionary!\n")

def print_easter_egg_menu():
    print("""
╔══════════════════════════════════════════╗
║         EASTER EGG CRACKING MENU        ║
╠══════════════════════════════════════════╣
║ 1) Manual Guess                         ║
║ 2) Dictionary Attack                    ║
║ 3) Back to Main Menu                    ║
╚══════════════════════════════════════════╝
""")

def easter_egg_menu():
    while True:
        print_easter_egg_menu()
        choice = input("Select an option: ").strip()

        if choice == '1':
            manual_crack_easter_egg()
        elif choice == '2':
            dictionary_crack_easter_egg()
        elif choice == '3':
            break
        else:
            print("Invalid option! Please try again.\n")

# ---------------------------
#         MAIN MENU
# ---------------------------

def print_main_menu():
    print("""
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
""")

def main():
    print(ASCII_BANNER)
    print("Welcome to the Flexible Hashing Benchmark (with crackable Easter Egg)!")
    print("(Type the menu number to select an option.)\n")

    while True:
        print_main_menu()
        choice = input("Your choice: ").strip()

        if choice == '1':
            # Run the chosen benchmark
            total_hashes, _ = hash_benchmark(hash_algorithm, benchmark_duration)
            # Show the distance analogy
            analysis_msg = distance_analogy(total_hashes)
            print(analysis_msg)

        elif choice == '2':
            show_fun_fact()

        elif choice == '3':
            show_system_info()

        elif choice == '4':
            settings_menu()

        elif choice == '5':
            easter_egg_menu()

        elif choice == '6':
            print("Exiting... Thanks for benchmarking! 👋")
            break

        else:
            print("Invalid option! Please try again.\n")

# ---------------------------
#           RUN
# ---------------------------

if __name__ == "__main__":
    main()
