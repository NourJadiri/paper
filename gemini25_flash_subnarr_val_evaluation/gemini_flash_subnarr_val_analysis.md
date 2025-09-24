# Gemini 2.5 Flash Results Analysis

**Experiment**: Gemini 2.5 Flash - Subnarrative Validation Devset  
**Model**: Google Gemini 2.5 Flash  
**Languages Analyzed**: BG, EN, HI, PT, RU  
**Primary Metric**: F1 Samples  

This analysis summarizes the performance of Gemini 2.5 Flash across different languages for hierarchical text classification.


## Language Performance Comparison

| Language | Model | Files | Narratives F1 Samples | Subnarratives F1 Samples | Narratives Labels | Subnarratives Labels |
|----------|-------|-------|----------------------|--------------------------|-------------------|----------------------|
| RU | Google Gemini 2.5 Flash | 32 | 0.6693 | 0.5078 | 11 | 40 |
| PT | Google Gemini 2.5 Flash | 35 | 0.6904 | 0.4367 | 15 | 41 |
| BG | Google Gemini 2.5 Flash | 35 | 0.5521 | 0.4211 | 21 | 67 |
| EN | Google Gemini 2.5 Flash | 41 | 0.5319 | 0.4166 | 22 | 80 |
| HI | Google Gemini 2.5 Flash | 35 | 0.4354 | 0.2687 | 13 | 42 |



## Performance Insights

### Overall Performance Rankings

**Best Overall Performance**: RU (Combined F1 Samples: 1.1771)

**Lowest Overall Performance**: HI (Combined F1 Samples: 0.7041)

**Best Narratives Performance**: PT (F1 Samples: 0.6904)

**Best Subnarratives Performance**: RU (F1 Samples: 0.5078)

### Performance Statistics

**Narratives F1 Samples**:
- Average: 0.5758
- Range: 0.4354 - 0.6904
- Standard Deviation: 0.0939

**Subnarratives F1 Samples**:
- Average: 0.4102
- Range: 0.2687 - 0.5078
- Standard Deviation: 0.0780

### Narratives vs Subnarratives Performance Gap

- Average gap (Narratives - Subnarratives): 0.1657
- Languages with smallest gap: EN
- Languages with largest gap: PT




## Narratives Performance by Language (Top 10)

### BG (Google Gemini 2.5 Flash)

**Overall Performance**: F1 Samples: 0.5521 | F1 Macro: 0.3861 | F1 Micro: 0.5298 | Files: 35 | Labels: 21

| Rank | Label | F1 Score | Precision | Recall | Support | TP | FP | FN | TN |
|------|-------|----------|-----------|--------|---------|----|----|----|----|
|  1 | CC: Amplifying Climate Fears | 0.947 | 0.900 | 1.000 |   9 |  9 |  1 |  0 | 25 |
|  2 | URW: Discrediting Ukraine | 0.833 | 0.714 | 1.000 |   5 |  5 |  2 |  0 | 28 |
|  3 | URW: Praise of Russia | 0.800 | 0.667 | 1.000 |   2 |  2 |  1 |  0 | 32 |
|  4 | URW: Amplifying war-related fears | 0.769 | 0.625 | 1.000 |   5 |  5 |  3 |  0 | 27 |
|  5 | CC: Criticism of climate movement | 0.667 | 0.500 | 1.000 |   1 |  1 |  1 |  0 | 33 |
|  6 | CC: Hidden plots by secret schemes of powerful groups | 0.667 | 1.000 | 0.500 |   2 |  1 |  0 |  1 | 33 |
|  7 | CC: Downplaying climate change | 0.571 | 0.667 | 0.500 |   4 |  2 |  1 |  2 | 30 |
|  8 | URW: Russia is the Victim | 0.545 | 0.375 | 1.000 |   3 |  3 |  5 |  0 | 27 |
|  9 | CC: Criticism of climate policies | 0.500 | 0.500 | 0.500 |   2 |  1 |  1 |  1 | 32 |
| 10 | CC: Criticism of institutions and authorities | 0.500 | 0.400 | 0.667 |   3 |  2 |  3 |  1 | 29 |

### EN (Google Gemini 2.5 Flash)

**Overall Performance**: F1 Samples: 0.5319 | F1 Macro: 0.4776 | F1 Micro: 0.5597 | Files: 41 | Labels: 22

