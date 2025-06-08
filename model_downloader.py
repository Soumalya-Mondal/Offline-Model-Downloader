# define main function
if __name__ == '__main__':
    # importing python module:S01
    try:
        from pathlib import Path
        import os
        import stat
        import sys
        import shutil
        # from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, AutoModelForSequenceClassification, AutoModelForTokenClassification
    except Exception as error:
        print(f'ERROR - [S01] - {str(error)}')

    # taking input from user:S02
    try:
        pass
    except Exception as error:
        print(f'ERROR - [S01] - {str(error)}')