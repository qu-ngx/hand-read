# Hand-Gesture-Reader

**What does this code do?** 
+ Reading simple idle hand gestures in Sign Language such as alphabetical symbols using a pre-trained model.
<br>(I trained almost all gestures except for Z and J since they require motions)</br>



![IMG_2648](https://github.com/qu-ngx/Hand-Gesture-Reader/assets/91497379/22970993-f1b1-42c8-b769-eea5715e09f7)

**How does it work?**
+ Well fairly easy since I have processed all input datas on my computer
+ You just have to put your hand in your camera. (Remember one hand only)




# Manual guide how to run the codes:

**Installing libraries and dependencies:** 
```
pip3 install open-cv tensorflow mediapipe numpy
```

+ Since I have trained model and converted images into readable form in model.p. (You do not have to train it manually)

**Head toward zsh, cmd, or cmd and run the code:**

```
python3 inference.py
```

<br>It should pop up a window like below and here comes the demonstration:</br>
**Note:** The model still sometimes have low inaccuracy and some input overload so try again if it exits unfortunately (And it will do)

<img src="https://github.com/qu-ngx/Hand-Gesture-Reader/assets/91497379/627dd714-4fc1-4d38-85ba-df9e963a7ae3" width="9000" height="700"/>
