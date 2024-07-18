import os
import subprocess

# 设置你的文件夹路径
folder_path = './data/12217_kashiwa-shi_city_2020_citygml_6_op/udx/bldg'

# 遍历文件夹中的所有文件
for filename in os.listdir(folder_path):
    if filename.endswith('.gml'):
        # 构建完整的文件路径
        file_path = os.path.join(folder_path, filename)
        
        # 构建输出文件路径
        # output_path = os.path.join(folder_path, filename.replace('.gml', '.geojson'))
        
        # 构建命令
        command = f'python cct.py geojson "{file_path}" --lod=1 --to-srid=6697'
        
        # 执行命令
        subprocess.run(command, shell=True)

print("Finish！")
