from abc import ABC, abstractmethod

# State Class
class State:
    # Constructor for state class, checks if it is an accept state, reject state or regular state.
    # Accept and Reject states are both initialized manually at creation of the TM, not by the user.
    # However, they share the same constructor.
    # The first two conditional statements are only accessed one time when creating the accept and reject states
    def __init__(self, acceptStateIn, rejectStateIn, stateIDIn, initialStateIn):
        # Handle case when initializing the accept state
        if acceptStateIn and int(stateIDIn) == -1:
            self.acceptState = True
            self.rejectState = False
            self.stateID = -1
        # Handle case when initializing the reject state
        elif rejectStateIn and int(stateIDIn) == -2:
            self.rejectState = True
            self.acceptState = False
            self.stateID = -2
        # Handle case when initializing a regular state
        else:
            self.acceptState = False
            self.rejectState = False
            self.stateID = stateIDIn

        # Set initial state to true if the user wants to make this state the initial state
        if initialStateIn == "True":
            self.initialState = True
        else:
            self.initialState = False


# Transition Class
class Transition:
    # Transition class constructor
    def __init__(self, stateOneIDin, stateTwoIDin, symbolReadin, symbolWritein, directionin):
        self.stateOne, self.stateTwo = self.createRelations(stateOneIDin, stateTwoIDin)
        self.symbolRead = symbolReadin
        self.symbolWrite = symbolWritein
        self.direction = directionin

    # Function to add the type of relationship between state one and state two
    @staticmethod
    def createRelations(stateOneIDin, stateTwoIDin):
        # Check bounds of states
        # If state one is not in the stateList
        if stateOneIDin >= len(TM.statesList) or stateOneIDin <= -3:
            print()
            print("First state does not exist")
            print()
            return False
        # If state two is not in the stateList
        elif stateTwoIDin >= len(TM.statesList) or stateOneIDin <= -3:
            print()
            print("Second state does not exist")
            print()
            return False

        # First check state one (case handling)
        # If the first state is the accept state
        if stateOneIDin == -1:
            # Assign the accept state from statesList to the first state
            stateOne = TM.statesList[0]

            # Check for the second state cases.
            # If the second state is the accept state
            if stateTwoIDin == -1:
                stateTwo = TM.statesList[0]
            # If the second state is the reject state
            elif stateTwoIDin == -2:
                stateTwo = TM.statesList[1]
            # If the second state is a regular state
            else:
                stateTwo = TM.statesList[stateTwoIDin + 2]
        # If the first state is the reject state
        elif stateOneIDin == -2:
            # Assign the reject state from statesList to the second state
            stateOne = TM.statesList[1]

            # Check for the second state cases.
            # If the second state is the accept state
            if stateTwoIDin == -1:
                stateTwo = TM.statesList[0]
            # If the second state is the reject state
            elif stateTwoIDin == -2:
                stateTwo = TM.statesList[1]
            # If the second state is a regular state
            else:
                stateTwo = TM.statesList[stateTwoIDin + 2]
        # If the first state is a regular state
        else:
            stateOne = TM.statesList[stateOneIDin + 2]
            # If the second state is the accept state
            if stateTwoIDin == -1:
                stateTwo = TM.statesList[0]
            # If the second state is the reject state
            elif stateTwoIDin == -2:
                stateTwo = TM.statesList[1]
            # If the second state is a regular state
            else:
                stateTwo = TM.statesList[stateTwoIDin + 2]

        return stateOne, stateTwo


