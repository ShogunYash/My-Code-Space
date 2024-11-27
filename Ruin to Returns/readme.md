# Ruin to Return: Probabilistic Analysis of Gambler's Game Dynamics  

This project explores probabilistic models related to gambling scenarios, focusing on wealth transitions, game durations, and winning probabilities. The algorithms are developed to analyze outcomes based on recursive formulations, stationary distributions, and binary precision techniques for enhanced computational accuracy.

---

## **Overview**

The project addresses key problems related to gambling dynamics:  
1. **Winning Probability**: Calculate the probability of a gambler reaching a specified wealth threshold before going bankrupt.  
2. **Expected Game Duration**: Determine the expected number of rounds a gambler plays before quitting or reaching specified limits.  
3. **Markov Chain Stationary Distribution**: Analyze the long-term distribution of wealth states and compute expected wealth.  
4. **Binary Precision Techniques**: Use high-precision binary representations for accurate probabilistic calculations.  

---

## **Features**

- **Winning Probability**:  
  - Calculates the likelihood of a gambler achieving a wealth goal before going bankrupt.
  - Supports scenarios with finite wealth thresholds and infinite wealth goals.
  
- **Expected Game Duration**:  
  - Computes the number of rounds before the game ends, considering win/lose probabilities.
  - Incorporates recursive calculations and binary representations for precision.  

- **Markov Chain Analysis**:  
  - Derives stationary distributions for long-term behavior in wealth transitions.  
  - Computes the expected wealth using Markov chain probabilities.  

---

## **Core Algorithms**

1. **Win Probability Calculation**  
   - Implements a formula-based and recursive approach for finite and infinite wealth scenarios.  

2. **Game Duration**  
   - Uses binary representation of `k/N` with high precision for accurate duration estimates.  

3. **Stationary Distribution**  
   - Computes long-term wealth probabilities using iterative normalization techniques.  

4. **Expected Wealth and Time**  
   - Calculates the gambler's expected wealth and the time required to reach specific states.  

---

## **Implementation Details**

- **Languages**: Python  
- **Key Techniques**:  
  - Recursive algorithms for state-based transitions.  
  - High-precision binary representations for accurate probabilistic calculations.  
  - Markov chain modeling for stationary distribution and wealth estimation.  

---

## **How to Run**  

1. Clone the repository:
   ```bash
   git clone https://github.com/ShogunYash/My-Code-Space.git
   cd My-Code-Space

