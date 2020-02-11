# Nintendo switch input modifier

An python-arduino based nintendo switch input modifier.

You'll an Arduino UNO, an FT1232 and a few jumpers.

## 1. First burn the control emulation firmware on the arduino

Make sure the Arduino has burned a code that does not use the serial interface and follow [these steps](https://www.arduino.cc/en/Hacking/DFUProgramming8U2) but instead of burning the lastest arduino firmware, burn the `joysicth.hex` firmware, wich is located at the `firmware` folder.

## 2. Mount the FT1232 circuit and connect it to your computer

In the `electronics` folder of this repo you can find photos of the electronic FTID - Arduino UNO circuit

## 3. Connect your pro-controller via bluetooth to your computer

Connect your pro-controller to the PC like a normal bluetooth device

## 4. Find your bluetooth controller event port

Go to `/dev/input`, you should see a lot of folder that start with `event`, disconnect your controller, execute `ls` to check the events that does no belong to your controller, then connect your controller again and execute `ls`, the new folder is the event folder of your controller.

## 5. Find serial port in wich the the FT1232 is connected

run at a terminal

```
dmesg | grep tty
```

and search for the line that says: `FTDI USB Serial Device converter now attached to`, at the end of that line you can find the serial port in wich your FTID is connected

## 6. Edit `bridge.py` in order to fit to your ports/setup

at the lines 7, 8 and 9 of `bridge.py` put your controller event folder path at the first line, your FTID serial port at the second line and comment or uncomment the line 9/10 in order to switch controller mapping.

## 7. connect your arduino to the nintendo/PC that will control

Make sure the last steps were executed successfully and then connect your arduino to the device that will control. Then run `bridge.py` script. It may fail a few times, just retry until your computer in controlling your switch/PC
