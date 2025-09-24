# Comprehensive Confusion Matrices - Gemini 2.5 Flash Results

**Experiment**: Gemini 2.5 Flash - Subnarrative Validation Devset  
**Model**: Google Gemini 2.5 Flash  
**Languages Analyzed**: BG, EN, HI, PT, RU  
**Analysis Type**: Per-Label Confusion Matrices  

This document provides detailed confusion matrices for every narrative and subnarrative label in every language analyzed by Gemini 2.5 Flash.


## Summary Statistics

### Performance Overview by Language

| Language | Model | Files | Narratives F1 | Subnarratives F1 | Narratives Labels | Subnarratives Labels |
|----------|-------|-------|---------------|------------------|-------------------|----------------------|
| BG | Google Gemini 2.5 Flash | 35 | 0.5521 | 0.4211 | 21 | 67 |
| EN | Google Gemini 2.5 Flash | 41 | 0.5319 | 0.4166 | 22 | 80 |
| HI | Google Gemini 2.5 Flash | 35 | 0.4354 | 0.2687 | 13 | 42 |
| PT | Google Gemini 2.5 Flash | 35 | 0.6904 | 0.4367 | 15 | 41 |
| RU | Google Gemini 2.5 Flash | 32 | 0.6693 | 0.5078 | 11 | 40 |

### Label Distribution Statistics

**Narratives:**
- Total unique labels across all languages: 22
- Total confusion matrices generated: 82

**Subnarratives:**
- Total unique labels across all languages: 89
- Total confusion matrices generated: 270


---

# Detailed Confusion Matrices


## Narratives Confusion Matrices


### BG - Narratives

**Language**: BG  
**Model**: Google Gemini 2.5 Flash  
**Total Files**: 35  
**Total Labels**: 21  
**F1 Macro**: 0.3861  
**F1 Micro**: 0.5298  
**F1 Samples**: 0.5521  

#### Confusion Matrix Summary Table (21 labels)

| Label | F1 | Precision | Recall | Support | TP | FP | FN | TN |
|-------|----|-----------|--------|---------|----|----|----|----|
| CC: Amplifying Climate Fears | 0.947 | 0.900 | 1.000 |   9 |  9 |  1 |  0 |  25 |
| URW: Discrediting Ukraine | 0.833 | 0.714 | 1.000 |   5 |  5 |  2 |  0 |  28 |
| URW: Praise of Russia | 0.800 | 0.667 | 1.000 |   2 |  2 |  1 |  0 |  32 |
| URW: Amplifying war-related fears | 0.769 | 0.625 | 1.000 |   5 |  5 |  3 |  0 |  27 |
| CC: Criticism of climate movement | 0.667 | 0.500 | 1.000 |   1 |  1 |  1 |  0 |  33 |
| CC: Hidden plots by secret schemes of powerful groups | 0.667 | 1.000 | 0.500 |   2 |  1 |  0 |  1 |  33 |
| CC: Downplaying climate change | 0.571 | 0.667 | 0.500 |   4 |  2 |  1 |  2 |  30 |
| URW: Russia is the Victim | 0.545 | 0.375 | 1.000 |   3 |  3 |  5 |  0 |  27 |
| CC: Criticism of climate policies | 0.500 | 0.500 | 0.500 |   2 |  1 |  1 |  1 |  32 |
| CC: Criticism of institutions and authorities | 0.500 | 0.400 | 0.667 |   3 |  2 |  3 |  1 |  29 |
| URW: Discrediting the West, Diplomacy | 0.500 | 0.333 | 1.000 |   5 |  5 | 10 |  0 |  20 |
| Other | 0.444 | 0.667 | 0.333 |   6 |  2 |  1 |  4 |  28 |
| URW: Negative Consequences for the West | 0.364 | 0.250 | 0.667 |   3 |  2 |  6 |  1 |  26 |
| CC: Controversy about green technologies | 0.000 | 0.000 | 0.000 |   0 |  0 |  4 |  0 |  31 |
| CC: Green policies are geopolitical instruments | 0.000 | 0.000 | 0.000 |   1 |  0 |  2 |  1 |  32 |
| CC: Questioning the measurements and science | 0.000 | 0.000 | 0.000 |   0 |  0 |  2 |  0 |  33 |
| URW: Blaming the war on others rather than the inv... | 0.000 | 0.000 | 0.000 |   2 |  0 |  5 |  2 |  28 |
| URW: Distrust towards Media | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 |  34 |
| URW: Hidden plots by secret schemes of powerful gr... | 0.000 | 0.000 | 0.000 |   0 |  0 |  3 |  0 |  32 |
| URW: Overpraising the West | 0.000 | 0.000 | 0.000 |   1 |  0 |  0 |  1 |  34 |
| URW: Speculating war outcomes | 0.000 | 0.000 | 0.000 |   0 |  0 |  5 |  0 |  30 |

**Legend:**
- **TP**: True Positives (correctly predicted positive)
- **FP**: False Positives (incorrectly predicted positive)
- **FN**: False Negatives (incorrectly predicted negative)
- **TN**: True Negatives (correctly predicted negative)


### EN - Narratives

**Language**: EN  
**Model**: Google Gemini 2.5 Flash  
**Total Files**: 41  
**Total Labels**: 22  
**F1 Macro**: 0.4776  
**F1 Micro**: 0.5597  
**F1 Samples**: 0.5319  

#### Confusion Matrix Summary Table (22 labels)

| Label | F1 | Precision | Recall | Support | TP | FP | FN | TN |
|-------|----|-----------|--------|---------|----|----|----|----|
| CC: Questioning the measurements and science | 0.889 | 0.800 | 1.000 |   4 |  4 |  1 |  0 |  36 |
| URW: Blaming the war on others rather than the inv... | 0.857 | 0.750 | 1.000 |   6 |  6 |  2 |  0 |  33 |
| URW: Discrediting the West, Diplomacy | 0.857 | 0.750 | 1.000 |   9 |  9 |  3 |  0 |  29 |
| URW: Discrediting Ukraine | 0.824 | 0.700 | 1.000 |   7 |  7 |  3 |  0 |  31 |
| URW: Distrust towards Media | 0.727 | 0.571 | 1.000 |   4 |  4 |  3 |  0 |  34 |
| CC: Climate change is beneficial | 0.667 | 0.500 | 1.000 |   1 |  1 |  1 |  0 |  39 |
| Other | 0.588 | 0.833 | 0.455 |  11 |  5 |  1 |  6 |  29 |
| CC: Green policies are geopolitical instruments | 0.571 | 0.500 | 0.667 |   3 |  2 |  2 |  1 |  36 |
| URW: Russia is the Victim | 0.571 | 0.400 | 1.000 |   2 |  2 |  3 |  0 |  36 |
| CC: Criticism of climate movement | 0.545 | 0.429 | 0.750 |   8 |  6 |  8 |  2 |  25 |
| CC: Criticism of institutions and authorities | 0.545 | 0.429 | 0.750 |   8 |  6 |  8 |  2 |  25 |
| CC: Controversy about green technologies | 0.500 | 0.333 | 1.000 |   2 |  2 |  4 |  0 |  35 |
| URW: Amplifying war-related fears | 0.462 | 0.300 | 1.000 |   3 |  3 |  7 |  0 |  31 |
| CC: Hidden plots by secret schemes of powerful groups | 0.444 | 0.400 | 0.500 |   4 |  2 |  3 |  2 |  34 |
| URW: Speculating war outcomes | 0.429 | 0.300 | 0.750 |   4 |  3 |  7 |  1 |  30 |
| CC: Downplaying climate change | 0.364 | 0.222 | 1.000 |   2 |  2 |  7 |  0 |  32 |
| CC: Criticism of climate policies | 0.333 | 0.200 | 1.000 |   3 |  3 | 12 |  0 |  26 |
| URW: Praise of Russia | 0.333 | 0.250 | 0.500 |   2 |  1 |  3 |  1 |  36 |
| CC: Amplifying Climate Fears | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 |  40 |
| URW: Hidden plots by secret schemes of powerful gr... | 0.000 | 0.000 | 0.000 |   0 |  0 |  3 |  0 |  38 |
| URW: Negative Consequences for the West | 0.000 | 0.000 | 0.000 |   1 |  0 |  8 |  1 |  32 |
| URW: Overpraising the West | 0.000 | 0.000 | 0.000 |   1 |  0 |  0 |  1 |  40 |

