### Tóm tắt:
Bài báo đề xuất mô hình FIBiLS sử dụng mạng nơ-ron tích chập 1 chiều (1-D CNN) kết hợp với BiLSTM để phát hiện sớm các sự cố té ngã ở người cao tuổi thông qua dữ liệu từ cảm biến đo lường quán tính (IMU). Nghiên cứu sử dụng tập dữ liệu SisFall công khai để huấn luyện và đánh giá mô hình, đạt độ chính xác ấn tượng lên tới 99,68%. Để tối ưu hóa cho các thiết bị biên, mô hình đã được nén thông qua các kỹ thuật cắt tỉa, lượng tử hóa và triển khai thử nghiệm thành công trên vi điều khiển NodeMCU. Giải pháp này hứa hẹn mang lại một phương pháp theo dõi thời gian thực gọn nhẹ, hiệu quả và có chi phí thấp giúp bảo vệ an toàn cho người già.

### BibTeX:
```bibtex
@article{gaud2025fibils,
  author={Gaud, Neha and Rathore, Maya and Suman, Ugrasen and Semwal, Vijay Bhaskar},
  journal={IEEE Sensors Journal},
  title={FIBiLS: Fall Detection of Healthy Elderly Using IMU Sensor and BiLSTM Model},
  year={2025},
  volume={25},
  number={19},
  pages={37124-37127},
  doi={10.1109/JSEN.2025.3602945}
}
```

---

## NỘI DUNG BÀI BÁO CHI TIẾT

IEEE SENSORS JOURNAL, VOL. 25, NO. 19, 1 OCTOBER 2025 

37124 

## FIBiLS: Fall Detection of Healthy Elderly Using IMU Sensor and BiLSTM Model 

Neha Gaud , _Member, IEEE_ , Maya Rathore , _Member, IEEE_ , Ugrasen Suman , and Vijay Bhaskar Semwal, _Senior Member, IEEE_ 

_**Abstract**_ **—Fall recovery refers to an individual’s ability to recover from external perturbation, and it is an obvious phenomenon in cluttered environments. Fall detection systems have evolved primarily for elderly individuals, who are more prone to falls that may lead to permanent disability or even death. In this article, a novel deep learning-based approach for early fall detection and monitoring individuals is proposed, while they perform daily tasks. The current Industry 4.0 revolution has witnessed the growing popularity of Internet of Things (IoT)-based solutions, with wearable sensing technology driving the use of wearable sensors for detecting such activities. This research utilizes dual wearable inertial measurement unit (IMU) sensors, worn on the body,** 

**==> picture [229 x 113] intentionally omitted <==**

**to monitor elderly individuals and detect potential falls during daily activities. The SisFall dataset, a publicly available dataset of falls, is used to train the deep learning-based model. The dataset includes 14 distinct fall categories, which account for various directions and magnitudes of falls. Data are collected for experimental purposes to evaluate the fall detection capabilities of elderly individuals. The SisFall dataset includes two age groups: adults (18 years and older) and the elderly (60 years and older). The research utilizes a 1-D convolutional neural network (CNN) and a bidirectional long short-term memory (BiLSTM) model to predict fall categories. The proposed FIBiLS (fall detecting using IMU sensor data and BiLSTM model) deep learning model demonstrates superior performance, achieving an accuracy of 99.68% with fast inference time. To facilitate edge computing, the method is implemented on a node MCU microcontroller board for fall detection. This approach outperforms previous research in both accuracy and complexity, providing better results with a more compact and less complex solution. This solution provides confidence to elderly individuals, enabling them to walk safely and independently.** 

_**Index Terms**_ **— Deep learning, edge computing, fall recovery, inertial measurement unit (IMU) sensors, Internet of Things (IoT), wearable device.** 

## I. INTRODUCTION 

ALLS is a major reason for the safety of elderly subjects **F** due to poor musculoskeletal integrity [2]. Aging affects their ability to negotiate external perturbation, which can lead to untimely death and permanent disability [3]. This becomes a significant factor of fear for older adults walking independently and potentially results in high medical costs [4]. Therefore, it is crucial to continuously monitor the daily activities of elderly patients, record fall incidents, and provide immediate support or intervention to prevent 

Received 3 June 2025; accepted 23 August 2025. Date of publication 1 September 2025; date of current version 2 October 2025. The associate editor coordinating the review of this article and approving it for publication was Dr. Junhui Qian. _(Corresponding author: Neha Gaud.)_ 

