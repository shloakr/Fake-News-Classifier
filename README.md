# Fake-News-Classifier

### Description 
This model uses a Passive Aggressive Classifier with the parameters of ```max_iter=50, C=0.5```. The dataset has 20,800 different articles with 10413 “Fake” and 10387 “Real”. The test size was 25% and the accuracy was 96.43%. Additionally, the K fold accuracy was 96.28% when ```cv=5```. To test the model further, testing was done with a different dataset. Using this dataset, the accuracy was 76.43%. Limitations: The datasets used were from 2016-2018 based on US politics hence the model works best with US political articles. This website was made using Flask as a backend and HTML, CSS and Java Script for frontend and validation.

### Video Example
https://drive.google.com/drive/folders/1SI3q2nJddkP1wzYJQVFELfPJC9pHzTe9?usp=sharing

### Landing Page
The **Predict** button redirects the user to the **Result** page.

The article used for this example is from the **New York Times**: https://www.nytimes.com/live/2021/05/18/world/israel-gaza-updates
![127 0 0 1_5000_ (1)](https://user-images.githubusercontent.com/70055735/118726675-471de200-b84f-11eb-846e-5e2a8ff4ceac.png)


### Result Page
Here the classification is outputted.

![127 0 0 1_5000_predict](https://user-images.githubusercontent.com/70055735/118726696-4edd8680-b84f-11eb-8231-03dd92379a95.png)

## To run this on your local host
**Mac or Linux**
Install VirtualEnv.<br/>
```python3 -m venv env```<br/>
```source env/bin/activate```<br/>
At this point make sure to have your virtual environment activated. You should get ```(env)``` in you terminal.<br/>
```pip install -r requirements.txt```<br/>
At this point make sure to be in your folder that holds the ```app.py``` file.<br/>
```python app.py```<br/>
Then copy paste the local host with the port in any web browser. It will most likely start with '127.0'.

## Issues
Hosting this projects takes 4GB ram on a VPS hence making it difficult to host.

## Cite
If you find the code in the repository useful, please cite it using:
```
@miscsShlaokr2021Fake-News-Classifier,
  author = {Shloak Rathod},
  title = {An Open Source Implementation of Fake News classification},
  year = {2021},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {Available at \url{https://github.com/shloakr/Fake-News-Classifier/}}
}
```
