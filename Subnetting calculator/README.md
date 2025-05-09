# 🧮 Subnet Calculator

A Python script to calculate subnet details including network address, broadcast address, usable IP range, and CIDR for a given IPv4 address and subnet mask.

---

## 🔧 Features
- Validates IPv4 addresses and subnet masks
- Calculates:
  - Network address
  - Broadcast address
  - Usable host IP range
  - CIDR notation
  - IP class
- Supports /CIDR and dotted decimal inputs

---

## 🚀 How to Run

```bash
python subnet_calculator.py

Enter IP address: 192.168.1.10
Enter subnet mask (CIDR or dotted): 255.255.255.0
```
## 📒 Sample Output
  IP Class: C
  CIDR Notation: /24
  Network Address: 192.168.1.0
  Usable IP Range: 192.168.1.1 - 192.168.1.254
  Broadcast Address: 192.168.1.255