Neha Gaud and Ugrasen Suman are with the School of Computer Science and Information Technology (SCSIT), DAVV, Indore 30332, India (e-mail: neha28gaud@gmail.com; ugrasen123@yahoo.com). 

Maya Rathore is with the Chameli Devi Group of Institutions, Indore 452020, India (e-mail: mayarathore114@gmail.com). 

Vijay Bhaskar Semwal is with the Department of CSE, MANIT Bhopal, Bhopal 462003, India (e-mail: vsemwal@manit.ac.in). Digital Object Identifier 10.1109/JSEN.2025.3602945 

further health deterioration [5]. Their mental health is also affected by these incidents since their fear of falling reduces their independence and quality of life [6]. It is crucial to develop technologies that can promptly identify falls and provide assistance in such cases [7]. Elderly individuals are particularly vulnerable to external forces, and they may lose balance while performing activities such as walking, running, or jogging [8]. The impact of a fall can be severe, leading to untimely death, memory loss, multiple injuries, or permanent disabilities [9]. The fall recovery capability of human beings depends on reflexive patterns [10]. The most widely used data collection techniques for fall tracking are computer vision and wearable sensor-based methods [11]. Researchers have used deep learning-based models for fall detection [12]. Deep learning techniques are more accurate in capturing intricate movement patterns without providing explicit features [13]. Fig. 1 shows the amplitude reading of different phases of fall while performing the daily activities. However, Fig. 2 shows the accelerometer reading for various fall events while performing the daily activities. 

1558-1748 © 2025 IEEE. All rights reserved, including rights for text and data mining, and training of artificial intelligence and similar technologies. Personal use is permitted, but republication/redistribution requires IEEE permission. Authorized licensed use limited to: Hanoi University of Science & Technology. Downloaded on April 02,2026 at 01:06:24 UTC from IEEE Xplore.  Restrictions apply. See https://www.ieee.org/publications/rights/index.html for more information. 

GAUD et al.: FIBiLS: FALL DETECTION OF HEALTHY ELDERLY USING IMU SENSOR AND BiLSTM MODEL 

37125 

## TABLE I 

SUMMARY OF STATE-OF-THE-ART WORK 

**==> picture [480 x 127] intentionally omitted <==**

**==> picture [168 x 101] intentionally omitted <==**

**==> picture [67 x 167] intentionally omitted <==**

**==> picture [168 x 67] intentionally omitted <==**

Fig. 1. Different fall subphases. 

**==> picture [219 x 159] intentionally omitted <==**

Fig. 2. Accelerometer recording for various fall events. 

The wearable sensor-based suits integration with a variety of sensors is becoming popular. However, these suits are difficult to wear for constant monitoring and tend to have inherent noise [10], and still, they are cost-effective. Researchers are exploring alternative techniques to capture fall data, such as using cameras, infrared sensors, or integrating other nonwearable sensor types. These techniques are costly and inaccurate. The goal of this research is to improve and simplify the design of fall detection systems by wearable hardware with deep learning methods [14]. Particularly in aging populations, these systems are a critical step in maintaining the independence, 

health, and safety of senior citizens [15]. Further, with the advancement of low-power edge devices, given the motivation of using a microcontroller board to run a deep learning model for real-time monitoring [16], [17]. 

The research proposes an early fall detection system that can later be integrated with an Internet of Things (IoT) system for early warning of falls, aiming to protect the health of the elderly population. Hardware such as node MCU (ESP32) microcontrollers (which process data), accelerometers (which measure speed), gyroscopes (which track rotation), and magnetometers (which detect direction), as well as the inertial measurement unit (IMU) (MPU6050) sensor (which measures movement), is used for the detection of falls. To identify falls in real-time, these sensors monitor changes in movement and transmit the data to the computer for training of deep learning models, such as convolutional neural networks (CNNs) (which are good at capturing spatial dependency), LSTMs (good at capturing sequential and temporal dependency), or combinations of these models [18]. The contribution of the author is listed as follows. 

## _A. Author’s Contribution_ 

The major contribution of this work is divided into four parts: data collection and preprocessing, model design and integration, design of an optimized compressed model, and performance compression. The whole work is divided as follows. 

- 1) _Data collection and preprocessing:_ For data collection, wearable IMU sensor-based method is used. The public dataset SisFall [1] is used in this study. For data preprocessing, various normalization and noise removal techniques are used [19]. 

- 2) _Model design and integration:_ To train the fall detection model, 1-D CNN with a bidirectional long short-term memory (BiLSTM)-based deep learning model is used to capture for spatial and temporal nature of the data. 

