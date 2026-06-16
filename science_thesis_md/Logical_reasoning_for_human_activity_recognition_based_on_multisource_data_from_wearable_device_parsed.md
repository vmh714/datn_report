### Tóm tắt:
Bài báo đề xuất một công nghệ nhận diện hành vi con người (HAR) dung lượng nhẹ dựa trên cảm biến đa nguồn từ các thiết bị đeo thông minh và suy luận logic. Khác với các phương pháp học máy truyền thống đòi hỏi nhiều tài nguyên tính toán, giải pháp này kết hợp lý thuyết suy luận bản thể luận với kỹ thuật xử lý tín hiệu. Hệ thống sử dụng dữ liệu từ bốn thiết bị thương mại phổ biến gồm kính, đồng hồ, điện thoại và giày chạy để phân tích mối quan hệ logic chuyển động giữa các chi. Kết quả thực nghiệm cho thấy phương pháp đạt độ chính xác trên 90% đối với 11 hoạt động hàng ngày và giảm đáng kể lượng dữ liệu huấn luyện cần thiết.

### BibTeX:
```bibtex
@article{Alsaadi2025,
  author = {Alsaadi, Mahmood and Keshta, Ismail and Ramesh, Janjhyam Venkata Naga and Nimma, Divya and Shabaz, Mohammad and pathak, Nirupma and Singh, Pavitar Parkash and Kiyosov, Sherzod and Soni, Mukesh},
  title = {Logical reasoning for human activity recognition based on multisource data from wearable device},
  journal = {Scientific Reports},
  year = {2025},
  volume = {15},
  pages = {380},
  doi = {10.1038/s41598-024-84532-8}
}
```

---

## NỘI DUNG BÀI BÁO CHI TIẾT

www.nature.com/scientificreports 

**==> picture [72 x 14] intentionally omitted <==**

## **OPEN Logical reasoning for human activity recognition based on multisource data from wearable device** 

**Mahmood Alsaadi[1] , Ismail Keshta[2] , Janjhyam Venkata Naga Ramesh[3,4] , Divya Nimma[5] , Mohammad Shabaz[6]**[] **, Nirupma pathak[7] , Pavitar Parkash Singh[8] , Sherzod Kiyosov[9] & Mukesh Soni[10,11]** 

**Smart wearable devices detection and recording of people’s everyday activities is critical for health monitoring, helping persons with disabilities, and providing care for the elderly. Most of the research that is being conducted uses a machine learning-based methodology; however, these approaches frequently have issues with high computing resource consumption, burdensome training data gathering, and restricted scalability across many contexts. This research suggests a behaviour detection technology based on multi-source sensing and logical reasoning to address these problems. In order to realize the natural fusion of signal processing and logical reasoning in behavior recognition research, this work designs a lightweight behavior recognition solution using the pertinent theories of ontology reasoning in classical artificial intelligence. Machine learning technology is also employed for behavior recognition using the same data set. Once the best model has been chosen, the cross-person recognition results after testing and modification of parameters are 90.8% and 92.1%, respectively. This technology was used to create a behaviour recognition system, and several tests were run to assess how well it worked. The findings demonstrate that the suggested strategy achieves over 90% recognition accuracy for 11 different daily activities, including jogging, walking, and stair climbing. Additionally, the suggested strategy dramatically minimises the quantity of user-provided training data needed in comparison to machine learning-based behaviour identification techniques.** 

**Keywords** Wearable devices, Logical reasoning, Human activity recognition, Multisource data, IMU, Data signal 

As a key technology for IoT applications, human activity recognition (HAR) has attracted great attention and attention from the domestic and foreign industrial and academic circles due to its multifaceted applications and academic value. With the gradual popularization of a variety of smart terminals in people’s daily lives, many technology companies and related scholars have invested in the research of behaviour recognition based on smart devices and have made a series of progress. However, various studies have obvious defects and deficiencies, and are increasingly unable to meet current needs. In terms of perception, existing work can be mainly divided into behaviour recognition based on signals such as radio frequency signals[1] , sound waves[2] , images[3] , and wearable devices sensor signals[4] . According to the recognition method, existing research work can be mainly divided into three categories: machine learning[5] , deep learning[6] , and physical modelling[7] . The general process of behaviour recognition technology using machine learning methods is to collect a suitable 

1Department of Computer Sciences, College of Sciences, University of Al Maarif, Al Anbar 31001, Iraq. 2Computer Science and Information Systems Department, College of Applied Sciences, AlMaarefa University, Riyadh, Saudi Arabia.[3] Department of CSE, Graphic Era Hill University, Dehradun 248002, India.[4] Department of CSE, Graphic Era Deemed to be University, Dehradun, Uttarakhand 248002, India.[5] Data Analyst in UMMC, University of Southern Mississippi, Hattiesburg, USA.[6] Present address: Model Institute of Engineering and Technology, Jammu, J&K, India.[7] CSE-R Department, KL University Andhra Pradesh, Vijayawada, India.[8] Department of Management, Lovely Professional University, Phagwara, India.[9] The Department of Tax and Taxation, Tashkent State University of Economics, Tashkent, Uzbekistan.[10] Dr. D. Y. Patil Vidyapeeth, Pune, Dr. D. Y. Patil School of Science & Technology, Tathawade, Pune, India.[11] Division of Research and Development, Lovely Professional University, Phagwara, India.  email: bhatsab4@gmail.com 

**Scientific Reports** |          (2025) 15:380 

1 

| https://doi.org/10.1038/s41598-024-84532-8 

www.nature.com/scientificreports/ 

number of training data sets, manually extract and select features, and then perform a series of modelling and classification. Training a suitable recognition model is a common method in early behaviour recognition research. Its advantages are that it requires less training multisource data and simpler model training, but it also has defects such as the need for manual feature selection and feature extraction and poor generalization ability. The idea of behaviour recognition technology based on deep learning is like that based on machine learning. The difference is that the latter can obtain the highest accuracy and does not require manual feature extraction, but it is more dependent on the size of the training multisource data set and the computing resources of the equipment. The behaviour recognition technology based on physical modelling mainly establishes a one-to-one mapping relationship between signal parameters such as amplitude and phase and user behaviour activities, to realize the recognition of different categories of activities through changes in signal parameters. This method has the advantages of no need for training, small amount of calculation, and high accuracy, but it can only be applied to a few regular activities, such as fitness exercises and arm swings. 

