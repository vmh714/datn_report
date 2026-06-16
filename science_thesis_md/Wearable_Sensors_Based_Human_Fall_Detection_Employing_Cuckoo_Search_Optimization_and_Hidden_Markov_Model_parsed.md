### Tóm tắt:
Bài báo đề xuất một phương pháp phát hiện ngã ở người cao tuổi sử dụng các cảm biến đeo trên người như gia tốc kế và con quay hồi chuyển. Quy trình xử lý bao gồm việc lọc nhiễu bằng bộ lọc Kalman, phân đoạn dữ liệu bằng phương pháp cửa sổ trượt và trích xuất các đặc trưng miền thời gian và tần số. Thuật toán tối ưu hóa bầy chim cúc cu (Cuckoo Search Optimization) được áp dụng để lựa chọn các đặc trưng tối ưu trước khi đưa vào phân loại bằng Mô hình Markov ẩn (HMM). Hệ thống đạt độ chính xác nhận dạng ấn tượng lên đến 93,7%, cho thấy tiềm năng ứng dụng thực tế cao trong việc giám sát và cảnh báo ngã thời gian thực.

### BibTeX:
```bibtex
@article{nazar2025wearable,
  author = {Nazar, Fakhra and Jalal, Ahmad},
  title = {Wearable Sensors-Based Human Fall Detection Employing Cuckoo Search Optimization and Hidden Markov Model},
  journal = {IEEE},
  year = {2025}
}
```

---

## NỘI DUNG BÀI BÁO CHI TIẾT

# Wearable Sensors-Based Human Fall Detection Employing Cuckoo Search Optimization and Hidden Markov Model 

Fakhra Nazar _Dept. of Computer Science Air University_ Islamabad, Pakistan fakhra_nazar@upr.edu.pk 

Ahmad Jalal _Dept. of Computer Science Air University_ Islamabad, Pakistan ahmadjalal@mail.au.edu.pk 

_**Abstract**_ **—The measurement of human motion using wearable sensing equipment is useful in detecting falls and assessing the security of the elderly. Accelerator and gyroscope sensors have been popularly applied in systems called human activity recognition (HAR) to measure the dynamics of human activities in real-life conditions. Such sensors have the potential to provide early warnings of abnormal operations and therefore act promptly in the healthcare setup. Here, we introduce an accurate and effective methodology for identifying fall-related behaviors based on optimized time and frequency domain features. In the first step, statistical and spectral features were obtained based on preprocessed data of inertial sensors. The attempt of feature selection was to improve the level of classification, and the Cuckoo Search Optimization algorithm was utilized. Each activity was subsequently classified by using Hidden Markov Models (HMMs) to train a Gaussian HMM model of each activity to capture sequential and temporal patterns. This model of human action transition is useful in modeling human behavior. It was experimentally found that it has a significant recognition accuracy of 93.7, which supports the claim that it works well in real-time fall detection and elderly surveillance.** 

_**Keywords—Artificial intelligence, cuckoo search optimization, deep learning, human activity recognition, hidden marcov model, machine learning.**_ 

I. INTRODUCTION 

As the population of the world gradually grows, especially in the ageing population, there has been a significant increment in age-related health issues with an increase in the rate of falls, chronic illnesses, less mobility and degenerative diseases. A close connection between human health and physical activity is the reason that medical experts consider it to be a key role to insert daily exercises into the everyday routine, which contributes to the improvement of physical and mental health. An active lifestyle has also been seen to prevent the occurrence of serious illnesses like heart diseases, diabetes and neurodegenerative diseases [1-3]. Human Activity Recognition (HAR) is crucial when coming up with smart systems capable of monitoring, assisting, and protecting individuals in a diverse environment. HAR is one of the important elements of intelligent systems provided by the powers of artificial intelligence and machine learning. Due to the recent advancements in sensors, microcontrollers, and wireless communication of data, wearable devices have become a part of our daily routine in no time. This has necessitated tracking exercises in areas that go past health care, elderly care, workplace safety, interactive gaming, rehabilitation therapy, military training, as well as emergency response systems [4-6]. 

The integration of wearable sensors and intelligent models initiated a considerable evolution of Human Activity Recognition (HAR) field, where machine learning and deep learning methods come to the forefront of advancing recognition accuracy and system adjustment to particular models. In 2018, Biagetti et al. offered a system of integrating wearable technologies (accelerometers and sEMG sensors) to monitor daily activities with higher levels of accuracy achieved by means of wireless sensor nodes [7]. In the same year, Erhan et al. developed a smartphone-based human activity recognition (HAR) solution using the embedded mobile phone sensor system to label the user activity, to capture the emerging importance of mobile HAR as they gain ubiquity and a wide range of sensors[8]. Later, in the year 2019, Nguyen et al. proposed the use of an ensemble learning to extend the use of conventional machine learning methods in human activity recognition using wearable sensor information in response to the drawbacks of hand [9]. In around 2021, Vishwanath et al. created a deep learning-based system to identify human activities via gait pattern of wearable IMU sensors and integrate different neural architecture networks to categorize human activities into seven discrete bodily movements in offline and online modes[10].In the same year, Alireza Abedin et al. suggested a deep learning HAR framework that optimizes feature discriminability through the utilization of inter-sensor relationships, data-agnostic augmentation as well as state-ofthe-art strategies of classification loss to better represent activities based on wearable sensor data[11]. Afterwards in 2022, Yee Jia Luwe, Chin Poo Lee and Kian Ming Lim presented a strong hybrid deep learning model that involves 1D-CNN and BiLSTM to reach a high-accuracy human activity recognition using wearable sensor data in various benchmark datasets[12].In 2023, Zijie Chen et al. proposed an MP-HAR, motion-powered, battery-free energyharvesting human activity recognition system, which combines harvesting energy with real-time activity sensing as a low-powered and sustainable solution to pervasive IoT scenarios[13]. Several approaches have been discussed so far in the field of Human Activity Recognition to achieve better accuracy, generalizability, and robustness in a sensor-based recognition scheme. This paper testifies to some features of time and frequency spectrum coupled with metaheuristic optimization and probabilistic modeling to achieve the same using wearable sensor data in fall-related activities. 