- 3) _Design of optimized compressed model:_ To support edge computing, the designed model is compressed using pruning and quantization to reduce model size. 

- 4) _Performance analysis:_ To evaluate the performance postcompression and after compression, the standard matrix accuracy, F1-score, precision, and recall are calculated and compared with the benchmark dataset. 

Authorized licensed use limited to: Hanoi University of Science & Technology. Downloaded on April 02,2026 at 01:06:24 UTC from IEEE Xplore.  Restrictions apply. 

IEEE SENSORS JOURNAL, VOL. 25, NO. 19, 1 OCTOBER 2025 

37126 

**==> picture [456 x 171] intentionally omitted <==**

Fig. 3. Fall detection system overview. 

**==> picture [249 x 115] intentionally omitted <==**

Fig. 4. Backward fall signal during walking when a slip occurs. 

- 5) _Deployment on node MCU:_ To support edge computing, the compressed model was fused on the node MCU board for real-time monitoring. 

## _B. Organization of This Article_ 

The whole article is organized into five sections as follows. Section I is the introduction section, which covers the intrinsic capability of individuals to fall and the ability to negotiate external forces. Section II is a review of the literature that provides a systematic review of recent state-of-the-art research on the diagnosis and recovery capacity of falls in recent years. Section III is the methodology section, which covers the description of private and public datasets, various preprocessing steps, the evaluation matrix, and the algorithm. Section IV presents the results and discussion, demonstrating the superiority of the FIBiLS model across different datasets. Section V concludes the paper and outlines directions for future work, emphasizing the critical aspects of the fall and the inherent limitations. 

## II. LITERATURE REVIEW 

Since elderly subjects experience health hazards during falls due to aging, as aging leads to various cognitive and physical changes. Detection of falls using deep learning has emerged as a significant study subject [4]. Table I presents the recent state-of-the-art work done in the field of fall diagnosis and human activity recognition (HAR) based on wearable sensors. 

**==> picture [249 x 110] intentionally omitted <==**

Fig. 5. Forward fall signal during walking when a tip occurs. 

**==> picture [227 x 136] intentionally omitted <==**

Fig. 6. SisFall data distribution. 

This section also presents a few popular approaches used for fall data classification. 

## _A. Ambient-Based Approaches_ 

Ambient-based technologies have been developed to address wearable device issues. Without the need of clothing, these systems detect falls using sensors positioned throughout the surroundings for example, utilizing floor vibration sensors. However, if the sensors are not positioned correctly or in complex areas, these systems may be inaccurate [21]. 

## _B. Vision-Based Approaches_ 

Vision-based systems use cameras or CCTV to keep close track of individuals and identify falls. For example, 

Authorized licensed use limited to: Hanoi University of Science & Technology. Downloaded on April 02,2026 at 01:06:24 UTC from IEEE Xplore.  Restrictions apply. 

GAUD et al.: FIBiLS: FALL DETECTION OF HEALTHY ELDERLY USING IMU SENSOR AND BiLSTM MODEL 

37127 

TABLE II 

DATASET DESCRIPTION AND SPLITS 

**==> picture [77 x 145] intentionally omitted <==**

**==> picture [86 x 145] intentionally omitted <==**

Rougier et al. [22] achieved high accuracy using motion analysis and silhouette tracking with a single camera. However, it suffers due to inadequate lighting and privacy issues. 

## _C. Multisensor Fusion_ 

Researchers use multisensor fusion for accurate tracking of movement. For instance, Bijalwan et al. [23] used an IMU and a Kinect sensor by combining signals from accelerometers, gyroscopes, and magnetometers. 

## _D. Deep Learning Approaches_ 

Recent advancements in deep-learning and machinelearning techniques have drawn the interest of researchers due to the capability to handle time-based data and intricate movement patterns [24], [25]. Even greater results are obtained by models that examine activity sequences, such as recurrent neural networks (RNNs) and long short-term memory (LSTM) networks [26], [27]. 

## III. METHODOLOGY 

The methodology is divided into five sections, which include datasets and subject descriptions, preprocessing of data, deep learning model descriptions, discussions of the proposed model framework, and evaluations and stability of results. Fig. 3 shows the detailed methodology of our work. 

## _A. Datasets and Subject Descriptions: SisFall Dataset_ 