Based on the above research and analysis, this paper is committed to designing a lightweight multi-source perception behaviour recognition technology. Many technology businesses and related scholars have invested in the study of behaviour detection based on smart devices and have made a number of advancements since the progressive popularization of various smart terminals in people’s daily lives. Nevertheless, there are a number of studies that are clearly flawed and falling short of the demands of the present. Regarding perception, current research can be broadly categorized as behaviour recognition using signals like imaging, sound waves, radio frequency signals, and wearable device sensor signals. This paper uses four common commercial mobile smart terminals (smart glasses, watches, mobile phones, running shoes) for networking, calls the inertial measurement unit sensors of each device, collects motion data from the user’s head, wrist, waist and feet, and processes and analyzes them to identify user behaviour. Lightweight is reflected in the abandonment of the model training process required by the bulky machine learning technology, and uses logical reasoning combined with signal processing related technologies for recognition. Based on the logical relationship between the upper and lower limbs, the multisource data collected by the sensor is analyzed using signal processing technology, reducing the multisource data processing pressure of the entire system, increasing the interpretability and scientific, reducing the overall scale of calculation, reducing the computing overhead of mobile devices, and ensuring real-time and response speed. Multi-dimensional perception is reflected in the fact that when collecting perception data, it is not limited to the sensor data of a single device, but the multisource data collected by multiple wearable devices worn on various parts of the body are unified and combined for analysis. Different from the previous data analysis of only a single device, this makes the description of the action more vivid. On the other hand, this system only uses common commercial mobile intelligent terminal devices in daily life, eliminating the inconvenience and discomfort caused by additional hardware devices to users during use. At the same time, an adaptive algorithm is added to provide matching recognition logic for users with different body characteristics, achieving flexibility in application scenarios and scope of application. The method of identifying and classifying human behaviours using machine learning and sensor data is known as human activity recognition, or HAR. In the fields of ubiquitous computing, human behaviour analysis, and human–computer interaction, human activity recognition is a crucial study topic. To identify simple and complex actions like walking, jogging, cooking, etc., researchers in these fields use a variety of machine learning methods. The process of rigorously using premises and relations between premises to deduce conclusions that are implicit or implied by the premises and relations is known as logical reasoning. This study analyzes the earlier findings after introducing the adaptive algorithm of the logical relationship threshold. The male and female chosen in the earlier article remain the fundamental threshold for testing. The findings demonstrate that the recognition outcomes exhibit varying degrees of growth and improvement, irrespective of whether the male or female is utilized as the fundamental threshold. This new behaviour recognition method has the following three advantages: 

1.  The universality of the device. Although the common commercial intelligent terminal devices in life have different shapes and functions, most of them are equipped with inertial measurement unit sensors. There is no need to carry other additional hardware devices, which reduces the user’s usage cost and burden and lowers the user’s usage threshold. 

2.  The flexibility of application scenarios, the use of signal processing technology and multi-dimensional perception methods can cope with challenges from different usage scenarios. Multisource data acquisition is not limited to a single device, but multiple mobile wearable devices are networked, multisource data is aggregated, and processed uniformly. At the same time, scientific logical reasoning algorithms are used to get rid of redundant data training modes, so that the recognition task can be completed in any scenario. 

3.  The robustness of the system. Based on the recognition method, an adaptive matching algorithm is added. According to the different performance of different users’ behaviour characteristics on the multisource data signal, the recognition conditions are automatically matched for each user to avoid the reduction of recognition accuracy caused by factors such as habits and body shape. 

Section “Related work”, overview of previous research relevant to behaviour recognition, methodologies, and in section “Behavior recognition based on multimodal data and logical reasoning”, integration of multiple data sources for effective behaviour recognition using reasoning. In section “Experimental part”, experimental setup, dataset, evaluation, and analysis to validate proposed recognition method, and in section “Conclusion”, conclude findings, contributions, limitations, and future research suggestions for improvement. 

**Scientific Reports** |          (2025) 15:380 

2 

| https://doi.org/10.1038/s41598-024-84532-8 

www.nature.com/scientificreports/ 

## **Related work** 

According to the different technical means adopted, the related work of behaviour recognition can be mainly divided into machine learning-based technology, deep learning-based technology and physical modelling-based technology. 

Behaviour recognition based on machine learning methods mainly includes the use of supervised learning, semi-supervised learning and unsupervised learning to identify behaviour. Among them, there are many works based on Wi-Fi signals combined with supervised learning for action or behaviour recognition, such as article[8] all use the channel state information (CSI) of Wi-Fi signals to realize action or behaviour recognition in specific scenarios. Among them, the work first used Wi-Fi signals combined with the Fresnel zone theory in physics and then used support vector machine (SVM) to detect human activity recognition; in addition, this paper used the Doppler effect caused by gestures on Wi-Fi to After supervised learning, 9 gestures were successfully recognized; This research[9] proposed a scalable behaviour recognition framework that uses mobile wearable devices[10] to collect sound signals to identify different types of activities; the literature[11] realized the use of cameras and supervised learning for behaviour recognition; The article[12] all deployed a large number of sensors on the human activity recognition, obtained sensor data during movement, and used supervised learning to achieve the purpose of behaviour recognition; these research work[13] both used sensors in smartphones to collect motion data and combined them with machine learning models to conduct related research on behaviour recognition; literatures[14] and[15] both used supervised learning to conduct research on behaviour recognition; this paper[16] Robust behaviour recognition was achieved using semi-supervised learning technology; this article[17] also implemented an action recognition system using unsupervised learning[18] . The advantage of the above work based on machine learning methods is that it does not require too much experimental data to obtain an acceptable accuracy rate[19] , but the disadvantage is that it requires manual feature selection and feature extraction of the multisource data[20] , and when the system encounters a new user, the recognition accuracy will be greatly reduced. In contrast to the data analysis of a single device in the past, this enhances the vividness of the action description. The bother and pain that come with using extra hardware devices is eliminated by this solution, which solely uses standard commercial mobile intelligent terminal devices in everyday life. The addition of an adaptive algorithm allows for flexibility in application scenarios and scope by providing matching recognition logic for users with varying body attributes. Deep learning is a multisource data analysis[21] method based on deep neural networks[22] that has emerged in recent years. Its advantages are mainly reflected in the fact that it does not require manual feature extraction and has a high classification accuracy. The function of facilitating correct diagnosis and processing through more precise grounds for thermal disorders is also anticipated based on the gathered data[23] . Regardless of their proprietary and commercial specifications, SemBox is a potential plug-andplay solution to accomplish semantic interoperability and collaboration amongst diverse health monitoring wearable devices. It can be tailored for applications that provide collaborative monitoring and decision-making across a variety of heterogeneous devices[24] . Our lives now revolve around digital healthcare services. Medical wearables, which streamline and enhance the diagnostic and therapeutic process, are being used by more and more patients and healthcare professionals for diagnosis and treatment[25] . The increase in machine learning (ML) and the popularity of smart wearables like smartwatches have created new avenues for the early diagnosis and treatment of a number of common illnesses, including diabetes, Parkinson’s disease, and cardiovascular disease[26] . Recent advancements in smartphones and wearable technology (WDs) have made it possible to track users’ movements continuously and anywhere. The sensitive and private data related to a user’s health is gathered by WDs and transmitted to the user’s terminal or smart device (SD). The SD enables the user to save the gathered data on the cloud server (CSE) for later distribution to other users, including medical professionals[27] . This proposed work[28] deployed sensors on the human activity recognition to obtain environmental information and used adaptive neural networks to achieve behaviour recognition. These article[29] both used a combination of multiple sensor data in mobile wearable devices to automatically learn the optimal features through deep convolutional neural networks, and completed the recognition of daily behaviours and mid-air gestures respectively; this paper[30] designed a system for action recognition based on multimodal sensor data using a special semi-stacked recurrent convolutional attention model[31] . Article[32] realized specific action or behaviour recognition based on deep convolution and long short-term memory networks; Laput et al. used sound signals and deep learning technology on a laptop to realize a system that can recognize many daily behaviours in life[33] ; this paper used convolutional neural networks to realize behaviour recognition research[34] ; and[35] also realized behaviour recognition using recurrent neural networks. Deep neural networks (DNN) and dynamic graphics models (DGM) are used in behaviour recognition research to identify experimental operation behaviors in biological labs. Both automated the recognition of everyday behaviours and motions in midair by utilizing a combination of various sensor inputs from mobile wearable devices to train deep convolutional neural networks to automatically learn the best attributes. Although compared with other existing methods, deep learning can achieve the highest accuracy and does not require manual feature extraction, its disadvantage is that it uses the most computing resources among all methods, the model training time is also the longest among all methods, and the amount of training data required is also the largest. 

