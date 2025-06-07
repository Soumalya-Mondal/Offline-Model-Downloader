# define main function
if __name__ == '__main__':
    # importing python module:S01
    try:
        from pathlib import Path
        import shutil
    except Exception as error:
        print(f'ERROR - {str(error)}')