import json

def load_data():
    try:
        with open('youtube_vedio_details.txt','r')as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def save_data_helper(vedios):
    with open('youtube_vedio_details.txt','w') as file:
        json.dump(vedios,file)

def list_all_vedios(videos):
    print("\n")
    print("*"*80)
    for index,video in enumerate(videos,start=1):
        print(f"{index}. {video['name']}, Duration: {video['time']}")
    print("*"*80)

def add_video(videos):
    name = input("Enter video name:")
    time = input("Enter video time:")
    videos.append({'name':name,'time': time})
    save_data_helper(videos)
    
def update_video_detail(videos):
    list_all_vedios(videos)
    index = int(input("Enter the vedio numer to update : "))
    if 1 <= index <= len(videos):
        name = input("Enter the new video name : ")
        time = input("Enter new lenght of the vedio : ")
        videos[index-1]  = {'name':name, 'time':time}
        save_data_helper(videos)
    else :
        print("Invalid index seleted")

def delete_video(videos):
    list_all_vedios(videos)
    to_del = int(input("Enter the video no. to be deleted : "))

    if 1<= to_del <= len(videos):
        del videos[to_del-1]
    else :
        print("Invalid video is selected")


def main():
    videos = load_data()
    while(True):
        print("\n--------------------- Youtube Manager-----------------")
        print("\n Enter a option : \n")
        print ("1. List all youtube videos")
        print ("2. Add a youtube vedio")
        print("3. Update a youtube vedio details")
        print("4. Delete a youtuube vedio")
        print("5. Exit the app")
        choice = input(" Enter your choice: ")
        # print(videos)

        match choice :
            case '1':
                list_all_vedios(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video_detail(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid Choice") 

if __name__ == "__main__":
    main()