In this research, the public dataset SisFall is used for experimental purposes [1]. This dataset is created to understand the entire fall detection system. It is captured using an IMU sensor embedded accelerometer and gyroscope with a sampling frequency of 200 Hz. Figs. 4 and 5 illustrate the raw signal analysis of falls corresponding to forward and backward falls, respectively, caused by tripping and slipping events. A total of 38 volunteers participated, out of whom 23 are young adults (under 30 years) and 15 are older adults (60 years and above). The dataset includes 15 distinct types of falls (such as forward, backward, and lateral falls) and 19 different activities of daily living (ADLs) such as walking, jogging, and jumping. Fig. 6 shows the distribution of the dataset and the splits for training and testing samples. Table II shows the description of the dataset in tabular form. 

TABLE III 

MODEL PARAMETER 

**==> picture [129 x 83] intentionally omitted <==**

## _B. Preprocessing of Data_ 

The dataset is initially preprocessed using min–max normalization. However, to make uniform scaling with zero mean and unit variance, the _z_ -score normalization was also computed. Equations (1) and (2) show min–max and _z_ -score normalization 

**==> picture [173 x 21] intentionally omitted <==**

**==> picture [154 x 20] intentionally omitted <==**

## _C. Proposed FIBiLS Model_ 

The architecture of the proposed model, FIBilS, is shown in Fig. 7. The proposed model uses BiLSTM to efficiently process the sequential data. It consists of two BiLSTM layers. The first BiLSTM layer, with 128 units, is configured to return sequences, ensuring that all subsequent layers can process the temporal dependencies captured. The second BiLSTM layer contains 64 units and focuses on further refining these sequential patterns. Dropout layers are strategically placed after each BiLSTM layer to improve generalization and mitigate overfitting risks. This is followed by a max-pooling layer to refine these features and reduce dimensionality. Following the BiLSTM layers, the network includes two fully connected (dense) layers. Both were activated with the ReLU function to extract high-level abstract features. Dropout layers are also included between these dense layers to ensure robustness. The data are processed in a way that allows the model to capture both short-term and long-term dependencies in the sequence. Table III provides the list of model architecture and model parameters. 

## _D. Model Optimization_ 

Deep learning models can be optimized using model pruning and quantization techniques to deploy them on edge devices. These techniques enable working in real-time applications on constrained memory and low-power devices without significantly sacrificing performance. To fuse the deep learning model on NodeMCU, it is required to compress the model and reduce its size. Pruning trims the insignificant weight of the trained model to zero. It is an iterative process and sets the weight to zero until the specified target sparsity. Essentially, removing the insignificant weight connections between layers of the trained model helps to reduce the model size and power consumption and executes quickly. Fig. 8 illustrates the model pruning process visually. However, model quantization 

Authorized licensed use limited to: Hanoi University of Science & Technology. Downloaded on April 02,2026 at 01:06:24 UTC from IEEE Xplore.  Restrictions apply. 

IEEE SENSORS JOURNAL, VOL. 25, NO. 19, 1 OCTOBER 2025 

37128 

**==> picture [350 x 115] intentionally omitted <==**

Fig. 7. Architecture of the proposed FIBiLS model. 

**==> picture [239 x 113] intentionally omitted <==**

TABLE IV 

SPECIFICATION SHEET OF PROPOSED HARDWARE SETUP 

**==> picture [191 x 73] intentionally omitted <==**

Fig. 8. Process of model pruning. 

## _E. Hardware Setup_ 

**==> picture [201 x 85] intentionally omitted <==**

Fig. 9. Process of model quantization. 

**==> picture [201 x 114] intentionally omitted <==**

Fig. 10. Hardware circuit. 

involves representing weights with fewer bits, typically 8 bits or fewer, instead of the standard 32 bits used in most deep learning frameworks as shown in Fig. 9. Equation (3) shows the process of conversion of the float value to int8 

**==> picture [220 x 75] intentionally omitted <==**

To provide real-time monitoring, the proposed fall detection system will combine wearable and ambient-based technology along with the MPU6050 sensor, ESP32 microcontroller, IMU, and force sensors. Real-time data collection will improve the system’s capacity to identify falls early. Fig. 10 shows the proposed hardware setup for the fall detection. This prototype uses a force sensor, battery, MPU6050 IMU sensor, buzzer, and microcontroller (NodeMCU (ESP8266) board), over which the compressed FIBiLS model has been fused to validate the results for the generation of fall detection alarms. The deep learning code was developed in Python simulations using Google Colab, which provides GPU facilities for parallel computing. The computer system was used based on _Microsoft Windows 11 with an Intel Core i7 processor and CPU clocked at 3.40 GHz, 64 GB of RAM, and a chipset of 2600._ Fig. 10 shows the physical design of the proposed hardware. Table IV provides the specification of the proposed hardware. The configuration and integration of these components are as wiring and connection of MPU6050 sensors: VCC to 3.3V on ESP32, GND to GND on ESP32, SCL to GPIO 22 on ESP32, SDA to GPIO 21 on ESP32, and force sensors as one terminal of each force sensor to GND other terminals to GPIO 36 and GPIO 39 on ESP32.Ensure secure connections and proper placement of sensors on the subject for accurate data capture. 