# Turing Machine Class
class TuringMachine(ABC):
    def __init__(self):
        # Tape variables
        self.headIndex = 0
        self.tapeMemory = []
        # List of states present in the turing machine
        self.statesList = []
        # List of transitions
        self.transitionList = []
        # State ID manipulation
        self.availableStateID = 0

        # Create a tape of size 5 with blanks
        for i in range(5):
            self.tapeMemory.append(" ")

    def displayTape(self):
        for i in range(len(self.tapeMemory)):
            element = self.tapeMemory[i]
            if element == " ":
                if i == self.headIndex:
                    print("|-| ", end='')
                else:
                    print("- ", end='')
            else:
                if i == self.headIndex:
                    print("|" + self.tapeMemory[i] + "| ", end='')
                else:
                    print(self.tapeMemory[i] + " ", end='')
        print()

    def addState(self, state):
        # Add state to the list of states
        self.statesList.append(state)
        # Increment ID available for next state creation
        self.availableStateID += 1

        # Display states
        self.displayStates()
        return True

    def removeState(self, stateID):
        # Check if user is trying to remove the accept state
        if stateID == -1:
            print("You can't remove the accept state.")
        # Check if user is trying to remove the reject state
        elif stateID == -2:
            print("You can't remove the reject state.")
        # Check if user is trying to remove a state that does not exist
        elif stateID >= len(self.statesList) or stateID <= -3:
            print("You can't remove a non-existent state.")
        # Else continue
        else:
            # Remove the state from the list
            self.statesList.remove(self.statesList[stateID + 2])
            # Inform the user
            print()
            print("State " + str(stateID) + " successfully removed.")
            print()

            # Display states
            self.displayStates()
            return True

        # If else block is not accessed, return False
        return False

    def displayStates(self):
        if len(self.statesList) != 0:
            print()
            print("-1 represents the accept state and -2 represents the reject state.")
            for i in range(len(self.statesList)):
                print("State: " + str(self.statesList[i].stateID) + ", ", end="")
            print()
            print()
        else:
            print()
            print("No states created yet.")
            print()

    # Function if the user wants to change the initial state
    def changeInitialState(self):
        # Get the list without the first two states (Accept and Reject states)
        sublist = self.statesList[2:]
        # Loop through the sublist
        for i in range(len(sublist)):
            # Check if there is an initial state in the TM
            if sublist[i].initialState:
                # Inform the user of the current state ID of the initial state and prompt for the ID to change.
                print("Current initial state: State " + str(sublist[i].stateID))
                print("Enter the ID of the initial state to disable initial state or other "
                      "IDs if you would like to change it to another state")
                self.displayStates()
                stateID = int(input("->"))

                # If the state ID does not exist
                if stateID >= len(self.statesList) or stateID <= -3:
                    print()
                    print("You can't set the initial state to a state that does not exist. ")
                    print()

                    return False
                # If the state ID given is the same as the original initial state, just disable it
                elif stateID == sublist[i].stateID:
                    sublist[i].initialState = False
                    print()
                    print("Initial state disabled.")
                    print()

                    return False
                # Else set the initial state to the new unique and in bounds state ID
                else:
                    sublist[i].initialState = False
                    sublist[stateID - 2].initialState = True

                    # Inform the user
                    print()
                    print("Initial state changed from State " + str(sublist[i].stateID)
                          + " to State " + str(sublist[stateID - 2].stateID))
                    print()

                    return True

        print()
        print("No initial state set yet.")
        print()
        return False

    def displayTransitions(self):
        print()
        indexNum = 1
        for transitionElement in self.transitionList:
            print(str(indexNum) +
                  ". (State  " + str(transitionElement.stateOne.stateID) + " -> State " +
                  str(transitionElement.stateTwo.stateID) + ", Symbol Read: " +
                  str(transitionElement.symbolRead) + ", Symbol Write: " +
                  str(transitionElement.symbolWrite) + ", Direction: " +
                  str(transitionElement.direction) + ")")
            indexNum += 1
        print()

    def addTransition(self, transitionIn):

        # Check
        if not (transitionIn.direction == "L" or transitionIn.direction == "R"):
            print()
            print("Not a valid transition, direction must be L or R")
            print()
            return False
        else:
            print()
            print("Transition added.")
            print()
            self.transitionList.append(transitionIn)
            self.displayTransitions()
            return True

    def removeTransition(self, transitionID):
        # Check if the transition list is empty
        if len(self.transitionList) == 0:
            print()
            print("No transitions created yet")
            print()
        # Check if the transition ID is out of bounds
        elif transitionToRemoveID <= 0 or transitionToRemoveID >= len(TM.transitionList):
            print()
            print("You can't remove a transition that does not exist.")
            print()
        # If transition list is not empty and the transition ID is not out of bounds, remove the transition
        else:
            self.transitionList.remove(self.transitionList[transitionID - 1])
            self.displayTransitions()

    @abstractmethod
    def updateHead(self, symbolToWrite, directionToMove):
        pass

    def checkLanguage(self, stringIn):
        stringElements = list(stringIn)

        # If the language is empty return true
        if stringElements[0] == "#":
            return True

        # Track current state
        currentState = ""

        # Get the initial state from the list of states
        for state in self.statesList:
            if state.initialState:
                currentState = state

        # If no current state initialized, return false
        if currentState == "":
            print()
            print("No initial state")
            print()
            return False

        # Loop through all the transitions and choose the one where the symbol being read from the expression is == to
        # the symbol read in the transition and where the currentState's id is == to the state one of the transition
        # Since TM's are deterministic, they are not allowed to have transition with the same symbol.
        transitionPicked = ""
        for element in stringElements:
            for currentTransition in self.transitionList:
                if (currentTransition.stateOne.stateID == currentState.stateID) and \
                        (currentTransition.symbolRead == element):
                    transitionPicked = currentTransition
            currentState = transitionPicked.stateTwo
            self.updateHead(transitionPicked.symbolWrite, transitionPicked.direction)
            self.displayTape()

        if currentState.stateID == -1:
            return True  # Language accepted

        return False  # Language rejected

    def clearTape(self):
        # Clear Contents
        for i in range(len(self.tapeMemory)):
            self.tapeMemory[i] = " "

        # Reset head to first cell in the tape
        self.headIndex = 0