The suggested study holds an effective model of identification and categorization of physical activities on the dataset kFall, which is specifically designed for the purpose of a fall detection procedure with the assistance of wearable 

979-8-3315-5804-8/25/$31.00 ©2025 IEEE 

Authorized licensed use limited to: Hanoi University of Science & Technology. Downloaded on June 14,2026 at 13:22:15 UTC from IEEE Xplore.  Restrictions apply. 

inertial (accelerometer and gyroscope) sensors.The Kalman filter was applied to pre-process the raw accelerometer and gyroscope signals so that the sensor noise could be eliminated, but important motion patterns are retained. It was then divided into meaningful subdivisions by using a sliding window segmentation method that provided an overlap of 50 percent so that the information about temporal dynamics could be extracted. In each of the segments, six major characteristics were calculated, namely the Shannon entropy, signal magnitude, standard deviation, spectral energy, and cumulative length in order to define linear and non-linear movement. The Cuckoo Search Algorithm was applied in order to optimize these features by minimizing redundancy and improving group discriminability in the feature space. The classifier was a Hidden Markov Model (HMM) because it works well in modeling the probability of transitions and sequential dependencies. The suggested system showed encouraging classification results, proving it has high potential for being applied in real-life implementations in fall detection, remote health monitoring, and assistive smart environments. 

The framework, proposed in this paper, is elaborated in the following sections of this paper. Section II describes the entire procedure, such as preprocessing and segmentation, optimization, and classification methodology. Section III states how the experiment was conducted on the KFall data, in addition to the evaluation criteria and the kinds of results that were evaluated by the authors.The operative rate of the system in terms of identifying activities and fall-related movements is also put in focus. And lastly, Section IV makes a conclusion to the study and presents possible directions for future improvements and actual implementation. 

## II. PROPOSED FRAMEWORK FOR SENSOR-BASED FALL DETECTION 

The paper has outlined a powerful and smart design of wearable sensor-based Human Activity Recognition (HAR) on the dataset called KFall. The sensor signals were obtained first as the raw signal, and these were filtered using a Kalman filter to remove the undesired noise and regain the quality of the signal. Denoised signals were then segmented with the sliding overlapping window methodology, maintaining continuity of activity development in time. A number of explanatory statistical and frequency-based features were then formed out of every window. They were Shannon entropy, magnitude signal, standard deviation, spectral energy, and cumulative length, and represented well the complexity, as well as the dynamics of human movement.To maximize optimization of the system, the windowing parameters have been optimized on the basis of the Cuckoo Search Optimization Algorithm. Lastly, a Hidden Markov Model (HMM) was used to model the sequence dependence of the features, which were extracted and hence classified the various activities of the human with absolute precision. Classification accuracy was used to determine the effectiveness of the system. Figure 1 presents the entire structural flow of the proposed HAR methodology. 

- _A. Pre-processing pipeline, Filtering and Sliding Window Technique:_ 

At the start, signal enhancement was performed to improve the quality of the raw sensor data from the KFall 

**==> picture [222 x 155] intentionally omitted <==**

Fig. 1. An overview of the proposed HAR framework using wearable sensors data. 

dataset. We used the Kalman filter in order to avoid random noise and maintain significant transitions in the activity signal [14]. This recursive filter estimated the true signal by predicting and updating values based on a mathematical model. The filter used the following equation: 

𝑥̂ 𝑘 = 𝑥̂ 𝑘𝑘−1 + 𝐾𝑘(𝑍𝑘 −𝐻𝑥̂̂𝑘−1)                     (1) _x̂k_ in this formula is the estimated state at time _k_ , which uses _x̂k-1_ is the previously estimated state, _zk_ is the newly taken measurement, _H_ is the observation model and _Kk_ is the Kalman gain that updates the estimate by taking into the measurement error. The Kalman gain is calculated on the basis of predicted error and measurement noise. The process guarantees that the filtered signal will be near to the actual underlying activity and have the least abrupt increases or anomalies. Figure 2 demonstrates the raw vs Kalman-filtered signal that provides the smoothing influence on Accelerometer data and still keeps a consequence of transitions that play a crucial role in HAR. 

**==> picture [244 x 82] intentionally omitted <==**

Fig. 2. Original and filtered signal of the accelerometer using the Kalman filter 

We did data segmentation through a sliding window method after we applied the Kalman filter to our noise reduction system[15]. To provide enough continuity in time, a fixed window size of 200 samples and an overlap of 50% (i.e., 100 samples) was applied. This model was used to give each segment some points of data to share relative to the adjacent segments without losing significant transitions between activities of falling, sitting, or walking. The segmentation process was realized through an iterative procedure of filter step size of: 

**==> picture [162 x 10] intentionally omitted <==**

where, _N_ =200, the window size, and _O_ =100, the overlap. The _step size_ that was obtained after using 100 samples resulted in overlapping window definitions of: 

𝑊𝑖 = {𝑥̂𝑗 ∣𝑗= 𝑖.𝑠𝑡𝑒𝑝𝑠𝑖𝑧𝑒,…,𝑖.𝑠𝑡𝑒𝑝𝑠𝑖𝑧𝑒+ 𝑁−1}     (3) 

This meant that each of the windows had some portion of the last window, and this reduced the effects of boundaries and consequently the possibility of overlooking key 

Authorized licensed use limited to: Hanoi University of Science & Technology. Downloaded on June 14,2026 at 13:22:15 UTC from IEEE Xplore.  Restrictions apply. 

