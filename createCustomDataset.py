import os
import shutil

database_folder = r"/media/tak/4650AF4250AF3817/BE Project/Database/GREYC-Web based KeyStroke dynamics Dataset/"
user_path = database_folder + r"database/users/"
path = database_folder + r"database/passwords/"
save_path = database_folder + r"custom_dataset/"

for user in os.listdir(path):
    # save the user_id, username and password
    user_details = open(user_path + user + ".txt", "r")
    os.makedirs(save_path + user)
    save_user = open(save_path + user + "/details.txt", "w")
    for i in range(0,3):
        save_user.write(user_details.readline())
    save_user.close()

    s_type = ["/genuine/", "/impostor/"]
    l = path + user
    s_l = save_path + user
    try:
        for session_type in s_type:
            counter = 1
            for session in os.listdir(path + user + session_type):
                if os.path.isdir(path + user + session_type + session):
                    location = l + session_type + session
                    save_location = s_l + session_type + str(counter) + "/"
                    os.makedirs(save_location)
                    shutil.copyfile(location + "/p_raw_press.txt", save_location + "raw_press.txt")
                    shutil.copyfile(location + "/p_raw_release.txt", save_location + "raw_release.txt")
                    counter += 1
    except NotADirectoryError:
        pass