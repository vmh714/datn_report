### Tóm tắt:
Bài báo nghiên cứu về phương pháp phát hiện té ngã trước khi xảy ra va chạm sử dụng một cảm biến đo lường quán tính duy nhất đeo trên người. Các tác giả đã xây dựng và chia sẻ công khai bộ dữ liệu chuyển động quy mô lớn mang tên FallTL thu thập từ nhiều phân đoạn cơ thể của các đối tượng tham gia. Đồng thời, họ đề xuất mô hình STA-Net với kiến trúc hai nhánh chú ý không gian và thời gian nhằm tối ưu hóa khả năng nhận diện chuyển động từ dữ liệu cảm biến. Thử nghiệm thực tế cho thấy giải pháp này đạt hiệu suất vượt trội và mở ra hướng đi đầy hứa hẹn cho các thiết bị giám sát sức khỏe thông minh.

### BibTeX:
```bibtex
@article{cai2026fall,
  author={Cai, Yize and Chen, Junxin and He, Qiang and Mou, Jun and Camacho, David},
  journal={IEEE Transactions on Neural Systems and Rehabilitation Engineering},
  title={Fall Monitoring With Single IMU: A Large-Scale Dataset and a Novel Dual-Branch Network},
  year={2026},
  volume={34},
  doi={10.1109/TNSRE.2025.3645365}
}
```

---

## NỘI DUNG BÀI BÁO CHI TIẾT

IEEE TRANSACTIONS ON NEURAL SYSTEMS AND REHABILITATION ENGINEERING, VOL. 34, 2026 

287 

## Fall Monitoring With Single IMU: A Large-Scale Dataset and a Novel Dual-Branch Network 

Yize Cai , Junxin Chen , _Senior Member, IEEE_ , Qiang He , _Member, IEEE_ , Jun Mou , _Senior Member, IEEE_ , and David Camacho , _Senior Member, IEEE_ 

_**Abstract**_ **— With the rapid growth of the elderly population, fall accidents have received increasing attention due to their serious health hazards. Pre-impact fall detection (PIFD) based on wearable sensors emerges as a promising approach for proactive fall prevention in healthcare monitoring. In this research, based on Inertial Measurement Units (IMUs), we construct and publicly provide a largescale motion dataset named FallTL, which includes falls and activities of daily living (ADLs) collected from multiple body segments. Furthermore, we develop STA-Net, a novel Spatial-Temporal Attention Network to perform PIFD based on IMU data from a single body segment. STA-Net incorporates a dual-branch architecture: a temporal attention branch that models temporal signal dependencies and a spatial attention branch that captures cross-modality feature interactions, enabling robust representation learning from sensor data. We evaluate STA-Net across three datasets and it achieves advantageous performance and comparable lead time under cross-subject validation, outperforming state-of-the-art baselines. In addition, our analysis further investigates the influence of sensor placement and data modality on detection performance. These results indicate that accurate and robust PIFD is feasible with minimally obtrusive, single-location sensor setups, offering practical implications for wearable fall monitoring systems.** 

Received 31 August 2025; revised 20 November 2025; accepted 10 December 2025. Date of publication 17 December 2025; date of current version 24 December 2025. This work was supported in part by the Fundamental Research Funds for the Central Universities under Grant DUT25YG229, in part by Xiaomi Young Talents Program, in part by the H2020 Training and Mobility Actions (TMA)-Marie Skłodowska-Curie Actions (MSCA)-Doctoral Networks (DN) Toward an Understanding of Artificial Intelligence (TUAI) Project “Toward an Understanding of Artificial Intelligence via a Transparent, Open, and Explainable Perspective” through HORIZON-MSCA-2023-DN-01-01 under Grant 101168344, in part by the Strategic Networking and Development Program funded by the Ministry of Science and ICT through the National Research Foundation of Korea under Grant RS-2023-00267476, in part by the Spanish Ministry of Science, Innovation and Universities under the AIEnhanCed SoluTIons for Autonomous Space Operations and AdVAnced Onboard Guidance NavigaTION and Control (ACTIVATION) Project under Grant PID2024-161963OB-C22, and in part by the Comunidad Autonoma de Madrid through the Cybersecurity and Resilient Artificial Intelligence for the Community of Madrid–Comunidad de Madrid (CIRMA-CAM) Project under Grant TEC-2024/COM-404. _(Corresponding author: Junxin Chen.)_ 

Yize Cai and Junxin Chen are with the School of Software, Dalian University of Technology, Dalian 116621, China (e-mail: junxinchen@ieee.org). Qiang He is with the Computer Science and Engineering, Northeastern University, Shenyang 110004, China. 

Jun Mou is with the School of Information Science and Engineering, Dalian Polytechnic University, Dalian 116034, China. David Camacho is with the School of Computer Systems Engineering, Universidad Politecnica de Madrid, 28031 Madrid, Spain. Digital Object Identifier 10.1109/TNSRE.2025.3645365 

## _**Index Terms**_ **— Pre-impact fall detection, wearable sensors, public dataset, deep learning, attention mechanism.** 

## I. INTRODUCTION 

HE increasing number of elderly individuals living alone **T** has raised significant concerns about their health and safety, with fall accidents being a particularly critical issue [1]. Studies indicate that approximately one-third of adults aged 65 and older experience at least one fall annually [2]. Falls can result in severe injuries or even fatality [3], and delayed medical intervention, especially beyond the critical first hour, can lead to more serious consequences [4]. Therefore, various fall detection systems (FDS) are developed [5]. These systems play a vital role in ensuring timely care and safeguarding the well-being of the elderly. 

FDS are typically categorized into context-aware systems and wearable systems according to the measurement method. Context-aware systems utilize ambient sensors [6] to monitor individual activities. While these systems can achieve high measurement accuracy, their applicability is often limited to indoor environments, with evidence that nearly 50% of falls occur outdoors [7]. In contrast, wearable sensor-based systems [8] offer compelling advantages [9]. Inertial Measurement Units (IMUs) serve as compact, cost-effective instruments capable of continuously capturing body dynamics in real time [10], [11]. Their integration into wearable systems enables low computational cost and precise motion tracking without reliance on external infrastructure [12]. These characteristics position IMU-based wearable FDS as a ideal measurement solution for fall monitoring across diverse real-world conditions. 

IMU-based FDS encompass two primary research directions: post-impact fall detection (FD) and pre-impact fall detection (PIFD). FD focuses on detecting falls by analyzing the comprehensive attributes of the entire fall signals [27], and the primary goal is to identify the occurrence of falls timely and provide assistance [20]. Extensive studies facilitate the development of numerous robust FD algorithms. For instance, Campanella et al. [28] introduce a lightweight feedforward neural network (FFNN) tailored for embedded device, using IMU data from a device placed in the right pocket. The model is trained and tested using both a self-collected dataset with 15 fall types and 19 ADL types and the public SisFall [18] dataset. 

In recent years, researchers have increasingly shifted focus from FD to PIFD, which represents a more proactive approach 

© 2025 The Authors. This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/ 

IEEE TRANSACTIONS ON NEURAL SYSTEMS AND REHABILITATION ENGINEERING, VOL. 34, 2026 

288 

by analyzing attributes solely from the pre-impact phase of fall signals [29]. This enables the activation of protective measures, such as inflatable airbag systems, to mitigate injury severity [30]. The free-fall phase directly reflects the likelihood of falling but includes complex patterns of signals, making it a critical but demanding area of research. For instance, Lin et al. [31] propose a novel dual-task learning (DTL) model based on a modified convolutional neural network (CNN)-long-short term memory (LSTM) model to perform PIFD and terrain classification. The collected dataset includes 16 activities performed by 10 young subjects, and 4 activities performed by 10 elderly subjects. 

Existing studies have explored a wide range of activity types and sensor configurations, often leveraging proprietary datasets tailored to specific experimental setups. However, the diversity in acquisition protocol and limited public availability of these datasets can make it challenging to benchmark approaches consistently and evaluate their generalizability. Moreover, most publicly available datasets are primarily designed for FD task, while public datasets suitable for PIFD task remain scarce. In terms of FDS algorithms, most existing methods rely on handcrafted features or shallow network structure to extract features, which constrains the model’s ability to effectively capture the complex temporal and spatial patterns inherent in IMU signals. Such features are often non-scalable and may fail to generalize well, ultimately limiting detection performance. 

