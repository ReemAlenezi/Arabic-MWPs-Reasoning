# Qudurat Dataset

Qudurat is an Arabic mathematical word problem dataset introduced in this work to evaluate the ability of large language models (LLMs) to understand and solve reasoning-based mathematical questions. The dataset is derived from the Academic Aptitude Test at Kuwait University, which is used for university admissions.

## Description
- Language: Arabic  
- Domain: Mathematical word problems  
- Size: 140 questions  
- Difficulty: Medium (high school level)  

## Construction
The dataset consists of 140 MWPs collected from previous Academic Aptitude Tests at Kuwait University. Many questions include detailed solution steps. For questions that originally contained only final answers, a mathematics specialist was assigned to provide complete step-by-step solutions.

## Format
Each example includes:
- Question  
- Reasoning steps  
- Final answer  

The dataset is provided in JSONL format.

## Problem Characteristics
- Number of reasoning steps: ranges from 1 to 8  
- Operations involved:  
  - Addition  
  - Subtraction  
  - Multiplication  
  - Division  

## Purpose
Qudurat is designed to evaluate the reasoning capabilities of LLMs on Arabic MWPs and to support students in preparing for aptitude tests by providing reliable problem-solving examples with detailed solutions.

## Notes
This dataset addresses the lack of Arabic resources for mathematical word problems and aims to support both research and education.

## Citation

If you use this dataset, please cite:

Alenezi, R., & Salman, A. (2025). *Qudurat Dataset*.  
Available at: https://github.com/ReemAlenezi/Arabic-MWPs-Reasoning