**Legend:**
- **TP**: True Positives (correctly predicted positive)
- **FP**: False Positives (incorrectly predicted positive)
- **FN**: False Negatives (incorrectly predicted negative)
- **TN**: True Negatives (correctly predicted negative)


### HI - Narratives

**Language**: HI  
**Model**: Google Gemini 2.5 Flash  
**Total Files**: 35  
**Total Labels**: 13  
**F1 Macro**: 0.3837  
**F1 Micro**: 0.4645  
**F1 Samples**: 0.4354  

#### Confusion Matrix Summary Table (13 labels)

| Label | F1 | Precision | Recall | Support | TP | FP | FN | TN |
|-------|----|-----------|--------|---------|----|----|----|----|
| URW: Amplifying war-related fears | 0.824 | 0.778 | 0.875 |   8 |  7 |  2 |  1 |  25 |
| CC: Amplifying Climate Fears | 0.667 | 1.000 | 0.500 |   4 |  2 |  0 |  2 |  31 |
| URW: Praise of Russia | 0.571 | 0.750 | 0.462 |  13 |  6 |  2 |  7 |  20 |
| URW: Discrediting the West, Diplomacy | 0.522 | 0.375 | 0.857 |   7 |  6 | 10 |  1 |  18 |
| URW: Distrust towards Media | 0.500 | 0.500 | 0.500 |   2 |  1 |  1 |  1 |  32 |
| URW: Russia is the Victim | 0.435 | 0.357 | 0.556 |   9 |  5 |  9 |  4 |  17 |
| URW: Speculating war outcomes | 0.400 | 0.300 | 0.600 |   5 |  3 |  7 |  2 |  23 |
| URW: Blaming the war on others rather than the inv... | 0.375 | 0.273 | 0.600 |   5 |  3 |  8 |  2 |  22 |
| URW: Discrediting Ukraine | 0.250 | 0.200 | 0.333 |   3 |  1 |  4 |  2 |  28 |
| Other | 0.222 | 0.143 | 0.500 |   2 |  1 |  6 |  1 |  27 |
| URW: Negative Consequences for the West | 0.222 | 0.167 | 0.333 |   3 |  1 |  5 |  2 |  27 |
| URW: Hidden plots by secret schemes of powerful gr... | 0.000 | 0.000 | 0.000 |   2 |  0 |  0 |  2 |  33 |
| URW: Overpraising the West | 0.000 | 0.000 | 0.000 |   2 |  0 |  0 |  2 |  33 |

**Legend:**
- **TP**: True Positives (correctly predicted positive)
- **FP**: False Positives (incorrectly predicted positive)
- **FN**: False Negatives (incorrectly predicted negative)
- **TN**: True Negatives (correctly predicted negative)


### PT - Narratives

**Language**: PT  
**Model**: Google Gemini 2.5 Flash  
**Total Files**: 35  
**Total Labels**: 15  
**F1 Macro**: 0.4909  
**F1 Micro**: 0.7287  
**F1 Samples**: 0.6904  

#### Confusion Matrix Summary Table (15 labels)

| Label | F1 | Precision | Recall | Support | TP | FP | FN | TN |
|-------|----|-----------|--------|---------|----|----|----|----|
| URW: Amplifying war-related fears | 1.000 | 1.000 | 1.000 |   1 |  1 |  0 |  0 |  34 |
| URW: Discrediting Ukraine | 1.000 | 1.000 | 1.000 |   3 |  3 |  0 |  0 |  32 |
| URW: Praise of Russia | 0.889 | 0.800 | 1.000 |   4 |  4 |  1 |  0 |  30 |
| CC: Amplifying Climate Fears | 0.878 | 1.000 | 0.783 |  23 | 18 |  0 |  5 |  12 |
| URW: Discrediting the West, Diplomacy | 0.875 | 0.875 | 0.875 |   8 |  7 |  1 |  1 |  26 |
| URW: Russia is the Victim | 0.857 | 0.750 | 1.000 |   3 |  3 |  1 |  0 |  31 |
| CC: Criticism of institutions and authorities | 0.737 | 0.636 | 0.875 |   8 |  7 |  4 |  1 |  23 |
| URW: Negative Consequences for the West | 0.667 | 0.500 | 1.000 |   1 |  1 |  1 |  0 |  33 |
| CC: Criticism of climate policies | 0.462 | 0.750 | 0.333 |   9 |  3 |  1 |  6 |  25 |
| CC: Controversy about green technologies | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 |  34 |
| CC: Green policies are geopolitical instruments | 0.000 | 0.000 | 0.000 |   0 |  0 |  2 |  0 |  33 |
| CC: Hidden plots by secret schemes of powerful groups | 0.000 | 0.000 | 0.000 |   1 |  0 |  0 |  1 |  34 |
| Other | 0.000 | 0.000 | 0.000 |   1 |  0 |  3 |  1 |  31 |
| URW: Blaming the war on others rather than the inv... | 0.000 | 0.000 | 0.000 |   0 |  0 |  3 |  0 |  32 |
| URW: Speculating war outcomes | 0.000 | 0.000 | 0.000 |   0 |  0 |  2 |  0 |  33 |

**Legend:**
- **TP**: True Positives (correctly predicted positive)
- **FP**: False Positives (incorrectly predicted positive)
- **FN**: False Negatives (incorrectly predicted negative)
- **TN**: True Negatives (correctly predicted negative)


### RU - Narratives

**Language**: RU  
**Model**: Google Gemini 2.5 Flash  
**Total Files**: 32  
**Total Labels**: 11  
**F1 Macro**: 0.5065  
**F1 Micro**: 0.6753  
**F1 Samples**: 0.6693  

#### Confusion Matrix Summary Table (11 labels)

