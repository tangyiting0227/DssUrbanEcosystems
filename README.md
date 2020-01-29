# CityBuzz
Urban Ecosystem Project at Digital Society School 

## About the Project
 The Urban Ecosystems Project focuses on the possibilities for the citizens to be an active part of making the cities green and help bees and other pollinators thrive in the city. Our team worked to create a digit-reality mobile game named CityBuzz, which involves the browser-based mobile game connected to the physical artificial flower. Through this game, the gardener and other citizens can be connected, and create a bee-friendly online community together.
 
 
## CityBuzz Manual
This manual will give you instructions about how the CityBuzz game (testing demo) works. With the technical details, it will guide you on how to build your Artificial Flower that can recognize Bees, and connect to the CityBuzz Web that can monitor bees visiting your garden.
If you want to check the clickable prototype, click [here](https://xd.adobe.com/view/9a9f1437-ca4f-45b2-433b-6e0755dfe5ea-ecae/?fullscreen&hints=off).

### Two Personas
* __The Gardeners__

if you have an open space where you have your garden.

* __The Pollinators__

if you don’t have an outdoor space or you want to travel and pollinate in the game.

### Basic Game rules
As a gardener, you need to plant flowers to complete the bee-friendly flower list provided by the game. As a pollinator, you need to visit the garden in the game to get bee-friendly flower fragments as much as possible.

* __The Gardeners__

    1. Download the game on your phone and get an artificial flower, then you need to create an account as a gardener. 
    
    2. You need to take the artificial flower to your rooftop garden and insert it in the soil among other flowers, install it and connect it with the game. 
    
    3. As a part of your game, you need to plant the flowers of the bee-friendly flower list in the game. After you plant the flowers, take a photo and upload it to the app. You will unlock this flower on the list and get points.
    
    4. Waiting the bees visit your garden, if the bees are visiting your garden, you will see the message in the game, and your artificial flower will light up in the artificial flower map.
    
    5. Waiting for other citizens (the pollinators in the game) to visit your garden after your artificial flower will light up in the artificial flower map. If other citizens check-in your garden, you can get points.

* __The Pollinators__

    1. Download the game on your phone and create an account as a pollinator. 
    
    2. Choose your bee character from the bee species list of the Netherlands.
    
    3. Make sure your bee is not died by getting nectar from the gardens in the game.
    
    4. Check the artificial flower map and see the artificial flowers lightened up in specific locations. 
    
    5. Visit the location lightened up on the map and collect nectar and flower fragments from that garden. 
     
    6. To collect more points, you can play daily challenges (e.g., take the bee quizzes.)
    
    7. Help bee researchers find bees in Amsterdam. If you find a bee, take a photo and upload it to the app. You can share your findings with the community and get points.
    
### How to set up the testing demo
__Step 1: Assemble the Artificial Flower components__

    (see the Artificial Flower Instruction Guide)

__Step 2: Setup the Raspberry Pi__

    2.1 To install Raspbian on your SD card
    
    2.2 Connect the raspberry pi with a monitor and keyboard
    
    2.3 Connect the power to the raspberry pi and turn it on
    
    2.4 Enable the pi camera
        1. Select Interfacing Options.
        2. Navigate to and select Camera.
        3. Choose Yes.
        4. Select OK.
        
    2.5 Enable Wi-Fi

__Step 3: Download the CityBuzz testing demo files from Github to the local__

__Step 4: Run the local server__

     Enter the following commands on the Raspberry Pi terminal: 
     
     cd Documents/CityBuzz/python app.py

__Step 5: Run the camera monitor page__

    Open the browser and tap your local server address and add ‘/raspberrypi/’
    
    e.g., http://127.0.0.1:5000/raspberrypi/
    
    Here we use the model of teachable machine to recognize bees. 
    
    Click [here](https://teachablemachine.withgoogle.com/) for more information about teachable machine.
    
    If you want to customize your bee monitor, you can go to /static/js/bee.js to change the model of teachable machine. 

__Step 6: Provide a web server to other users__

    Open another terminal and enter the following commands: 
    
    cd ./ngrok http 5000
    
    You will get a random URL.
       
__Step 7: Experience the interface with your mobile device__

    Enter random URLs/ports provided by the local server the browser in mobile device and add ‘/citybuzz/’


### The workflow of the testing demo
__1. Welcome page__

    /templates/citybuzz.html

__2. Choose your persona__

    /templates/rolechoose.html

__3. If you choose gardener, create a gardener account__

    /templates/gardenerlogin.html

__3.1 You will see the bee monitoring page__

    /templates/ArtificialFlowerDoc.html
    
    If the bee is not detected by the camera, the screen will show the artificial flower icon. 
    
    If the bee is detected by the camera, the screen will show the bee icon.

__4. If you choose pollinator, create a pollinator account__

    /templates/citizenrlogin.html

__4.1 choose Your bee character__

    /templates/choosebee.html

__4.2 Check the health status of your bee__

    /templates/beestatus.html
    
    Your bee will lose the health points if your don't get nectar from the game. 
    
    Click the icon of 'Get nectar', and you can go to Artificial flower map.

__4.3 Get nectar and flower fragments from artificial flower__

    /templates/artificialflowermap.html
    
    You can click the icon of bees in the map, the icon presents the artificial flower. 
    
    After click the icon, you can choose one of the flowers which are planted in this rooftop garden. 
    
    Then, you can get nectar and one flower fragment.

__4.4 Take bee quiz__

    /templates/artificialflowermap.html
    
    You can take bee quiz by cliking quizmark icon. 
    
    If your answer is right, you can get one flower fragment.

__4.5 Check the flowers collection__

    /templates/artificialflowermap.html
    
    After you get flower fragment, you can go back beestatus page, check your flowers collection and the health points of your bee.