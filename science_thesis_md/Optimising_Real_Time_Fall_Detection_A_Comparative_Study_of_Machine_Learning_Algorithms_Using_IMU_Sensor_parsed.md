### Tóm tắt:
Bài báo nghiên cứu giải pháp tối ưu hóa hệ thống phát hiện té ngã theo thời gian thực sử dụng cảm biến đo lường quán tính (IMU) gắn ở vùng cổ. Nghiên cứu tiến hành so sánh hiệu suất của bốn thuật toán học máy bao gồm SVM, Random Forest, CNN và mạng nơ-ron nhân tạo (ANN) trên tập dữ liệu thực nghiệm mô phỏng các tư thế ngã và hoạt động thường ngày. Kết quả cho thấy mô hình ANN đạt hiệu quả cao nhất với độ chính xác 98% và thời gian phản hồi cực nhanh chỉ 0,1 giây. Hệ thống này được thiết kế tối ưu để tích hợp vào các thiết bị đeo thông minh nhằm kích hoạt kịp thời các cơ chế bảo vệ như áo phao túi khí cho người cao tuổi.

### BibTeX:
```bibtex
@inproceedings{aqillah2025optimising,
  title={Optimising Real-Time Fall Detection: A Comparative Study of Machine Learning Algorithms Using IMU Sensor},
  author={Aqillah, Muhammad Fasha and Cahyadi, Willy Anugrah and Mukhtar, Husneni and Indriyanto, Sigit and Setiyadi, Suto},
  booktitle={2025 IEEE International Conference on Artificial Intelligence for Learning and Optimization (ICoAILO)},
  year={2025},
  publisher={IEEE}
}
```

---

## NỘI DUNG BÀI BÁO CHI TIẾT

The 2025 IEEE International Conference on Artificial Intelligence for Learning and Optimization (ICoAILO) 

# Optimising Real-Time Fall Detection: A Comparative Study of Machine Learning Algorithms Using IMU Sensor 

1[st] Muhammad Fasha Aqillah 2[nd] Willy Anugrah Cahyadi 3[rd] Husneni Mukhtar _School of Electrical Engineering School of Electrical Engineering School of Electrical Engineering Telkom University Telkom University Telkom University_ Bandung, Indonesia Bandung, Indonesia Bandung, Indonesia mfashaa@student.telkomuniversity.ac.id waczze@telkomuniversity.ac.id husnenimukhtar@telkomuniversity.ac.id 

4[th] Sigit Indriyanto _School of Electrical Engineering Telkom University)_ Bandung, Indonesia sigitindriyanto@student.telkomuniversity.ac.id 

5[th] Suto Setiyadi _School of Electrical Engineering Telkom University_ Bandung, Indonesia sutosetiyadisod@telkomuniversity.ac.id 

_**Abstract**_ **—Falls can happen to anyone and require rapid detection to minimise injury risks such as fractures, reduced mobility, and increased dependency. This study proposes a real-time fall detection algorithm using an IMU sensor to capture body movement data (acceleration, angular velocity, and orientation). It compares four machine learning models, Support Vector Machine (SVM), Random Forest (RF), Convolutional Neural Network (CNN), and Artificial Neural Network (ANN) to identify the optimal solution. Data were collected through simulated fall and non-fall activities, including walking, standing, and directional falls, synchronised with IMU readings at 100Hz. ANN achieved the best performance (98% accuracy, 0.1s latency), followed by CNN (97%), RF (96%), and SVM (90%). Demonstrating its suitability for immediate fall recognition, the system is designed to trigger a protective response (e.g., airbag activation) upon detecting a fall. These results highlight the potential of ANN-based algorithms for reliable and low-latency fall detection in wearable devices.** 

_**Index Terms**_ **—IMU sensor, fall detection, Machine Learning, ANN, airbag vest.** 

## I. INTRODUCTION 

Falls constitute a significant public health concern and are among the leading causes of disability, particularly in older adults. The definition of a fall is an unintentional descent to the ground or a lower level that is not precipitated by a major intrinsic event, such as a stroke or an overwhelming environmental hazard [1]. Numerous studies [2] have established a significant association between falls and increased rates of morbidity, mortality, and functional impairment. While falls can occur across various age groups—including children and athletes—their frequency and impact are notably higher in older people. In this population, comorbidities significantly contribute to a heightened fall risk and a greater vulnerability to fall-related injuries [3] [4]. Falls are a leading cause of injury among the in the elderly, often resulting in fractures or long-term mobility impairment. Rapid detection of falls is critical to minimise harm. Still, existing wearable systems face challenges in balancing accuracy and realtime performance [5] [6] [7]. Technological advancements 

