# Gemini 2.5 Flash Results Analysis

**Experiment**: Gemini 2.5 Flash - No Validation Devset  
**Model**: Google Gemini 2.5 Flash  
**Languages Analyzed**: BG, EN, HI, PT, RU  
**Primary Metric**: F1 Samples  

This analysis summarizes the performance of Gemini 2.5 Flash across different languages for hierarchical text classification.


## Language Performance Comparison

| Language | Model | Files | Narratives F1 Samples | Subnarratives F1 Samples | Narratives Labels | Subnarratives Labels |
|----------|-------|-------|----------------------|--------------------------|-------------------|----------------------|
| PT | Google Gemini 2.5 Flash | 35 | 0.7489 | 0.4737 | 14 | 40 |
| RU | Google Gemini 2.5 Flash | 32 | 0.6958 | 0.4754 | 11 | 41 |
| BG | Google Gemini 2.5 Flash | 35 | 0.5799 | 0.4104 | 21 | 71 |
| EN | Google Gemini 2.5 Flash | 41 | 0.5132 | 0.3815 | 22 | 83 |
| HI | Google Gemini 2.5 Flash | 35 | 0.4715 | 0.2976 | 13 | 46 |



## Performance Insights

### Overall Performance Rankings

**Best Overall Performance**: PT (Combined F1 Samples: 1.2226)

**Lowest Overall Performance**: HI (Combined F1 Samples: 0.7691)

**Best Narratives Performance**: PT (F1 Samples: 0.7489)

**Best Subnarratives Performance**: RU (F1 Samples: 0.4754)

### Performance Statistics

**Narratives F1 Samples**:
- Average: 0.6019
- Range: 0.4715 - 0.7489
- Standard Deviation: 0.1056

**Subnarratives F1 Samples**:
- Average: 0.4077
- Range: 0.2976 - 0.4754
- Standard Deviation: 0.0660

### Narratives vs Subnarratives Performance Gap

- Average gap (Narratives - Subnarratives): 0.1942
- Languages with smallest gap: EN
- Languages with largest gap: PT




## Narratives Performance by Language (Top 15)

### BG (Google Gemini 2.5 Flash)

**Overall Performance**: F1 Samples: 0.5799 | F1 Macro: 0.4236 | F1 Micro: 0.5584 | Files: 35 | Labels: 21

| Rank | Label | F1 Score | Precision | Recall | Support | TP | FP | FN | TN |
|------|-------|----------|-----------|--------|---------|----|----|----|----|
|  1 | CC: Amplifying Climate Fears | 0.900 | 0.818 | 1.000 |   9 |  9 |  2 |  0 | 24 |
|  2 | URW: Discrediting Ukraine | 0.833 | 0.714 | 1.000 |   5 |  5 |  2 |  0 | 28 |
|  3 | CC: Criticism of climate policies | 0.800 | 0.667 | 1.000 |   2 |  2 |  1 |  0 | 32 |
|  4 | URW: Praise of Russia | 0.800 | 0.667 | 1.000 |   2 |  2 |  1 |  0 | 32 |
|  5 | URW: Amplifying war-related fears | 0.769 | 0.625 | 1.000 |   5 |  5 |  3 |  0 | 27 |
|  6 | CC: Criticism of climate movement | 0.667 | 0.500 | 1.000 |   1 |  1 |  1 |  0 | 33 |
|  7 | CC: Criticism of institutions and authorities | 0.667 | 0.500 | 1.000 |   3 |  3 |  3 |  0 | 29 |
|  8 | CC: Hidden plots by secret schemes of powerful groups | 0.667 | 1.000 | 0.500 |   2 |  1 |  0 |  1 | 33 |
|  9 | CC: Downplaying climate change | 0.571 | 0.667 | 0.500 |   4 |  2 |  1 |  2 | 30 |
| 10 | URW: Discrediting the West, Diplomacy | 0.526 | 0.357 | 1.000 |   5 |  5 |  9 |  0 | 21 |
| 11 | URW: Negative Consequences for the West | 0.500 | 0.400 | 0.667 |   3 |  2 |  3 |  1 | 29 |
| 12 | URW: Russia is the Victim | 0.500 | 0.333 | 1.000 |   3 |  3 |  6 |  0 | 26 |
| 13 | Other | 0.444 | 0.667 | 0.333 |   6 |  2 |  1 |  4 | 28 |
| 14 | URW: Blaming the war on others rather than the invader | 0.250 | 0.167 | 0.500 |   2 |  1 |  5 |  1 | 28 |
| 15 | CC: Controversy about green technologies | 0.000 | 0.000 | 0.000 |   0 |  0 |  2 |  0 | 33 |