## _F. Proposed Algorithm and Evaluation Matrix_ 

Algorithm 1 shows the various steps of the proposed FIBiLST model along with various performance matrices. To evaluate how well our model works, we use several performance metrics (4)–(6). These metrics compare the actual outcomes ( _y_ ) with the predicted outcomes ( _[y]_ ) from our experiments. 

Authorized licensed use limited to: Hanoi University of Science & Technology. Downloaded on April 02,2026 at 01:06:24 UTC from IEEE Xplore.  Restrictions apply. 

GAUD et al.: FIBiLS: FALL DETECTION OF HEALTHY ELDERLY USING IMU SENSOR AND BiLSTM MODEL 

37129 

**Algorithm 1** BiLSTM Model for Fall Data Classification (FIBiLS) 

**Require:** Time-series data _aX , aY , aZ , gX , gY , gZ_ its labels _Y_ , training parameters (epochs, optimizer, batch size, etc.) **Ensure:** Final classification results and model evaluation metrics. **Preprocessing:** 

Normalize the input data _X_ to obtain _Xscaled_ 

**==> picture [181 x 71] intentionally omitted <==**

**BiLSTM Model Training:** Initialize a BiLSTM model: 

BiLSTM = Sequential(Bidirectional LSTM, Dense, Dropout layers) 

BiLSTM2 = BiLSTM _(_ Layer1 _)_ → BiLSTM _(_ Layer2 _)_ 

**==> picture [100 x 30] intentionally omitted <==**

−→ ←− _ht_ = LSTM _(_[−−→] _ht_ −1 _,_[−→] _xt )_ and _ht_ = LSTM _(_[←−−] _ht_ +1 _,_[←−] _xt )_ Compile the BiLSTM model using the Adam optimizer and categorical cross-entropy loss BiLSTM.fit( _Xtrain, Ytrain,_ validation data, epochs, batch size) **Evaluation:** 

Generate confusion matrix and calculate performance metrics (e.g., sensitivity, specificity) 

**==> picture [98 x 9] intentionally omitted <==**

**==> picture [170 x 111] intentionally omitted <==**

1) _Mean Squared Error (mse):_ 

**==> picture [180 x 27] intentionally omitted <==**

## 2) _Root-Mean-Squared Error (RMSE):_ 

**==> picture [190 x 30] intentionally omitted <==**

3) _Mean Absolute Error (MAE):_ 

**==> picture [180 x 25] intentionally omitted <==**

IV. RESULT DISCUSSION 

In this research, a computationally low-power and compressed fall detection system is developed. The experiment 

**==> picture [241 x 156] intentionally omitted <==**

Fig. 11. Accuracy versus loss curve before compression. 

**==> picture [243 x 157] intentionally omitted <==**

Fig. 12. Accuracy versus loss curve before compression. 

setup uses ESP32 microcontrollers, MPU6050 IMU sensors, and force sensors, focusing on accurate and timely fall detection. Various deep-learning algorithms were employed to process real-time sensor data, evaluated through critical performance metrics. The SisFall data are divided into a 80%, 10%, and 10% split of training, validation, and testing, and multiple models are tested, especially the 1-D CNN and BiLSTM model. The table demonstrates the performance over fall data, and the table provides the ablation study of results along with a comparison with state-of-the-art work. The results are also compared based on error matrix like mse and MAE. 

Table V shows the performance of various deep-learning models over the SisFall dataset. The results demonstrate the superior performance of our proposed model, FIBiLS, over other models. Table V presents the comparison with other benchmark mark datasets, with their inference time. Our proposed model has shown great accuracy with a small memory footprint compared to others, having high inference time. The reduced model size of our model was 60 kb compared to other models like CNN and LSTM take more than 1.5 GB of flash memory, which makes them impractical to run in real time on edge devices. Fig 11 shows the accuracy and loss % of the proposed FIBiLS for SisFall data without compression. However, Fig. 12 shows the accuracy loss % of the proposed FIBiLS for SisFall data after compressing the model. 

