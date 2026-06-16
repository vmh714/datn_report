### Tóm tắt:
Bài báo giới thiệu bộ dữ liệu FallAllD, một nguồn dữ liệu mở lớn về hoạt động hằng ngày và các vụ ngã của con người phục vụ học máy và học sâu. Nghiên cứu phân tích các hạn chế của các bộ dữ liệu hiện hành như dải đo hẹp, tần số lấy mẫu thấp và thiếu kịch bản thực tế. Bằng việc thu thập dữ liệu từ ba thiết bị đeo ở các vị trí khác nhau, FallAllD cung cấp một môi trường thử nghiệm đa dạng hơn. Thử nghiệm trên các thuật toán cho thấy bộ dữ liệu này giúp đánh giá chính xác hơn khả năng hoạt động thực tế của hệ thống phát hiện té ngã.

### BibTeX:
```bibtex
@article{saleh2021fallalld,
  author={Saleh, Majd and Abbas, Manuel and Le Bouquin Jeannès, Régine},
  journal={IEEE Sensors Journal},
  title={FallAllD: An Open Dataset of Human Falls and Activities of Daily Living for Classical and Deep Learning Applications},
  year={2021},
  volume={21},
  number={2},
  pages={1849-1858},
  doi={10.1109/JSEN.2020.3018335}
}
```

---

## NỘI DUNG BÀI BÁO CHI TIẾT

IEEE SENSORS JOURNAL, VOL. 21, NO. 2, JANUARY 15, 2021 

1849 

## FallAllD: An Open Dataset of Human Falls and Activities of Daily Living for Classical and Deep Learning Applications 

Majd Saleh , Manuel Abbas, and Régine Le Bouquin Jeannès , Member, IEEE 

_**Abstract—In the last two decades, a wide variety of wearable fall detection systems have been proposed. Most of them were based on machine learning. While the reported results give the impression that the problem is almost solved, crucial questions raise about the representation capacity of the considered datasets and accordingly the reliability of performance evaluation.In this article, the limitations of a multitude of state-of-the-art fall detection datasets are discussed. Particularly, limitations related to the sensors that are used to capture the motion signals, the positions of these wearable sensors, the sampling frequency and the measurement range are discussed. Moreover, limitations concerning the simulation protocol e.g. the considered types of falls are discussed. A comprehensive data acquisition system and simulation**_ 

_**protocol are proposed to overcome these limitations. Consequently, a large dataset, namely FallAllD, is proposed. It consists of**_ **26 420** _**files collected using three data-loggers worn on the waist, wrist and neck of the subjects. Motion signals are captured using an accelerometer, gyroscope, magnetometer and barometer with efficient configurations that suit the potential applications. The performance of deep learning and classical learning-based algorithms is evaluated on the proposed dataset as well as some reference datasets. The results show significant performance differences when considering different datasets. The reasons underlying these differences are discussed and the advantages of FallAllD are highlighted. Moreover, challenges of acceleration-based fall detection are deeply analyzed. This analysis reveals the main reasons underlying false positives and false negatives. FallAllD could be used in fall detection, fall prevention and human activity recognition contexts.**_ 

_**Index Terms— Dataset, deep learning, elderly health-care, fall detection, human activity recognition, machine learning, wearable sensors.**_ 

## I. INTRODUCTION 

HE importance of fall detection systems for the elderly **T** raises from the fact that the faster a medical intervention takes place, the higher the possibility of avoiding serious consequences of falls. Fall detection systems could be divided into 

Manuscript received July 25, 2020; revised August 16, 2020; accepted August 17, 2020. Date of publication August 20, 2020; date of current version December 16, 2020. This work was supported in part by the European Union through the European Regional Development Fund (ERDF), in part by the Ministry of Higher Education and Research, in part by the French Region of Brittany and Rennes Métropole, and in part by the French National Research Agency (ANR) in the context of the ACCORDS Project under Grant ANR-17-CE19-0024-01. The associate editor coordinating the review of this article and approving it for publication was Dr. Edward Sazonov. (Corresponding author: Majd Saleh.) 

The authors are with the LTSI–UMR 1099, Inserm, Université de Rennes 1, 35000 Rennes, France (e-mail: majd.saleh@univ-rennes1.fr; manuel.abbas@univ-rennes1.fr; regine.le-bouquin-jeannes@ univ-rennes1.fr). 

Digital Object Identifier 10.1109/JSEN.2020.3018335 

ambient and wearable ones. The former class is restricted to indoor usage while the latter has the advantage of accompanying the elderly all the time indoors and outdoors. In this article, wearable fall detection devices are considered. The sensors that are typically used in these devices are explored hereafter. 

The brilliant technology of Micro-Electro-Mechanical Systems (MEMS) enabled to produce a variety of sensors, e.g. accelerometers and gyroscopes, in small-size and light-weight packages. Nowadays, these MEMS-based sensors are widely used in wearable devices. In the context of fall detection and human activity recognition, accelerometers are the most widely used sensors thanks to their low power consumption and their ability to capture the body movements meaningfully. For instance, Saleh _et al_ . [1] recently proposed an accelerationbased fall detection algorithm for wrist worn devices. They showed that acceleration-based solutions could achieve very high accuracy if a large set of complicated features is used. However, they showed that such kind of solutions could not be 

1558-1748 © 2020 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information. 

Authorized licensed use limited to: Hanoi University of Science & Technology. Downloaded on April 02,2026 at 01:53:57 UTC from IEEE Xplore.  Restrictions apply. 

IEEE SENSORS JOURNAL, VOL. 21, NO. 2, JANUARY 15, 2021 

1850 

