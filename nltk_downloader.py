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
            print('INFO - [S03] - "NLTK" Data Directory Already Present')
        else:
            # creating "NLTK" folder
            nltk_data_folder_path.mkdir(parents = True, exist_ok = True)
            # check if "NLTK" folder created or not
            if ((nltk_data_folder_path.exists()) and (nltk_data_folder_path.is_dir())):
                NLTK_DATA_FOLDER_PRESENT_STATUS = True
                print('SUCCESS - [S03] - "NLTK" Data Directory Created')
            else:
                NLTK_DATA_FOLDER_PRESENT_STATUS = False
                print('ERROR - [S03] - "NLTK" Data Directory Not Created, Hence Stop Execution')
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
                    print('INFO - [S05-A] - "stopwords" Old Folder Deleted')
                else:
                    print('ERROR - [S05-A] - "stopwords" Old Folder Not Deleted; Manual Intervention Is Required, Hence Stop Execution')
                    sys.exit(1)
        except Exception as error:
            print(f'ERROR - [S05-A] - {str(error)}')

        # downloading "stopwords" data from "NLTK":S05-B
        try:
            nltk.download('stopwords', download_dir = nltk_data_folder_path)
        except Exception as error:
            print(f'ERROR - [S05-B] - {str(error)}')

        # check if "stopword" folder path created:S05-C
        try:
            if ((stopwords_nltk_data_folder_path.exists()) and (stopwords_nltk_data_folder_path.is_dir())):
                STOPWORDS_DATA_FOLDER_PRESENT_STATUS = True
                print('SUCCESS - [S05-C] - "stopwords" Downloaded Successfully')
            else:
                STOPWORDS_DATA_FOLDER_PRESENT_STATUS = False
                print('ERROR - [S05-C] - "stopwords" Not Downloaded Successfully, Hence Stop Execution')
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
                print('SUCCESS - [S05-E] - "stopwords" Data Downloaded And Loaded Successfully')
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
                    print('SUCCESS - [S05-F] - "stopwords.zip" File Deleted Successfully')
                else:
                    print('INFO - [S05-F] - "stopwords.zip" File Not Deleted, Hence Manual Intervention Is Required')
            except Exception as error:
                print(f'ERROR - [S05-F] - {str(error)}')
    ########################################################################