## **Behavior recognition based on multimodal data and logical reasoning Overall system design** 

This project designed and implemented a behaviour recognition system based on universal heterogeneous wearable devices, BehaviourLog. The basic idea of the system is to integrate the motion data of multiple wearable devices to judge 12 behaviours of upper and lower limbs, display and record the recognition results in real time, and form a user BehaviourLog. Figure 1 is the overall flow chart of BehaviourLog. The system recognizes 12 upper and lower limb behaviour activities including brushing teeth, swinging arms, writing, typing, walking, 

**Scientific Reports** |          (2025) 15:380 

3 

| https://doi.org/10.1038/s41598-024-84532-8 

www.nature.com/scientificreports/ 

**==> picture [249 x 258] intentionally omitted <==**

**Fig. 1** . Flow chart of overall system. 

running, climbing stairs, descending stairs, riding a bicycle, taking an escalator up, taking an escalator down, and standing still. To identify the behaviors of experimental operations in biological labs. This proposed approach employed adaptive neural networks to recognize behavior and placed sensors on human activity to gather environmental data. Both finished recognizing everyday behaviors and mid-air motions, respectively, by combining various sensor data from mobile wearable devices to automatically learn the best characteristics using deep convolutional neural networks. Through data collection, preprocessing, logical judgment and behaviour recognition, lightweight and robust user daily behaviour recognition is achieved. BehaviourLog uses four mainstreams wearable devices including smart glasses, smart watches, smart phones and smart running shoes as perception units. The smart running shoes here are realized by installing an inertial measurement unit (IMU) module with Bluetooth on ordinary sports shoes. These four devices also collect 4 human activity recognition for motion data accordingly. The paper develops the motion data of four parts (head, wrist, waist and foot) of the four devices respectively, calls their IMU sensor modules, and transmits them to the PC server through Bluetooth or Wi-Fi at the same time after unifying the multisource data packet format. A data integration and processing platform is designed and developed on the PC side to uniformly process and analyze the multisource data received from the four devices. 

After the system receives data from the wearable devices, it first performs preprocessing operations on the data, mainly including action starting point detection, multisource data signal denoising and filtering, and autocorrelation calculation and action uniqueness representation extraction. After the representation is obtained, in order to achieve lightweight behaviour recognition, this paper uses the relevant theories of knowledge graphs in traditional artificial intelligence, and uses the OWL2 logical description specification proposed by the World Wide Web Consortium (W3C) combined with the subsequent summary of the action judgment relationship matrix to describe the behaviour recognition logic rules of this paper. The action to be recognized is taken as an entity, and the logical rules of each action can be distinguished as relational semantics, thus forming the logical reasoning hierarchy of the 12 behaviours to be recognized by this system. This logic contains the action entities and the judgment relationship between them, that is, the rules. 

Based on the above logical reasoning level, this system can perform behaviour recognition on the collected data. However, this paper found that the recognition results of some actions of different volunteers were not ideal, especially for the two groups of actions of running and walking, going upstairs and going downstairs. Analysis found that the two groups of action signals were very close, and the judgment relationship was also very similar, and the physiological characteristics of the volunteers were also very close. Therefore, this paper proposed the hypothesis that the physiological conditions of different users have a great influence on the specified logical rules. To solve this problem, this paper designed an algorithm for adaptive adjustment of the logical judgment relationship, through the root mean square (RMS) difference of each window of the walking action between different users, and combined with the recognition logical judgment conditions of the template user’s action to fit an adaptive function, so that the system can be initialized by pre-collecting the multisource data signal of the user’s walking action, and the personalized logical rules of the new user can be obtained under the calculation of the adaptive function, so that this system can realize robust behaviour recognition for different users. 

**Scientific Reports** |          (2025) 15:380 

4 

| https://doi.org/10.1038/s41598-024-84532-8 

www.nature.com/scientificreports/ 

## **Data collection and processing** 

Smart glasses, watches and mobile phones were worn on the volunteers’ heads, left wrists and waists (the mobile phones were placed in the side pockets of the pants), and the Bluetooth module with IMU was fixed on the outside of the volunteers’ right sports shoes. After communicating with the volunteers about precautions and requirements, the communication switches of all devices were turned on to connect them with the host. After collecting the data signals of the volunteers, this paper displayed the signals and made preliminary observations and analyses on them. The raw data signals of the accelerometer sensors for the two actions of going upstairs and going downstairs are shown in Fig. 2. 

Compared with the accelerometer sensor data signals of going upstairs in Fig. 2a and going downstairs in Fig. 2b, there are obvious differences between the two peaks in the cycle, and the peak of going upstairs is generally larger than that of going downstairs. At the same time, the data on the z-axis of the accelerometer also show that the order of the peaks and troughs in the two actions of going upstairs and going downstairs in one cycle is different. The movement rules of going upstairs and going downstairs in daily life are also different. Without considering special circumstances, since going upstairs is a state of climbing up, and going downstairs can be regarded as a state of walking downhill, going upstairs is generally slower than going downstairs. Moreover, from the perspective of each step, going upstairs is to lift the foot first and then put it down, while going downstairs is to put the foot down first, which corresponds to the signal difference described in Fig. 2a and b. Similarly, by comparing other actions, a preliminary feasibility analysis conclusion is obtained: the data generated by different actions on the IMU sensor are different, and each action has some signal characteristics that can be uniquely distinguished from other actions. This feature is also consistent with the common sense of movement of the action in the real world and known physical common sense. Then, an action signal detection algorithm based on the short-term energy change of the signal characteristic, namely the threshold overlapping sliding window model of RMS, is used to detect the starting point of the behaviour activity. According to the RMS value of each lower limb action, this paper sets the upper threshold to 10 and the lower threshold to 5. It is believed that when the RMS value in the window is greater than 10 or less than 5, the user’s lower limb has moved, which means that the user’s behaviour is moving, not standing still. The collected IMU raw data is processed and the data is preliminarily processed using the first-order complementary filter. In the first-order complementary filter, the weight of the accelerometer value is set to 0.1, and the filter sampling time is set to 0.005. Then, the mean smoothing filter is used, and the filter window is set to 5. By comparing the changes of the data signal in the time domain and frequency domain before and after filtering, it can be clearly seen that a lot of high-frequency noise is effectively removed. Then, the collected data signal is periodically detected using autocorrelation calculation, and the peak point of the signal is marked. And remove the abnormal peak points, the time interval between every two peaks is the movement cycle of this action. 

**==> picture [437 x 290] intentionally omitted <==**

**Fig. 2** . Data signal from the lower limb movement accelerometer. 

**Scientific Reports** |          (2025) 15:380 

5 

| https://doi.org/10.1038/s41598-024-84532-8 

www.nature.com/scientificreports/ 

**==> picture [196 x 21] intentionally omitted <==**

**----- Start of picture text -----**<br>
Brush Swing arm Typing Write<br>Brush – PERIOD.T PERIOD.If PERIOD.If<br>**----- End of picture text -----**<br>


||**Brush**|**Swing arm**|**Typing**|**Write**|
|---|---|---|---|---|
|Brush|–|PERIOD.T|PERIOD.If|PERIOD.If|
||||||
|Swing arm|PERIOD.T|–|PERIOD.If|PERIOD.If|
|Typing|PERIOD.If|PERIOD.If|–|ACC.Z.amp|
|Write|PERIOD.If|PERIOD.If|ACC.Z.amp|–|