embedded in wearables since these latter have limited computational resources and limited battery capacity. Wang _et al_ . [2] proposed a fall detector based on accelerometer and barometer. Despite its quite low power consumption (about two years of autonomy), the specificity of this fall detector was only 87 _._ 3% when evaluated on unseen test set. Sabatini _et al_ . [3] used three sensors in their fall detector. They designed an extended Kalman filter to fuse the measurements of accelerometer and gyroscope in order to estimate the orientation of the wearable device. Given the estimated orientation, the static gravity acceleration is canceled and the vertical dynamic acceleration is estimated. This latter is fused with the barometric altimeter output using a complementary filter in order to estimate the vertical velocity and the height of the user. Their fall detection algorithm is based on the last two quantities. Pierleoni _et al_ . [4] used four sensors in their fall detector. Particularly, they first use Madgwick sensor fusion algorithm [5] in order to estimate the orientation of the wearable device using accelerometer, gyroscope and magnetometer. The orientation of the wearable device is used to recognize the vertical component of the acceleration in the Earth frame. This vertical acceleration is fused with the measured pressure to estimate the altitude of the user which is in turn used by the fall detection algorithm. To sum up, researchers were generally interested in one or more of the following sensors: accelerometer, gyroscope, magnetometer and barometer as tools to capture the body movements. 

From methodological point of view, a multitude of fall detection algorithms have been proposed in the last two decades. Some of them are threshold-based like [3], [4] while the majority are machine learning-based like [1], [2], [6]–[9] to cite a few. Thresholds in threshold-based methods are defined depending on the available data. Similarly, the whole training process in machine learning-based methods depends on the available data. Clearly, the need for a representative dataset is essential. 

Nowadays, a multitude of fall detection datasets are publicly available. Casilari _et al_ . [10] conducted an interesting study on more than 10 public datasets for wearable fall detection systems. They summarized and compared the characteristics of these datasets in terms of the positions of the wearable sensing units and the types of sensors that were used to capture the body movement. They also compared the types of falls and activities of daily living (ADLs) that are considered in these datasets. The aforementioned characteristics are considerably different across those datasets. Before discussing the limitations of the state-of-the-art datasets, a reference protocol for evaluating fall detectors is introduced. 

Noury _et al_ . [11] conducted a detailed study on the performance evaluation of fall detectors. They spotted the light on the difficulties of comparing the results when evaluating fall detection systems in the absence of a common evaluation benchmark. They proposed an important protocol for simulating falls and ADLs. Some main aspects of this protocol are: 1) it considers forward, backward and lateral falls as well as falls caused by syncope, 2) falls should be simulated in two scenarios: with/without recovery, 3) fall simulations should consider the presence and absence of rotation while falling, 

and 4) for more realistic simulation, subjects have the option to avoid any type of falls or ADLs if it is not convenient for them. This study is the cornerstone of our proposed protocol that will be discussed later. 

In this article, we first explain the limitations of the stateof-the-art datasets in Section II where we define the factors to be considered for building a realistic dataset. In Section III, we explore the proposed data acquisition system where the considered sensors and their configurations are explored. A comprehensive fall and ADL simulation protocol is proposed in Section IV. Following the proposed protocol, 15 subjects accepted to simulate the falls and ADLs which resulted in a large dataset, namely FallAllD. This dataset is described in the same Section IV. In order to experimentally validate our claims regarding the limitations and drawbacks of the state-of-the-art datasets, Section V is devoted to a comparative study between the results of classical machine learning and deep learning algorithms on FallAllD dataset and two reference ones. Section VI continues this validation where the effect of sampling frequency and measurement range on classification performance is analyzed in the context of acceleration-based fall detection. The distribution of false negatives and false positives over the types of falls and ADLs, respectively, is studied also in Section VI where the objective is to show the most challenging falls to detect and the most confusing ADLs. A technical description of FallAllD dataset is briefly explored in Section VII while Section VIII concludes the paper and discusses some potential future works. 

II. THE STATE-OF-THE-ART DATASETS FOR FALL 

DETECTION SYSTEMS: LIMITATIONS AND DRAWBACKS 

In the introduction, the need for a representative, thus realistic, dataset of human falls and ADLs was tackled. Indeed, a representative dataset should satisfy two conditions: 1) the body motion is well captured by the wearable sensors, and 2) the possible types of falls and ADLs that could occur in real world conditions are covered. 

Starting by the first condition, measurement range and sampling frequency of the considered sensors play an important role in the data acquisition system. Some reference datasets were acquired with _Fs_ = 5 Hz [12] and _Fs_ = 20 Hz [13]. When using such low sampling frequencies, some local features in the activity signal are lost. This limitation could affect the task of discriminating falls from ADLs. Classification accuracy as a function of sampling frequency will be explained in Section VI-A in the context of accelerationbased fall detection. Regarding the measurement range, some datasets like [12], [14]–[16] adopted a small measurement range of acceleration, numerically ±2 g only. Since the accelerometers used in these datasets are capacitive MEMS ones, i.e. they measure both the static acceleration of the Earth gravity (1 g) and the dynamic acceleration of the body movement, it is highly expected to face the saturation acceleration even with common ADLs. This could introduce a higher confusion between falls and ADLs for classifiers and thus the classification accuracy could be reduced. This claim will be proven in Section VI-B where the classification accuracy as a function of acceleration measurement range is studied. 

Authorized licensed use limited to: Hanoi University of Science & Technology. Downloaded on April 02,2026 at 01:53:57 UTC from IEEE Xplore.  Restrictions apply. 

SALEH et al.: FALLALLD: OPEN DATASET OF HUMAN FALLS AND ACTIVITIES OF DAILY LIVING 

1851 

Regarding the second condition, most datasets do not cover the possible types of falls and ADLs. For instance, in real world conditions, an elderly person could recover after falling down. Nevertheless, some serious consequences could occur even if the subject feels fine. Particularly, some subdural hematoma might happen with an elderly person because of a minor trauma like falling out of a chair especially if he/she takes medications that thin the blood [17], [18]. As mentioned in the introduction, Noury _et al_ . [11] recommended to consider falls with recovery when evaluating the performance of fall detectors. Indeed, the significance of considering falls followed by recovery is twofold: 1) it enables the medical team to be aware about a potential subdural hematoma from the early period of falling and consequently to make the necessary interventions, and 2) this feature makes the fall detection algorithm more robust against slight movements (not only recovery) that could occur after the user falls down. Falls followed with recovery have not been considered in the state-of-the-art datasets like [12], [13], [19]. In addition, some datasets consider quite limited types of falls and ADLs like [12], [13]. 

