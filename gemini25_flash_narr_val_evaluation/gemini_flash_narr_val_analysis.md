# Gemini 2.5 Flash Results Analysis

**Experiment**: Gemini 2.5 Flash - Narrative Validation Devset  
**Model**: Google Gemini 2.5 Flash  
**Languages Analyzed**: BG, EN, HI, PT, RU  
**Primary Metric**: F1 Samples  

This analysis summarizes the performance of Gemini 2.5 Flash across different languages for hierarchical text classification.


## Language Performance Comparison

| Language | Model | Files | Narratives F1 Samples | Subnarratives F1 Samples | Narratives Labels | Subnarratives Labels |
|----------|-------|-------|----------------------|--------------------------|-------------------|----------------------|
| PT | Google Gemini 2.5 Flash | 35 | 0.7335 | 0.4681 | 15 | 43 |
| RU | Google Gemini 2.5 Flash | 32 | 0.7080 | 0.4786 | 11 | 41 |
| BG | Google Gemini 2.5 Flash | 35 | 0.5721 | 0.4049 | 21 | 74 |
| EN | Google Gemini 2.5 Flash | 41 | 0.5241 | 0.3675 | 22 | 84 |
| HI | Google Gemini 2.5 Flash | 35 | 0.4217 | 0.3082 | 13 | 44 |



## Performance Insights

### Overall Performance Rankings

**Best Overall Performance**: PT (Combined F1 Samples: 1.2017)

**Lowest Overall Performance**: HI (Combined F1 Samples: 0.7300)

**Best Narratives Performance**: PT (F1 Samples: 0.7335)

**Best Subnarratives Performance**: RU (F1 Samples: 0.4786)

### Performance Statistics

**Narratives F1 Samples**:
- Average: 0.5919
- Range: 0.4217 - 0.7335
- Standard Deviation: 0.1162

**Subnarratives F1 Samples**:
- Average: 0.4055
- Range: 0.3082 - 0.4786
- Standard Deviation: 0.0635

### Narratives vs Subnarratives Performance Gap

- Average gap (Narratives - Subnarratives): 0.1864
- Languages with smallest gap: HI
- Languages with largest gap: PT




## Narratives Performance by Language (Top 15)

### BG (Google Gemini 2.5 Flash)

**Overall Performance**: F1 Samples: 0.5721 | F1 Macro: 0.4060 | F1 Micro: 0.5290 | Files: 35 | Labels: 21

| Rank | Label | F1 Score | Precision | Recall | Support | TP | FP | FN | TN |
|------|-------|----------|-----------|--------|---------|----|----|----|----|
|  1 | CC: Amplifying Climate Fears | 0.947 | 0.900 | 1.000 |   9 |  9 |  1 |  0 | 25 |
|  2 | URW: Discrediting Ukraine | 0.833 | 0.714 | 1.000 |   5 |  5 |  2 |  0 | 28 |
|  3 | CC: Criticism of climate policies | 0.800 | 0.667 | 1.000 |   2 |  2 |  1 |  0 | 32 |
|  4 | URW: Amplifying war-related fears | 0.769 | 0.625 | 1.000 |   5 |  5 |  3 |  0 | 27 |
|  5 | CC: Criticism of climate movement | 0.667 | 0.500 | 1.000 |   1 |  1 |  1 |  0 | 33 |
|  6 | CC: Criticism of institutions and authorities | 0.667 | 0.500 | 1.000 |   3 |  3 |  3 |  0 | 29 |
|  7 | CC: Downplaying climate change | 0.667 | 1.000 | 0.500 |   4 |  2 |  0 |  2 | 31 |
|  8 | CC: Hidden plots by secret schemes of powerful groups | 0.667 | 1.000 | 0.500 |   2 |  1 |  0 |  1 | 33 |
|  9 | Other | 0.600 | 0.750 | 0.500 |   6 |  3 |  1 |  3 | 28 |
| 10 | URW: Negative Consequences for the West | 0.545 | 0.375 | 1.000 |   3 |  3 |  5 |  0 | 27 |
| 11 | URW: Discrediting the West, Diplomacy | 0.500 | 0.364 | 0.800 |   5 |  4 |  7 |  1 | 23 |
| 12 | URW: Praise of Russia | 0.500 | 0.500 | 0.500 |   2 |  1 |  1 |  1 | 32 |
| 13 | URW: Russia is the Victim | 0.364 | 0.250 | 0.667 |   3 |  2 |  6 |  1 | 26 |
| 14 | CC: Controversy about green technologies | 0.000 | 0.000 | 0.000 |   0 |  0 |  3 |  0 | 32 |
| 15 | CC: Green policies are geopolitical instruments | 0.000 | 0.000 | 0.000 |   1 |  0 |  3 |  1 | 31 |