transitions between activities. The segmented accelerometer signals are as illustrated in Figure 3. This approach aided reproducible and representative feature extraction since it retained dependencies of features over the time windows necessary in the context of Human Activity Recognition with wearable sensors. 

**==> picture [244 x 87] intentionally omitted <==**

Fig. 3. A Sliding Window-Based Data Segmentation over accelerometer data 

## _B. Computation of Activity-Specific Features:_ 

Five different features were then extracted on each axis of the acceleration and gyroscope data (x, y, and z). **Shanoon Entropy:** This feature measures the randomness or the uncertainty in the accelerometer and the gyroscope signal [16]. An increase in entropy means that the activity is more complicated or unpredictable. 

**==> picture [173 x 10] intentionally omitted <==**

In this case, _H_ is the Shannon entropy, _pi_ is the probability of an occurrence of a value in the _i[th]_ signal, and _n_ is a number of possible signal values corresponding to a spectrum. To be able to choose activities, entropy is particularly applicable in HAR since various activities have disparate levels of signal complexity. In Figure 4, we can see the Shannon entropy of the accelerometer signal during the activity of Forward Fall while walking, caused by a slip. 

**==> picture [244 x 105] intentionally omitted <==**

Fig. 4. Shannon Entropy of Accelerometer signal Along X, Y, and Z Axes 

**Standard Deviation** : Standard deviation is a measure of the extent of dispersion or the variability of accelerometer and gyroscope data around the mean [17]. Standard Deviation is calculated as: 

**==> picture [179 x 23] intentionally omitted <==**

In this case, the standard deviation refers to σ, individual data points are _xi_ , the mean is _μ_ , and the number of samples is _N_ .The calculation of this feature was carried out on all axes of both the accelerometer and the gyroscope data. Figure 5 represents the visualization of the standard deviation in various segments of Gyroscope signals data. 

**Spectral Energy:** The strength of the signal in the frequency domain, shown as spectral energy, indicates how periodic that type of movement is, e.g., how someone is walking or riding a bicycle [18]. The equation below is that of spectral energy. 

**==> picture [167 x 11] intentionally omitted <==**

**==> picture [245 x 103] intentionally omitted <==**

Fig. 5. Axis-Wise Standard Deviation of Gyroscope Signals for Activity Recognition 

Where _X(fi)_ is the discrete Fourier Transform (DFT) of a signal at frequency _fi_ and _N_ is the number of frequency bins. To cover both translational and rotational frequency components, each side of the two sensors was calculated on the basis of this feature. Figure 6 represents the spectral distribution of energy from Accelerometer signals data in activities. 

**==> picture [244 x 103] intentionally omitted <==**

Fig. 6. Spectral energy computed for each Accelerometer axis data 

**Cumulative Length:** Cumulative length recorded the overall distance a signal followed through a window, which was used to represent the richness and the scope of movement [19]. Cumulative length equation is as follows: 

**==> picture [174 x 14] intentionally omitted <==**

Where _CL_ is the total length, and _xi_ means the consecutive signal values. This was done per accelerometer and gyroscope axis, which provides an indication of the movement path of the activity. Figure 7 is the visualization of cumulative lengths along the chosen segments windowed Gyroscope data. 

**==> picture [245 x 93] intentionally omitted <==**

Fig. 7. Cumulative Angular Displacement from each Gyroscope Axis signal 

**Magnitude signal feature:** Magnitude signal is a typical feature in signal processing Human Activity Recognition (HAR) to retrieve the overall intensity of movement by summing up the x, y, and z elements of sensor data in a single scalar value [19, 20]. This feature is used as an overall activity data of the three-axis accelerometer or gyroscope measurements. It gave a common scale of the strength of motion and served to distinguish between the stationary and the moving activities. 

Authorized licensed use limited to: Hanoi University of Science & Technology. Downloaded on June 14,2026 at 13:22:15 UTC from IEEE Xplore.  Restrictions apply. 

The equation of signal magnitude is as follows: 

𝑀= √𝑥̂[2] + 𝑦[2] + 𝑧[2] (8) 

In this equation, _x, y_ , and _z_ represent signal values along each individual axis. The accelerometer and the gyroscope were computed separately, with the magnitude of translational and rotational movement. The magnitude variation in the values of the Accelerometer readings is observed in Fig. 8. 

**==> picture [244 x 133] intentionally omitted <==**

Fig. 8. Accelerometer-Based Signal Magnitude Area (SMA) 

## _C. Features Optimisation Strategy:_ 

In this research, one metaheuristic approach, specifically the Cuckoo Search Optimization (CSO) tool feature selection mechanism, was used after the original segmented sensor data were utilized in retrieving the initial set of features. CSO draws its inspiration on the behaviour of cuckoo birds with brood parasitism, by searching the feature space through a population of nests, encoded as a binary-valued nest, where a feature in the population will be represented by either a 1 or a 0, where a 1 will indicate that this is a selected feature, and a 0 will exclude it [21]. The algorithm improves the population into better-performing combinations because of randomized mechanisms of exploration and selection. The quality of the feature subset is quantified by the mean classification accuracy of 3-fold cross-validation of a Random Forest classifier to calculate the fitness function of each nest: 

**==> picture [202 x 19] intentionally omitted <==**

In order to achieve such diversity in the search, the algorithm uses a bitwise strategy of XOR mutation. It takes advantage of the mutation process (bitwise XOR) in order to simulate the Levy flight move in the search space. 

**==> picture [169 x 12] intentionally omitted <==**

Where _x[(t)]_ is the current binary feature vector, and _step_ is a binary random vector generated. In case the newly formed nest is of greater fitness, then the original will be shelved. A small percentage of nests is also probabilistically abandoned according to a discovery probability pa, and new random nests are added to keep the diversity of exploration. The search was performed 20 times on a 12-nest population. The most successful feature mask produced using this process substantially diminished the dimensions of the feature, and much discriminative information concerning activity was preserved. The last model, which has been retrained with the help of only the selected features, showed a better classification accuracy and efficiency. Algorithm 1 shows the pseudocode of the CSO-based feature selection, which summarizes the pseudocode of the initialization of the solution, mutation, evaluation, and selection. 

