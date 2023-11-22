## Cross Currency Arbitrage Detector

### Description

    This is assigment of the course "Alogrithm Design and Analysis" at CJLU - AUT Joint BCIS Program 2023.
        
    This project implements a program that detects arbitrage opportunities in currency exchange rates.

### Usage

    The program is written in Python 3.9.18, using the following libraries:
    - requests
    - numpy

### Quick Start

        1. Clone the repository
        2. Run the program
            - Install the required libraries:
                pip install -r requirements.txt
            - Run the program:
                python main.py
        3. Check the output result
        e.g.:
        ```
            # Test case 1
            There exists arbitrage opportunity in this currency exchange system.
            USD -> EUR -> CNY -> USD
            Profit margin is 1.060395672
            
            # Test case 2
            There is no arbitrage opportunity in this currency exchange system.
            
            # Test case 3 from real world data
            There exists arbitrage opportunity in this currency exchange system.
            NZD -> HKD -> NZD
            Profit margin is 1.00000051326
            There exists arbitrage opportunity in this currency exchange system.
            HKD -> NZD -> HKD
            Profit margin is 1.00000051326
        ```
    