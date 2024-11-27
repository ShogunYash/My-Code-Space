# Optimized Flight Route Planner with Cost and Time Constraints  

## Overview  
This project implements an efficient flight route planning system capable of finding the best paths between cities based on various optimization criteria such as minimizing flight counts, costs, or a combination of both. It features robust data structures and algorithms, including priority queues, heaps, and adjacency lists, to ensure scalability and performance.  

## Key Features  
- **Least Flights, Earliest Route:** Finds the quickest path in terms of the number of flights and earliest arrival.  
- **Cheapest Route:** Calculates the route with the minimum fare while adhering to time constraints.  
- **Least Flights, Cheapest Route:** Balances the number of flights and total fare for an optimal route.  
- **Dynamic Validity Checks:** Ensures routes adhere to layover and time window constraints.  

## Components  
1. **Flight Class:** Represents individual flights with attributes like flight number, start city, departure time, end city, arrival time, and fare.  
2. **Data Structures:**  
   - **Queue:** For breadth-first search in least flights calculation.  
   - **Heap:** A priority queue for optimized extraction in cost and time-based route planning.  
3. **Planner Class:** Implements core algorithms for route planning, adjacency list construction, and backtracking to retrieve paths.  
4. **Utility Functions:** Include path reconstruction, time validation, and flight comparison.  

## Algorithms  
- **Breadth-First Search (BFS):** Used for finding the least flights and earliest routes.  
- **Priority Queues:** Optimizes extraction based on fare or flight counts using custom comparison functions.  
- **Backtracking:** Reconstructs the flight path from the final destination to the start city.  

## Input Details  
- **Flights:** Each flight includes a unique identifier, start and end cities, departure and arrival times, and fare.  
- **Cities:** Represented as integers starting from 0, where each integer corresponds to a unique city.  
- **Time:** Modeled as a continuous, non-negative integer starting from `t=0`.  

## How to Use  
1. Clone the repository:  
   ```bash
   git clone https://github.com/ShogunYash/My-Code-Space.git  
   cd My-Code-Space/Mind-Games  

