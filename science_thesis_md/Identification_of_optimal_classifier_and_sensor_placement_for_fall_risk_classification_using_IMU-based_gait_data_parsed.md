### Tóm tắt:
Nghiên cứu đánh giá ảnh hưởng của thuật toán phân loại và vị trí đặt cảm biến đo lường quán tính (IMU) đến độ chính xác của việc phân loại nguy cơ té ngã ở người cao tuổi khi đi bộ. Dữ liệu từ 93 người tham gia cho thấy hiệu suất phân loại phụ thuộc nhiều vào vị trí đặt cảm biến hơn là thuật toán được lựa chọn. Mô hình tối ưu nhất đạt độ chính xác 90,1%, sử dụng thuật toán SVM với cảm biến đặt ở bắp chân trái.

### BibTeX:
```bibtex
@article{park2025identification,
  title={Identification of optimal classifier and sensor placement for fall risk classification using IMU-based gait data},
  author={Park, Junwoo and Lim, Kitaek and Lee, Seyoung and Choi, Jongwon and Choi, Woochol Joseph},
  journal={Gait \& Posture},
  volume={122},
  pages={352--357},
  year={2025},
  publisher={Elsevier},
  doi={10.1016/j.gaitpost.2025.08.068}
}
```

---

## NỘI DUNG BÀI BÁO CHI TIẾT (AI OCR)

ScienceDirect

Gait & Posture
Volume 122, October 2025, Pages 352-357

Identification of optimal classifier and sensor placement for fall risk classification using IMU-based gait data

Junwoo Park, Kitaek Lim, Seyoung Lee, Jongwon Choi, Woochol Joseph Choi ✉

Show more
Share Cite

https://doi.org/10.1016/j.gaitpost.2025.08.068
Get rights and content

Highlights
* Fall risk classification performance was compared using inertial measurement unit data of gait.
* The best classifier was a support vector machine with the left lower leg sensor.
* Classification performance was associated with the sensor placement rather than the classification algorithm.

Abstract

Background
Fall risk can be classified using gait data collected from inertial measurement units (IMU). However, the optimal classifier and placement of IMU sensors to maximize classification performance have not yet been suggested.

Research question
Is there an optimal IMU application strategy that yields the highest accuracy for classifying fall risk during gait?

Methods
Ninety-three community-dwelling older adults were grouped into low or high risk of a fall. Then, kinematic data were acquired with 10 IMU sensors placed on body segments when they walked 10 m. The mean and variance of linear acceleration and angular velocity of IMU data were used as input features. We compared the performance of models trained using support vector machine (SVM), decision tree (DT), random forest (RF), K-nearest neighbors (KNN), extreme gradient boosting (XGBoost), and light gradient boosting machine (LightGBM) to evaluate the optimal combination of classification algorithm and sensor placement.

Results
Sensor placement was associated with the classification performance (F = 7.39, p < 0.001), and the lower leg was the optimal sensor placement yielding the highest accuracy. However, neither the classification algorithm nor their interaction showed significant effects (p > 0.05). The best classification performance was achieved by the SVM using the left lower leg sensor with 90.1 % accuracy, 95.7 % sensitivity, and 84.1 % specificity.

Significance
Fall risk classification performance was affected by the placement of IMU sensors, with the lower leg showing the highest classification accuracy. Our results should provide insights to advance fall prevention technology in older adults.

Introduction
Falls are common in older adults. A quarter of community-dwelling older adults experience falls every year [1]. Over one-third of older adults report at least one fall requiring medical treatment [2]. Furthermore, falls often lead to death, and the fall death rate has increased by 111 % from 2007 (18,334 deaths) to 2021 (38,742 deaths) [3], [4]. However, falls are preventable events, and therefore, continuous research efforts are needed to prevent falls in older adults.

Gait impairments have been suggested as risk factors for falls in older adults. Fletcher & Hirdes have suggested that older adults with impaired gait are 2.5 times more likely to experience falls [5]. Allali et al. have suggested that gait parameters are associated with fall history in older adults [6]. Brodie et al. have suggested that fallers show significantly decreased gait quality (i.e., lower gait endurance, higher within-walk variability, and lower between-walk adaptability) and declined Timed Up-and-Go test (TUG) performance [7]. These findings collectively support that a strong correlation exists between gait and the risk of falls in older adults.