**Table 1** . Upper limb action judgment relationship matrix. 

**==> picture [324 x 148] intentionally omitted <==**

**Fig. 3** . Standard logical language representation of cycling actions. 

## **Behaviour recognition based on logical reasoning** 

## _Action judgment relationship matrix_ 

The data signal is subjected to wavelet transform operation, and the frequency f, amplitude Amp, cycle length T, periodicity If and peak value Max of each action data signal are recorded. Combined with the physical laws of each action in reality, the action of standing still is quite special, because when this action occurs, all data signals have no characteristics, so this action does not need to be judged by the relationship matrix. Then the signal attributes that can be used to distinguish the other 11 actions are listed, that is, the discriminant relationship between actions. According to these judgment relationships, two actions can be selected. This paper uses these judgment relationships to propose a judgment relationship matrix for Behavioral actions. The matrix contains each action instance and the discrimination conditions between each two actions. The specific contents of the judgment relationship matrix of upper and lower limb actions are listed in Table 1. The data in Table 1 comes from the sensor in the smart watch. 

The judgment conditions in the matrix include signal properties such as periodicity, amplitude and frequency of each axis of the accelerometer, amplitude, frequency and maximum value of each axis of the gyroscope. These judgment conditions indicate that two actions can be judged based on the properties of a certain sensor data. For example, the two actions of walking and running can be distinguished by the amplitude and frequency of the accelerometer data in the combined direction. 

## _Logical rules for action judgment_ 

After obtaining the action judgment relationship matrix, the OWL2 ontology language is used to describe the logic, and the content in the matrix is abstracted. The content in the matrix can just serve as the relationship between entities in the description logic. For example: the main data of cycling action comes from the footstep’s device. Therefore, in order to judge the cycling action, it is necessary to first detect that the footsteps device has generated a valid motion signal, that is, the condition for judging the start of the action mentioned above is that the continuous RMS value is greater than the threshold. The footstep’s device provides the majority of the cycling action data. Consequently, the first stage in determining the cycle action is to determine whether the footsteps device has produced a legitimate motion signal; that is, the continuous RMS value must be higher than the threshold in order to determine when the activity indicated above began. In addition, each motion cycle completes a full circle on the bicycle’s side, and the footfall have regular periodic motions in accordance with the principle of cycling action. Therefore, compared with other behaviours mainly based on the lower limbs, the frequency amplitude of its gyroscope will show obvious differences, as shown in the content of the action judgment relationship matrix proposed in section “Action judgment relationship matrix”. Then use the standard logical language in ontology reasoning to describe it (see Fig. 3), and then use the logical description of each action to establish a behaviour recognition knowledge base based on the nine-axis IMU sensor data, and store all action descriptions in this library for easy call during recognition. 

It can be seen that there are many threshold settings in the description logic of cycling. Through the analysis and summary of the data of the experimenter, this paper sets some fixed thresholds for conditional judgment in the system. Based on the established behaviour recognition knowledge base, each action entity and the 

**Scientific Reports** |          (2025) 15:380 

6 

| https://doi.org/10.1038/s41598-024-84532-8 

www.nature.com/scientificreports/ 

description logic between them are displayed in a tree structure, and a behaviour recognition logic tree suitable for 12 actions of this system is constructed, as shown in Fig. 4. The input data of the logic tree is the action data of multiple sensors, and then it is classified according to the different judgment relationships in the logic tree, and finally the specific action category identified is output. The logic tree contains 12 action entities and the relationship between each action entity, among which the action entity is in the sharp-cornered rectangle, and the judgment relationship between entities is in the rounded rectangle. 

The logic tree of behaviour recognition is an abstract expression of the behaviour recognition knowledge base. It can be seen from the logic tree that after the data is collected by 4 devices, using the method of action starting point detection mentioned in the previous article, if the RMS value of the signal in 3 consecutive windows is detected to be less than the specified threshold, it is considered that no action has occurred. Then, the recognition algorithm for taking the escalator up and down is used to detect whether the user is riding the escalator. If not, the user is in a stationary state. If the RMS value of the signal in three consecutive windows is greater than the specified threshold, it is considered that an action has occurred. At the same time, the device with the largest RMS value is selected as the main sensor device for the action. Human activity sensors are utilized to gather ambient data, and adaptable neural networks are employed to recognize behaviour. This article developed a system for action recognition based on multimodal sensor data using a unique semi-stacked recurrent convolutional attention model. It also used a combination of multiple sensor data in mobile wearable devices to automatically learn the optimal features through deep convolutional neural networks, and it finished the recognition of daily behaviours and mid-air gestures, respectively. The part of the human activity recognition where the device is located is considered to be the main active limb (upper limb or lower limb) of this behaviour. If the signal of the foot device is weak or discontinuous, the user may not move and is in a stationary state. The specific behaviour of the user can be judged based on the data signal of the hand device. If the signal of the foot device meets the judgment conditions, the user’s lower limbs are moving. At the same time, the signal received by the hand device can also be judged, and the footsteps and hand movements can be recognized at the same time to provide more behaviour information. 

This paper designs a recognition algorithm specifically for the special situation of taking an elevator up or down. The core idea of the algorithm is very simple. It can effectively detect the obvious convex and concave waves in the accelerometer due to weightlessness and overweight when taking an elevator up or down. If the convex wave is detected first, it means going up, and vice versa, it means going down. This paper conducted 10 experiments on taking an elevator up or down, recording the peak or valley value of each convex or concave wave and the number of sampling points on both sides, and appropriately increased or decreased 10 units relative to the maximum or minimum value as the threshold to describe a convex wave or a concave wave. Whenever a convex wave or a concave wave is identified, it is considered to be the behaviour of taking an elevator up or down only when the adjacent valid action is a concave wave or a convex wave. 

**==> picture [362 x 297] intentionally omitted <==**

**Fig. 4** . Behaviour recognition rule logic tree. 

**Scientific Reports** |          (2025) 15:380 

7 

| https://doi.org/10.1038/s41598-024-84532-8 

www.nature.com/scientificreports/ 

## _Logical relationship adaptation_ 

Each logical relationship has one or more thresholds. In order to test the accuracy of the above action judgment logic, the system first uses a person’s data as a benchmark, and selects the threshold suitable for her/him in each logical relationship according to his/her data as the threshold of the logical relationship in the system. 

This paper selects the threshold of a volunteer and applies it to the logical relationship of lower limb actions. 19 volunteers were recruited. After they put on the equipment and collected data, the action logical relationship was used for behaviour recognition, and the recognition effect was observed to test whether it can be accurately judged. Each lower limb action was repeated for 60 s, and the data of these 19 volunteers were transmitted to the system to calculate the accuracy. The results showed that only one of the 19 volunteers was completely correctly recognized, while the others had large errors, especially in the four actions of walking, running, going up stairs and going down stairs. The poor recognition situation was analyzed again. By comparing the physiological characteristics of the 20 volunteers, namely height and weight, this paper found that: Volunteer No. 1 and Volunteer No. 4, which are the basic thresholds of the logical relationship in the system, are both girls and their physiological conditions in height and weight are very similar. The other volunteers have a lot of differences in physiological indicators. Gender differences not only lead to differences in body shape, but also in Behavioral habits. Therefore, this paper preliminarily judges that the body shape of different users will have a great impact on the recognition results of this system. 