### EN (Google Gemini 2.5 Flash)

**Overall Performance**: F1 Samples: 0.5132 | F1 Macro: 0.5398 | F1 Micro: 0.5714 | Files: 41 | Labels: 22

| Rank | Label | F1 Score | Precision | Recall | Support | TP | FP | FN | TN |
|------|-------|----------|-----------|--------|---------|----|----|----|----|
|  1 | URW: Overpraising the West | 1.000 | 1.000 | 1.000 |   1 |  1 |  0 |  0 | 40 |
|  2 | URW: Distrust towards Media | 0.889 | 0.800 | 1.000 |   4 |  4 |  1 |  0 | 36 |
|  3 | URW: Discrediting Ukraine | 0.875 | 0.778 | 1.000 |   7 |  7 |  2 |  0 | 32 |
|  4 | CC: Green policies are geopolitical instruments | 0.857 | 0.750 | 1.000 |   3 |  3 |  1 |  0 | 37 |
|  5 | CC: Questioning the measurements and science | 0.857 | 1.000 | 0.750 |   4 |  3 |  0 |  1 | 37 |
|  6 | URW: Blaming the war on others rather than the invader | 0.857 | 0.750 | 1.000 |   6 |  6 |  2 |  0 | 33 |
|  7 | URW: Discrediting the West, Diplomacy | 0.842 | 0.800 | 0.889 |   9 |  8 |  2 |  1 | 30 |
|  8 | CC: Climate change is beneficial | 0.667 | 0.500 | 1.000 |   1 |  1 |  1 |  0 | 39 |
|  9 | CC: Hidden plots by secret schemes of powerful groups | 0.667 | 1.000 | 0.500 |   4 |  2 |  0 |  2 | 37 |
| 10 | URW: Praise of Russia | 0.571 | 0.400 | 1.000 |   2 |  2 |  3 |  0 | 36 |
| 11 | CC: Criticism of climate movement | 0.571 | 0.462 | 0.750 |   8 |  6 |  7 |  2 | 26 |
| 12 | URW: Speculating war outcomes | 0.500 | 0.333 | 1.000 |   4 |  4 |  8 |  0 | 29 |
| 13 | CC: Criticism of institutions and authorities | 0.476 | 0.385 | 0.625 |   8 |  5 |  8 |  3 | 25 |
| 14 | Other | 0.471 | 0.667 | 0.364 |  11 |  4 |  2 |  7 | 28 |
| 15 | URW: Amplifying war-related fears | 0.462 | 0.300 | 1.000 |   3 |  3 |  7 |  0 | 31 |

### HI (Google Gemini 2.5 Flash)

**Overall Performance**: F1 Samples: 0.4715 | F1 Macro: 0.3971 | F1 Micro: 0.4841 | Files: 35 | Labels: 13

