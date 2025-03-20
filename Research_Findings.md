# Research Findings: Biodiversity in National Parks 
## Overview
This study analyzes biodiversity in U.S. National Parks, examining distribution, status, and statistical relationships. Using various technologies including plotting, statistical tests, and machine learning, we were able to better understand and predict the changes in biodiversity between parks.

## Key Findings
### 1. Species Distribution Across National Parks
- The most common species categories in national parks are:
-   **Vascular Plants** (19,560 species)
-   **Birds** (2,364 species)
-   **Mammals** (1,200 species)
- **Evaluation:** Parks with the highest recocrded biodiversity show a prevalence of vascular plants and bird species, suggesting these ecosystems are dominant in national park regions. Further, this reflects the significance of these groups in evaluating the whole biosphere. The dominance of vascular plants aligns with the fact that many national parks contain diverse plant life that thrives in different climates and altitudes. Birds are highly adaptable and found in multiple ecosystems, contributiong to their prevalence. Mammals, though fewer in number, are significant due to their role in park ecosystems, acting as predators, herbivores, or keystone species.
- 

### 2. Conservation Status and Species Risk
- The conservation status distribution:
-   **Not Listed**: 24,752 species
-   **Species of Concern**: 732 species
-   **Endangered**: 80 species
-   **Threatened**: 44 species
-   **In Recovery**: 24 species
- **Evaluation:** The overwhelming majority of species in national parks are **not at risk**, but a significant number fall under protected conservation categories. The large proportion of "Not listed" species indicates that most wildlife in parks is stable, benefitting from the protected nature of the environments. However, the presence of hundreds of at-risk species suggest habitat loss, climate change, or human interference are impacting biodiversity. Species in recover suggest conservation efforts are making progress, but the small number of recovered species highlights the difficulty of restoring populations once they begin to decline.

- ### 3. Chi-Square Test: Conservation Status vs. Species Category
- **Chi-Square Statistic:** 3,130.23
- **P-Value:** 0.0 (highly significant)
- **Evaluation:** There is a strong association between species category and conservation status. Mammals and amphibians have higher proportions of endangered species than vascular plants. This finding makes sense becuase mammals and amphibians often have specific habitat requirements, making them more vulnerable to environmental changes. Vascular plants, in contrast, have wider distribution and adaptation strategies, leading to fewer conservation concerns. Amphibians are particularly sensitive due to the permeable property of their skin, which makes them susceptible to pollution and climate shifts.

- ### 4. ANOVA: Variance in Observations Across Parks
- **F-Statistic:** 81,547.46
- **P-Value:** 0.0 (highly significant)
- **Evaluation:** Species observations differ significantly between parks, indicating variability in biodiversity due to geography, park-size, or ecosystem types. This result aligns with expectations, as national parks differ in size, climate, and habitat diversity, leadning to different biodiversity levels. Larger parks or those with diverse ecosystems (forests, wetlands, mountains) tend to host more species. Some parks may have limited b iodiversity due to their location in extreme environments (e.g., deserts or tundras).
  
## Data Visualizations
![SpeciesCountByCategory](https://github.com/user-attachments/assets/0d4a3a4d-6cc6-46b3-b457-ee76306354ca)
![MostObserved](https://github.com/user-attachments/assets/6886138d-d55c-4fc1-ad26-540cd62bc311)
**Evaluation:** The most observed species are likely those that are common and easily detectable by park monitoring systems. The dominance of certain species in observations could reflect population adundance, but may also indicate biases in data collection methods.

## Predictive Modeling: Identifying Endangered Species
A **Random Forest Classifier** was trained to predict whether a species is endangered based on:
- **Category**
- **Park Name**
- **Observation Count**
### Model Performance
- **Accuracy:** 96.9%
- **Precision & Recall:**
-   Non-Endangered Species (0): High accuracy in identifying these species.
-   Endangered Species (1): Precision is **59%**, but recall is **20%**, meaning the model striggles to detect endangered species as of now.
### Model Insiights
- While the model performs well overall, it struggles with recall for endangered species, likely due to class imbalance (far fewer endangered species in the dataset)
- Improving feature engineering or using oversampling/undersampling techniques could enhance predictive performance.
- The high accuracy suggests the model effectively differentiates between common species and those of concern. The poor recall for endangered species indicated that the model is biased toward the majority class. Further improvements could include incorporating additional environmental variables or balancing the dataset to improve endangered species detection.

## Conclusion & Future Work
National parks host rich biodiversity, with clear trends in conservation status. Furture improvements could include improving endangered specices prediction using more park-specific features. Further, investigating factors in climate and habitat could help determine their effect on observations. By developing an interactive dashboard, we could enhance the visualization and understanding of this data for a wider audience. Overall, this research underscores the importance of nationhal parks in species conservation and highlights areas where further monitoring and pretection efforts could be strengthened. By refining predictive models and exploring additional ecological factors, conservationists can enhance efforts to pretect at-risk species more effectively. 

#**Note: These findings were determined from various tests in the "Analysis.py" script. These can be replicated by running this script in a suitable code environment with the raw data csv files.**