| Label | F1 | Precision | Recall | Support | TP | FP | FN | TN |
|-------|----|-----------|--------|---------|----|----|----|----|
| Other | 0.889 | 0.800 | 1.000 |   4 |  4 |  1 |  0 |  27 |
| URW: Discrediting Ukraine | 0.882 | 0.789 | 1.000 |  15 | 15 |  4 |  0 |  13 |
| URW: Praise of Russia | 0.857 | 0.923 | 0.800 |  15 | 12 |  1 |  3 |  16 |
| URW: Discrediting the West, Diplomacy | 0.710 | 0.688 | 0.733 |  15 | 11 |  5 |  4 |  12 |
| URW: Amplifying war-related fears | 0.667 | 0.500 | 1.000 |   2 |  2 |  2 |  0 |  28 |
| URW: Russia is the Victim | 0.500 | 0.400 | 0.667 |   3 |  2 |  3 |  1 |  26 |
| URW: Speculating war outcomes | 0.400 | 0.250 | 1.000 |   3 |  3 |  9 |  0 |  20 |
| URW: Negative Consequences for the West | 0.333 | 0.200 | 1.000 |   1 |  1 |  4 |  0 |  27 |
| URW: Blaming the war on others rather than the inv... | 0.333 | 0.250 | 0.500 |   4 |  2 |  6 |  2 |  22 |
| URW: Distrust towards Media | 0.000 | 0.000 | 0.000 |   2 |  0 |  1 |  2 |  29 |
| URW: Hidden plots by secret schemes of powerful gr... | 0.000 | 0.000 | 0.000 |   1 |  0 |  1 |  1 |  30 |

**Legend:**
- **TP**: True Positives (correctly predicted positive)
- **FP**: False Positives (incorrectly predicted positive)
- **FN**: False Negatives (incorrectly predicted negative)
- **TN**: True Negatives (correctly predicted negative)


## Subnarratives Confusion Matrices


### BG - Subnarratives

**Language**: BG  
**Model**: Google Gemini 2.5 Flash  
**Total Files**: 35  
**Total Labels**: 67  
**F1 Macro**: 0.2747  
**F1 Micro**: 0.4017  
**F1 Samples**: 0.4211  

#### Confusion Matrix Summary Table (67 labels)

| Label | F1 | Precision | Recall | Support | TP | FP | FN | TN |
|-------|----|-----------|--------|---------|----|----|----|----|
| CC: Criticism of climate movement: Climate movemen... | 1.000 | 1.000 | 1.000 |   1 |  1 |  0 |  0 |  34 |
| CC: Criticism of climate policies: Climate policie... | 1.000 | 1.000 | 1.000 |   1 |  1 |  0 |  0 |  34 |
| CC: Downplaying climate change: Climate cycles are... | 1.000 | 1.000 | 1.000 |   1 |  1 |  0 |  0 |  34 |
| CC: Hidden plots by secret schemes of powerful gro... | 1.000 | 1.000 | 1.000 |   1 |  1 |  0 |  0 |  34 |
| URW: Amplifying war-related fears: By continuing t... | 1.000 | 1.000 | 1.000 |   1 |  1 |  0 |  0 |  34 |
| URW: Amplifying war-related fears: There is a real... | 1.000 | 1.000 | 1.000 |   2 |  2 |  0 |  0 |  33 |
| URW: Praise of Russia: Praise of Russian President... | 1.000 | 1.000 | 1.000 |   1 |  1 |  0 |  0 |  34 |
| URW: Praise of Russia: Russia has international su... | 1.000 | 1.000 | 1.000 |   1 |  1 |  0 |  0 |  34 |
| CC: Amplifying Climate Fears: Amplifying existing ... | 0.947 | 0.900 | 1.000 |   9 |  9 |  1 |  0 |  25 |
| URW: Russia is the Victim: The West is russophobic | 0.857 | 0.750 | 1.000 |   3 |  3 |  1 |  0 |  31 |
| CC: Criticism of climate movement: Other | 0.667 | 0.500 | 1.000 |   1 |  1 |  1 |  0 |  33 |
| CC: Criticism of institutions and authorities: Cri... | 0.667 | 0.500 | 1.000 |   1 |  1 |  1 |  0 |  33 |
| URW: Praise of Russia: Praise of Russian military ... | 0.667 | 0.500 | 1.000 |   1 |  1 |  1 |  0 |  33 |
| URW: Discrediting Ukraine: Discrediting Ukrainian ... | 0.571 | 0.400 | 1.000 |   2 |  2 |  3 |  0 |  30 |
| URW: Discrediting Ukraine: Ukraine is a puppet of ... | 0.571 | 0.400 | 1.000 |   2 |  2 |  3 |  0 |  30 |
| CC: Criticism of institutions and authorities: Cri... | 0.500 | 0.500 | 0.500 |   2 |  1 |  1 |  1 |  32 |
| CC: Downplaying climate change: Weather suggests t... | 0.500 | 1.000 | 0.333 |   3 |  1 |  0 |  2 |  32 |
| URW: Amplifying war-related fears: Other | 0.500 | 0.333 | 1.000 |   2 |  2 |  4 |  0 |  29 |
| URW: Amplifying war-related fears: Russia will als... | 0.500 | 0.333 | 1.000 |   1 |  1 |  2 |  0 |  32 |
| URW: Discrediting Ukraine: Ukraine is a hub for cr... | 0.500 | 0.333 | 1.000 |   1 |  1 |  2 |  0 |  32 |
| URW: Discrediting Ukraine: Ukraine is associated w... | 0.500 | 0.333 | 1.000 |   1 |  1 |  2 |  0 |  32 |
| URW: Discrediting the West, Diplomacy: Other | 0.471 | 0.333 | 0.800 |   5 |  4 |  8 |  1 |  22 |
| CC: Amplifying Climate Fears: Doomsday scenarios f... | 0.444 | 0.286 | 1.000 |   2 |  2 |  5 |  0 |  28 |
| Other | 0.444 | 0.667 | 0.333 |   6 |  2 |  1 |  4 |  28 |
| URW: Discrediting Ukraine: Discrediting Ukrainian ... | 0.400 | 0.250 | 1.000 |   1 |  1 |  3 |  0 |  31 |
| URW: Negative Consequences for the West: Other | 0.364 | 0.250 | 0.667 |   3 |  2 |  6 |  1 |  26 |
| CC: Amplifying Climate Fears: Other | 0.333 | 0.500 | 0.250 |   4 |  1 |  1 |  3 |  30 |
| CC: Amplifying Climate Fears: Earth will be uninha... | 0.000 | 0.000 | 0.000 |   0 |  0 |  2 |  0 |  33 |
| CC: Amplifying Climate Fears: Whatever we do it is... | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 |  34 |
| CC: Controversy about green technologies: Other | 0.000 | 0.000 | 0.000 |   0 |  0 |  4 |  0 |  31 |
| CC: Controversy about green technologies: Renewabl... | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 |  34 |
| CC: Controversy about green technologies: Renewabl... | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 |  34 |
| CC: Criticism of climate movement: Ad hominem atta... | 0.000 | 0.000 | 0.000 |   1 |  0 |  1 |  1 |  33 |
| CC: Criticism of climate policies: Climate policie... | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 |  34 |
| CC: Criticism of climate policies: Climate policie... | 0.000 | 0.000 | 0.000 |   1 |  0 |  0 |  1 |  34 |
| CC: Criticism of climate policies: Other | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 |  34 |
| CC: Criticism of institutions and authorities: Cri... | 0.000 | 0.000 | 0.000 |   0 |  0 |  2 |  0 |  33 |
| CC: Criticism of institutions and authorities: Cri... | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 |  34 |
| CC: Criticism of institutions and authorities: Other | 0.000 | 0.000 | 0.000 |   0 |  0 |  2 |  0 |  33 |
| CC: Downplaying climate change: Other | 0.000 | 0.000 | 0.000 |   0 |  0 |  3 |  0 |  32 |
| CC: Green policies are geopolitical instruments: C... | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 |  34 |
| CC: Green policies are geopolitical instruments: G... | 0.000 | 0.000 | 0.000 |   1 |  0 |  0 |  1 |  34 |
| CC: Green policies are geopolitical instruments: O... | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 |  34 |
| CC: Hidden plots by secret schemes of powerful gro... | 0.000 | 0.000 | 0.000 |   1 |  0 |  1 |  1 |  33 |
| CC: Hidden plots by secret schemes of powerful gro... | 0.000 | 0.000 | 0.000 |   1 |  0 |  0 |  1 |  34 |
| CC: Questioning the measurements and science: Data... | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 |  34 |
| CC: Questioning the measurements and science: Other | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 |  34 |
| CC: Questioning the measurements and science: Scie... | 0.000 | 0.000 | 0.000 |   0 |  0 |  2 |  0 |  33 |
| URW: Amplifying war-related fears: NATO should/wil... | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 |  34 |
| URW: Blaming the war on others rather than the inv... | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 |  34 |
| URW: Blaming the war on others rather than the inv... | 0.000 | 0.000 | 0.000 |   1 |  0 |  4 |  1 |  30 |
| URW: Blaming the war on others rather than the inv... | 0.000 | 0.000 | 0.000 |   1 |  0 |  1 |  1 |  33 |
| URW: Discrediting Ukraine: Discrediting Ukrainian ... | 0.000 | 0.000 | 0.000 |   0 |  0 |  4 |  0 |  31 |
| URW: Discrediting Ukraine: Situation in Ukraine is... | 0.000 | 0.000 | 0.000 |   0 |  0 |  2 |  0 |  33 |
| URW: Discrediting the West, Diplomacy: Diplomacy d... | 0.000 | 0.000 | 0.000 |   0 |  0 |  2 |  0 |  33 |
| URW: Discrediting the West, Diplomacy: The EU is d... | 0.000 | 0.000 | 0.000 |   0 |  0 |  2 |  0 |  33 |
| URW: Discrediting the West, Diplomacy: The West do... | 0.000 | 0.000 | 0.000 |   0 |  0 |  4 |  0 |  31 |
| URW: Discrediting the West, Diplomacy: The West is... | 0.000 | 0.000 | 0.000 |   0 |  0 |  4 |  0 |  31 |
| URW: Distrust towards Media: Ukrainian media canno... | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 |  34 |
| URW: Distrust towards Media: Western media is an i... | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 |  34 |
| URW: Hidden plots by secret schemes of powerful gr... | 0.000 | 0.000 | 0.000 |   0 |  0 |  3 |  0 |  32 |
| URW: Overpraising the West: The West belongs in th... | 0.000 | 0.000 | 0.000 |   1 |  0 |  0 |  1 |  34 |
| URW: Praise of Russia: Other | 0.000 | 0.000 | 0.000 |   0 |  0 |  2 |  0 |  33 |
| URW: Russia is the Victim: Other | 0.000 | 0.000 | 0.000 |   0 |  0 |  7 |  0 |  28 |
| URW: Russia is the Victim: Russia actions in Ukrai... | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 |  34 |
| URW: Russia is the Victim: UA is anti-RU extremists | 0.000 | 0.000 | 0.000 |   0 |  0 |  2 |  0 |  33 |
| URW: Speculating war outcomes: Other | 0.000 | 0.000 | 0.000 |   0 |  0 |  5 |  0 |  30 |

