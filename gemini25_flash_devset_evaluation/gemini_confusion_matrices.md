# Comprehensive Confusion Matrices - Gemini 2.5 Flash Results

**Experiment**: Gemini 2.5 Flash - No Validation Devset  
**Model**: Google Gemini 2.5 Flash  
**Languages Analyzed**: BG, EN, HI, PT, RU  
**Analysis Type**: Per-Label Confusion Matrices  

This document provides detailed confusion matrices for every narrative and subnarrative label in every language analyzed by Gemini 2.5 Flash.


## Summary Statistics

### Performance Overview by Language

| Language | Model | Files | Narratives F1 | Subnarratives F1 | Narratives Labels | Subnarratives Labels |
|----------|-------|-------|---------------|------------------|-------------------|----------------------|
| BG | Google Gemini 2.5 Flash | 35 | 0.5799 | 0.4104 | 21 | 71 |
| EN | Google Gemini 2.5 Flash | 41 | 0.5132 | 0.3815 | 22 | 83 |
| HI | Google Gemini 2.5 Flash | 35 | 0.4715 | 0.2976 | 13 | 46 |
| PT | Google Gemini 2.5 Flash | 35 | 0.7489 | 0.4737 | 14 | 40 |
| RU | Google Gemini 2.5 Flash | 32 | 0.6958 | 0.4754 | 11 | 41 |

### Label Distribution Statistics

**Narratives:**
- Total unique labels across all languages: 22
- Total confusion matrices generated: 81

**Subnarratives:**
- Total unique labels across all languages: 89
- Total confusion matrices generated: 281


---

# Detailed Confusion Matrices


## Narratives Confusion Matrices


### BG - Narratives

**Language**: BG  
**Model**: Google Gemini 2.5 Flash  
**Total Files**: 35  
**Total Labels**: 21  
**F1 Macro**: 0.4236  
**F1 Micro**: 0.5584  
**F1 Samples**: 0.5799  

#### Confusion Matrix Summary Table (21 labels)

| Label | F1 | Precision | Recall | Support | TP | FP | FN | TN |
|-------|----|-----------|--------|---------|----|----|----|----|
| CC: Amplifying Climate Fears | 0.900 | 0.818 | 1.000 |   9 |  9 |  2 |  0 |  24 |
| URW: Discrediting Ukraine | 0.833 | 0.714 | 1.000 |   5 |  5 |  2 |  0 |  28 |
| CC: Criticism of climate policies | 0.800 | 0.667 | 1.000 |   2 |  2 |  1 |  0 |  32 |
| URW: Praise of Russia | 0.800 | 0.667 | 1.000 |   2 |  2 |  1 |  0 |  32 |
| URW: Amplifying war-related fears | 0.769 | 0.625 | 1.000 |   5 |  5 |  3 |  0 |  27 |
| CC: Criticism of climate movement | 0.667 | 0.500 | 1.000 |   1 |  1 |  1 |  0 |  33 |
| CC: Criticism of institutions and authorities | 0.667 | 0.500 | 1.000 |   3 |  3 |  3 |  0 |  29 |
| CC: Hidden plots by secret schemes of powerful groups | 0.667 | 1.000 | 0.500 |   2 |  1 |  0 |  1 |  33 |
| CC: Downplaying climate change | 0.571 | 0.667 | 0.500 |   4 |  2 |  1 |  2 |  30 |
| URW: Discrediting the West, Diplomacy | 0.526 | 0.357 | 1.000 |   5 |  5 |  9 |  0 |  21 |
| URW: Negative Consequences for the West | 0.500 | 0.400 | 0.667 |   3 |  2 |  3 |  1 |  29 |
| URW: Russia is the Victim | 0.500 | 0.333 | 1.000 |   3 |  3 |  6 |  0 |  26 |
| Other | 0.444 | 0.667 | 0.333 |   6 |  2 |  1 |  4 |  28 |
| URW: Blaming the war on others rather than the inv... | 0.250 | 0.167 | 0.500 |   2 |  1 |  5 |  1 |  28 |
| CC: Controversy about green technologies | 0.000 | 0.000 | 0.000 |   0 |  0 |  2 |  0 |  33 |
| CC: Green policies are geopolitical instruments | 0.000 | 0.000 | 0.000 |   1 |  0 |  3 |  1 |  31 |
| CC: Questioning the measurements and science | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 |  34 |
| URW: Distrust towards Media | 0.000 | 0.000 | 0.000 |   0 |  0 |  2 |  0 |  33 |
| URW: Hidden plots by secret schemes of powerful gr... | 0.000 | 0.000 | 0.000 |   0 |  0 |  4 |  0 |  31 |
| URW: Overpraising the West | 0.000 | 0.000 | 0.000 |   1 |  0 |  0 |  1 |  34 |
| URW: Speculating war outcomes | 0.000 | 0.000 | 0.000 |   0 |  0 |  7 |  0 |  28 |

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
**F1 Macro**: 0.5398  
**F1 Micro**: 0.5714  
**F1 Samples**: 0.5132  

#### Confusion Matrix Summary Table (22 labels)

| Label | F1 | Precision | Recall | Support | TP | FP | FN | TN |
|-------|----|-----------|--------|---------|----|----|----|----|
| URW: Overpraising the West | 1.000 | 1.000 | 1.000 |   1 |  1 |  0 |  0 |  40 |
| URW: Distrust towards Media | 0.889 | 0.800 | 1.000 |   4 |  4 |  1 |  0 |  36 |
| URW: Discrediting Ukraine | 0.875 | 0.778 | 1.000 |   7 |  7 |  2 |  0 |  32 |
| CC: Green policies are geopolitical instruments | 0.857 | 0.750 | 1.000 |   3 |  3 |  1 |  0 |  37 |
| CC: Questioning the measurements and science | 0.857 | 1.000 | 0.750 |   4 |  3 |  0 |  1 |  37 |
| URW: Blaming the war on others rather than the inv... | 0.857 | 0.750 | 1.000 |   6 |  6 |  2 |  0 |  33 |
| URW: Discrediting the West, Diplomacy | 0.842 | 0.800 | 0.889 |   9 |  8 |  2 |  1 |  30 |
| CC: Climate change is beneficial | 0.667 | 0.500 | 1.000 |   1 |  1 |  1 |  0 |  39 |
| CC: Hidden plots by secret schemes of powerful groups | 0.667 | 1.000 | 0.500 |   4 |  2 |  0 |  2 |  37 |
| URW: Praise of Russia | 0.571 | 0.400 | 1.000 |   2 |  2 |  3 |  0 |  36 |
| CC: Criticism of climate movement | 0.571 | 0.462 | 0.750 |   8 |  6 |  7 |  2 |  26 |
| URW: Speculating war outcomes | 0.500 | 0.333 | 1.000 |   4 |  4 |  8 |  0 |  29 |
| CC: Criticism of institutions and authorities | 0.476 | 0.385 | 0.625 |   8 |  5 |  8 |  3 |  25 |
| Other | 0.471 | 0.667 | 0.364 |  11 |  4 |  2 |  7 |  28 |
| URW: Amplifying war-related fears | 0.462 | 0.300 | 1.000 |   3 |  3 |  7 |  0 |  31 |
| CC: Downplaying climate change | 0.444 | 0.286 | 1.000 |   2 |  2 |  5 |  0 |  34 |
| CC: Criticism of climate policies | 0.333 | 0.200 | 1.000 |   3 |  3 | 12 |  0 |  26 |
| CC: Controversy about green technologies | 0.286 | 0.200 | 0.500 |   2 |  1 |  4 |  1 |  35 |
| URW: Russia is the Victim | 0.250 | 0.167 | 0.500 |   2 |  1 |  5 |  1 |  34 |
| CC: Amplifying Climate Fears | 0.000 | 0.000 | 0.000 |   0 |  0 |  2 |  0 |  39 |
| URW: Hidden plots by secret schemes of powerful gr... | 0.000 | 0.000 | 0.000 |   0 |  0 |  2 |  0 |  39 |
| URW: Negative Consequences for the West | 0.000 | 0.000 | 0.000 |   1 |  0 |  6 |  1 |  34 |

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
**F1 Macro**: 0.3971  
**F1 Micro**: 0.4841  
**F1 Samples**: 0.4715  