## Algorithm 1: 

|Algorithm 1:|Algorithm 1:|
|---|---|
|Pseudo code for the Cuckoo Search Optimization||
|Input:||
|−|X: Feature matrix|
|−|y: Activity labels|
|−|n_nests: Number of candidate solutions (nests)|
|−|max_iter: Maximum number of generations|
|−|pa: Discovery probability (abandonment rate)|
|1.|Initialize nests randomly as binary vectors (0: unselected, 1:|
||selected)|
|2.|Evaluate the fitness of each nest:|
|For|each nest:|
|−|Select features where bit == 1|
|−|Train Random Forest with 3-fold cross-validation|
|−|Fitness = mean classification accuracy|
|3.|Identify the best nest and store its fitness|
|4.|For generation = 1 to max_iter:|
||a<br>Generate new nests by XOR-based mutation:|
||For each nest:|
||−<br>step ← random binary vector|
||−<br>new_nest = XOR(nest, step)|
||b<br>Evaluate fitness of all new nests using the same fitness|
||function|
||c<br>Replace nests if new_nest has better fitness|
||d<br>Abandon a fraction (pa) of the worst nests:|
||−<br>Replace them with new random binary solutions|
||e<br>Update global best_nest if a new higher fitness is found|
||f<br>Append best_fitness to fitness_trace|
|5.|Return best_nest, best_fitness, fitness_trace|



Figure 9 shows the classification confidence of available feature subsets to various activities of falls in a 3D fitness landscape. The gradient of the color and texture of the surface proves the convergence nature and stability of the Cuckoo Search algorithm when finding out the feature combinations that have high quality related to Human Activity Recognition. 

**==> picture [211 x 159] intentionally omitted <==**

Fig.9 Graphical description of 3D fitness plot of Cuckoo Search accuracy on feature subsets 

## _D. Classification with Probabilistic Modeling_ 

In the suggested Human Activity Recognition (HAR) model, Hidden Markov Models (HMMs) were applied to classify the data presented as a model that allowed for representing the temporal relationship and sequential pattern in time-series data gathered through sensors[22]. It was started with a 75:25 split, preventing imbalance in the training and test sets of all 15 classes of the fall-related activities. The Gaussian HMM applied consisted of three hidden states per activity; each representing various temporal portions of the activity: the onset, the execution, and the termination. Such architecture enabled the model to learn the statistical patterns of a certain class. The training was done on all the models 

Authorized licensed use limited to: Hanoi University of Science & Technology. Downloaded on June 14,2026 at 13:22:15 UTC from IEEE Xplore.  Restrictions apply. 

under the Baum-Welch algorithm up to 100 runs, expecting a diagonal covariance structure due to numerical stability. Assume the sequence of feature vectors that were observed as: 

𝑂= {𝑜1, 𝑜2, 𝑜3, … . 𝑜𝑇} (11) 

_Ot_ in this equation is the feature vector at time step t. Given some trained HMM _λk_ corresponding to a given class _k_ , the probability of the observation sequence is found as: 

𝑃(𝑂∣𝜆𝑘) = ∑𝑃( 𝑂𝑄 **∣** 𝑄, 𝜆𝑘). 𝑃(𝑄∣𝜆𝑘)      (12) Here, _Q_ ={ _q1,q2,..., qT_ } is the hidden state sequence. In the inference step, the activity ŷ is predicted as the label that entails the highest log-likelihood of the model. 

ŷ = 𝑎𝑟𝑔𝑚𝑎𝑥̂𝑘𝑙𝑜𝑔𝑃(𝑂∣𝜆𝑘)                (13) 

This method allows the classifier to be able to track the temporal change of every activity class, and it is especially practical in distinguishing visually or kinetically related actions like slips, trips, falls, and fainting episodes. Table 1 displays the values of the hyperparameters of the HMM that are used to perform classification. 

TABLE I. HYPERPARAMETER SETUP OF CLASS-SPECIFIC HIDDEN MARKOV 

|HYPERPARAMETERSETUP OFCLASS-SPECIFICHIDDEN|HYPERPARAMETERSETUP OFCLASS-SPECIFICHIDDEN|
|---|---|
|MODELS||
|n_components|3|
|covariance_type|diag|
|n_iter|100|
|<br>init_params|Random|



This modular architecture using HMM helps in real-time interpretability and extensibility, which are very important to healthcare applications, smart monitoring, and emergency response systems. 

## III. EXPERIMENTAL VALIDATION 

## _A. KFall Dataset Description:_ 

In our work, we utilized data on wearable sensors of elderly individuals during fall detection using KFall dataset, which is comprised of labeled time-series data [23]. The dataset consists of measurements of an accelerometer, gyroscope, and a magnetometer worn on the waist, recorded at 100 Hz. In the current study, accelerometer and gyroscope data were utilized, and no other information was incorporated because of the focus on the motion dynamics, which helped 

to detect falls, and the efficiency of the sensors. It incorporates fall events such as Backward fall when trying to sit down, Backward fall while sitting caused by fainting, Backward fall while walking caused by a slip, Fall while walking, with use of hands on a table to dampen fall caused by fainting, Forward fall when trying to get up, Forward fall when trying to sit down, Forward fall while jogging caused by a trip, Forward fall while sitting caused by fainting, Forward fall while walking caused by a slip, Forward fall while walking caused by a trip, Forward lateral fall while walking caused by a slip, Vertical (forward) fall while walking caused by fainting, Lateral fall when trying to get up, Lateral fall when trying to sit down, and Lateral fall while sitting caused by fainting. In this work, only the signals of the accelerometer and gyroscope were used, as this is the best way to describe human motion, with the reason of maintaining the efficiency of the sensors. The data is labeled clearly and has a wide range of activities that would be suitable for training a machine learning model to detect falls and classify activities. 