### EN (Google Gemini 2.5 Flash)

**Overall Performance**: F1 Samples: 0.5241 | F1 Macro: 0.5369 | F1 Micro: 0.5607 | Files: 41 | Labels: 22

| Rank | Label | F1 Score | Precision | Recall | Support | TP | FP | FN | TN |
|------|-------|----------|-----------|--------|---------|----|----|----|----|
|  1 | CC: Climate change is beneficial | 1.000 | 1.000 | 1.000 |   1 |  1 |  0 |  0 | 40 |
|  2 | URW: Overpraising the West | 1.000 | 1.000 | 1.000 |   1 |  1 |  0 |  0 | 40 |
|  3 | URW: Discrediting the West, Diplomacy | 0.947 | 0.900 | 1.000 |   9 |  9 |  1 |  0 | 31 |
|  4 | CC: Questioning the measurements and science | 0.889 | 0.800 | 1.000 |   4 |  4 |  1 |  0 | 36 |
|  5 | URW: Discrediting Ukraine | 0.824 | 0.700 | 1.000 |   7 |  7 |  3 |  0 | 31 |
|  6 | URW: Distrust towards Media | 0.800 | 0.667 | 1.000 |   4 |  4 |  2 |  0 | 35 |
|  7 | CC: Green policies are geopolitical instruments | 0.667 | 0.667 | 0.667 |   3 |  2 |  1 |  1 | 37 |
|  8 | URW: Blaming the war on others rather than the invader | 0.667 | 0.667 | 0.667 |   6 |  4 |  2 |  2 | 33 |
|  9 | CC: Hidden plots by secret schemes of powerful groups | 0.600 | 0.500 | 0.750 |   4 |  3 |  3 |  1 | 34 |
| 10 | CC: Criticism of climate movement | 0.571 | 0.462 | 0.750 |   8 |  6 |  7 |  2 | 26 |
| 11 | CC: Criticism of institutions and authorities | 0.522 | 0.400 | 0.750 |   8 |  6 |  9 |  2 | 24 |
| 12 | URW: Amplifying war-related fears | 0.500 | 0.333 | 1.000 |   3 |  3 |  6 |  0 | 32 |
| 13 | URW: Russia is the Victim | 0.500 | 0.333 | 1.000 |   2 |  2 |  4 |  0 | 35 |
| 14 | Other | 0.471 | 0.667 | 0.364 |  11 |  4 |  2 |  7 | 28 |
| 15 | CC: Controversy about green technologies | 0.444 | 0.286 | 1.000 |   2 |  2 |  5 |  0 | 34 |

### HI (Google Gemini 2.5 Flash)

**Overall Performance**: F1 Samples: 0.4217 | F1 Macro: 0.3795 | F1 Micro: 0.4474 | Files: 35 | Labels: 13