offer new opportunities to address these challenges, providing additional protection for older people. This innovation was developed using an Inertial Measurement Unit (IMU) sensor and artificial intelligence (AI) in machine learning, integrated with a wearable device. The IMU sensor detects the user’s acceleration , angular velocity, and agility. The system will then identify the user’s movement patterns and indicate the risk of falling [8] [9]. Although IMU sensors have been widely used to detect falls [10] [11] [12] [13], most studies focus on single-algorithm approaches [14] [15]. A comprehensive comparison of multiple machine learning models [16] for classifying IMU data—especially under time constraints—is still lacking. This research used an IMU sensor installed near the user’s neck, recording acceleration, angular velocity, and angle orientation data on three axes (X, Y, Z). This data is used as input for the classification process using four machine learning algorithms compared in this study: Support Vector Machine (SVM), Random Forest (RF), Convolutional Neural Network (CNN), and Artificial Neural Network (ANN) [17] [18]. Each algorithm is evaluated based on its ability to. Distinguishing between normal movement and falling patterns in older people is crucial. We optimise for accuracy and latency, identifying the optimal model for both accuracy and the response time. The output can trigger protective mechanisms, demonstrating potential for integration into wearable devices. 

## II. SYSTEM ARCHITECTURE 

A fall is when a person or object loses balance and moves downward. Humans can fall in various ways, such as tripping, slipping, sliding, or suddenly losing consciousness. For the elderly, falls are one of the leading causes of serious injury. Various approaches have been developed to reduce the impact of falls, such as using Inertial Measurement Unit (IMU) sensors and artificial intelligence (AI) algorithms, which have shown great potential in detecting body movement patterns that lead to falls. 

13 

979-8-3315-6928-0/25/$31.00 ©2025 IEEE 

Authorized licensed use limited to: Hanoi University of Science & Technology. Downloaded on April 02,2026 at 01:02:46 UTC from IEEE Xplore.  Restrictions apply. 

The 2025 IEEE International Conference on Artificial Intelligence for Learning and Optimization (ICoAILO) 

## _A. Sensor Configuration and Data Acquisition_ 

This study uses an IMU sensor in a system designed to detect and monitor user movements. Data obtained from IMU sensors includes acceleration, angular velocity, and body orientation angle. The sensor is installed on the posterior part of the C7 vertebra, which is generally recommended for fall detection studies due to its proximity to the body’s center of mass and its ability to capture changes in the orientation of the upper body effectively. This location minimizes the influence of limb movements and provides a stable point for capturing the overall dynamics of the body. 

The sensor is mounted on the posterior part of the C7 vertebra, which is generally recommended for fall detection studies due to its proximity to the body’s center of mass and ability to capture changes in upper body orientation effectively. This location minimizes the influence of limb movements and provides a stable point for capturing overall body dynamics [19], [20]. 

This system uses an IMU sensor from WitMotion, specifically the WT61PCTTL model, whose technical specifications can be seen in Table I. Some studies use IMU sensors placed on the C7 vertebra, so in this study, the IMU sensor is placed on the C7 vertebra to reconstruct real-time spinal morphometry, reinforcing the validity of sensor placement on the upper spine for motion analysis applications. The sensor streams 9-axis data (3-axis accelerometer, 3-axis gyroscope, and 3-axis orientation) to the preprocessing module via USB, operating at a sampling frequency of 100 Hz. 

Several components support this study’s data collection process and actual system implementation. Figure 2 shows the system model diagram of the airbag system vest used. 

**==> picture [225 x 110] intentionally omitted <==**

Fig. 2. System model diagram. 

The processing stage involves a microcontroller (Arduino Uno) running a pre-trained machine learning model. This module analyses incoming IMU data to classify the user’s activity and detect potential real-time fall events. 

The processing stage involves a microcontroller (Arduino Uno) running a pre-trained machine learning model. This module analyses incoming IMU data to classify the user’s activity and detect potential real-time fall events. 

Once a fall is detected at the output stage, the system triggers a high-torque DS3235SG servo motor to activate the airbag deployment mechanism. The servo releases a CO2 canister that rapidly inflates the vest, protecting the user. 

