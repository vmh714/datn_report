### Tóm tắt:
Nghiên cứu này đề xuất một phương pháp phát hiện té ngã tiên tiến sử dụng kiến trúc học sâu dư thừa 1D-ResNeXt tùy chỉnh để phân tích tín hiệu chuyển động từ cảm biến IMU (gia tốc kế và con quay hồi chuyển). Hệ thống được đánh giá bằng tập dữ liệu PIF thu thập từ 12 cá nhân thực hiện các hoạt động thường ngày và các tình huống té ngã giả định. Kết quả thực nghiệm cho thấy mô hình đạt độ chính xác vượt trội lên tới 92,27% khi kết hợp cả hai loại cảm biến, vượt qua các mô hình học sâu truyền thống như CNN, LSTM và GRU. Nghiên cứu này đóng góp ý nghĩa vào việc phát triển các thiết bị đeo thông minh hỗ trợ giám sát sức khỏe và chăm sóc người cao tuổi.

### BibTeX:
```bibtex
@article{mekruksavanich2025imu,
  title={IMU-Based Human Fall Detection Using Deep Residual Networks for Advancing Health and Injury Prevention},
  author={Mekruksavanich, Sakorn and Phaphan, Wikanda and Jitpattanakul, Anuchit},
  journal={IEEE},
  year={2025},
  pages={197--198}
}
```

---

## NỘI DUNG BÀI BÁO CHI TIẾT

# IMU-Based Human Fall Detection Using Deep Residual Networks for Advancing Health and Injury Prevention 

Sakorn Mekruksavanich[1] , Wikanda Phaphan[2] and Anuchit Jitpattanakul[3] _[,][∗]_ 

> 1 _Department of Computer Engineering, School of Information and Communication Technology University of Phayao_ , Phayao, Thailand sakorn.me@up.ac.th 

> 2 _Research Group in Statistical Learning and Inference, Department of Applied Statistics Faculty of Applied Science, King Mongkut’s University of Technology North Bangkok_ , Bangkok, Thailand wikanda.p@sci.kmutnb.ac.th 

> 3 _Intelligent and Nonlinear Dynamic Innovations Research Center, Department of Mathematics Faculty of Applied Science, King Mongkut’s University of Technology North Bangkok_ , Bangkok, Thailand 

anuchit.j@sci.kmutnb.ac.th 

_**Abstract**_ **—This study introduces an advanced fall detection approach that leverages deep residual learning applied to motion signals captured from inertial measurement unit (IMU) sensors. Falls are a leading cause of injury and mortality among older adults and other vulnerable groups, particularly in settings where immediate medical assistance may be delayed. To address this critical health concern, the proposed method analyzes the temporal characteristics of tri-axial accelerometer and gyroscope data to distinguish between fall events and normal daily activities with high reliability. A customized one-dimensional ResNeXt architecture was developed to extract hierarchical motion features while overcoming common training challenges such as vanishing gradients. The system was evaluated using the PIF dataset, which comprises simulated fall and non-fall activities collected from 12 individuals of varying ages and physical conditions. The model demonstrated robust performance, achieving detection accuracies of 91.52% using accelerometer data, 83.80% using gyroscope data, and 92.27% when both sensor types were combined. These results consistently surpassed those of conventional deep learning models, including CNN, LSTM, BiLSTM, GRU, and BiGRU. The integration of multimodal sensor signals significantly enhanced recognition performance, highlighting the importance of sensor fusion for accurate fall detection. This research contributes to the development of intelligent health monitoring systems and has practical applications in wearable technologies, remote patient care, and eldercare solutions. The proposed framework supports preventive healthcare initiatives by enabling timely intervention and reducing the risk of fall-related injuries, thereby promoting safer and healthier living conditions for at-risk populations.** 

_**Keywords**_ **—Fall detection, IMU sensors, motion signals, deep residual network, smart health monitoring, urban safety technologies, elderly care systems.** 

## I. INTRODUCTION 

Falls constitute a significant public health issue, particularly affecting the elderly, and are recognized as one of the primary contributors to injury-related hospital admissions and fatalities [1]. The World Health Organization reports that approximately 684,000 deaths annually result from falls, making them the 

second most common cause of unintentional injury mortality worldwide [2]. Among older adults, the consequences of falling extend well beyond physical harm, often leading to psychological effects such as heightened fear of future falls, loss of mobility, and overall decline in quality of life [3], [4]. 

