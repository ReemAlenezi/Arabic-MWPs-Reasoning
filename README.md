# Arabic MWPs Reasoning

This repository provides Arabic mathematical word problem (MWP) datasets and evaluation resources for reasoning with large language models (LLMs).

## 📚 Datasets

This repository includes three Arabic mathematical reasoning datasets:

- **AGSM8K**: Arabic translation of GSM8K with step-by-step reasoning  
- **Qudurat**: Academic aptitude test problems with detailed solutions  
- **ArabicMWPs**: Translated dataset from AddSub and MultiArith  

All datasets are available in the `datasets/` directory.

## 🧠 Prompts

The repository includes prompt templates used in experiments:

- English and Arabic prompts  
- Zero-shot Chain-of-Thought (CoT)  
- Manual Chain-of-Thought (CoT)  

Located in the `prompts/` directory.

## 📊 Results

Experimental results, including self-consistency evaluation, are available in:

`results/results.csv`

Self-consistency is implemented using sampling with majority voting across multiple reasoning paths.

## 🔁 Reproducibility

All datasets, prompts, and partial experimental results are publicly available to support reproducibility.


## 📄 Citation

If you use this work, please cite:

Alenezi, R., & Salman, A. (2025). *Arabic MWP Reasoning Datasets*.  
Available at: https://github.com/ReemAlenezi/Arabic-MWPs-Reasoning