Authorized licensed use limited to: Hanoi University of Science & Technology. Downloaded on April 02,2026 at 01:06:24 UTC from IEEE Xplore.  Restrictions apply. 

IEEE SENSORS JOURNAL, VOL. 25, NO. 19, 1 OCTOBER 2025 

37130 

TABLE V 

RESULTS TABLE FOR DIFFERENT MODELS ON SISFALL DATASET 

**==> picture [504 x 52] intentionally omitted <==**

## TABLE VI 

COMPARATIVE RESULTS OF DIFFERENT MODELS 

**==> picture [504 x 41] intentionally omitted <==**

## V. CONCLUSION AND CHALLENGES WITH FUTURE DIRECTIONS 

In this research, a fall detection system is designed based on 1-D CNN and a BiLSTM-based deep-learning model. This research utilized the SisFall dataset to design a fall detection system to assess the capabilities of the elderly. This research highlights the integration of wearable sensors, including accelerometers, gyroscopes, and force sensors, with advanced hardware components like the MPU6050 sensor and ESP32 microcontroller to collect and process motion data accurately. The proposed deep learning models, FIBiLS model, have shown the significant performance of detecting falls. However, earlier models fail to capture the bidirectional association of data. Hence, this paper proposed a FIBiLS model for fall detection. The proposed FIBiLS model has achieved a 98.78% fall detection rate on the SisFall dataset. To demonstrate the model’s stability and fairness in terms of generalization capability, the model performance is evaluated multiple times. The model is compressed using pruning and quantization and fused on the NodeMCU board for real-time fall detection, and has also shown superior performance in terms of accuracy and inference time. 

The major challenge with this research is user acceptance, influenced by comfort, style, and usability, which remains a barrier, especially for wearable devices. Privacy concerns are significant, particularly for camera-based and ambient systems, requiring strict adherence to privacy regulations. Future efforts should focus on hybrid solutions combining wearable and ambient sensors, leveraging big data and adaptive learning to improve performance. Collaboration across disciplines can drive innovation, aiming for reliable systems that safeguard vulnerable populations. 

## ACKNOWLEDGMENT 

The fall validation experiment was conducted at the IoT and Human Ergonomic, Assistive, and Haptic Laboratory (HEAHL) of MANIT Bhopal, for which the authors are grateful. The authors also extend their thanks to the volunteer participants and the creator of the dataset. 

## REFERENCES 

- [1] A. Sucerquia, J. López, and J. Vargas-Bonilla, “SisFall: A fall and movement dataset,” _Sensors_ , vol. 17, no. 1, p. 198, Jan. 2017. 

- [2] S. Kumar, P. Yadav, and V. B. Semwal, “A comprehensive analysis of lower extremity based gait cycle disorders and muscle analysis,” in _Proc. Int. Conf. Mach. Learn. Image Process. Netw. Secur. Data Sci._ , Cham, Switzerland: Springer, Dec. 2022, pp. 325–336. 

- [3] S. Kiran, Q. Riaz, M. Hussain, M. Zeeshan, and B. Krüger, “Unveiling fall origins: Leveraging wearable sensors to detect pre-impact fall causes,” _IEEE Sensors J._ , vol. 24, no. 15, pp. 24086–24095, Aug. 2024. 

- [4] S. Usmani, A. Saboor, M. Haris, M. A. Khan, and H. Park, “Latest research trends in fall detection and prevention using machine learning: A systematic review,” _Sensors_ , vol. 21, no. 15, p. 5134, Jul. 2021. 

- [5] V. B. Semwal, A. Kumar, P. Nargesh, and V. Soni, “Tracking of fall detection using IMU sensor: An IoHT application,” in _Proc. Mach. Learn._ , 2023, pp. 815–826. 

- [6] R. Jain and V. B. Semwal, “A novel feature extraction method for preimpact fall detection system using deep learning and wearable sensors,” _IEEE Sensors J._ , vol. 22, no. 23, pp. 22943–22951, Dec. 2022. 

- [7] T.-H. Chi, K.-C. Liu, C.-Y. Hsieh, Y. Tsao, and C.-T. Chan, “Prefallkd: Pre-impact fall detection via CNN-vit knowledge distillation,” in _IEEE Int. Conf. Acoust., Speech Signal Process., Proc._ , vol. 2023, Jun. 2023, pp. 1–5. 

- [8] S. K. Challa, A. Kumar, V. B. Semwal, and N. Dua, “An optimized deep learning model for human activity recognition using inertial measurement units,” _Expert Syst._ , vol. 40, no. 10, p. 13457, Dec. 2023. 