From acceptability point of view, people could prefer wristworn, neck-worn or waist-worn devices. Some datasets considered only waist-worn devices like [12], [19] which is another limitation. 

With a simplified dataset, very high classification accuracy could be achieved. However, such a high accuracy does not necessarily reflect the performance in real world conditions. Indeed, in Section V, we show how easy a 98% accuracy is achievable on some reference datasets. 

The objective of the current work is to propose a dataset that overcomes the aforementioned limitations and drawbacks. The proposed data acquisition system and simulation protocol are discussed in detail in the following two sections. 

## III. THE PROPOSED DATA ACQUISITION SYSTEM 

Three identical data-loggers developed by our partner society RF-TRACK were used to acquire the motion signals. Participants in activity simulations simultaneously wore the three devices on their neck, wrist and waist. Please note that the proposed dataset FallAllD is not intended for a fall detection system that simultaneously uses several spatially distributed devices to detect falls. Instead, it is intended to be used in a fall detection system that depends only on one device worn either on the waist, the neck or the wrist of its user. Clearly, it could be also used in a position-invariant fall detection system. Each data-logger is equipped with the inertial module LSM9DS1 which contains: 1) a 3-axial accelerometer configured such that the sampling frequency _Fs[a]_[=][238][Hz] and the measurement range is ±8 g, 2) a 3-axial gyroscope configured such that the sampling frequency _Fs[g]_[=][ 238 Hz and] the angular rate is ±2000 dps and 3) a 3-axial magnetometer configured such that the sampling frequency is _Fs[m]_ = 80 Hz and the full scale magnetic field is ±4 Gauss. In addition, each data-logger is equipped with the MS5607-02BA03 barometer configured with a sampling frequency _Fs[b]_ = 10 Hz. It measures the air pressure as well as the temperature. Dataloggers use the micro-controller MSP430F5528 made by Texas 

**==> picture [232 x 286] intentionally omitted <==**

Fig. 1. a) positions of wearable data-loggers, b) the printed circuit of a data-logger, c) motion signals of a backward fall caused by a slip and followed by recovery captured using 3-axial accelerometer, 3-axial gyroscope, 3-axial magnetometer and a barometer. 

Instruments. The positions of the wearable data-loggers, their printed circuit and an example showing the signals acquired using the 4 sensors of a neck-worn device are illustrated respectively in sub-figures a,b and c of Figure 1. In the given example, the subject was walking for the first 9 seconds. The cyclic activity is clear in the acceleration signal. We also note that the mean value of the component _ax_ of acceleration is about 1 g. Indeed, _ax_ corresponds to the direction of the Earth gravity field when the subject is walking. Since the used accelerometer is a MEMS capacitive one, it responds to the static acceleration of the Earth gravity and the dynamic one caused by the body movement which explains why _ax_ ≈ 1 g. Right after the 9 _[th]_ second, the subject slipped and rotated then fell down backward on the ground. The impact shock is clear around the 10 _[th]_ second in the acceleration signal. The subject stayed inactive for about 3 seconds. During the inactivity period, the mean value of the pressure signal is clearly higher compared to the pre-fall phase. This means that the altitude of the device is lower in the inactivity phase than in the pre-fall phase. At the 14 _[th]_ second, the subject succeeded to recover and continued walking. In the next section, the simulation protocol is described in detail. 

## IV. THE PROPOSED FALL AND ADL SIMULATION PROTOCOL 

The proposed simulation protocol follows the recommendations of Noury _et al_ . [11] with three major extensions: 1) it systematically covers all possible types of falls, 2) it 

Authorized licensed use limited to: Hanoi University of Science & Technology. Downloaded on April 02,2026 at 01:53:57 UTC from IEEE Xplore.  Restrictions apply. 

IEEE SENSORS JOURNAL, VOL. 21, NO. 2, JANUARY 15, 2021 

1852 

**==> picture [397 x 122] intentionally omitted <==**

Fig. 2. The systematic way of considering all the possible scenarios of falling in the proposed dataset FallAllD. 

does not only consider fall detector evaluation problem (in which it is statistically sufficient to collect about 600 data points [11]) but importantly, it targets the machine learningbased fall detection in which higher number of data samples are required to avoid over-fitting and hence to improve the generalization capability of trained machines, and 3) falls followed by recovery are considered as positive samples rather than negative ones. In other words, the fall detector should send an alarm even if the subject succeeded to recover after falling. This is because of the potential risks related to subdural hematoma [17], [18] that have been introduced in Section II. 

In order to systematically cover the possible types of falls, we first consider the posture of the subject before falling down. Precisely, we distinguish between falls that occur while the subject is inactive (standing, sitting or lying) and while he is moving (walking, jogging or attempting to sit/lie down). A multitude of possible reasons of falls are covered in the simulations. Particularly, slip, trip, syncope, loss of balance and rotation while lying are taken into account. All possible directions (the fact from which the name FallAllD is derived) are considered. For instance, slipping while walking could occur in six directions: forward/backward, with/without rotation where rotation could be to the left or to the right. In contrast, tripping while walking normally occurs forward without rotation. Figure 2 summarizes the proposed rules of simulating falls. As shown in this figure, most types of falls end with lying except for some slow falls caused by syncope in which the subject tries to protect himself / herself by resorting to an object, e.g. a wall, and could end with sitting. All types of falls except for those caused by syncope are simulated in two scenarios: with and without recovery. The total number of the considered fall types is 35. They are detailed in Figure 8. For realistic simulation, no mattresses are used to protect the subjects because such dampening tools could affect the motion signals, especially the impact shock captured by the accelerometer. Instead, a body protection equipment is used as illustrated in Figure 3. It consists of a helmet, a jacket with arm protection, knee pads and a protection for the back. Regarding the ADLs, the proposed protocol distinguishes between two major types: cyclic ADLs e.g. walking and jogging and transient ADLs e.g. sitting down and lying down. The starting and ending phases of the cyclic ADLs are also segmented and considered as transient ADLs e.g. stop walking. Indeed, the transient phases of cyclic activities are expected to 