# Turing machine with one-sided tape
class OneSidedTM(TuringMachine):
    def __init__(self):
        super().__init__()

    def updateHead(self, symbolToWrite, directionToMove):
        # Write symbol on tape
        self.tapeMemory[self.headIndex] = symbolToWrite

        # If the direction for the head is right
        if directionToMove == "R":
            # Check if the head is at the right end of the tape
            if self.headIndex == len(self.tapeMemory) - 1:
                # If true, add 5 more blank cells
                for i in range(5):
                    self.tapeMemory.append(" ")

            # Shift the head pointer to the right by one cell
            self.headIndex += 1
        # If the direction for the head is left
        elif directionToMove == "L":
            # Since this a one-sided tape TM, if the head is at the beginning of the tape, don't shift
            if self.headIndex == 0:
                pass
            # Else shift the head pointer to the left by one cell
            else:
                self.headIndex -= 1


class TwoSidedTM(TuringMachine):
    def __init__(self):
        super().__init__()

    def updateHead(self, symbolToWrite, directionToMove):
        # Write symbol on tape
        self.tapeMemory[self.headIndex] = symbolToWrite

        # If the direction for the head is right
        if directionToMove == "R":
            # Check if the head is at the right end of the tape
            if self.headIndex == len(self.tapeMemory) - 1:
                # If true, add 5 more blank cells
                for i in range(5):
                    self.tapeMemory.append(" ")

            # Shift the head pointer to the right by one cell
            self.headIndex += 1
        # If the direction for the head is left
        elif directionToMove == "L":
            # Since this a one-sided tape TM, if the head is at the beginning of the tape, don't shift
            if self.headIndex == 0:
                for i in range(5):
                    self.tapeMemory.insert(0, " ")
                    self.headIndex += 4
            # Else shift the head pointer to the left by one cell
            else:
                self.headIndex -= 1


def printCommands():
    print("1) Add a state")
    print("2) Remove a state")
    print("3) Add transition between states")
    print("4) Remove transition between states")
    print("5) Change initial state")
    print("6) Display States")
    print("7) Display Transitions")
    print("8) Continue")
    print("9) Quit")


print("Enter type of Tape for the TM: ")
print("1) One-sided Tape")
print("2) Two-sided Tape")
tmType = input("-> ")

TM = ""
if tmType == "1":
    TM = OneSidedTM()
    print("Design your One-sided TM:")
else:
    # TM = TwoSidedTM()
    print("Design your Two-sided TM:")

acceptState = State(True, False, -1, "False")
rejectState = State(False, True, -2, "False")
TM.statesList.append(acceptState)
TM.statesList.append(rejectState)

initialStateGiven = False
command = ""
while True:
    printCommands()
    command = input("-> ")

    # Add a state
    if command == "1":
        initialStateInput = "False"
        if not initialStateGiven:
            print("Is this the initial state? ('True' or 'False')")
            initialStateInput = input("->")
            if initialStateInput == "True":
                initialStateGiven = True
            else:
                initialStateGiven = False

        newState = State(False, False, TM.availableStateID, initialStateInput)
        TM.addState(newState)
    # Remove a state
    elif command == "2":
        if len(TM.statesList) <= 2:
            print()
            print("No states created yet.")
            print()
        else:
            stateIDToRemove = int(input("Enter State ID you would like to remove: "))
            TM.removeState(stateIDToRemove)
    # Add a new transition
    elif command == "3":
        # Ask user for the first state ID
        print("Enter the state ID for the first state:")
        stateOneID = int(input("->"))

        # Ask user for the second state ID
        print("Enter the state ID for the second state:")
        stateTwoID = int(input("->"))

        # Ask for the symbol read
        print("Enter the symbol read for the transition:")
        symbolRead = input("->")

        # Ask for the symbol to write when shift directions
        print("Enter the symbol you would like to update with for the transition:")
        symbolWrite = input("->")

        # Ask for the direction to move
        print("Enter the direction for the transition ('L' or 'R'):")
        direction = input("->")

        # Check if the direction is valid
        if direction not in ["L", "R"]:
            print()
            print("Not a valid direction, must be 'L' or 'R'.")
            print()
        else:
            # Initialize transition
            newTransition = Transition(stateOneID, stateTwoID, symbolRead, symbolWrite, direction)
            # Add transition to TM
            TM.addTransition(newTransition)
    # Remove an existing transition
    elif command == "4":
        # Prompt user
        TM.displayTransitions()
        print("Enter the transition ID you would like to remove:")
        transitionToRemoveID = int(input("->"))

        TM.removeTransition(transitionToRemoveID)
    # Change the initial state
    elif command == "5":
        TM.changeInitialState()
    # Display the states created
    elif command == "6":
        TM.displayStates()
    # Display the transitions created
    elif command == "7":
        TM.displayTransitions()
    # Add language and see if the TM accepts or rejects.
    elif command == "8":

        # Prompt user for language
        print("Enter expression")
        expression = input("->")

        # Display language to user
        print()
        print("E = " + expression)
        print()

        if TM.checkLanguage(expression):
            print()
            print("Expression Accepted.")
            print()
        else:
            print()
            print("Expression Rejected.")
            print()

        TM.clearTape()
    elif command == "9":
        print()
        print("Program has ended")
        print()
        break
    else:
        print()
        print("Not a valid command. Try again.")
        print()
