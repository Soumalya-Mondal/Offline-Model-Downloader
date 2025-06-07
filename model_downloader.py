# define main function
if __name__ == '__main__':
    # define constant
    MODELS_FOLDER_PRESENT_STATUS = False

    # importing python module:S01
    try:
        from pathlib import Path
        import sys
        import shutil
        # from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
    except Exception as error:
        print(f'ERROR - [S01] - {str(error)}')

    ######################### For User Define Function #########################
    # define "delete_folder" function
    def delete_folder(folder_path: Path) -> bool: #type: ignore
        # check if folder is present
        if ((folder_path.exists()) and (folder_path.is_dir())):
            # remove the folder
            shutil.rmtree(folder_path)
            # check if folder is deleted or not
            if (not (folder_path.exists())):
                return True
            else:
                return False
    ############################################################################

    # define folder path:S02
    try:
        user_folder_path = Path.home()
        huggingface_hub_folder_path = Path(user_folder_path) / '.cache' / 'huggingface' / 'hub'
        huggingface_locks_folder_path = Path(huggingface_hub_folder_path) / '.locks'
        parent_folder_path = Path.cwd()
        models_folder_path = Path(parent_folder_path) / 'Models'
    except Exception as error:
        print(f'ERROR - [S02] - {str(error)}')

    # check if "Models" folder is present:S03
    try:
        if ((models_folder_path.exists()) and (models_folder_path.is_dir())):
            MODELS_FOLDER_PRESENT_STATUS = True
            print('INFO    - "Models" Already Present')
        else:
            # creating "Models" folder
            models_folder_path.mkdir()
            # check if "Models" folder created or not
            if ((models_folder_path.exists()) and (models_folder_path.is_dir())):
                MODELS_FOLDER_PRESENT_STATUS = True
                print('SUCCESS - "Models" Folder Created Successfully')
            else:
                MODELS_FOLDER_PRESENT_STATUS = False
                print('ERROR   - "Models" Folder Not Create, Hence Stop Execution')
                sys.exit(1)
    except Exception as error:
        print(f'ERROR - [S03] - {str(error)}')

    # define model specific folder path:S04
    if (MODELS_FOLDER_PRESENT_STATUS):
        try:
            # define model name
            model_name = 'prithivida/grammar_error_correcter_v1'
            # define "model_specific" folder path
            model_specific_folder_path = Path(models_folder_path) / f"{model_name.split('/')[0]}--{model_name.split('/')[1].replace('-', '_')}"
            # define "model_cache_specific" folder path
            model_cache_specific_folder_path = Path(huggingface_hub_folder_path) / f"models--{model_name.split('/')[0]}--{model_name.split('/')[1].replace('-', '_')}"
            # define "model_locks_specific" folder path
            model_locks_specific_folder_path = Path(huggingface_locks_folder_path) / f"models--{model_name.split('/')[0]}--{model_name.split('/')[1].replace('-', '_')}"
        except Exception as error:
            print(f'ERROR - [S04] - {str(error)}')

    # delete old folder:S05
    if (MODELS_FOLDER_PRESENT_STATUS):
        try:
            # delete "model_specific" folder
            if (delete_folder(folder_path = model_specific_folder_path)):
                print(f'SUCCESS - "{Path(*model_specific_folder_path.parts[-2:])}" Old Folder Deleted Successfully')
            else:
                print(f'INFO    - "{Path(*model_specific_folder_path.parts[-2:])}" Old Folder Not Deleted; Manual Intervention Required, Hence Stop Execution')
                sys.exit(1)
            # delete "model_locks_specific" folder
            if (delete_folder(folder_path = model_locks_specific_folder_path)):
                print(f'SUCCESS - "{Path(*model_locks_specific_folder_path.parts[-2:])}" Old Folder Deleted Successfullt')
            else:
                print(f'INFO    - "{Path(*model_locks_specific_folder_path.parts[-2:])}" Old Folder Not Deleted; Manual Intervention Required, Hence Stop Execution')
                sys.exit(1)
            # delete "model_cache_specific" folder
            if (delete_folder(folder_path = model_cache_specific_folder_path)):
                print(f'SUCCESS - "{Path(*model_cache_specific_folder_path.parts[-2:])}" Old Folder Deleted Successfully')
            else:
                print(f'INFO    - "{Path(*model_cache_specific_folder_path.parts[-2:])}" Old Folder Not Deleted; Manual Intervention Required, Hence Stop Execution')
                sys.exit(1)
        except Exception as error:
            print(f'ERROR - [S04] - {str(error)}')

    # # initialize "Autotokenizer" for model download:S05
    # if (MODELS_FOLDER_PRESENT_STATUS):
    #     try:
    #         tokenizer = AutoTokenizer.from_pretrained(model_name)
    #         tokenizer.save_pretrained(model_specific_folder_path)
    #     except Exception as error:
    #         print(f'ERROR - [S05] - {str(error)}')

    # # download the model:S06
    # if (MODELS_FOLDER_PRESENT_STATUS):
    #     try:
    #         model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    #     except Exception as error:
    #         print(f'ERROR - [S06] - {str(error)}')

    # # save the model into "Models" folder:S07
    # if (MODELS_FOLDER_PRESENT_STATUS):
    #     try:
    #         model.save_pretrained(model_specific_folder_path)
    #     except Exception as error:
    #         print(f'ERROR - [S07] - {str(error)}')