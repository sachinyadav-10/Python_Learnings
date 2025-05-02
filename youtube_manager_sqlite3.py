import sqlite3
con = sqlite3.connect("youtube_video_details.db")
cur= con.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS videos(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        time TEXT NOT NULL
    )
''')

def list_videos():
    cur.execute("SELECT * FROM videos")
    for row in cur.fetchall():
        print(row)

def add_videos(name , time):
    cur.execute("INSERT INTO videos (name , time) VALUES (?,?)", (name,time))
    con.commit()
def update_videos(new_name , new_time, id):
    cur.execute("UPDATE videos SET name =? , time=? WHERE ID=?"(new_name,new_time,id))
    con.commit()
def delete_videos(id):
    cur.execute("DELETE  FROM videos where id = ?",(id,))
    con.commit()

def main():
    while(True):
        print("YOUTUBE MANAGER APP WITH SQLITE3")
        print("1. List all Videos")
        print("2. Add videos")
        print("3. Update videos")
        print("4. Delete videos")
        print("5. Exit app")
        choice = input("Enter your choice : ")

        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter the name of video : ")
            time = input("Enter the time of video : ")
            add_videos(name,time)
        elif choice == '3':
            video_id=input("Enter video id to update : ")
            name = input("Enter the name of video : ")
            time = input("Enter the time of video : ")
            update_videos(name,time,video_id)
        elif choice == '4':
            index = int(input("Enter video Id to delete : "))
            delete_videos(index)
        elif choice == '5':
            break
        else :
            print("Invalid option selection")
    con.close()

if __name__ == "__main__":
    main()