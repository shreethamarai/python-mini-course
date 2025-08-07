# 🐍 Python Mini Course (with GitHub Version Control)

A complete, hands-on Python learning roadmap structured into 4 levels, built with a focus on monotasking, self-discipline, and professional development. This course is version-controlled using Git and structured for clarity and long-term learning.

---

## 📚 Overview

This course is designed for self-learners who want to:
- Master Python from fundamentals to advanced topics
- Practice Object-Oriented Programming with real examples
- Learn Data Structures & Algorithms in Python with Big-O analysis
- Understand system-level and networking concepts for backend apps
- Maintain clean version-controlled code with Git/GitHub
- Use WSL-Ubuntu as a consistent development environment
- Apply testing, debugging, and secure development practices

---

## 🧰 System Requirements

- **OS:** WSL 2 with Ubuntu 20.04 or 22.04
- **Python:** Python 3.10 or above
- **Git:** Latest Git version installed
- **Text Editor:** VS Code (optional but recommended)

---

## ⚙️ Setup Instructions (Ubuntu WSL)

```bash
# Update packages
sudo apt update && sudo apt upgrade -y

# Install Python and pip
sudo apt install python3 python3-pip -y

# Install Git
sudo apt install git -y

# (Optional) Install virtualenv
pip3 install virtualenv


## 📦 Required Python Libraries

```bash
pip3 install numpy pandas requests pylint pytest memory_profiler matplotlib psycopg2-binary pymongo websockets paho-mqtt

📁 Project Folder Structure
python-mini-course/
│
├── level-1-python-fundamentals/
├── level-2-oop/
├── level-3-dsa/
├── level-4-systems-networking/
├── extras/
├── resources/
├── README.md
├── LICENSE
└── .gitignore

🧠 Course Syllabus
🔹 Level 1: Python Fundamentals
Python Setup, Comments, Variables

Type Conversion, Input/Output, Operators

Control Flow: if, for, while, break, continue

Data Types: Numbers, Strings, List, Set, Tuple, Dictionary

Functions, Recursion, *args and **kwargs, Scopes

Modules, Packages, File Handling (txt, CSV, JSON, YAML)

Exception Handling (built-in, custom)

Advanced: List Comprehension, Lambda, Generator, Decorator, @property

RegEx, pip, assert, Debugging and Unit Testing


### 🔹 Level 2: Object-Oriented Programming (OOP)
- Classes, Objects, Attributes, Methods
- Constructors, `__str__`, `__repr__`
- Inheritance & Polymorphism
- Encapsulation & Abstraction
- Operator Overloading
- Class & Static Methods, Data Classes

✅ *Includes: class-based examples, test-driven OOP design, and `pdb` debugging*

---

### 🔹 Level 3: Data Structures and Algorithms (DSA)
- Big-O Complexity Analysis (Time/Space)
- Arrays, Linked Lists, Stacks, Queues
- Hash Maps, Sets, Dictionaries
- Trees, Binary Search Trees, Trie
- Graphs: BFS, DFS, adjacency lists
- Sorting and Searching Algorithms
- Optimized vs Brute-force Approaches
- Space & Time Complexity Comparison

✅ *Includes: problem-based exercises, `pytest`, and complexity breakdown*

---

### 🔹 Level 4: Linux System Programming & Networking

#### 📂 Linux System Basics
- File system layout, permissions, groups
- Process & package management
- Environment variables, system logs

#### 📡 Linux Networking
- IP address, hostname, routing
- Ports, ping, netstat, ss, nmap
- Firewall basics

#### 💻 Shell Scripting
- Bash scripting, loops, variables
- Automating Python scripts
- Cron jobs

#### 🌐 Internet Protocols with Python
- TCP, UDP, WebSockets
- MQTT, FTP, HTTP, SMTP
- DNS resolution, ICMP pings