**==> picture [245 x 129] intentionally omitted <==**

Fig. 3. Body protection equipment used when collecting the proposed dataset FallAllD. 

show higher confusion with falls and thus it is useful to train machines to discriminate between falls and these confusing ADLs. Moreover, by assigning these ADLs to separate types, the reasons underlying false positives could be analyzed in more detail. ADLs related to using the lifts and using public transportation are also considered. The total number of ADLs types is 44. Twelve of them are related to activities practiced by hand e.g. clapping hands, and they concern only the wristworn device. Figure 4 shows all the considered types of ADLs. Simulations were executed by 15 subjects (8 males and 7 females). The ranges of their ages, weighs and heights are [21 → 53] years, [48 → 85] kg and [158 → 187] cm, respectively. The average age, weight and height are 32 years, 67 kg and 171 cm, respectively. As recommended in [11], each subject selected the devices and the activities that are convenient for him. For both waist and neck-worn devices, 14 subjects simulated the ADLs while 12 simulated the falls. For wrist-worn devices, 13 subjects simulated the ADLs while 10 simulated the falls. In total, FallAllD contains 26 420 files. The length of each data file is 20 s. For falls and transient ADLs, files are centered around the transition moment while each cyclic ADL is present in the whole corresponding file. For a better understanding of the fall simulation protocol, note that some videos of a young subject simulating falls are available online alongside the dataset. 

As mentioned in Section III, each data logger is equipped with 4 sensors of different types, namely accelerometer, gyroscope, magnetometer and barometer. Any combination of these sensors can be used to detect falling. Some widely 

Authorized licensed use limited to: Hanoi University of Science & Technology. Downloaded on April 02,2026 at 01:53:57 UTC from IEEE Xplore.  Restrictions apply. 

SALEH et al.: FALLALLD: OPEN DATASET OF HUMAN FALLS AND ACTIVITIES OF DAILY LIVING 

1853 

**==> picture [251 x 239] intentionally omitted <==**

Fig. 4. Types of activities of daily living in the proposed dataset FallAllD. 

used combinations are: {accelerometer}, {accelerometer + barometer} and {accelerometer + gyroscope + barometer}. For the sake of simplicity, we focus on acceleration-based fall detection in the next sections. 

V. MACHINE-LEARNING-BASED FALL DETECTION: A COMPARATIVE STUDY BETWEEN THREE DATASETS 

In this section, a comparative study between the proposed dataset FallAllD and two reference datasets Sisfall [19] and UMA-Fall [13] is conducted in the context of accelerationbased fall detection. For straightforward and fair comparison, only data that are collected using waist-worn devices are considered in this section since Sisfall dataset supports only the waist position. Moreover, tri-axial acceleration data of FallAllD and Sisfall are down-sampled at 20 Hz, i.e. the sampling frequency adopted by UMA-Fall. 

The proposed fall detection algorithms cover two distinct methodologies: 

- 1) Deep Neural Networks (DNN) where the process of feature extraction is automated. Particularly, we propose a deep Convolutional Neural Network (CNN) where both time and space structures of the 3-axial acceleration data are preserved. In addition, a Long Short-Term Memory (LSTM) recurrent neural network and a stacked autoencoder (SAE) are proposed. 

- 2) Classical machine learning methods applied to simple statistical features. Particularly, mean, standard deviation and range are calculated for each component { _x, y, z_ } of the acceleration signal leading to a 9-component features vector. The considered classical methods are: a _shallow_ feed-forward Multi-Layer Perceptron (MLP), a Support Vector Machine (SVM) with linear and quadratic kernels, a _k_ -Nearest Neighbors ( _k_ -NN) classifier and a Random Forest classifier [20]. 

The architecture of the proposed CNN is illustrated in Figure 5. It is a simple sequential model with 2 convolutional layers separated by a max-pooling layer. The output of the second convolutional layer is flattened and fed to a fully connected layer. The proposed LSTM-based model has two LSTM layers. The number of hidden units in these layers is 32 and 64, respectively. The output of the second layer is fed to a dense layer that consists of two neurons. The proposed SAE-based classifier is illustrated in Figure 6 where three identical channel-wise convolutional autoencoders are used to learn a representation of each acceleration channel { _ax, ay, az_ }. The main building block is a one dimensional convolutional layer with kernel size = 7. The number of filters in each layer is shown in Figure 6-A. Once an autoencoder is trained, the encoder part is separated to be used by a classification system. Its task is to extract the learned discriminant features from the input signal. These features are then supplied to a dense classifier as shown in Figure 6-B. The length of the input signals in the proposed CNN and LSTM is 260 = 13 s ×20 Hz. Similarly, the length of the input signals in the proposed SAE is 256 = 12 _._ 8 s ×20 Hz. In practice, this corresponds to the size of the sliding window when the proposed schemes work online i.e. acceleration samples in the last 13 seconds are buffered to be supplied to the fall detection algorithm. Note that the size of the sliding window could have a significant impact on the results. On the one hand, a too long sliding window could contain random activities that could confuse the classifier. On the other hand, a too short sliding window could not be able to capture all the phases of falls. The proposed size (around 13 seconds) is not too large while it is sufficient to capture all the phases of a fall i.e. pre-fall, free-fall, impact shock, body adjustment and post-fall phases. 

Regarding the configurations of the classical machine learning classifiers, the MLP consists of two hidden layers with 15 and 2 neurons, respectively. Its activation function is the logistic sigmoid _f (x)_ = 1 _/(_ 1+ _exp(_ − _x))_ . The _k_ -NN classifier is configured to _k_ = 3. Finally, the depth of trees in the random forest is set to 2. 