**==> picture [236 x 177] intentionally omitted <==**

**----- Start of picture text -----**<br>
TABLE II. CLASSIFICATION REPORT OF HMM CLASSIFIER RECOGNITION<br>ACCURACY USING KFALL DATASET<br>Precision  Recall  F1- Support<br>BS  0.987  0.760  0.859  100<br>BF  0.990  1.000  0.995  100<br>BL  1.000  0.990  0.995  100<br>TF  0.907  0.880  0.893  100<br>FS  0.958  0.920  0.939  100<br>FT  0.779  0.810  0.794  100<br>FJ  1.000  0.990  0.995  100<br>FF  0.990  0.980  0.985  100<br>FW  0.793  0.960  0.869  100<br>TW  0.990  1.000  0.995  100<br>SW  0.961  0.990  0.975  100<br>VF  0.933  0.980  0.956  100<br>SS  0.970  0.980  0.975  100<br>ST  0.868  0.920  0.893  100<br>SF  0.989  0.900  0.942  100<br>Mean Accuracy:                0.937<br>**----- End of picture text -----**<br>


***** BS=FallBack-Sit,BF=FallBack-Faint,BL=FallBack-Slip,TF=FallTableFaint, FS=FallFwd-Stand,FT=FallFwd-Sit,FJ=FallFwd-Jog,FF=FallFwdFaintSit, FW=FallFwd-SlipWalk,TW=FallFwd-TripWalk,SW=FallSideSlipWalk,VF= FallVert-FaintWalk,SS=FallSide-Stand,ST=FallSideSit,SF=FallSide-FaintSit 