**Legend:**
- **TP**: True Positives (correctly predicted positive)
- **FP**: False Positives (incorrectly predicted positive)
- **FN**: False Negatives (incorrectly predicted negative)
- **TN**: True Negatives (correctly predicted negative)


### EN - Subnarratives

**Language**: EN  
**Model**: Google Gemini 2.5 Flash  
**Total Files**: 41  
**Total Labels**: 80  
**F1 Macro**: 0.3062  
**F1 Micro**: 0.4038  
**F1 Samples**: 0.4166  

#### Confusion Matrix Summary Table (80 labels)

| Label | F1 | Precision | Recall | Support | TP | FP | FN | TN |
|-------|----|-----------|--------|---------|----|----|----|----|
| CC: Climate change is beneficial: CO2 is beneficial | 1.000 | 1.000 | 1.000 |   1 |  1 |  0 |  0 |  40 |
| CC: Criticism of climate policies: Climate policie... | 1.000 | 1.000 | 1.000 |   1 |  1 |  0 |  0 |  40 |
| CC: Downplaying climate change: Human activities d... | 1.000 | 1.000 | 1.000 |   2 |  2 |  0 |  0 |  39 |
| URW: Discrediting the West, Diplomacy: The EU is d... | 1.000 | 1.000 | 1.000 |   1 |  1 |  0 |  0 |  40 |
| URW: Praise of Russia: Russia is a guarantor of pe... | 1.000 | 1.000 | 1.000 |   1 |  1 |  0 |  0 |  40 |
| URW: Blaming the war on others rather than the inv... | 0.857 | 0.750 | 1.000 |   6 |  6 |  2 |  0 |  33 |
| CC: Hidden plots by secret schemes of powerful gro... | 0.800 | 0.667 | 1.000 |   2 |  2 |  1 |  0 |  38 |
| URW: Discrediting Ukraine: Ukraine is associated w... | 0.800 | 0.667 | 1.000 |   2 |  2 |  1 |  0 |  38 |
| CC: Criticism of institutions and authorities: Cri... | 0.750 | 0.600 | 1.000 |   6 |  6 |  4 |  0 |  31 |
| URW: Discrediting the West, Diplomacy: Diplomacy d... | 0.750 | 0.600 | 1.000 |   3 |  3 |  2 |  0 |  36 |
| URW: Discrediting the West, Diplomacy: The West do... | 0.727 | 0.571 | 1.000 |   4 |  4 |  3 |  0 |  34 |
| URW: Discrediting the West, Diplomacy: Other | 0.667 | 0.556 | 0.833 |   6 |  5 |  4 |  1 |  31 |
| CC: Criticism of climate movement: Climate movemen... | 0.667 | 0.500 | 1.000 |   4 |  4 |  4 |  0 |  33 |
| URW: Amplifying war-related fears: There is a real... | 0.667 | 0.500 | 1.000 |   2 |  2 |  2 |  0 |  37 |
| URW: Blaming the war on others rather than the inv... | 0.667 | 0.500 | 1.000 |   1 |  1 |  1 |  0 |  39 |
| URW: Praise of Russia: Praise of Russian President... | 0.667 | 0.500 | 1.000 |   1 |  1 |  1 |  0 |  39 |
| URW: Russia is the Victim: The West is russophobic | 0.667 | 0.500 | 1.000 |   1 |  1 |  1 |  0 |  39 |
| URW: Speculating war outcomes: Russian army is col... | 0.667 | 1.000 | 0.500 |   2 |  1 |  0 |  1 |  39 |
| URW: Distrust towards Media: Western media is an i... | 0.667 | 0.600 | 0.750 |   4 |  3 |  2 |  1 |  35 |
| Other | 0.588 | 0.833 | 0.455 |  11 |  5 |  1 |  6 |  29 |
| CC: Questioning the measurements and science: Meth... | 0.571 | 0.500 | 0.667 |   3 |  2 |  2 |  1 |  36 |
| CC: Controversy about green technologies: Renewabl... | 0.500 | 0.333 | 1.000 |   1 |  1 |  2 |  0 |  38 |
| CC: Criticism of climate movement: Ad hominem atta... | 0.500 | 0.400 | 0.667 |   3 |  2 |  3 |  1 |  35 |
| CC: Questioning the measurements and science: Scie... | 0.500 | 0.333 | 1.000 |   1 |  1 |  2 |  0 |  38 |
| URW: Discrediting Ukraine: Ukraine is a puppet of ... | 0.500 | 0.400 | 0.667 |   3 |  2 |  3 |  1 |  35 |
| URW: Discrediting Ukraine: Discrediting Ukrainian ... | 0.462 | 0.300 | 1.000 |   3 |  3 |  7 |  0 |  31 |
| URW: Discrediting Ukraine: Discrediting Ukrainian ... | 0.444 | 0.286 | 1.000 |   2 |  2 |  5 |  0 |  34 |
| CC: Controversy about green technologies: Renewabl... | 0.400 | 0.250 | 1.000 |   1 |  1 |  3 |  0 |  37 |
| CC: Criticism of institutions and authorities: Other | 0.400 | 0.250 | 1.000 |   1 |  1 |  3 |  0 |  37 |
| URW: Amplifying war-related fears: By continuing t... | 0.400 | 0.250 | 1.000 |   1 |  1 |  3 |  0 |  37 |
| URW: Discrediting Ukraine: Discrediting Ukrainian ... | 0.400 | 0.250 | 1.000 |   1 |  1 |  3 |  0 |  37 |
| URW: Praise of Russia: Praise of Russian military ... | 0.400 | 0.250 | 1.000 |   1 |  1 |  3 |  0 |  37 |
| URW: Russia is the Victim: Other | 0.400 | 0.250 | 1.000 |   1 |  1 |  3 |  0 |  37 |
| URW: Speculating war outcomes: Ukrainian army is c... | 0.400 | 0.333 | 0.500 |   2 |  1 |  2 |  1 |  37 |
| CC: Criticism of institutions and authorities: Cri... | 0.364 | 0.250 | 0.667 |   3 |  2 |  6 |  1 |  32 |
| CC: Criticism of climate movement: Other | 0.353 | 0.231 | 0.750 |   4 |  3 | 10 |  1 |  27 |
| CC: Controversy about green technologies: Other | 0.333 | 0.200 | 1.000 |   1 |  1 |  4 |  0 |  36 |
| URW: Discrediting Ukraine: Situation in Ukraine is... | 0.286 | 0.167 | 1.000 |   1 |  1 |  5 |  0 |  35 |
| CC: Criticism of institutions and authorities: Cri... | 0.250 | 0.167 | 0.500 |   2 |  1 |  5 |  1 |  34 |
| URW: Discrediting the West, Diplomacy: The West is... | 0.250 | 0.143 | 1.000 |   1 |  1 |  6 |  0 |  34 |
| CC: Criticism of climate movement: Climate movemen... | 0.222 | 0.167 | 0.333 |   3 |  1 |  5 |  2 |  33 |
| CC: Downplaying climate change: Other | 0.222 | 0.125 | 1.000 |   1 |  1 |  7 |  0 |  33 |
| CC: Criticism of climate policies: Climate policie... | 0.182 | 0.100 | 1.000 |   1 |  1 |  9 |  0 |  31 |
| CC: Criticism of climate policies: Other | 0.154 | 0.083 | 1.000 |   1 |  1 | 11 |  0 |  29 |
| CC: Amplifying Climate Fears: Amplifying existing ... | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 |  40 |
| CC: Amplifying Climate Fears: Doomsday scenarios f... | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 |  40 |
| CC: Climate change is beneficial: Temperature incr... | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 |  40 |
| CC: Controversy about green technologies: Renewabl... | 0.000 | 0.000 | 0.000 |   0 |  0 |  2 |  0 |  39 |
| CC: Criticism of climate policies: Climate policie... | 0.000 | 0.000 | 0.000 |   0 |  0 |  6 |  0 |  35 |
| CC: Criticism of institutions and authorities: Cri... | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 |  40 |
| CC: Downplaying climate change: Ice is not melting | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 |  40 |
| CC: Downplaying climate change: Sea levels are not... | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 |  40 |
| CC: Downplaying climate change: Temperature increa... | 0.000 | 0.000 | 0.000 |   0 |  0 |  2 |  0 |  39 |
| CC: Downplaying climate change: Weather suggests t... | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 |  40 |
| CC: Green policies are geopolitical instruments: C... | 0.000 | 0.000 | 0.000 |   2 |  0 |  2 |  2 |  37 |
| CC: Green policies are geopolitical instruments: O... | 0.000 | 0.000 | 0.000 |   1 |  0 |  3 |  1 |  37 |
| CC: Hidden plots by secret schemes of powerful gro... | 0.000 | 0.000 | 0.000 |   1 |  0 |  5 |  1 |  35 |
| CC: Hidden plots by secret schemes of powerful gro... | 0.000 | 0.000 | 0.000 |   1 |  0 |  0 |  1 |  40 |
| CC: Questioning the measurements and science: Data... | 0.000 | 0.000 | 0.000 |   1 |  0 |  0 |  1 |  40 |
| CC: Questioning the measurements and science: Gree... | 0.000 | 0.000 | 0.000 |   0 |  0 |  2 |  0 |  39 |
| CC: Questioning the measurements and science: Other | 0.000 | 0.000 | 0.000 |   0 |  0 |  2 |  0 |  39 |
| URW: Amplifying war-related fears: NATO should/wil... | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 |  40 |
| URW: Amplifying war-related fears: Other | 0.000 | 0.000 | 0.000 |   0 |  0 |  7 |  0 |  34 |
| URW: Amplifying war-related fears: Russia will als... | 0.000 | 0.000 | 0.000 |   0 |  0 |  2 |  0 |  39 |
| URW: Blaming the war on others rather than the inv... | 0.000 | 0.000 | 0.000 |   0 |  0 |  4 |  0 |  37 |
| URW: Discrediting Ukraine: Other | 0.000 | 0.000 | 0.000 |   1 |  0 |  1 |  1 |  39 |
| URW: Discrediting Ukraine: Rewriting Ukraine’s his... | 0.000 | 0.000 | 0.000 |   0 |  0 |  2 |  0 |  39 |
| URW: Discrediting Ukraine: Ukraine is a hub for cr... | 0.000 | 0.000 | 0.000 |   1 |  0 |  0 |  1 |  40 |
| URW: Discrediting the West, Diplomacy: The West is... | 0.000 | 0.000 | 0.000 |   0 |  0 |  2 |  0 |  39 |
| URW: Discrediting the West, Diplomacy: West is tir... | 0.000 | 0.000 | 0.000 |   0 |  0 |  2 |  0 |  39 |
| URW: Distrust towards Media: Other | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 |  40 |
| URW: Distrust towards Media: Ukrainian media canno... | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 |  40 |
| URW: Hidden plots by secret schemes of powerful gr... | 0.000 | 0.000 | 0.000 |   0 |  0 |  3 |  0 |  38 |
| URW: Negative Consequences for the West: Other | 0.000 | 0.000 | 0.000 |   0 |  0 |  8 |  0 |  33 |
| URW: Negative Consequences for the West: Sanctions... | 0.000 | 0.000 | 0.000 |   1 |  0 |  0 |  1 |  40 |
| URW: Overpraising the West: The West belongs in th... | 0.000 | 0.000 | 0.000 |   1 |  0 |  0 |  1 |  40 |
| URW: Praise of Russia: Other | 0.000 | 0.000 | 0.000 |   1 |  0 |  2 |  1 |  38 |
| URW: Russia is the Victim: Russia actions in Ukrai... | 0.000 | 0.000 | 0.000 |   0 |  0 |  2 |  0 |  39 |
| URW: Russia is the Victim: UA is anti-RU extremists | 0.000 | 0.000 | 0.000 |   0 |  0 |  2 |  0 |  39 |
| URW: Speculating war outcomes: Other | 0.000 | 0.000 | 0.000 |   0 |  0 | 10 |  0 |  31 |