In order to verify whether the above judgment is correct, the body posture information of each volunteer who took part in the experiment was registered. Through the statistics of body posture information, it was found that the body postures of different volunteers were indeed quite different. In response to this problem, this paper designed a method that can adaptively change the threshold in the logical relationship according to the user’s body posture characteristics. First, the matching thresholds that are completely suitable for each of the 20 volunteers were obtained, which are called the basic thresholds here. Then, through support vector regression SVR, a threshold adaptive function was fitted using the difference in RMS in the action start window of the “walking” action of different volunteers and their respective basic thresholds. With this fitting function, when a new user uses the system, it only needs to walk two steps, collect the “walking” data, and perform a simple calculation with the template threshold pre-existing in the system to complete the initialization, and then the logical relationship that conforms to the new user can be obtained. The algorithm idea of the adaptive threshold is shown in formula (1): 

**==> picture [400 x 13] intentionally omitted <==**

Among them, _F_ ( _x_ ) is the fitting function you want to get, and THRESHOLD _D_ BASE is the value. In this way, when you have the single “walk” action data of template user B and its threshold, combined with the data passed in by new user A, you can get a new threshold suitable for A. With the threshold suitable for the new user, you can Achieve adaptive action logic relationships. 

This article uses Support Vector Regression (SVR) to fit the objective function _F_ ( _x_ ). The threshold value of template user B’s single “move”, the threshold value of new user A’s single “move” and the RMS difference between the two people constitute a piece of data used by SVR. A total of 1330 such pieces were used during SVR fitting. data. By adjusting the fitting function and data segmentation method, it was finally determined that using the RBF kernel function and 50–50 training and testing of 20 people’s data can obtain the optimal fitting results, and then obtain a function _F_ ( _x_ ) that can automatically adjust the logical relationship. In order to verify the effect of the fitting function, a boy was randomly selected from the volunteers and selected together with the girl data collected in the previous article as template data. The thresholds in the action logic relationships in the system were set to thresholds suitable for their data and kept unchanged, and then the recognition test was carried out on each lower limb action of the other 19 volunteers, with the threshold of girls as the basis. 

After introducing the adaptive algorithm of the logical relationship threshold, this paper compares the previous results, and still uses the male and female selected in the previous article as the basic threshold for testing. The results show that regardless of whether the male or female is used as the basic threshold, the recognition results have different degrees of growth and improvement. 

## **Experimental part System implementation** 

This paper uses Google Glass3, Huawei smart watch Watch2, Xiaomi smart phone Redmi K20Pro and an IMU Bluetooth module to implement the BehaviorLog system. Google Glass3, Huawei Watch2 and Redmi K20Pro can all run Android programs. The Android programs for these three devices to send and receive IMU sensor data are developed using Java language, including user interface, business logic, network communication and data transmission. The Android platform provides interfaces for calling three sensors in the device: accelerometer, gyroscope and magnetometer, to facilitate developers to use. The IMU Bluetooth module on the foot uses the MPU9250 nine-axis IMU module to collect acceleration, gyroscope and magnetic intensity data. The control unit uses the Arduino Bluno microcontroller, the communication part uses the Bluetooth 4.0 module, and there is a power supply unit. MATLAB is used to develop the upper computer, and the lower computer code is written 2 in C language. The specific configuration of each device is listed in Table . On the PC The client/server model is used on the client side, and an application is developed to connect four devices and transmit data synchronously (the data integration and processing platform introduced in section “Related work”). The TCP data transmission method is adopted. The three devices, Google smart glasses, Huawei smart watches, and Xiaomi smart phones, are connected to the PC side through Wi-Fi signals, and the IMU module is connected to the PC side through Bluetooth. The sampling rate of each sensor is unified to 50 Hz. 

**Scientific Reports** |          (2025) 15:380 

8 

| https://doi.org/10.1038/s41598-024-84532-8 

www.nature.com/scientificreports/ 

**==> picture [242 x 22] intentionally omitted <==**

**----- Start of picture text -----**<br>
Device OS CPU Frequency (GHz)<br>Google Glass 3 Android4.0.4 OMAP 4430 1.2<br>**----- End of picture text -----**<br>


|**Device**|**OS**|**CPU**|**Frequency (GHz)**|
|---|---|---|---|
|Google Glass 3|Android4.0.4|OMAP 4430|1.2|
|Huawei Watch 2|AndroidWear 2.0|Snapdragon Wear 2100|1.2|
|XiaoMi K 20 Pro|MIUI 10|Snapdragon 855|2.84|
|IMU Module|MATLAB GUI|ATmega 328|16|



**Table 2** . Main parameters of the experimental equipment. 

## **Experimental plan** 

After using the experimental equipment introduced in the previous article to build the system, 20 experimental personnel were randomly recruited on campus, including 10 boys and 10 girls. After each person wore the equipment described in this article, they performed experiments on a total of 12 upper and lower limb movements (including sitting still, walking, running, riding a bicycle, going up and down stairs, taking an elevator up and down, swinging arms, brushing teeth, typing and writing). In addition to going up and down elevators and sitting still, each action was repeated 100 times in each scenario, and each person collected 30 times for taking an elevator up and down (three different elevators were used, two of which were in the college building, one was a normal passenger elevator, the other was a larger and slower freight elevator, and there was a passenger elevator in the dormitory building, each elevator was 10 times each) and sitting still for 60 s. 

In order to illustrate the universality of the method described in this article, in each scenario, each action was tested according to the above standards (since elevators are commonly found in buildings, they were only performed in the college building and the dormitory building). The experiment was conducted in the following scenarios: 

1.  Inside the college building. This scenario is the college teaching building, which has multiple laboratories, conference rooms, etc. During the experiment, in order to simulate the daily situation in the college building, the experiment was conducted in this scenario on weekdays. It was allowed for people to pass by the volunteers, and interference from others was allowed when the action was uninterrupted. 

2.  Student dormitory. The dormitory area is about 4 m × 12 m, with a total of 4 people. During the experiment, people in the dormitory were allowed to work, chat or occasionally walk freely as usual. 

3.  Open space outside the college building. This scenario is the campus outside the teaching building, with more vehicles and pedestrians. In order to further increase environmental interference, this paper chose to conduct the experiment during the noon time period when there are more students or passers-by. 

It should be noted that when conducting the experiment of going up and down stairs, the interval between the two flights of stairs was walked normally without stopping. When conducting the experiment of taking the elevator up and down, people who were not related to the experiment were allowed to be in the elevator, and the number of floors to go up or down was not fixed. When conducting the experiment of cycling, two different bicycles were selected. At the same time, before conducting the experiment on each volunteer, this paper will record their height and weight. 

The experimental evaluation includes the following parts: (1) Compare the test results in different scenarios to evaluate the impact of different environments on the system; (2) Compare the test results of different users when using the system to evaluate the impact of different users on the system; (3) Compare with the methods that require data training, select the support vector machine, decision tree in the machine learning method and the CNN model in deep learning, through optimization and testing, use the optimal model for recognition, and count the recognition results respectively, and compare with the results obtained by the system implemented in this paper. Here, the recognition accuracy of each action is expressed as the proportion of the number of correctly recognized actions to the total number of actions. 

## **Behaviour recognition experimental results and evaluation of logical reasoning** 

## _Scenario diversity_ 

