# OS_Task1
implementations of the Producer-Consumer problem and matrix multiplication for Operating Systems.

# Operating Systems Programs

This repository contains Python implementations of programs based on concepts covered in the Operating Systems course.

## Programs Included

### 1. Producer-Consumer Problem

The Producer-Consumer problem is implemented using Python. The program consists of a producer that adds items to a shared buffer and a consumer that removes items from the buffer.

The buffer has a fixed maximum capacity. The program handles the conditions where the buffer becomes full or empty and ensures that the producer and consumer operate correctly.

**File:** `producer_consumer.py`

### 2. Matrix Multiplication

The program performs multiplication of two 100 × 100 matrices. The matrices are generated with random values, and the resulting matrix is calculated using separate threads for each result cell.

The program performs a total of 1,000,000 multiplication operations and displays the progress of the calculation through an animation.

**File:** `matrix_multiplication.py`

The generated animation is saved as:

`matrix_multiplication.gif`

## Technologies Used

- Python 3
- Matplotlib
- Pillow

## How to Run

### Producer-Consumer Problem

```bash
python producer_consumer.py
