import json
import os
import json
import pandas as pd

def load_mc_data(dataset, context, type):
    background = []
    labels = []
    questions = []
    paragraphs = []
    question_id = []
    for i in range(len(dataset)):
        cont = ''
        cont_list = []
        for idx, para in enumerate(dataset[i]['paragraphs']):
            cont += context[para]
            cont_list.append(context[para])
            if type != 'test':
                if dataset[i]['relevant'] == para:
                    labels.append(idx)
        question_id.append(dataset[i]['id'])
        background.append(cont)
        paragraphs.append(cont_list)
        questions.append(dataset[i]['question'])

    if type != 'test':
        return background, labels, questions, paragraphs, question_id
    else:
        return background, questions, paragraphs, question_id

def load_qa_data(dataset, context, type):

    paragraphs = []
    paragraph_id = []
    questions = []
    answer_dict = []
    for i in range(len(dataset)):
        
        para_id = dataset[i]['relevant']
        paragraph = context[para_id]
        question = dataset[i]['question']
        if type != 'test':
            answer = dataset[i]['answer']
            answers = {"text": [answer["text"]], 
                       "answer_start": [answer["start"]]}
            answer_dict.append(answers)
        paragraphs.append(paragraph)
        paragraph_id.append(dataset[i]['id'])
        questions.append(question)
    if type != 'test':
        return paragraph_id, paragraphs, questions, answer_dict
    else:
        return paragraph_id, paragraphs, questions

def main():
    with open('./dataset/context.json') as f:
        context = json.load(f)
        
    for type in ['train', 'valid']:
        with open(f'./dataset/{type}.json') as f:
            dataset = json.load(f)
        if type != 'test':
            background, labels, questions, paragraphs, question_id = load_mc_data(dataset, context, type)
        else:
            background, questions, paragraphs, question_id = load_mc_data(dataset, context, type)

        df = pd.DataFrame({'id': question_id, 'context': background})
        para_df = pd.DataFrame(paragraphs, columns=['choice_0', 'choice_1', 'choice_2', 'choice_3'])
        df = pd.concat([df, para_df], axis=1)
        df['question'] = questions
        if type != 'test':
            df['label'] = labels
        df.to_json(f'./dataset/{type}_mc.json', orient='records', lines=False, indent=4, force_ascii=False)
        if type != 'test':
            paragraph_id, paragraphs, questions, answers = load_qa_data(dataset, context, type)
            df = pd.DataFrame({'id': paragraph_id, 'context': paragraphs, 'question': questions, 'answers': answers})
        else:
            pass
            # paragraph_id, paragraphs, questions = load_qa_data(dataset, context, type)
            # df = pd.DataFrame({'id': paragraph_id, 'context': paragraphs, 'question': questions})

        df.to_json(f'./dataset/{type}_qa.json', orient='records', lines=False, indent=4, force_ascii=False)

if __name__ == '__main__':
    main()
        