| Rank | Label | F1 Score | Precision | Recall | Support | TP | FP | FN | TN |
|------|-------|----------|-----------|--------|---------|----|----|----|----|
|  1 | CC: Amplifying Climate Fears | 0.857 | 1.000 | 0.750 |   4 |  3 |  0 |  1 | 31 |
|  2 | URW: Amplifying war-related fears | 0.778 | 0.700 | 0.875 |   8 |  7 |  3 |  1 | 24 |
|  3 | URW: Praise of Russia | 0.667 | 0.727 | 0.615 |  13 |  8 |  3 |  5 | 19 |
|  4 | URW: Discrediting the West, Diplomacy | 0.609 | 0.438 | 1.000 |   7 |  7 |  9 |  0 | 19 |
|  5 | URW: Distrust towards Media | 0.500 | 0.500 | 0.500 |   2 |  1 |  1 |  1 | 32 |
|  6 | URW: Russia is the Victim | 0.421 | 0.400 | 0.444 |   9 |  4 |  6 |  5 | 20 |
|  7 | URW: Blaming the war on others rather than the invader | 0.375 | 0.273 | 0.600 |   5 |  3 |  8 |  2 | 22 |
|  8 | Other | 0.286 | 0.200 | 0.500 |   2 |  1 |  4 |  1 | 29 |
|  9 | URW: Speculating war outcomes | 0.267 | 0.200 | 0.400 |   5 |  2 |  8 |  3 | 22 |
| 10 | URW: Discrediting Ukraine | 0.222 | 0.167 | 0.333 |   3 |  1 |  5 |  2 | 27 |
| 11 | URW: Negative Consequences for the West | 0.182 | 0.125 | 0.333 |   3 |  1 |  7 |  2 | 25 |
| 12 | URW: Hidden plots by secret schemes of powerful groups | 0.000 | 0.000 | 0.000 |   2 |  0 |  0 |  2 | 33 |
| 13 | URW: Overpraising the West | 0.000 | 0.000 | 0.000 |   2 |  0 |  0 |  2 | 33 |

### PT (Google Gemini 2.5 Flash)

**Overall Performance**: F1 Samples: 0.7489 | F1 Macro: 0.4756 | F1 Micro: 0.7460 | Files: 35 | Labels: 14

| Rank | Label | F1 Score | Precision | Recall | Support | TP | FP | FN | TN |
|------|-------|----------|-----------|--------|---------|----|----|----|----|
|  1 | CC: Amplifying Climate Fears | 0.878 | 1.000 | 0.783 |  23 | 18 |  0 |  5 | 12 |
|  2 | URW: Discrediting the West, Diplomacy | 0.875 | 0.875 | 0.875 |   8 |  7 |  1 |  1 | 26 |
|  3 | URW: Praise of Russia | 0.857 | 1.000 | 0.750 |   4 |  3 |  0 |  1 | 31 |
|  4 | URW: Discrediting Ukraine | 0.800 | 1.000 | 0.667 |   3 |  2 |  0 |  1 | 32 |
|  5 | CC: Criticism of climate policies | 0.714 | 1.000 | 0.556 |   9 |  5 |  0 |  4 | 26 |
|  6 | CC: Criticism of institutions and authorities | 0.700 | 0.583 | 0.875 |   8 |  7 |  5 |  1 | 22 |
|  7 | URW: Negative Consequences for the West | 0.667 | 0.500 | 1.000 |   1 |  1 |  1 |  0 | 33 |
|  8 | URW: Russia is the Victim | 0.667 | 0.500 | 1.000 |   3 |  3 |  3 |  0 | 29 |
|  9 | Other | 0.500 | 0.333 | 1.000 |   1 |  1 |  2 |  0 | 32 |
| 10 | CC: Controversy about green technologies | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 | 34 |
| 11 | CC: Green policies are geopolitical instruments | 0.000 | 0.000 | 0.000 |   0 |  0 |  2 |  0 | 33 |
| 12 | CC: Hidden plots by secret schemes of powerful groups | 0.000 | 0.000 | 0.000 |   1 |  0 |  0 |  1 | 34 |
| 13 | URW: Amplifying war-related fears | 0.000 | 0.000 | 0.000 |   1 |  0 |  0 |  1 | 34 |
| 14 | URW: Blaming the war on others rather than the invader | 0.000 | 0.000 | 0.000 |   0 |  0 |  2 |  0 | 33 |

### RU (Google Gemini 2.5 Flash)

**Overall Performance**: F1 Samples: 0.6958 | F1 Macro: 0.5213 | F1 Micro: 0.6879 | Files: 32 | Labels: 11