| Rank | Label | F1 Score | Precision | Recall | Support | TP | FP | FN | TN |
|------|-------|----------|-----------|--------|---------|----|----|----|----|
|  1 | CC: Questioning the measurements and science | 0.889 | 0.800 | 1.000 |   4 |  4 |  1 |  0 | 36 |
|  2 | URW: Blaming the war on others rather than the invader | 0.857 | 0.750 | 1.000 |   6 |  6 |  2 |  0 | 33 |
|  3 | URW: Discrediting the West, Diplomacy | 0.857 | 0.750 | 1.000 |   9 |  9 |  3 |  0 | 29 |
|  4 | URW: Discrediting Ukraine | 0.824 | 0.700 | 1.000 |   7 |  7 |  3 |  0 | 31 |
|  5 | URW: Distrust towards Media | 0.727 | 0.571 | 1.000 |   4 |  4 |  3 |  0 | 34 |
|  6 | CC: Climate change is beneficial | 0.667 | 0.500 | 1.000 |   1 |  1 |  1 |  0 | 39 |
|  7 | Other | 0.588 | 0.833 | 0.455 |  11 |  5 |  1 |  6 | 29 |
|  8 | CC: Green policies are geopolitical instruments | 0.571 | 0.500 | 0.667 |   3 |  2 |  2 |  1 | 36 |
|  9 | URW: Russia is the Victim | 0.571 | 0.400 | 1.000 |   2 |  2 |  3 |  0 | 36 |
| 10 | CC: Criticism of climate movement | 0.545 | 0.429 | 0.750 |   8 |  6 |  8 |  2 | 25 |

### HI (Google Gemini 2.5 Flash)

**Overall Performance**: F1 Samples: 0.4354 | F1 Macro: 0.3837 | F1 Micro: 0.4645 | Files: 35 | Labels: 13

| Rank | Label | F1 Score | Precision | Recall | Support | TP | FP | FN | TN |
|------|-------|----------|-----------|--------|---------|----|----|----|----|
|  1 | URW: Amplifying war-related fears | 0.824 | 0.778 | 0.875 |   8 |  7 |  2 |  1 | 25 |
|  2 | CC: Amplifying Climate Fears | 0.667 | 1.000 | 0.500 |   4 |  2 |  0 |  2 | 31 |
|  3 | URW: Praise of Russia | 0.571 | 0.750 | 0.462 |  13 |  6 |  2 |  7 | 20 |
|  4 | URW: Discrediting the West, Diplomacy | 0.522 | 0.375 | 0.857 |   7 |  6 | 10 |  1 | 18 |
|  5 | URW: Distrust towards Media | 0.500 | 0.500 | 0.500 |   2 |  1 |  1 |  1 | 32 |
|  6 | URW: Russia is the Victim | 0.435 | 0.357 | 0.556 |   9 |  5 |  9 |  4 | 17 |
|  7 | URW: Speculating war outcomes | 0.400 | 0.300 | 0.600 |   5 |  3 |  7 |  2 | 23 |
|  8 | URW: Blaming the war on others rather than the invader | 0.375 | 0.273 | 0.600 |   5 |  3 |  8 |  2 | 22 |
|  9 | URW: Discrediting Ukraine | 0.250 | 0.200 | 0.333 |   3 |  1 |  4 |  2 | 28 |
| 10 | Other | 0.222 | 0.143 | 0.500 |   2 |  1 |  6 |  1 | 27 |

### PT (Google Gemini 2.5 Flash)

**Overall Performance**: F1 Samples: 0.6904 | F1 Macro: 0.4909 | F1 Micro: 0.7287 | Files: 35 | Labels: 15

| Rank | Label | F1 Score | Precision | Recall | Support | TP | FP | FN | TN |
|------|-------|----------|-----------|--------|---------|----|----|----|----|
|  1 | URW: Amplifying war-related fears | 1.000 | 1.000 | 1.000 |   1 |  1 |  0 |  0 | 34 |
|  2 | URW: Discrediting Ukraine | 1.000 | 1.000 | 1.000 |   3 |  3 |  0 |  0 | 32 |
|  3 | URW: Praise of Russia | 0.889 | 0.800 | 1.000 |   4 |  4 |  1 |  0 | 30 |
|  4 | CC: Amplifying Climate Fears | 0.878 | 1.000 | 0.783 |  23 | 18 |  0 |  5 | 12 |
|  5 | URW: Discrediting the West, Diplomacy | 0.875 | 0.875 | 0.875 |   8 |  7 |  1 |  1 | 26 |
|  6 | URW: Russia is the Victim | 0.857 | 0.750 | 1.000 |   3 |  3 |  1 |  0 | 31 |
|  7 | CC: Criticism of institutions and authorities | 0.737 | 0.636 | 0.875 |   8 |  7 |  4 |  1 | 23 |
|  8 | URW: Negative Consequences for the West | 0.667 | 0.500 | 1.000 |   1 |  1 |  1 |  0 | 33 |
|  9 | CC: Criticism of climate policies | 0.462 | 0.750 | 0.333 |   9 |  3 |  1 |  6 | 25 |
| 10 | CC: Controversy about green technologies | 0.000 | 0.000 | 0.000 |   0 |  0 |  1 |  0 | 34 |

