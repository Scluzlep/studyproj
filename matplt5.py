import os

# 配置文件所在的路径，在Windows下pip配置文件通常位于此
config_path = os.path.join(os.environ['APPDATA'], 'pip', 'pip.ini')

# 要设置的源地址
new_index_url = "https://pypi.tuna.tsinghua.edu.cn/simple"

# 配置文件中表示源的配置项的头部
index_url_key = "index-url"


def modify_pip_source():
    # 判断配置文件所在的目录是否存在，不存在则创建
    dir_path = os.path.dirname(config_path)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    # 判断配置文件是否存在
    if not os.path.exists(config_path):
        with open(config_path, 'w') as f:
            f.write(f"[global]\n{index_url_key} = {new_index_url}\n")
    else:
        # 配置文件存在，读取内容
        with open(config_path, 'r') as f:
            lines = f.readlines()
        global_section_index = None
        index_url_line_index = None
        # 查找是否有[global]这个节
        for index, line in enumerate(lines):
            if line.strip() == "[global]":
                global_section_index = index
                break
        if global_section_index is not None:
            # 在[global]节里查找index-url这一行
            for index in range(global_section_index, len(lines)):
                if lines[index].startswith(index_url_key):
                    index_url_line_index = index
                    break
            if index_url_line_index is None:
                # 如果没找到index-url这一行配置，就在[global]节最后添加
                lines.insert(global_section_index + 1, f"{index_url_key} = {new_index_url}\n")
                with open(config_path, 'w') as f:
                    f.writelines(lines)
            else:
                # 如果找到了，就替换原来的源地址
                lines[index_url_line_index] = f"{index_url_key} = {new_index_url}\n"
                with open(config_path, 'w') as f:
                    f.writelines(lines)
        else:
            # 如果没有[global]节，就添加[global]节和对应的源配置
            lines.append(f"[global]\n{index_url_key} = {new_index_url}\n")
            with open(config_path, 'w') as f:
                f.writelines(lines)


if __name__ == "__main__":
    modify_pip_source()