| Rank | Label | F1 Score | Precision | Recall | Support | TP | FP | FN | TN |
|------|-------|----------|-----------|--------|---------|----|----|----|----|
|  1 | CC: Amplifying Climate Fears | 0.857 | 1.000 | 0.750 |   4 |  3 |  0 |  1 | 31 |
|  2 | URW: Amplifying war-related fears | 0.737 | 0.636 | 0.875 |   8 |  7 |  4 |  1 | 23 |
|  3 | URW: Praise of Russia | 0.636 | 0.778 | 0.538 |  13 |  7 |  2 |  6 | 20 |
|  4 | URW: Discrediting the West, Diplomacy | 0.526 | 0.417 | 0.714 |   7 |  5 |  7 |  2 | 21 |
|  5 | URW: Distrust towards Media | 0.500 | 0.500 | 0.500 |   2 |  1 |  1 |  1 | 32 |
|  6 | Other | 0.333 | 0.200 | 1.000 |   2 |  2 |  8 |  0 | 25 |
|  7 | URW: Speculating war outcomes | 0.308 | 0.250 | 0.400 |   5 |  2 |  6 |  3 | 24 |
|  8 | URW: Russia is the Victim | 0.300 | 0.273 | 0.333 |   9 |  3 |  8 |  6 | 18 |
|  9 | URW: Blaming the war on others rather than the invader | 0.286 | 0.222 | 0.400 |   5 |  2 |  7 |  3 | 23 |
| 10 | URW: Discrediting Ukraine | 0.250 | 0.200 | 0.333 |   3 |  1 |  4 |  2 | 28 |
| 11 | URW: Negative Consequences for the West | 0.200 | 0.143 | 0.333 |   3 |  1 |  6 |  2 | 26 |
| 12 | URW: Hidden plots by secret schemes of powerful groups | 0.000 | 0.000 | 0.000 |   2 |  0 |  0 |  2 | 33 |
| 13 | URW: Overpraising the West | 0.000 | 0.000 | 0.000 |   2 |  0 |  0 |  2 | 33 |

### PT (Google Gemini 2.5 Flash)

**Overall Performance**: F1 Samples: 0.7335 | F1 Macro: 0.5455 | F1 Micro: 0.7302 | Files: 35 | Labels: 15

| Rank | Label | F1 Score | Precision | Recall | Support | TP | FP | FN | TN |
|------|-------|----------|-----------|--------|---------|----|----|----|----|
|  1 | CC: Hidden plots by secret schemes of powerful groups | 1.000 | 1.000 | 1.000 |   1 |  1 |  0 |  0 | 34 |
|  2 | URW: Amplifying war-related fears | 1.000 | 1.000 | 1.000 |   1 |  1 |  0 |  0 | 34 |
|  3 | URW: Russia is the Victim | 1.000 | 1.000 | 1.000 |   3 |  3 |  0 |  0 | 32 |
|  4 | URW: Praise of Russia | 0.857 | 1.000 | 0.750 |   4 |  3 |  0 |  1 | 31 |
|  5 | CC: Amplifying Climate Fears | 0.850 | 1.000 | 0.739 |  23 | 17 |  0 |  6 | 12 |
|  6 | CC: Criticism of climate policies | 0.824 | 0.875 | 0.778 |   9 |  7 |  1 |  2 | 25 |
|  7 | URW: Discrediting Ukraine | 0.800 | 1.000 | 0.667 |   3 |  2 |  0 |  1 | 32 |
|  8 | CC: Criticism of institutions and authorities | 0.737 | 0.636 | 0.875 |   8 |  7 |  4 |  1 | 23 |
|  9 | URW: Discrediting the West, Diplomacy | 0.615 | 0.800 | 0.500 |   8 |  4 |  1 |  4 | 26 |
| 10 | Other | 0.500 | 0.333 | 1.000 |   1 |  1 |  2 |  0 | 32 |
| 11 | CC: Green policies are geopolitical instruments | 0.000 | 0.000 | 0.000 |   0 |  0 |  2 |  0 | 33 |
| 12 | URW: Blaming the war on others rather than the invader | 0.000 | 0.000 | 0.000 |   0 |  0 |  4 |  0 | 31 |
| 13 | URW: Hidden plots by secret schemes of powerful groups | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 | 34 |
| 14 | URW: Negative Consequences for the West | 0.000 | 0.000 | 0.000 |   1 |  0 |  2 |  1 | 32 |
| 15 | URW: Overpraising the West | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 | 34 |

### RU (Google Gemini 2.5 Flash)

**Overall Performance**: F1 Samples: 0.7080 | F1 Macro: 0.5802 | F1 Micro: 0.6928 | Files: 32 | Labels: 11

