import collections.abc
import collections
collections.MutableMapping = collections.abc.MutableMapping
collections.Mapping = collections.abc.Mapping
collections.Callable = collections.abc.Callable
from itertools import dropwhile, takewhile
from datetime import datetime
import instaloader
import csv

class GetInstagramProfile():
    def __init__(self):
        self.ig = instaloader.Instaloader()

    def user_profile_pic(self,username):
        self.ig = instaloader.Instaloader()
        self.ig.load_session_from_file("episode_clusters")
        self.ig.download_profile(username, profile_pic_only=True)
        print("User Profile Pic Downloaded")

    def user_all_pics(self,username):
         self.ig = instaloader.Instaloader()
         self.ig.load_session_from_file("episode_clusters")
         self.ig.download_profile(username , profile_pic_only=False)
         print("All Post Pics Downloaded")
         
    def posts_info_with_comments(self,username):
        with open(username+'.csv', 'w', newline='', encoding='utf-8') as file:
            self.ig = instaloader.Instaloader()
            self.ig.load_session_from_file("episode_clusters") # change Username according to the firefox
            writer = csv.writer(file)
            posts = instaloader.Profile.from_username(self.ig.context, username).get_posts()
            mylist=[]
            for post in posts:
                pdate = str(post.date)
                pprofile = (post.profile)
                pcaption = (post.caption)
                plike = str(post.likes)
                pcom = str(post.comments)
                ploc = str(post.location)
                fields = ['Date' ,'Location', 'Profile' , 'Description' , 'Likes' , 'Comments No.' , 'Commentor' ,'Comment']
                for comment in post.get_comments():
                    comown = comment.owner.username
                    comtxt = comment.text
                    list1 = [pdate,ploc ,pprofile ,pcaption , plike , pcom , comown , comtxt]
                    mylist.append(list1)
            writer = csv.writer(file)
            writer.writerow(fields)
            writer.writerows(mylist)
            print("Post Info With comments Extracted Successfully")
        
    def posts_info_without_comments(self,username):
            SINCE = datetime(2021, 6, 28)
            UNTIL = datetime(2023, 8, 12)
            self.ig = instaloader.Instaloader()
            self.ig.load_session_from_file("episode_clusters") # change Username according to the firefox
            #no = int(input('Enter No. of Posts: ')) --> Can be used for option of no. of posts we need
            with open(username+'.csv', 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                posts = instaloader.Profile.from_username(self.ig.context, username).get_posts()
                mylist=[]
                comlist=[]
                i=0
                for post in takewhile(lambda p: p.date > SINCE, dropwhile(lambda p: p.date > UNTIL, posts)):
                    #if i<no:
                        pdate = str(post.date)
                        pprofile = (post.profile)
                        pcaption = (post.caption)
                        plike = str(post.likes)
                        pcom = str(post.comments)
                        purl = post.url
                        fields = ['Date' , 'Profile' , 'Description' , 'Likes' , 'Comments' , 'Picture URL']
                        list1 = [pdate ,pprofile ,pcaption , plike , pcom ,purl]
                        mylist.append(list1)
                        i=i+1
                    #else:
                        #break
                writer = csv.writer(file)
                writer.writerow(fields)
                writer.writerows(mylist)   
                print('Post Info without comments Exported Successfully')                    

if __name__=="__main__":
    img = GetInstagramProfile()
    user = input("Enter Username: ")
    print("1.Print Profile Pic")
    print("2.Download Post pics")
    print("3.Get All post Data with Picture URL")
    print("4.Get All post Data with Comments\n")
    ip = int(input("Enter your choice: "))
    if ip ==1:
        img.user_profile_pic(user)
    elif ip ==2:
        img.user_all_pics(user)
    elif ip==3:
        img.posts_info_without_comments(user)
    elif ip==4:
        img.posts_info_with_comments(user)
    else:
        print('Invalid Option!')
    