One of the most critical factors in reducing the severity of fall outcomes is minimizing the time between the occurrence of the fall and the delivery of medical assistance. Empirical studies have shown that extended periods spent on the floor following a fall significantly increase the risk of secondary complications, including dehydration, hypothermia, pressure ulcers, and pneumonia [5]. Alarmingly, about 50% of elderly individuals who remain on the ground for over an hour postfall die within six months, regardless of whether the fall caused direct physical injury [6]. 

Historically, fall detection technologies have relied on ambient sensors such as surveillance cameras, floor pressure pads, and infrared motion detectors installed in the user’s living environment [7]. While effective under supervised conditions, these systems are limited in terms of spatial coverage, often raise privacy concerns, and involve complex setup and maintenance. In contrast, wearable devices equipped with inertial measurement units (IMUs) offer several advantages. These include mobility, continuous tracking regardless of the user’s location, and enhanced privacy protection [8]–[12]. 

Initial wearable fall detection systems employed thresholdbased techniques, where a fall was identified when sensor values exceeded predefined limits [13]. Although computationally lightweight, these methods lacked adaptability to individual movement variability and frequently triggered false positives. The adoption of classical machine learning algorithms, such as support vector machines, random forests, and k-nearest neighbors (k-NN), represented a significant improvement. These methods classified fall events by extracting statistical and temporal features from IMU signals [14]. However, their 

979-8-3315-8898-4/25/$31.00 ©2025 IEEE 

Authorized licensed use limited to: Hanoi University of Science & Technology. Downloaded on April 02,2026 at 00:57:37 UTC from IEEE Xplore.  Restrictions apply. 197 

reliance on manual feature engineering imposed limitations on scalability and generalization [15]. 

The emergence of deep learning has transformed many signal interpretation tasks by enabling the automatic learning of features directly from raw sensor input [16]–[20]. Architectures such as convolutional neural networks (CNNs) [21], [22] and recurrent neural networks (RNNs) [23]–[25] have been employed in fall detection, demonstrating promising levels of accuracy [26]. Yet, as these networks become increasingly complex in their ability to learn temporal dependencies, they suffer more from the vanishing gradient problem, which hinders practical training on sequential motion data. 

To overcome this limitation, residual networks (ResNet)—first proposed by He et al. [27]—introduce shortcut connections that allow gradients to propagate through alternative computational paths during backpropagation. This design mitigates the vanishing gradient issue, leading to significant performance improvements in image classification tasks. However, its potential in analyzing time-series motion data, particularly for fall detection using IMU sensors, remains underexplored and merits further investigation. This study introduces a deep residual neural network architecture designed explicitly for detecting human falls using tri-axial signals from accelerometers and gyroscopes obtained from wearable IMU sensors. The key contributions of this work are outlined as follows: 

- We present a custom-designed 1D-ResNeXt model specifically optimized for processing temporal motion data. This architecture leverages multi-kernel convolutional modules and residual skip connections to efficiently capture both short-range and long-range temporal dependencies in human movement sequences. 

- A rigorous evaluation framework is established using the PIF dataset, which includes a wide range of simulated fall incidents and daily activities performed by 12 individuals of varying ages and physical conditions. The evaluation takes into account differences in sensor positioning, participant characteristics, and environmental conditions. 

- The proposed method is benchmarked against several state-of-the-art deep learning models, including CNN, LSTM, BiLSTM, GRU, and BiGRU. The comparative results demonstrate that our approach consistently outperforms these baselines across different sensor input configurations. 

- Experimental results underscore the effectiveness of sensor fusion, showing that combining accelerometer and gyroscope data achieves the highest classification accuracy of 92.27%, confirming the complementary nature of these sensing modalities in fall detection. 

systems and the use of deep learning models for time-series signal classification. 

## _A. Fall Detection Using Wearable Sensors_ 

Wearable technology has become increasingly popular in fall detection applications due to its compactness, userfriendliness, and capability for continuous monitoring. Among the various sensor types, accelerometers and gyroscopes are most commonly utilized, as they provide measurements of linear acceleration and angular velocity, respectively [28]. 

Beyond these standard sensors, researchers have also explored the integration of additional modalities, such as barometric pressure sensors and magnetometers, to improve detection reliability. For instance, Bianchi et al. [29] enhanced fall detection accuracy by combining accelerometer data with barometric readings, capitalizing on altitude changes during falls. Similarly, Kau et al. [30] employed a sensor fusion strategy involving accelerometers, gyroscopes, and magnetometers. Their system used a cascaded classifier, achieving an accuracy rate of 92%, which demonstrates the benefits of multi-sensor integration. 

## _B. Deep Learning Approaches in Fall Detection_ 

