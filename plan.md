### **Proposed Paper Title:**

*An Agentic, Pipeline-Driven Approach to Zero-Shot Hierarchical Narrative Classification*

*(This title highlights your main contributions: the agentic framework and its more robust pipeline evolution, emphasizing the zero-shot aspect which is a key strength.)*

---

### **Academic Paper Writing Plan**

#### **1. Introduction**

*   **1.1. Motivation:** Start with the broader context. The challenge of identifying complex, nested narratives in online news, especially in high-stakes domains like geopolitical conflicts and climate change. Briefly touch upon the spread of disinformation.
*   **1.2. Problem Definition:** Introduce **SemEval-2025 Task 10, Subtask 2** as the concrete problem. Define it as a Hierarchical Multi-Label Classification (HMLC) task with a two-level taxonomy. State the key challenges presented by the task: extreme class imbalance, the need for hierarchical consistency, and multilingual complexities.
*   **1.3. Existing Approaches & Gaps:** Briefly summarize the traditional methods (like those mentioned in your SemEval paper: Binary Relevance, fine-tuning Transformers like XLM-RoBERTa). Point out their limitations in this specific context (e.g., data-hungry, struggle with zero-shot generalization, difficulty encoding complex reasoning). This sets the stage for your LLM-based approaches.
*   **1.4. Our Contributions:** State your contributions clearly and concisely.
    *   We introduce a **zero-shot agentic framework** that decomposes the HMLC problem into specialized, manageable binary classification tasks, achieving competitive performance without any task-specific fine-tuning.
    *   We propose a novel **configurable actor-critic pipeline** as an evolution of the agentic system, designed for enhanced traceability, modularity, and robustness by incorporating explicit validation steps and evidence extraction.
    *   We provide a thorough analysis of three distinct architectural paradigms for this task: a standard fine-tuning baseline, the agentic framework, and the traceable pipeline.
    *   We conduct an in-depth error analysis that highlights the challenges of class imbalance and semantic ambiguity in narrative detection.

#### **2. Task and Data Analysis**

*   **2.1. Task Formalization:** Reiterate that the task is to map a document to a set of `(narrative, sub-narrative)` pairs.
*   **2.2. Dataset Deep Dive:** This is where your Jupyter notebook analysis comes in.
    *   **Statistics:** Present key statistics (number of documents, labels, languages) from the SemEval dataset. Use Table 2 from your paper as a starting point.
    *   **Class Imbalance:** Show the long-tail distribution of narratives and sub-narratives. Use the bar charts (like Figures 2-5 from your paper) to visually demonstrate how few examples exist for many classes. This is crucial for justifying your zero-shot approach and discussing the baseline's failures.
    *   **Label Correlation:** (Optional but strong) Create a co-occurrence heatmap to show which labels frequently appear together. This highlights the "multi-label" nature of the problem.
*   **2.3. Evaluation Metrics:** Clearly define the official metrics: **Sample-Averaged F1** (the primary ranking metric) and **Macro F1**. Explain what each metric emphasizes (Sample F1 focuses on per-instance correctness, while Macro F1 gives equal weight to rare classes).

#### **3. System Architectures**

This is the core of your paper. Describe each system in its own subsection, building a logical progression from simple to complex.

*   **3.1. Architecture 0: Fine-Tuning Baseline**
    *   **Model:** Fine-tuned XLM-RoBERTa.
    *   **Method:** Frame the task as a standard multi-label problem where the model outputs a vector of logits, one for each sub-narrative, followed by a sigmoid activation.
    *   **Challenges & Mitigation Strategies:** Explicitly discuss the problems you faced.
        *   **Class Imbalance:** Mention that a standard `BCEWithLogitsLoss` fails. Discuss the mitigation strategy you considered or implemented, such as using `pos_weight` to give more importance to positive samples for rare classes.
        *   **Data Scarcity:** Acknowledge that with few examples, the model is prone to overfitting and struggles to learn robust representations for tail-end classes.

*   **3.2. Architecture 1: Zero-Shot Agentic Framework**
    *   This section will be a refined version of your SemEval paper's description.
    *   **Core Idea:** Decomposing the complex multi-label task into a set of parallel binary decisions handled by specialized LLM agents.
    *   **Components:** Describe the roles of the **Manager Agent**, **Narrative Agents**, and **Sub-narrative Agents**. Use the diagram (Figure 1 from your paper) to illustrate the information flow.
    *   **Workflow:** Explain the two-step process: (1) The Manager queries Narrative Agents to get coarse-level predictions. (2) For each predicted narrative, a new group of Sub-narrative Agents is spawned for fine-grained classification.
    *   **Implementation:** Mention the use of AutoGen for orchestration and GPT models as the agent backbone. Highlight the critical role of prompt engineering (e.g., the instruction to be strict and answer '0' if unsure).

