# Qt6 Example using QThreads
This example project is created from several qt references. 
It is a QtQuick QML application using PySide6 bindings. 
Developed using Qt Version 6.2.

## Motivation: 

Since i had notorious problems to create threadsafe applications i created this project for reference only. 

## Functionality: 

An Qt Quick application is created to show several buttons, a label and a TextArea. 
A controller class is connected to QML engine using QML_ELEMENT macro implementing connection between worker thread and GUI. 
The worker thread can be started, stopped and reset from GUI and the GUI is updated using signals and slots. 

## Usage: 

With buttons the user can controll the application. TextArea is used to show results from application. A Label shows Text from message-buttons and a progressbar shows overall threadloop-progress. 

### Test GUI-Threads

With buttons "Message 1" and "Message 2" the Label's text can be changed to test if main thread is deadlocked. 

### Start worker thread

With button "Run fibonacci" the worker thread gets started.

### Stop worker thread

With the button "Interrupt" the requestInterrupt() slot of the workerthread is called which is handled inside of the run() method.

### Reset workerthread loop

The run() method of the workerthread uses an integer to calculate fibonacci numbers. the loop stops if a set value is reached.
With the button "Reset threadloop" this counter is reset to 0 using a connection between controller's signal and a slot in workerthread. 