In recent years, deep learning techniques have emerged as powerful tools for modeling human motion patterns and detecting falls. CNNs have been widely applied to extract spatial representations from sensor signals. In contrast, RNNs, including their variants, are effective in capturing sequential dependencies over time. 

He et al. [31] introduced a fall detection model based on CNN, known as FD-CNN, which achieved improved specificity compared to traditional threshold-based algorithms. However, CNNs may lose temporal resolution due to the convolution process, particularly when applied to continuous time-series data. To address this limitation, Musci et al. [32] proposed an LSTM-based model that learns temporal dynamics by processing long-duration sequences, thereby preserving time-dependent features critical to fall detection. 

Although wearable sensor-based systems and deep learning architectures have significantly advanced the field of fall detection, challenges remain—particularly regarding model robustness, generalization across populations, and effective multi-sensor data fusion. In response to these gaps, this study introduces a novel 1D-ResNeXt architecture designed to utilize motion signals from multiple wearable sensors. This proposed model aims to improve detection accuracy and reliability by combining hierarchical feature learning with deep temporal modeling in fall detection applications. 

## II. RELATED WORKS 

## III. THE FALL DETECTION FRAMEWORK 

Over the past two decades, fall detection technologies have seen substantial advancement, transitioning from basic threshold-based methods to more advanced deep learningbased solutions. This section surveys prior research relevant to fall detection, with a particular focus on wearable sensor-based 

The fall detection system employed in this study is a sensor-driven framework that comprises four core stages: data collection, data pre-processing, data preparation, and model training and evaluation, as illustrated in Fig. 1. 

Authorized licensed use limited to: Hanoi University of Science & Technology. Downloaded on April 02,2026 at 00:57:37 UTC from IEEE Xplore.  Restrictions apply. 198 

**==> picture [439 x 158] intentionally omitted <==**

**----- Start of picture text -----**<br>
���������������� ������������������� ��������������� ����������������������������������<br>��� ��������������� ����� ��������<br>����� ���������������������� �������� ������ �������<br>����������� ����<br>���� ���������������� ���������������<br>��������� ���<br>�������������� ���<br>������������� ������������ ���� ������<br>��������� ���������������������<br>��� �����<br>��������������� ����������������� ��������������<br>��������������<br>����������<br>���� ���� �������<br>���� ������� �������<br>������������<br>�������������<br>�������<br>����������<br>���������<br>**----- End of picture text -----**<br>


Fig. 1. The fall detection framework based on smart wearable sensors used in this work. 

## _A. PIF Dataset_ 

The PIF Dataset [33] is a publicly available collection containing annotated samples of fall events and activities of daily living (ADLs) captured using a custom-designed wearable sensing device. The dataset utilizes the MPU6050 sensor, an IMU featuring 9 degrees of freedom. This includes a 3-axis accelerometer, a 3-axis gyroscope, and an integrated temperature sensor. The device operates within a voltage range of 3.3 V to 5 V DC. 

The accelerometer supports sensitivity ranges of _±_ 2g, _±_ 4g, _±_ 8g, and _±_ 16g, while the gyroscope offers angular velocity measurement capabilities of _±_ 250, _±_ 500, _±_ 1000, and _±_ 2000°/s. This configuration enables the device to record linear acceleration, rotational velocity, orientation, and body temperature. The prototype, based on the MPU-6050, was securely positioned at waist level for each participant during data collection. 

Sensor readings were acquired through a custom-built data acquisition system, and the extracted features were saved in individual csv files corresponding to each subject. The dataset comprises recordings from 12 individuals with diverse characteristics, including age, body weight, and height. Each participant was instructed to perform seven distinct ADLs and eight types of falls, with two repetitions per activity. 

Feature extraction was conducted using the tockn Arduino library. For each subject, one-minute sequences were recorded for regular activities, while 20-second segments were captured for fall events. 

## _B. Pre-processing of IMU Sensor Data_ 

Before training the deep learning models, the raw data collected from the IMU sensors undergoes several pre-processing operations to enhance signal consistency and reduce noise. These steps are crucial for enhancing input quality and ensuring the reliability of model performance. 

Initially, a low-pass Butterworth filter with a cutoff frequency of 20 Hz is applied to the raw signals. This filtering process effectively suppresses high-frequency noise while retaining relevant motion characteristics related to human activi- 

ties and fall incidents. The use of this filter is significant due to the inherent susceptibility of IMU devices to disturbances such as electromagnetic interference and mechanical vibrations. 

To standardize the range of sensor outputs, we then employed the Min-Max normalization method. This technique scales each feature into the range [0 _,_ 1] according to the equation: 