### RU (Google Gemini 2.5 Flash)

**Overall Performance**: F1 Samples: 0.6693 | F1 Macro: 0.5065 | F1 Micro: 0.6753 | Files: 32 | Labels: 11

| Rank | Label | F1 Score | Precision | Recall | Support | TP | FP | FN | TN |
|------|-------|----------|-----------|--------|---------|----|----|----|----|
|  1 | Other | 0.889 | 0.800 | 1.000 |   4 |  4 |  1 |  0 | 27 |
|  2 | URW: Discrediting Ukraine | 0.882 | 0.789 | 1.000 |  15 | 15 |  4 |  0 | 13 |
|  3 | URW: Praise of Russia | 0.857 | 0.923 | 0.800 |  15 | 12 |  1 |  3 | 16 |
|  4 | URW: Discrediting the West, Diplomacy | 0.710 | 0.688 | 0.733 |  15 | 11 |  5 |  4 | 12 |
|  5 | URW: Amplifying war-related fears | 0.667 | 0.500 | 1.000 |   2 |  2 |  2 |  0 | 28 |
|  6 | URW: Russia is the Victim | 0.500 | 0.400 | 0.667 |   3 |  2 |  3 |  1 | 26 |
|  7 | URW: Speculating war outcomes | 0.400 | 0.250 | 1.000 |   3 |  3 |  9 |  0 | 20 |
|  8 | URW: Negative Consequences for the West | 0.333 | 0.200 | 1.000 |   1 |  1 |  4 |  0 | 27 |
|  9 | URW: Blaming the war on others rather than the invader | 0.333 | 0.250 | 0.500 |   4 |  2 |  6 |  2 | 22 |
| 10 | URW: Distrust towards Media | 0.000 | 0.000 | 0.000 |   2 |  0 |  1 |  2 | 29 |




## Subnarratives Performance by Language (Top 10)

### BG (Google Gemini 2.5 Flash)

**Overall Performance**: F1 Samples: 0.4211 | F1 Macro: 0.2747 | F1 Micro: 0.4017 | Files: 35 | Labels: 67

| Rank | Label | F1 Score | Precision | Recall | Support | TP | FP | FN | TN |
|------|-------|----------|-----------|--------|---------|----|----|----|----|
|  1 | CC: Criticism of climate movement: Climate movement is alarmist | 1.000 | 1.000 | 1.000 |   1 |  1 |  0 |  0 | 34 |
|  2 | CC: Criticism of climate policies: Climate policies have neg... | 1.000 | 1.000 | 1.000 |   1 |  1 |  0 |  0 | 34 |
|  3 | CC: Downplaying climate change: Climate cycles are natural | 1.000 | 1.000 | 1.000 |   1 |  1 |  0 |  0 | 34 |
|  4 | CC: Hidden plots by secret schemes of powerful groups: Blami... | 1.000 | 1.000 | 1.000 |   1 |  1 |  0 |  0 | 34 |
|  5 | URW: Amplifying war-related fears: By continuing the war we ... | 1.000 | 1.000 | 1.000 |   1 |  1 |  0 |  0 | 34 |
|  6 | URW: Amplifying war-related fears: There is a real possibili... | 1.000 | 1.000 | 1.000 |   2 |  2 |  0 |  0 | 33 |
|  7 | URW: Praise of Russia: Praise of Russian President Vladimir ... | 1.000 | 1.000 | 1.000 |   1 |  1 |  0 |  0 | 34 |
|  8 | URW: Praise of Russia: Russia has international support from... | 1.000 | 1.000 | 1.000 |   1 |  1 |  0 |  0 | 34 |
|  9 | CC: Amplifying Climate Fears: Amplifying existing fears of g... | 0.947 | 0.900 | 1.000 |   9 |  9 |  1 |  0 | 25 |
| 10 | URW: Russia is the Victim: The West is russophobic | 0.857 | 0.750 | 1.000 |   3 |  3 |  1 |  0 | 31 |