|,<br>gyroscope, and a magnetometer worn on the waist, recorded<br>at 100 Hz. In the current study, accelerometer and gyroscope<br>data were utilized, and no other information was incorporated<br>because of the focus on the motion dynamics, which helped<br>Faint, FS=FallFwd-Stand,FT=FallFwd-Sit,FJ=FallFwd-Jog,FF=FallFwd-<br>FaintSit, FW=FallFwd-SlipWalk,TW=FallFwd-TripWalk,SW=FallSide-<br>SlipWalk,VF= FallVert-FaintWalk,SS=FallSide-Stand,ST=FallSide-<br>Sit,SF=FallSide-FaintSit|,<br>gyroscope, and a magnetometer worn on the waist, recorded<br>at 100 Hz. In the current study, accelerometer and gyroscope<br>data were utilized, and no other information was incorporated<br>because of the focus on the motion dynamics, which helped<br>Faint, FS=FallFwd-Stand,FT=FallFwd-Sit,FJ=FallFwd-Jog,FF=FallFwd-<br>FaintSit, FW=FallFwd-SlipWalk,TW=FallFwd-TripWalk,SW=FallSide-<br>SlipWalk,VF= FallVert-FaintWalk,SS=FallSide-Stand,ST=FallSide-<br>Sit,SF=FallSide-FaintSit|,<br>gyroscope, and a magnetometer worn on the waist, recorded<br>at 100 Hz. In the current study, accelerometer and gyroscope<br>data were utilized, and no other information was incorporated<br>because of the focus on the motion dynamics, which helped<br>Faint, FS=FallFwd-Stand,FT=FallFwd-Sit,FJ=FallFwd-Jog,FF=FallFwd-<br>FaintSit, FW=FallFwd-SlipWalk,TW=FallFwd-TripWalk,SW=FallSide-<br>SlipWalk,VF= FallVert-FaintWalk,SS=FallSide-Stand,ST=FallSide-<br>Sit,SF=FallSide-FaintSit|,<br>gyroscope, and a magnetometer worn on the waist, recorded<br>at 100 Hz. In the current study, accelerometer and gyroscope<br>data were utilized, and no other information was incorporated<br>because of the focus on the motion dynamics, which helped<br>Faint, FS=FallFwd-Stand,FT=FallFwd-Sit,FJ=FallFwd-Jog,FF=FallFwd-<br>FaintSit, FW=FallFwd-SlipWalk,TW=FallFwd-TripWalk,SW=FallSide-<br>SlipWalk,VF= FallVert-FaintWalk,SS=FallSide-Stand,ST=FallSide-<br>Sit,SF=FallSide-FaintSit|,<br>gyroscope, and a magnetometer worn on the waist, recorded<br>at 100 Hz. In the current study, accelerometer and gyroscope<br>data were utilized, and no other information was incorporated<br>because of the focus on the motion dynamics, which helped<br>Faint, FS=FallFwd-Stand,FT=FallFwd-Sit,FJ=FallFwd-Jog,FF=FallFwd-<br>FaintSit, FW=FallFwd-SlipWalk,TW=FallFwd-TripWalk,SW=FallSide-<br>SlipWalk,VF= FallVert-FaintWalk,SS=FallSide-Stand,ST=FallSide-<br>Sit,SF=FallSide-FaintSit|,<br>gyroscope, and a magnetometer worn on the waist, recorded<br>at 100 Hz. In the current study, accelerometer and gyroscope<br>data were utilized, and no other information was incorporated<br>because of the focus on the motion dynamics, which helped<br>Faint, FS=FallFwd-Stand,FT=FallFwd-Sit,FJ=FallFwd-Jog,FF=FallFwd-<br>FaintSit, FW=FallFwd-SlipWalk,TW=FallFwd-TripWalk,SW=FallSide-<br>SlipWalk,VF= FallVert-FaintWalk,SS=FallSide-Stand,ST=FallSide-<br>Sit,SF=FallSide-FaintSit|,<br>gyroscope, and a magnetometer worn on the waist, recorded<br>at 100 Hz. In the current study, accelerometer and gyroscope<br>data were utilized, and no other information was incorporated<br>because of the focus on the motion dynamics, which helped<br>Faint, FS=FallFwd-Stand,FT=FallFwd-Sit,FJ=FallFwd-Jog,FF=FallFwd-<br>FaintSit, FW=FallFwd-SlipWalk,TW=FallFwd-TripWalk,SW=FallSide-<br>SlipWalk,VF= FallVert-FaintWalk,SS=FallSide-Stand,ST=FallSide-<br>Sit,SF=FallSide-FaintSit|,<br>gyroscope, and a magnetometer worn on the waist, recorded<br>at 100 Hz. In the current study, accelerometer and gyroscope<br>data were utilized, and no other information was incorporated<br>because of the focus on the motion dynamics, which helped<br>Faint, FS=FallFwd-Stand,FT=FallFwd-Sit,FJ=FallFwd-Jog,FF=FallFwd-<br>FaintSit, FW=FallFwd-SlipWalk,TW=FallFwd-TripWalk,SW=FallSide-<br>SlipWalk,VF= FallVert-FaintWalk,SS=FallSide-Stand,ST=FallSide-<br>Sit,SF=FallSide-FaintSit|,<br>gyroscope, and a magnetometer worn on the waist, recorded<br>at 100 Hz. In the current study, accelerometer and gyroscope<br>data were utilized, and no other information was incorporated<br>because of the focus on the motion dynamics, which helped<br>Faint, FS=FallFwd-Stand,FT=FallFwd-Sit,FJ=FallFwd-Jog,FF=FallFwd-<br>FaintSit, FW=FallFwd-SlipWalk,TW=FallFwd-TripWalk,SW=FallSide-<br>SlipWalk,VF= FallVert-FaintWalk,SS=FallSide-Stand,ST=FallSide-<br>Sit,SF=FallSide-FaintSit|,<br>gyroscope, and a magnetometer worn on the waist, recorded<br>at 100 Hz. In the current study, accelerometer and gyroscope<br>data were utilized, and no other information was incorporated<br>because of the focus on the motion dynamics, which helped<br>Faint, FS=FallFwd-Stand,FT=FallFwd-Sit,FJ=FallFwd-Jog,FF=FallFwd-<br>FaintSit, FW=FallFwd-SlipWalk,TW=FallFwd-TripWalk,SW=FallSide-<br>SlipWalk,VF= FallVert-FaintWalk,SS=FallSide-Stand,ST=FallSide-<br>Sit,SF=FallSide-FaintSit|,<br>gyroscope, and a magnetometer worn on the waist, recorded<br>at 100 Hz. In the current study, accelerometer and gyroscope<br>data were utilized, and no other information was incorporated<br>because of the focus on the motion dynamics, which helped<br>Faint, FS=FallFwd-Stand,FT=FallFwd-Sit,FJ=FallFwd-Jog,FF=FallFwd-<br>FaintSit, FW=FallFwd-SlipWalk,TW=FallFwd-TripWalk,SW=FallSide-<br>SlipWalk,VF= FallVert-FaintWalk,SS=FallSide-Stand,ST=FallSide-<br>Sit,SF=FallSide-FaintSit|,<br>gyroscope, and a magnetometer worn on the waist, recorded<br>at 100 Hz. In the current study, accelerometer and gyroscope<br>data were utilized, and no other information was incorporated<br>because of the focus on the motion dynamics, which helped<br>Faint, FS=FallFwd-Stand,FT=FallFwd-Sit,FJ=FallFwd-Jog,FF=FallFwd-<br>FaintSit, FW=FallFwd-SlipWalk,TW=FallFwd-TripWalk,SW=FallSide-<br>SlipWalk,VF= FallVert-FaintWalk,SS=FallSide-Stand,ST=FallSide-<br>Sit,SF=FallSide-FaintSit|,<br>gyroscope, and a magnetometer worn on the waist, recorded<br>at 100 Hz. In the current study, accelerometer and gyroscope<br>data were utilized, and no other information was incorporated<br>because of the focus on the motion dynamics, which helped<br>Faint, FS=FallFwd-Stand,FT=FallFwd-Sit,FJ=FallFwd-Jog,FF=FallFwd-<br>FaintSit, FW=FallFwd-SlipWalk,TW=FallFwd-TripWalk,SW=FallSide-<br>SlipWalk,VF= FallVert-FaintWalk,SS=FallSide-Stand,ST=FallSide-<br>Sit,SF=FallSide-FaintSit|,<br>gyroscope, and a magnetometer worn on the waist, recorded<br>at 100 Hz. In the current study, accelerometer and gyroscope<br>data were utilized, and no other information was incorporated<br>because of the focus on the motion dynamics, which helped<br>Faint, FS=FallFwd-Stand,FT=FallFwd-Sit,FJ=FallFwd-Jog,FF=FallFwd-<br>FaintSit, FW=FallFwd-SlipWalk,TW=FallFwd-TripWalk,SW=FallSide-<br>SlipWalk,VF= FallVert-FaintWalk,SS=FallSide-Stand,ST=FallSide-<br>Sit,SF=FallSide-FaintSit|,<br>gyroscope, and a magnetometer worn on the waist, recorded<br>at 100 Hz. In the current study, accelerometer and gyroscope<br>data were utilized, and no other information was incorporated<br>because of the focus on the motion dynamics, which helped<br>Faint, FS=FallFwd-Stand,FT=FallFwd-Sit,FJ=FallFwd-Jog,FF=FallFwd-<br>FaintSit, FW=FallFwd-SlipWalk,TW=FallFwd-TripWalk,SW=FallSide-<br>SlipWalk,VF= FallVert-FaintWalk,SS=FallSide-Stand,ST=FallSide-<br>Sit,SF=FallSide-FaintSit|,<br>gyroscope, and a magnetometer worn on the waist, recorded<br>at 100 Hz. In the current study, accelerometer and gyroscope<br>data were utilized, and no other information was incorporated<br>because of the focus on the motion dynamics, which helped<br>Faint, FS=FallFwd-Stand,FT=FallFwd-Sit,FJ=FallFwd-Jog,FF=FallFwd-<br>FaintSit, FW=FallFwd-SlipWalk,TW=FallFwd-TripWalk,SW=FallSide-<br>SlipWalk,VF= FallVert-FaintWalk,SS=FallSide-Stand,ST=FallSide-<br>Sit,SF=FallSide-FaintSit|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|TABLE III.HMM BASED CONFUSION MATRIX FOR15ACTIVITIES USING KFALL DATASET||||||||||||||||
||**BS**|**BF**|**BL**|**TF**|**FS**|**FT**|**FJ**|**FF**|**FW**|**TW**|**SW**|**VF**|**SS**|**ST**|**SF**|
|**BS**|**76**|0|0|0|1|9|0|0|13|0|0|1|0|0|0|
|**BF**|0|**100**|0|0|0|0|0|0|0|0|0|0|0|0|0|
|**BL**|0|0|**99**|0|0|0|0|0|0|0|0|0|1|0|0|
|**TF**|0|0|0|**88**|0|0|0|0|0|0|0|0|1|11|0|
|**FS**|1|0|0|0|**92**|0|0|0|4|0|0|1|0|2|0|
|**FT**|0|0|0|7|1|**81**|0|0|8|0|0|3|0|0|0|
|**FJ**|0|0|0|0|0|0|**99**|1|0|0|0|0|0|0|0|
|**FF**|0|0|0|0|0|0|0|**98**|0|1|0|0|0|0|1|
|**FW**|0|0|0|0|0|4|0|0|**96**|0|0|0|0|0|0|
|**TW**|0|0|0|0|0|0|0|0|0|**100**|0|0|0|0|0|
|**SW**|0|0|0|0|0|0|0|0|0|0|**99**|0|1|0|0|
|**VF**|0|0|0|0|0|0|0|0|0|0|1|**98**|0|1|0|
|**SS**|0|0|0|2|0|0|0|0|0|0|0|0|**98**|0|0|
|**ST**|0|0|0|0|2|1|0|0|0|0|3|2|0|**92**|0|
|**SF**|0|1|0|0|0|9|0|0|0|0|0|0|0|0|**90**|
|**Accuracy:                                                             0.937**||||||||||||||||