| Rank | Label | F1 Score | Precision | Recall | Support | TP | FP | FN | TN |
|------|-------|----------|-----------|--------|---------|----|----|----|----|
|  1 | Other | 1.000 | 1.000 | 1.000 |   4 |  4 |  0 |  0 | 28 |
|  2 | URW: Discrediting Ukraine | 0.857 | 0.750 | 1.000 |  15 | 15 |  5 |  0 | 12 |
|  3 | URW: Praise of Russia | 0.857 | 0.923 | 0.800 |  15 | 12 |  1 |  3 | 16 |
|  4 | URW: Discrediting the West, Diplomacy | 0.759 | 0.786 | 0.733 |  15 | 11 |  3 |  4 | 14 |
|  5 | URW: Speculating war outcomes | 0.667 | 0.500 | 1.000 |   3 |  3 |  3 |  0 | 26 |
|  6 | URW: Amplifying war-related fears | 0.571 | 0.400 | 1.000 |   2 |  2 |  3 |  0 | 27 |
|  7 | URW: Russia is the Victim | 0.500 | 0.400 | 0.667 |   3 |  2 |  3 |  1 | 26 |
|  8 | URW: Distrust towards Media | 0.400 | 0.333 | 0.500 |   2 |  1 |  2 |  1 | 28 |
|  9 | URW: Hidden plots by secret schemes of powerful groups | 0.286 | 0.167 | 1.000 |   1 |  1 |  5 |  0 | 26 |
| 10 | URW: Negative Consequences for the West | 0.286 | 0.167 | 1.000 |   1 |  1 |  5 |  0 | 26 |
| 11 | URW: Blaming the war on others rather than the invader | 0.200 | 0.167 | 0.250 |   4 |  1 |  5 |  3 | 23 |




## Subnarratives Performance by Language (Top 15)

### BG (Google Gemini 2.5 Flash)

**Overall Performance**: F1 Samples: 0.4049 | F1 Macro: 0.2260 | F1 Micro: 0.3538 | Files: 35 | Labels: 74

| Rank | Label | F1 Score | Precision | Recall | Support | TP | FP | FN | TN |
|------|-------|----------|-----------|--------|---------|----|----|----|----|
|  1 | CC: Amplifying Climate Fears: Amplifying existing fears of g... | 1.000 | 1.000 | 1.000 |   9 |  9 |  0 |  0 | 26 |
|  2 | CC: Criticism of climate policies: Climate policies are only... | 1.000 | 1.000 | 1.000 |   1 |  1 |  0 |  0 | 34 |
|  3 | CC: Downplaying climate change: Climate cycles are natural | 1.000 | 1.000 | 1.000 |   1 |  1 |  0 |  0 | 34 |
|  4 | CC: Hidden plots by secret schemes of powerful groups: Blami... | 1.000 | 1.000 | 1.000 |   1 |  1 |  0 |  0 | 34 |
|  5 | CC: Hidden plots by secret schemes of powerful groups: Other | 1.000 | 1.000 | 1.000 |   1 |  1 |  0 |  0 | 34 |
|  6 | URW: Amplifying war-related fears: There is a real possibili... | 1.000 | 1.000 | 1.000 |   2 |  2 |  0 |  0 | 33 |
|  7 | CC: Criticism of climate movement: Climate movement is alarmist | 0.667 | 0.500 | 1.000 |   1 |  1 |  1 |  0 | 33 |
|  8 | CC: Criticism of climate movement: Other | 0.667 | 0.500 | 1.000 |   1 |  1 |  1 |  0 | 33 |
|  9 | CC: Criticism of climate policies: Climate policies have neg... | 0.667 | 0.500 | 1.000 |   1 |  1 |  1 |  0 | 33 |
| 10 | URW: Amplifying war-related fears: By continuing the war we ... | 0.667 | 0.500 | 1.000 |   1 |  1 |  1 |  0 | 33 |
| 11 | URW: Discrediting Ukraine: Ukraine is a hub for criminal act... | 0.667 | 0.500 | 1.000 |   1 |  1 |  1 |  0 | 33 |
| 12 | URW: Praise of Russia: Praise of Russian President Vladimir ... | 0.667 | 0.500 | 1.000 |   1 |  1 |  1 |  0 | 33 |
| 13 | Other | 0.600 | 0.750 | 0.500 |   6 |  3 |  1 |  3 | 28 |
| 14 | URW: Negative Consequences for the West: Other | 0.600 | 0.429 | 1.000 |   3 |  3 |  4 |  0 | 28 |
| 15 | URW: Discrediting Ukraine: Discrediting Ukrainian government... | 0.571 | 0.400 | 1.000 |   2 |  2 |  3 |  0 | 30 |

