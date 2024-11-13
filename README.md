# Turing Machine Simulator

A Python-based Turing Machine simulator that allows users to design, configure, and execute Turing Machines (TMs) with one-sided or two-sided tapes. This simulator includes functionality for defining states, adding transitions, setting an initial state, and checking if an input language is accepted or rejected by the machine.

## Features
- **State Management**: Create, remove, and manage accept, reject, and standard states.
- **Transitions**: Define transitions between states with customizable read and write symbols and directional movement (left or right).
- **Tape**: Simulate a one-sided or two-sided tape, with dynamic resizing for storage during computation.
- **Execution**: Load a string onto the tape and check if the Turing Machine accepts or rejects it based on the defined states and transitions.
- **Interactive Console Interface**: Provides commands for configuring the Turing Machine and executing the language check.

## Classes Overview

### `State`
Represents a state in the Turing Machine, which can be an accept, reject, or regular state.
- **Parameters**:
  - `acceptStateIn`: Boolean indicating if this is an accept state.
  - `rejectStateIn`: Boolean indicating if this is a reject state.
  - `stateIDIn`: Unique ID for each state.
  - `initialStateIn`: Boolean indicating if this is the initial state.

### `Transition`
Defines transitions between states based on input symbol, output symbol, and directional movement.
- **Parameters**:
  - `stateOneIDin`: ID of the starting state.
  - `stateTwoIDin`: ID of the destination state.
  - `symbolReadin`: Symbol the machine reads to trigger this transition.
  - `symbolWritein`: Symbol the machine writes during this transition.
  - `directionin`: Direction of the head movement (`L` for left, `R` for right).

### `TuringMachine` (Abstract Base Class)
Base class for Turing Machines, containing common attributes and methods. Includes tape initialization, state and transition handling, and core Turing Machine logic.
- **Attributes**:
  - `tapeMemory`: List representing the machine's tape.
  - `statesList`: List of all states in the machine.
  - `transitionList`: List of all transitions.
  - `headIndex`: Position of the tape head.

### `OneSidedTM` and `TwoSidedTM`
Subclasses of `TuringMachine` for specific machine types:
- **`OneSidedTM`**: Simulates a Turing Machine with a one-sided tape (no movement allowed to the left of the starting position).
- **`TwoSidedTM`**: Simulates a Turing Machine with a two-sided tape, allowing movement in both directions.

## Installation
To use the Turing Machine simulator, clone this repository and ensure you have Python 3 installed.