## TABLE I. SPESCIFICATION OF IMU SENSOR (WT61PCTTL) 

|ABLE I.<br>SPESCIFICATIO|N OFIMU SENSOR(WT61PCTT|
|---|---|
|**Parameter**|**Specification**|
|Sensor Type|9-axis IMU (Accelerometer,<br>Gyroscope,Magnetometer)|
|Accelerometer Range|_±_16g|
|Gyroscope Range|_±_2000~~_◦_~~/s|
|Magnetometer Range|_±_4900_µ_T|
|SamplingFrequency|0.2–200 Hz(set to 100 Hz)|
|Communication Interface|TTL(UART),USB|
|Power Supply|DC 3.3–5 V|



Several components support this study’s data collection process and actual system implementation. Figure 1 shows the design of the airbag system vest used. On the back of the vest, precisely near the user’s neck, a WitMotion WT61PCTTL sensor is installed. This position was chosen to obtain optimal upper body orientation data, as changes in position in that area are often an early indicator of a fall state. 

**==> picture [177 x 126] intentionally omitted <==**

Fig. 1. Placement of the WitMotion WT61PCTTL IMU sensor on the airbag vest. 

## _B. Signal Processing Pipeline_ 

_1) Training Process:_ The training process involves preparing and developing a machine learning model for fall detection. It starts with collecting IMU data from simulated activities, followed by data preprocessing such as filtering, normalization, and segmentation. Machine learning algorithms, including SVM, RF, CNN, and ANN, are trained and evaluated to determine the most suitable model for classification. The selected model is then saved for deployment in the system. This entire workflow can be seen in Figure 3. 

**==> picture [229 x 67] intentionally omitted <==**

Fig. 3. Block diagram of machine learning training process for fall detection. 

_2) Inference Process:_ The inference process refers to the system’s real-time operation using the pre-trained model. The microcontroller running the trained ANN model continuously collects and analyses live IMU data. The system performs classification to detect potential falls and, upon detection, activates the protective airbag mechanism. This process is illustrated in Figure 4. 

14 

Authorized licensed use limited to: Hanoi University of Science & Technology. Downloaded on April 02,2026 at 01:02:46 UTC from IEEE Xplore.  Restrictions apply. 

The 2025 IEEE International Conference on Artificial Intelligence for Learning and Optimization (ICoAILO) 

**==> picture [229 x 67] intentionally omitted <==**

Fig. 4. Block diagram of machine learning training process for fall detection. 

As illustrated in Figure 4, the inference pipeline begins with the WitMotion WT61PCTTL IMU sensor capturing live 9-axis data (3-axis acceleration, 3-axis gyroscope, and 3-axis orientation) and transmitting it to the microcontroller at a sampling rate of 100 Hz. The microcontroller loads the pretrained ANN model to process incoming data and classify the user’s state as “Fall” or “Not Fall.” If a fall is detected, the system immediately sends a signal to the DS3235SG servo motor, triggering the deployment of the airbag vest within milliseconds to protect the user. This real-time inference process ensures rapid response while operating within the resource constraints of embedded hardware. 

## _C. Data Collection_ 

_1) Participant Characteristics:_ Data were collected from 5 healthy adults (age 24±2 years, height 152±23 cm, weight 45±15 kg) with no history of mobility disorders for 10 days. Participants provided informed consent and were instructed to simulate falls onto a 30 cm-thick foam mat for safety. 

_2) Experimental Protocol:_ As part of the data collection protocol, each participant performed non-fall and fall activities. Non-fall activities included standing for 90 seconds and walking for another 90 seconds. These were designed to capture natural body movements, such as posture adjustments and arm swings, that must be distinguished from actual falls. The fall scenarios were divided into three types: forward falls, backwards falls, and lateral falls. Participants performed 10 forward falls to simulate tripping, 10 backwards falls to simulate loss of balance, and 10 lateral falls (5 times for each side) to cover sideways falling events. All sessions were video-recorded and time-synchronised with IMU data captured at 100 Hz. This procedure ensured a balanced dataset of fall and non-fall events for training the classification models. 

**==> picture [230 x 202] intentionally omitted <==**

Fig. 5. Illustration of the experimental timeline. 