| Protocol     | Use Case                     | Python Library           |
|--------------|------------------------------|--------------------------|
| TCP/UDP      | Socket Programming           | `socket`                 |
| HTTP/HTTPS   | REST APIs, Web Communication | `requests`, `httpx`      |
| MQTT         | IoT Messaging                | `paho-mqtt`              |
| WebSockets   | Real-time Communication      | `websockets`             |
| FTP/SFTP     | File Transfers               | `ftplib`, `paramiko`     |
| SMTP/IMAP    | Email Automation             | `smtplib`, `imaplib`     |
| DNS/ICMP     | Network Tools                | `scapy`, `ping3`         |

Folder suggestion:
```plaintext
extras/
└── 06_internet_protocols/
    ├── 01_tcp_udp_socket/
    ├── 02_http_requests/
    ├── 03_mqtt_pub_sub/
    ├── 04_websockets/
    ├── 05_ftp_smtp/
    └── 06_dns_icmp_tools/
```

---

✅ *Includes: real-world automation scripts, log parsing, and ping tools*

## 🛠️ Debugging & Profiling Tools

- `pdb` – step-by-step Python debugger
- `py-spy` – lightweight performance profiler
- `timeit` – check speed of code snippets
- `memory_profiler` – analyze memory usage

Examples provided in:  
`extras/04_python_debugging/` and  
`level-3-dsa/10_code_optimization/`

---

## 🔐 Secure Development Practices

- Secure credential handling (use `.env` files, avoid hardcoding secrets)
- Avoid unsafe eval/exec functions
- Input validation and sanitation (against XSS, injections)
- Basic GitHub security: use `.gitignore`, avoid leaking tokens

---

## 🧪 Practice Projects (Suggested)

- 🧮 Build a CLI calculator with tests
- 📋 Create a to-do app with JSON file storage
- 🌐 REST API using FastAPI or Flask
- 📊 Sensor simulator using MQTT + live dashboard
- 🧠 Interview-style DSA challenge set
- 📂 Backup automation script using `cron`
- 🧾 Web scraper with BeautifulSoup or Requests

---

## ✅ Optional Tools

- GitHub CLI / VS Code Git integration
- Notion or Obsidian for note-taking
- Jupyter for visual explanations
- UML drawing tools (e.g., diagrams.net)

---

## 🧾 License

This course is under the [MIT License](./LICENSE).

---

## ✨ Final Note

This is more than a course — it's a rebuild plan.  
One concept. One folder. One commit at a time.  
Be consistent, not perfect. Let's get started. 🚀

This course is ideal for:
- Self-paced learners and bootcampers
- Job seekers prepping for interviews
- Developers wanting to build solid Python foundations
- Anyone interested in backend systems and optimization

> “Write clean code. Learn the systems. Master the tools.”



---

## 🔐 Secure Python Development Practices

### ✅ Code-Level Security

- **Never hardcode secrets** – Use `.env` files + `python-dotenv`
- **Input validation** – Always sanitize external input
- **Avoid unsafe shell access** – Use `subprocess.run()` safely
- **Secure dependencies** – Use `pip-audit`, `safety`
- **Avoid wildcard imports** – Use explicit imports
- **Limit exposure** – Don’t expose test keys, ports, or tokens

### ✅ Git Repository Security

- **Use .gitignore** – Avoid tracking sensitive/runtime files
- **Scan commits for secrets** – Use `gitleaks` or `git-secrets`
- **Clean commit history if leaked** – Use `filter-branch` or BFG
- **Protect branches** – Enforce reviews + status checks on GitHub
- **Limit metadata leaks** – Don’t leave real server data in code

### ✅ Summary Checklist

| Layer         | Best Practice                         | Tool / Tip                 |
|---------------|----------------------------------------|----------------------------|
| Code          | Secrets in .env                        | `python-dotenv`            |
| Code          | Input validation, try-except           | Manual                     |
| Code          | Shell safety                           | `subprocess.run()`         |
| Code          | Dependency scan                        | `pip-audit`, `safety`      |
| Git           | Ignore sensitive files                 | `.gitignore`               |
| Git           | Secret scanning                        | `gitleaks`, `git-secrets`  |
| Git           | History cleanup                        | `filter-branch`, BFG       |
| GitHub        | PR protection                          | Branch settings            |

