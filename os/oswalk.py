class Oswalk:

    def get_recent_files(data_dir):
        """
            Loops across the root directory to fetch the file
            :return: A list containing location of all the files
            """

        # Debug
        print("Searching for files ... ")

        index_files = []
        last_job = ''
        # Remove any fwd slash if present
        if data_dir.endswith('/') is True:
            last_index = data_dir.rfind("/")
            data_dir = data_dir[:last_index]

        starting_level = data_dir.count(os.sep)
        for root, dirs, files in (os.walk(data_dir, topdown=True)):
            level = root.count(os.sep) - starting_level
            if level == 1:
                for dirs_ in dirs:
                    last_job = last_folder_name  # it can be name of recent added folder

            if level == 2:  # Level 2 is where I want to recursivly look for files
                for dirs_ in dirs:
                    if dirs_ > last_job_names:  # Check for if folder name is not there, then look for files
                        for sub_root, sub_dirs, sub_files in (os.walk(os.path.join(root, dirs_), topdown=True)):
                            for sub_files_ in sub_files:
                                if 'index.html' in sub_files_:
                                    index_files.append(os.path.join(sub_root, sub_files_))
                    else:
                        dir.remove(dirs_)

            # Debug
        print(" Collected list of files ... ")
        print(index_files)
        return index_files