Table I shows the experimental results of evaluating the aforementioned methods on the FallAllD, Sisfall and UMAFall datasets in terms of balanced accuracy i.e. the average between sensitivity and specificity. Note that all these datasets are unbalanced since they contain more ADLs than falls. Therefore, balanced accuracy is more expressive than accuracy. For realistic evaluation, a leave-one-subject-out cross validation is adopted to evaluate the performance. It is better than randomizing the data and applying k-fold cross validation since the adopted method ensures that all the activities of the subject on which we are evaluating the performance are completely unseen by the machine. This also enables to investigate whether classification performance is subject dependent or not as we will see in sub-section VI-C. Starting by the simplest classifier i.e. the linear SVM, the classification accuracy exceeds 95% on Sisfall and UMA-Fall datasets. Recalling that the extracted features are also quite simple, this reveals that the classification problem with those two datasets is not challenging. However, this does not mean that the fall detection problem itself is easy since with more realistic 

Authorized licensed use limited to: Hanoi University of Science & Technology. Downloaded on April 02,2026 at 01:53:57 UTC from IEEE Xplore.  Restrictions apply. 

IEEE SENSORS JOURNAL, VOL. 21, NO. 2, JANUARY 15, 2021 

1854 

TABLE I 

BALANCED ACCURACY OF SEVERAL MACHINE LEARNING METHODS EVALUATED ON THREE DATASETS: FALLALLD, SISFALL AND UMA-FALL 

**==> picture [345 x 45] intentionally omitted <==**

**==> picture [251 x 262] intentionally omitted <==**

Fig. 5. The proposed convolutional neural network for accelerationbased fall detection with Fs = 20 Hz: CNN Model-1 

simulations, i.e. with FallAllD, the accuracy achieved by this linear SVM is less than 85%. In addition, Table I shows that the accuracy exceeds 98% for Sisfall and UMA-Fall when applying the _k_ -NN and MLP, respectively, to the considered features. However, the best accuracy achieved on FallAllD using classical machine learning methods is 90 _._ 10% (using the random forest classifier). Hence, more complicated features are required to represent the realistic activities in FallAllD. In fact, when we consider more types of falls and ADLs, the probability of having ambiguity between these two classes (Fall/ADL) becomes higher and thus the classification task becomes more difficult. This explains why the results on the FallAllD dataset, which considers a wide variety of falls and ADLs, are lower than the results on the two reference datasets. 

Now let us discuss the results of the deep neural networks. On the FallAllD dataset, the CNN and the SAEbased classifiers show comparable results and they outperform all the classical methods, contrary to the LSTM classifier. On the Sisfall dataset, the three considered DNNs show around 99% of accuracy outperforming all the classical methods. On the contrary, most of the considered classical methods outperform the DNNs on the UMA-Fall dataset. Indeed, this result is logical since small-size datasets like UMA-Fall are not suitable for deep learning applications. The best accuracy 

achieved on the FallAllD dataset is around 93%. This shows that the fall detection problem is still challenging for the classifiers explored so far. Moreover, it is expected to have more difficulties with wrist-worn devices since such devices could show more complicated movements than a waist-worn device. To show and explain fall detection challenges, the next section is dedicated to deeply analyze the FallAllD dataset. 

## VI. FALL DETECTION CHALLENGES 

The objective of this section is to show and analyze the challenges of acceleration-based fall detection. Due to the limited computational capacity and limited battery charge of wearable sensors, most fall detection algorithms in the literature use a brief representation of the motion signals i.e. a small set of features are extracted to be used by a classical low-computational-cost classifier. Therefore, despite its powerful classification capacity, deep learning is not a suitable solution for wearable sensors due to embeddability challenges. However, our objective is not to propose an embeddable fall detection algorithm but rather to analyze the challenges of classifying falls and ADLs. In other words, we are interested in investigating the achievable accuracy apart from the model complexity. CNN is a good choice to conduct this analysis thanks to its ability to deal with the whole 2D-data (time × 3 acceleration components) as an input and thus to automate feature extraction. Let us note that fall detection systems that require high computational complexity could be implemented in the same way proposed in our previous work [1] where a simple low-complexity highly-sensitive algorithm is embedded in the wearable device as a first stage of the fall detection system. In case an activity is classified as a fall by this simple embedded system, the latest raw 3D acceleration data e.g. around 1 K Byte for the last 4 seconds with _fs_ = 40 Hz, are sent to a remote server that executes a highly accurate (both sensitive and specific) algorithm to detect falls. In the same way, our proposed CNN-based solution could be used on a server in cooperation with a low-cost highly-sensitive embeddable solution. 

In the analysis conducted in this section, the waist, neck and wrist-worn devices are considered. The effect of sampling frequency is first analyzed. The effect of acceleration measurement range is then studied. Finally, the distribution of false negatives and false positives over the types of falls and ADLs, respectively, is discussed where the goal is to show the most difficult falls to detect and the most confusing ADLs. 

## A. The Effect of Sampling Frequency 

In the previous section, the acceleration signal was downsampled at 20 Hz in order to compare the performance with 

Authorized licensed use limited to: Hanoi University of Science & Technology. Downloaded on April 02,2026 at 01:53:57 UTC from IEEE Xplore.  Restrictions apply. 

SALEH et al.: FALLALLD: OPEN DATASET OF HUMAN FALLS AND ACTIVITIES OF DAILY LIVING 

1855 

**==> picture [433 x 242] intentionally omitted <==**

Fig. 6. The proposed channel-wise convolutional stacked autoencoder for fall detection. A) self supervised learning. B) a dense classifier based on the trained encoders. C) majority voting. 

UMA-Fall dataset in which data are acquired at _Fs_ = 20 Hz. However, when higher sampling frequencies are considered, more local features could be extracted from the data which possibly lead to better classification accuracy. Liu _et al._ [21] have shown that the sampling rate requirements were classifierdependent. When conducted their study on the Sisfall dataset, they have shown that _Fs_ = 22 Hz was sufficient to achieve an accuracy _>_ 97% when using SVM, _k_ -NN, Naïve Bayes and Decision Tree classifiers. This result is consistent with our results shown in Table I. Wang _et al._ [2] proposed a neckworn low-power fall detector equipped with an accelerometer and a barometer. They used the accelerometer in two operating modes: 1) measurement mode where they used _Fs_ = 50 Hz, and 2) low-power mode where _Fs_ = 6 Hz. Their fall detection algorithm is a low-complexity threshold-based one. Despite the relatively high sampling rate in the measurement mode, the sensitivity and specificity of this system are only 93 _._ 0% and 87 _._ 3%, respectively. 

