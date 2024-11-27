# AES-128 Bit Decryption System on FPGA  

This project implements an **AES-128 bit decryption system** using VHDL, designed for FPGA deployment. The system utilizes a Finite State Machine (FSM) to manage the decryption pipeline through 10 rounds of inverse AES operations, ensuring efficient and secure decryption of ciphertext.

---

## **Overview**

The project focuses on the hardware implementation of the AES decryption algorithm, emphasizing modularity, resource optimization, and accuracy. It is designed for FPGA platforms, making it suitable for high-speed, hardware-based cryptographic applications.

---

## **Features**

- **Finite State Machine (FSM)**:  
  - Controls the decryption flow through states like `AddRoundKey`, `InvShiftRows`, `InvSubBytes`, and `InvMixColumns`.
  
- **Modular Design**:  
  - Separate components for each AES operation, enabling reusable and scalable implementation.  

- **Efficient Resource Usage**:  
  - Utilizes single-port ROMs for ciphertext and precomputed round keys, minimizing hardware overhead.  

- **Hardware-Compatible**:  
  - Designed and tested for Vivado FPGA tools, ensuring seamless deployment.  

---

## **Core Components**

1. **Ciphertext and Round Key ROMs**  
   - Stores the encrypted data and precomputed round keys for efficient access during decryption.  

2. **AES Operation Modules**  
   - `AddRoundKey`: Combines the current state with the round key using bitwise XOR.  
   - `InvShiftRows`: Performs inverse row-wise shifts in the AES state matrix.  
   - `InvSubBytes`: Implements the inverse S-box transformation.  
   - `InvMixColumns`: Applies the inverse column-wise mixing for rounds 1-9.  

3. **Finite State Machine (FSM)**  
   - Manages the decryption process across multiple rounds, ensuring correct sequencing of operations.  

---

## **Implementation Details**

- **Language**: VHDL  
- **Tools**: Vivado Design Suite  
- **Key Techniques**:  
  - FSM-based control flow for round operations.  
  - ROM-based storage for efficient data retrieval.  
  - Modular design for scalability and debugging.  

---

## **How to Run**

1. Clone the repository:
   ```bash
   git clone https://github.com/ShogunYash/My-Code-Space.git
   cd My-Code-Space