#### Confusion Matrix Summary Table (13 labels)

| Label | F1 | Precision | Recall | Support | TP | FP | FN | TN |
|-------|----|-----------|--------|---------|----|----|----|----|
| CC: Amplifying Climate Fears | 0.857 | 1.000 | 0.750 |   4 |  3 |  0 |  1 |  31 |
| URW: Amplifying war-related fears | 0.778 | 0.700 | 0.875 |   8 |  7 |  3 |  1 |  24 |
| URW: Praise of Russia | 0.667 | 0.727 | 0.615 |  13 |  8 |  3 |  5 |  19 |
| URW: Discrediting the West, Diplomacy | 0.609 | 0.438 | 1.000 |   7 |  7 |  9 |  0 |  19 |
| URW: Distrust towards Media | 0.500 | 0.500 | 0.500 |   2 |  1 |  1 |  1 |  32 |
| URW: Russia is the Victim | 0.421 | 0.400 | 0.444 |   9 |  4 |  6 |  5 |  20 |
| URW: Blaming the war on others rather than the inv... | 0.375 | 0.273 | 0.600 |   5 |  3 |  8 |  2 |  22 |
| Other | 0.286 | 0.200 | 0.500 |   2 |  1 |  4 |  1 |  29 |
| URW: Speculating war outcomes | 0.267 | 0.200 | 0.400 |   5 |  2 |  8 |  3 |  22 |
| URW: Discrediting Ukraine | 0.222 | 0.167 | 0.333 |   3 |  1 |  5 |  2 |  27 |
| URW: Negative Consequences for the West | 0.182 | 0.125 | 0.333 |   3 |  1 |  7 |  2 |  25 |
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
**Total Labels**: 14  
**F1 Macro**: 0.4756  
**F1 Micro**: 0.7460  
**F1 Samples**: 0.7489  

#### Confusion Matrix Summary Table (14 labels)

| Label | F1 | Precision | Recall | Support | TP | FP | FN | TN |
|-------|----|-----------|--------|---------|----|----|----|----|
| CC: Amplifying Climate Fears | 0.878 | 1.000 | 0.783 |  23 | 18 |  0 |  5 |  12 |
| URW: Discrediting the West, Diplomacy | 0.875 | 0.875 | 0.875 |   8 |  7 |  1 |  1 |  26 |
| URW: Praise of Russia | 0.857 | 1.000 | 0.750 |   4 |  3 |  0 |  1 |  31 |
| URW: Discrediting Ukraine | 0.800 | 1.000 | 0.667 |   3 |  2 |  0 |  1 |  32 |
| CC: Criticism of climate policies | 0.714 | 1.000 | 0.556 |   9 |  5 |  0 |  4 |  26 |
| CC: Criticism of institutions and authorities | 0.700 | 0.583 | 0.875 |   8 |  7 |  5 |  1 |  22 |
| URW: Negative Consequences for the West | 0.667 | 0.500 | 1.000 |   1 |  1 |  1 |  0 |  33 |
| URW: Russia is the Victim | 0.667 | 0.500 | 1.000 |   3 |  3 |  3 |  0 |  29 |
| Other | 0.500 | 0.333 | 1.000 |   1 |  1 |  2 |  0 |  32 |
| CC: Controversy about green technologies | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 |  34 |
| CC: Green policies are geopolitical instruments | 0.000 | 0.000 | 0.000 |   0 |  0 |  2 |  0 |  33 |
| CC: Hidden plots by secret schemes of powerful groups | 0.000 | 0.000 | 0.000 |   1 |  0 |  0 |  1 |  34 |
| URW: Amplifying war-related fears | 0.000 | 0.000 | 0.000 |   1 |  0 |  0 |  1 |  34 |
| URW: Blaming the war on others rather than the inv... | 0.000 | 0.000 | 0.000 |   0 |  0 |  2 |  0 |  33 |

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
**F1 Macro**: 0.5213  
**F1 Micro**: 0.6879  
**F1 Samples**: 0.6958  

#### Confusion Matrix Summary Table (11 labels)

| Label | F1 | Precision | Recall | Support | TP | FP | FN | TN |
|-------|----|-----------|--------|---------|----|----|----|----|
| Other | 1.000 | 1.000 | 1.000 |   4 |  4 |  0 |  0 |  28 |
| URW: Discrediting Ukraine | 0.857 | 0.750 | 1.000 |  15 | 15 |  5 |  0 |  12 |
| URW: Discrediting the West, Diplomacy | 0.824 | 0.737 | 0.933 |  15 | 14 |  5 |  1 |  12 |
| URW: Praise of Russia | 0.815 | 0.917 | 0.733 |  15 | 11 |  1 |  4 |  16 |
| URW: Amplifying war-related fears | 0.667 | 0.500 | 1.000 |   2 |  2 |  2 |  0 |  28 |
| URW: Speculating war outcomes | 0.462 | 0.300 | 1.000 |   3 |  3 |  7 |  0 |  22 |
| URW: Russia is the Victim | 0.444 | 0.333 | 0.667 |   3 |  2 |  4 |  1 |  25 |
| URW: Negative Consequences for the West | 0.333 | 0.200 | 1.000 |   1 |  1 |  4 |  0 |  27 |
| URW: Blaming the war on others rather than the inv... | 0.333 | 0.250 | 0.500 |   4 |  2 |  6 |  2 |  22 |
| URW: Distrust towards Media | 0.000 | 0.000 | 0.000 |   2 |  0 |  1 |  2 |  29 |
| URW: Hidden plots by secret schemes of powerful gr... | 0.000 | 0.000 | 0.000 |   1 |  0 |  3 |  1 |  28 |

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
**Total Labels**: 71  
**F1 Macro**: 0.2819  
**F1 Micro**: 0.3824  
**F1 Samples**: 0.4104  

#### Confusion Matrix Summary Table (71 labels)