**==> picture [176 x 25] intentionally omitted <==**

where _x_ denotes the original signal value and _x[′]_ represents the normalized counterpart. Normalization ensures that each feature contributes equally to the learning process and avoids dominance by features with larger numeric scales. 

Lastly, the continuous time-series data is segmented into uniform time windows using a sliding window technique with a 50% overlap between adjacent segments. For ADLs, we adopted a window size of one second. A similar segmentation strategy is used for fall events. This temporal windowing method provides sufficient contextual information for the model to distinguish between regular movements and abrupt fall occurrences accurately. 

## _C. The Proposed 1D-ResNeXt Model_ 

In this study, we introduced a deep residual architecture named 1D-ResNeXt, designed to enhance the performance of sensor-based human activity recognition (HAR). The proposed model draws its foundational concept from ResNeXt [34]. Unlike InceptionNet, which merges multi-scale features through concatenation, our approach employs element-wise addition of feature maps generated by convolutional kernels of varying sizes. This architectural choice significantly reduces the total number of learnable parameters. As a result, the model becomes more efficient, making it particularly well-suited for low-latency applications and deployment in resourceconstrained edge computing environments. 

The proposed model incorporates three multi-kernel modules, each utilizing convolutional filters of different sizes. 

Authorized licensed use limited to: Hanoi University of Science & Technology. Downloaded on April 02,2026 at 00:57:37 UTC from IEEE Xplore.  Restrictions apply. 199 

**==> picture [151 x 170] intentionally omitted <==**

**----- Start of picture text -----**<br>
�����<br>������ ������ ������<br>������ ������ ������<br>��� ������<br>������<br>���<br>**----- End of picture text -----**<br>


Fig. 2. The multi-kernel module presented in this work. 

Specifically, each module includes three distinct kernel dimensions: 1 _×_ 1, 1 _×_ 5, and 1 _×_ 7. To minimize the overall computational burden and reduce the number of trainable parameters, 1 _×_ 1 convolutions are applied before the multiscale kernels. A detailed illustration of this module structure is provided in Fig. 2. 

The 1D-ResNeXt architecture consists of five sequential multi-kernel modules, which enable the automatic learning and extraction of spatial representations during the initial processing stage. Following this, 1 _×_ 1 convolutional layers are again employed to compress the feature maps by reducing the number of channels. The complete network configuration is illustrated in Fig. 3. 

## IV. EXPERIMENTS AND RESEARCH FINDINGS 

This section outlines the experimental configuration and presents the results used to assess the effectiveness of the proposed neural network for fall detection. The evaluation is conducted across multiple scenarios based on motion signals collected from wearable sensors positioned at the waist. 

All experiments were executed using the Google Colab Pro+ platform, equipped with a Tesla V100 GPU, to ensure efficient computation. The implementation was carried out using Python 3.6.9, along with key libraries, including TensorFlow 2.2.0, Keras 2.3.1, Scikit-Learn, NumPy 1.18.5, and Pandas 1.0.5. 

To validate the performance of the proposed network, we conducted a series of experiments focused on fall recognition. Additionally, the model’s performance was benchmarked against several widely used deep learning architectures, including CNN, LSTM, BiLSTM, GRU, and BiGRU. 

During the experiments, motion signal data were partitioned using a 5-fold cross-validation strategy to ensure reliable and unbiased performance evaluation. Multiple experimental trials were conducted to assess the recognition capability of five baseline deep learning architectures. The outcomes of these evaluations were quantified using key performance metrics, 

including accuracy, loss, and F1-score, as summarized in Table I. 

TABLE I 

PERFORMANCE COMPARISON OF BASELINE DEEP LEARNING MODELS AND THE PROPOSED 1D-RESNEXT USING ACCELEROMETER DATA 

|**Model**|**Classifcation Performance**|
|---|---|
||**Accuracy**<br>**Loss**<br>**F1-score**|
|CNN<br>LSTM<br>BiLSTM<br>GRU<br>BiGRU<br>**1D-ResNeXt**|89.77%(±2.44%)<br>0.29(±0.06)<br>89.59%(±2.51%)<br>87.55%(±4.32%)<br>0.42(±0.12)<br>87.13%(±4.80%)<br>89.27%(±2.58%)<br>0.32(±0.02)<br>89.07%(±2.56%)<br>90.02%(±1.14%)<br>0.31(±0.07)<br>89.83%(±1.21%)<br>88.52%(±3.67%)<br>0.32(±0.06)<br>88.43%(±3.67%)<br>**91.52%**(±**1.98%**)<br>**0.28**(±**0.09**)<br>**91.46%**(±**1.97%**)|