- [9] N. Gaud, M. Rathore, and U. Suman, “Hybrid deep learning-based human activity recognition (HAR) using wearable sensors: An edge computing approach,” in _Proc. Int. Conf. Data Analytics Manage._ , 2024, pp. 399–410. 

- [10] V. B. Semwal, C. Kumar, P. K. Mishra, and G. C. Nandi, “Design of vector field for different subphases of gait and regeneration of gait pattern,” _IEEE Trans. Autom. Sci. Eng._ , vol. 15, no. 1, pp. 104–110, Jan. 2018. 

- [11] V. B. Semwal, N. Gaud, P. Lalwani, V. Bijalwan, and A. K. Alok, “Pattern identification of different human joints for different human walking styles using inertial measurement unit (IMU) sensor,” _Artif. Intell. Rev._ , vol. 55, no. 2, pp. 1149–1169, Feb. 2022. 

- [12] A. Özdemir and B. Barshan, “Detecting falls with wearable sensors using machine learning techniques,” _Sensors_ , vol. 14, no. 6, pp. 10691–10708, Jun. 2014. 

- [13] V. Soni, H. Yadav, S. Bijrothiya, and V. B. Semwal, “CABMNet: An adaptive two-stage deep learning network for optimized spatial and temporal analysis in fall detection,” _Biomed. Signal Process. Control_ , vol. 96, Oct. 2024, Art. no. 106506. 

- [14] N. Kumari, A. Yadagani, B. Behera, V. B. Semwal, and S. Mohanty, “Human motion activity recognition and pattern analysis using compressed deep neural networks,” _Comput. Methods Biomechanics Biomed. Eng., Imag. Visualizat._ , vol. 12, no. 1, Dec. 2024, Art. no. 2331052. 

- [15] N. Gaud, M. Rathore, and U. Suman, “Human gait analysis and activity recognition: A review,” in _Proc. IEEE Guwahati Subsection Conf. (GCON)_ , Jun. 2023, pp. 1–6. 

- [16] D. L. Cong, B. N. Quang, D. T. Minh, D. T. Cao, and M. N. Ngoc, “Continuous wearable-based fall detection using tiny machine learning,” in _Proc. 9th Int. Conf. Applying New Technol. Green Buildings (ATiGB)_ , Aug. 2024, pp. 339–344. 

Authorized licensed use limited to: Hanoi University of Science & Technology. Downloaded on April 02,2026 at 01:06:24 UTC from IEEE Xplore.  Restrictions apply. 

GAUD et al.: FIBiLS: FALL DETECTION OF HEALTHY ELDERLY USING IMU SENSOR AND BiLSTM MODEL 

37131 

- [17] N. Gaud, M. Rathore, and U. Suman, “MHCNLS-HAR: Multiheaded CNN-LSTM-based human activity recognition leveraging a novel wearable edge device for elderly health care,” _IEEE Sensors J._ , vol. 24, no. 21, pp. 35394–35405, Nov. 2024. 

- [18] S. K. Challa, A. Kumar, V. B. Semwal, and N. Dua, “An optimizedLSTM and RGB-D sensor-based human gait trajectory generator for bipedal robot walking,” _IEEE Sensors J._ , vol. 22, no. 24, pp. 24352–24363, Dec. 2022. 

- [19] P. Tokas, V. B. Semwal, and S. Jain, “A lightweight and explainable hybrid deep learning model for wearable sensor-based human activity recognition,” _IEEE Sensors J._ , vol. 25, no. 12, pp. 22618–22628, Jun. 2025. 

- [20] P. Tokas, V. B. Semwal, and S. Jain, “A smartphone-based human activities recognition using novel multi-stream movelets on fusion of accelerometer and gyroscope data and classification using different distance metrics,” _Multimedia Tools Appl._ , vol. 84, no. 25, pp. 30259–30280, Oct. 2024. 

- [21] Y. Dong et al., “Ambient floor vibration sensing advances the accessibility of functional gait assessments for children with muscular dystrophies,” _Sci. Rep._ , vol. 14, no. 1, May 2024. [Online]. Available: https://www.nature.com/articles/s41598-024-60034-5 

- [22] C. Rougier, J. Meunier, A. St-Arnaud, and J. Rousseau, “Robust video surveillance for fall detection based on human shape deformation,” _IEEE Trans. Circuits Syst. Video Technol._ , vol. 21, no. 5, pp. 611–622, May 2011. 