| Label | F1 | Precision | Recall | Support | TP | FP | FN | TN |
|-------|----|-----------|--------|---------|----|----|----|----|
| CC: Criticism of climate movement: Ad hominem atta... | 1.000 | 1.000 | 1.000 |   1 |  1 |  0 |  0 |  34 |
| CC: Criticism of climate policies: Climate policie... | 1.000 | 1.000 | 1.000 |   1 |  1 |  0 |  0 |  34 |
| CC: Downplaying climate change: Climate cycles are... | 1.000 | 1.000 | 1.000 |   1 |  1 |  0 |  0 |  34 |
| CC: Hidden plots by secret schemes of powerful gro... | 1.000 | 1.000 | 1.000 |   1 |  1 |  0 |  0 |  34 |
| CC: Hidden plots by secret schemes of powerful gro... | 1.000 | 1.000 | 1.000 |   1 |  1 |  0 |  0 |  34 |
| URW: Amplifying war-related fears: There is a real... | 1.000 | 1.000 | 1.000 |   2 |  2 |  0 |  0 |  33 |
| URW: Praise of Russia: Praise of Russian President... | 1.000 | 1.000 | 1.000 |   1 |  1 |  0 |  0 |  34 |
| CC: Amplifying Climate Fears: Amplifying existing ... | 0.900 | 0.818 | 1.000 |   9 |  9 |  2 |  0 |  24 |
| CC: Criticism of climate movement: Climate movemen... | 0.667 | 0.500 | 1.000 |   1 |  1 |  1 |  0 |  33 |
| CC: Criticism of climate movement: Other | 0.667 | 0.500 | 1.000 |   1 |  1 |  1 |  0 |  33 |
| CC: Criticism of climate policies: Climate policie... | 0.667 | 0.500 | 1.000 |   1 |  1 |  1 |  0 |  33 |
| CC: Criticism of institutions and authorities: Cri... | 0.667 | 0.500 | 1.000 |   2 |  2 |  2 |  0 |  31 |
| URW: Amplifying war-related fears: By continuing t... | 0.667 | 0.500 | 1.000 |   1 |  1 |  1 |  0 |  33 |
| URW: Praise of Russia: Praise of Russian military ... | 0.667 | 0.500 | 1.000 |   1 |  1 |  1 |  0 |  33 |
| URW: Praise of Russia: Russia has international su... | 0.667 | 0.500 | 1.000 |   1 |  1 |  1 |  0 |  33 |
| URW: Russia is the Victim: The West is russophobic | 0.600 | 0.429 | 1.000 |   3 |  3 |  4 |  0 |  28 |
| URW: Discrediting Ukraine: Discrediting Ukrainian ... | 0.571 | 0.400 | 1.000 |   2 |  2 |  3 |  0 |  30 |
| URW: Discrediting the West, Diplomacy: Other | 0.500 | 0.364 | 0.800 |   5 |  4 |  7 |  1 |  23 |
| CC: Downplaying climate change: Weather suggests t... | 0.500 | 1.000 | 0.333 |   3 |  1 |  0 |  2 |  32 |
| URW: Amplifying war-related fears: Other | 0.500 | 0.333 | 1.000 |   2 |  2 |  4 |  0 |  29 |
| URW: Amplifying war-related fears: Russia will als... | 0.500 | 0.333 | 1.000 |   1 |  1 |  2 |  0 |  32 |
| URW: Discrediting Ukraine: Ukraine is a hub for cr... | 0.500 | 0.333 | 1.000 |   1 |  1 |  2 |  0 |  32 |
| URW: Discrediting Ukraine: Ukraine is a puppet of ... | 0.500 | 0.333 | 1.000 |   2 |  2 |  4 |  0 |  29 |
| URW: Discrediting Ukraine: Ukraine is associated w... | 0.500 | 0.333 | 1.000 |   1 |  1 |  2 |  0 |  32 |
| URW: Negative Consequences for the West: Other | 0.500 | 0.400 | 0.667 |   3 |  2 |  3 |  1 |  29 |
| Other | 0.444 | 0.667 | 0.333 |   6 |  2 |  1 |  4 |  28 |
| CC: Criticism of institutions and authorities: Cri... | 0.400 | 0.250 | 1.000 |   1 |  1 |  3 |  0 |  31 |
| URW: Blaming the war on others rather than the inv... | 0.400 | 0.250 | 1.000 |   1 |  1 |  3 |  0 |  31 |
| CC: Amplifying Climate Fears: Doomsday scenarios f... | 0.364 | 0.222 | 1.000 |   2 |  2 |  7 |  0 |  26 |
| URW: Discrediting Ukraine: Discrediting Ukrainian ... | 0.333 | 0.200 | 1.000 |   1 |  1 |  4 |  0 |  30 |
| CC: Amplifying Climate Fears: Other | 0.333 | 0.500 | 0.250 |   4 |  1 |  1 |  3 |  30 |
| CC: Amplifying Climate Fears: Earth will be uninha... | 0.000 | 0.000 | 0.000 |   0 |  0 |  2 |  0 |  33 |
| CC: Controversy about green technologies: Other | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 |  34 |
| CC: Controversy about green technologies: Renewabl... | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 |  34 |
| CC: Controversy about green technologies: Renewabl... | 0.000 | 0.000 | 0.000 |   0 |  0 |  2 |  0 |  33 |
| CC: Criticism of climate movement: Climate movemen... | 0.000 | 0.000 | 0.000 |   0 |  0 |  2 |  0 |  33 |
| CC: Criticism of climate policies: Climate policie... | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 |  34 |
| CC: Criticism of climate policies: Other | 0.000 | 0.000 | 0.000 |   0 |  0 |  3 |  0 |  32 |
| CC: Criticism of institutions and authorities: Cri... | 0.000 | 0.000 | 0.000 |   0 |  0 |  2 |  0 |  33 |
| CC: Criticism of institutions and authorities: Cri... | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 |  34 |
| CC: Criticism of institutions and authorities: Other | 0.000 | 0.000 | 0.000 |   0 |  0 |  2 |  0 |  33 |
| CC: Downplaying climate change: Human activities d... | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 |  34 |
| CC: Downplaying climate change: Other | 0.000 | 0.000 | 0.000 |   0 |  0 |  3 |  0 |  32 |
| CC: Green policies are geopolitical instruments: C... | 0.000 | 0.000 | 0.000 |   0 |  0 |  2 |  0 |  33 |
| CC: Green policies are geopolitical instruments: G... | 0.000 | 0.000 | 0.000 |   1 |  0 |  1 |  1 |  33 |
| CC: Green policies are geopolitical instruments: O... | 0.000 | 0.000 | 0.000 |   0 |  0 |  2 |  0 |  33 |
| CC: Hidden plots by secret schemes of powerful gro... | 0.000 | 0.000 | 0.000 |   1 |  0 |  1 |  1 |  33 |
| CC: Questioning the measurements and science: Other | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 |  34 |
| CC: Questioning the measurements and science: Scie... | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 |  34 |
| URW: Amplifying war-related fears: NATO should/wil... | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 |  34 |
| URW: Blaming the war on others rather than the inv... | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 |  34 |
| URW: Blaming the war on others rather than the inv... | 0.000 | 0.000 | 0.000 |   1 |  0 |  6 |  1 |  28 |
| URW: Discrediting Ukraine: Discrediting Ukrainian ... | 0.000 | 0.000 | 0.000 |   0 |  0 |  4 |  0 |  31 |
| URW: Discrediting Ukraine: Other | 0.000 | 0.000 | 0.000 |   0 |  0 |  3 |  0 |  32 |
| URW: Discrediting Ukraine: Situation in Ukraine is... | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 |  34 |
| URW: Discrediting the West, Diplomacy: Diplomacy d... | 0.000 | 0.000 | 0.000 |   0 |  0 |  3 |  0 |  32 |
| URW: Discrediting the West, Diplomacy: The EU is d... | 0.000 | 0.000 | 0.000 |   0 |  0 |  3 |  0 |  32 |
| URW: Discrediting the West, Diplomacy: The West do... | 0.000 | 0.000 | 0.000 |   0 |  0 |  4 |  0 |  31 |
| URW: Discrediting the West, Diplomacy: The West is... | 0.000 | 0.000 | 0.000 |   0 |  0 |  3 |  0 |  32 |
| URW: Discrediting the West, Diplomacy: The West is... | 0.000 | 0.000 | 0.000 |   0 |  0 |  6 |  0 |  29 |
| URW: Discrediting the West, Diplomacy: West is tir... | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 |  34 |
| URW: Distrust towards Media: Ukrainian media canno... | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 |  34 |
| URW: Distrust towards Media: Western media is an i... | 0.000 | 0.000 | 0.000 |   0 |  0 |  2 |  0 |  33 |
| URW: Hidden plots by secret schemes of powerful gr... | 0.000 | 0.000 | 0.000 |   0 |  0 |  4 |  0 |  31 |
| URW: Overpraising the West: The West belongs in th... | 0.000 | 0.000 | 0.000 |   1 |  0 |  0 |  1 |  34 |
| URW: Praise of Russia: Other | 0.000 | 0.000 | 0.000 |   0 |  0 |  2 |  0 |  33 |
| URW: Russia is the Victim: Other | 0.000 | 0.000 | 0.000 |   0 |  0 |  4 |  0 |  31 |
| URW: Russia is the Victim: Russia actions in Ukrai... | 0.000 | 0.000 | 0.000 |   0 |  0 |  5 |  0 |  30 |
| URW: Russia is the Victim: UA is anti-RU extremists | 0.000 | 0.000 | 0.000 |   0 |  0 |  3 |  0 |  32 |
| URW: Speculating war outcomes: Other | 0.000 | 0.000 | 0.000 |   0 |  0 |  6 |  0 |  29 |
| URW: Speculating war outcomes: Russian army is col... | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 |  34 |