To evaluate the impact of different environments on the system, experiments were conducted in the above three scenarios. Due to the particularity of the scenarios in which some actions occur, some actions are only tested in the corresponding scenarios, such as cycling can only be performed outdoors, so the accuracy result of Cycle in the figure only has one scenario. We used experimental data of 10 actions (walking, running, going up stairs, going down stairs, cycling, typing, writing, swinging arms, brushing teeth and standing still) except taking the elevator up and down. As shown in Fig. 5, scene 1 corresponds to the scene inside the college building, scene 2 corresponds to the scene inside the student dormitory, and scene 3 corresponds to the scene outside the college building. The data of the same volunteer in the three scenarios were used for testing. The average recognition results of the three actions (brushing teeth, walking and swinging arms) that can be tested in all three scenarios are 92.3%, 93.7% and 92. 9%, the results are not much different. The experimental results show that different scenes and environments have almost no effect on the recognition effect of this system. This is because the IMU sensor is only sensitive to the user’s motion state. Using logical judgment and behaviour recognition, it is possible to recognize the daily behaviour of users in a lightweight and reliable manner. Behaviour Log employs four popular wearables as perception units: smart watches, smart phones, smart glasses, and smart running shoes. By adding an inertial measurement unit (IMU) module with Bluetooth to standard athletic shoes, these smart running shoes are made possible. For motion data, these four devices additionally gather four human 

**Scientific Reports** |          (2025) 15:380 

9 

| https://doi.org/10.1038/s41598-024-84532-8 

www.nature.com/scientificreports/ 

**==> picture [363 x 202] intentionally omitted <==**

**Fig. 5** . Recognition accuracy in different scenarios. 

**==> picture [363 x 218] intentionally omitted <==**

**Fig. 6** . Recognition accuracy of different vertical elevators. 

activity recognition data points. When the user’s motion state does not change, other factors have almost no interference with it. 

Then, we conducted experiments on the recognition of elevator riding in three different elevators, corresponding to elevator1, elevator2 and elevator3 in Fig. 6. Elevator1 and elevator2 are two different passenger elevators, and elevator3 is a freight elevator. We randomly selected data from nine volunteers for testing, and each volunteer took each elevator up and down five times. It can be seen that the recognition accuracy of the two passenger elevators is very high, reaching 98.9% and 97.8% on average. Only one or two of the ten tests were misidentified due to the crowding in the elevator, which caused the volunteers to make extra movements in the elevator. The recognition of the freight elevator was relatively poor because the situation in the freight elevator was more complicated, and the freight elevator rose or fell at a slower speed, which was also prone to jitter. But overall, the recognition of different elevators was similar, proving that the different types of elevators would not affect the recognition of the action by this system. 

## _User diversity_ 

Since the physiological characteristics and exercise habits of each user are different, in order to verify the system’s support for user diversity, the experimental data of 19 volunteers who provided the basic threshold were selected 7 for recognition. The results are shown in Fig. . It can be seen that there is no big difference in the recognition 

**Scientific Reports** |          (2025) 15:380 

10 

| https://doi.org/10.1038/s41598-024-84532-8 

www.nature.com/scientificreports/ 

**==> picture [363 x 206] intentionally omitted <==**

**Fig. 7** . Recognition accuracy among different users. 

results of these 19 users. The average recognition accuracy reached 89.3%, and the standard deviation was about 1.8%, indicating that the recognition effect of the system is not much different for different users. 

## **Comparative evaluation with machine learning techniques** 

_Traditional machine learning methods for behaviour recognition_ 

This paper proposes a lightweight non-training behaviour recognition technology, and compares the behaviour recognition results using machine learning methods under the same data set. Two common machine learning methods (support vector machine SVM and decision tree DT) are selected here to recognize lower limb movements. 

SVM and DT both adopt two training and testing methods. One is single-user recognition, using 70% of a person’s data for training and 30% for testing to obtain a recognition result; the other is cross-person recognition, using the data of 10 out of 20 volunteers for training and the remaining 10 for testing to obtain a recognition result. The data sets of both methods are randomly divided, so when adjusting the optimal model, it is repeated 10 times, and then the average recognition rate is calculated. A field of study called Human Activity Recognition (HAR) aims to develop and evaluate new methods for precisely identifying human activities through signals. Datasets from vision-based and sensor-based devices can be used to create state-of-the-art activity recognition algorithms. The majority of early activity recognition research, including, concentrated on vision-based activity identification, which produced systems that could successfully identify activities. By strategically positioning capturing devices, like cameras, to record the actions of environmental elements, the vision-based dataset is produced. Figure 8a and b show the confusion matrix of the action recognition results using the SVM model under two training and testing methods. It can be seen from the confusion matrix that the human activity recognition result of SVM is still very high. After repeating training and testing 10 times, the average recognition rate of single user recognition reached 95%. 4%, but the cross-person recognition rate is only 84.7%. Through optimization and testing, the methods that require data training—the CNN model in deep learning, the support vector machine, and the decision tree in machine learning—select the best model for recognition, count the results of that recognition, and compare them with the outcomes of the system used in this paper. In this case, the proportion of successfully recognized actions to all actions is used to describe the recognition accuracy of each action. This also shows that the method of using data training also needs to overcome the difficulty of cross-person recognition. There are differences in the action data signals of different users. The reduction in the cross-person recognition rate illustrates this point. It can be seen that the main problem is still concentrated on the actions of going up and down stairs, walking and running. This also verifies the hypothesis proposed in this article again. Similar to the results obtained by SVM, the recognition rate of cross-person recognition by the decision tree has decreased. After 10 repeated training and testing, the average recognition rate of single user recognition is 86.9%, and the cross-person recognition rate has dropped to 80.2%. 

## _Deep learning method to achieve behaviour recognition_ 

For the data set collected in the previous article, the length of a piece of data is uniformly divided according to 100 sampling points on 9 data channels, that is, the size of a piece of data is 9*100. Finally, 50% of all data is used for deep learning training, 25% for verification, and 25% for testing. Then this paper implements a deep learning model based on the Keras framework for behaviour recognition, and designs and implements a convolutional neural network model based on LeNet. The recognition accuracy of this model under 30, 40 and 50 iterations are 88.7%, 92.5% and 91.9% respectively, and the average is 91%. 

**Scientific Reports** |          (2025) 15:380 

11 

| https://doi.org/10.1038/s41598-024-84532-8 

www.nature.com/scientificreports/ 

**==> picture [361 x 472] intentionally omitted <==**

**Fig. 8** . ( **a** ) Introducing former female students as templates. ( **b** ) Introducing former male students as templates. 

## _Comparative evaluation_ 

After summarizing the human activity recognition results in the previous article, the recognition effects of the four technical means in cross-person recognition were obtained. As shown in Fig. 9, the average recognition accuracy of the system proposed in this topic is 89.3%, the average recognition accuracy of deep learning is 91%, the average recognition accuracy of SVM is 84.7%, and the average recognition accuracy of DT is only 80.2%. It is not difficult to find that compared with traditional machine learning, the method in this paper has certain advantages in recognition results. It is difficult for SVM and DT methods to get rid of the problem of poor accuracy in cross-person recognition. Compared with the human activity recognition effect of deep learning, the human activity recognition accuracy of this paper is slightly lower, but the deep learning method requires longer samples and more computing time. 

Then, the number of samples and the required operation time (here, specifically the amount of data and operation time required to implement the human activity recognition model or recognition logic, and the operation time is the average of 10 times) required by the system implemented in this paper and the above two data training-based technical means to achieve behaviour recognition were counted. As shown in Fig. 10, it can be clearly seen that, by comparison, the system proposed in this paper does not require a large amount of sampled data, and the operation time required by the system is much shorter than that of the other two methods. 

