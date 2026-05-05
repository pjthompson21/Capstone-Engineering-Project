import subprocess
import time
import sys


def run(cmd):
    """Execute shell command and print output cleanly."""
    print(f"\n[+] Running: {cmd}\n")

    result = subprocess.run(
        cmd,
        shell=True,
        text=True,
        capture_output=True
    )

    if result.stdout:
        print(result.stdout)

    if result.stderr:
        print("[stderr]")
        print(result.stderr)

    return result.returncode


# --------------------------------
# Attack Scenario 1: Privilege Escalation
# --------------------------------
def scenario_1():
    print("\n=== Attack Scenario #1: Privilege Escalation ===")

    commands = [
    # 1. LIST SUDO COMMANDS AVAILABLE TO USER
    "sudo -l",

    # 2. SHOW CURRENT USER IDENTITY
    "id",

    # 3. VALIDATE CURRENT USER
    "whoami",

    # 4. ATTEMPT DIRECT ACCESS
    "cat /etc/shadow",

    # 5. PRIVILEGE ESCALATION ATTEMPT
    "sudo cat /etc/shadow",

    # 6. START FULL PRIVILEGED SESSION
    "sudo -v",

    # 7. VERIFY ROOT CONTEXT
    "whoami",

    # 8. EXIT SESSION
    "exit"
]

    for cmd in commands:
        run(cmd)
        time.sleep(1)


# ------------------------------
# Attack Scenario 2: Persistence (Cron)
# ------------------------------
def scenario_2():
    print("\n=== Attack Scenario #2: Persistence (Cron) ===")

    commands = [
    # 1. CREATE PERSISTENCE
    "echo '* * * * * echo persistence_test >> /tmp/persist.log' | crontab -",

    # 2. VERIFY PERSISTENCE
    "crontab -l",

    # 3. EXECUTION SIGNAL
    "sleep 30 && logger 'CRON persistence executed by pjt0012'",

    # 4. MODIFY PERSISTENCE
    "echo '* * * * * echo updated_persistence >> /tmp/persist.log' | crontab -"
]

    for cmd in commands:
        run(cmd)
        time.sleep(1)


# -------------------------------------------
# Attack Scenario 3: File Integrity Monitoring (FIM)
# -------------------------------------------
def scenario_3():
    print("\n=== Attack Scenario #3: Staging, Execution, Cleanup (FIM) ===")

    commands = [
    # 1. CREATE FILE
    "echo 'SOC TEST FILE' > /tmp/soc_fim_test.txt",

    # 2. MODIFY FILE 
    "echo 'MODIFIED CONTENT 1' >> /tmp/soc_fim_test.txt",
    "echo 'MODIFIED CONTENT 2' >> /tmp/soc_fim_test.txt",

    # 3. ACCESS FILE 
    "cat /tmp/soc_fim_test.txt",

    # 4. CHANGE PERMISSIONS
    "chmod 600 /tmp/soc_fim_test.txt",

    # 5. DELETE FILE
    "rm /tmp/soc_fim_test.txt"
]

    for cmd in commands:
        run(cmd)
        time.sleep(1)


# -------------------------
# Cleanup
# -------------------------
def cleanup():
    print("\n=== Cleanup ===")

    commands = [
        "crontab -r 2>/dev/null",
        "rm -f /tmp/soc_fim_test.txt /tmp/persist.log",
        "logger 'CLEANUP: removed cron persistence test artifacts'"
    ]

    for cmd in commands:
        run(cmd)


# -------------------------
# Menu
# -------------------------
def main():
    while True:
        print("\n==============================")
        print(" SOC Attack Scenario Runner")
        print("==============================")
        print("1. Privilege Escalation")
        print("2. Persistence (Cron)")
        print("3. Staging, Execution, Cleanup (FIM)")
        print("4. Cleanup")
        print("5. Exit")

        choice = input("\nSelect attack scenario: ")

        if choice == "1":
            scenario_1()
        elif choice == "2":
            scenario_2()
        elif choice == "3":
            scenario_3()
        elif choice == "4":
            cleanup()
        elif choice == "5":
            sys.exit(0)
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