Building upon existing research, we first propose a comprehensive motion simulation protocol and construct a large-scale motion dataset publicly available using self-developed data collection system. This dataset includes IMU signals from eight body segments and is suitable for both PIFD and FD tasks. In addition, we exploit the temporal and spatial characteristics of IMU signals and propose STA-Net, a novel architecture that leverages both temporal and spatial attention mechanisms for detecting falls. 

The main contributions of this research are as follows. 

- 1) Utilizing IMU-based measurement technology, we construct FallTL, a large-scale motion dataset for simulating falls and ADLs. To the best of authors’ knowledge, FallTL is the first multi-body segment dataset that is suitable for both PIFD and FD tasks. The dataset is publicly available at https://zenodo.org/records/17552449 

- 2) We propose STA-Net, a novel deep learning network for both PIFD and FD tasks based on IMU data from a single body segment. Combining the advantages of spatial attention and temporal attention mechanism to extract key features, STA-Net achieves excellent performance. 

- 3) Our experimental analysis reveals that both placement and data modality of sensor exert a significant impact on both PIFD and FD tasks. The results highlight the critical role of measurement configuration and modality selection in enhancing detection performance. 

The rest of this paper is organized as follows. Section II discusses the related works. Section III describes the construction details of the proposed FallTL dataset. Section IV introduces the structure of the proposed STA-Net. Section V details the implementation process of experiments. Section VI 

and VII present the results and discussions according to the experiments. The conclusion is given in Section VIII. 

## II. RELATED WORKS 

## _A. Public Datasets_ 

In recent years, with the advancement of FDS, several publicly available datasets based on IMUs are released. We summarize these datasets according to the following criteria: i) the dataset must be fully publicly accessible and must include both falls and ADLs; ii) the dataset should involve at least 10 subjects. The summarized datasets are listed in Table I. 

A crucial aspect of fall-related datasets is the inclusion of temporal annotations, which precisely delineate the different phases of falls. These annotations enable the rigorous extraction of fall-related sequences from the recorded signals and support the development of reliable detection models. As listed in Table I, most existing fall datasets lack detailed annotation of fall phases, making it difficult to isolate and analyze specific temporal components such as the pre-impact stage. Furthermore, the few datasets that include temporal annotations typically cover only limited fall phases and are restricted to a single sensor location, thereby constraining their applicability for comprehensive multi-segment and phase-specific analysis. In terms of simulation protocols, these datasets exhibit a wide range of fall and ADL types. However, the selection of activities lacks a systematic taxonomy according to fall-related characteristics or fully grounded in clinical and biomechanical studies. Thus, a gap remains in the representativeness and realism of these datasets in capturing real-world complexity and variability. 

Compared with existing datasets, a key advantage of FallTL dataset is the inclusion of comprehensive temporal annotations. Moreover, FallTL provides complete four phase temporal annotations across eight body segments, and includes comprehensive activity types and a large number of subjects, enabling a more diverse and realistic representation of fall scenarios that is suitable for both PIFD and FD tasks. 

## _B. Deep Learning for FDS_ 

Using deep learning (DL) for IMU-based FDS has attracted increasing studies. CNN based structure is used to extract spatial features from IMU signals. Choi et al. [32] propose a modified directed acyclic graph-CNN (DAG-CNN) architecture to perform PIFD task. To better capture temporal features, recurrent neural networks (RNNs) is introduced in detection models. Kiran et al. [29] utilize a CNN-bidirectional gated recurrent unit (BiGRU) model with residual connections for PIFD task. Jain and Semwal [33] introduce an ensemble classifier combining CNN and LSTM, trained on carefully designed temporal features for PIFD task. Yi et al. [34] propose a novel unsupervised learning method based on a denoising LSTM-based convolutional variational autoencoder (CVAE) model to solve the problem of lack of fall data of FD task. More recently, attention mechanisms are investigated for IMU-based FDS. Al-qaness et al. [35] combine CNN, LSTM and self-attention mechanism to improve the accuracy of FD model by exploiting global context and key features indicating 

CAI et al.: FALL MONITORING WITH SINGLE IMU: A LARGE-SCALE DATASET AND A NOVEL DUAL-BRANCH NETWORK 

289 

TABLE I 

COMPARISON OF FALL DATASETS BASED ON IMUS (A REFERS TO ACCELEROMETER, G TO GYROSCOPE, O TO ORIENTATION MEASUREMENT, M TO MAGNETOMETER, AND B TO BAROMETER) 

**==> picture [503 x 189] intentionally omitted <==**

falls. Wang and Wu [36] introduce transformer into models and perform FD task through CNN and Transformer encoder. 

Compared with existing research, STA-Net introduces a novel dual-branch architecture to directly extract temporal and spatial features from IMU signals. To further enhance feature selection, the model incorporates squeeze-excitation module [37] and criss-cross attention module [38] in separate branches, enabling dynamic focus on the most critical features of the global sequence. This design not only improves discriminative power but also enhances model generalization across diverse real-world scenarios. 

## III. PROPOSED DATASET 

In this section, the generation details of the proposed FallTL dataset are presented, including data acquisition, fall phase definition, as well as the dataset organization. 

## _A. Data Acquisition System_ 

In order to collect human motion data, a motion monitoring platform is designed and implemented [39], [40]. The platform consists of multiple wireless sensor nodes, a video node, and a mobile control center. The overall data acquisition environment is shown in Fig. 1 (a). 

Each wireless sensor node comprises four main modules: a sensing module (JY901S, WIT Motion, Shenzhen, China), a control module (ESP32-CAM, Ai-Thinker, Shenzhen, China) integrated with a Bluetooth Low Energy System on Chip (BLE SoC), a storage module, and a power module, as shown in Figs. 1 (c) and (d). The sensing module captures motion data and integrates a three-axis accelerometer, a three-axis gyroscope, and a three-axis magnetometer, as listed in Table II. Sensing module communicates with the control module through Inter-Integrated Circuit (I2C) protocol, with a sampling frequency of 200 Hz. The control module integrates a BLE SoC, enabling wireless sensor node control and data conversion. Data is stored in real-time on a microSD card 

**==> picture [251 x 310] intentionally omitted <==**

Fig. 1. Overview of the data acquisition framework. 

through the serial peripheral interface (SPI) protocol, and a 500-mAh rechargeable battery powers the node. 

A total of eight wireless sensor nodes are attached to specific body segments: the chest, waist, left and right forearms, left and right thighs, and left and right shanks, as illustrated in Fig. 1(b). Each IMU measures the motion of its corresponding body segment within a local coordinate system that is defined by the International Society of Biomechanics (ISB) [41]. During data acquisition, the sensing module within the 

IEEE TRANSACTIONS ON NEURAL SYSTEMS AND REHABILITATION ENGINEERING, VOL. 34, 2026 

290 

TABLE II 

SENSOR PARAMETERS 

**==> picture [50 x 50] intentionally omitted <==**

wireless sensor node measures raw motion data of body segment, including acceleration, angular velocity, and magnetic field. Using an integrated attitude solver based on the Kalman filter, the sensing module computes the raw Euler angles data, and finally stores raw data in the registers of sensing module. The control module retrieves the raw data from the sensing module registers and calculates the physical quantities. Finally, the calculated physical quantities, including acceleration, angular velocity and orientation measurement, are transmitted by the control module to the storage module. 

As for synchronized video capture, a 120[◦] wide-angle camera is used for the video node, with a resolution of 3860 _×_ 2160 pixels and a frame rate of up to 90 FPS. The mobile control center is a PC-based graphical user interface (GUI) application developed with the Qt framework. It communicates with the wireless sensor nodes through BLE protocol and interacts with the video node through USB wired connection. The video data is stored in the mobile control center. The mobile control center continuously monitors the abnormal status of wireless sensor nodes and video node, providing real-time feedback within the GUI [42]. Data synchronization between nodes is handled using Python multi-threading method, with a timestamp correction technique ensuring precise time alignment with the mobile control center. 

## _B._ 

