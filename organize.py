import os
import shutil



from_dir = "C:/Users/SOS GAMER/Downloads"
to_dir = "C:/Users/SOS GAMER/Desktop/byjus/102"

list_of_files = os.listdir(from_dir)


for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)
    
    if extension == '':
        continue

    if extension in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:

        path1 = from_dir + '/' + file_name
        path2 = to_dir + '/' + "Arquivo_Imagem"
        path3 = to_dir + '/' + "Arquivo_Imagem" + '/' + file_name


        if os.path.exists(path2):
            print("Movendo " + file_name + ".....")

            shutil.move(path1, path3)

        else:
            os.makedirs(path2)  
            print("Movendo " + file_name + ".....")
            shutil.move(path1, path3)