### EN (Google Gemini 2.5 Flash)

**Overall Performance**: F1 Samples: 0.4166 | F1 Macro: 0.3062 | F1 Micro: 0.4038 | Files: 41 | Labels: 80

| Rank | Label | F1 Score | Precision | Recall | Support | TP | FP | FN | TN |
|------|-------|----------|-----------|--------|---------|----|----|----|----|
|  1 | CC: Climate change is beneficial: CO2 is beneficial | 1.000 | 1.000 | 1.000 |   1 |  1 |  0 |  0 | 40 |
|  2 | CC: Criticism of climate policies: Climate policies are only... | 1.000 | 1.000 | 1.000 |   1 |  1 |  0 |  0 | 40 |
|  3 | CC: Downplaying climate change: Human activities do not impa... | 1.000 | 1.000 | 1.000 |   2 |  2 |  0 |  0 | 39 |
|  4 | URW: Discrediting the West, Diplomacy: The EU is divided | 1.000 | 1.000 | 1.000 |   1 |  1 |  0 |  0 | 40 |
|  5 | URW: Praise of Russia: Russia is a guarantor of peace and pr... | 1.000 | 1.000 | 1.000 |   1 |  1 |  0 |  0 | 40 |
|  6 | URW: Blaming the war on others rather than the invader: The ... | 0.857 | 0.750 | 1.000 |   6 |  6 |  2 |  0 | 33 |
|  7 | CC: Hidden plots by secret schemes of powerful groups: Blami... | 0.800 | 0.667 | 1.000 |   2 |  2 |  1 |  0 | 38 |
|  8 | URW: Discrediting Ukraine: Ukraine is associated with nazism | 0.800 | 0.667 | 1.000 |   2 |  2 |  1 |  0 | 38 |
|  9 | CC: Criticism of institutions and authorities: Criticism of ... | 0.750 | 0.600 | 1.000 |   6 |  6 |  4 |  0 | 31 |
| 10 | URW: Discrediting the West, Diplomacy: Diplomacy does/will n... | 0.750 | 0.600 | 1.000 |   3 |  3 |  2 |  0 | 36 |

### HI (Google Gemini 2.5 Flash)

**Overall Performance**: F1 Samples: 0.2687 | F1 Macro: 0.2451 | F1 Micro: 0.2894 | Files: 35 | Labels: 42

| Rank | Label | F1 Score | Precision | Recall | Support | TP | FP | FN | TN |
|------|-------|----------|-----------|--------|---------|----|----|----|----|
|  1 | URW: Amplifying war-related fears: There is a real possibili... | 1.000 | 1.000 | 1.000 |   5 |  5 |  0 |  0 | 30 |
|  2 | URW: Distrust towards Media: Western media is an instrument ... | 1.000 | 1.000 | 1.000 |   1 |  1 |  0 |  0 | 34 |
|  3 | URW: Amplifying war-related fears: By continuing the war we ... | 0.750 | 0.600 | 1.000 |   3 |  3 |  2 |  0 | 30 |
|  4 | CC: Amplifying Climate Fears: Amplifying existing fears of g... | 0.667 | 1.000 | 0.500 |   4 |  2 |  0 |  2 | 31 |
|  5 | URW: Discrediting Ukraine: Ukraine is a puppet of the West | 0.667 | 0.500 | 1.000 |   1 |  1 |  1 |  0 | 33 |
|  6 | URW: Discrediting the West, Diplomacy: West is tired of Ukraine | 0.667 | 1.000 | 0.500 |   2 |  1 |  0 |  1 | 33 |
|  7 | URW: Praise of Russia: Praise of Russian President Vladimir ... | 0.667 | 0.500 | 1.000 |   1 |  1 |  1 |  0 | 33 |
|  8 | URW: Speculating war outcomes: Russian army is collapsing | 0.667 | 1.000 | 0.500 |   2 |  1 |  0 |  1 | 33 |
|  9 | URW: Blaming the war on others rather than the invader: The ... | 0.500 | 0.333 | 1.000 |   3 |  3 |  6 |  0 | 26 |
| 10 | URW: Russia is the Victim: Russia actions in Ukraine are onl... | 0.444 | 0.286 | 1.000 |   2 |  2 |  5 |  0 | 28 |