### EN (Google Gemini 2.5 Flash)

**Overall Performance**: F1 Samples: 0.3675 | F1 Macro: 0.2947 | F1 Micro: 0.3617 | Files: 41 | Labels: 84

| Rank | Label | F1 Score | Precision | Recall | Support | TP | FP | FN | TN |
|------|-------|----------|-----------|--------|---------|----|----|----|----|
|  1 | CC: Climate change is beneficial: CO2 is beneficial | 1.000 | 1.000 | 1.000 |   1 |  1 |  0 |  0 | 40 |
|  2 | URW: Discrediting Ukraine: Ukraine is a hub for criminal act... | 1.000 | 1.000 | 1.000 |   1 |  1 |  0 |  0 | 40 |
|  3 | URW: Discrediting the West, Diplomacy: The EU is divided | 1.000 | 1.000 | 1.000 |   1 |  1 |  0 |  0 | 40 |
|  4 | URW: Overpraising the West: The West belongs in the right si... | 1.000 | 1.000 | 1.000 |   1 |  1 |  0 |  0 | 40 |
|  5 | URW: Praise of Russia: Russia is a guarantor of peace and pr... | 1.000 | 1.000 | 1.000 |   1 |  1 |  0 |  0 | 40 |
|  6 | URW: Discrediting the West, Diplomacy: Other | 0.857 | 0.750 | 1.000 |   6 |  6 |  2 |  0 | 33 |
|  7 | CC: Downplaying climate change: Human activities do not impa... | 0.800 | 0.667 | 1.000 |   2 |  2 |  1 |  0 | 38 |
|  8 | CC: Green policies are geopolitical instruments: Climate-rel... | 0.800 | 0.667 | 1.000 |   2 |  2 |  1 |  0 | 38 |
|  9 | URW: Discrediting Ukraine: Ukraine is associated with nazism | 0.800 | 0.667 | 1.000 |   2 |  2 |  1 |  0 | 38 |
| 10 | URW: Distrust towards Media: Western media is an instrument ... | 0.750 | 0.750 | 0.750 |   4 |  3 |  1 |  1 | 36 |
| 11 | CC: Questioning the measurements and science: Methodologies/... | 0.667 | 0.667 | 0.667 |   3 |  2 |  1 |  1 | 37 |
| 12 | CC: Questioning the measurements and science: Scientific com... | 0.667 | 0.500 | 1.000 |   1 |  1 |  1 |  0 | 39 |
| 13 | URW: Amplifying war-related fears: There is a real possibili... | 0.667 | 0.500 | 1.000 |   2 |  2 |  2 |  0 | 37 |
| 14 | URW: Blaming the war on others rather than the invader: The ... | 0.667 | 0.667 | 0.667 |   6 |  4 |  2 |  2 | 33 |
| 15 | URW: Praise of Russia: Praise of Russian President Vladimir ... | 0.667 | 0.500 | 1.000 |   1 |  1 |  1 |  0 | 39 |

### HI (Google Gemini 2.5 Flash)

**Overall Performance**: F1 Samples: 0.3082 | F1 Macro: 0.2529 | F1 Micro: 0.3175 | Files: 35 | Labels: 44