The experimental findings presented in Table I indicate that the proposed 1D-ResNeXt architecture consistently outperforms all baseline deep learning models for fall detection when utilizing accelerometer data. The model achieves an accuracy of 91.52%(±1.98%), a loss value of 0.28(±0.09), and an F1-score of 91.46%(±1.97%). These results surpass those of conventional models such as CNN (89.77%), LSTM (87.54%), BiLSTM (89.27%), GRU (90.02%), and BiGRU (88.52%). 

The enhanced performance of 1D-ResNeXt can be attributed to its architectural design, which incorporates multikernel convolutional modules and residual learning paths. This structure effectively mitigates the vanishing gradient issue, allowing the model to extract both short-range and long-range temporal features from motion sequences. The model’s strong performance across multiple evaluation metrics highlights its robustness and generalization capability. 

By leveraging residual connections, the network supports deeper configurations without experiencing degradation in training performance. This capability yields more expressive feature extraction and higher classification accuracy, demonstrating the effectiveness of the proposed approach for fall detection using wearable IMU sensors. 

TABLE II 

PERFORMANCE COMPARISON OF BASELINE DEEP LEARNING MODELS AND THE PROPOSED 1D-RESNEXT USING GYROSCOPE DATA 

|**Model**|**Classifcation Performance**|
|---|---|
||**Accuracy**<br>**Loss**<br>**F1-score**|
|CNN<br>LSTM<br>BiLSTM<br>GRU<br>BiGRU<br>**1D-ResNeXt**|73.83%(±4.40%)<br>0.55(±0.06)<br>73.27%(±5.07%)<br>73.09%(±7.13%)<br>0.56(±0.03)<br>71.96%(±7.56%)<br>56.86%(±4.15%)<br>0.70(±0.05)<br>47.39%(±10.66%)<br>69.35%(±6.19%)<br>0.62(±0.04)<br>68.37%(±6.52%)<br>59.11%(±4.07%)<br>0.72(±0.10)<br>51.24%(±10.84%)<br>**83.80%**(±**4.41%**)<br>**0.42**(±**0.08**)<br>**83.58%**(±**4.52%**)|



Table II reports the evaluation metrics of several deep learning architectures applied to fall detection using gyroscope sensor data. The results highlight noticeable performance differences when compared to accelerometer-based models. The proposed 1D-ResNeXt architecture achieves the highest performance, recording an accuracy of 83.80%(±4.41%), a 

Authorized licensed use limited to: Hanoi University of Science & Technology. Downloaded on April 02,2026 at 00:57:37 UTC from IEEE Xplore.  Restrictions apply. 200 

**==> picture [340 x 97] intentionally omitted <==**

**----- Start of picture text -----**<br>
�����<br>����������� ������������������� ��������������������<br>���<br>����<br>���� �� ��� ������� �� ������<br>����������<br>�����������<br>������������������<br>**----- End of picture text -----**<br>


Fig. 3. The 1D-ResNeXt model. 

loss of 0.42(±0.08), and an F1-score of 83.58%(±4.52%), significantly outperforming all baseline methods. 

In contrast, the baseline models demonstrate substantially reduced effectiveness when trained on gyroscope data. Specifically, CNN yields an accuracy of 73.83%(±4.40%), LSTM reaches 73.09%(±7.13%), GRU achieves 69.35%(±6.19%), BiLSTM reports 56.86%(±4.15%), and BiGRU performs at 59.11%(±4.07%). This performance gap, with the proposed model exceeding the best baseline by nearly 10 percentage points, underscores the enhanced capacity of 1D-ResNeXt to model and interpret rotational movement patterns inherent in gyroscope signals. 

This performance advantage is primarily attributed to the network’s multi-kernel module design, which enables effective feature extraction across multiple temporal resolutions. Such architecture allows the model to capture the intricate rotational dynamics characteristic of fall events, thereby improving classification accuracy when using gyroscopic input data. 

## TABLE III 

PERFORMANCE COMPARISON OF BASELINE DEEP LEARNING MODELS AND THE PROPOSED 1D-RESNEXT USING ACCELEROMETER AND GYROSCOPE DATA 