| Rank | Label | F1 Score | Precision | Recall | Support | TP | FP | FN | TN |
|------|-------|----------|-----------|--------|---------|----|----|----|----|
|  1 | Other | 1.000 | 1.000 | 1.000 |   4 |  4 |  0 |  0 | 28 |
|  2 | URW: Discrediting Ukraine | 0.857 | 0.750 | 1.000 |  15 | 15 |  5 |  0 | 12 |
|  3 | URW: Discrediting the West, Diplomacy | 0.824 | 0.737 | 0.933 |  15 | 14 |  5 |  1 | 12 |
|  4 | URW: Praise of Russia | 0.815 | 0.917 | 0.733 |  15 | 11 |  1 |  4 | 16 |
|  5 | URW: Amplifying war-related fears | 0.667 | 0.500 | 1.000 |   2 |  2 |  2 |  0 | 28 |
|  6 | URW: Speculating war outcomes | 0.462 | 0.300 | 1.000 |   3 |  3 |  7 |  0 | 22 |
|  7 | URW: Russia is the Victim | 0.444 | 0.333 | 0.667 |   3 |  2 |  4 |  1 | 25 |
|  8 | URW: Negative Consequences for the West | 0.333 | 0.200 | 1.000 |   1 |  1 |  4 |  0 | 27 |
|  9 | URW: Blaming the war on others rather than the invader | 0.333 | 0.250 | 0.500 |   4 |  2 |  6 |  2 | 22 |
| 10 | URW: Distrust towards Media | 0.000 | 0.000 | 0.000 |   2 |  0 |  1 |  2 | 29 |
| 11 | URW: Hidden plots by secret schemes of powerful groups | 0.000 | 0.000 | 0.000 |   1 |  0 |  3 |  1 | 28 |




## Subnarratives Performance by Language (Top 15)

### BG (Google Gemini 2.5 Flash)

**Overall Performance**: F1 Samples: 0.4104 | F1 Macro: 0.2819 | F1 Micro: 0.3824 | Files: 35 | Labels: 71

| Rank | Label | F1 Score | Precision | Recall | Support | TP | FP | FN | TN |
|------|-------|----------|-----------|--------|---------|----|----|----|----|
|  1 | CC: Criticism of climate movement: Ad hominem attacks on key... | 1.000 | 1.000 | 1.000 |   1 |  1 |  0 |  0 | 34 |
|  2 | CC: Criticism of climate policies: Climate policies are only... | 1.000 | 1.000 | 1.000 |   1 |  1 |  0 |  0 | 34 |
|  3 | CC: Downplaying climate change: Climate cycles are natural | 1.000 | 1.000 | 1.000 |   1 |  1 |  0 |  0 | 34 |
|  4 | CC: Hidden plots by secret schemes of powerful groups: Blami... | 1.000 | 1.000 | 1.000 |   1 |  1 |  0 |  0 | 34 |
|  5 | CC: Hidden plots by secret schemes of powerful groups: Other | 1.000 | 1.000 | 1.000 |   1 |  1 |  0 |  0 | 34 |
|  6 | URW: Amplifying war-related fears: There is a real possibili... | 1.000 | 1.000 | 1.000 |   2 |  2 |  0 |  0 | 33 |
|  7 | URW: Praise of Russia: Praise of Russian President Vladimir ... | 1.000 | 1.000 | 1.000 |   1 |  1 |  0 |  0 | 34 |
|  8 | CC: Amplifying Climate Fears: Amplifying existing fears of g... | 0.900 | 0.818 | 1.000 |   9 |  9 |  2 |  0 | 24 |
|  9 | CC: Criticism of climate movement: Climate movement is alarmist | 0.667 | 0.500 | 1.000 |   1 |  1 |  1 |  0 | 33 |
| 10 | CC: Criticism of climate movement: Other | 0.667 | 0.500 | 1.000 |   1 |  1 |  1 |  0 | 33 |
| 11 | CC: Criticism of climate policies: Climate policies have neg... | 0.667 | 0.500 | 1.000 |   1 |  1 |  1 |  0 | 33 |
| 12 | CC: Criticism of institutions and authorities: Criticism of ... | 0.667 | 0.500 | 1.000 |   2 |  2 |  2 |  0 | 31 |
| 13 | URW: Amplifying war-related fears: By continuing the war we ... | 0.667 | 0.500 | 1.000 |   1 |  1 |  1 |  0 | 33 |
| 14 | URW: Praise of Russia: Praise of Russian military might | 0.667 | 0.500 | 1.000 |   1 |  1 |  1 |  0 | 33 |
| 15 | URW: Praise of Russia: Russia has international support from... | 0.667 | 0.500 | 1.000 |   1 |  1 |  1 |  0 | 33 |