| Rank | Label | F1 Score | Precision | Recall | Support | TP | FP | FN | TN |
|------|-------|----------|-----------|--------|---------|----|----|----|----|
|  1 | URW: Amplifying war-related fears: There is a real possibili... | 1.000 | 1.000 | 1.000 |   5 |  5 |  0 |  0 | 30 |
|  2 | URW: Distrust towards Media: Western media is an instrument ... | 1.000 | 1.000 | 1.000 |   1 |  1 |  0 |  0 | 34 |
|  3 | CC: Amplifying Climate Fears: Amplifying existing fears of g... | 0.857 | 1.000 | 0.750 |   4 |  3 |  0 |  1 | 31 |
|  4 | URW: Amplifying war-related fears: By continuing the war we ... | 0.750 | 0.600 | 1.000 |   3 |  3 |  2 |  0 | 30 |
|  5 | URW: Discrediting the West, Diplomacy: The West is overreacting | 0.667 | 1.000 | 0.500 |   2 |  1 |  0 |  1 | 33 |
|  6 | URW: Discrediting the West, Diplomacy: West is tired of Ukraine | 0.667 | 1.000 | 0.500 |   2 |  1 |  0 |  1 | 33 |
|  7 | URW: Speculating war outcomes: Russian army is collapsing | 0.667 | 1.000 | 0.500 |   2 |  1 |  0 |  1 | 33 |
|  8 | URW: Praise of Russia: Russia has international support from... | 0.667 | 0.750 | 0.600 |  10 |  6 |  2 |  4 | 23 |
|  9 | URW: Praise of Russia: Praise of Russian military might | 0.444 | 0.333 | 0.667 |   3 |  2 |  4 |  1 | 28 |
| 10 | URW: Amplifying war-related fears: Russia will also attack o... | 0.400 | 1.000 | 0.250 |   4 |  1 |  0 |  3 | 31 |
| 11 | URW: Discrediting Ukraine: Ukraine is a puppet of the West | 0.400 | 0.250 | 1.000 |   1 |  1 |  3 |  0 | 31 |
| 12 | URW: Negative Consequences for the West: Sanctions imposed b... | 0.400 | 0.500 | 0.333 |   3 |  1 |  1 |  2 | 31 |
| 13 | URW: Praise of Russia: Praise of Russian President Vladimir ... | 0.400 | 0.250 | 1.000 |   1 |  1 |  3 |  0 | 31 |
| 14 | URW: Discrediting the West, Diplomacy: Other | 0.364 | 0.250 | 0.667 |   3 |  2 |  6 |  1 | 26 |
| 15 | Other | 0.333 | 0.200 | 1.000 |   2 |  2 |  8 |  0 | 25 |

### PT (Google Gemini 2.5 Flash)

**Overall Performance**: F1 Samples: 0.4681 | F1 Macro: 0.3100 | F1 Micro: 0.4757 | Files: 35 | Labels: 43

| Rank | Label | F1 Score | Precision | Recall | Support | TP | FP | FN | TN |
|------|-------|----------|-----------|--------|---------|----|----|----|----|
|  1 | CC: Criticism of climate policies: Climate policies are only... | 1.000 | 1.000 | 1.000 |   2 |  2 |  0 |  0 | 33 |
|  2 | CC: Criticism of institutions and authorities: Criticism of ... | 1.000 | 1.000 | 1.000 |   1 |  1 |  0 |  0 | 34 |
|  3 | URW: Discrediting Ukraine: Discrediting Ukrainian government... | 1.000 | 1.000 | 1.000 |   2 |  2 |  0 |  0 | 33 |
|  4 | URW: Russia is the Victim: Other | 1.000 | 1.000 | 1.000 |   3 |  3 |  0 |  0 | 32 |
|  5 | CC: Criticism of institutions and authorities: Criticism of ... | 0.800 | 0.667 | 1.000 |   4 |  4 |  2 |  0 | 29 |
|  6 | URW: Praise of Russia: Other | 0.800 | 0.667 | 1.000 |   2 |  2 |  1 |  0 | 32 |
|  7 | CC: Amplifying Climate Fears: Amplifying existing fears of g... | 0.733 | 0.688 | 0.786 |  14 | 11 |  5 |  3 | 16 |
|  8 | CC: Criticism of institutions and authorities: Criticism of ... | 0.667 | 0.500 | 1.000 |   1 |  1 |  1 |  0 | 33 |
|  9 | URW: Discrediting Ukraine: Ukraine is a puppet of the West | 0.667 | 0.500 | 1.000 |   1 |  1 |  1 |  0 | 33 |
| 10 | URW: Praise of Russia: Russia has international support from... | 0.667 | 0.500 | 1.000 |   1 |  1 |  1 |  0 | 33 |
| 11 | URW: Russia is the Victim: The West is russophobic | 0.667 | 0.500 | 1.000 |   1 |  1 |  1 |  0 | 33 |
| 12 | CC: Amplifying Climate Fears: Earth will be uninhabitable soon | 0.500 | 0.333 | 1.000 |   1 |  1 |  2 |  0 | 32 |
| 13 | CC: Criticism of institutions and authorities: Other | 0.500 | 0.333 | 1.000 |   1 |  1 |  2 |  0 | 32 |
| 14 | Other | 0.500 | 0.333 | 1.000 |   1 |  1 |  2 |  0 | 32 |
| 15 | URW: Discrediting the West, Diplomacy: Diplomacy does/will n... | 0.500 | 0.333 | 1.000 |   1 |  1 |  2 |  0 | 32 |

