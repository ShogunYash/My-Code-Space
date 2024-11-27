# LED Multiplexed Display Controller Using VHDL  

This project implements a **4-digit LED display controller** using VHDL, designed to display four 4-bit binary inputs on a multiplexed seven-segment display. The design leverages modular components for timing, multiplexing, and decoding to ensure efficient and accurate operation.

---

## **Overview**  

The controller cycles through four binary inputs and displays their corresponding digits on a seven-segment display using **time-division multiplexing**. The **Timing Block** ensures precise refresh rates and input cycling, enabling seamless and flicker-free display updates.

---

## **Features**  

- **Precise Clock Division**:  
  - Reduces a 100 MHz input clock to a lower frequency (100 Hz) for refresh rate control.  

- **Time-Division Multiplexing**:  
  - Cycles through four inputs, activating one display at a time using the `anodes` signals.  

- **Modular Design**:  
  - Includes separate components for timing, multiplexing, and decoding for scalability.  

- **Real-Time Display Updates**:  
  - Efficiently switches between inputs to provide a seamless user experience.  

---

## **Core Components**  

1. **Timing Block**:  
   - **Clock Division**: Divides the 100 MHz clock to a suitable frequency for display refreshing.  
   - **Mux Select Signal**: Cycles through four display inputs using a counter-based state machine.  
   - **Anode Control**: Activates one display at a time based on the counter state.  

2. **MUX4**:  
   - Selects one of the four 4-bit inputs (`input0` to `input3`) for display.  

3. **Seven Segment Decoder**:  
   - Converts a 4-bit binary input to seven-segment signals (`a` to `g`) for display.  

---

## **Implementation Details**  

- **Language**: VHDL  
- **Tools**: Vivado Design Suite  
- **Key Techniques**:  
  - Clock division for display refresh rates.  
  - Time-division multiplexing for efficient LED control.  
  - Modular and scalable design for flexibility.  

---

## **How to Run**  

1. Clone the repository:  
   ```bash
   git clone https://github.com/ShogunYash/My-Code-Space.git
   cd My-Code-Space

