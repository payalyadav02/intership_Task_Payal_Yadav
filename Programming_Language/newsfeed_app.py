import os
news = []
def menu():
    while True:
        print("\n--- Dynamic News Feed ---")
        print("1. Add News Details")
        print("2. List News")
        print("3. Exit App")
        
        choice = input("Select your choice: ").strip()
        if choice == "1":
            add_news()
        elif choice == "2":
            list_news()
        elif choice == "3":
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option.")

def add_news():
    print("\n--- Add News ---")
    title = input("Enter Your Title: ")
    description = input("Enter Your Title Description: ")
    image_path = input("Enter Your Picture Path or URL: ")
    news.append({
        "title": title,
        "description": description,
        "image_path": image_path
    })
    print("\n-------------- News Added Successfully! ---------------")

def list_news():
    print("\n--- List News ---")
    if not news:
        print("------------------No News Available To Display!------------")
        return
     
    items_per_page = 3
    total_news = len(news)
    total_pages = (total_news + items_per_page - 1) // items_per_page

    page = 1
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("\n--- List News ---")
        print(f"Displaying Page {page}/{total_pages}\n")
        

        start = (page - 1) * items_per_page
        end = start + items_per_page
        current_news_feed = news[start:end]

        for i, news_item in enumerate(current_news_feed, start=1):
            print(f"News- {start + i}")
            print(f"Title: {news_item['title']}")
            print(f"Description: {news_item['description']}")
            print(f"Image Path/URL: {news_item['image_path']}\n")

        print("Options: [N]ext page, [P]revious page, [E]xit to main menu")
        choice = input("Enter your choice: ").strip().lower()

        if choice == "n" and page < total_pages:
            page += 1
        elif choice == "p" and page > 1:
            page -= 1
        elif choice == "e":
            break
        else:
            print("Invalid choice! Please try again.")

menu()