The process of human falling is described as follows [29], [32], [43]: during performing normal activities, a fall may occur at a certain moment. Once a fall onsets, the subject starts to lose balance, marking the transition from stable motion to uncontrolled descent. The body then tilts in a specific direction, and the acceleration increases rapidly due to the combined effects of gravity and body movement, reaching its peak at the moment of ground impact. After impact, the body goes through a brief period of adjustment, with stable acceleration. Subsequently, the individual may attempt to recover or seek external assistance, leading to varying acceleration patterns depending on movement intensity. 

Based on above process, the fall activity can be divided into four phases: (1) normal activities to fall onset, (2) fall onset to impact (pre-impact phase), (3) impact to recovery onset (postimpact phase), and (4) recovery onset to recovery completion, as shown in Fig. 2. The PIFD task is based on phase (2), while FD task is based on phases (2) and (3). 

## _C. Dataset Organization_ 

_1) Participants:_ In this research, 45 healthy young participants (39 males and 6 females, age 22.24 _±_ 1.48 years, stature 

Fig. 2. Phases and attributes of falls. 

176.07 _±_ 7.42 cm, and body mass 74.79 _±_ 20.89 kg) without any history of musculoskeletal disorder are chosen. All subjects sign the informed consent form before participating in the experiment. This study is approved by the Biological and Medical Ethics Committee of Dalian University of Technology (protocol number DUTST240603-01). 

_2) Activity Selection:_ Based on fall phases introduced in Section III-B, three key attributes are included in this research when analyzing falls: starting movements, fall directions, and ending movements, as shown in Fig. 2. 

Starting movements refer to the normal activities of subjects before the fall occurs. According to related studies [4], [18], [44], [45], high fall-risk activities in older adults include walking, attempting to stand up or sit down, ascending or descending stairs and picking up objects. Additionally, syncope-related falls, characterized by loss of consciousness [46], represent a significant concern in emergency room admissions and are associated with high mortality rates among older adults [47]. Based on these analysis, six types of starting movements are selected, categorized into static types (syncoperelated activities, including static standing and static sitting) and dynamic types (walking, attempting to stand up or sit down, and picking up objects). Stair-related falls are excluded from this research because of the high risk of injury. Fall direction plays a critical role in real-life medical diagnosis, as medical professionals often rely on fall direction to assess the locations of injuries [48]. Fall directions are defined according to the primary orientation of the body’s descent relative to the sagittal and frontal planes [49], [50]. Ultimately, three fall directions (forward, backward, and lateral) are included in this research. Specifically, forward falls occur when the body tilts anteriorly toward the sagittal plane, backward falls when the body moves posteriorly, and lateral falls when the motion is directed toward either side of the frontal plane. Ending movements of fall are introduced based on prior study [25], distinguishing between falls with and without recovery. This distinction is clinically relevant, as it aids healthcare providers in identifying potential complications, such as subdural hematomas [51], and facilitates timely medical intervention. Furthermore, incorporating the recovery phase in fall analysis can enhance the robustness of detection models [25]. In summary, for fall activities, FallTL dataset encompasses six types of starting movements, three types of fall directions, and two types of ending movements, forming a total of 34 distinct fall activities. Note that the starting movement of picking up does not include backward falls. 

CAI et al.: FALL MONITORING WITH SINGLE IMU: A LARGE-SCALE DATASET AND A NOVEL DUAL-BRANCH NETWORK 

291 

**==> picture [515 x 187] intentionally omitted <==**

Fig. 3. Visualization examples of FallTL dataset. 

ADLs are divided into three types: static (standing, sitting, lying, and side lying), cycle (walking, shuffle with a stoop, and jogging), and transition (lie down, get up, pick up, sit down, and stand up). The initial and final phases of cyclic ADLs (such as the initiation and termination of walking) are included to capture the entire process of activity. Furthermore, the static phases before and after transition activities are included. These phases are particularly relevant, as they introduce higher confusion when distinguishing ADLs from falls. 

## _D. Dataset Description_ 

All participants perform 34 falls and 12 ADLs, while wearing IMUs on eight body segments to capture acceleration, angular velocity, and orientation modalities. To ensure the data reflect real-life scenarios, researchers provide guidance only regarding pre-impact phase to prevent injury. All other phases and activities are conducted according to the participants’ natural behaviors and habits. Furthermore, no restrictions are limited on any additional activities, allowing the collected data to be closer to real-world activities. A representative visualization of ADLs and falls is illustrated in Fig. 3. In total, the FallTL dataset contains approximately 28.43 hours of recorded data, providing a comprehensive and diverse foundation for PIFD and FD research. The dataset and detailed information are publicly available at https://zenodo.org/records/17552449 

## _E. Annotation Strategy_ 

For reliable detection, it is critical to detect falls during the fall phase, so the various phases of falls should be annotated as defined in Section III-B. Therefore, the objective of annotation is to determine the transition moments between these phases. In order to accurately confirm the transition moments, a method combining the sum magnitude vector (SMV) and synchronized video clips is used to divide each phase. The SMV of acceleration is calculated using 

**==> picture [177 x 19] intentionally omitted <==**

where _ax_ , _ay_ and _az_ represent the accelerations along three axes. For a fall signal sequence consisting of four phases, the annotation strategy is described as follows: 

- 1) Determining the exact onset of falls between phase (1) and (2) is challenging based solely on SMV. therefore, this moment is identified primarily through video clips. Specifically, the moment when the body first begins to tilt in the video clip is identified as the onset of fall. 

- 2) The moment of impact with the ground between phase (2) and (3) is the most critical moment in fall sequence, but it is difficult to pinpoint precisely through video clips. Notably, this is when the SMV reaches its highest value during the fall. It should be noted that the instant at which the SMV reaches its maximum value varies among different body segments, as each segment contacts the ground at slightly different times. To determine the impact moment for different body segments, we adopt the following strategy. A ground-contact time window is first coarsely estimated from the synchronized video clips, defined as the period between the subject’s first contact with the ground and the completion of fullbody contact. Within this time window, the acceleration signals from each body segment are examined, and the moment corresponding to the maximum SMV value is identified as the precise impact instant. 

- 3) The onset of recovery between phase (3) and phase (4) is relatively distinct in video clips, as it corresponds to the first visible effort of the subject to regain posture or movement after the impact. Therefore, the moment when recovery begins in the video clip is directly identified as the onset of recovery. 

Phase annotation through video clips involves some subjective judgment of the researcher. This annotation strategy divides the various phases of fall signals, allowing DL model to better learn features of falls and ADLs. 

## IV. METHODOLOGY 

In this section, we introduce the proposed STA-Net designed for both PIFD and FD tasks. The task definition, structure 

IEEE TRANSACTIONS ON NEURAL SYSTEMS AND REHABILITATION ENGINEERING, VOL. 34, 2026 

292 

**==> picture [493 x 264] intentionally omitted <==**

Fig. 4. Proposed STA-Net structure, consisting of spatial attention branch, Temporal attention branch, and output block. 

of the proposed STA-Net and the loss strategy to mitigate data imbalance is introduced. As shown in Fig. 4, the STA-Net consists of Spatial Attention Branch (SAB), Temporal Attention Branch (TAB) and Output block. 

## _A._ 

Fall-related detection tasks aim to distinguish falls and ADLs using multiple sensor signals from a single body segment. Each training sample is defined as _S i_ = ( _Xi_ , _yi_ ), where _Xi_ ∈ R _[N][×][W]_ represents the sensor signal data, and _yi_ ∈ _Y_ denotes the corresponding label. Here, _W_ represents the length of signal sequence, while _N_ represents the number of signal modalities obtained from multiple sensors. The label set is defined as _Y_ = {0, 1}, indicating whether to fall. 

## _B. Spatial Attention Branch_ 

_1) Multi-Scale Feature Extraction:_ The IMU signal is a timecontinuous sequence containing multiple signal modalities, effectively mining the spatial interaction features between different modalities can improve the performance of detection model. Therefore, the multi-scale feature extraction [52] structure based on 2-dimensional CNN (Conv 2D) is employed to extract the multi-scale spatial features of the signal sequence. Given an input sequence _X_ ∈ R[1] _[×][N][×][W]_ , the multi-scale feature extraction can be as 