### RU (Google Gemini 2.5 Flash)

**Overall Performance**: F1 Samples: 0.4786 | F1 Macro: 0.3323 | F1 Micro: 0.4392 | Files: 32 | Labels: 41

| Rank | Label | F1 Score | Precision | Recall | Support | TP | FP | FN | TN |
|------|-------|----------|-----------|--------|---------|----|----|----|----|
|  1 | Other | 1.000 | 1.000 | 1.000 |   4 |  4 |  0 |  0 | 28 |
|  2 | URW: Praise of Russia: Praise of Russian military might | 0.833 | 0.714 | 1.000 |   5 |  5 |  2 |  0 | 25 |
|  3 | URW: Speculating war outcomes: Ukrainian army is collapsing | 0.800 | 0.667 | 1.000 |   2 |  2 |  1 |  0 | 29 |
|  4 | URW: Discrediting Ukraine: Discrediting Ukrainian government... | 0.720 | 0.562 | 1.000 |   9 |  9 |  7 |  0 | 16 |
|  5 | URW: Discrediting Ukraine: Ukraine is a hub for criminal act... | 0.667 | 1.000 | 0.500 |   2 |  1 |  0 |  1 | 30 |
|  6 | URW: Discrediting Ukraine: Ukraine is associated with nazism | 0.667 | 0.500 | 1.000 |   1 |  1 |  1 |  0 | 30 |
|  7 | URW: Discrediting the West, Diplomacy: The West does not car... | 0.667 | 0.571 | 0.800 |   5 |  4 |  3 |  1 | 24 |
|  8 | URW: Discrediting the West, Diplomacy: West is tired of Ukraine | 0.667 | 1.000 | 0.500 |   2 |  1 |  0 |  1 | 30 |
|  9 | URW: Negative Consequences for the West: Sanctions imposed b... | 0.667 | 0.500 | 1.000 |   1 |  1 |  1 |  0 | 30 |
| 10 | URW: Praise of Russia: Praise of Russian President Vladimir ... | 0.667 | 0.500 | 1.000 |   2 |  2 |  2 |  0 | 28 |
| 11 | URW: Russia is the Victim: The West is russophobic | 0.667 | 1.000 | 0.500 |   2 |  1 |  0 |  1 | 30 |
| 12 | URW: Praise of Russia: Russia has international support from... | 0.600 | 0.600 | 0.600 |   5 |  3 |  2 |  2 | 25 |
| 13 | URW: Discrediting Ukraine: Ukraine is a puppet of the West | 0.571 | 0.400 | 1.000 |   4 |  4 |  6 |  0 | 22 |
| 14 | URW: Discrediting Ukraine: Discrediting Ukrainian military | 0.571 | 0.444 | 0.800 |   5 |  4 |  5 |  1 | 22 |
| 15 | URW: Praise of Russia: Russia is a guarantor of peace and pr... | 0.545 | 0.500 | 0.600 |   5 |  3 |  3 |  2 | 24 |