**Legend:**
- **TP**: True Positives (correctly predicted positive)
- **FP**: False Positives (incorrectly predicted positive)
- **FN**: False Negatives (incorrectly predicted negative)
- **TN**: True Negatives (correctly predicted negative)


### EN - Subnarratives

**Language**: EN  
**Model**: Google Gemini 2.5 Flash  
**Total Files**: 41  
**Total Labels**: 83  
**F1 Macro**: 0.3116  
**F1 Micro**: 0.4019  
**F1 Samples**: 0.3815  

#### Confusion Matrix Summary Table (83 labels)

| Label | F1 | Precision | Recall | Support | TP | FP | FN | TN |
|-------|----|-----------|--------|---------|----|----|----|----|
| CC: Climate change is beneficial: CO2 is beneficial | 1.000 | 1.000 | 1.000 |   1 |  1 |  0 |  0 |  40 |
| CC: Downplaying climate change: Human activities d... | 1.000 | 1.000 | 1.000 |   2 |  2 |  0 |  0 |  39 |
| URW: Discrediting the West, Diplomacy: The EU is d... | 1.000 | 1.000 | 1.000 |   1 |  1 |  0 |  0 |  40 |
| URW: Overpraising the West: The West belongs in th... | 1.000 | 1.000 | 1.000 |   1 |  1 |  0 |  0 |  40 |
| URW: Speculating war outcomes: Russian army is col... | 1.000 | 1.000 | 1.000 |   2 |  2 |  0 |  0 |  39 |
| URW: Blaming the war on others rather than the inv... | 0.857 | 0.750 | 1.000 |   6 |  6 |  2 |  0 |  33 |
| URW: Discrediting the West, Diplomacy: Other | 0.857 | 0.750 | 1.000 |   6 |  6 |  2 |  0 |  33 |
| URW: Discrediting Ukraine: Ukraine is associated w... | 0.800 | 0.667 | 1.000 |   2 |  2 |  1 |  0 |  38 |
| CC: Criticism of institutions and authorities: Cri... | 0.769 | 0.714 | 0.833 |   6 |  5 |  2 |  1 |  33 |
| URW: Distrust towards Media: Western media is an i... | 0.750 | 0.750 | 0.750 |   4 |  3 |  1 |  1 |  36 |
| CC: Controversy about green technologies: Renewabl... | 0.667 | 0.500 | 1.000 |   1 |  1 |  1 |  0 |  39 |
| CC: Criticism of climate movement: Climate movemen... | 0.667 | 0.500 | 1.000 |   4 |  4 |  4 |  0 |  33 |
| CC: Green policies are geopolitical instruments: C... | 0.667 | 0.500 | 1.000 |   2 |  2 |  2 |  0 |  37 |
| CC: Hidden plots by secret schemes of powerful gro... | 0.667 | 1.000 | 0.500 |   2 |  1 |  0 |  1 |  39 |
| CC: Questioning the measurements and science: Scie... | 0.667 | 0.500 | 1.000 |   1 |  1 |  1 |  0 |  39 |
| URW: Amplifying war-related fears: There is a real... | 0.667 | 0.500 | 1.000 |   2 |  2 |  2 |  0 |  37 |
| URW: Blaming the war on others rather than the inv... | 0.667 | 0.500 | 1.000 |   1 |  1 |  1 |  0 |  39 |
| URW: Discrediting Ukraine: Other | 0.667 | 0.500 | 1.000 |   1 |  1 |  1 |  0 |  39 |
| URW: Praise of Russia: Praise of Russian President... | 0.667 | 0.500 | 1.000 |   1 |  1 |  1 |  0 |  39 |
| URW: Praise of Russia: Russia is a guarantor of pe... | 0.667 | 0.500 | 1.000 |   1 |  1 |  1 |  0 |  39 |
| CC: Criticism of climate movement: Ad hominem atta... | 0.571 | 0.500 | 0.667 |   3 |  2 |  2 |  1 |  36 |
| URW: Discrediting Ukraine: Ukraine is a puppet of ... | 0.545 | 0.375 | 1.000 |   3 |  3 |  5 |  0 |  33 |
| CC: Criticism of climate policies: Climate policie... | 0.500 | 0.333 | 1.000 |   1 |  1 |  2 |  0 |  38 |
| CC: Green policies are geopolitical instruments: O... | 0.500 | 0.333 | 1.000 |   1 |  1 |  2 |  0 |  38 |
| URW: Discrediting Ukraine: Discrediting Ukrainian ... | 0.500 | 0.333 | 1.000 |   3 |  3 |  6 |  0 |  32 |
| URW: Discrediting Ukraine: Discrediting Ukrainian ... | 0.500 | 0.333 | 1.000 |   2 |  2 |  4 |  0 |  35 |
| URW: Discrediting the West, Diplomacy: Diplomacy d... | 0.500 | 0.400 | 0.667 |   3 |  2 |  3 |  1 |  35 |
| URW: Speculating war outcomes: Ukrainian army is c... | 0.500 | 0.333 | 1.000 |   2 |  2 |  4 |  0 |  35 |
| Other | 0.471 | 0.667 | 0.364 |  11 |  4 |  2 |  7 |  28 |
| URW: Discrediting the West, Diplomacy: The West do... | 0.462 | 0.333 | 0.750 |   4 |  3 |  6 |  1 |  31 |
| CC: Criticism of institutions and authorities: Cri... | 0.400 | 0.286 | 0.667 |   3 |  2 |  5 |  1 |  33 |
| CC: Criticism of institutions and authorities: Other | 0.400 | 0.250 | 1.000 |   1 |  1 |  3 |  0 |  37 |
| CC: Questioning the measurements and science: Meth... | 0.400 | 0.500 | 0.333 |   3 |  1 |  1 |  2 |  37 |
| URW: Amplifying war-related fears: By continuing t... | 0.400 | 0.250 | 1.000 |   1 |  1 |  3 |  0 |  37 |
| URW: Discrediting Ukraine: Discrediting Ukrainian ... | 0.400 | 0.250 | 1.000 |   1 |  1 |  3 |  0 |  37 |
| CC: Controversy about green technologies: Other | 0.333 | 0.200 | 1.000 |   1 |  1 |  4 |  0 |  36 |
| URW: Discrediting Ukraine: Situation in Ukraine is... | 0.333 | 0.200 | 1.000 |   1 |  1 |  4 |  0 |  36 |
| URW: Discrediting the West, Diplomacy: The West is... | 0.333 | 0.200 | 1.000 |   1 |  1 |  4 |  0 |  36 |
| URW: Praise of Russia: Praise of Russian military ... | 0.333 | 0.200 | 1.000 |   1 |  1 |  4 |  0 |  36 |
| CC: Criticism of climate movement: Climate movemen... | 0.333 | 0.333 | 0.333 |   3 |  1 |  2 |  2 |  36 |
| CC: Criticism of institutions and authorities: Cri... | 0.286 | 0.200 | 0.500 |   2 |  1 |  4 |  1 |  35 |
| CC: Downplaying climate change: Other | 0.286 | 0.167 | 1.000 |   1 |  1 |  5 |  0 |  35 |
| URW: Russia is the Victim: Other | 0.286 | 0.167 | 1.000 |   1 |  1 |  5 |  0 |  35 |
| CC: Criticism of climate movement: Other | 0.250 | 0.167 | 0.500 |   4 |  2 | 10 |  2 |  27 |
| CC: Criticism of climate policies: Climate policie... | 0.200 | 0.111 | 1.000 |   1 |  1 |  8 |  0 |  32 |
| CC: Criticism of climate policies: Other | 0.143 | 0.077 | 1.000 |   1 |  1 | 12 |  0 |  28 |
| CC: Amplifying Climate Fears: Amplifying existing ... | 0.000 | 0.000 | 0.000 |   0 |  0 |  2 |  0 |  39 |
| CC: Amplifying Climate Fears: Doomsday scenarios f... | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 |  40 |
| CC: Climate change is beneficial: Temperature incr... | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 |  40 |
| CC: Controversy about green technologies: Renewabl... | 0.000 | 0.000 | 0.000 |   1 |  0 |  4 |  1 |  36 |
| CC: Controversy about green technologies: Renewabl... | 0.000 | 0.000 | 0.000 |   0 |  0 |  2 |  0 |  39 |
| CC: Criticism of climate policies: Climate policie... | 0.000 | 0.000 | 0.000 |   0 |  0 |  9 |  0 |  32 |
| CC: Criticism of institutions and authorities: Cri... | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 |  40 |
| CC: Downplaying climate change: CO2 concentrations... | 0.000 | 0.000 | 0.000 |   0 |  0 |  2 |  0 |  39 |
| CC: Downplaying climate change: Ice is not melting | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 |  40 |
| CC: Downplaying climate change: Temperature increa... | 0.000 | 0.000 | 0.000 |   0 |  0 |  3 |  0 |  38 |
| CC: Hidden plots by secret schemes of powerful gro... | 0.000 | 0.000 | 0.000 |   1 |  0 |  2 |  1 |  38 |
| CC: Hidden plots by secret schemes of powerful gro... | 0.000 | 0.000 | 0.000 |   1 |  0 |  0 |  1 |  40 |
| CC: Questioning the measurements and science: Data... | 0.000 | 0.000 | 0.000 |   1 |  0 |  0 |  1 |  40 |
| CC: Questioning the measurements and science: Gree... | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 |  40 |
| CC: Questioning the measurements and science: Other | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 |  40 |
| URW: Amplifying war-related fears: NATO should/wil... | 0.000 | 0.000 | 0.000 |   0 |  0 |  2 |  0 |  39 |
| URW: Amplifying war-related fears: Other | 0.000 | 0.000 | 0.000 |   0 |  0 |  8 |  0 |  33 |
| URW: Amplifying war-related fears: Russia will als... | 0.000 | 0.000 | 0.000 |   0 |  0 |  3 |  0 |  38 |
| URW: Blaming the war on others rather than the inv... | 0.000 | 0.000 | 0.000 |   0 |  0 |  4 |  0 |  37 |
| URW: Discrediting Ukraine: Rewriting Ukraine’s his... | 0.000 | 0.000 | 0.000 |   0 |  0 |  2 |  0 |  39 |
| URW: Discrediting Ukraine: Ukraine is a hub for cr... | 0.000 | 0.000 | 0.000 |   1 |  0 |  0 |  1 |  40 |
| URW: Discrediting the West, Diplomacy: The West is... | 0.000 | 0.000 | 0.000 |   0 |  0 |  2 |  0 |  39 |
| URW: Discrediting the West, Diplomacy: West is tir... | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 |  40 |
| URW: Distrust towards Media: Other | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 |  40 |
| URW: Distrust towards Media: Ukrainian media canno... | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 |  40 |
| URW: Hidden plots by secret schemes of powerful gr... | 0.000 | 0.000 | 0.000 |   0 |  0 |  2 |  0 |  39 |
| URW: Negative Consequences for the West: Other | 0.000 | 0.000 | 0.000 |   0 |  0 |  6 |  0 |  35 |
| URW: Negative Consequences for the West: Sanctions... | 0.000 | 0.000 | 0.000 |   1 |  0 |  1 |  1 |  39 |
| URW: Overpraising the West: NATO will destroy Russia | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 |  40 |
| URW: Overpraising the West: The West has the stron... | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 |  40 |
| URW: Praise of Russia: Other | 0.000 | 0.000 | 0.000 |   1 |  0 |  3 |  1 |  37 |
| URW: Praise of Russia: Russian invasion has strong... | 0.000 | 0.000 | 0.000 |   0 |  0 |  2 |  0 |  39 |
| URW: Russia is the Victim: Russia actions in Ukrai... | 0.000 | 0.000 | 0.000 |   0 |  0 |  5 |  0 |  36 |
| URW: Russia is the Victim: The West is russophobic | 0.000 | 0.000 | 0.000 |   1 |  0 |  3 |  1 |  37 |
| URW: Russia is the Victim: UA is anti-RU extremists | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 |  40 |
| URW: Speculating war outcomes: Other | 0.000 | 0.000 | 0.000 |   0 |  0 |  9 |  0 |  32 |
| URW: Speculating war outcomes: Russian army will l... | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 |  40 |