**==> picture [208 x 73] intentionally omitted <==**

where _fk×k_ represents a Conv 2D operation with a _k×k_ kernel, and the number of filters for each branch is set to 8, 16, 32, and 64, respectively. The output of these branches is concatenated and passed through a Conv2D with 64 filters to fuse features. 

_2) SE Channel Attention:_ Considering that the local receptive field of Conv2D can only extract local contextual information, in order to further improve the representational power of the network, Squeeze-and-Excitation (SE) Block [37] is integrated to explicitly model the interdependence between Conv2D feature channels. For an input feature map _X_[′] ∈ R _[C][×][N][×][W]_ , the SE operation is defined as 

**==> picture [192 x 61] intentionally omitted <==**

where _s_ ∈ R _[C]_ is a channel descriptor by applies global average pooling to squeeze the global spatial information, _W_ 1 ∈ R _[C]_[/] _[r][×][C]_ and _W_ 2 ∈ R _[C][×][C]_[/] _[r]_ are the learnable weight matrices, _ReLU_ (·) is rectified linear unit (ReLU) activation function, and σ denotes the sigmoid activation function. 

SE Block expresses the whole signal sequence through local descriptors and obtains descriptor-specific channel weights, which ensures that the network is able to improve the sensitivity to informative features so that subsequent network can exploit them and suppress less useful features. 

_3) Residual Block:_ Considering the challenges of gradient vanishing and gradient exploding that occur with the increase of depth in traditional neural networks, residual block [53] is introduced containing multi-scale feature extractor and SE block. Specifically, a simple hopping mechanism is employed 

CAI et al.: FALL MONITORING WITH SINGLE IMU: A LARGE-SCALE DATASET AND A NOVEL DUAL-BRANCH NETWORK 

293 

to connect the remaining network modules between network layers, thereby reducing the feature loss and learning residuals (i.e., the discrepancy between input and output). Finally, a ReLU activation function is used to preserve positive values, enhancing residual connection effectiveness. 

_4) CNN 2D:_ To further enhance the integration of spatial features, a CNN 2D block is incorporated at the end of spatial branch. It consists of a Conv 2D layer with 64 filters and a kernel size of 3 _×_ 3, followed by a Batch Normalization (BN) layer and ReLU activation function to improve training stability and non-linearity. Finally, a max pooling layer is applied to reduce the spatial dimensions and the number of learnable parameters. 

## _C._ . _Temporal Attention Branch_ 

_1) Bi-GRU:_ For IMU signals, effectively mining the dependencies between time series can improve detection performance. In this research, Bi-GRU is integrated into the network to capture temporal features in both forward and backward directions. Given an input sequence _X_ = [ _x_ 1, _x_ 2, . . . , _xW_ ], _xt_ ∈ R _[N]_ , where _W_ is the sequence length, and _N_ is the input singal modalities, the Bi-GRU is performed to extract temporal features as 

**==> picture [198 x 55] intentionally omitted <==**

where _ht_ ∈ R[2] _[d]_ , and _d_ is the hidden dimension of a GRU. 

_2) Criss-Cross Attention:_ For IMU data, there exist i) strong cross-modal correlations between the three-axis accelerometer and three-axis gyroscope signals, and ii) temporal dependencies across consecutive timesteps due to continuous motion dynamics. While some works adopt self-attention mechanism [36], [54] to exploit these properties, such approaches require constructing dense attention maps that measure pairwise relationships between all data points, resulting in high computational cost and latency. For both PIFD and FD tasks, which demands rapid inference within a short time window, this overhead is undesirable. In order to strengthen the network’s attention to the features at different timesteps and the features of different signal modalities at the same timestep in sequence data, while enabling timely detection, we combine Bi-GRU with Criss-Cross Attention (CCA) [38] to design a distinctive temporal attention mechanism. The crisscross attention mechanism selectively models key temporal and cross-modal interactions, enabling efficient and effective feature aggregation for timely detection. 

For the output _H_ = [ _h_ 1, _h_ 2, _h_ 3, . . . , _HW_ ] of Bi-GRU, three feature maps _Q_ , _K_ and _V_ are generated through three learnable matrices. Attention scores are calculated along the cross paths through affinity operation. The features at position _p_ in feature map _Q_ are extracted to extract content _Qp_ . From feature map _K_ , the content corresponding to the same rows and columns as _p_ is extracted to form set Ω _p_ . The affinity operation is defined as 

**==> picture [151 x 14] intentionally omitted <==**

where _sp_ ∈ _S_ indicates the correlation degree between _Qp_ and Ω _p_ , and _S_ is the attention score matrix. Then, a softmax layer on _S_ over the channel dimension is applied to calculate the final attention map _A_ . 

Following the attention map, the aggregation operation integrates contextual information from various regions of signal sequence to form a global feature representation. For the position _u_ of _V_ , the set Φ _u_ is the collection of the content which are in the same row or column with position _u_ . The aggregation operation is defined as 

**==> picture [174 x 24] intentionally omitted <==**

where _Hu_[′][is][a][feature][representation][in][output][feature][maps] _H_[′] ∈ R _[N]_ . The contextual information generated by above operations is added to _H_ , enhancing the local features and strengthening the data point-level representation. 

_3) CNN 1D:_ Similar to SAB, a CNN 1D block is integrated at the end of the temporal branch to enhance feature integration. Compared to Conv 2D, Conv 1D is more effective at capturing temporal dependencies. Specifically, two Conv 1D layers, each with 64 filters and a kernel size of 3 _×_ 3, are applied, followed by a BN layer to stabilize training. 

## _D. Output Block_ 

The outputs of SAB and TAB are flattened, then elementwise addition is performed before entering the output block. The output block contains an Multi-Layer Perceptron (MLP) consisting of three fully connected layers with 128, 64, and 2 units, respectively. Each layer is set with a a dropout rate of 0.5 to avoid overfitting. Finally, a softmax activation function is used to calculate detection score for 

## _E. Loss Strategy_ 

Compared to ADLs, falls are characterized by their suddenness and brevity, which make them more challenging to distinguish and and result in a substantially smaller number of available data samples. Traditional cross-entropy loss function [55] makes the model tends to be biased toward the majority class and easily distinguishable negative samples (i.e., ADLs). To mitigate this issue, we adopt focal loss function [56], which assigns greater emphasis to the minority and hard-to-classify samples. The focal loss is formulated as 

**==> picture [222 x 31] intentionally omitted <==**

where _p_ represents the predicted probability, and _y_ denotes the true class label. The weighting factor α ∈ [0, 1] is introduced to address class imbalance by assigning different weights to the loss function. This factor is determined based on the class distribution and imposes a higher penalty when the model misclassifies samples from the underrepresented class. γ is a focusing parameter, which is used to reduce the loss contribution of well-classified samples. By dynamically scaling the loss contribution of samples, focal loss encourages the model to focus more on learning from challenging and underrepresented class, thereby improving model performance. 

IEEE TRANSACTIONS ON NEURAL SYSTEMS AND REHABILITATION ENGINEERING, VOL. 34, 2026 

294 

## V. EXPERIMENTS 

In this section, experiments are performed on the proposed FallTL dataset and two publicly available datasets. The benchmark datasets description, data processing, model training, and evaluation metrics are introduced in detail. 

## _A._ . _Benchmark Datasets_ 

_1) KFall Dataset [26]:_ KFall dataset comprises recordings from 32 young Korean male subjects, capturing 21 falls and 15 ADLs. Data are collected using a waist-worn sensor at a sampling frequency of 100 Hz, incorporating acceleration, gyroscope, and orientation measurement. This dataset provides annotated annotations for fall sequences, including the moment of fall onset and impact, based on synchronized video clips, and is therefore applicable to both PIFD and FD tasks. We divide fall sequences into three phases: (1) normal activities to fall onset, (2) fall onset to impact (pre-impact phase), and (3) impact to sequence termination (post-impact phase). 