**Legend:**
- **TP**: True Positives (correctly predicted positive)
- **FP**: False Positives (incorrectly predicted positive)
- **FN**: False Negatives (incorrectly predicted negative)
- **TN**: True Negatives (correctly predicted negative)


### HI - Subnarratives

**Language**: HI  
**Model**: Google Gemini 2.5 Flash  
**Total Files**: 35  
**Total Labels**: 42  
**F1 Macro**: 0.2451  
**F1 Micro**: 0.2894  
**F1 Samples**: 0.2687  

#### Confusion Matrix Summary Table (42 labels)

| Label | F1 | Precision | Recall | Support | TP | FP | FN | TN |
|-------|----|-----------|--------|---------|----|----|----|----|
| URW: Amplifying war-related fears: There is a real... | 1.000 | 1.000 | 1.000 |   5 |  5 |  0 |  0 |  30 |
| URW: Distrust towards Media: Western media is an i... | 1.000 | 1.000 | 1.000 |   1 |  1 |  0 |  0 |  34 |
| URW: Amplifying war-related fears: By continuing t... | 0.750 | 0.600 | 1.000 |   3 |  3 |  2 |  0 |  30 |
| CC: Amplifying Climate Fears: Amplifying existing ... | 0.667 | 1.000 | 0.500 |   4 |  2 |  0 |  2 |  31 |
| URW: Discrediting Ukraine: Ukraine is a puppet of ... | 0.667 | 0.500 | 1.000 |   1 |  1 |  1 |  0 |  33 |
| URW: Discrediting the West, Diplomacy: West is tir... | 0.667 | 1.000 | 0.500 |   2 |  1 |  0 |  1 |  33 |
| URW: Praise of Russia: Praise of Russian President... | 0.667 | 0.500 | 1.000 |   1 |  1 |  1 |  0 |  33 |
| URW: Speculating war outcomes: Russian army is col... | 0.667 | 1.000 | 0.500 |   2 |  1 |  0 |  1 |  33 |
| URW: Blaming the war on others rather than the inv... | 0.500 | 0.333 | 1.000 |   3 |  3 |  6 |  0 |  26 |
| URW: Russia is the Victim: Russia actions in Ukrai... | 0.444 | 0.286 | 1.000 |   2 |  2 |  5 |  0 |  28 |
| URW: Amplifying war-related fears: Russia will als... | 0.400 | 1.000 | 0.250 |   4 |  1 |  0 |  3 |  31 |
| URW: Negative Consequences for the West: Sanctions... | 0.400 | 0.500 | 0.333 |   3 |  1 |  1 |  2 |  31 |
| URW: Praise of Russia: Russia has international su... | 0.400 | 0.600 | 0.300 |  10 |  3 |  2 |  7 |  23 |
| URW: Discrediting Ukraine: Discrediting Ukrainian ... | 0.333 | 0.333 | 0.333 |   3 |  1 |  2 |  2 |  30 |
| URW: Discrediting the West, Diplomacy: Other | 0.286 | 0.182 | 0.667 |   3 |  2 |  9 |  1 |  23 |
| URW: Discrediting the West, Diplomacy: The West do... | 0.286 | 0.250 | 0.333 |   3 |  1 |  3 |  2 |  29 |
| URW: Praise of Russia: Praise of Russian military ... | 0.286 | 0.250 | 0.333 |   3 |  1 |  3 |  2 |  29 |
| URW: Praise of Russia: Other | 0.286 | 0.167 | 1.000 |   1 |  1 |  5 |  0 |  29 |
| URW: Discrediting the West, Diplomacy: Diplomacy d... | 0.222 | 0.143 | 0.500 |   2 |  1 |  6 |  1 |  27 |
| Other | 0.200 | 0.125 | 0.500 |   2 |  1 |  7 |  1 |  26 |
| URW: Speculating war outcomes: Other | 0.167 | 0.100 | 0.500 |   2 |  1 |  9 |  1 |  24 |
| CC: Amplifying Climate Fears: Doomsday scenarios f... | 0.000 | 0.000 | 0.000 |   0 |  0 |  2 |  0 |  33 |
| CC: Amplifying Climate Fears: Other | 0.000 | 0.000 | 0.000 |   1 |  0 |  0 |  1 |  34 |
| URW: Amplifying war-related fears: NATO should/wil... | 0.000 | 0.000 | 0.000 |   1 |  0 |  3 |  1 |  31 |
| URW: Amplifying war-related fears: Other | 0.000 | 0.000 | 0.000 |   1 |  0 |  6 |  1 |  28 |
| URW: Blaming the war on others rather than the inv... | 0.000 | 0.000 | 0.000 |   0 |  0 |  5 |  0 |  30 |
| URW: Blaming the war on others rather than the inv... | 0.000 | 0.000 | 0.000 |   2 |  0 |  4 |  2 |  29 |
| URW: Discrediting Ukraine: Discrediting Ukrainian ... | 0.000 | 0.000 | 0.000 |   0 |  0 |  4 |  0 |  31 |
| URW: Discrediting Ukraine: Situation in Ukraine is... | 0.000 | 0.000 | 0.000 |   0 |  0 |  2 |  0 |  33 |
| URW: Discrediting Ukraine: Ukraine is associated w... | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 |  34 |
| URW: Discrediting the West, Diplomacy: The EU is d... | 0.000 | 0.000 | 0.000 |   0 |  0 |  5 |  0 |  30 |
| URW: Discrediting the West, Diplomacy: The West is... | 0.000 | 0.000 | 0.000 |   2 |  0 |  0 |  2 |  33 |
| URW: Discrediting the West, Diplomacy: The West is... | 0.000 | 0.000 | 0.000 |   1 |  0 |  3 |  1 |  31 |
| URW: Distrust towards Media: Other | 0.000 | 0.000 | 0.000 |   1 |  0 |  2 |  1 |  32 |
| URW: Hidden plots by secret schemes of powerful gr... | 0.000 | 0.000 | 0.000 |   2 |  0 |  0 |  2 |  33 |
| URW: Negative Consequences for the West: Other | 0.000 | 0.000 | 0.000 |   0 |  0 |  4 |  0 |  31 |
| URW: Overpraising the West: The West has the stron... | 0.000 | 0.000 | 0.000 |   2 |  0 |  0 |  2 |  33 |
| URW: Praise of Russia: Russia is a guarantor of pe... | 0.000 | 0.000 | 0.000 |   3 |  0 |  2 |  3 |  30 |
| URW: Russia is the Victim: Other | 0.000 | 0.000 | 0.000 |   0 |  0 |  8 |  0 |  27 |
| URW: Russia is the Victim: The West is russophobic | 0.000 | 0.000 | 0.000 |   7 |  0 |  1 |  7 |  27 |
| URW: Speculating war outcomes: Russian army will l... | 0.000 | 0.000 | 0.000 |   1 |  0 |  0 |  1 |  34 |
| URW: Speculating war outcomes: Ukrainian army is c... | 0.000 | 0.000 | 0.000 |   1 |  0 |  2 |  1 |  32 |

