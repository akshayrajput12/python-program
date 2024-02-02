import instaloader
run = instaloader.Instaloader()
acc = input("Enter account name: ")
run.download_profile(acc, profile_pic_only = True)
