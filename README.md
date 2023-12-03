# Hack10-TheNextHokage

This repository is written for the Hack@10 hackathon by **TheNextHokage**. This is a AI game developed for entertainment while training players on Jutsu techniques.

## Download the Repo

- Install git
```
sudo apt install git
```

- Clone the repository
```
git clone https://github.com/yinloonkhor/Hack10-TheNextHokage.git
```

- Go to the cloned folder
```
cd Hack10-TheNextHokage
```

## Hand Sign
![image](https://github.com/yinloonkhor/Hack10-TheNextHokage/assets/152722201/2f481b3a-9abc-4838-b57f-ab652cba79f2)

## Demo
![ezgif com-video-to-gif](https://github.com/yinloonkhor/Hack10-TheNextHokage/assets/152722201/bd8de2c6-c677-4b48-baf9-a58baa65bdf0)


https://github.com/yinloonkhor/Hack10-TheNextHokage/assets/152722201/0ed346a1-cb29-465c-8c79-bb222e344662




## Training
The dataset is forked from a Roboflow project and preprocessed [here](https://app.roboflow.com/eddy-miner-mwie9/naruto-t7o4a/2). Training is done using YOLOv8n with batch size of 12, image size of 640 and 80 epochs by running train.py after downloading the dataset.

Various training variants can be located at runs/detect, however the best pt file is found to be Yolov8n variant with 80 epochs (the one at the main directory as well). User can run TheNextHokage.ipynb to start the game. Enjoy!


## Credit to
Naruto Hand Signs Dataset

https://universe.roboflow.com/vgu-aeaes/naruto-hand-sign/browse?queryText=&pageSize=50&startingIndex=0&browseQuery=true