_2) FallAllD Dataset [25]:_ FallAllD is a large-scale dataset designed for FD task, comprising motion data collected from 15 participants aged 21 to 53. The data is measured using three wearable data loggers positioned at waist, forearm, and neck. It includes signals from an accelerometer, gyroscope, magnetometer, and barometer. The accelerometer and gyroscope data are sampled at a frequency of 238 Hz, the magnetometer at 80 Hz, and the barometer at 10 Hz. Unlike FallTL and KFall, FallAllD does not provide time annotations. 

- _B. Data Processing_ 

_1) Normalization:_ To reduce the impact of varying sensor scales on model performance and minimize potential training bias, data normalization is performed. Specifically, z-score normalization is used, which standardizes the data based on its mean and standard deviation, effectively transforming the signal values to a consistent scale. 

_2) Segmentation:_ A fixed-size overlapping sliding window method is used in this research. For the FallTL and KFall datasets, which include time annotations, window labels are assigned based on fall phases. For PIFD task, windows containing the pre-impact phase annotations are labeled as fall, while all other windows are labeled as ADL. For FD task, windows containing either pre-impact or post-impact phase annotations are labeled as fall, whereas the remaining windows are labeled as ADL. Following existing research [18], [32], [36], a 1-second sliding window with a 50% overlap is employed. For the FallAllD dataset, which lacks temporal annotations, window labels are determined by the origin of the sequence. Windows generated from fall sequences are labeled as fall, whereas those derived from ADL sequences are labeled as ADL. In accordance with the original FallAllD protocol [25], a 13-second non-overlapping window is adopted. 

## _C. Training Details_ 

Experiments are conducted on a AMD EPYC 9754 CPU with 60GB memory and a NVIDIA GeForce RTX 4090D with 24GB memory. The operating system is Ubuntu 20.04, and 

## TABLE III 

TRAINING CONFIGURATIONS OF STA-NET 

**==> picture [69 x 106] intentionally omitted <==**

**==> picture [137 x 106] intentionally omitted <==**

all models are trained using PyTorch 1.11.0 framework with Python 3.8. The number of training epochs of STA-Net is set to 100 with Adam optimizer. The detailed training configurations of STA-Net are listed in Table III. 

To assess the stability and robustness of the proposed model, leave-one-group-out cross-validation method is utilized. Specifically, subjects are divided into 5 groups, 4 of which are selected as training sets and remaining group is used to test model. This method evaluates the model’s generalization to new subjects, facilitating a comprehensive assessment of model performance. 

## _D. Evaluation Metrics_ 

All experiments employ a window-based evaluation strategy, where the metrics are calculated based on the classification results of segmented windows. The trained models are evaluated in terms of sensitivity (SEN), specificity (SPE), accuracy (ACC), and lead time. SEN represents the proportion of correctly identified fall windows among all actual fall windows, whereas SPE measures the proportion of correctly identified ADL windows among all ADL windows. ACC represents the overall correctness of the model’s classification results across all classes. ACC, SEN and SPE are defined as 

**==> picture [194 x 32] intentionally omitted <==**

**==> picture [203 x 39] intentionally omitted <==**

where TP is the number of true positives, FP is the number of false positives, TN is the number of true negatives, and FN is the number of false negatives. Lead time refers to the time interval between the moment when the algorithm successfully detects an impending fall and the actual moment of impact, which is as 

**==> picture [170 x 11] intentionally omitted <==**

where _timpact_ represents the timestamp of the fall impact, and _tpred_ denotes the timestamp when a fall is detected. _Tlead_ quantifies how early the system can identify a fall before the impact occurs, thereby reflecting the model’s ability to provide timely warnings for preventive interventions. 

CAI et al.: FALL MONITORING WITH SINGLE IMU: A LARGE-SCALE DATASET AND A NOVEL DUAL-BRANCH NETWORK 

295 

TABLE IV 

RESULTS OF STA-NET USING ACCURACY (%), SENSITIVITY (%), AND SPECIFICITY (%) ON FALLTL DATASET 

**==> picture [469 x 81] intentionally omitted <==**

TABLE V 

RESULTS OF STA-NET ON FALLTL DATASET (WAIST) 

**==> picture [232 x 72] intentionally omitted <==**

## VI. RESULTS 

This section presents all experimental results including comprehensive evaluation of STA-Net on three datasets, model ablation, and comparison with existing methods. 

## _A. Performance Evaluation of STA-Net_ 

_1) Results of Multiple Body Segments:_ The performance of the proposed STA-Net is evaluated on the FallTL dataset using leave-one-group-out cross-validation method to assess the model’s applicability in various realistic sensor location settings on both PIFD and FD tasks. For each sensor placement, the model is trained and tested with data from the corresponding location. Table IV lists the results regarding three evaluation metrics. For the PIFD task, the chest and waist yield the best results, achieving average accuracy, sensitivity, and specificity of 94.20%, 94.12%, 94.29% for the chest, and 93.64%, 94.07%, and 94.18% for the waist, respectively. For the FD task, all evaluated body segments achieve comparable average evaluation metrics, highlighting the stability and effectiveness of STA-Net in FD scenarios. Considering that the performance in FD task is generally more influenced by the detection algorithm than the placement of sensors [16], the excellent performance of STA-Net effectively compensates for potential variations caused by sensor location, underscoring the model’s advanced structure and its practical value across diverse deployment scenarios. 

We further conduct experiments using different combinations of IMU signals to assess the model’s capability of handling various data modalities. Specifically, three modality configurations are considered: i) acceleration only; ii) acceleration and angular velocity; and iii) acceleration, angular velocity, and orientation measurement. Experimental results are listed in Table V. For PIFD task, when using only acceleration signals, STA-Net achieves an average accuracy of 78.96%. By introducing angular velocity and orientation measurement alongside acceleration, performance improves notably across 

the board, reaching 94.20% average accuracy. Additionally, the standard deviations decrease significantly in this setting, indicating a more stable detection performance. For FD task, STA-Net performs exceptionally well with only acceleration input, achieving average metrics of 97.46% accuracy, 98.67% sensitivity, and 97.88% specificity. Further inclusion of angular velocity and orientation measurement signals yields only slight improvements, with the average accuracy being 98.01% under configuration iii). Overall, the STA-Net achieves advantageous results on the different combinations of signal modalities, demonstrating its robustness and adaptability to varying combinations of input signals. 

_2) Results of Public Datasets:_ To further evaluate the performance of the proposed STA-Net across multiple data distributions, we utilize two publicly benchmark datasets for fall-related detection: KFall and FallAllD. The evaluation results are shown in Fig. 5. 

For the KFall dataset, STA-Net achieves an average accuracy of 96.06% on PIFD task and 99.28% on FD task. Notably, performance on the FD task consistently surpasses that of the PIFD task, aligning with results observed on the FallTL dataset. In the case of FallAllD dataset, due to the lack of temporal annotations, only the FD task is conducted. Based on acceleration and angular velocity data captured from chest, waist and forearm, STA-Net achieves average accuracies of 94.58%, 92.92% and 91.62%, respectively. 

Compared to the FallTL and KFall datasets, the performance of STA-Net on FallAllD dataset is relatively lower. We attribute this performance gap primarily to the absence of fall phase annotations in the FallAllD dataset. Therefore, coarse segmentation using fixed-size sliding windows may have introduced label noise by including non-fall phases within the fall-labeled windows. This likely affected the model’s ability to accurately distinguish falls from ADLs, thereby limiting its overall performance on FallAllD dataset. 

_3) Model Size and Latency:_ To explore the deployment potential of STA-Net on mobile devices, we evaluate its number of parameters, model size, training time, inference time, and lead time on FallTL dataset (waist). The model is optimized using PyTorch Mobile [57]. The training time refers to the duration required to train a mini-batch of 64 samples, while the inference time denotes the execution time for processing one IMU sample. The results indicate that STA-Net contains 1,323.59K parameters, has a model size of 22.40 MB, requires 5.06 s for training, achieves an average inference time of 70.30 ms and lead time of 456.69 _±_ 294.58 ms. 

IEEE TRANSACTIONS ON NEURAL SYSTEMS AND REHABILITATION ENGINEERING, VOL. 34, 2026 

296 

TABLE VI 

MODEL ABLATION RESULTS USING THREE EVALUATION METRICS ON FALLTL (WAIST) AND KFALL DATASETS 