**Legend:**
- **TP**: True Positives (correctly predicted positive)
- **FP**: False Positives (incorrectly predicted positive)
- **FN**: False Negatives (incorrectly predicted negative)
- **TN**: True Negatives (correctly predicted negative)


### PT - Subnarratives

**Language**: PT  
**Model**: Google Gemini 2.5 Flash  
**Total Files**: 35  
**Total Labels**: 41  
**F1 Macro**: 0.3425  
**F1 Micro**: 0.4972  
**F1 Samples**: 0.4367  

#### Confusion Matrix Summary Table (41 labels)

| Label | F1 | Precision | Recall | Support | TP | FP | FN | TN |
|-------|----|-----------|--------|---------|----|----|----|----|
| CC: Criticism of institutions and authorities: Cri... | 1.000 | 1.000 | 1.000 |   1 |  1 |  0 |  0 |  34 |
| CC: Criticism of institutions and authorities: Cri... | 1.000 | 1.000 | 1.000 |   1 |  1 |  0 |  0 |  34 |
| URW: Amplifying war-related fears: Other | 1.000 | 1.000 | 1.000 |   1 |  1 |  0 |  0 |  34 |
| URW: Discrediting Ukraine: Discrediting Ukrainian ... | 1.000 | 1.000 | 1.000 |   2 |  2 |  0 |  0 |  33 |
| URW: Praise of Russia: Russia has international su... | 1.000 | 1.000 | 1.000 |   1 |  1 |  0 |  0 |  34 |
| URW: Russia is the Victim: The West is russophobic | 1.000 | 1.000 | 1.000 |   1 |  1 |  0 |  0 |  34 |
| URW: Russia is the Victim: Other | 0.857 | 0.750 | 1.000 |   3 |  3 |  1 |  0 |  31 |
| URW: Praise of Russia: Other | 0.800 | 0.667 | 1.000 |   2 |  2 |  1 |  0 |  32 |
| URW: Praise of Russia: Russia is a guarantor of pe... | 0.800 | 0.667 | 1.000 |   2 |  2 |  1 |  0 |  32 |
| CC: Amplifying Climate Fears: Amplifying existing ... | 0.710 | 0.647 | 0.786 |  14 | 11 |  6 |  3 |  15 |
| CC: Amplifying Climate Fears: Earth will be uninha... | 0.667 | 0.500 | 1.000 |   1 |  1 |  1 |  0 |  33 |
| CC: Criticism of institutions and authorities: Cri... | 0.667 | 1.000 | 0.500 |   4 |  2 |  0 |  2 |  31 |
| URW: Discrediting Ukraine: Ukraine is a puppet of ... | 0.667 | 0.500 | 1.000 |   1 |  1 |  1 |  0 |  33 |
| URW: Discrediting the West, Diplomacy: Other | 0.667 | 0.800 | 0.571 |   7 |  4 |  1 |  3 |  27 |
| CC: Criticism of institutions and authorities: Cri... | 0.615 | 0.444 | 1.000 |   4 |  4 |  5 |  0 |  26 |
| CC: Amplifying Climate Fears: Doomsday scenarios f... | 0.545 | 0.375 | 1.000 |   3 |  3 |  5 |  0 |  27 |
| URW: Discrediting the West, Diplomacy: Diplomacy d... | 0.400 | 0.250 | 1.000 |   1 |  1 |  3 |  0 |  31 |
| CC: Criticism of institutions and authorities: Other | 0.333 | 0.200 | 1.000 |   1 |  1 |  4 |  0 |  30 |
| CC: Amplifying Climate Fears: Other | 0.316 | 1.000 | 0.188 |  16 |  3 |  0 | 13 |  19 |
| CC: Amplifying Climate Fears: Whatever we do it is... | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 |  34 |
| CC: Controversy about green technologies: Renewabl... | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 |  34 |
| CC: Criticism of climate policies: Climate policie... | 0.000 | 0.000 | 0.000 |   1 |  0 |  4 |  1 |  30 |
| CC: Criticism of climate policies: Climate policie... | 0.000 | 0.000 | 0.000 |   2 |  0 |  0 |  2 |  33 |
| CC: Criticism of climate policies: Climate policie... | 0.000 | 0.000 | 0.000 |   0 |  0 |  3 |  0 |  32 |
| CC: Criticism of climate policies: Other | 0.000 | 0.000 | 0.000 |   6 |  0 |  0 |  6 |  29 |
| CC: Green policies are geopolitical instruments: C... | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 |  34 |
| CC: Green policies are geopolitical instruments: G... | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 |  34 |
| CC: Green policies are geopolitical instruments: O... | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 |  34 |
| CC: Hidden plots by secret schemes of powerful gro... | 0.000 | 0.000 | 0.000 |   1 |  0 |  0 |  1 |  34 |
| Other | 0.000 | 0.000 | 0.000 |   1 |  0 |  3 |  1 |  31 |
| URW: Blaming the war on others rather than the inv... | 0.000 | 0.000 | 0.000 |   0 |  0 |  2 |  0 |  33 |
| URW: Blaming the war on others rather than the inv... | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 |  34 |
| URW: Discrediting Ukraine: Other | 0.000 | 0.000 | 0.000 |   1 |  0 |  0 |  1 |  34 |
| URW: Discrediting Ukraine: Situation in Ukraine is... | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 |  34 |
| URW: Discrediting the West, Diplomacy: The West is... | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 |  34 |
| URW: Discrediting the West, Diplomacy: The West is... | 0.000 | 0.000 | 0.000 |   0 |  0 |  3 |  0 |  32 |
| URW: Negative Consequences for the West: Other | 0.000 | 0.000 | 0.000 |   1 |  0 |  0 |  1 |  34 |
| URW: Negative Consequences for the West: Sanctions... | 0.000 | 0.000 | 0.000 |   0 |  0 |  2 |  0 |  33 |
| URW: Praise of Russia: Praise of Russian military ... | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 |  34 |
| URW: Speculating war outcomes: Other | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 |  34 |
| URW: Speculating war outcomes: Ukrainian army is c... | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 |  34 |