**Legend:**
- **TP**: True Positives (correctly predicted positive)
- **FP**: False Positives (incorrectly predicted positive)
- **FN**: False Negatives (incorrectly predicted negative)
- **TN**: True Negatives (correctly predicted negative)


### HI - Subnarratives

**Language**: HI  
**Model**: Google Gemini 2.5 Flash  
**Total Files**: 35  
**Total Labels**: 46  
**F1 Macro**: 0.2376  
**F1 Micro**: 0.3071  
**F1 Samples**: 0.2976  

#### Confusion Matrix Summary Table (46 labels)

| Label | F1 | Precision | Recall | Support | TP | FP | FN | TN |
|-------|----|-----------|--------|---------|----|----|----|----|
| URW: Amplifying war-related fears: There is a real... | 1.000 | 1.000 | 1.000 |   5 |  5 |  0 |  0 |  30 |
| URW: Distrust towards Media: Western media is an i... | 1.000 | 1.000 | 1.000 |   1 |  1 |  0 |  0 |  34 |
| CC: Amplifying Climate Fears: Amplifying existing ... | 0.857 | 1.000 | 0.750 |   4 |  3 |  0 |  1 |  31 |
| URW: Amplifying war-related fears: By continuing t... | 0.750 | 0.600 | 1.000 |   3 |  3 |  2 |  0 |  30 |
| URW: Discrediting the West, Diplomacy: West is tir... | 0.667 | 1.000 | 0.500 |   2 |  1 |  0 |  1 |  33 |
| URW: Amplifying war-related fears: Russia will als... | 0.571 | 0.667 | 0.500 |   4 |  2 |  1 |  2 |  30 |
| URW: Discrediting Ukraine: Ukraine is a puppet of ... | 0.500 | 0.333 | 1.000 |   1 |  1 |  2 |  0 |  32 |
| URW: Discrediting the West, Diplomacy: The West is... | 0.500 | 0.500 | 0.500 |   2 |  1 |  1 |  1 |  32 |
| URW: Speculating war outcomes: Ukrainian army is c... | 0.500 | 0.333 | 1.000 |   1 |  1 |  2 |  0 |  32 |
| URW: Praise of Russia: Russia has international su... | 0.471 | 0.571 | 0.400 |  10 |  4 |  3 |  6 |  22 |
| URW: Praise of Russia: Praise of Russian military ... | 0.462 | 0.300 | 1.000 |   3 |  3 |  7 |  0 |  25 |
| URW: Negative Consequences for the West: Sanctions... | 0.400 | 0.500 | 0.333 |   3 |  1 |  1 |  2 |  31 |
| URW: Russia is the Victim: Russia actions in Ukrai... | 0.364 | 0.222 | 1.000 |   2 |  2 |  7 |  0 |  26 |
| URW: Discrediting Ukraine: Discrediting Ukrainian ... | 0.333 | 0.333 | 0.333 |   3 |  1 |  2 |  2 |  30 |
| URW: Blaming the war on others rather than the inv... | 0.308 | 0.200 | 0.667 |   3 |  2 |  8 |  1 |  24 |
| Other | 0.286 | 0.200 | 0.500 |   2 |  1 |  4 |  1 |  29 |
| URW: Blaming the war on others rather than the inv... | 0.286 | 0.200 | 0.500 |   2 |  1 |  4 |  1 |  29 |
| URW: Discrediting the West, Diplomacy: Other | 0.286 | 0.182 | 0.667 |   3 |  2 |  9 |  1 |  23 |
| URW: Praise of Russia: Praise of Russian President... | 0.286 | 0.167 | 1.000 |   1 |  1 |  5 |  0 |  29 |
| URW: Discrediting the West, Diplomacy: The West is... | 0.250 | 0.143 | 1.000 |   1 |  1 |  6 |  0 |  28 |
| URW: Praise of Russia: Russia is a guarantor of pe... | 0.250 | 0.200 | 0.333 |   3 |  1 |  4 |  2 |  28 |
| URW: Discrediting the West, Diplomacy: The West do... | 0.222 | 0.167 | 0.333 |   3 |  1 |  5 |  2 |  27 |
| URW: Russia is the Victim: The West is russophobic | 0.200 | 0.333 | 0.143 |   7 |  1 |  2 |  6 |  26 |
| URW: Speculating war outcomes: Other | 0.182 | 0.111 | 0.500 |   2 |  1 |  8 |  1 |  25 |
| CC: Amplifying Climate Fears: Doomsday scenarios f... | 0.000 | 0.000 | 0.000 |   0 |  0 |  2 |  0 |  33 |
| CC: Amplifying Climate Fears: Other | 0.000 | 0.000 | 0.000 |   1 |  0 |  0 |  1 |  34 |
| URW: Amplifying war-related fears: NATO should/wil... | 0.000 | 0.000 | 0.000 |   1 |  0 |  4 |  1 |  30 |
| URW: Amplifying war-related fears: Other | 0.000 | 0.000 | 0.000 |   1 |  0 |  7 |  1 |  27 |
| URW: Blaming the war on others rather than the inv... | 0.000 | 0.000 | 0.000 |   0 |  0 |  3 |  0 |  32 |
| URW: Discrediting Ukraine: Discrediting Ukrainian ... | 0.000 | 0.000 | 0.000 |   0 |  0 |  4 |  0 |  31 |
| URW: Discrediting Ukraine: Discrediting Ukrainian ... | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 |  34 |
| URW: Discrediting Ukraine: Other | 0.000 | 0.000 | 0.000 |   0 |  0 |  3 |  0 |  32 |
| URW: Discrediting Ukraine: Rewriting Ukraine’s his... | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 |  34 |
| URW: Discrediting Ukraine: Situation in Ukraine is... | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 |  34 |
| URW: Discrediting Ukraine: Ukraine is associated w... | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 |  34 |
| URW: Discrediting the West, Diplomacy: Diplomacy d... | 0.000 | 0.000 | 0.000 |   2 |  0 |  6 |  2 |  27 |
| URW: Discrediting the West, Diplomacy: The EU is d... | 0.000 | 0.000 | 0.000 |   0 |  0 |  3 |  0 |  32 |
| URW: Distrust towards Media: Other | 0.000 | 0.000 | 0.000 |   1 |  0 |  2 |  1 |  32 |
| URW: Hidden plots by secret schemes of powerful gr... | 0.000 | 0.000 | 0.000 |   2 |  0 |  0 |  2 |  33 |
| URW: Negative Consequences for the West: Other | 0.000 | 0.000 | 0.000 |   0 |  0 |  7 |  0 |  28 |
| URW: Overpraising the West: The West has the stron... | 0.000 | 0.000 | 0.000 |   2 |  0 |  0 |  2 |  33 |
| URW: Praise of Russia: Other | 0.000 | 0.000 | 0.000 |   1 |  0 |  6 |  1 |  28 |
| URW: Russia is the Victim: Other | 0.000 | 0.000 | 0.000 |   0 |  0 |  6 |  0 |  29 |
| URW: Russia is the Victim: UA is anti-RU extremists | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 |  34 |
| URW: Speculating war outcomes: Russian army is col... | 0.000 | 0.000 | 0.000 |   2 |  0 |  0 |  2 |  33 |
| URW: Speculating war outcomes: Russian army will l... | 0.000 | 0.000 | 0.000 |   1 |  0 |  0 |  1 |  34 |