**Scientific Reports** |          (2025) 15:380 

12 

| https://doi.org/10.1038/s41598-024-84532-8 

www.nature.com/scientificreports/ 

**==> picture [363 x 205] intentionally omitted <==**

**Fig. 9** . Comparison of recognition results of four technologies. 

This is very friendly to small mobile smart devices, successfully getting rid of the long operation time brought by a large number of samples, and realizing lightweight behaviour recognition. From the current comparison of results, the new behaviour recognition technology proposed in this paper has made a breakthrough. 

## **Conclusion** 

This paper uses the relevant theories of ontology reasoning in traditional artificial intelligence to design a lightweight behaviour recognition solution, realizing the organic combination of signal processing and logical reasoning in behaviour recognition research. The inertial measurement unit (IMU) sensor commonly found on commercial smart devices is used to collect the user’s motion data signals. The logical relationship between the 12 movements of the upper and lower limbs is extracted through signal processing related technologies and the common sense of the laws of human activity recognition in the real world. The behaviour recognition without data training is realized by logical reasoning. This paper also designs and implements the adaptive function of the logical relationship, which solves the barrier that the fixed threshold in the logical relationship cannot match different users. Through experimental testing and analysis, the average accuracy of the system when randomly selecting the data of a woman and a man as the basic threshold for human activity recognition is 92.1% and 90.8% respectively. After introducing the adaptive algorithm, the human activity recognition accuracy is increased by 9.6% and 5.2% respectively. The reliance of logical reasoning on premises or assumptions is one of its drawbacks. A set of premises that are taken for granted form the foundation of logical reasoning. These presumptions, however, could not always be true or dependable, which could result in faulty reasoning. At the same time, when using the same data set, machine learning technology is used for behaviour recognition. After adjusting parameters and testing, the results of cross-person recognition after selecting the optimal model are 92.1% and 90.8% respectively, which is not much different from the system evaluation results proposed in this paper. However, the machine learning method is much more demanding in terms of data sample volume and computing time than the system proposed in this paper. 

Although this paper has achieved lightweight behaviour recognition, there are still some areas that can be continuously improved and supplemented. 

1.  The recognition content of this system is still limited to some basic behaviours such as walking, running, going up and down stairs, and it cannot recognize more specific behaviours such as sweeping the floor, eating, and watching TV. In this regard, other sensor device information can be added, such as microphones, GPS, etc., so that more scene information can be added, and body movements and scenes can be combined to achieve more fine-grained recognition content. 

2.  When using this system, the IMU sensors of each device must always be turned on and connected to the host. This brings a lot of extra power consumption and shortens the power-on time of the device. For this, polling or triggering methods can be used to reduce power consumption. 

3.  The signal processing part will take up a lot of system response time. Although it is not as complex as machine learning, it also takes up a lot of resources. Therefore, optimizing the data processing algorithm is also a top priority. In order to further transplant this system to smaller mobile intelligent terminals, a new behaviour recognition method is provided for mobile intelligent terminals. 

**Scientific Reports** |          (2025) 15:380 

13 

| https://doi.org/10.1038/s41598-024-84532-8 

www.nature.com/scientificreports/ 

**==> picture [361 x 484] intentionally omitted <==**

**Fig. 10** . ( **a** ) No. of samples used comparison of recognition results. ( **b** ) Training time comparison of recognition results. 

## **Data availability** 

The datasets used and/or analysed during the current study available from the corresponding author on reasonable request. 

Received: 24 October 2024; Accepted: 22 December 2024 

**==> picture [133 x 12] intentionally omitted <==**

## **References** 

1. Kim, M., Cho, M., Chung, C. & Kyung, K.-U. Stretchable, transparent and multifunctional PVC-gel heater: A novel approach to skin-mountable, wearable thermal devices. _npj Flex. Electron._ **8** (1), 59 (2024). 

> 2. Li, Y.-L. et al. HAKE: A knowledge engine foundation for human activity understanding. _IEEE Trans. Pattern Anal. Mach. Intell._ **45** (7), 8494–8506. https://doi.org/10.1109/TPAMI.2022.3232797 (2023). 

> 3. Zhu, Y. et al. A flexible and biocompatible triboelectric nanogenerator with tunable internal resistance for powering wearable devices. _Sci. Rep._ **6** (1), 22233 (2016). 

**Scientific Reports** |          (2025) 15:380 

14 

| https://doi.org/10.1038/s41598-024-84532-8 

www.nature.com/scientificreports/ 

4. Tang, W., Qing, L., Li, L., Wang, Y. & Zhu, C. Progressive graph reasoning-based social relation recognition. _IEEE Trans. Multimed._ **26** , 6012–6024. https://doi.org/10.1109/TMM.2023.3344359 (2024). 

5. Hayano, J., Adachi, M., Sasaki, F. & Yuda, E. Quantitative detection of sleep apnea in adults using inertial measurement unit embedded in wristwatch wearable devices. _Sci. Rep._ **14** (1), 4050 (2024). 

6. Arias, O., Wurm, J., Hoang, K. & Jin, Y. Privacy and security in internet of things and wearable devices. _IEEE Trans. Multi-Scale Comput. Syst._ **1** (2), 99–109. https://doi.org/10.1109/TMSCS.2015.2498605 (2015). 

7. Zhao, S., Hong, X., Yang, J., Zhao, Y. & Ding, G. Toward label-efficient emotion and sentiment analysis. _Proc. IEEE_ **111** (10), 1159–1197. https://doi.org/10.1109/JPROC.2023.3309299 (2023). 

8. Klimek, R. Exploration of human activities using message streaming brokers and automated logical reasoning for ambient-assisted services. _IEEE Access_ **6** , 27127–27155. https://doi.org/10.1109/ACCESS.2018.2834532 (2018). 

9. Zolfaghari, S., Stoev, T. & Yordanova, K. Enhancing kitchen activity recognition: A benchmark study of the rostock KTA dataset. _IEEE Access_ **12** , 14364–14384. https://doi.org/10.1109/ACCESS.2024.3356352 (2024). 

10. Popoola, O. P. & Wang, K. Video-based abnormal human behavior recognition: A review. _IEEE Trans. Syst. Man Cybern. Part C (Appl. Rev.)_ **42** (6), 865–878. https://doi.org/10.1109/TSMCC.2011.2178594 (2012). 

11. Wang, Z. et al. A survey on CSI-based human behavior recognition in through-the-wall scenario. _IEEE Access_ **7** , 78772–78793. https://doi.org/10.1109/ACCESS.2019.2922244 (2019). 

12. Chen, Y. & Shen, C. Performance analysis of smartphone-sensor behavior for human activity recognition. _IEEE Access_ **5** , 3095– 3110. https://doi.org/10.1109/ACCESS.2017.2676168 (2017). 

13. Xing, Y. et al. Driver activity recognition for intelligent vehicles: A deep learning approach. _IEEE Trans. Veh. Technol._ **68** (6), 5379–5390. https://doi.org/10.1109/TVT.2019.2908425 (2019). 

14. Brdiczka, O., Langet, M., Maisonnasse, J. & Crowley, J. L. Detecting human behavior models from multimodal observation in a smart home. _IEEE Trans. Autom. Sci. Eng._ **6** (4), 588–597. https://doi.org/10.1109/TASE.2008.2004965 (2009). 