### EN (Google Gemini 2.5 Flash)

**Overall Performance**: F1 Samples: 0.3815 | F1 Macro: 0.3116 | F1 Micro: 0.4019 | Files: 41 | Labels: 83

| Rank | Label | F1 Score | Precision | Recall | Support | TP | FP | FN | TN |
|------|-------|----------|-----------|--------|---------|----|----|----|----|
|  1 | CC: Climate change is beneficial: CO2 is beneficial | 1.000 | 1.000 | 1.000 |   1 |  1 |  0 |  0 | 40 |
|  2 | CC: Downplaying climate change: Human activities do not impa... | 1.000 | 1.000 | 1.000 |   2 |  2 |  0 |  0 | 39 |
|  3 | URW: Discrediting the West, Diplomacy: The EU is divided | 1.000 | 1.000 | 1.000 |   1 |  1 |  0 |  0 | 40 |
|  4 | URW: Overpraising the West: The West belongs in the right si... | 1.000 | 1.000 | 1.000 |   1 |  1 |  0 |  0 | 40 |
|  5 | URW: Speculating war outcomes: Russian army is collapsing | 1.000 | 1.000 | 1.000 |   2 |  2 |  0 |  0 | 39 |
|  6 | URW: Blaming the war on others rather than the invader: The ... | 0.857 | 0.750 | 1.000 |   6 |  6 |  2 |  0 | 33 |
|  7 | URW: Discrediting the West, Diplomacy: Other | 0.857 | 0.750 | 1.000 |   6 |  6 |  2 |  0 | 33 |
|  8 | URW: Discrediting Ukraine: Ukraine is associated with nazism | 0.800 | 0.667 | 1.000 |   2 |  2 |  1 |  0 | 38 |
|  9 | CC: Criticism of institutions and authorities: Criticism of ... | 0.769 | 0.714 | 0.833 |   6 |  5 |  2 |  1 | 33 |
| 10 | URW: Distrust towards Media: Western media is an instrument ... | 0.750 | 0.750 | 0.750 |   4 |  3 |  1 |  1 | 36 |
| 11 | CC: Controversy about green technologies: Renewable energy i... | 0.667 | 0.500 | 1.000 |   1 |  1 |  1 |  0 | 39 |
| 12 | CC: Criticism of climate movement: Climate movement is alarmist | 0.667 | 0.500 | 1.000 |   4 |  4 |  4 |  0 | 33 |
| 13 | CC: Green policies are geopolitical instruments: Climate-rel... | 0.667 | 0.500 | 1.000 |   2 |  2 |  2 |  0 | 37 |
| 14 | CC: Hidden plots by secret schemes of powerful groups: Blami... | 0.667 | 1.000 | 0.500 |   2 |  1 |  0 |  1 | 39 |
| 15 | CC: Questioning the measurements and science: Scientific com... | 0.667 | 0.500 | 1.000 |   1 |  1 |  1 |  0 | 39 |

### HI (Google Gemini 2.5 Flash)

**Overall Performance**: F1 Samples: 0.2976 | F1 Macro: 0.2376 | F1 Micro: 0.3071 | Files: 35 | Labels: 46