**Legend:**
- **TP**: True Positives (correctly predicted positive)
- **FP**: False Positives (incorrectly predicted positive)
- **FN**: False Negatives (incorrectly predicted negative)
- **TN**: True Negatives (correctly predicted negative)


### RU - Subnarratives

**Language**: RU  
**Model**: Google Gemini 2.5 Flash  
**Total Files**: 32  
**Total Labels**: 40  
**F1 Macro**: 0.3342  
**F1 Micro**: 0.4454  
**F1 Samples**: 0.5078  

#### Confusion Matrix Summary Table (40 labels)

| Label | F1 | Precision | Recall | Support | TP | FP | FN | TN |
|-------|----|-----------|--------|---------|----|----|----|----|
| URW: Discrediting Ukraine: Ukraine is a hub for cr... | 1.000 | 1.000 | 1.000 |   2 |  2 |  0 |  0 |  30 |
| URW: Negative Consequences for the West: Sanctions... | 1.000 | 1.000 | 1.000 |   1 |  1 |  0 |  0 |  31 |
| URW: Praise of Russia: Praise of Russian military ... | 0.909 | 0.833 | 1.000 |   5 |  5 |  1 |  0 |  26 |
| Other | 0.889 | 0.800 | 1.000 |   4 |  4 |  1 |  0 |  27 |
| URW: Praise of Russia: Praise of Russian President... | 0.800 | 0.667 | 1.000 |   2 |  2 |  1 |  0 |  29 |
| URW: Discrediting Ukraine: Discrediting Ukrainian ... | 0.783 | 0.643 | 1.000 |   9 |  9 |  5 |  0 |  18 |
| URW: Amplifying war-related fears: NATO should/wil... | 0.667 | 1.000 | 0.500 |   2 |  1 |  0 |  1 |  30 |
| URW: Discrediting Ukraine: Ukraine is a puppet of ... | 0.667 | 0.500 | 1.000 |   4 |  4 |  4 |  0 |  24 |
| URW: Discrediting Ukraine: Ukraine is associated w... | 0.667 | 0.500 | 1.000 |   1 |  1 |  1 |  0 |  30 |
| URW: Russia is the Victim: The West is russophobic | 0.667 | 1.000 | 0.500 |   2 |  1 |  0 |  1 |  30 |
| URW: Discrediting the West, Diplomacy: The West is... | 0.571 | 0.400 | 1.000 |   2 |  2 |  3 |  0 |  27 |
| URW: Speculating war outcomes: Ukrainian army is c... | 0.571 | 0.400 | 1.000 |   2 |  2 |  3 |  0 |  27 |
| URW: Discrediting Ukraine: Discrediting Ukrainian ... | 0.571 | 0.444 | 0.800 |   5 |  4 |  5 |  1 |  22 |
| URW: Discrediting the West, Diplomacy: The EU is d... | 0.500 | 0.500 | 0.500 |   2 |  1 |  1 |  1 |  29 |
| URW: Praise of Russia: Russia has international su... | 0.500 | 0.667 | 0.400 |   5 |  2 |  1 |  3 |  26 |
| URW: Praise of Russia: Russia is a guarantor of pe... | 0.500 | 0.667 | 0.400 |   5 |  2 |  1 |  3 |  26 |
| URW: Russia is the Victim: UA is anti-RU extremists | 0.500 | 0.333 | 1.000 |   1 |  1 |  2 |  0 |  29 |
| URW: Blaming the war on others rather than the inv... | 0.444 | 0.333 | 0.667 |   3 |  2 |  4 |  1 |  25 |
| URW: Discrediting the West, Diplomacy: Other | 0.375 | 0.250 | 0.750 |   4 |  3 |  9 |  1 |  19 |
| URW: Discrediting the West, Diplomacy: The West do... | 0.333 | 0.286 | 0.400 |   5 |  2 |  5 |  3 |  22 |
| URW: Discrediting the West, Diplomacy: Diplomacy d... | 0.286 | 0.200 | 0.500 |   2 |  1 |  4 |  1 |  26 |
| URW: Speculating war outcomes: Other | 0.167 | 0.100 | 0.500 |   2 |  1 |  9 |  1 |  21 |
| URW: Amplifying war-related fears: By continuing t... | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 |  31 |
| URW: Amplifying war-related fears: Other | 0.000 | 0.000 | 0.000 |   0 |  0 |  3 |  0 |  29 |
| URW: Amplifying war-related fears: There is a real... | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 |  31 |
| URW: Blaming the war on others rather than the inv... | 0.000 | 0.000 | 0.000 |   0 |  0 |  3 |  0 |  29 |
| URW: Blaming the war on others rather than the inv... | 0.000 | 0.000 | 0.000 |   1 |  0 |  4 |  1 |  27 |
| URW: Discrediting Ukraine: Discrediting Ukrainian ... | 0.000 | 0.000 | 0.000 |   0 |  0 |  2 |  0 |  30 |
| URW: Discrediting Ukraine: Other | 0.000 | 0.000 | 0.000 |   0 |  0 |  2 |  0 |  30 |
| URW: Discrediting Ukraine: Situation in Ukraine is... | 0.000 | 0.000 | 0.000 |   0 |  0 |  6 |  0 |  26 |
| URW: Discrediting the West, Diplomacy: The West is... | 0.000 | 0.000 | 0.000 |   2 |  0 |  0 |  2 |  30 |
| URW: Discrediting the West, Diplomacy: West is tir... | 0.000 | 0.000 | 0.000 |   2 |  0 |  1 |  2 |  29 |
| URW: Distrust towards Media: Ukrainian media canno... | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 |  31 |
| URW: Distrust towards Media: Western media is an i... | 0.000 | 0.000 | 0.000 |   2 |  0 |  0 |  2 |  30 |
| URW: Hidden plots by secret schemes of powerful gr... | 0.000 | 0.000 | 0.000 |   1 |  0 |  1 |  1 |  30 |
| URW: Negative Consequences for the West: Other | 0.000 | 0.000 | 0.000 |   0 |  0 |  5 |  0 |  27 |
| URW: Praise of Russia: Other | 0.000 | 0.000 | 0.000 |   1 |  0 |  9 |  1 |  22 |
| URW: Praise of Russia: Russian invasion has strong... | 0.000 | 0.000 | 0.000 |   0 |  0 |  2 |  0 |  30 |
| URW: Russia is the Victim: Other | 0.000 | 0.000 | 0.000 |   0 |  0 |  4 |  0 |  28 |
| URW: Russia is the Victim: Russia actions in Ukrai... | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 |  31 |

**Legend:**
- **TP**: True Positives (correctly predicted positive)
- **FP**: False Positives (incorrectly predicted positive)
- **FN**: False Negatives (incorrectly predicted negative)
- **TN**: True Negatives (correctly predicted negative)


---

## Notes

- **TP (True Positives)**: Correctly identified positive cases
- **FP (False Positives)**: Incorrectly identified positive cases (Type I error)
- **TN (True Negatives)**: Correctly identified negative cases
- **FN (False Negatives)**: Incorrectly identified negative cases (Type II error)

- **Precision**: TP / (TP + FP) - How many selected items are relevant
- **Recall**: TP / (TP + FN) - How many relevant items are selected
- **F1 Score**: 2 * (Precision * Recall) / (Precision + Recall) - Harmonic mean of precision and recall

**Generated for**: Gemini 2.5 Flash - Subnarrative Validation Devset  
**Model**: Google Gemini 2.5 Flash  
**Languages**: BG, EN, HI, PT, RU