15. Dong, Q., Wu, Y. & Hu, Z. Pointwise Motion Image (PMI): A novel motion representation and its applications to abnormality detection and behavior recognition. _IEEE Trans. Circuits Syst. Video Technol._ **19** (3), 407–416.  h t t p s : / / d o i . o r g / 1 0 . 1 1 0 9 / T C S V T . 2 0 0 9 . 2 0 1 3 5 0 3 (2009). 

- 16 Deep, S. et al. A survey on anomalous behavior detection for elderly care using dense-sensing networks. _IEEE Commun. Surv. Tutor._ **22** (1), 352–370. https://doi.org/10.1109/COMST.2019.2948204 (2020). 

17. Ramirez, J., Segura, J. C., Gorriz, J. M. & Garcia, L. Improved voice activity detection using contextual multiple hypothesis testing for robust speech recognition. _IEEE Trans. Audio Speech Lang. Process._ **15** (8), 2177–2189. https://doi.org/10.1109/TASL.2007.903937 (2007). 

18. Candamo, J., Shreve, M., Goldgof, D. B., Sapper, D. B. & Kasturi, R. Understanding transit scenes: A survey on human behaviorrecognition algorithms. _IEEE Trans. Intell. Transp. Syst._ **11** (1), 206–224. https://doi.org/10.1109/TITS.2009.2030963 (2010). 

19. Gao, W., Wei, T., Huang, H., Chen, X. & Li, Q. Toward a systematic survey on wearable computing for education applications. _IEEE IoT J._ **9** (15), 12901–12915. https://doi.org/10.1109/JIOT.2022.3168324 (2022). 

- 20 Jeon, E. S. et al. Role of data augmentation strategies in knowledge distillation for wearable sensor data. _IEEE IoT J._ **9** (14), 12848– 12860. https://doi.org/10.1109/JIOT.2021.3139038 (2022). 

21. Guo, A. & Ma, J. Context-aware scheduling in personal data collection from multiple wearable devices. _IEEE Access_ **5** , 2602–2614. https://doi.org/10.1109/ACCESS.2017.2666419 (2017). 

22. Hu, Y. et al. An ensemble classification model for depression based on wearable device sleep data. _IEEE J. Biomed. Health Inform._ **28** (5), 2602–2612. https://doi.org/10.1109/JBHI.2023.3258601 (2024). 

23. Kim, J. & Kim, S. Data analysis for thermal disease wearable devices. _J. Web Eng._ **20** (1), 89–102.  h t t p s : / / d o i . o r g / 1 0 . 1 3 0 5 2 / j w e 1 5 4 0 - 9 5 8 9 . 2 0 1 4 (2021). 

24. Pathak, N., Mukherjee, A. & Misra, S. SemBox: Semantic interoperability in a box for wearable e-health devices. _IEEE J. Biomed. Health Inform._ **27** (5), 2306–2313. https://doi.org/10.1109/JBHI.2022.3168071 (2023). 

- 25 Lin, H., He, Q., Hu, J. & Wang, X. Blockchain-based data access security solutions for medical wearables. _IEEE/ACM Trans. Comput. Biol. Bioinform._ **21** (4), 1117–1128. https://doi.org/10.1109/TCBB.2023.3281819 (2024). 

26. Jiang, Z., Van Zoest, V., Deng, W., Ngai, E. C. H. & Liu, J. Leveraging machine learning for disease diagnoses based on wearable devices: A survey. _IEEE IoT J._ **10** (24), 21959–21981. https://doi.org/10.1109/JIOT.2023.3313158 (2023). 

- 27 Tanveer, M., Khan, A. U., Ahmad, M., Nguyen, T. N. & El-Latif, A. A. A. Resource-efficient authenticated data sharing mechanism for smart wearable systems. _IEEE Trans. Netw. Sci. Eng._ **10** (5), 2525–2536. https://doi.org/10.1109/TNSE.2022.3203927 (2023). 

- 28 Seneviratne, S. et al. A survey of wearable devices and challenges. _IEEE Commun. Surv. Tutor._ **19** (4), 2573–2620.  h t t p s : / / d o i . o r g / 1 0 . 1 1 0 9 / C O M S T . 2 0 1 7 . 2 7 3 1 9 7 9 (2017). 

29. Zhan, C., Dai, Z., Yin, S., Carroll, K. C. & Soltanian, M. R. Conceptualizing future groundwater models through a ternary framework of multisource data, human expertise, and machine intelligence. _Water Res._ **257** , 121679 (2024). 

- 30 Guo, Y., Tang, J., Liu, H., Yang, X. & Deng, M. Identifying up-to-date urban land-use patterns with visual and semantic features based on multisource geospatial data. _Sustain. Cities Soc._ **101** , 105184 (2024). 

31. Zhong, H., Xu, R., Lu, H., Liu, Y. & Zhu, M. Dynamic assessment of population exposure to traffic-originated PM2.5 based on multisource geo-spatial data. _Transp. Res. Part D Transp. Environ._ **124** , 103923 (2023). 

- 32 Zhu, L. et al. Multisource Wasserstein adaptation coding network for EEG emotion recognition. _Biomed. Signal Process. Control_ **76** , 103687 (2022). 

- 33 Cang, J., Wu, P. & Lin, S. Redefining the boundaries of Chinese cities: Analysis based on multisource geographical big data. _Cities_ **149** , 104984 (2024). 

- 34 Ren, K. et al. TEMDI: A temporal enhanced multisource data integration model for accurate PM2.5 concentration forecasting. _Atmos. Pollut. Res._ **15** (11), 102269 (2024). 

35. Zanetti, R., Arza, A., Aminifar, A. & Atienza, D. Real-time EEG-based cognitive workload monitoring on wearable devices. _IEEE Trans. Biomed. Eng._ **69** (1), 265–277. https://doi.org/10.1109/TBME.2021.3092206 (2022). 

## **Author contributions** 

Conceptualization, Methodology, Software, Original Writing, Validation, Visualization: Mahmood Alsaadi, Ismail Keshta, Janjhyam Venkata Naga Ramesh and Divya Nimma. Software, Review and write up, Resources, Data Curation, Project Administration and Supervisor: Mohammad Shabaz, Nirupma pathak, Pavitar Parkash Singh, Sherzod Kiyosov and Mukesh Soni. 

## **Declarations** 

## **Competing interests** 

This research does not involve any human or animal participation. 

**Scientific Reports** |          (2025) 15:380 

15 

| https://doi.org/10.1038/s41598-024-84532-8 

www.nature.com/scientificreports/ 

## **Ethical consent** 

Informed Consent was obtained from all the participants involved in the study. 

## **Bioethics and guidelines** 

The protocol was approved by Model Institute of Engineering and Technology Review Board in accordance with the relevant guidelines of the Model Institute of Engineering and Technology, Jammu, J&K, India. 

## **Additional information** 

**Correspondence** and requests for materials should be addressed to M.S. 

**Reprints and permissions information** is available at www.nature.com/reprints. 

**Publisher’s note** Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations. 

**Open Access** This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if you modified the licensed material. You do not have permission under this licence to share adapted material derived from this article or parts of it. The images or other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit  h t t p : / / c r e a t i v e c o m m o n s . o r g / l i c e n s e s / b y - n c - n d / 4 . 0 / . 

© The Author(s) 2024 

**Scientific Reports** |          (2025) 15:380 

16 

| https://doi.org/10.1038/s41598-024-84532-8 

