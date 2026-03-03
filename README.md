# Python Snippets

Small Python experiments and standalone scripts exploring different core Python concepts.

This repository contains short programs and single-file examples used to practice:

- Concurrency (threading, multiprocessing, asyncio)
- Mathematical simulations
- Inter-process communication
- Event-driven programming
- Core Python language features

---

## 📂 Contents

### 🔢 Monte Carlo π Estimation (asyncio)
Estimate π using a Monte Carlo simulation with asynchronous tasks.

Concepts covered:
- `async` / `await`
- `asyncio.gather`
- Cooperative multitasking
- CPU-bound vs async limitations

---

### 🧵 Multiprocessing – Rock, Paper, Scissors
Simulation of a multi-process rock-paper-scissors game:

- 3 child processes
- Parent process as referee
- Communication via `multiprocessing.Pipe`
- Tie-break logic
- Process lifecycle management

Concepts covered:
- IPC (Inter-Process Communication)
- Process synchronization
- Parent/child process architecture

---

### 🔥 Prime Numbers – Parallel Computation
Compare different concurrency models for CPU-bound tasks:

- Sequential execution
- `threading`
- `multiprocessing`

Used to explore:
- Global Interpreter Lock (GIL)
- Performance differences
- True parallelism vs concurrency

---

## 🚀 Purpose

This repository serves as:

- A personal learning sandbox
- A reference for concurrency patterns
- A collection of small reproducible experiments

---

## 🧠 Topics Explored

- `threading`
- `multiprocessing`
- `asyncio`
- Random simulations
- Performance comparison

---

## 📌 Notes

Most examples are educational and focus on understanding behavior rather than production optimization.

---

## 🧑‍💻 Author

Personal experimentation repository.
