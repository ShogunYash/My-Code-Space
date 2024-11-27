# Strategic Simulations and Optimal Play: Mind Games in Probabilistic and Adaptive Environments  

This project explores probabilistic modeling, adaptive strategies, and optimal decision-making using modular arithmetic, Monte Carlo simulations, and recursive computations. The primary focus is on developing robust algorithms to analyze and predict outcomes in strategic games involving Alice and Bob as players.

---

## **Overview**  

The project delves into the mathematics and strategy behind competitive games with the following objectives:  
1. **Calculate Winning Probabilities**: Use modular arithmetic to compute probabilities of outcomes in constrained scenarios.  
2. **Analyze Game Duration and Variance**: Predict expected game rounds and their variance.  
3. **Simulate Adaptive Strategies**: Model and simulate Alice and Bob's decisions using predefined and adaptive strategies.  
4. **Optimize Future Strategies**: Use dynamic programming and recursive computations to determine optimal strategies for maximizing points.

---

## **Features**  

- **Modular Arithmetic Operations**:  
  - Efficient implementation of modular addition, multiplication, and division for constrained computations.  

- **Monte Carlo Simulations**:  
  - Adaptive and probabilistic strategies for Alice and Bob, evolving based on game outcomes.  

- **Recursive Probability and Expectation Calculations**:  
  - Dynamic programming approach to calculate probabilities, expectations, and variances for game outcomes.  

- **Optimal Strategy Planning**:  
  - Recursive algorithms for determining Alice's best strategies based on current and future rounds.  

---

## **Core Components**  

### **1. Modular Arithmetic Functions**  
- Implements modular addition, multiplication, and division under a fixed modulus (1000000007).  
- Enables efficient computation for constrained probability and variance calculations.  

### **2. Game Duration and Probability (Question 1)**  
- Calculates the probability of Alice winning specific rounds using recursive DP.  
- Computes the expected value and variance of game outcomes.  

### **3. Adaptive Strategy Simulation (Question 2)**  
- Simulates rounds between Alice and Bob using a payoff matrix.  
- Bob and Alice adapt their strategies based on the results of previous rounds.  
- Monte Carlo simulations analyze long-term outcomes over large numbers of rounds.  

### **4. Optimal Strategy Calculation (Question 3)**  
- Determines the optimal strategy for Alice to maximize points in future rounds.  
- Uses a payoff matrix and dynamic programming to compute best strategies and expected points recursively.  

---

## **Implementation Details**  

- **Language**: Python  
- **Techniques**:  
  - Modular arithmetic for constrained calculations.  
  - Monte Carlo simulations for probabilistic modeling.  
  - Recursive computations and dynamic programming for optimal strategy design.  

---

## **How to Run**  

1. Clone the repository:  
   ```bash
   git clone https://github.com/ShogunYash/My-Code-Space.git
   cd My-Code-Space/Mind-Games