**==> picture [56 x 54] intentionally omitted <==**

**==> picture [165 x 90] intentionally omitted <==**

**==> picture [165 x 90] intentionally omitted <==**

**==> picture [189 x 163] intentionally omitted <==**

**==> picture [57 x 319] intentionally omitted <==**

**==> picture [189 x 157] intentionally omitted <==**

Fig. 5. Results of STA-Net on public datasets: (a) results of PIFD and FD tasks on KFall dataset; (b) results of FD task using chest, waist and forearm signals from FallAllD dataset. 

Considering that the activation time required for active protection measures is 120 ms [58], STA-Net clearly meets this time constraint. These results demonstrate that STA-Net maintains a favorable trade-off between detection accuracy and computational efficiency, making it well-suited for delopying on mobile devices. 

## TABLE VII 

MODEL ABLATION RESULTS OF SELF-ATTENTION AND CRISS-CROSS ATTENTION ON FALLTL (WAIST) DATASET 

and/or temporal branches and their corresponding attention modules: i) S model is the spatial branch without SE module; ii) SA model is the spatial branch with SE module; iii) T model is the temporal branch without CCA module; iv) TA mode is the temporal branch with CCA module; v) ST mode contains both temporal branch and spatial branch without SE and CCA module; vi) STA mode contains both temporal branch and spatial branch with SE and CCA module. The comparison results are listed in Table VI. Comprehensive comparative experiments demonstrate the superiority of the branch structure and attention mechanisms. Furthermore, the results indicate that temporal features contribute more significantly than spatial features in enhancing the detection performance on IMU signals. 

To further illustrate the characteristics of CCA, we depict the attention maps of fall and ADL samples from PIFD task, as shown in Fig. 6, where lighter colors represent higher CCA weights. For falls, CCA assigns greater attention weights of the pre-impact phases, as shown in the right portion of Fig. 6 (a). In contrast, for ADLs, CCA maintains relatively constant weights across the same modality features throughout the entire time sequences. The visualization results indicate the ability of CCA module to effectively distinguish dynamic transitions in fall scenarios from the stable patterns of ADLs. In addition, we replace CCA with traditional self-attention mechanism, and the results are shown in Table VII. CCA outperforms the self-attention mechanism in both classification performance and lead time. 

## _C. Comparison With Existing Works_ 

## _B. Model Ablation_ 

To comprehensively evaluate the contributions of the temporal and spatial branches and attention mechanisms, we conduct ablation experiments for PIFD task. These experiments progressively remove specific components of STA-Net to assess their individual impact on overall performance. We construct six sub-models by selectively disabling the spatial 

We conduct comparison experiments for PIFD task between proposed model and several existing models on FallTL and KFall dataset to verify the performance of STA-Net, as listed in Table VIII. To enable a comprehensive comparison of different architectures, we select existing models with various structures and combination strategies. We adhered as closely as possible to the original architectures and hyperparameter settings of the 

CAI et al.: FALL MONITORING WITH SINGLE IMU: A LARGE-SCALE DATASET AND A NOVEL DUAL-BRANCH NETWORK 

297 

## TABLE VIII 

COMPARISON RESULTS OF STA-NET WITH EXISTING MODELS ON FALLTL (WAIST) AND KFALL DATASETS 

**==> picture [457 x 80] intentionally omitted <==**

**==> picture [108 x 108] intentionally omitted <==**

**==> picture [109 x 108] intentionally omitted <==**

**==> picture [108 x 107] intentionally omitted <==**

**==> picture [109 x 107] intentionally omitted <==**

**==> picture [108 x 108] intentionally omitted <==**

**==> picture [109 x 108] intentionally omitted <==**

Fig. 6. Heatmaps of CCA: (a) fall samples, (b) ADL samples. 

TABLE IX 

IMPLEMENTATION DETAILS OF EXISTING MODELS 

**==> picture [191 x 67] intentionally omitted <==**

respective methods. The implementation details of comparison models are listed in Table IX. 

The comparison results on two datasets in Table VIII demonstrate that the proposed STA-Net outperforms the existing models while exhibits comparable lead time. This further 

demonstrates the effectiveness of the structure that utilizes the SAB and TAB structures to process the original signals separately for fall-related detection. Furthermore, models that integrate CNN and RNN (ConvLSTM, CNN-BiGRU, and MKLS-Net) outperform both DAG-CNN, which relies solely on CNNs, and PTN, which combines CNN and Transformer components. These results underscore the importance of jointly capturing and integrating both temporal and spatial features from IMU data to improve the robustness of detection models. 

## VII. DISCUSSION 

Based on experimental results, this section presents an in-depth analysis of the impact of sensor placement and input signal modality on detection performance. In addition, the limitations and future works are discussed. 

## _A. Impact of Input Data Modality_ 

Table V presents the performance of PIFD and FD tasks under different input modalities. For the PIFD task, a noticeable degradation in detection performance is observed as input modalities reduces, highlighting the critical role of kinematic information (angular velocity and orientation measurement) in maintaining robust detection performence. In contrast, the FD task demonstrates relatively stable performance across different input configurations, with STA-Net achieving excellent performance using accelerometer data. This difference can be attributed to two main factors. On the one hand, the PIFD task relies solely on pre-impact phase signals, which excludes critical features such as impact, resulting in a reduced amount of discriminative information. On the other hand, the short temporal duration of the pre-impact phase imposes a greater demand on temporal modeling capabilities, making the task more sensitive to data imbalance and noise. 

Moreover, incorporating explicit orientation data alongside accelerometer and gyroscope measurements enables the model to more effectively capture postural features characteristic of fall events. This explicit representation establishes a coherent relationship between motion dynamics (captured by accelerometer and gyroscope signals) and posture evolution (captured by orientation measurements), thereby facilitating more efficient feature learning for both PIFD and FD tasks. 

## _B. Impact of Sensor Locations_ 

Existing studies [16] have investigated how sensor placement influences FD performance. However, the impact of 

IEEE TRANSACTIONS ON NEURAL SYSTEMS AND REHABILITATION ENGINEERING, VOL. 34, 2026 

298 

sensor location on the performance of PIFD models has not been systematically explored. In this study, we explicitly evaluate both PIFD and FD tasks, isolating the pre-impact phase to assess how sensor placement affects detection performance prior to ground contact. 

Table IV and Fig. 5 (b) illustrate the detection results of STA-Net using signals from multiple sensor Locations on FallTL and FallAllD datasets. In both datasets, the chest and waist sensor locations consistently achieve the highest detection performance. Owing to their anatomical proximity to the trunk, these regions are inherently less susceptible to variations arising from inter-individual differences in motor behavior. Consequently, the biomechanical and functional consistency of the torso confers a degree of robustness that is not as readily observed in distal extremities, where interpersonal variability in movement patterns and behavioral expressions tends to be more pronounced. 

## _C. Limitations and Future Works_ 

The FallTL dataset proposed in this research is derived from simulated experiments conducted in a controlled laboratory environment, rather than from real-world falls. The participants are limited to young and healthy individuals, as it would be hazardous to involve elderly subjects in fall scenarios. Nevertheless, considering that real falls tend to occur with greater velocity and stronger impact [32], the dataset and the proposed model remain of considerable significance. Moreover, the dataset lacks near-fall scenarios, which share similar motion patterns with real falls and should be correctly identified by the model to prevent false alarms [31], [32], [59]. Additionally, the proposed STA-Net does not offer fine-grained classification across different types of falls. As discussed in Section III-B, a detailed classification based on the characteristics of falls can offer numerous advantages. Therefore, future works can explore more fine-grained classification methods to enhance the applicability of FDS. 

## VIII. CONCLUSION 

In this research, we first construct FallTL, a large-scale motion dataset designed to simulate both falls and ADLs. Notably, FallTL includes time-annotated fall phases, making it well-suited for both PIFD and FD tasks. In addition, we propose STA-Net, a novel dual-branch network architecture that captures temporal and spatial features from sensor signals for fall-related detection. Furthermore, we conduct an in-depth analysis of the influence of input signal modalities and sensor placements on detection performance, revealing the significant impact of these factors on the robustness of FDS models. This research provides valuable data and insights, aiming at facilitating the development of more robust and proactive solutions for elderly protection. 