- [23] V. Bijalwan, V. B. Semwal, and T. K. Mandal, “Fusion of multi-sensorbased biomechanical gait analysis using vision and wearable sensor,” _IEEE Sensors J._ , vol. 21, no. 13, pp. 14213–14220, Jul. 2021. 

- [24] S. Campanella, A. Alnasef, L. Falaschetti, A. Belli, P. Pierleoni, and L. Palma, “A novel embedded deep learning wearable sensor for fall detection,” _IEEE Sensors J._ , vol. 24, no. 9, pp. 15219–15229, May 2024. 

- [25] V. Soni, G. Yadav, and V. B. Semwal, “Elderly fall detection using attention based dilated CNN and dilated BiLSTM,” in _Proc. Int. Conf. Autom. Comput. (AUTOCOM)_ , Mar. 2024, pp. 575–579. 

- [26] M. K. Sain, J. Singha, S. Saini, and V. B. Semwal, “Human action recognition using ConvBiLSTM-GRU in indoor environment,” in _Proc. IEEE Global Conf. Artif. Intell. Internet Things (GCAIoT)_ , Dec. 2023, pp. 179–186. 

- [27] V. B. Semwal et al., “Development of the LSTM model and universal polynomial equation for all the sub-phases of human gait,” _IEEE Sensors J._ , vol. 23, no. 14, pp. 15892–15900, Jul. 2023. 

**Neha Gaud** (Member, IEEE) received the M.Sc. degree from the School of Computer Science, Devi Ahilya Vishwavidyalaya, Indore, India, and the M.Phil. degree in computer science from the Institute of Computer Science, Vikram University, Ujjain, India. She is currently pursuing the Ph.D. degree in computer science with the School of Computer Science and Information Technology, Devi Ahilya Vishwavidyalaya. She has more than 7 years of Teaching Experience with the Government College of Agar. She has published more than ten publications in various SCI, Scopus Journal, and refereed conferences. Her research interests include human–robot interaction, the IoT, and wearable sensor-based health monitoring systems, machine learning, and AI. 

**Maya Rathore** (Member, IEEE) received the master’s degree in computer applications from Rajiv Gandhi Technical University, Bhopal, India, and the Ph.D. degree in computer science from Devi Ahilya University, Indore, India. 

Presently, she is working as a Professor with the CSE Department, Chameli Devi Group of Institutions, Indore. She is having more than 18 years of academic experience. She has contributed 24 research publications in various national and international conferences and journals. She has co-authored a book on OOAD and published two book chapters (Springer). Her areas of research are software engineering, service-oriented computing, distributed computing, and cloud computing. 

**Ugrasen Suman** received the master’s degree in computer applications from Rani Durgawati University Jabalpur, Jabalpur, India, and the Ph.D. degree in computer science from Devi Ahilya University, Indore, India. 

He was the Dean of Engineering Sciences with Devi Ahilya University. Presently, he is working as a Professor with the School of Computer Science and Information Technology. He has more than 22 years of experience in teaching and research. Presently, he is the Chairman Central BoS for designing and implementing the B.Sc. (computer maintenance) syllabus as per NEP-2020 at the state level. 

Dr. Suman was a member of BoS, DRC, CET, Proctorial Board, AntiRagging, UFM, Flying Squad, in DAVV, and a member of BoS and RDC in various other Universities. He has been a TPC member/ an editorial member/ and a reviewer in various conferences and journals. He is a member of the Departmental IQAC, Planning, Assessment and Research Committee, Examination, Admission, and Anti-ragging. He is a member of IEEE-CS, a Life Member of CSI, and a Senior Member of IACSIT and IAENG. He has been the Chairman BoS Computer Science and IT (2019–2023). He is a reviewer in IEEE TRANSACTIONS ON SOFTWARE ENGINEERING and the _Journal of Software: Evolution and Process_ (Wiley). He has chaired various technical sessions and delivered several expert lectures. Also, he has served as a subject expert in various selection committees in IITs, public service commissions, universities, and colleges. 

**Vijay Bhaskar Semwal** (Senior Member, IEEE) received the Ph.D. degree from IIIT Allahabad, Allahabad, India, in 2017. 

**==> picture [73 x 91] intentionally omitted <==**

He is an Assistant Professor (Grade-I) with CSE, MANIT Bhopal, Bhopal, India. His research interests include machine learning, human activity recognition (HAR), bipedal locomotion, and push recovery. 

Authorized licensed use limited to: Hanoi University of Science & Technology. Downloaded on April 02,2026 at 01:06:24 UTC from IEEE Xplore.  Restrictions apply. 