| Rank | Label | F1 Score | Precision | Recall | Support | TP | FP | FN | TN |
|------|-------|----------|-----------|--------|---------|----|----|----|----|
|  1 | URW: Amplifying war-related fears: There is a real possibili... | 1.000 | 1.000 | 1.000 |   5 |  5 |  0 |  0 | 30 |
|  2 | URW: Distrust towards Media: Western media is an instrument ... | 1.000 | 1.000 | 1.000 |   1 |  1 |  0 |  0 | 34 |
|  3 | CC: Amplifying Climate Fears: Amplifying existing fears of g... | 0.857 | 1.000 | 0.750 |   4 |  3 |  0 |  1 | 31 |
|  4 | URW: Amplifying war-related fears: By continuing the war we ... | 0.750 | 0.600 | 1.000 |   3 |  3 |  2 |  0 | 30 |
|  5 | URW: Discrediting the West, Diplomacy: West is tired of Ukraine | 0.667 | 1.000 | 0.500 |   2 |  1 |  0 |  1 | 33 |
|  6 | URW: Amplifying war-related fears: Russia will also attack o... | 0.571 | 0.667 | 0.500 |   4 |  2 |  1 |  2 | 30 |
|  7 | URW: Discrediting Ukraine: Ukraine is a puppet of the West | 0.500 | 0.333 | 1.000 |   1 |  1 |  2 |  0 | 32 |
|  8 | URW: Discrediting the West, Diplomacy: The West is overreacting | 0.500 | 0.500 | 0.500 |   2 |  1 |  1 |  1 | 32 |
|  9 | URW: Speculating war outcomes: Ukrainian army is collapsing | 0.500 | 0.333 | 1.000 |   1 |  1 |  2 |  0 | 32 |
| 10 | URW: Praise of Russia: Russia has international support from... | 0.471 | 0.571 | 0.400 |  10 |  4 |  3 |  6 | 22 |
| 11 | URW: Praise of Russia: Praise of Russian military might | 0.462 | 0.300 | 1.000 |   3 |  3 |  7 |  0 | 25 |
| 12 | URW: Negative Consequences for the West: Sanctions imposed b... | 0.400 | 0.500 | 0.333 |   3 |  1 |  1 |  2 | 31 |
| 13 | URW: Russia is the Victim: Russia actions in Ukraine are onl... | 0.364 | 0.222 | 1.000 |   2 |  2 |  7 |  0 | 26 |
| 14 | URW: Discrediting Ukraine: Discrediting Ukrainian government... | 0.333 | 0.333 | 0.333 |   3 |  1 |  2 |  2 | 30 |
| 15 | URW: Blaming the war on others rather than the invader: The ... | 0.308 | 0.200 | 0.667 |   3 |  2 |  8 |  1 | 24 |

### PT (Google Gemini 2.5 Flash)

**Overall Performance**: F1 Samples: 0.4737 | F1 Macro: 0.3387 | F1 Micro: 0.4725 | Files: 35 | Labels: 40

| Rank | Label | F1 Score | Precision | Recall | Support | TP | FP | FN | TN |
|------|-------|----------|-----------|--------|---------|----|----|----|----|
|  1 | CC: Criticism of institutions and authorities: Criticism of ... | 1.000 | 1.000 | 1.000 |   1 |  1 |  0 |  0 | 34 |
|  2 | CC: Criticism of institutions and authorities: Other | 1.000 | 1.000 | 1.000 |   1 |  1 |  0 |  0 | 34 |
|  3 | URW: Discrediting Ukraine: Discrediting Ukrainian government... | 1.000 | 1.000 | 1.000 |   2 |  2 |  0 |  0 | 33 |
|  4 | URW: Discrediting Ukraine: Ukraine is a puppet of the West | 1.000 | 1.000 | 1.000 |   1 |  1 |  0 |  0 | 34 |
|  5 | URW: Praise of Russia: Other | 1.000 | 1.000 | 1.000 |   2 |  2 |  0 |  0 | 33 |
|  6 | URW: Russia is the Victim: Other | 0.750 | 0.600 | 1.000 |   3 |  3 |  2 |  0 | 30 |
|  7 | CC: Amplifying Climate Fears: Amplifying existing fears of g... | 0.688 | 0.611 | 0.786 |  14 | 11 |  7 |  3 | 14 |
|  8 | CC: Amplifying Climate Fears: Earth will be uninhabitable soon | 0.667 | 0.500 | 1.000 |   1 |  1 |  1 |  0 | 33 |
|  9 | CC: Criticism of climate policies: Climate policies are only... | 0.667 | 1.000 | 0.500 |   2 |  1 |  0 |  1 | 33 |
| 10 | CC: Criticism of institutions and authorities: Criticism of ... | 0.667 | 0.500 | 1.000 |   1 |  1 |  1 |  0 | 33 |
| 11 | URW: Discrediting the West, Diplomacy: Other | 0.667 | 0.800 | 0.571 |   7 |  4 |  1 |  3 | 27 |
| 12 | URW: Praise of Russia: Russia has international support from... | 0.667 | 0.500 | 1.000 |   1 |  1 |  1 |  0 | 33 |
| 13 | CC: Criticism of institutions and authorities: Criticism of ... | 0.545 | 0.429 | 0.750 |   4 |  3 |  4 |  1 | 27 |
| 14 | Other | 0.500 | 0.333 | 1.000 |   1 |  1 |  2 |  0 | 32 |
| 15 | URW: Praise of Russia: Russia is a guarantor of peace and pr... | 0.500 | 0.500 | 0.500 |   2 |  1 |  1 |  1 | 32 |