Efforts have been made to predict one's fall risk using inertial measurement unit (IMU) data of gait. Garcia-de-Villa et al. have suggested that gait parameters (i.e., stride length) identified with a foot-mounted IMU may predict the likelihood of a severe fall causing injuries and/or loss of consciousness, with 80% accuracy using a support vector machine (SVM) [8]. Qiu et al. have suggested that fall risk can be predicted with IMU data acquired from three body parts (lower back, upper leg, and lower leg) using SVM with 90% accuracy [9]. Nishiyama et al. have suggested that features of IMU data collected at the waist during gait can be used to classify fall risk with 94% accuracy using a gradient-boosting decision tree (DT) (LightGBM) [10]. Noh et al. also have suggested that the extreme gradient boosting (XGBoost) shows 70% accuracy to classify fall risk with bilateral foot insole IMU sensors [11]. Drover et al. have suggested that straight walking features from IMU data of the pelvis and shanks can also be used to classify potential falls with 62% accuracy using random forest (RF) [12]. However, these studies have utilized IMU data from certain body parts, excluding arms and heads, which are known to play an important role in gait stability [13], [14]. Furthermore, previous studies reported considerable variability in classification performance across models, indicating a lack of consistency. This limitation highlights the importance of identifying optimal sensor placement and a classification algorithm to enhance fall risk classification performance.

TUG and Tinetti scales are fall risk assessment tools commonly used in clinics, but these are subjective, and no consensus exists on the optimal cut-off values for classifying high versus low fall risk [8], [15]. Downton Fall Risk Index and Berg Balance Scale are also common in assessing one's risk of a fall, but they all have the same limitation [16], [17]. In contrast, a physiological profile assessment tool (PPA) provides comprehensive fall risk scores and an age-specific normal range, which can be used as cut-off values to identify individuals at risk [18]. The PPA assesses 5 physiological factors related to one's balance ability. The Melbourne Edge test assesses participants' visual contrast sensitivity by requiring them to identify the direction of contrast edges on circular patches presented at various angles (horizontal, vertical, diagonal) using a PPA keycard [18], [19], [20]. The proprioception test measures the degree of differences between the right and left toes with the eyes closed during knee extension and flexion [18], [19], [20]. The hand reaction time test measures reaction time with a switch on a modified computer mouse when a red light next to the switch is activated [18], [19], [20]. The knee extension strength test assesses the knee extensor strength recorded in kilograms with a strap connected to a spring gauge placed around the legs to measure the strength of the dominant leg [18], [19], [20]. The postural sway test records movements of the body in 2 directions (anterior-posterior, medial-lateral) using a rod connected to the belt at the waist while standing on the PPA rubber mat for 30 s [18], [19], [20]. These objective assessments, which normally require approximately 45 min per participant, provide a more nuanced and quantifiable evaluation of an individual's fall risk. To improve clinical feasibility, Lord et al. introduced a short-form version of the PPA, and this abbreviated assessment takes only 15 min and has been shown to yield comparable results in terms of overall fall risk classification [18].

Against the background, we used the short-form PPA to group older adults into high or low risk of a fall. We then collected data with IMU sensors placed on 10 different body parts while walking. The extracted features of IMU data were then used to classify the group. The aim of this study was to suggest the optimal combinations of sensor placement and classification algorithm needed to achieve the best performance in classifying fall risk using IMU data of gait.

Access through your organization
Check access to the full text by signing in through your organization.
Access through your organization

Section snippets

Participants
Ninety-three community-dwelling older adults (19 males, 74 females) participated. On average, participants' age, height, and weight were 77.8 (SD 7.1) years, 153.9 (7.6) cm, and 57.5 (8) kg, respectively. 15 (16%) reported using a mobility aid in daily life. However, all were able to walk 10 m without assistance from their aides. Exclusion criteria included participants who could not walk independently without walking aids for 10 m, and/or diagnosed with neurological diseases or debilitating ...