In this section, the classification accuracy is studied for two sampling frequencies _Fs_ ∈{20 _,_ 40} Hz. To conduct this study, the same CNN architecture shown in Figure 5 (namely Model-1) is considered when _Fs_ = 20 Hz. However, a deeper CNN (namely Model-2) is proposed for _Fs_ = 40 Hz. This is because the higher sampling frequency we use, the features extracted by the first convolutional layer will be more local and thus we need a deeper architecture to abstract these features and get more efficient global features. Model-2 is shown in Figure 7. It contains 4 convolutional layers and has 48 _,_ 258 trainable parameters. It is deeper than Model-1 which contains two convolutional layers and has 9 _,_ 858 trainable parameters (around 20% of Model-1 parameters size). 

Table II compares the classification accuracy of Model-1 and Model-2 when applied to acceleration signals with two 

**==> picture [251 x 118] intentionally omitted <==**

Fig. 7. The proposed convolutional neural network for accelerationbased fall detection with Fs = 40 Hz: CNN Model-2. 

TABLE II 

BALANCED ACCURACY OF TWO CNN ARCHITECTURES EVALUATED ON THE FALLALLD DATASET WITH TWO DIFFERENT SAMPLING FREQUENCIES 

**==> picture [149 x 46] intentionally omitted <==**

**==> picture [34 x 46] intentionally omitted <==**

sampling frequencies _Fs_ ∈{20 _,_ 40} Hz. Clearly, for all the considered positions (waist, neck and wrist) Model-1 outperforms Model-2 for _Fs_ = 20 Hz while Model-2 outperforms Model-1 for _Fs_ = 40 Hz. This result confirms what we introduced regarding the need for deeper CNNs with higher sampling frequencies. Moreover, the accuracy is always improved with _Fs_ = 40 Hz. This means that acquiring acceleration data with _Fs_ = 20 Hz, e.g. like in UMA-Fall, is insufficient since it leads to a loss of important local features of the motion signal. Note that using _Fs_ = 40 Hz is still 

Authorized licensed use limited to: Hanoi University of Science & Technology. Downloaded on April 02,2026 at 01:53:57 UTC from IEEE Xplore.  Restrictions apply. 

IEEE SENSORS JOURNAL, VOL. 21, NO. 2, JANUARY 15, 2021 

1856 

**==> picture [505 x 321] intentionally omitted <==**

Fig. 8. Distribution of false negatives and false positives over the fall and ADL types, respectively. Abbreviations in the captions are: F : Forward, B: Backward, L: Lateral, rec: with recovery, rot: with rotation. 

practical for wearable sensors from power consumption point of view. Finally, we note from Table II that classification accuracy is similar for waist and neck-worn devices while it is notably smaller for the wrist-worn devices. This is an expected result since a wrist-worn device moves with higher degrees of freedom than the other two devices. This freedom leads to more complicated movements that could confuse the 

In all analyses in the following sub-sections, Model-2 with _Fs_ = 40 Hz is adopted. 

## B. The Effect of the Acceleration Measurement Range 

In FallAllD, the acceleration measurement range is ±8 g units while in some reference datasets like [12], [14]–[16], the range is only ±2 g. As discussed in Section II, it is highly expected to face the saturation acceleration even with normal ADLs when using a limited measurement range. This phenomenon could considerably affect the classification accuracy. To show the effect of acceleration measurement range on classification performance, acceleration signals in FallAllD are truncated at ±2 g and ±4 g. The Model-2 convolutional network is used to classify the original as well as truncated acceleration signals. Table III shows the results of this comparison. Ranges of ±2 g and ±4 g show similar classification accuracy while this latter clearly increases when the acceleration range is ±8 g. This confirms the need for this ±8 g acceleration range and justifies why we adopted it in FallAllD. 

## TABLE III 

BALANCED ACCURACY EVALUATED ON THE FALLALLD DATASET FOR THREE DIFFERENT MEASUREMENT RANGES OF ACCELERATION 

**==> picture [91 x 46] intentionally omitted <==**

**==> picture [67 x 45] intentionally omitted <==**

C. Distribution of False Negatives and False Positives 

Figure 8 shows the distribution of false negatives (FN) and false positives (FP) over the types of falls and ADLs, respectively. Starting by false positives, we note that for waist, neck and wrist-worn devices, lying down and turning while lying are the main ADLs that are classified as falls. Failing to stand up (collapsing to a chair) is another source of false positives. However, this activity could arguably be considered as a fall if we follow the very general definition by WHO [22]: _“A fall is defined as an event which results in a person coming to rest inadvertently on the ground or floor or other lower level”_ . Jumping and stumbling while walking are also sources of false alarms. Finally, for the wrist-worn device only, beating a table and clapping hands are main sources of false alarms. 

Regarding the sensitivity, Figure 8 shows that higher sensitivity is achieved using neck and waist devices than wrist devices. As we discussed in sub-section VI-A, wrist has 

Authorized licensed use limited to: Hanoi University of Science & Technology. Downloaded on April 02,2026 at 01:53:57 UTC from IEEE Xplore.  Restrictions apply. 

SALEH et al.: FALLALLD: OPEN DATASET OF HUMAN FALLS AND ACTIVITIES OF DAILY LIVING 

1857 

TABLE IV 

FALSE NEGATIVES AND SENSITIVITY: FALLS FOLLOWED BY RECOVERY VS. FALLS NOT FOLLOWED BY RECOVERY 

**==> picture [47 x 46] intentionally omitted <==**

**==> picture [149 x 46] intentionally omitted <==**

more degrees of freedom and it could show more complicated movements than neck and waist. Therefore, wrist is the most challenging position among the considered ones. Now considering only the falls that could be followed by recovery (i.e. excluding the falls caused by syncope), the total number of false negatives and the corresponding sensitivity are summarized in Table IV where two cases are considered: the subject is able / not able to recover after falling. Clearly, higher sensitivity is achieved when falls are not followed by recovery. Particularly, recovery has a notable impact on the sensitivity of wrist-worn devices. Therefore, fall detection problem is more challenging when considering falls followed by recovery. 