### RU (Google Gemini 2.5 Flash)

**Overall Performance**: F1 Samples: 0.4754 | F1 Macro: 0.3241 | F1 Micro: 0.4453 | Files: 32 | Labels: 41

| Rank | Label | F1 Score | Precision | Recall | Support | TP | FP | FN | TN |
|------|-------|----------|-----------|--------|---------|----|----|----|----|
|  1 | Other | 1.000 | 1.000 | 1.000 |   4 |  4 |  0 |  0 | 28 |
|  2 | URW: Negative Consequences for the West: Sanctions imposed b... | 1.000 | 1.000 | 1.000 |   1 |  1 |  0 |  0 | 31 |
|  3 | URW: Praise of Russia: Praise of Russian President Vladimir ... | 1.000 | 1.000 | 1.000 |   2 |  2 |  0 |  0 | 30 |
|  4 | URW: Praise of Russia: Praise of Russian military might | 0.909 | 0.833 | 1.000 |   5 |  5 |  1 |  0 | 26 |
|  5 | URW: Russia is the Victim: The West is russophobic | 0.800 | 0.667 | 1.000 |   2 |  2 |  1 |  0 | 29 |
|  6 | URW: Discrediting Ukraine: Discrediting Ukrainian government... | 0.783 | 0.643 | 1.000 |   9 |  9 |  5 |  0 | 18 |
|  7 | URW: Praise of Russia: Russia is a guarantor of peace and pr... | 0.750 | 1.000 | 0.600 |   5 |  3 |  0 |  2 | 27 |
|  8 | URW: Discrediting Ukraine: Ukraine is associated with nazism | 0.667 | 0.500 | 1.000 |   1 |  1 |  1 |  0 | 30 |
|  9 | URW: Discrediting the West, Diplomacy: The EU is divided | 0.667 | 0.500 | 1.000 |   2 |  2 |  2 |  0 | 28 |
| 10 | URW: Speculating war outcomes: Ukrainian army is collapsing | 0.667 | 0.500 | 1.000 |   2 |  2 |  2 |  0 | 28 |
| 11 | URW: Discrediting Ukraine: Ukraine is a puppet of the West | 0.571 | 0.400 | 1.000 |   4 |  4 |  6 |  0 | 22 |
| 12 | URW: Discrediting Ukraine: Discrediting Ukrainian military | 0.571 | 0.444 | 0.800 |   5 |  4 |  5 |  1 | 22 |
| 13 | URW: Discrediting the West, Diplomacy: The West does not car... | 0.571 | 0.444 | 0.800 |   5 |  4 |  5 |  1 | 22 |
| 14 | URW: Amplifying war-related fears: NATO should/will directly... | 0.500 | 0.500 | 0.500 |   2 |  1 |  1 |  1 | 29 |
| 15 | URW: Discrediting Ukraine: Ukraine is a hub for criminal act... | 0.500 | 0.500 | 0.500 |   2 |  1 |  1 |  1 | 29 |



## Summary

This analysis provides a comprehensive view of Gemini 2.5 Flash performance across languages, focusing on F1 Samples as the primary evaluation metric. The results show language-specific performance patterns that can inform deployment strategies and model optimization efforts.
