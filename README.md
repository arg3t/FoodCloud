# FoodCloud
<div style="text-align:center"><img src="/logo.png" style="width:500px;height:500px;">/></div>

Foodcloud is a project that aims to ensure food safety and transparency between producers and consumer by continuosly tracking the ingredients used in a product from the farm to the supermarket. This is ensured and supported using several technological hardware & software that we have developed including a mobile app, an api and a robot that reorganizes the products in the shelf according to their best before date , therefore significantly decreasing food waste and ensuring 100% consumer safety.

## How does it work?
We start tracking each raw ingredient in the farm and log every process that is applied on it and whether they were applied safely. I won't be getting into the logistics of how we are achieving this, however you can find a detialed report on it at the end of this README. After logging each process made on the ingredients, we stick a qr code that contains unique integer on the product which is associated with that product's details in our database. This QR code comes into play in two parts: firstly, it enables the user to access its every single detail by scanning th qr code using our mobile app(which also warns the user in case they have any allergies associated with their profile) and also in our robot BarcoShelf which scans the QR codes and uses them to figure out their Best Before Dates.

## How does the robot work?
Even though the robot has a very simple function, there were lots of engineering issues that we had to overcome. Firstly, because we had to use at least one Ev3 according to the guidelines of the competition that we were participating in, we used an Ev3 which controls the motors according to the commands from our main controller Raspberry Pi. At first I planned to interface these two interface using the i2c protocol, however neither of those cards could act as a slave. So because of this, I had to add an Arduino Nano in between which connects to the Ev3 with i2c and RpI with Serial. It simply acts as a bridge and nothing else. After solving this problem, we encountered an even bigger software problem. The robot could only have space for one product which meant that we could not move two products at the same time. This was an especially hard problem for me since it was my first year in programming. However, I came up with a fairly elgeant solution which I will be explaining in the next chapters. 
### How does the sorting work?