**Legend:**
- **TP**: True Positives (correctly predicted positive)
- **FP**: False Positives (incorrectly predicted positive)
- **FN**: False Negatives (incorrectly predicted negative)
- **TN**: True Negatives (correctly predicted negative)


### PT - Subnarratives

**Language**: PT  
**Model**: Google Gemini 2.5 Flash  
**Total Files**: 35  
**Total Labels**: 40  
**F1 Macro**: 0.3387  
**F1 Micro**: 0.4725  
**F1 Samples**: 0.4737  

#### Confusion Matrix Summary Table (40 labels)

| Label | F1 | Precision | Recall | Support | TP | FP | FN | TN |
|-------|----|-----------|--------|---------|----|----|----|----|
| CC: Criticism of institutions and authorities: Cri... | 1.000 | 1.000 | 1.000 |   1 |  1 |  0 |  0 |  34 |
| CC: Criticism of institutions and authorities: Other | 1.000 | 1.000 | 1.000 |   1 |  1 |  0 |  0 |  34 |
| URW: Discrediting Ukraine: Discrediting Ukrainian ... | 1.000 | 1.000 | 1.000 |   2 |  2 |  0 |  0 |  33 |
| URW: Discrediting Ukraine: Ukraine is a puppet of ... | 1.000 | 1.000 | 1.000 |   1 |  1 |  0 |  0 |  34 |
| URW: Praise of Russia: Other | 1.000 | 1.000 | 1.000 |   2 |  2 |  0 |  0 |  33 |
| URW: Russia is the Victim: Other | 0.750 | 0.600 | 1.000 |   3 |  3 |  2 |  0 |  30 |
| CC: Amplifying Climate Fears: Amplifying existing ... | 0.688 | 0.611 | 0.786 |  14 | 11 |  7 |  3 |  14 |
| CC: Amplifying Climate Fears: Earth will be uninha... | 0.667 | 0.500 | 1.000 |   1 |  1 |  1 |  0 |  33 |
| CC: Criticism of climate policies: Climate policie... | 0.667 | 1.000 | 0.500 |   2 |  1 |  0 |  1 |  33 |
| CC: Criticism of institutions and authorities: Cri... | 0.667 | 0.500 | 1.000 |   1 |  1 |  1 |  0 |  33 |
| URW: Discrediting the West, Diplomacy: Other | 0.667 | 0.800 | 0.571 |   7 |  4 |  1 |  3 |  27 |
| URW: Praise of Russia: Russia has international su... | 0.667 | 0.500 | 1.000 |   1 |  1 |  1 |  0 |  33 |
| CC: Criticism of institutions and authorities: Cri... | 0.545 | 0.429 | 0.750 |   4 |  3 |  4 |  1 |  27 |
| Other | 0.500 | 0.333 | 1.000 |   1 |  1 |  2 |  0 |  32 |
| URW: Praise of Russia: Russia is a guarantor of pe... | 0.500 | 0.500 | 0.500 |   2 |  1 |  1 |  1 |  32 |
| CC: Criticism of climate policies: Other | 0.444 | 0.667 | 0.333 |   6 |  2 |  1 |  4 |  28 |
| CC: Criticism of institutions and authorities: Cri... | 0.400 | 1.000 | 0.250 |   4 |  1 |  0 |  3 |  31 |
| URW: Discrediting the West, Diplomacy: Diplomacy d... | 0.400 | 0.250 | 1.000 |   1 |  1 |  3 |  0 |  31 |
| URW: Russia is the Victim: The West is russophobic | 0.400 | 0.250 | 1.000 |   1 |  1 |  3 |  0 |  31 |
| CC: Amplifying Climate Fears: Doomsday scenarios f... | 0.364 | 0.250 | 0.667 |   3 |  2 |  6 |  1 |  26 |
| CC: Amplifying Climate Fears: Other | 0.222 | 1.000 | 0.125 |  16 |  2 |  0 | 14 |  19 |
| CC: Controversy about green technologies: Other | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 |  34 |
| CC: Criticism of climate policies: Climate policie... | 0.000 | 0.000 | 0.000 |   1 |  0 |  4 |  1 |  30 |
| CC: Criticism of climate policies: Climate policie... | 0.000 | 0.000 | 0.000 |   0 |  0 |  3 |  0 |  32 |
| CC: Green policies are geopolitical instruments: C... | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 |  34 |
| CC: Green policies are geopolitical instruments: G... | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 |  34 |
| CC: Green policies are geopolitical instruments: O... | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 |  34 |
| CC: Hidden plots by secret schemes of powerful gro... | 0.000 | 0.000 | 0.000 |   1 |  0 |  0 |  1 |  34 |
| URW: Amplifying war-related fears: Other | 0.000 | 0.000 | 0.000 |   1 |  0 |  0 |  1 |  34 |
| URW: Blaming the war on others rather than the inv... | 0.000 | 0.000 | 0.000 |   0 |  0 |  2 |  0 |  33 |
| URW: Blaming the war on others rather than the inv... | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 |  34 |
| URW: Discrediting Ukraine: Other | 0.000 | 0.000 | 0.000 |   1 |  0 |  0 |  1 |  34 |
| URW: Discrediting Ukraine: Situation in Ukraine is... | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 |  34 |
| URW: Discrediting the West, Diplomacy: The West do... | 0.000 | 0.000 | 0.000 |   0 |  0 |  2 |  0 |  33 |
| URW: Discrediting the West, Diplomacy: The West is... | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 |  34 |
| URW: Discrediting the West, Diplomacy: The West is... | 0.000 | 0.000 | 0.000 |   0 |  0 |  5 |  0 |  30 |
| URW: Discrediting the West, Diplomacy: West is tir... | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 |  34 |
| URW: Negative Consequences for the West: Other | 0.000 | 0.000 | 0.000 |   1 |  0 |  0 |  1 |  34 |
| URW: Negative Consequences for the West: Sanctions... | 0.000 | 0.000 | 0.000 |   0 |  0 |  2 |  0 |  33 |
| URW: Russia is the Victim: Russia actions in Ukrai... | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 |  34 |

