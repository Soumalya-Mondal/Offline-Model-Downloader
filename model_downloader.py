# define main function
if __name__ == '__main__':
    # importing python module:S01
    try:
        import sys
        from pathlib import Path
        import os
        import stat
        import shutil
        # from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, AutoModelForSequenceClassification, AutoModelForTokenClassification
    except Exception as error:
        print(f'ERROR - [S01] - {str(error)}')

    # taking "model_classification" input from user:S02
    try:
        model_classification_user_input = str(input('[INFO]  - (1) - Grammar Correction\n[INFO]  - (2) - Text Simplification\n[INFO]  - (3) - Toxic Content Detection\n[INFO]  - (4) - Sentiment Analysis\n[INFO]  - (5) - Named Entity Recognition\n[INFO]  - (6) - Zero-Shot Classification\n[INFO]  - (7) - Summarization\n[INFO]  - (8) - Paraphrasing\n\n[INPUT] - Choose Any Option (e.g., 1, 2, 3): ')).strip()
        # check user input
        if (str(model_classification_user_input) == ''):
            print('\nERROR   - You Choose Nothing, Hence Stop Execution')
            sys.exit(1)
    except Exception as error:
        print(f'ERROR - [S02] - {str(error)}')

    # define available model based on classification:S03
    try:
        available_models_list = {
            "1": {
                "task": "Grammar Correction",
                "models": {
                    "prithivida/grammar_error_correcter_v1": "seq2seq",
                    "vennify/t5-base-grammar-correction": "seq2seq",
                    "pszemraj/flan-t5-base-grammar-synthesis": "seq2seq"
                }
            },
            "2": {
                "task": "Text Simplification",
                "models": {
                    "t5-base": "seq2seq",
                    "mrm8488/t5-base-finetuned-summarize-news": "seq2seq"
                }
            },
            "3": {
                "task": "Toxic Content Detection",
                "models": {
                    "unitary/toxic-bert": "sequence_classification",
                    "mrm8488/bert-tiny-finetuned-toxic-pytorch": "sequence_classification"
                }
            },
            "4": {
                "task": "Sentiment Analysis",
                "models": {
                    "distilbert-base-uncased-finetuned-sst-2-english": "sequence_classification",
                    "nlptown/bert-base-multilingual-uncased-sentiment": "sequence_classification"
                }
            },
            "5": {
                "task": "Named Entity Recognition",
                "models": {
                    "dbmdz/bert-large-cased-finetuned-conll03-english": "token_classification",
                    "dslim/bert-base-NER": "token_classification",
                    "xlm-roberta-large-finetuned-conll03-english": "token_classification"
                }
            },
            "6": {
                "task": "Zero-Shot Classification",
                "models": {
                    "facebook/bart-large-mnli": "sequence_classification"
                }
            },
            "7": {
                "task": "Summarization",
                "models": {
                    "google/pegasus-xsum": "seq2seq",
                    "facebook/bart-large-cnn": "seq2seq",
                    "sshleifer/distilbart-cnn-12-6": "seq2seq"
                }
            },
            "8": {
                "task": "Paraphrasing",
                "models": {
                    "ramsrigouthamg/t5_paraphraser": "seq2seq",
                    "Vamsi/T5_Paraphrase_Paws": "seq2seq"
                }
            }
        }
    except Exception as error:
        print(f'ERROR - [S03] - {str(error)}')

    # printing available model as per user classification input:S04
    try:
        # check if user option present in available classification list
        if model_classification_user_input in available_models_list:
            # fetching classification details
            classification_details = available_models_list[model_classification_user_input]
            # fetching classification name
            classification_name = classification_details['task']
            # fetching available model for specific classification
            selected_available_models = classification_details['models']
            # sort available models alphabetically
            sorted_selected_available_models = sorted(selected_available_models.keys())
            # define empty available model map dict
            available_model_map = {}
            # printing classification banner
            print(f"\n{'~' * 15} You choose {classification_name} Classification {'~' * 15}")
            # loop thorugh all the models with label
            for idx, model_name in enumerate(sorted_selected_available_models):
                available_model_map[chr(65 + idx)] = model_name
                print(f"[INFO]  - ({chr(65 + idx)}) - {model_name}")
            # taking model name input from user
            model_choice_user_input = input("\n[INPUT] - Choose A Model To Download (e.g., A, B, C): ").strip().upper()
    except Exception as error:
        print(f'ERROR - [S04] - {str(error)}')