### PT (Google Gemini 2.5 Flash)

**Overall Performance**: F1 Samples: 0.4367 | F1 Macro: 0.3425 | F1 Micro: 0.4972 | Files: 35 | Labels: 41

| Rank | Label | F1 Score | Precision | Recall | Support | TP | FP | FN | TN |
|------|-------|----------|-----------|--------|---------|----|----|----|----|
|  1 | CC: Criticism of institutions and authorities: Criticism of ... | 1.000 | 1.000 | 1.000 |   1 |  1 |  0 |  0 | 34 |
|  2 | CC: Criticism of institutions and authorities: Criticism of ... | 1.000 | 1.000 | 1.000 |   1 |  1 |  0 |  0 | 34 |
|  3 | URW: Amplifying war-related fears: Other | 1.000 | 1.000 | 1.000 |   1 |  1 |  0 |  0 | 34 |
|  4 | URW: Discrediting Ukraine: Discrediting Ukrainian government... | 1.000 | 1.000 | 1.000 |   2 |  2 |  0 |  0 | 33 |
|  5 | URW: Praise of Russia: Russia has international support from... | 1.000 | 1.000 | 1.000 |   1 |  1 |  0 |  0 | 34 |
|  6 | URW: Russia is the Victim: The West is russophobic | 1.000 | 1.000 | 1.000 |   1 |  1 |  0 |  0 | 34 |
|  7 | URW: Russia is the Victim: Other | 0.857 | 0.750 | 1.000 |   3 |  3 |  1 |  0 | 31 |
|  8 | URW: Praise of Russia: Other | 0.800 | 0.667 | 1.000 |   2 |  2 |  1 |  0 | 32 |
|  9 | URW: Praise of Russia: Russia is a guarantor of peace and pr... | 0.800 | 0.667 | 1.000 |   2 |  2 |  1 |  0 | 32 |
| 10 | CC: Amplifying Climate Fears: Amplifying existing fears of g... | 0.710 | 0.647 | 0.786 |  14 | 11 |  6 |  3 | 15 |

### RU (Google Gemini 2.5 Flash)

**Overall Performance**: F1 Samples: 0.5078 | F1 Macro: 0.3342 | F1 Micro: 0.4454 | Files: 32 | Labels: 40

| Rank | Label | F1 Score | Precision | Recall | Support | TP | FP | FN | TN |
|------|-------|----------|-----------|--------|---------|----|----|----|----|
|  1 | URW: Discrediting Ukraine: Ukraine is a hub for criminal act... | 1.000 | 1.000 | 1.000 |   2 |  2 |  0 |  0 | 30 |
|  2 | URW: Negative Consequences for the West: Sanctions imposed b... | 1.000 | 1.000 | 1.000 |   1 |  1 |  0 |  0 | 31 |
|  3 | URW: Praise of Russia: Praise of Russian military might | 0.909 | 0.833 | 1.000 |   5 |  5 |  1 |  0 | 26 |
|  4 | Other | 0.889 | 0.800 | 1.000 |   4 |  4 |  1 |  0 | 27 |
|  5 | URW: Praise of Russia: Praise of Russian President Vladimir ... | 0.800 | 0.667 | 1.000 |   2 |  2 |  1 |  0 | 29 |
|  6 | URW: Discrediting Ukraine: Discrediting Ukrainian government... | 0.783 | 0.643 | 1.000 |   9 |  9 |  5 |  0 | 18 |
|  7 | URW: Amplifying war-related fears: NATO should/will directly... | 0.667 | 1.000 | 0.500 |   2 |  1 |  0 |  1 | 30 |
|  8 | URW: Discrediting Ukraine: Ukraine is a puppet of the West | 0.667 | 0.500 | 1.000 |   4 |  4 |  4 |  0 | 24 |
|  9 | URW: Discrediting Ukraine: Ukraine is associated with nazism | 0.667 | 0.500 | 1.000 |   1 |  1 |  1 |  0 | 30 |
| 10 | URW: Russia is the Victim: The West is russophobic | 0.667 | 1.000 | 0.500 |   2 |  1 |  0 |  1 | 30 |



## Summary

This analysis provides a comprehensive view of Gemini 2.5 Flash performance across languages, focusing on F1 Samples as the primary evaluation metric. The results show language-specific performance patterns that can inform deployment strategies and model optimization efforts.