**Legend:**
- **TP**: True Positives (correctly predicted positive)
- **FP**: False Positives (incorrectly predicted positive)
- **FN**: False Negatives (incorrectly predicted negative)
- **TN**: True Negatives (correctly predicted negative)


### RU - Subnarratives

**Language**: RU  
**Model**: Google Gemini 2.5 Flash  
**Total Files**: 32  
**Total Labels**: 41  
**F1 Macro**: 0.3241  
**F1 Micro**: 0.4453  
**F1 Samples**: 0.4754  

#### Confusion Matrix Summary Table (41 labels)

| Label | F1 | Precision | Recall | Support | TP | FP | FN | TN |
|-------|----|-----------|--------|---------|----|----|----|----|
| Other | 1.000 | 1.000 | 1.000 |   4 |  4 |  0 |  0 |  28 |
| URW: Negative Consequences for the West: Sanctions... | 1.000 | 1.000 | 1.000 |   1 |  1 |  0 |  0 |  31 |
| URW: Praise of Russia: Praise of Russian President... | 1.000 | 1.000 | 1.000 |   2 |  2 |  0 |  0 |  30 |
| URW: Praise of Russia: Praise of Russian military ... | 0.909 | 0.833 | 1.000 |   5 |  5 |  1 |  0 |  26 |
| URW: Russia is the Victim: The West is russophobic | 0.800 | 0.667 | 1.000 |   2 |  2 |  1 |  0 |  29 |
| URW: Discrediting Ukraine: Discrediting Ukrainian ... | 0.783 | 0.643 | 1.000 |   9 |  9 |  5 |  0 |  18 |
| URW: Praise of Russia: Russia is a guarantor of pe... | 0.750 | 1.000 | 0.600 |   5 |  3 |  0 |  2 |  27 |
| URW: Discrediting Ukraine: Ukraine is associated w... | 0.667 | 0.500 | 1.000 |   1 |  1 |  1 |  0 |  30 |
| URW: Discrediting the West, Diplomacy: The EU is d... | 0.667 | 0.500 | 1.000 |   2 |  2 |  2 |  0 |  28 |
| URW: Speculating war outcomes: Ukrainian army is c... | 0.667 | 0.500 | 1.000 |   2 |  2 |  2 |  0 |  28 |
| URW: Discrediting Ukraine: Ukraine is a puppet of ... | 0.571 | 0.400 | 1.000 |   4 |  4 |  6 |  0 |  22 |
| URW: Discrediting Ukraine: Discrediting Ukrainian ... | 0.571 | 0.444 | 0.800 |   5 |  4 |  5 |  1 |  22 |
| URW: Discrediting the West, Diplomacy: The West do... | 0.571 | 0.444 | 0.800 |   5 |  4 |  5 |  1 |  22 |
| URW: Amplifying war-related fears: NATO should/wil... | 0.500 | 0.500 | 0.500 |   2 |  1 |  1 |  1 |  29 |
| URW: Discrediting Ukraine: Ukraine is a hub for cr... | 0.500 | 0.500 | 0.500 |   2 |  1 |  1 |  1 |  29 |
| URW: Discrediting the West, Diplomacy: Diplomacy d... | 0.444 | 0.286 | 1.000 |   2 |  2 |  5 |  0 |  25 |
| URW: Discrediting the West, Diplomacy: The West is... | 0.444 | 0.286 | 1.000 |   2 |  2 |  5 |  0 |  25 |
| URW: Praise of Russia: Russia has international su... | 0.444 | 0.500 | 0.400 |   5 |  2 |  2 |  3 |  25 |
| URW: Blaming the war on others rather than the inv... | 0.400 | 0.286 | 0.667 |   3 |  2 |  5 |  1 |  24 |
| URW: Speculating war outcomes: Other | 0.364 | 0.222 | 1.000 |   2 |  2 |  7 |  0 |  23 |
| URW: Discrediting the West, Diplomacy: Other | 0.235 | 0.154 | 0.500 |   4 |  2 | 11 |  2 |  17 |
| URW: Amplifying war-related fears: By continuing t... | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 |  31 |
| URW: Amplifying war-related fears: Other | 0.000 | 0.000 | 0.000 |   0 |  0 |  2 |  0 |  30 |
| URW: Amplifying war-related fears: There is a real... | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 |  31 |
| URW: Blaming the war on others rather than the inv... | 0.000 | 0.000 | 0.000 |   0 |  0 |  3 |  0 |  29 |
| URW: Blaming the war on others rather than the inv... | 0.000 | 0.000 | 0.000 |   1 |  0 |  6 |  1 |  25 |
| URW: Discrediting Ukraine: Discrediting Ukrainian ... | 0.000 | 0.000 | 0.000 |   0 |  0 |  4 |  0 |  28 |
| URW: Discrediting Ukraine: Other | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 |  31 |
| URW: Discrediting Ukraine: Rewriting Ukraine’s his... | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 |  31 |
| URW: Discrediting Ukraine: Situation in Ukraine is... | 0.000 | 0.000 | 0.000 |   0 |  0 |  6 |  0 |  26 |
| URW: Discrediting the West, Diplomacy: The West is... | 0.000 | 0.000 | 0.000 |   2 |  0 |  1 |  2 |  29 |
| URW: Discrediting the West, Diplomacy: West is tir... | 0.000 | 0.000 | 0.000 |   2 |  0 |  0 |  2 |  30 |
| URW: Distrust towards Media: Ukrainian media canno... | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 |  31 |
| URW: Distrust towards Media: Western media is an i... | 0.000 | 0.000 | 0.000 |   2 |  0 |  0 |  2 |  30 |
| URW: Hidden plots by secret schemes of powerful gr... | 0.000 | 0.000 | 0.000 |   1 |  0 |  3 |  1 |  28 |
| URW: Negative Consequences for the West: Other | 0.000 | 0.000 | 0.000 |   0 |  0 |  4 |  0 |  28 |
| URW: Praise of Russia: Other | 0.000 | 0.000 | 0.000 |   1 |  0 |  8 |  1 |  23 |
| URW: Praise of Russia: Russian invasion has strong... | 0.000 | 0.000 | 0.000 |   0 |  0 |  3 |  0 |  29 |
| URW: Russia is the Victim: Other | 0.000 | 0.000 | 0.000 |   0 |  0 |  5 |  0 |  27 |
| URW: Russia is the Victim: Russia actions in Ukrai... | 0.000 | 0.000 | 0.000 |   0 |  0 |  2 |  0 |  30 |
| URW: Russia is the Victim: UA is anti-RU extremists | 0.000 | 0.000 | 0.000 |   1 |  0 |  3 |  1 |  28 |

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

**Generated for**: Gemini 2.5 Flash - No Validation Devset  
**Model**: Google Gemini 2.5 Flash  
**Languages**: BG, EN, HI, PT, RU
