from collections import Counter
from concurrent.futures import ThreadPoolExecutor
import multiprocessing as mp

def get_most_common_answer(responses):
    return Counter(responses).most_common(1)[0][0]

def process_single_sample(args):
    question, prompt, model, parser = args
    chain = prompt | model | parser
    response = chain.invoke({"question": question})
    return response[0]["final_answer"], response[0]["steps"]

def get_predicted_answer(question, model, parser, prompt, num_samples=1):
    args = [(question, prompt, model, parser) for _ in range(num_samples)]
    with ThreadPoolExecutor(max_workers=mp.cpu_count()) as executor:
        results = list(executor.map(process_single_sample, args))

    answers = [r[0] for r in results]
    steps = [r[1] for r in results]
    return answers, steps
