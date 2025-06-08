# define main function
if __name__ == '__main__':
    # define constant
    NLTK_DATA_FOLDER_PRESENT_STATUS = False

    # importing python module:S01
    try:
        from pathlib import Path
        import shutil
        import sys
        import nltk
    except Exception as error:
        print(f'ERROR - [S01] - {str(error)}')

    ######################### Custom Function Section #########################
    # define "delete_file" function
    def delete_file(file_path: Path) -> bool: #type: ignore
        # check if file is present
        if (file_path.exists()):
            # remove the file
            file_path.unlink()
            # check if file deleted or not
            if (not (file_path.exists())):
                return True
            else:
                return False
        else:
            return False

    # define "delete_folder" function
    def delete_folder(folder_path: Path) -> bool: #type: ignore
        # check if folder is present
        if (folder_path.exists()):
            # remove the folder
            shutil.rmtree(folder_path)
            # check if folder deleted or not
            if (not (folder_path.exists())):
                return True
            else:
                return False
        else:
            return False
    ###########################################################################

    # define folder path:S02
    try:
        parent_folder_path = Path.cwd()
        nltk_data_folder_path = Path(parent_folder_path) / 'NLTK'
    except Exception as error:
        print(f'ERROR - [S02] - {str(error)}')

    # check if "NLTK" folder is present:S03
    try:
        if ((nltk_data_folder_path.exists()) and (nltk_data_folder_path.is_dir())):
            NLTK_DATA_FOLDER_PRESENT_STATUS = True
            print('INFO - "NLTK" Data Directory Already Present')
        else:
            # creating "NLTK" folder
            nltk_data_folder_path.mkdir(parents = True, exist_ok = True)
            # check if "NLTK" folder created or not
            if ((nltk_data_folder_path.exists()) and (nltk_data_folder_path.is_dir())):
                NLTK_DATA_FOLDER_PRESENT_STATUS = True
                print('SUCCESS - "NLTK" Data Directory Created')
            else:
                NLTK_DATA_FOLDER_PRESENT_STATUS = False
                print('ERROR - "NLTK" Data Directory Not Created, Hence Stop Execution')
                sys.exit(1)
    except Exception as error:
        print(f'ERROR - [S03] - {str(error)}')

    # configure "NLTK" download path:S04
    if (NLTK_DATA_FOLDER_PRESENT_STATUS):
        try:
            nltk.data.path.append(nltk_data_folder_path)
        except Exception as error:
            print(f'ERROR - [S04] - {str(error)}')

    ######################### For "stopwords" Data #########################
    if (NLTK_DATA_FOLDER_PRESENT_STATUS):
        print('\n' + '~' * 61)
        # define constant
        STOPWORDS_DATA_FOLDER_PRESENT_STATUS = False
        STOPWORDS_DATA_LOAD_STATUS = False

        # define "stopwords" folder path
        stopwords_nltk_data_folder_path = Path(nltk_data_folder_path) / 'corpora' / 'stopwords'

        # check if old "stopwords" folder is present:S05-A
        try:
            if ((stopwords_nltk_data_folder_path.exists()) and (stopwords_nltk_data_folder_path.is_dir())):
                # calling "delete_folder" function
                if (delete_folder(folder_path = stopwords_nltk_data_folder_path)):
                    print('INFO    - "stopwords" Old Folder Deleted')
                else:
                    print('ERROR   - "stopwords" Old Folder Not Deleted; Manual Intervention Is Required, Hence Stop Execution')
                    sys.exit(1)
        except Exception as error:
            print(f'ERROR - [S05-A] - {str(error)}')

        # downloading "stopwords" data from "NLTK":S05-B
        try:
            nltk.download('stopwords', download_dir = nltk_data_folder_path, quiet = True)
        except Exception as error:
            print(f'ERROR - [S05-B] - {str(error)}')

        # check if "stopword" folder path created:S05-C
        try:
            if ((stopwords_nltk_data_folder_path.exists()) and (stopwords_nltk_data_folder_path.is_dir())):
                STOPWORDS_DATA_FOLDER_PRESENT_STATUS = True
                print('SUCCESS - "stopwords" Downloaded Successfully')
            else:
                STOPWORDS_DATA_FOLDER_PRESENT_STATUS = False
                print('ERROR   - "stopwords" Not Downloaded Successfully, Hence Stop Execution')
                sys.exit(1)
        except Exception as error:
            print(f'ERROR - [S05-C] - {str(error)}')

        # import "nltk.corpus" module:S05-D
        if (STOPWORDS_DATA_FOLDER_PRESENT_STATUS):
            try:
                from nltk.corpus import stopwords
            except Exception as error:
                print(f'ERROR - [S05-D] - {str(error)}')

        # load "stopwords" data to check:S05-E
        if (STOPWORDS_DATA_FOLDER_PRESENT_STATUS):
            try:
                stop_words = stopwords.words('english')
                print('SUCCESS - "stopwords" Data Downloaded And Loaded Successfully')
                STOPWORDS_DATA_LOAD_STATUS = True
            except LookupError:
                STOPWORDS_DATA_LOAD_STATUS = False
                print('ERROR - [S05-E] - "stopwords" Data Not Found Or Corrupted, Hence Stop Execution')
                sys.exit(1)
            except Exception as error:
                STOPWORDS_DATA_LOAD_STATUS = False
                print(f'ERROR - [S05-E] - {str(error)}')

        # delete "stopwords.zip" file:S05-F
        if (STOPWORDS_DATA_LOAD_STATUS):
            try:
                # define "stopwords.zip" file path
                stopwords_data_zip_file_path = Path(nltk_data_folder_path) / 'corpora' / 'stopwords.zip'
                # calling "delete_file" function
                if (delete_file(file_path = stopwords_data_zip_file_path)):
                    print('SUCCESS - "stopwords.zip" File Deleted Successfully')
                else:
                    print('INFO    - "stopwords.zip" File Not Deleted, Hence Manual Intervention Is Required')
            except Exception as error:
                print(f'ERROR - [S05-F] - {str(error)}')
        print('~' * 61)
    ########################################################################

    ########################## For "wordnet" Data ##########################
    if (NLTK_DATA_FOLDER_PRESENT_STATUS):
        print('\n' + '~' * 63)
        # define constant
        WORDNET_DATA_FILE_PRESENT_STAUS = False

        # define "wordnet.zip" file path
        wordnet_nltk_data_zip_file_path = Path(nltk_data_folder_path) / 'corpora' / 'wordnet.zip'

        # check if old "wordnet.zip" file is present:S06-A
        try:
            if (wordnet_nltk_data_zip_file_path.exists()):
                # calling "delete_file" function
                if (delete_file(file_path = wordnet_nltk_data_zip_file_path)):
                    print('INFO    - "wordnet.zip" Old File Deleted')
                else:
                    print('ERROR   - "wordnet.zip" Old File Not Deleted; Manual Intervention Is Required, Hence Stop Execution')
                    sys.exit(1)
        except Exception as error:
            print(f'ERROR - [S06-A] - {str(error)}')

        # downloading "wordnet" data from "NLTK":S06-B
        try:
            nltk.download('wordnet', download_dir = nltk_data_folder_path, quiet = True)
        except Exception as error:
            print(f'ERROR - [S06-B] - {str(error)}')

        # check if "wordnet.zip" file created:S06-C
        try:
            if (wordnet_nltk_data_zip_file_path.exists()):
                WORDNET_DATA_FILE_PRESENT_STAUS = True
                print('SUCCESS - "wordnet.zip" Downloaded Successfully')
            else:
                WORDNET_DATA_FILE_PRESENT_STAUS = False
                print('ERROR   - "wordnet.zip" Not Downloaded Successfully, Hence Stop Execution')
                sys.exit(1)
        except Exception as error:
            print(f'ERROR - [S06-C] - {str(error)}')

        # import "nltk.corpus" module:S06-D
        if (WORDNET_DATA_FILE_PRESENT_STAUS):
            try:
                from nltk.corpus import wordnet
            except Exception as error:
                print(f'ERROR - [S06-D] - {str(error)}')

        # load "wordnet.zip" data to check:S06-E
        if (WORDNET_DATA_FILE_PRESENT_STAUS):
            try:
                synsets = wordnet.synsets('example')
                print('SUCCESS - "wordnet.zip" Data Downloaded And Loaded Successfully')
            except LookupError:
                print('ERROR - [S06-E] - "wordnet.zip" Data Not Found Or Corrupted, Hence Stop Execution')
                sys.exit(1)
            except Exception as error:
                print(f'ERROR - [S06-E] - {str(error)}')
                sys.exit(1)
        print('~' * 63)
    ########################################################################

    ########################### For "punkt" Data ###########################
    if (NLTK_DATA_FOLDER_PRESENT_STATUS):
        print('\n' + '~' * 60)
        # define constant
        PUNKT_DATA_FOLDER_PRESENT_STATUS = False
        PUNKT_DATA_LOAD_STATUS = False

        # define "punkt" folder path
        punkt_nltk_data_folder_path = Path(nltk_data_folder_path) / 'tokenizers' / 'punkt'

        # check if old "punkt" folder is present:S07-A
        try:
            if (punkt_nltk_data_folder_path.exists() and (punkt_nltk_data_folder_path.is_dir())):
                # calling "delete_folder" function
                if (delete_folder(folder_path = punkt_nltk_data_folder_path)):
                    print('INFO    - "punkt" Old File Deleted')
                else:
                    print('ERROR   - "punkt" Old File Not Deleted; Manual Intervention Is Required, Hence Stop Execution')
                    sys.exit(1)
        except Exception as error:
            print(f'ERROR - [S07-A] - {str(error)}')

        # downloading "punkt" data from "NLTK":S07-B
        try:
            nltk.download('punkt', download_dir = nltk_data_folder_path, quiet = True)
        except Exception as error:
            print(f'ERROR - [S07-B] - {str(error)}')

        # check if "punkt" folder path created:S07-C
        try:
            if ((punkt_nltk_data_folder_path.exists()) and (punkt_nltk_data_folder_path.is_dir())):
                PUNKT_DATA_FOLDER_PRESENT_STATUS = True
                print('SUCCESS - "punkt" Downloaded Successfully')
            else:
                PUNKT_DATA_FOLDER_PRESENT_STATUS = False
                print('ERROR   - "punkt" Not Downloaded Successfully, Hence Stop Execution')
                sys.exit(1)
        except Exception as error:
            print(f'ERROR - [S07-C] - {str(error)}')

        # import "nltk.tokenize" module:S07-D
        if (PUNKT_DATA_FOLDER_PRESENT_STATUS):
            try:
                from nltk.tokenize import sent_tokenize, word_tokenize
            except Exception as error:
                print(f'ERROR - [S07-D] - {str(error)}')

        # load "punkt" data to check:S07-E
        if (PUNKT_DATA_FOLDER_PRESENT_STATUS):
            try:
                test_text = "Hello! This is a test for punkt tokenizer. Let's see how it works."
                sentences = sent_tokenize(test_text)
                words = word_tokenize(test_text)
                print('SUCCESS - "punkt" Data Downloaded And Tokenized Successfully')
                PUNKT_DATA_LOAD_STATUS = True
            except LookupError:
                PUNKT_DATA_LOAD_STATUS = False
                print('ERROR - [S07-E] - "punkt" Data Not Found Or Corrupted, Hence Stop Execution')
                sys.exit(1)
            except Exception as error:
                PUNKT_DATA_LOAD_STATUS = False
                print(f'ERROR - [S07-E] - {str(error)}')

        # delete "punkt.zip" file:S07-F
        if (PUNKT_DATA_LOAD_STATUS):
            try:
                # define "punkt.zip" file path
                punkt_data_zip_file_path = Path(nltk_data_folder_path) / 'tokenizers' / 'punkt.zip'
                # calling "delete_file" function
                if (delete_file(file_path = punkt_data_zip_file_path)):
                    print('SUCCESS - "punkt.zip" File Deleted Successfully')
                else:
                    print('INFO    - "punkt.zip" File Not Deleted, Hence Manual Intervention Is Required')
            except Exception as error:
                print(f'ERROR - [S07-F] - {str(error)}')
    print('~' * 60)
    ########################################################################