Authorized licensed use limited to: Hanoi University of Science & Technology. Downloaded on June 14,2026 at 13:22:15 UTC from IEEE Xplore.  Restrictions apply. 

TABLE IV. ACCURACY COMPARISON BETWEEN PROPOSED AND EXISTING 

|HAR M|ODELS|
|---|---|
|**Methods**|**Recognition Accuracy (%)**|
|[24]|84.89|
|[25]|89|
|[26]|89.37|
|**Proposed approach **|**93.7**|



## _B. Experimental Validation:_ 

This study has studied experimental findings. The report of the classification accuracy is provided in Table II, whereas the confusion matrix generated with the use of KFall dataset is shown in Table III. Table IV presents a comparative evaluation with traditional solutions on fall detection systems. 

## IV. CONCLUSION 

This paper suggested an Activity Recognition system that involved fall detection with the aid of sensor data (wearable sensors). We applied the KFall dataset that was freely available and contained labeled time-series data. Based on the captured signals, accelerometer and gyroscope measurements were solely chosen among others since the data should be efficient, and motion-related features should be targeted. The first stage was the use of the preprocessing method of filtering and windowing. There were five features we extracted using windowed data. Then, we used the Cuckoo Search Optimization algorithm to point out the most relevant features, to use them as classification, and essentially reduce the data dimensions. Subsequently, Hidden Markov Models (HMMs) as classifiers were used, with each activity trained on a distinct model in order to capture temporal dynamics over 15 classes related to fall activities. The results determined that the approximate accuracy of the classification in our system was 93.7%, proving its efficiency as a method of modeling consequential human activity data. 

To increase the accuracy, in the future we will be able to add additional types of sensors, build complex hierarchies of features derived after training, and employ current deep hybrid models. These extensions can also enhance the HAR systems in applications such as elderly fall prevention applications, health monitoring, and smart healthcare. 

## REFERENCES 

- [1] J. Zhao _et al._ , "Physical activity and the risk of developing 8 age-related diseases: epidemiological and Mendelian randomization studies," _Eur. Rev. Aging Phys. Act._ , vol. 21, no. 24, Sep. 2024. 

- [2] Z. Ungvari _et al._ , "The multifaceted benefits of walking for healthy aging: from Blue Zones to molecular mechanisms," _GeroScience_ , vol. 45, pp. 3211–3239, Jul. 2023. 

- [3] M. B. Pinheiro _et al._ , "Impact of physical activity programs and services for older adults: a rapid review," _Int. J. Behav. Nutr. Phys. Act._ , vol. 19, Art. no. 87, Jul. 2022. 

- [4] T. S. Qureshi _et al._ , "A systematic literature review on human activity recognition using smart devices: advances, challenges, and future directions," _Artif. Intell. Rev._ , vol. 58, Art. no. 276, Jun. 2025. 

- [5] G. Mu, Y. Zhang, Z. Yan, Q. Yu, and Q. Wang, "Recent advancements in wearable sensors: integration with machine learning for human– machine interaction," _RSC Adv._ , vol. 15, pp. 7844–7854, Mar. 2025. 

- [6] J. Kim, K. Lee, and J. Jeon, "Systematic literature review of wearable devices and data analytics for construction safety and health," _Expert Syst. Appl._ , vol. 257, Art. no. 125038, Dec. 2024. 

- [7] G. Biagetti, P. Crippa, L. Falaschetti, S. Orcioni, and C. Turchetti, "Human activity monitoring system based on wearable sEMG and accelerometer wireless sensor nodes," _BioMedical Engineering OnLine_ , vol. 17, Art. no. 132, Nov. 2018. 

