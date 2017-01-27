import os
import shutil

database_folder = r"/home/riddhi/keystroke/data/custom_datas/"
user_path = database_folder + r"users/"
path = database_folder + r"passwords/"
save_path = database_folder + r"custom_datas/"

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
                    shutil.copyfile(location + "/userid.txt", save_location + "userid.txt")
                    shutil.copyfile(location + "/date.txt", save_location + "date.txt")
                    shutil.copyfile(location + "/genuine.txt", save_location + "genuine.txt")
                    shutil.copyfile(location + "/password.txt", save_location + "password.txt")
                    shutil.copyfile(location + "/p_release_codes.txt", save_location + "p_release_codes.txt")
                    shutil.copyfile(location + "/p_raw_press.txt", save_location + "raw_press.txt")
                    shutil.copyfile(location + "/p_raw_release.txt", save_location + "raw_release.txt")
                    shutil.copyfile(location + "/p_pp.txt", save_location + "pp.txt")
                    shutil.copyfile(location + "/p_rr.txt", save_location + "rr.txt")
                    shutil.copyfile(location + "/p_pr.txt", save_location + "pr.txt")
                    shutil.copyfile(location + "/p_rp.txt", save_location + "rp.txt")
                    shutil.copyfile(location + "/p_total.txt", save_location + "total.txt")

                    counter += 1
    except NotADirectoryError:
        pass

