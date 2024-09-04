#from transformers import BartForConditionalGeneration, BartTokenizer, pipeline
import torch

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

'''def summarize(rawtext: list, hn: list):
    model_name = "facebook/bart-large-cnn"
    tokenizer = BartTokenizer.from_pretrained(model_name, clean_up_tokenization_spaces=True)
    model = BartForConditionalGeneration.from_pretrained(model_name)
    summarize_pipe = pipeline('summarization', model=model, tokenizer=tokenizer, device=device)

    for i in range(len(rawtext)):
        prompt = rawtext[i]

        encoded_input = tokenizer(prompt, truncation=True, max_length=1024)
        decoded_input = tokenizer.decode(encoded_input["input_ids"], skip_special_tokens=True)

        summary = summarize_pipe(decoded_input, max_length=30)[0]['summary_text']
        hn[i]['summary']=summary

    return hn'''

def compilation(summaries: list, hn: list):
    for i in range(len(summaries)):
        hn[i]['summary']=summaries[i]

    return hn