Based on Figure 5, the data collection process is divided into standing and walking. This was chosen so that movements that occur when a person is standing or walking will not be detected as a fall when the wearable sensor is in use. This is because when a person is standing or walking, that person’s body parts will not remain still, but there will still be some additional movements that must be distinguished from the condition of falling. Activities such as standing or walking still produce variations in body movement, such as shifts in body weight or arm swinging, which, if not correctly recognised by the system, can lead to false positive fall detections. Therefore, standing and walking data are explicitly collected to train the model to identify the user’s natural movements when not in a dangerous situation. Data collection for standing and walking is conducted over 90 seconds, as 1 second yields 100 samples, resulting in 9000 data points per activity. This number is adjusted to be equivalent to the amount of data obtained from fall events, ensuring that the data distribution for model training is balanced and not biased toward one class. 

The fall data collection process is divided into four parts, but the right fall and left fall are combined into one category: ”lateral falls.” The fall scenarios performed are falling forward and backwards 10 times each, while falling to the right and left are each performed 5 times, so that when added together, there are 10 fall tests. This aims to balance the data distribution across all fall categories and optimally support the model learning process. 

## _D. Data Annotation and Validation_ 

The IMU data was recorded directly using the WitMotion software, which provided real-time visualisation and data logging of acceleration, angular velocity, and orientation at 100 Hz. Each activity, standing, walking, forward fall, backwards fall, and lateral fall, was manually labelled during the recording process based on the predefined experimental timeline. This ensured that data segments corresponded accurately to the intended activities. 

A subset of the labelled dataset was rechecked for validation to confirm consistency and correctness. This involved reviewing the activity logs and sensor plots in the WitMotion software to verify that each label matched the characteristic patterns of the respective movements. Any discrepancies identified during this process were corrected before using the dataset for model training. 

## _E. Machine Learning Integration_ 

Several studies have used IMU data to apply machine learning (ML) algorithms for fall detection. Koo et al. (2021) [21] investigated multiple classifiers, including Support Vector Machine (SVM), Random Forest (RF), and Artificial Neural Network (ANN), highlighting their applicability to post-fall detection across datasets [14]. O[¨ ] zdemir and Barshan (2014) also demonstrated the potential of ML models, such as ANN and CNN, in processing wearable IMU sensor data for robust fall detection systems [22]. 

Four machine learning models/algorithms, such as Support Vector Machine (SVM), Random Forest (RF), Artificial Neural Network (ANN), and Convolutional Neural Network (CNN), are used to recognise movement patterns. These 

15 

Authorized licensed use limited to: Hanoi University of Science & Technology. Downloaded on April 02,2026 at 01:02:46 UTC from IEEE Xplore.  Restrictions apply. 

The 2025 IEEE International Conference on Artificial Intelligence for Learning and Optimization (ICoAILO) 

models are pre-trained using data representing various user activity conditions, including walking, standing still, and falling in some directions. 

_1) Support Vector Machine (SVM):_ The SVM model was trained using the RBF (Radial Basis Function) kernel with parameters _C_ = 1 _._ 0 and gamma = ‘scale’. This model was chosen because it works well for small-to-medium-sized data and is suitable for data with non-linear margins. After the training process, the model was used to predict test data, and the results were evaluated using a confusion matrix and classification report. 

_2) Random Forest:_ The Random Forest model was trained using 50 estimators, with a maximum tree depth limited to 8. Other parameters such as min samples split = 4, min samples leaf = 4, and max features = 3 were also used to reduce overfitting. 

_3) Convolutional Neural Network (CNN):_ CNN recognises patterns from IMU data that are converted into a sequential form. The input is modified using reshape() to have dimensions [samples, time steps, features], and the CNN model consists of one Conv1D layer with 32 filters and kernel size 3, followed by MaxPooling1D, then several dense layers. 

_4) Artificial Neural Network (ANN):_ ANN was built using six hidden layers, each with 32 neurons and ReLU activation, and one output layer using softmax activation. This model was trained using the Adam optimiser and sparse categorical crossentropy loss function, with training parameters similar to those of the CNN. 

## III. RESULTS AND DISCUSSION 

This section explains the results of the data processing using machine learning algorithms, including classification outcomes, analysis, and discussion. Figure 3 illustrates the signal pre-processing described in subsection “B. Signal Processing Pipeline.” This stage includes filtering to remove sensor noise, normalisation to standardise the value range across axes, and segmentation to divide the continuous data into manageable time windows for analysis. 

## _A. Time-Series Visualization of IMU Data_ 

Examples of the pre-processed signals for each activity are shown in Figures 6, 7, and 8, displaying acceleration (Acc), angular velocity (Gyro), and orientation angles (Angle) across all three axes (X, Y, Z). 