|**Model**|**Classifcation Performance**|
|---|---|
||**Accuracy**<br>**Loss**<br>**F1-score**|
|CNN<br>LSTM<br>BiLSTM<br>GRU<br>BiGRU<br>**1D-ResNeXt**|91.27%(±1.78%)<br>0.26(±0.05)<br>91.17%(±1.81%)<br>91.28%(±2.34%)<br>0.29(±0.07)<br>91.15%(±2.39%)<br>91.27%(±2.97%)<br>0.29(±0.08)<br>91.15%(±3.02%)<br>88.05%(±4.28%)<br>0.32(±0.10)<br>87.82%(±4.37%)<br>88.06%(±6.89%)<br>0.31(±0.10)<br>87.54%(±7.68%)<br>**92.27%**(±**2.14%**)<br>**0.26**(±**0.07**)<br>**92.20%**(±**2.13%**)|



Table III presents the evaluation metrics for fall detection when utilizing a fusion of accelerometer and gyroscope data. The results indicate substantial performance gains across all models compared to scenarios where individual sensor modalities were used independently. The 1D-ResNeXt model continues to outperform all other approaches, achieving the highest accuracy of 92.27%(±2.14%), the lowest loss at 0.26(±0.07), and the best F1-score of 92.20%(±2.12%). 

Notably, both LSTM and BiLSTM architectures exhibit marked improvement with the combined data, each reaching an accuracy of approximately 91.27%. The CNN model closely follows with 91.26%, while GRU and BiGRU deliver slightly lower performance, around 88.05%. These findings 

underscore the complementary characteristics of accelerometer and gyroscope sensors—the former capturing linear acceleration and the latter encoding angular motion—thereby enhancing the representation of fall-related activities when used together. 

The consistently strong performance of 1D-ResNeXt across all sensor configurations underscores its ability to learn and integrate informative features from multimodal sensor data effectively. This validates the robustness of the proposed architecture in real-world fall detection scenarios, where sensor fusion significantly enhances reliability and accuracy. 

## V. CONCLUSION AND FUTURE WORKS 

This study introduced 1D-ResNeXt, a novel deep residual architecture designed for human fall detection using motion signals from IMU sensors. By integrating multi-kernel convolutional modules with residual connections, the model effectively captures complex temporal dependencies in both accelerometer and gyroscope data. Comprehensive experiments on the PIF dataset confirmed that 1D-ResNeXt consistently outperformed standard deep-learning models across individual and fused sensor inputs. Key results include: (1) 91.52% accuracy with accelerometer data, (2) 83.80% with gyroscope data, and (3) 92.27% using sensor fusion. These findings highlight the complementary nature of combined motion sensors and demonstrate the model’s ability to capture features at multiple temporal resolutions, improving the distinction between falls and routine activities. 

The proposed system contributes to the advancement of sensor-based fall detection by offering enhanced feature representation and classification accuracy, making it suitable for deployment in wearable devices, intelligent health monitoring, and assisted living environments. However, certain limitations remain. The model’s generalizability could benefit from validation on larger, more diverse populations and across various sensor placements. Additionally, optimizing the network for low-power edge devices through compression and quantization is critical for practical implementation. 

Future work includes (1) detecting pre-fall patterns to enable early intervention, (2) integrating additional biosignals for holistic monitoring, (3) developing personalized models that adapt to individual behavior, and (4) employing federated learning to support privacy-preserving training. These direc- 

Authorized licensed use limited to: Hanoi University of Science & Technology. Downloaded on April 02,2026 at 00:57:37 UTC from IEEE Xplore.  Restrictions apply. 201 

tions will help bridge the gap between experimental results and robust, real-world fall detection systems. 

## ACKNOWLEDGMENT 

This research project was supported by University of Phayao and Thailand Science Research and Innovation Fund (Fundamental Fund 2025, Grant No. 5014/2567). 

## REFERENCES 

- [1] P. Iamtrakul, S. Chayphong, S. Jomnonkwao, and V. Ratanavaraha, “The association of falls risk in older adults and their living environment: A case study of rural area, thailand,” _Sustainability_ , vol. 13, no. 24, 2021. 

- [2] World Health Organization, “Falls: Fact sheets,” https://www.who.int/news-room/fact-sheets/detail/falls (accessed May 15, 2025). 

- [3] Y. Li, P. Liu, Y. Fang, X. Wu, Y. Xie, Z. Xu, H. Ren, and F. Jing, “A decade of progress in wearable sensors for fall detection (2015–2024): A network-based visualization review,” _Sensors_ , vol. 25, no. 7, 2025. 