- [8] E. Bulbul, A. Çetin, and İ. A. Doğru, "Human Activity Recognition Using Smartphones," in _Proc. 2018 2nd Int. Symp. Multidisciplinary Studies and Innovative Technologies (ISMSIT)_ , Ankara, Turkey, pp. 1– 5, Oct. 2018. 

- [9] H. D. Nguyen, K. P. Tran, X. Zeng, L. Koehl, and G. Tartare, "Wearable Sensor Data Based Human Activity Recognition using Machine Learning: A new approach," _arXiv preprint_ arXiv:1905.03809, May 2019. 

- [10] V. Bijalwan, V. B. Semwal, and V. Gupta, "Wearable sensor-based pattern mining for human activity recognition: deep learning approach," _Industrial Robot: The International Journal of Robotics Research and Application_ , vol. 49, no. 1, pp. 132–143, Jan. 2022. 

- [11] A. Abedin, M. Ehsanpour, Q. Shi, H. Rezatofighi, and D. C. Ranasinghe, "Attend and Discriminate: Beyond the State-of-the-Art for Human Activity Recognition Using Wearable Sensors," _Proc. ACM Interact. Mob. Wearable Ubiquitous Technol._ , vol. 5, no. 1, Art. no. 1, pp. 1–22, Mar. 2021. 

- [12] Y. J. Luwe, C. P. Lee, and K. M. Lim, "Wearable Sensor-Based Human Activity Recognition with Hybrid Deep Learning Model," _Informatics_ , vol. 9, no. 3, Art. no. 56, Jul. 2022. 

- [13] Z. Chen, L. Teng, L. Xu, J. Yu, and J. Liang, "MP-HAR: A Novel Motion-Powered Real-Time Human Activity Recognition System," _IEEE Internet of Things Journal_ , vol. 11, no. 5, pp. 7652–7663, Mar. 2024 

- [14] T. F. N. Bukht, A. Alazeb, N. Almudawi, H. Liu, and others, "Robust Human Interaction Recognition Using Extended Kalman Filter," _Computers, Materials & Continua_ , vol. 81, no. 2, pp. 2987–3002, Nov. 2024. 

- [15] A. Dehghani, O. Sarbishei, T. Glatard, and E. Shihab, "A Quantitative Comparison of Overlapping and Non-Overlapping Sliding Windows for Human Activity Recognition Using Inertial Sensors," _Sensors_ , vol. 19, no. 22, Art. no. 5026, Nov. 2019. 

- [16] M. Bennasar, B. A. Price, D. Gooch, A. K. Bandara, and B. Nuseibeh, "Significant features for human activity recognition using tri-axial accelerometers," _Sensors_ , vol. 22, no. 19, Art. no. 7482, Oct. 2022. 

- [17] B. A. Atalaa, I. Ziedan, A. Alenany, and A. Helmi, "Feature engineering for human activity recognition," _International Journal of Advanced Computer Science and Applications (IJACSA)_ , vol. 12, no. 2, pp. 206–214, 2021. 

- [18] E. C. Dinarević, J. B. Husić, and S. Baraković, “Step by step towards effective human activity recognition: A balance between energy consumption and latency in health and wellbeing applications,” _Sensors_ , vol. 19, no. 23, p. 5206, Nov. 2019. 

- [19] F. Nazar and A. Jalal, "Wearable Sensor-Based Activity Recognition Over Statistical Features Selection and MLP Approach," in _Proceedings of the 2025 IEEE Emerging Trends in Electrical, Computer and Technology Engineering (ETECTE)_ , Islamabad, Pakistan, pp. 1–7, Apr. 2025. 

- [20] F. Nazar and A. Jalal, "Wearable Sensors-based Activity Classification for Intelligent Healthcare Monitoring," in _Proc. IEEE Int. Conf. Adv. Comput. Sci. (ICACS)_ , Islamabad, Pakistan, pp. 1–7, Feb. 2025. 

- [21] E. Neelima and M. S. P. Babu, "Genome feature optimization and coronary artery disease prediction using cuckoo search," _Comput. Sci. Inf. Technol._ , vol. 1, no. 3, pp. 106–115, Nov. 2020. 

- [22] T. Xue and H. Liu, "Hidden Markov Model and its application in human activity recognition and fall detection: A review," in _Proc. 10th Int. Conf. Commun., Signal Process., and Syst. (CSPS)_ , Changbaishan, China, Oct. 2021. 

- [23] X. Yu, J. Jang, and S. Xiong, "A large-scale open motion dataset (KFall) and benchmark algorithms for detecting pre-impact fall of the elderly using wearable inertial sensors," _Front. Aging Neurosci._ , vol. 13, Art. no. 692865, Jul. 2021. 

- [24] N. De Raeve, A. Shahid, M. de Schepper, E. De Poorter, I. Moerman, J. Verhaevert, P. Van Torre, and H. Rogier, “Bluetooth-Low-EnergyBased Fall Detection and Warning System for Elderly People in Nursing Homes,” _J. Sensors_ , vol. 2022, Art. no. 9930681, Jan. 2022. 

- [25] S. N. Moutsis _et al._ , "PIPTO: Precise Inertial-Based Pipeline for Threshold-Based Fall Detection Using Three-Axis Accelerometers," _Sensors_ , vol. 23, no. 18, Art. no. 7951, Sep. 2023. 

- [26] D. A. Nguyen _et al._ , “Towards a New Multi-tasking Learning Approach for Human Fall Detection,” in _Proc. 12th Conf. Information Technology and Its Applications (CITA 2023)_ , Lecture Notes in Networks and Systems, vol. 734, Springer, pp. 50–61, Jul. 2023. 

Authorized licensed use limited to: Hanoi University of Science & Technology. Downloaded on June 14,2026 at 13:22:15 UTC from IEEE Xplore.  Restrictions apply. 