**==> picture [62 x 8] intentionally omitted <==**

- [1] M. C. Nevitt, S. R. Cummings, and E. S. Hudes, “Risk factors for injurious falls: A prospective study,” _J. Gerontol._ , vol. 46, no. 5, pp. M164–M170, Sep. 1991. 

- [2] V. L. L. Bittencourt, S. L. Graube, E. M. F. Stumm, I. D. E. Battisti, M. M. Loro, and E. R. Winkelmann, “Factors associated with the risk of falls in hospitalized adult patients,” _Revista da Escola de Enfermagem da USP_ , vol. 51, May 2017, Art. no. e03237. 

- [3] R. Cuevas-Trisan, “Balance problems and fall risks in the elderly,” _Clinics Geriatric Med._ , vol. 35, no. 2, pp. 173–183, May 2019. 

- [4] S. R. Lord, J. A. Ward, P. Williams, and K. J. Anstey, “An epidemiological study of falls in older community-dwelling women: The Randwick falls and fractures study,” _Austral. New Zealand J. Public Health_ , vol. 17, no. 3, pp. 240–245, Sep. 1993. 

- [5] L. Ren and Y. Peng, “Research of fall detection and fall prevention technologies: A systematic review,” _IEEE Access_ , vol. 7, pp. 77702–77722, 2019. 

- [6] F. Jin, A. Sengupta, and S. Cao, “MmFall: Fall detection using 4- D mmWave radar and a hybrid variational RNN AutoEncoder,” _IEEE Trans. Autom. Sci. Eng._ , vol. 19, no. 2, pp. 1245–1257, Apr. 2022. 

- [7] S. R. Lord, C. Sherrington, H. B. Menz, and J. C. T. Close, _Falls in Older People: Risk Factors and Strategies for Prevention_ , 2nd ed. Cambridge, U.K.: Cambridge Univ. Press, 2007. 

- [8] J. Chen et al., “Digital twin empowered wireless healthcare monitoring for smart home,” _IEEE J. Sel. Areas Commun._ , vol. 41, no. 11, pp. 3662–3676, Nov. 2023. 

- [9] J. Chen, S. Sun, L. Zhang, B. Yang, and W. Wang, “Compressed sensing framework for heart sound acquisition in Internet of Medical Things,” _IEEE Trans. Ind. Informat._ , vol. 18, no. 3, pp. 2000–2009, Mar. 2022. 

- [10] Y. Cai, B. Guo, F. Salim, and Z. Hong, “Towards generalizable human activity recognition: A survey,” 2025, _arXiv:2508.12213_ . 

- [11] S. Chen, C. Zhu, X. Chen, and J. Yi, “Machine learning-based real-time walking activity and posture estimation in construction with a single wearable inertial measurement unit,” _IEEE Trans. Autom. Sci. Eng._ , vol. 22, pp. 16144–16156, 2025. 

- [12] R. Gravina, P. Alinia, H. Ghasemzadeh, and G. Fortino, “Multisensor fusion in body sensor networks: State-of-the-art and research challenges,” _Inf. Fusion_ , vol. 35, pp. 68–80, May 2017. 

- [13] O. Ojetola, E. Gaura, and J. Brusey, “Data set for fall events and daily activities from inertial sensors,” in _Proc. 6th ACM Multimedia Syst. Conf._ , 2015, pp. 243–248. 

- [14] S. Gasparrini et al., “Proposal and experimental evaluation of fall detection solution based on wearable and depth data fusion,” in _ICT Innovations 2015: Emerging Technologies for Better Living 7_ . Cham, Switzerland: Springer, 2016, pp. 99–108. 

- [15] G. Vavoulas, C. Chatzaki, T. Malliotakis, M. Pediaditis, and M. Tsiknakis, “The mobiact dataset: Recognition of activities of daily living using smartphones,” in _Proc. Int. Conf. Inf. Commun. Technol. Ageing Well E-Health_ , vol. 2. Set´ubal, Portugal: SciTePress, 2016, pp. 143–151. 

- [16] A. Ozdemir,[¨] “An analysis on sensor locations of the human body for wearable fall detection devices: Principles and practice,” _Sensors_ , vol. 16, no. 8, p. 1161, Jul. 2016. 

- [17] E. Casilari, J. A. Santoyo-Ram´on, and J. M. Cano-Garc´ıa, “UMAFall: A multisensor dataset for the research on automatic fall detection,” _Proc. Comput. Sci._ , vol. 110, pp. 32–39, Jan. 2017. 

- [18] A. Sucerquia, J. L´opez, and J. Vargas-Bonilla, “SisFall: A fall and movement dataset,” _Sensors_ , vol. 17, no. 1, p. 198, Jan. 2017. 

- [19] D. Micucci, M. Mobilio, and P. Napoletano, “UniMiB SHAR: A dataset for human activity recognition using acceleration data from smartphones,” _Appl. Sci._ , vol. 7, no. 10, p. 1101, Oct. 2017. 

- [20] O. Aziz, M. Musngi, E. J. Park, G. Mori, and S. N. Robinovitch, “A comparison of accuracy of fall detection algorithms (threshold-based vs. machine learning) using Waist-mounted tri-axial accelerometer signals from a comprehensive set of falls and non-fall trials,” _Med. Biol. Eng. Comput._ , vol. 55, no. 1, pp. 45–55, Jan. 2017. 

- [21] T.-H. Tran et al., “A multi-modal multi-view dataset for human fall analysis and preliminary investigation on modality,” in _Proc. 24th Int. Conf. Pattern Recognit. (ICPR)_ , Aug. 2018, pp. 1947–1952. 

- [22] F.-T. Wang, H.-L. Chan, M.-H. Hsu, C.-K. Lin, P.-K. Chao, and Y.J. Chang, “Threshold-based fall detection using a hybrid of tri-axial accelerometer and gyroscope,” _Physiol. Meas._ , vol. 39, no. 10, Oct. 2018, Art. no. 105002. 

- [23] S. S. Saha, S. Rahman, M. J. Rasna, A. K. M. Mahfuzul Islam, and A. Rahman Ahad, “DU-MD: An open-source human action dataset for ubiquitous wearable sensors,” in _Proc. Joint 7th Int. Conf. Informat., Electron. Vis. (ICIEV) 2nd Int. Conf. Imag., Vis. Pattern Recognit. (icIVPR)_ , Jun. 2018, pp. 567–572. 

- [24] L. Mart´ınez-Villase˜nor, H. Ponce, J. Brieva, E. Moya-Albor, J. N´u˜nezMart´ıne, and C. Pe˜nafort-Asturiano, “UP-fall detection dataset: A multimodal approach,” _Sensors_ , vol. 19, no. 9, p. 1988, Apr. 2019. 

CAI et al.: FALL MONITORING WITH SINGLE IMU: A LARGE-SCALE DATASET AND A NOVEL DUAL-BRANCH NETWORK 

299 