- [4] S. Giovannini, F. Brau, V. Galluzzo, D. A. Santagada, C. Loreti, L. Biscotti, A. Laudisio, G. Zuccal`a, and R. Bernabei, “Falls among older adults: Screening, identification, rehabilitation, and management,” _Applied Sciences_ , vol. 12, no. 15, 2022. 

- [5] J. Fleming and C. Brayne, “Inability to get up after falling, subsequent time on floor, and summoning help: prospective cohort study in people over 90,” _BMJ_ , vol. 337, 2008. 

- [6] R. Zhao, W. Zhu, C. Han, B. Wei, H. Zhang, A. Rahman, and C. Li, “Pedestrian fall detection methods for public traffic areas: A literature review,” _Applied Sciences_ , vol. 14, no. 19, 2024. 

- [7] N. T. Newaz and E. Hanada, “The methods of fall detection: A literature review,” _Sensors_ , vol. 23, no. 11, 2023. 

- [8] S. Mekruksavanich, C. Promsakon, and A. Jitpattanakul, “Locationbased daily human activity recognition using hybrid deep learning network,” in _2021 18th International Joint Conference on Computer Science and Software Engineering (JCSSE)_ , 2021, pp. 1–5. 

- [9] A. Hussain, S. Ali, M.-I. Joo, and H.-C. Kim, “A deep learning approach for detecting and classifying cat activity to monitor and improve cat’s well-being using accelerometer, gyroscope, and magnetometer,” _IEEE Sensors Journal_ , vol. 24, no. 2, pp. 1996–2008, 2024. 

- [10] S. Mekruksavanich, D. Tancharoen, and A. Jitpattanakul, “Motionnext: A deep learning neural network for recognizing human motions related activities using inertial sensors,” in _2024 23rd International Symposium on Communications and Information Technologies (ISCIT)_ , 2024, pp. 218–222. 

- [11] J. Tang, B. He, J. Xu, T. Tan, Z. Wang, Y. Zhou, and S. Jiang, “Synthetic imu datasets and protocols can simplify fall detection experiments and optimize sensor configuration,” _IEEE Transactions on Neural Systems and Rehabilitation Engineering_ , vol. 32, pp. 1233–1245, 2024. 

- [12] S. Mekruksavanich and A. Jitpattanakul, “Sensor-based complex human activity recognition from smartwatch data using hybrid deep learning network,” in _2021 36th International Technical Conference on Circuits/Systems, Computers and Communications (ITC-CSCC)_ , 2021, pp. 1–4. 

- [13] A. Bourke, J. O’Brien, and G. Lyons, “Evaluation of a threshold-based tri-axial accelerometer fall detection algorithm,” _Gait & Posture_ , vol. 26, no. 2, pp. 194–199, 2007. 

- [14] M. Schneider, K. Seeser-Reich, A. Fiedler, and U. Frese, “Enhancing slip, trip, and fall prevention: Real-world near-fall detection with advanced machine learning technique,” _Sensors_ , vol. 25, no. 5, 2025. 

- [15] B. A. Atalaa, I. Ziedan, A. Alenany, and A. Helmi, “Feature engineering for human activity recognition,” _International Journal of Advanced Computer Science and Applications_ , vol. 12, no. 2, 2021. 

- [16] S. Mekruksavanich, W. Phaphan, and A. Jitpattanakul, “A deep multitask learning network for activity recognition and user identification using smartphone sensors,” _Procedia Computer Science_ , vol. 256, pp. 1350–1357, 2025, cENTERIS - International Conference on ENTERprise Information Systems / ProjMAN - International Conference on Project MANagement / HCist - International Conference on Health and Social Care Information Systems and Technologies. 

- [17] N. A. Choudhury and B. Soni, “Enhanced complex human activity recognition system: A proficient deep learning framework exploiting physiological sensors and feature learning,” _IEEE Sensors Letters_ , vol. 7, no. 11, pp. 1–4, 2023. 

- [18] S. Mekruksavanich, N. Hnoohom, W. Phaphan, and A. Jitpattanakul, “A comparative study of validation methods for sensor-based human activity recognition using deep learning models,” in _2025 Joint International Conference on Digital Arts, Media and Technology with ECTI Northern Section Conference on Electrical, Electronics, Computer and Telecommunications Engineering (ECTI DAMT & NCON)_ , 2025, pp. 686–691. 

- [19] A. D. Mohapatra, A. Aggarwal, and R. K. Tripathy, “Automated recognition of hand gestures from multichannel emg sensor data using time–frequency domain deep learning for iot applications,” _IEEE Sensors Letters_ , vol. 8, no. 6, pp. 1–4, 2024. 

- [20] S. Mekruksavanich, O. Surinta, and A. Jitpattanakul, “A deep neural network with aggregated residual transformation for smartwatch-based human activity recognition in real world situations,” _ICIC Express Letters_ , vol. 19, no. 3, pp. 343–351, 2025. 

- [21] V. M. Reddy Anakala, M. Rashmi, B. V. Natesha, and R. M. Reddy Guddeti, “Fall detection and elderly monitoring system using the cnn,” in _Machine Learning and Computational Intelligence Techniques for Data Engineering_ , P. Singh, D. Singh, V. Tiwari, and S. Misra, Eds. Singapore: Springer Nature Singapore, 2023, pp. 171–182. 

- [22] N. Hnoohom, S. Mekruksavanich, and A. Jitpattanakul, “Pre-impact and impact fall detection based on a multimodal sensor using a deep residual network,” _Intelligent Automation & Soft Computing_ , vol. 36, no. 3, pp. 3371–3385, 2023. 

- [23] Y. Uotani, K. Yamamoto, C. Ye, M. Bouazizi, and T. Ohtsuki, “An lstmbased approach for fall detection using accelerometer-collected data,” in _2023 28th Asia Pacific Conference on Communications (APCC)_ , 2023, pp. 250–255. 

- [24] S. Mekruksavanich, N. Hnoohom, W. Phaphan, and A. Jitpattanakul, “Orthopedic walker fall detection and motion classification using bidirectional gated recurrent unit neural network,” in _2025 Joint International Conference on Digital Arts, Media and Technology with ECTI Northern Section Conference on Electrical, Electronics, Computer and Telecommunications Engineering (ECTI DAMT & NCON)_ , 2025, pp. 447–452. 

- [25] T. Ahmad, J. Wu, H. S. Alwageed, F. Khan, J. Khan, and Y. Lee, “Human activity recognition based on deep-temporal learning using convolution neural networks features and bidirectional gated recurrent unit with features selection,” _IEEE Access_ , vol. 11, pp. 33 148–33 159, 2023. 

- [26] S. Mekruksavanich, P. Jantawong, N. Hnoohom, and A. Jitpattanakul, “Automatic fall detection using deep neural networks with aggregated residual transformation,” in _2022 37th International Technical Conference on Circuits/Systems, Computers and Communications (ITC-CSCC)_ , 2022, pp. 811–814. 

- [27] K. He, X. Zhang, S. Ren, and J. Sun, “Deep residual learning for image recognition,” in _2016 IEEE Conference on Computer Vision and Pattern Recognition (CVPR)_ , 2016, pp. 770–778. 

- [28] S. Mekruksavanich and A. Jitpattanakul, “Fallnext: A deep residual model based on multi-branch aggregation for sensor-based fall detection,” _ECTI Transactions on Computer and Information Technology (ECTI-CIT)_ , vol. 16, no. 4, pp. 352—364, Sep. 2022. 

- [29] F. Bianchi, S. J. Redmond, M. R. Narayanan, S. Cerutti, and N. H. Lovell, “Barometric pressure and triaxial accelerometry-based falls event detection,” _IEEE Transactions on Neural Systems and Rehabilitation Engineering_ , vol. 18, no. 6, pp. 619–627, 2010. 

- [30] L.-J. Kau and C.-S. Chen, “A smart phone-based pocket fall accident detection, positioning, and rescue system,” _IEEE Journal of Biomedical and Health Informatics_ , vol. 19, no. 1, pp. 44–56, 2015. 

- [31] J. He, Z. Zhang, X. Wang, and S. Yang, “A low power fall sensing technology based on fd-cnn,” _IEEE Sensors Journal_ , vol. 19, no. 13, pp. 5110–5118, 2019. 

- [32] M. Musci, D. De Martini, N. Blago, T. Facchinetti, and M. Piastra, “Online fall detection using recurrent neural networks on smart wearable devices,” _IEEE Transactions on Emerging Topics in Computing_ , vol. 9, no. 3, pp. 1276–1289, 2021. 

- [33] M. K. Dhaliwal, R. Sharma, and R. Kaur, “PIF dataset: a comprehensive dataset of physiological and inertial features for recognition of human activities,” _Multimedia Tools and Applications_ , vol. 83, no. 29, pp. 73 607–73 625, Sep. 2024. 

- [34] S. Xie, R. Girshick, P. Doll´ar, Z. Tu, and K. He, “Aggregated residual transformations for deep neural networks,” in _2017 IEEE Conference on Computer Vision and Pattern Recognition (CVPR)_ , 2017, pp. 5987– 5995. 

Authorized licensed use limited to: Hanoi University of Science & Technology. Downloaded on April 02,2026 at 00:57:37 UTC from IEEE Xplore.  Restrictions apply. 202 