*   **3.3. Architecture 2: Traceable Actor-Critic Pipeline**
    *   **Motivation:** Frame this as the next logical step, addressing the limitations of Architecture 1 (e.g., lack of traceability, potential for unverified outputs).
    *   **Core Idea:** A modular, multi-stage pipeline where "Actor" nodes generate claims and "Critic" nodes validate them.
    *   **Pipeline Stages:** Detail the flow:
        1.  **(Optional) Pre-processing:** Text cleaning.
        2.  **Topic Classification:** A simple classifier determines the high-level topic (CC/URW/Other).
        3.  **Narrative Actor:** An LLM generates a structured JSON containing a list of potential `(narrative, evidence_quote, reasoning)`.
        4.  **Narrative Critic:** A separate, stricter LLM validates each claim from the Actor. It checks if the evidence actually supports the narrative. Invalid claims are discarded or sent back for a retry.
        5.  **Sub-narrative Actor & Critic:** A batched process for all validated narratives.
    *   **Key Advantages:** Emphasize **Traceability** (outputs are grounded in evidence from the text), **Modularity** (YAML config allows swapping models for each node), and **Reliability** (the Critic step actively reduces hallucinations).

#### **4. Experiments and Results**

*   **4.1. Experimental Setup:** Detail the models used for each architecture (e.g., `xlm-roberta-base`, `gpt-4o-mini`), libraries (Hugging Face Transformers, AutoGen), and setup (e.g., zero-shot prompting vs. fine-tuning).
*   **4.2. Main Results:**
    *   Present a central table comparing the performance of **Architecture 0 (Baseline)**, **Architecture 1 (Agentic)**, and **Architecture 2 (Pipeline)** on the English test set using Sample F1 and Macro F1. This will be your key results table.
    *   Include the official baseline and your final rank from the competition for context.
*   **4.3. Error Analysis:**
    *   Use the confusion matrices from your SemEval paper (Table 7) to discuss which narratives were frequently confused (e.g., "Criticism of climate policies" vs. "Criticism of institutions and authorities").
    *   Discuss the performance on rare classes, highlighting the "zero True Positives" issue mentioned in your paper. Explain *why* the agentic approach might still perform better than the fine-tuned baseline on these.
*   **4.4. Ablation Study / Negative Results:** This is the perfect place to discuss your `NarrativesClassifier` model.
    *   **Title:** "Analysis of an Embedding-Similarity Approach".
    *   **Method:** Describe the architecture: a bi-encoder that computes cosine similarity between a text embedding and pre-computed label embeddings. Mention you used `BCEWithLogitsLoss` with `pos_weights`.
    *   **Results:** State that its performance was significantly lower than the other methods.
    *   **Hypothesis:** Speculate on why it failed. For example: "The semantic descriptions of some sub-narratives are too similar, leading to non-discriminative label embeddings. Simple cosine similarity may be insufficient to capture the nuanced conditions under which a narrative is present."

#### **5. Discussion**

*   **5.1. Comparison of Architectures:** Synthesize the results. Why did the agentic/pipeline models outperform the fine-tuning baseline? (Answer: Leveraging the vast world knowledge and reasoning of LLMs is more effective than fine-tuning on a small, imbalanced dataset). What are the trade-offs between Architecture 1 and 2? (Answer: Speed/simplicity vs. traceability/reliability).
*   **5.2. Limitations:** Be critical of your own work.
    *   **Latency & Cost:** The LLM-based approaches are slow and expensive due to API calls.
    *   **Prompt Sensitivity:** Performance can be sensitive to the exact wording of the prompts.
    *   **Implicit Narratives:** The binary decision approach struggles with narratives that require "reading between the lines" or deep cultural context.
*   **5.3. Future Directions:** Propose clear next steps based on your findings.
    *   **Hybrid Models:** Propose combining the architectures. Use a fast, fine-tuned model (like your `NarrativesClassifier` or the baseline) as a **candidate retriever** to identify a small set of possible labels, then use a powerful **LLM-based re-ranker/critic** (from Arch 2) to make the final decision. This balances speed and accuracy.
    *   **Improving the Embedding Model:** Suggest ways to fix the `NarrativesClassifier`. For instance, instead of static label embeddings, use the LLM to generate richer, context-dependent label definitions.
    *   **Efficiency:** Explore model distillation, local open-source LLMs (Llama3, Mistral), or caching strategies to mitigate latency and cost.

#### **6. Conclusion**

*   Briefly summarize the problem, your proposed agentic and pipeline solutions, and your key findings. Conclude that for complex reasoning tasks like hierarchical narrative detection with limited data, decomposing the problem for large language models offers a more effective and adaptable paradigm than traditional fine-tuning.