**==> picture [238 x 124] intentionally omitted <==**

Fig. 6. Time series IMU data of walking activity: (60 samples) acceleration, angular velocity, and orientation. 

_1) Sensor Data for Walking Activity:_ This figure shows the variations in IMU signals during walking. Periodic fluctuations are visible, particularly in Acc Z and Gyro Z, corresponding to the rhythmic motion of the body while taking steps. These patterns are crucial for distinguishing walking from fall events, as they exhibit consistent amplitude and frequency, unlike abrupt fall movements. 

**==> picture [238 x 124] intentionally omitted <==**

Fig. 7. Time series IMU data of standing activity: (60 samples) acceleration, angular velocity, and orientation. 

_2) Sensor Data for Standing Activity:_ The IMU signals across all axes remain relatively stable during standing, with minimal fluctuations. Acc and Gyro values are close to zero, indicating no significant movement. The model must recognise this static pattern to avoid false positives in fall detection. 

_3) Sensor Data for Forward Fall:_ This figure illustrates a forward fall event. Sudden and sharp changes are observed in all axes, especially in Acc Z and Gyro Y, reflecting the body’s rapid forward motion. The orientation angles ( _θx_ , _θy_ , _θz_ ) also shift significantly, providing additional temporal features for accurate classification. These rapid variations in acceleration and angular velocity indicate a significant change in the body’s position, which is crucial for differentiating a fall from other activities like walking or standing. The data from the IMU sensor allows the system to detect the fall trajectory and distinguish between various types of falls based on the unique patterns observed in the sensor readings 

**==> picture [238 x 124] intentionally omitted <==**

Fig. 8. Time series IMU data of forward fall: (60 samples) acceleration, angular velocity, and orientation. 

_4) Sensor Data for Backwards Fall:_ In backwards falls, distinct patterns emerge with opposite directional changes. Gyro X and Acc Y exhibit pronounced peaks due to the body’s backwards rotation. These features help the model differentiate between forward and backwards falls. 

16 

Authorized licensed use limited to: Hanoi University of Science & Technology. Downloaded on April 02,2026 at 01:02:46 UTC from IEEE Xplore.  Restrictions apply. 

The 2025 IEEE International Conference on Artificial Intelligence for Learning and Optimization (ICoAILO) 

**==> picture [236 x 123] intentionally omitted <==**

**==> picture [247 x 120] intentionally omitted <==**

Fig. 11. Classification result of all models. 

Fig. 9. Time series IMU data of backward fall: (60 samples) acceleration, angular velocity, and orientation. 

_5) Sensor Data for Side Fall:_ Side falls, or lateral falls, occur when a person falls to the left or right. These falls are often subtle, making them harder to detect. However, IMU sensors capture distinct patterns in acceleration (Acc X/Y/Z) and gyroscope (Gyro X/Y/Z) data. During a side fall, the X and Y axes show significant changes as the body shifts left or right, while Gyro Z detects the horizontal rotation. By analyzing these variations, the system can accurately differentiate lateral falls from other activities and activate protective responses, such as airbag deployment. 

**==> picture [238 x 125] intentionally omitted <==**

Fig. 10. Time series IMU data of side fall: (60 samples) acceleration, angular velocity, and orientation. 

## _B. Model Performance and Classification Results with Confusion Matrix_ 

All models were evaluated using 5-fold cross-validation. The Artificial Neural Network (ANN) achieved the highest accuracy (98%) and F1 score (0.97), demonstrating superior performance in recognising complex movement patterns from IMU data. CNN closely followed with an accuracy of 97%, demonstrating strong capabilities in processing sequential data, although it showed slight sensitivity to movements parallel to the axis (see Figure 12 and Table II). RF performed well with an accuracy of 96% and demonstrated reasonably good computational efficiency (latency of 150 ms vs. 100 ms for ANN), making it more suitable for embedded systems. SVM achieved an accuracy of 90%, the lowest among the models, primarily due to frequent misclassification between walking and falling forward (Figs. 12 and 11). 

**==> picture [225 x 224] intentionally omitted <==**

Fig. 12. All model confusion matrix. 

