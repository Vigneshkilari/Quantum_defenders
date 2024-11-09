# Rogue Wi-Fi Access Point Detection and Network Packet Analyzer for Intrusion Detection

## Overview

This project, **Rogue Wi-Fi Access Point Detection and Network Packet Analyzer for Intrusion Detection**, aims to enhance network security by combining rogue Wi-Fi detection and real-time packet analysis. Using anomaly detection and blockchain-based logging, it identifies unauthorized access points (APs) and malicious network activities, ensuring integrity and auditability of security events.

### Key Features

1. **Rogue Wi-Fi Access Point Detection**
   - Scans Wi-Fi networks for untrusted APs, identifying "evil twins" that mimic legitimate networks.
   - Validates APs by comparing SSID and MAC address against a trusted network list.
   - Alerts administrators through configurable channels (email, SMS, or dashboard).

2. **Network Packet Analyzer**
   - Captures and filters network traffic in real-time, analyzing protocols like TCP, UDP, and HTTP.
   - Uses anomaly detection to identify suspicious patterns and potential intrusions.
   - Generates detailed reports on traffic activity and flagged events.

3. **Blockchain Integration for Secure Logging**
   - Logs critical security events on the Polygon blockchain for tamper-proof, immutable records.
   - Provides transparency and auditability for security compliance and investigation.

4. **Dashboard Interface**
   - Real-time monitoring of network status, rogue APs, and flagged traffic anomalies.
   - Data visualizations and interactive alerts enable quick responses to potential threats.

---

## Table of Contents
- [Project Objectives](#project-objectives)
- [Technology Stack](#technology-stack)
- [Installation and Setup](#installation-and-setup)
- [Usage Guide](#usage-guide)
- [Architecture Overview](#architecture-overview)
- [Testing and Optimization](#testing-and-optimization)
- [Challenges](#challenges)
- [Future Improvements](#future-improvements)
- [License](#license)

---

## Project Objectives

1. **Rogue AP Detection**: Detect and alert unauthorized APs that may attempt to impersonate legitimate networks.
2. **Intrusion Detection via Packet Analysis**: Identify malicious network activities, such as unauthorized data transfers and port scans.
3. **Blockchain Integrity**: Securely log security events for tamper-proof auditing.
4. **Real-Time Monitoring**: Display insights on a user-friendly dashboard with visualizations and interactive alerts.

---

## Technology Stack

- **Programming Language**: Python
- **Wi-Fi Detection and Packet Analysis**: `Scapy`, `Pyshark`
- **Anomaly Detection**: `scikit-learn` for statistical and machine learning models
- **Blockchain Integration**: `web3.py` for Polygon blockchain logging
- **Dashboard**: Flask (backend), HTML/CSS/JavaScript with Chart.js for visualizations
- **Database**: SQLite for local storage, with selective logs sent to Polygon blockchain for tamper-proof records

---
## Usage Guide

- **Rogue AP Detection**: The script scans nearby Wi-Fi networks, checks SSIDs and MAC addresses against a trusted list, and flags any anomalies as rogue APs.
- **Network Packet Analysis**: Captures packets and inspects traffic for patterns indicative of malicious activity, logging results to the dashboard.
- **Real-Time Dashboard**: Displays alerts, traffic volume graphs, protocol distribution, and more. Access the dashboard at [http://localhost:5000](http://localhost:5000).

---

## Architecture Overview

- **Rogue AP Detection Module**: Scans networks using Scapy and Pyshark to identify suspicious APs and flag evil twins.
- **Packet Capture and Analysis**: Filters and analyzes packets in real-time, using machine learning to detect abnormal traffic.
- **Blockchain Logging**: Logs critical security events to the Polygon blockchain, ensuring the integrity and immutability of network events.
- **Dashboard**: Provides a UI for monitoring alerts, viewing traffic patterns, and responding to threats.

---

## Testing and Optimization

- **Unit Testing**: Each module includes unit tests for functionality validation.
- **Load Testing**: Simulate traffic loads to evaluate performance.
- **False Positive Reduction**: Fine-tune anomaly detection thresholds to reduce incorrect flagging of legitimate APs.

---

## Challenges

- **Network Overhead**: Managing high traffic volumes in real-time can be resource-intensive.
- **False Positives**: Rogue AP detection may occasionally misidentify legitimate networks, requiring ongoing optimization.
- **Blockchain Costs**: Logging all events may incur high costs; selectively log only critical events to optimize.

---

## Future Improvements

- **Enhanced Machine Learning**: Integrate deep learning for improved anomaly detection accuracy.
- **Cross-Platform Compatibility**: Extend functionality to mobile platforms for broader usability.
- **Distributed Logging**: Investigate using decentralized storage for additional data security and redundancy.