The underlying reasons of false negatives could be concluded from Figure 8. Falling from bed and slow falling that occur while the subject is sliding his back over a wall (to protect himself / herself) are difficult to detect. This result holds for all the considered positions of wearable devices. For waist-worn devices, no other types seem to reveal any difficulty while, for neck and wrist-worn devices, backward falls are clearly more challenging than forward ones. 

Figure 9 shows the distribution of false positives and false negatives per subject. Labels “NA” in the _x_ axis indicate that the subject has not simulated the corresponding activities. For instance, the subject number 4 has worn the three devices but has only simulated ADLs. We observe that the performance is subject dependent, e.g. subject number 5 shows a considerably higher number of false positives and false negatives with the neck-worn device than with the waist and wrist-worn devices. On the contrary, subject number 2 shows a higher number of false negatives with the wrist-worn device than with the two other devices. This confirms that leave-one-subject-out cross validation is a good strategy to evaluate the performance. It does not only enable to study the distribution of false decisions per subject but also gives realistic results that reflect the performance of the classifier in real world conditions under the assumption that the sample is sufficiently representative. In order to investigate whether the latter user-dependent performance is related to the age of the user, the following study is conducted. Two age groups have been extracted from the FallAllD dataset: 1) the youngest subjects whose ages are less than 25 years and 2) the oldest subjects whose ages are greater than 45 years. Table V shows the average sensitivity and specificity evaluated on these two groups. Clearly, the results on the two considered groups are very close which reveals that the performance evaluated using the CNN Model-2 on the FallAllD dataset is almost age-independent. 

## VII. TECHNICAL DESCRIPTION OF FALLALLD 

FallAllD contains 26 420 files. These files are stored in comma-separated values (csv) format. We developed two tools 

**==> picture [247 x 175] intentionally omitted <==**

Fig. 9. Distribution of false negatives and false positives over subjects. 

TABLE V 

THE AVERAGE SENSITIVITY AND SPECIFICITY EVALUATED USING THE CNN MODEL-2 ON TWO AGE GROUPS IN FALLALLD: 1) PARTICIPANTS _<_ 25 YEARS OLD, AND 2) PARTICIPANTS _>_ 45 YEARS OLD 

for encapsulating the data. The first is a MATLAB script that converts the dataset into a MATLAB structure stored as a “.mat” file. The structure contains 8 fields {SubjectID, ActivityID, TrialNo, Device, Acc, Gyr, Mag, Bar}. The second tool is a Python script that converts the dataset into a Pandas dataframe stored in hdf (“.h5”) or pickle (“.pkl”) formats. The dataframe has the same fields as the MATLAB structure. Dataset files as well as the two described tools are available on IEEE DataPort on the following link http://dx.doi.org/10.21227/bnya-mn34. 

## VIII. CONCLUSIONS AND FUTURE WORK 

In this article, a new dataset of human falls and activities of daily living, namely FallAllD, was proposed. It overcomes the drawbacks of the state-of-the-art datasets. FallAllD covers a broad spectrum of falls and ADLs. It considers neck, waist and wrist worn fall detectors. Four sensors namely accelerometer, gyroscope, magnetometer and barometer were used and carefully configured to suite the potential applications such as fall detection, fall prevention and human activity recognition. 

The capability of using FallAllD in classical and deep learning applications was validated and the advantages of this dataset were highlighted. Moreover, the challenges of acceleration-based fall detection were analyzed. Currently, FallAllD is used by our team for developing practical fall detection solutions where both classification accuracy and computational complexity, thus embeddability, have to be taken into account. Moreover, the performance of the under-development fall detection algorithms is currently evaluated in real world conditions on 20 elderly subjects in nursing homes. The outcomes of this experimental study are to be published soon. 

Authorized licensed use limited to: Hanoi University of Science & Technology. Downloaded on April 02,2026 at 01:53:57 UTC from IEEE Xplore.  Restrictions apply. 

IEEE SENSORS JOURNAL, VOL. 21, NO. 2, JANUARY 15, 2021 

1858 

## ACKNOWLEDGMENT 

The authors would like to thank Pierre Cherel and Michel Le Mer, with RF-TRACK society, and Pr. Dominique Somme, with CHU-Rennes hospital, for their valuable contributions to this work. 

## REFERENCES 

- [1] M. Saleh, N. Georgi, M. Abbas, and R. L. B. Jeannes, “A highly reliable wrist-worn acceleration-based fall detector,” in _Proc. 27th Eur. Signal Process. Conf. (EUSIPCO)_ , A Coruña, Spain, Sep. 2019. 

   - [18] Y. Tanaka and K. Ohno, “Chronic subdural hematoma–an up-to-date concept,” _J. Med. Dental Sci._ , vol. 60, no. 2, pp. 55–61, 2013. 

   - [19] A. Sucerquia, J. López, and J. Vargas-Bonilla, “SisFall: A fall and movement dataset,” _Sensors_ , vol. 17, no. 12, p. 198, Jan. 2017. 

   - [20] Z. Liu, M. Yang, Y. Yuan, and K. Yan Chan, “Fall detection and personnel tracking system using infrared array sensors,” _IEEE Sensors J._ , vol. 20, no. 16, pp. 9558–9566, Apr. 2020. 

   - [21] K.-C. Liu, C.-Y. Hsieh, S. J.-P. Hsu, and C.-T. Chan, “Impact of sampling rate on wearable-based fall detection systems based on machine learning models,” _IEEE Sensors J._ , vol. 18, no. 23, pp. 9882–9890, Dec. 2018. 

   - [22] World Health Organization. (Jan. 2018). _Falls_ . Accessed: Mar. 23, 2019. [Online]. Available: https://www. who.int/news-room/fact-sheets/detail/falls 

- [2] C. Wang _et al._ , “Low-power fall detector using triaxial accelerometry and barometric pressure sensing,” _IEEE Trans. Ind. Informat._ , vol. 12, no. 6, pp. 2302–2311, Dec. 2016. 

