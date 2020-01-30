# CityBuzz
__An Urban Ecosystem Project at Digital Society School__   
  
  
Designers: Yiting Tang, Asli Erdem, Vivika Ekman, Mudita Singh  
Supervisor: Ilaria Zonda  
Collaborator: Qizhang(Kevin) Sun    
Programmer: Yiting Tang  
    
Last Update: 30/01/2020  
  
_A clickable prototype can be found [here](https://xd.adobe.com/view/9a9f1437-ca4f-45b2-433b-6e0755dfe5ea-ecae/?fullscreen&hints=off)._
_If you have any questions, please do not hesitate to contact us via [email](mailto:urbanecosystems.dss@gmail.com)._

## About the Project
CityBuzz is an urban design project. This project aims at encouraging people to grow more flowers so that human-being can be an active part of making the city green and helping the city pollinator (e.g., bees) thrives. The product of this project is a digit-reality game that uses data from a physical installation in the city to play in a browser-based mobile interface.  
  
## Manual of the CityBuzz Game
This manual gives you instructions about:  
* [Basic game rules](#rules)
 * [The Gardeners](#gardener)
 * [Pollinators](#pollinator)
* [Artificial follower (physical installation)](#installation)
* [Web server setup and web-based mobile interface access](#interface)
 * [Webserver setup](#server)    
 * [Web-based mobile](#acceess)   
 * [Program notes](#note)  
  
## Basic Game rules <a name="rules"></a>  
  
This game involves two characters, _the gardener_ and _the pollinator_.  
  
### The Gardeners<a name="gardener"></a>

You select _the gardener_ character if you have an open space to build your garden. The goal of _the gardener_ is to achieve a higher rank by gaining points. _The gardener points_ can be gained in three ways.  
* __Attract _pollinator_ by growing more flowers.__   
Although growing more flowers does not directly give gardener more points, but it invites more bees. When bees visit the garden, _the gardener_ receives a message in the game. The logo in the artificial flower map in the interface is lighted up at the same time, which attracts _the pollinator_ to visit and collect _pollinator points_. Meanwhile, the visits of _the pollinator_ directly convert to _gardener points_.  
* __Grow more kinds of bee-friendly flowers listed in the game.__   
The game encourages gardeners to increase the diversity of the flowers and the flowers that benefits to the pollinators. Gardeners upload a picture of the grown flowers in their garden to the interface. Each kind of planted bee-friendly flower listed in the game can light up the related flower logo in the interface, which accelerates the points gaining.   
  
__Gardeners setup__  
  
1. Register an account in the interface; and  
2. "Plant" artificial flower in the middle of the garden and connect it to the game (see [Artificial follower (physical installation) setup](#installation) for more details).  
  
__Now, _the gardeners_ are good to go! Start to grow the garden and wait for your bees and _the pollinators'_ visits!__


### The Pollinators<a name="pollinator"></a>  
  
You select _the pollinator_ if you do not have an open space to build your garden or you simply want to travel and pollinate in the game. The goal of _the pollinator_ is to achieve a higher rank by gaining points while keeping the _digital bee(s)_ in the interface alive. Besides, _the pollinator_ has two sets of achievements, which are flower fragments collection and digital bee collection.   
  
__The _pollinator_ can gain _pollinator points_ in three ways.__  
  
* __Visit gardens__<a name="visitgarden"></a>  
When bees visit the garden of _the gardener_, the logo of the visited garden in the artificial flower map in the interface is lightened up. _The pollinator_ can collect the _pollinator points_ by physically visit the location when the logo is lightened up.    
* __Daily challenges__<a name="challenge"></a>    
_The pollinator_ can complete the _daily challenge_ (e.g., take the bee quizzes) to gain _pollinator points_. The _daily challenges_ appear in the artificial flower map randomly. _The pollinator_ can simply click on the question mark icon in the artificial flower map to complete the _daily challenge_.   
  
__The digital bee(s)__<a name="digitalbee"></a>  

You can choose one _digital bee_ at the beginning of the game. The health of _digital bees_ drops along with the time. To feed the _digital bee_, _the pollinator_ can [visit gardens](#visitgarden). _The pollinator_ can complete the digital bee collection by having all _digital bees_ on the list provided by the game. To have more _digital bees_, _the pollinator_ has to gain more points to get an upgrade. Please also note that when _the pollinator_ has more _digital bees_, more foods are required to keep them alive.  
  
__The flower fragments__  

To complete the flower fragments collection. You can:  
* [Visit gardens](#visitgarden); or  
* [Complete daily challenge(s)](#challenge)  
_The pollinator_ can only collect flower fragments when _the gardener_ grows the same kind of flowers. For example, when _the gardener_ grows sunflowers and roses, _the pollinator_ can only select a flower fragment between sunflower and rose.
 
__Pollinator setup__  
  
1. Register an account in the interface; and  
2. Choose a _[digital bee](#digitalbee)_ from the bee species list of the Netherlands provided by the game.  
  
__Now, _the pollinators_ are good to go! Start to visit the gardens! _The pollinator_ can also help bee researchers to find new bee species in Amsterdam. Simply take a photo and upload it to the interface to share the findings with the community. Of course, points are rewarded.__

## Artificial follower (physical installation)<a name="installation"></a>  
  
  The _Artificial Flower_ is a physical installation with Raspberry Pi that are used to collect real-world data, including:  
* recognize bees  
* count number of bees passing-by  
* send data back to the server for further process  
  
Here we use the model of a teachable machine to recognize bees. Click [here](https://teachablemachine.withgoogle.com/) to find out more about the teachable machine. To customize the bee monitor, modify the JavaScript file at `/static/js/bee.js` to change the model of the teachable machine.   
      
Followed by installing the artificial follower (for more information about artificial follower installation, see the Artificial Flower Instruction Guide), _the gardener_ needs to set up the Raspberry Pi by:  
1. To install Raspbian on your SD card  
2. Connect the raspberry pi with a monitor and keyboard  
3. Connect the power to the raspberry pi and turn it on  
4. Enable the pi camera  
  4.1. Select Interfacing Options.  
  4.2. Navigate to and select the camera.  
  4.3. Choose Yes.  
  4.4. Select OK.  
5. Enable Wi-Fi  
    
## Web server setup and web-based mobile interface access<a name="interface"></a>  

### Webserver setup<a name="server"></a>
  
  The demo only takes one _gardener_. In this case, the Raspberry Pi also takes responsibility as a server for the web-based interface. To set up the server:
  
1. Download the CityBuzz testing demo files from Github to the Raspberry Pi; and  
2. Navigate to the root folder of CityBuzz files; and  
3. Initialize the database by running `python initialDB.py` on the Raspberry Pi terminal; and  
4. Start the local server by running `python app.py` on the Raspberry Pi terminal; and  
5. Broadcast the local server using _ngrok_. To use _ngrok_, install [ngrok](http://www.ngrok.com) by following the instruction on the official website. Then, open another terminal and run ngrok by entering `./ngrok http 5000` in the terminal.   
  
__Now, the server is ready. Other players can access the website by the link provided by ngrok.__  

To test the setup, _the gardener_ can open the browser and access the link: [http://127.0.0.1:5000/raspberrypi/](http://127.0.0.1:5000/raspberrypi/). _The gardener_ should see the camera video and bees count.   
       
### Web-based mobile interface access<a name="access"></a>  
  
  After broadcasting the local server, _ngrok_ provides a URL to access the website. To visit the home page, access the URL + `/citybuzz/` in a mobile device.  
    
### Program notes<a name="note"></a> 

This is a website running under the Python web application framework <a href="https://palletsprojects.com/p/flask/" target="_blank">"Flask"</a>. For required software installation and environment setup, please refers to the <a href="https://flask.palletsprojects.com/en/1.1.x/" target="_blank">documentation</a>. Data is stored as a DB file in the "data" folder.

__A summary of folders and files__  
  
+ data: Data storage folder.
+ static: Static elements, including code for stylesheets, Javascripts and images.
+ templates: HTML pages
+ app.py: Main back-end python file, including website flows and so on.
+ config.py: Configuration of the website, including security key, database path, and switch for debugging.
+ initialDB.py: Database initialization python file.
+ models.py: Defining tables in the database  
  
    
__&#169; All rights about the design reserved by Yiting Tang, Asli Erdem, Vivika Ekman and Mudita Singh.__  
__&#169; All rights about the interface program reserved by Yiting Tang and Qizhang (Kevin) Sun.__  
__&#169; All rights about the artificial flower design reserved by Asli Erdem, Vivika Ekman and Mudita Singh.__  