The quantitative performance of all evaluated machine learning models is summarized in Table II. The Artificial Neural Network (ANN) achieved the highest accuracy (98%) and F1-score (0.97), demonstrating excellent capability in capturing complex temporal patterns from IMU signals. Convolutional Neural Network (CNN) followed closely with an accuracy of 97% and F1-score of 0.96, showing strong sequential data processing abilities but with slightly higher latency. Random Forest (RF) performed robustly with an accuracy of 96% and a lower latency of 120 ms, making it suitable for embedded systems where computational efficiency is critical. Support Vector Machine (SVM) recorded the lowest accuracy (90%) and F1-score (0.89), primarily due to misclassification of transitional movements like walking and forward falls. However, SVM still exhibited a relatively low latency of 170 ms, which may be advantageous for resource-constrained devices. 

TABLE II. PERFORMANCE COMPARISON OF MACHINE LEARNING MODELS FOR FALL DETECTION 

||MODELS|FORFALLDE|TECTION||
|---|---|---|---|---|
|**Model**|**Accuracy**|**Precision**|**Recall**|**F1 Score**|
|ANN<br>CNN<br>RF<br>SVM|98%<br>97%<br>96%<br>90%|97%<br>96%<br>95%<br>89%|98%<br>97%<br>96%<br>90%|0.97<br>0.96<br>0.95<br>0.89|



17 

Authorized licensed use limited to: Hanoi University of Science & Technology. Downloaded on April 02,2026 at 01:02:46 UTC from IEEE Xplore.  Restrictions apply. 

The 2025 IEEE International Conference on Artificial Intelligence for Learning and Optimization (ICoAILO) 

As shown in Fig. 12 and Fig. 11, our Artificial Neural Network (ANN) achieved the highest performance with 98% accuracy and 0.97 macro F1-score, outperforming recent models. For instance, Zhang et al. (2024) [23] reported 99.3–99.6% accuracy using a Dual Stream CNN Self Attention (DSCS) model, but our ANN matches such high performance with a much simpler architecture and 100 ms latency, making it ideal for real-time wearable systems. 

The Convolutional Neural Network (CNN) achieved 97% accuracy and 0.96 F1-score, classifying posture-based classes like Standing and Lateral Fall with high precision. However, it still misclassified dynamic fall events (13 forward falls, 14 backward falls). This aligns with findings from Liu et al. (2023) [24], where a CNN GRU ensemble, despite achieving 98% accuracy, faced similar challenges in recognizing transitional movements [25]. Our results suggest that CNN’s temporal encoding could benefit from recurrent layers to reduce such misclassifications. 

Random Forest (RF) demonstrated 96% accuracy and 0.95 F1-score, with very few misclassifications (e.g., 3 lateral falls misidentified as walking). Its ensemble structure provides resilience to noise, consistent with Casilari et al. (2022) [26], who endorse RF for its robustness in embedded fall detection systems. Combined with its 120 ms latency, RF remains a strong choice for resource-constrained platforms. 

Support Vector Machine (SVM) achieved 90% accuracy and 0.89 F1-score, but frequently misclassified Walking as Standing (214 instances) and Forward Falls (19 instances). These misclassifications highlight SVM’s limitations in capturing temporal dependencies in IMU data. Recent studies reaffirm this issue: in near-fall detection tasks, Frontiers in Digital Health (2023) [ **?** ] noted SVM underperformed compared to neural architectures like CNN and LSTM due to weaker sequential modeling capabilities. Furthermore, Kchouri et al. (2022) [26] report that classical SVM is sensitive to outliers and requires complex hyperparameter tuning, making it less reliable for real-time systems. 

Feature importance analysis revealed that angular velocity on the Z-axis (Gyro Z) and acceleration on the X-axis (Acc X) are the most significant contributors to classification performance, particularly for distinguishing between fall types. Error analysis indicates that Walking and Forward Falls are the most frequently confused classes, suggesting overlapping signal patterns during transitional phases. 

## _C. Quantitative Evaluation of Machine Learning Models_ 

The performance of four machine learning models, Artificial Neural Network (ANN), Convolutional Neural Network (CNN), Random Forest (RF), and Support Vector Machine (SVM) was evaluated using 5-fold cross-validation. As summarized in Table II, ANN achieved the highest accuracy (98%) and F1-score (0.97). CNN followed closely with an accuracy of 97%, while RF and SVM achieved 96% and 90% accuracy, respectively. 

In terms of latency, ANN performed inference in 100 ms, outperforming CNN (180 ms) and SVM (170 ms). RF exhibited the lowest latency among all models (120 ms), making it highly favorable for embedded systems where computational efficiency is critical. 

