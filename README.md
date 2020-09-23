## Programming of Internet of Things (COSC2755)

# Description:
The following project was developed as a part of Internet of Things, otherwise known as IOT for the Raspberry Pi utilising the sense hat attachment. The project essentially lets the user use the joystick on the pi to browse through a menu which has various programs of different display capabilities. 

- The first program generates different emojis and displays on pressing the joystick. 
- The second program allows the user to detect the current temperature using the hat and display it on the hat using its led display system. Here the program also displays text on the hat in different colours depending the current temperature, for example if the temperature is 10 degrees celcius or lesser the temperature is displayed in blue color. 
- The third option on the menu allows the user to roll a die which lets the user see what number they have rolled on the die.
- The fourth option allows the user can also play a game of dice against another player by shaking the Pi to acheieve a score which is displayed on screen, the player to achieve the highest score wins. There is also a program which generates different emojis and displays on pressing the joystick

#### Instructions to download and run

#### 1. Download the source code onto the Raspberry Pi
```
sudo git clone https://github.com/adiraj297/Iot-Sensehat-programming.git
```

#### 2. Move into the downloaded folder
```
cd iot-assignment1
```

#### 3. Run the code
```
sudo python3 main.py
```
