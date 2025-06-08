import os

topics = [
    "Sliding Window",
    "Two Pointers",
    "Interval",
    "Stack",
    "Linked List",
    "Binary Search",
    "Heap",
    "Depth First Search",
    "Breadth First Search",
    "Backtracking",
    "Graph",
    "Dynamic Programming",
    "Greedy Algorithms",
    "Trie",
    "Prefix Sum",
    "Matrices",
]

print("Creating folders...")
for i, topic in enumerate(topics, start=1):
    # folder_name = f"{i:02d}-{topic.lower().replace(' ', '-')}"
    folder_name = f"{i}-{topic.lower().replace(' ', '-')}"
    os.makedirs(folder_name, exist_ok=True)
    print(f"Created folder: {folder_name}")

    # create overview.md file under the folder
    if not os.path.exists(f"{folder_name}/overview.md"):
        with open(f"{folder_name}/overview.md", "w") as f:
            f.write(f"# {topic}\n\n")
    print(f"Created overview.md file under {folder_name}")

print("Folders created successfully!")