Fig. 12 and Fig. 11 present the classification reports and confusion matrix, illustrating detailed per-class performance and common misclassification patterns for each model. 

## _D. Feature Importance and Error Analysis_ 

Analysis indicated that Gyro Z (angular velocity) and Acc X (acceleration) were the most critical in distinguishing fall types, particularly in rapid rotational and translational movements. Error analysis showed frequent misclassifications between Walking and Falling Forward, particularly in SVM and CNN models. These overlaps suggest the need for enhanced temporal feature extraction to improve classification accuracy. 

## _E. Power Consumption Analysis_ 

A power consumption analysis was performed to assess the endurance of the wearable system powered by an 11.1 V 3500 mAh Li-Po battery. The system integrates a WitMotion WT61PCTTL IMU sensor, Arduino Uno microcontroller, and a DS3235SG servo motor. During monitoring mode, where only the IMU and microcontroller are active, the system consumes approximately 2.66 W with an average current draw of 0.24 A. Under these conditions, the battery can sustain continuous operation for up to 14.6 hours (875 minutes), supporting sensor data acquisition and fall detection processing without airbag deployment. 

The servo motor is activated only when a fall is detected. As such activations are infrequent in typical daily usage, the additional power required for airbag deployment contributes minimally to overall consumption. Considering occasional activations, the system’s operational time reduces slightly but remains sufficient for over 12 hours of full functionality. 

At a low battery level ( 20% capacity), the output voltage drops near the safe operational threshold ( 9.9 V). This voltage drop significantly affects the DS3235SG servo motor, which may fail to deliver the required torque for airbag deployment. In this state, the system can continue monitoring and detecting falls but is no longer reliable for triggering mechanical protection. Prompt recharging is therefore recommended to ensure complete system functionality and user safety. 

## IV. CONCLUSION 

Our systematic comparison of four machine learning algorithms for IMU-based fall detection revealed that the Artificial Neural Network (ANN) achieved the highest accuracy (98%) with low latency (0.1s), making it suitable for real-time applications. CNN and Random Forest also demonstrated strong performance (97% and 96% accuracy) with lower computational complexity, while Support Vector Machine (SVM) (90%) struggled with detecting similar movement patterns. This study provides three key contributions: (1) a comprehensive evaluation framework for fall detection algorithms, (2) empirical evidence that ANN architectures optimally balance accuracy and speed for this application. 

Our standardised testing protocol enables direct comparison with future studies. While promising, this study has limitations: data were collected from young adults simulating falls, and computational efficiency was not optimised for embedded devices. Future work should: (1) validate the 

18 

Authorized licensed use limited to: Hanoi University of Science & Technology. Downloaded on April 02,2026 at 01:02:46 UTC from IEEE Xplore.  Restrictions apply. 

The 2025 IEEE International Conference on Artificial Intelligence for Learning and Optimization (ICoAILO) 

models with elderly participants, (2) implement the system on edge hardware, and (3) explore sensor fusion with other modalities (e.g., pressure sensors). 

## ACKNOWLEDGEMENT 

This research is funded by Koneksi, Australia’s Indonesia Knowledge Partnerships Platform, which is managed by Cowater International Inc. Number: 1447/CRG/2024/42-TelU. 

## REFERENCES 

- [1] N. et al El-Bendary, “Fall detection and prevention for the elderly: A review of trends and challenges,” _International Journal on Smart Sensing and Intelligent Systems_ , vol. 6, pp. 1230–1266, 2013. 

   - [23] e. a. Z. Jinxi, “An effective deep learning framework for fall detection: model development and study design,” _Journal of medical internet research_ , vol. 26, p. e56750, 2024. 

   - [24] e. a. L. Chien-Pin, “Deep learning-based fall detection algorithm using ensemble model of coarse-fine cnn and gru networks,” _2023 IEEE International Symposium on Medical Measurements and Applications (MeMeA)_ , 2023. 

   - [25] A. I. F. Sophini and M. J. D. ubramaniam, “Wearable sensor systems for fall risk assessment: A review,” _Frontiers in digital health 4_ , p. 921506, 2022. 

   - [26] e. a. K. Mohammad, “Smart fall detection by enhanced svm with fuzzy logic membership function,” _Journal of Universal Computer Science (JUCS)_ , vol. 29, 2023. 

