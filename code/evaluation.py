from bert_score import score as bert_score

def calculate_bertscore(references, candidates, lang="Ar"):
    P, R, F1 = bert_score(
        candidates, references,
        lang=lang,
        rescale_with_baseline=True
    )
    return P.mean().item(), R.mean().item(), F1.mean().item()
