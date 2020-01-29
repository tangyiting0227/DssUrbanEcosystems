# CityBuzz
__An Urban Ecosystem Project at Digital Society School__   
  
  
Designers: Yiting Tang, Asli Erdem, Vivika Ekman, Mudita Singh  
Supervisor: Ilaria Zonda  
  
  
Programmer: Yiting Tang  
Technical Support: Qizhang(Kevin) Sun  
  
    
Last Update: 29/01/2020  
  
_A clickable prototype can be found [here](https://xd.adobe.com/view/9a9f1437-ca4f-45b2-433b-6e0755dfe5ea-ecae/?fullscreen&hints=off)._

## About the Project
CityBuzz is an urban design project. This project aims at encouraging people to grow more flowers so that human-being can be an active part of making the city green and helping the city pollinator (e.g., bees) thrives. The product of this project is a digit-reality game that uses data from an physical installation in the city to play in a browser-based mobile interface.  
  
This game involves two charaterrs, the _citizen_ and the _gardener_. The _gardener_ gains points and achievements by growing flowers in real life to attract the _citizen_. The _citizen_ keeps their bees alive and gains a higher rank in the game by collecting the pollen produced by the _gardener_. Artificial flowers, the physical installations, placing in the gardens collect data from real world, such as number of bees passing-by and number of flowers being grown, and transfer to the digital game interface.
 
 
## Manual of the CityBuzz Game
This manual gives you instructions about how the CityBuzz game works. The technical details guides you to build your own _Artificial Flower_ and setup the _digital interface_. The _Artificial Flower_ is a physical installation that are used to collect real world data, including:
* recognize bees
* count number of bees passing-by
* send data back to server for further process

### Two characters
* __The Gardeners__

    You select _the gardener_ character if you have an open space to build your garden.  
    
  
* __The Pollinators__

    You select the _the pollinator_ if you do not have an open space to build your garden or you simply want to travel and pollinate in the game.

### Basic Game rules
As a gardener, you need to plant flowers to complete the bee-friendly flower list provided by the game. As a pollinator, you need to visit the garden in the game to get bee-friendly flower fragments as much as possible.

* __The Gardeners__

    1. Open the game on your phone and get an artificial flower, then you need to create an account as a gardener. 
    
    2. You need to take the artificial flower to your rooftop garden and insert it in the soil among other flowers, install it and connect it with the game. 
    
    3. As a part of your game, you need to plant the flowers of the bee-friendly flower list in the game. After you plant the flowers, take a photo and upload it to the app. You will unlock this flower on the list and get points.
    
    4. Waiting the bees visit your garden, if the bees are visiting your garden, you will see the message in the game, and your artificial flower will light up in the artificial flower map.
    
    5. Waiting for other citizens (the pollinators in the game) to visit your garden after your artificial flower will light up in the artificial flower map. If other citizens check-in your garden, you can get points.

* __The Pollinators__

    1. Open the game on your phone and create an account as a pollinator. 
    
    2. Choose your bee character from the bee species list of the Netherlands.
    
    3. Make sure your bee is not died by getting nectar from the gardens in the game.
    
    4. Check the artificial flower map and see the artificial flowers lightened up in specific locations. 
    
    5. Visit the location lightened up on the map and collect nectar and flower fragments from that garden. 
     
    6. To collect more points, you can play daily challenges (e.g., take the bee quizzes.)
    
    7. Help bee researchers find bees in Amsterdam. If you find a bee, take a photo and upload it to the app. You can share your findings with the community and get points.
    
### How to set up the testing demo  

1. Assemble the Artificial Flower components  
  
  (see the Artificial Flower Instruction Guide)  
  

2. Setup the Raspberry Pi  
  2.1. To install Raspbian on your SD card  
  2.2. Connect the raspberry pi with a monitor and keyboard  
  2.3 Connect the power to the raspberry pi and turn it on  
  2.4 Enable the pi camera  
  &nbsp;&nbsp;&nbsp;&nbsp;2.4.1 Select Interfacing Options.  
  &nbsp;&nbsp;&nbsp;&nbsp;2.4.2 Navigate to and select Camera.  
  &nbsp;&nbsp;&nbsp;&nbsp;2.4.3 Choose Yes.  
  &nbsp;&nbsp;&nbsp;&nbsp;2.4.4 Select OK.  
  2.5 Enable Wi-Fi

3. Download the CityBuzz testing demo files from Github to the local

4. Run the local server

  Enter the root folder of the codes and run `python app.py` on the Raspberry Pi terminal.  
  

5. Run the camera monitor page  

  Open the browser and access the link: [http://127.0.0.1:5000/raspberrypi/](http://127.0.0.1:5000/raspberrypi/)  
  Here we use the model of teachable machine to recognize bees. Click [here](https://teachablemachine.withgoogle.com/) to find out more about teachable machine.  
  If you want to customize your bee monitor, you can go to `/static/js/bee.js` to change the model of teachable machine. 

6. Provide a web server to other users  

    6.1. Install [ngrok](ngrok.com)  
    6.2. Open another terminal and run ngrok by enter `./ngrok http 5000` in the terminal. Other players can access the website by the link provided by ngrok.  
       
7. Experience the interface with your mobile device

    Enter provided URL + `/citybuzz/` in mobile device  


### The workflow of the testing demo
1. Welcome page locates at `/templates/citybuzz.html`  
  
2. Charater choice page at `/templates/rolechoose.html`  
  
3. Gardener account creating page at `/templates/gardenerlogin.html`  
  
  3.1 Bee monitoring page at `/templates/ArtificialFlowerDoc.html`  
    If the bee is not detected by the camera, the screen will show the artificial flower icon. If the bee is detected by the camera, the screen will show the bee icon.  
      
4. Pollinator account creating page at `/templates/citizenrlogin.html`  
  
    4.1 Bee character choice page at `/templates/choosebee.html`  
      
    4.2 Bee health status page at `/templates/beestatus.html`  
  &nbsp;&nbsp;&nbsp;&nbsp;Your bee will lose the health points if your don't get nectar from the game. By clicking the icon of 'Get nectar', you can go to Artificial flower map to recharge health points.  
    
    4.3 Get nectar and flower fragments from artificial flower at `/templates/artificialflowermap.html`   
  &nbsp;&nbsp;&nbsp;&nbsp;You can click the icon of bees in the map, the icon presents the artificial flower. After click the icon, you can choose one of the flowers which are planted in this rooftop garden. Then, you can get nectar and one flower fragment.  
    
    4.4 Take bee quiz at `/templates/artificialflowermap.html`  
  &nbsp;&nbsp;&nbsp;&nbsp;You can take bee quiz by cliking quizmark icon. If your answer is right, you can get one flower fragment.  
    
    4.5 Check the flowers collection  at `/templates/artificialflowermap.html`  
  &nbsp;&nbsp;&nbsp;&nbsp;After you get flower fragment, you can go back beestatus page, check your flowers collection and the health points of your bee.