- [3] A. M. Sabatini, G. Ligorio, A. Mannini, V. Genovese, and L. Pinna, “Prior-to- and post-impact fall detection using inertial and barometric altimeter measurements,” _IEEE Trans. Neural Syst. Rehabil. Eng._ , vol. 24, no. 7, pp. 774–783, Jul. 2016. 

- [4] P. Pierleoni _et al._ , “A wearable fall detector for elderly people based on AHRS and barometric sensor,” _IEEE Sensors J._ , vol. 16, no. 17, pp. 6733–6744, Sep. 2016. 

- [5] S. O. H. Madgwick, A. J. L. Harrison, and R. Vaidyanathan, “Estimation of IMU and MARG orientation using a gradient descent algorithm,” in _Proc. IEEE Int. Conf. Rehabil. Robot._ , Zürich, Switzerland, Jun. 2011. 

- [6] M. Saleh and R. L. B. Jeannes, “Elderly fall detection using wearable sensors: A low cost highly accurate algorithm,” _IEEE Sensors J._ , vol. 19, no. 8, pp. 3156–3164, Apr. 2019. 

- [7] M. Saleh and R. Le Bouquin Jeannes, “An efficient machine learningbased fall detection algorithm using local binary features,” in _Proc. 26th Eur. Signal Process. Conf. (EUSIPCO)_ , Rome, Italy, Sep. 2018. 

_**Majd Saleh**_ received the Ph.D. degree in electronic engineering and telecommunications from Al-Baath University, Syria, in 2017. Since 2017, he has been a Postdoctoral Researcher with the Laboratoire Traitement du Signal et de l’Image, Inserm, Université de Rennes 1, France. His research interests include machine learning, pattern recognition, natural language processing, blind source separation, and numerical optimization. He focused on health monitoring, human activity recognition, and biomedical signal processing in the fields of EEG and brain-MRS signal processing. 

- [8] F. Bianchi, S. J. Redmond, M. R. Narayanan, S. Cerutti, and N. H. Lovell, “Barometric pressure and triaxial accelerometry-based falls event detection,” _IEEE Trans. Neural Syst. Rehabil. Eng._ , vol. 18, no. 6, pp. 619–627, Dec. 2010. 

- [9] G. Shi, C. S. Chan, W. J. Li, K.-S. Leung, Y. Zou, and Y. Jin, “Mobile human airbag system for fall protection using MEMS sensors and embedded SVM classifier,” _IEEE Sensors J._ , vol. 9, no. 5, pp. 495–503, May 2009. 

- [10] E. Casilari, J.-A. Santoyo-Ramón, and J.-M. Cano-García, “Analysis of public datasets for wearable fall detection systems,” _Sensors_ , vol. 17, no. 7, p. 1513, Jun. 2017. 

- [11] N. Noury, P. Rumeau, A. K. Bourke, G. ÓLaighin, and J. E. Lundy, “A proposal for the classification and evaluation of fall detectors,” _IRBM_ , vol. 29, no. 6, pp. 340–349, Dec. 2008. 

- [12] A. Wertner, P. Czech, and V. Pammer-Schindler, “An open labelled dataset for mobile phone sensing based fall detection,” in _Proc. 12th EAI Int. Conf. Mobile Ubiquitous Syst., Comput., Netw. Services_ , Coimbra, Portugal, Jun. 2015, pp. 277–278. 

**==> picture [72 x 91] intentionally omitted <==**

_**Manuel Abbas**_ received the Engineering degree in electronics and telecommunications from the Faculty of Engineering, Lebanese University, Branch II, Roumieh, Lebanon, in 2018, and the master’s degree in signal and image processing from the École Centrale de Nantes, France, in 2018. He is currently pursuing the Ph.D. degree with the Laboratoire Traitement du Signal et de l’Image, Inserm, Université de Rennes 1, France. His research interests include health monitoring, telemedicine, machine learning, and data science. 

- [13] E. Casilari, J. A. Santoyo-Ramón, and J. M. Cano-García, “Analysis of a smartphone-based architecture with multiple mobility sensors for fall detection,” _PLoS ONE_ , vol. 11, no. 12, Dec. 2016, Art. no. e0168069. 

- [14] D. Micucci, M. Mobilio, and P. Napoletano, “UniMiB SHAR: A dataset for human activity recognition using acceleration data from smartphones,” _Appl. Sci._ , vol. 7, no. 10, p. 1101, Oct. 2017. 

- [15] C. Medrano, R. Igual, I. Plaza, and M. Castro, “Detecting falls as novelties in acceleration patterns acquired with smartphones,” _PLoS ONE_ , vol. 9, no. 4, Apr. 2014, Art. no. e94811. 

- [16] G. Vavoulas, M. Pediaditis, E. G. Spanakis, and M. Tsiknakis, “The MobiFall dataset: An initial evaluation of fall detection algorithms using smartphones,” in _Proc. 13th IEEE Int. Conf. Bioinf. BioEngineering_ , Chania, Greece, Nov. 2013. 

- [17] Harvard Health. (2019). _Subdural Hematoma, What Is It?_ Accessed: Mar. 23, 2020. [Online]. Available: https://www.health. harvard.edu/a_to_z/subdural-hematoma-a-to-z 

_**Régine Le Bouquin Jeannès**_ (Member, IEEE) received the Ph.D. degree in signal processing and telecommunications from Rennes University, France, in 1991. She is currently a Professor with the Laboratoire Traitement du Signal et de l’Image, (LTSI) Inserm, Université de Rennes 1, and belongs to Centre de Recherche en Information Biomédicale sino-français (CRIBs), a French-Chinese Laboratory associated with the Institut national de la santé et de la recherche médicale (Inserm). Her research interests include biomedical signals processing and modeling in the field of epilepsy and brain connectivity and health monitoring and telecare. 

Authorized licensed use limited to: Hanoi University of Science & Technology. Downloaded on April 02,2026 at 01:53:57 UTC from IEEE Xplore.  Restrictions apply. 