## Summary

This analysis provides a comprehensive view of Gemini 2.5 Flash performance across languages, focusing on F1 Samples as the primary evaluation metric. The results show language-specific performance patterns that can inform deployment strategies and model optimization efforts.

## Overall Summary of Impact

The inclusion of a validation step ("Narrative Validation Devset") versus its exclusion ("No Validation Devset") has a mixed but generally small impact on the model's performance, as measured by the F1 Samples score. There is no universally "better" approach; the effect varies by language and by whether narratives or subnarratives are being classified.

* Portuguese (PT), Bulgarian (BG), and Hindi (HI) generally see a slight performance increase in narrative classification without the validation step.
* Russian (RU) and English (EN) tend to perform slightly better on narrative classification with the validation step.
* The performance changes are mostly marginal, typically within a range of +/- 1.5%. The most significant change was observed in Hindi (HI) narratives, which saw a nearly 5% improvement in its F1 score without the validation step.
* The overall performance rankings of the languages remain consistent across both experiments, with PT and RU as the top performers and HI as the lowest performer.

### Performance Comparison: With vs. Without Validation

The following table directly compares the primary F1 Samples metric for each language from the two experiments. "With Validation" refers to the "Narrative Validation Devset" experiment, and "Without Validation" refers to the "No Validation Devset" experiment.

| Language | Metric | F1 Score (With Validation) | F1 Score (Without Validation) | Change | Better Performance |
|----------|--------|----------------------------|-------------------------------|--------|-------------------|
| PT | Narratives F1 Samples | 0.7335 | 0.7489 | +0.0154 | Without Validation |
| PT | Subnarratives F1 Samples | 0.4681 | 0.4737 | +0.0056 | Without Validation |
| RU | Narratives F1 Samples | 0.7080 | 0.6958 | -0.0122 | With Validation |
| RU | Subnarratives F1 Samples | 0.4786 | 0.4754 | -0.0032 | With Validation |
| BG | Narratives F1 Samples | 0.5721 | 0.5799 | +0.0078 | Without Validation |
| BG | Subnarratives F1 Samples | 0.4049 | 0.4104 | +0.0055 | Without Validation |
| EN | Narratives F1 Samples | 0.5241 | 0.5132 | -0.0109 | With Validation |
| EN | Subnarratives F1 Samples | 0.3675 | 0.3815 | +0.0140 | Without Validation |
| HI | Narratives F1 Samples | 0.4217 | 0.4715 | +0.0498 | Without Validation |
| HI | Subnarratives F1 Samples | 0.3082 | 0.2976 | -0.0106 | With Validation |

### Detailed Analysis

1. **Portuguese (PT)**: Performance improved slightly across both narratives (+0.0154) and subnarratives (+0.0056) when the validation step was removed. This suggests the validation step was not beneficial for this language.

2. **Russian (RU)**: This is the only language where including the validation step improved performance for both narratives and subnarratives. The scores dropped by 0.0122 and 0.0032, respectively, without it.

3. **Bulgarian (BG)**: Similar to Portuguese, Bulgarian saw a minor performance boost in both categories (+0.0078 for narratives, +0.0055 for subnarratives) without the validation step.

4. **English (EN)**: The results for English were mixed. The validation step was beneficial for classifying broader narratives (F1 score dropped by 0.0109 without it). However, for the more granular subnarratives, performance was better without the validation step (F1 score increased by 0.0140).

5. **Hindi (HI)**: Hindi also showed mixed results and the most dramatic change. Narrative classification improved significantly (F1 score increased by +0.0498) without the validation step. Conversely, subnarrative classification was slightly better with the validation step (F1 score dropped by 0.0106 without it).

In conclusion, the data indicates that the utility of a validation step is language-dependent and can even have opposing effects on classifying hierarchical labels (narratives vs. subnarratives) within the same language. For most languages in this test, removing the validation step either slightly improved or had a negligible effect on overall performance, with Russian being the notable exception where validation proved consistently helpful.
