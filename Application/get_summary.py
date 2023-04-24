import re


def get_summary(folder_path, case_letter, sim_number):
    result = []
    for k in range(1, sim_number+1):
        result_file_name = f'{folder_path}/sim{k}{case_letter}_2_summary_{case_letter}'
        with open(result_file_name) as f:
            head = next(f.read() for _ in range(9))
            head_splitted = re.split('\n', head)
            # head_splitted.insert(0, result_file_name)
            head_splitted.remove('')
            temp_head_splitted_list = []
            for i in head_splitted:
                temp_head_splitted = re.split(': ', i)[1]
                temp_head_splitted_list.append(float(temp_head_splitted))
            result.append(temp_head_splitted_list)
    return result
