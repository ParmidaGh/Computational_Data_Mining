<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f172a,35:1d4ed8,70:7c3aed,100:059669&height=220&section=header&text=Computational%20Data%20Mining&fontSize=38&fontColor=ffffff&fontAlignY=50&animation=fadeIn" />
</div>

---

# Computational Data Mining: Linear Algebra, Spectral Methods, and Markov Models from Scratch

A collection of hands-on implementations of the numerical and probabilistic foundations of data mining, covering matrix subspaces, eigenvalue computation, QR factorization, and Markov chain modeling, each built from first principles in Python.

<div align="left">

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![NumPy](https://img.shields.io/badge/NumPy-Numerical_Computing-013243?style=flat&logo=numpy&logoColor=white)](https://numpy.org/)
[![SymPy](https://img.shields.io/badge/SymPy-Symbolic_Mathematics-3B5526?style=flat&logo=sympy&logoColor=white)](https://www.sympy.org/)
[![NetworkX](https://img.shields.io/badge/NetworkX-Graph_Modeling-2E7D32?style=flat)](https://networkx.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557C?style=flat)](https://matplotlib.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=flat&logo=jupyter&logoColor=white)](https://jupyter.org/)
[![Linear Algebra](https://img.shields.io/badge/Topic-Linear_Algebra-1D4ED8?style=flat)](#)
[![Markov Chains](https://img.shields.io/badge/Topic-Markov_Chains-059669?style=flat)](#)
[![License](https://img.shields.io/badge/License-MIT-4B5563?style=flat)](https://opensource.org/licenses/MIT)

</div>

## Abstract

Most data mining techniques rest on a small set of mathematical building blocks: vector spaces, matrix factorizations, eigen-analysis, and probabilistic state models. This repository gathers the computational projects completed for the Computational Data Mining course at the University of Tehran. Each project implements a core algorithm directly rather than calling a library routine, making the underlying mechanics transparent. The collection spans Gauss-Jordan elimination with fundamental subspace extraction, the Power Method with Gram-Schmidt QR decomposition, and Markov chain simulation with graph visualization.

## Table of Contents

1. [Overview](#overview)
2. [Key Features](#key-features)
3. [Projects](#projects)
4. [Topic Map](#topic-map)
5. [Tools and Technologies](#tools-and-technologies)
6. [Repository Structure](#repository-structure)
7. [Installation and Usage](#installation-and-usage)
   - [Clone Repository](#clone-repository)
   - [Run a Project](#run-a-project)
8. [License](#license)
9. [Author](#author)
10. [Support](#support)

---

# Overview

**Computational Data Mining** is a structured portfolio of three self-contained projects. Each lives in its own folder with a dedicated README, a runnable implementation, and built-in test cases, so every algorithm can be explored independently.

The repository is designed around three ideas:

* Understand each algorithm by implementing its core steps manually
* Verify results through reproducible test cases and example outputs
* Connect classical numerical methods to their roles in modern data mining

---

# Key Features

* Gauss-Jordan elimination with null, row, and column space basis extraction
* Dominant eigenpair estimation using the Power Method
* QR decomposition through the Gram-Schmidt process
* Markov chain modeling with multi-step probabilities and path simulation
* Heat map and directed graph visualization
* Interactive console input alongside built-in test cases
* One dedicated README per project

---

# Projects

| Project | Focus | Core Methods |
|:---------|:-------|:--------------|
| [Fundamental Subspaces Analyzer](./Fundamental_Subspaces_Gauss_Jordan) | Structure of the linear system represented by a matrix | Gauss-Jordan elimination, null space, row space, column space, linear combinations of dependent columns |
| [Power Method and QR Decomposition](./Power_Method_and_QR_Decomposition) | Eigenvalue computation and orthogonal factorization | Power Method, Gram-Schmidt orthogonalization, QR decomposition |
| [Markov Chain Analysis](./Markov_Chain) | Probabilistic state transitions between cities | Transition matrices, matrix powers, stochastic simulation, graph visualization |

---

# Topic Map

```mermaid
flowchart LR

A[Computational Data Mining]

A --> B[Matrix Structure]
A --> C[Spectral and Orthogonal Methods]
A --> D[Probabilistic Models]

B --> B1[Gauss-Jordan Elimination]
B --> B2[Fundamental Subspaces]

C --> C1[Power Method]
C --> C2[Gram-Schmidt QR]

D --> D1[Markov Chains]
D --> D2[Graph Visualization]

B2 -.-> E[Dimensionality Reduction]
C1 -.-> F[PageRank and Spectral Analysis]
C2 -.-> G[Least Squares]
D1 -.-> F
```

These methods connect directly to practical data mining tasks: rank and subspace analysis supports feature redundancy detection and dimensionality reduction, eigenvalue methods underlie PageRank and spectral techniques, QR factorization supports least-squares solving, and Markov chains model sequential and navigational behavior.

---

# Tools and Technologies

| Component | Purpose |
|:-----------|:---------|
| Python | Core implementation language |
| NumPy | Matrix operations, norms, and sampling |
| SymPy | Exact symbolic null space computation |
| NetworkX | Directed graph construction |
| Matplotlib | Heat map and graph visualization |
| Jupyter Notebook | Interactive execution for notebook-based projects |

---

# Repository Structure

```text
Computational_Data_Mining
│
├── Fundamental_Subspaces_Gauss_Jordan/
│   ├── fundamental_subspaces_analyzer.py
│   └── README.md
│
├── Power_Method_and_QR_Decomposition/
│   ├── power_method_and_gram_schmidt_qr.ipynb
│   └── README.md
│
├── Markov_Chain/
│   ├── markov_chain_city_transitions.py
│   └── README.md
│
└── README.md
```

---

# Installation and Usage

## Clone Repository

```bash
git clone https://github.com/ParmidaGh/Computational_Data_Mining.git

cd Computational_Data_Mining
```

## Run a Project

Enter a project folder and follow the instructions in its README. For example:

```bash
cd HW1_Fundamental_Subspaces_Gauss_Jordan

python fundamental_subspaces_analyzer.py
```

---

# License

This project is licensed under the MIT License.

---

## Author

**Parmida Ghamari**
M.Sc. Student, University of Tehran
Research Assistant @ Social Networks Lab

**Research Interests:** Computational Data Mining, Numerical Linear Algebra, Matrix Factorization, Stochastic Processes, Natural Language Processing

📧 [Parmida.ghamari@gmail.com](mailto:Parmida.ghamari@gmail.com) | 💻 [github.com/ParmidaGh](https://github.com/ParmidaGh) | 💼 [linkedin.com/in/parmida-ghamari](https://www.linkedin.com/in/parmida-ghamari)

---

## Support

If you find this repository useful, consider giving it a star ⭐️

---

<p align="center">
Built with Python, NumPy, SymPy, NetworkX, and Matplotlib
</p>