- [2] et. al Y. Zhong, “Mechanism-driven strategies for reducing fall risk in the elderly: A multidisciplinary review of exercise interventions,” _Healthcare_ , vol. 12, p. 2394, 2023. 

- [3] A. Xin, “Using imu to determine velocity of falling object and hence develop framework to optimize parachute size for falling uav,” in _in IRC-SET 2022: Proceedings of the 8th IRC Conference on Science, Engineering and Technology, August 2022_ . Singapore, 2023. 

- [4] J. L. E. A. O’Loughlin, “Incidence of and risk factors for falls and injurious falls among the community-dwelling elderly,” _American journal of epidemiology_ , vol. 3, pp. 342–354, 1993. 

- [5] Q. X. O. A. J. L. Xu, “The risk of falls among the aging population: a systematic review and meta-analysis,” _Frontiers in public health_ , vol. 10, p. 902599. 

- [6] E. E. A. Garc´ıa, “Towards effective detection of elderly falls with cnnlstm neural networks,” _Neurocomputing_ , vol. 500, pp. 231–240, 2022. 

- [7] X. e. a. Yan, “Wearable imu-based real-time motion warning system for construction workers’ musculoskeletal disorders prevention,” _Automation in construction_ , vol. 74, pp. 2–11, 2017. 

- [8] U. E. A. Manupibul, “Integration of force and imu sensors for developing low-cost portable gait measurement system in lower extremities,” _Scientific Reports_ , vol. 13, p. 10653, 2023. 

- [9] C. E. A. Yi, “Detecting and correcting imu movements during joint angle estimation,” _IEEE Transactions on Instrumentation and Measurement_ , vol. 71, pp. 1–14, 2022. 

- [10] L. E. A. Donisi, “Wearable sensors and artificial intelligence for physical ergonomics: A systematic review of literature,” _Diagnostics_ , vol. 12, p. 3048, 2022. 

- [11] A. E. A. Dahiya, “Efficient hand gesture recognition using artificial intelligence and imu based wearable device,” _IEEE Sensors Letters_ , 2024. 

- [12] H.-C. E. A. Lin, “Fall recognition based on an imu wearable device and fall verification through a smart speaker and the iot,” _Sensors_ , vol. 23, p. 5472, 2023. 

- [13] J. E. A. Tang, “Synthetic imu datasets and protocols can simplify fall detection experiments and optimize sensor configuration,” _IEEE transactions on neural systems and rehabilitation engineering_ , 2024. 

- [14] et. al S. Albawi S., “Understanding of a convolutional neural network,” _in Proceedings of the 2017 international conference on engineering and technology (ICET)_ , pp. 1–6, 7 2017. 

- [15] et.al T.B. Rodrigues, “Fall detection system by machine learning framework for public health,” _Procedia Computer Science_ , vol. 141, pp. 358–365, 2018. 

- [16] S. Badgujar and A. S. Pillai, “Fall detection for elderly people using machine learning,” in _2020 11th International Conference on Computing, Communication and Networking Technologies (ICCCNT)_ , 2020, pp. 1–4. 

- [17] S. R. E. et.al, “Fall detection and monitoring using machine learning: A comparative study,” _(IJACSA) International Journal of Advanced Computer Science and Applications_ , vol. 14, pp. 723–748, 2023. 

- [18] H. M. I. Istiqomah, “Development human activity recognition for the elderly using inertial sensor and statistical feature,” in _Proceeding of the 3rd International Conference on Electronics, Biomedical Engineering, and Health Informatics_ , 2023. 

- [19] et. al C. Tufisi, “Forward fall detection using inertial data and machine learning,” _Appl. Sci_ , vol. 14, p. 10552, 2024. 

- [20] J. Tan, “Study of spine morphometry based on inertial measure-ment unit,” in _2024 4th International Conference on Electrical Engineering and Control Science (IC2ECS). IEEE_ , 2024. 

- [21] e. a. K. Bummo, “The performance of post-fall detection using the cross-dataset: feature vectors, classifiers and processing conditions,” _Sensors_ , vol. 21, p. 4638, 2021. 

- [22] A. Turan and B. B. O[¨ ] zdemir, “Detecting falls with wearable sensors using machine learning techniques,” _Sensors_ , vol. 14, pp. 10 691– 10 708, 2014. 

19 

Authorized licensed use limited to: Hanoi University of Science & Technology. Downloaded on April 02,2026 at 01:02:46 UTC from IEEE Xplore.  Restrictions apply. 