Results
Among 93 older adults, 42 (6 males, 36 females) were at high risk of a fall, and 51 (13 males, 38 females) were at low risk. The PPA fall risk score averaged 3.7 (SD = 1.8) and 1.3 (SD = 1.7) for the high and low risk groups, respectively. Demographic information for each group is shown in Table 2.

The two-way ANOVA revealed a significant main effect of sensor placement on classification accuracy (F = 7.39, p < 0.001), suggesting that sensors placed on the lower leg yielded significantly higher ...

Discussion
The purpose of this study was to suggest the most appropriate classification algorithm and the placement of IMU sensors required to generate the best-performing fall risk classification model while walking. We found that classification performance depended on the placement of sensors. The best performance was observed when the sensor was placed on the left lower leg, achieving 90.1 % accuracy with SVM. In contrast, the poorest performance occurred with a sensor on the head, where the same ...

Conclusion
We evaluated the impact of classifier selection and IMU sensor placement on the accuracy of fall risk classification using gait data. The results indicated that classification accuracy was influenced by sensor placement, while the choice of classifier had a negligible effect. The highest overall performance was achieved using an SVM model with data collected from the left lower leg. These findings offer valuable insights for the advancement of fall prevention technologies targeting older adults. ...

CRediT authorship contribution statement
Junwoo Park: Writing – original draft, Visualization, Validation, Software, Methodology, Investigation, Formal analysis, Data curation, Conceptualization. Kitaek Lim: Investigation, Data curation. Seyoung Lee: Investigation. Jongwon Choi: Investigation. Woochol Joseph Choi: Writing – review & editing, Validation, Resources, Project administration, Methodology, Funding acquisition, Conceptualization. ...

Declaration of Competing Interest
None of the authors above have any financial or personal relationships with other people or organizations that could inappropriately influence this work, including employment, consultancies, stock ownership, honoraria, paid expert testimony, patent applications/registrations, and grants or other funding. ...

Acknowledgments
This work was supported, in part, by the Brain Korea 21 FOUR Project, the National Research Foundation of Korea (NRF) for the Department of Physical Therapy in the Graduate School of Yonsei University, and by the Regional Innovation Strategy (RIS) program through the National Research Foundation of Korea (NRF) funded by the Ministry of Education (MOE), Republic of Korea (Grant No. 2022RIS-005). ...

Recommended articles

References (28)

G. Allali et al.
Falls, cognitive impairment, and gait performance: results from the GOOD initiative
J. Am. Med. Dir. Assoc. (2017)

D. Nishiyama et al.
Accurate fall risk classification in elderly using one gait cycle data and machine learning
Clin. Biomech. (2024)

J.D. Ortega et al.
Effects of aging and arm swing on the metabolic cost of stability in human walking
J. Biomech. (2008)

M.W. Rivolta et al.
Evaluation of the tinetti score and fall risk assessment via accelerometry-based movement analysis
Artif. Intell. Med. (2019)

M.J. Bueno-García et al.
Characteristics of the downton fall risk assessment scale in hospitalised patients
Enfermería Clínica (2017)

T. Kim et al.
Epidemiology of fall and its socioeconomic risk factors in community-dwelling Korean elderly
PLoS One (2020)

G. Bergen
Falls and fall injuries among adults aged ≥ 65 years—United States, 2014
MMWR Morb. Mortal. Wkly. Rep. (2016)

E. Burns
Deaths from falls among persons aged ≥ 65 years—United States, 2007–2016
MMWR Morb. Mortal. Wkly. Rep. (2018)

R. Kakara
Nonfatal and fatal falls among adults aged ≥ 65 years—United States, 2020–2021
MMWR Morb. Mortal. Wkly. Rep. (2023)

P.C. Fletcher et al.
Risk factors for serious falls among community-based seniors: results from The National population health survey
Can. J. Aging/La Rev. Can. du Vieil. (2002)

View more references

Cited by (0)

View full text

© 2025 Elsevier B.V. All rights reserved, including those for text and data mining, AI training, and similar technologies.