import numpy as np
import json
import pandas as pd
import argparse
import os

def load_qa_data(dataset, choice_data, context_data):

    paragraphs = []
    paragraph_id = []
    questions = []

    for i in range(len(dataset)):
        choice = choice_data[i]
        context_idx = dataset[i]["paragraphs"][choice]
        paragraph = context_data[context_idx]
        # paragraph = dataset[i][f'choice_{choice}']
        question = dataset[i]['question']
        paragraphs.append(paragraph)
        paragraph_id.append(dataset[i]['id'])
        questions.append(question)

    return paragraph_id, paragraphs, questions

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--context_file", type=str, required=True)
    parser.add_argument("--test_file", type=str, required=True)
    parser.add_argument("--choice_file", type=str, required=True)
    parser.add_argument("--folder_path", type=str, required=True)
    args = parser.parse_args()

    choice_file = os.path.join(args.folder_path, args.choice_file)
    output_file = os.path.join(args.folder_path, 'test_qa.json')

    with open(args.test_file) as f:
        dataset = json.load(f)
    with open(args.context_file) as f:
        context_data = json.load(f)
    choice_data = np.load(choice_file)
    paragraph_id, paragraphs, questions = load_qa_data(dataset, choice_data, context_data)
    df = pd.DataFrame({'id': paragraph_id, 'context': paragraphs, 'question': questions})
    df.to_json(output_file, orient='records', lines=False, indent=4, force_ascii=False)

if __name__ == "__main__":
    main()