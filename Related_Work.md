# GPTs are GPTs: An Early Look at the Labor Market Impact Potential of Large Language Models 
 
Eloundou et al. (2023) provide the first systematic assessment of LLM exposure across the U.S. labor market. Using a rubric-based framework combining human expert evaluation with GPT-4 self-assessment, they evaluated 1,016 occupations to determine which work tasks could be significantly affected by LLMs. 

**Key Contributions**

_Methodology_: The authors developed a two-tier exposure framework measuring (α) direct LLM exposure through current interfaces, and (β) LLM + complementary software exposure. Tasks were classified based on whether LLMs could reduce completion time by at least 50%. 

**Findings:**

- 80% of U.S. workers have ≥10% of tasks affected by LLMs; 19% have ≥50% affected 

- Higher-wage occupations show greater exposure, reversing historical automation patterns 

- Software multiplier effect: β exposure (47-56% of tasks) dramatically exceeds α exposure (15%) 

- Provides occupation-level exposure scores for all O*NET SOC codes (publicly available at https://github.com/openai/GPTs-are-GPTs) 

**Limitations and Gaps We Address**

1. While foundational, this work has key limitations our project addresses: 

2. Static Occupation Codes: Provides pre-computed scores for standardized occupations only. Our approach: Dynamic pipeline accepting arbitrary job descriptions, enabling assessment of emerging roles. 

3. Limited Skill Granularity: Evaluates tasks but doesn't extract underlying skills. Our approach: Explicit skill extraction to identify which competencies drive automation risk, enabling skill-level insights. 

4. U.S.-Centric: Confined to U.S. labor market using O*NET. Our approach: Global framework incorporating international taxonomies (ISCO, ESCO) and regional labor market trends. 

5. No Personalization: Occupation-level scores miss within-occupation variation. Our approach: Job-posting-level analysis capturing role-specific task compositions. 

**How We Build on This Work** 

We use Eloundou et al.'s exposure scores as validated ground truth features in our ML model, extending their work by: (1) processing natural language job descriptions rather than requiring occupation codes, (2) extracting and weighting specific skills, (3) incorporating additional contextual features (geography, industry, temporal trends), and (4) enabling global applicability through multi-taxonomy support. Our project transforms their academic insights into a practical, real-time assessment tool for job automation risk. 

**References**

Eloundou, T., Manning, S., Mishkin, P., & Rock, D. (2024). GPTs are GPTs: Labor market impact potential of LLMs. Science, 384(6703), 1306-1308.
Paper: https://arxiv.org/abs/2303.10130
Code: https://github.com/openai/GPTs-are-GPTs