## IoT Devices Classification Web App [Python-ML Project For Beginners]

The Script is written in `python` and for UI interface `flask` is used.

<a href="https://flask.palletsprojects.com/en/1.1.x/"><img src="https://miro.medium.com/max/438/1*0G5zu7CnXdMT9pGbYUTQLQ.png" width="150" height="100"/></a>
## Screenshot

![](https://github.com/Lovepreet-Singh-LPSK/IoT-Devices-Classification/blob/master/pic/1.png)

## How To Run Program

**NOTE** : After cloning, Download <a href="https://drive.google.com/file/d/1B8HAYDa-Fcbtcb3YYTY680KHa5EyloN-/view?usp=sharing">Network Classification Dataset</a> and place csv file to cloned directory (IoT-Devices-Classification).

```bash
$ git clone https://github.com/Lovepreet-Singh-LPSK/IoT-Devices-Classification.git
$ cd IoT-Devices-Classification
$ python app.py
-- Now run address http://127.0.0.1:5000/ in your browser.
```

**NOTE** : This Code contains pretrained model which we trained. You can use that or can follow easy steps to train the model.  
## IoT Devices Classification by Analyzing Network Traffic Characteristics (Steps)→
Steps to Follow:
![](https://github.com/Lovepreet-Singh-LPSK/IoT-Devices-Classification/blob/master/pic/2.png)
- 1.) Parsing → Use Wireshark Tool to convert the Pcap file to CSV because we will use CSV file as a dataset for ML classification. Add Features by using column addition option from the Wireshark tool.
##### For adding a column in Wireshark so that this column can be the feature in our CSV file, Follow these steps →
``Go to Edit→ Preferences→ Columns and click on add button.``
![](https://github.com/Lovepreet-Singh-LPSK/IoT-Devices-Classification/blob/master/pic/3.png)
![](https://github.com/Lovepreet-Singh-LPSK/IoT-Devices-Classification/blob/master/pic/4.png)
``We have added new columns of Ports, Mac Address (For separating IoTs).``
- 2.) Use Mac address CSV for separating the features of individual IoT devices and label them.
**NOTE** : ​ You do not need to perform preprocessing because This code has all CSV already (Extracted from Wireshark Tool).  
- 3.) After Labelling the dataset, Remove Protocols like ARP and ICMPv6.
- 4.) Now, We have extracted the ports, Dns and Average packet size which is total data sent and received divided by number of packets.
- 5.) And After labeling the dataset, we have analyzed feature importance using data polation and we found that DNS, Average Packet Size and Ports, these three features are enough for classification.
- 6.) We found that these three features are forming dense clusters and thus KNN worked well because it works on the principle of Euclidean Distance.
## Contributing

##### Feel Free to build more robust trained model. Because it is a very Basic one. 