- [25] M. Saleh, M. Abbas, and R. B. Le Jeann`es, “FallAllD: An open dataset of human falls and activities of daily living for classical and deep learning applications,” _IEEE Sensors J._ , vol. 21, no. 2, pp. 1849–1858, Jan. 2021. 

- [26] X. Yu, J. Jang, and S. Xiong, “A large-scale open motion dataset (KFall) and benchmark algorithms for detecting pre-impact fall of the elderly using wearable inertial sensors,” _Frontiers Aging Neurosci._ , vol. 13, Jul. 2021, Art. no. 692865. 

- [27] Y. Wu, Y. Su, R. Feng, N. Yu, and X. Zang, “Wearable-sensor-based preimpact fall detection system with a hierarchical classifier,” _Measurement_ , vol. 140, pp. 283–292, Jul. 2019. 

- [28] S. Campanella, A. Alnasef, L. Falaschetti, A. Belli, P. Pierleoni, and L. Palma, “A novel embedded deep learning wearable sensor for fall detection,” _IEEE Sensors J._ , vol. 24, no. 9, pp. 15219–15229, May 2024. 

- [29] S. Kiran, Q. Riaz, M. Hussain, M. Zeeshan, and B. Kr¨uger, “Unveiling fall origins: Leveraging wearable sensors to detect pre-impact fall causes,” _IEEE Sensors J._ , vol. 24, no. 15, pp. 24086–24095, Aug. 2024. 

- [30] O. K. Botonis et al., “Wearable airbag technology and machine learned models to mitigate falls after stroke,” _J. Neuroeng. Rehabil._ , vol. 19, no. 1, p. 60, Dec. 2022. 

- [31] C.-L. Lin, Y.-H. Ho, F.-Y. Lin, P.-S. Sung, and C.-Y. Huang, “Fall-risk monitoring in diverse terrains using dual-task learning and wearable sensing system,” _IEEE J. Biomed. Health Informat._ , vol. 29, no. 6, pp. 4059–4070, Jun. 2025. 

- [32] A. Choi et al., “Deep learning-based near-fall detection algorithm for fall risk monitoring system using a single inertial measurement unit,” _IEEE Trans. Neural Syst. Rehabil. Eng._ , vol. 30, pp. 2385–2394, 2022. 

- [33] R. Jain and V. B. Semwal, “A novel feature extraction method for preimpact fall detection system using deep learning and wearable sensors,” _IEEE Sensors J._ , vol. 22, no. 23, pp. 22943–22951, Dec. 2022. 

- [34] M.-K. Yi, K. Han, and S. O. Hwang, “Fall detection of the elderly using denoising LSTM-based convolutional variant autoencoder,” _IEEE Sensors J._ , vol. 24, no. 11, pp. 18556–18567, Jun. 2024. 

- [35] M. A. A. Al-Qaness, Z. Jiang, and J. Shen, “MKLS-Net: Multikernel convolution LSTM and self-attention for fall detection based on wearable sensors,” _IEEE Internet Things J._ , vol. 12, no. 8, pp. 10139–10149, Apr. 2025. 

- [36] S. Wang and J. Wu, “Patch-transformer network: A wearable-sensorbased fall detection method,” _Sensors_ , vol. 23, no. 14, p. 6360, Jul. 2023. 

- [37] J. Chen et al., “A robust deep learning framework based on spectrograms for heart sound classification,” _IEEE_ / _ACM Trans. Comput. Biol. Bioinf._ , vol. 21, no. 4, pp. 936–947, Jul. 2024. 

- [38] Z. Huang, X. Wang, L. Huang, C. Huang, Y. Wei, and W. Liu, “CCNet: Criss-cross attention for semantic segmentation,” in _Proc. IEEE_ / _CVF Int. Conf. Comput. Vis. (ICCV)_ , Oct. 2019, pp. 603–612. 

- [39] G. Fortino, S. Galzarano, R. Gravina, and W. Li, “A framework for collaborative computing and multi-sensor data fusion in body sensor networks,” _Inf. Fusion_ , vol. 22, pp. 50–70, Mar. 2015. 

- [40] S. Iyengar, F. T. Bonda, R. Gravina, A. Guerrieri, G. Fortino, and A. Sangiovanni-Vincentelli, “A framework for creating healthcare monitoring applications using wireless body sensor networks,” in _Proc. 3rd Int. ICST Conf. Body Area Netw._ , 2008, pp. 1–2. 

- [41] A. Cereatti et al., “ISB recommendations on the definition, estimation, and reporting of joint kinematics in human motion analysis applications using wearable inertial measurement technology,” _J. Biomech._ , vol. 173, Aug. 2024, Art. no. 112225. 

- [42] G. Fortino, R. Giannantonio, R. Gravina, P. Kuryloski, and R. Jafari, “Enabling effective programming and flexible management of efficient body sensor network applications,” _IEEE Trans. Human-Mach. Syst._ , vol. 43, no. 1, pp. 115–133, Jan. 2013. 

- [43] M. Saleh, M. Abbas, J. Prud’Homm, D. Somme, and R. Le Bouquin Jeann`es, “A reliable fall detection system based on analyzing the physical activities of older adults living in long-term care facilities,” _IEEE Trans. Neural Syst. Rehabil. Eng._ , vol. 29, pp. 2587–2594, 2021. 

- [44] P. Silsupadol, K.-C. Siu, A. Shumway-Cook, and M. H. Woollacott, “Training of balance under single{-} and dual-task conditions in older adults with balance impairment,” _Phys. Therapy_ , vol. 86, no. 2, pp. 269–281, Feb. 2006. 

- [45] H. M. Toussaint, Y. M. Michies, M. N. Faber, D. A. C. M. Commissaris, and J. H. van Die¨en, “Scaling anticipatory postural adjustments dependent on confidence of load estimation in a bi-manual whole-body lifting task,” _Exp. Brain Res._ , vol. 120, no. 1, pp. 85–94, Apr. 1998. 

- [46] A. Shahzad and K. Kim, “FallDroid: An automated smart-phone-based fall detection system using multiple kernel learning,” _IEEE Trans. Ind. Informat._ , vol. 15, no. 1, pp. 35–44, Jan. 2019. 

- [47] P. Goyal and M. S. Maurer, “Syncope in older adults,” _J. Geriatric Cardiol., JGC_ , vol. 13, no. 5, pp. 380–386, 2016. 

- [48] V. Komisar and S. N. Robinovitch, “The role of fall biomechanics in the cause and prevention of bone fractures in older adults,” _Current Osteoporosis Rep._ , vol. 19, no. 4, pp. 381–390, Aug. 2021. 

- [49] M. Kangas, A. Konttila, P. Lindgren, I. Winblad, and T. J¨ams¨a, “Comparison of low-complexity fall detection algorithms for body attached accelerometers,” _Gait Posture_ , vol. 28, no. 2, pp. 285–291, Aug. 2008. 

- [50] R. Y. W. Lee and A. J. Carlisle, “Detection of falls using accelerometers and mobile phone technology,” _Age Ageing_ , vol. 40, no. 6, pp. 690–696, Nov. 2011. 

- [51] Y. Tanaka and K. Ohno, “Chronic subdural hematoma—An up-to-date concept,” _J. Med. Dental Sci._ , vol. 60, no. 2, pp. 55–61, 2013. 

- [52] W. Wang et al., “Cross-modality LGE-CMR segmentation using imageto-image translation based data augmentation,” _IEEE_ / _ACM Trans. Comput. Biol. Bioinf._ , vol. 20, no. 4, pp. 2367–2375, Jul. 2023. 

- [53] K. He, X. Zhang, S. Ren, and J. Sun, “Deep residual learning for image recognition,” in _Proc. IEEE Conf. Comput. Vis. Pattern Recognit. (CVPR)_ , Jun. 2016, pp. 770–778. 

- [54] C. Zhao, K. Liu, H. Zheng, W. Song, Z. Pei, and W. Chen, “Crossmodality self-attention and fusion-based neural network for lower limb locomotion mode recognition,” _IEEE Trans. Autom. Sci. Eng._ , vol. 22, pp. 5411–5424, 2025. 

- [55] Z. Zhang and M. R. Sabuncu, “Generalized cross entropy loss for training deep neural networks with noisy labels,” in _Proc. Adv. Neural Inf. Process. Syst._ , vol. 31, 2018, pp. 8792–8802. 

- [56] T.-Y. Lin, P. Goyal, R. Girshick, K. He, and P. Doll´ar, “Focal loss for dense object detection,” in _Proc. IEEE Int. Conf. Comput. Vis. (ICCV)_ , Oct. 2017, pp. 2980–2988. 

- [57] A. Paszke et al., “PyTorch: An imperative style, high-performance deep learning library,” in _Proc. Adv. Neural Inf. Process. Syst._ , vol. 32, 2019. 

- [58] T. Tamura, T. Yoshimura, M. Sekine, M. Uchida, and O. Tanaka, “A wearable airbag to prevent fall injuries,” _IEEE Trans. Inf. Technol. Biomed._ , vol. 13, no. 6, pp. 910–914, Nov. 2009. 

- [59] W. Saadeh, S. A. Butt, and M. A. B. Altaf, “A patient-specific single sensor IoT-based wearable fall prediction and detection system,” _IEEE Trans. Neural Syst. Rehabil. Eng._ , vol. 27, no. 5, pp. 995–1003, May 2019. 

