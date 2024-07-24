# BeeMyCoCreator
A collaborative music project involving multiple people and a robotic arm. It generates subsequent melodies using a recurrent neural network based on user input notes.

![image](https://github.com/RachelR1001/BeeMyCoCreator/assets/148432322/e22bafbd-ed82-4210-897c-ae683b23b32c)


![image](https://github.com/RachelR1001/BeeMyCoCreator/assets/148432322/6269085a-7ce6-4d0b-b918-0888517728dd)


## Table of Contents

- [Introduction](#introduction)
- [Prototype](#Prototype)

## Introduction
**1. Background** 

  Current research has predominantly focused on the co-creative process between humans and AI collaborators. However, there is a scarcity of research exploring multi-person co-creation of music involving AI and robotic arms. Furthermore, additional investigation is necessary to elucidate the role of tangibility in such a system.
Consequently, we aim to explore the impact of incorporating tangible interfaces (robotic arms) and various modes of AI involvement on user experience within this creative process.

**2. Computational Pipeline** 

  - Stage 1: Data Transformation
    - Transmit user-inputted notes signals from a physical device to the server via WebSocket protocol
    - Convert the notes data into MIDI pitches

  - Stage 2: Melody Generation
    - Chord Extraction: Extract chord information from received notes to support harmonic context for melody generation.
    - Sequence Quantization: Transform the note sequence into a quantized format, dividing time into specific steps, for input to the machine learning model.
    - Melody Continuation: Use the Recurrent Neural Network model (MusicRNN) to predict and generate the continuation of a note sequence, returning the extended sequence.

  - Stage 3: Musical Rendering
    - Map the computed melody to physical spatial positions, and use a robotic arm equipped with OpenCV to detect, recognize, and play the physical piano keys.

**3. System Overview & Co-Creation Modes** 
![image](https://github.com/RachelR1001/BeeMyCoCreator/assets/148432322/e0f30d21-c09d-4c03-8d9d-8fa1fee51e62)

![image](https://github.com/RachelR1001/BeeMyCoCreator/assets/148432322/90b59c60-29b6-4231-a935-fc4628423c74)

## Prototype
![3ca7563b7b5d1310e7c7623f81ffd280](https://github.com/user-attachments/assets/f17a717c-eb0c-4bfd-8d5e-9442cc3e07e6)

Demo Video: https://drive.google.com/file/d/1BKs5SPSQnY_7f82DKYORGSf-so-rsW5b/view?usp=sharing
