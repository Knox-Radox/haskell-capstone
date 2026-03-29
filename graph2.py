import matplotlib.pyplot as plt

# Features and their relative importance (arbitrary scale)
features = [
    "Multi-threaded Server", 
    "File Metadata Management", 
    "User-Specified Downloads", 
    "Error Handling"
]
importance = [9, 8, 7, 8]  # Scale from 1 to 10

# Create a bar chart
plt.figure(figsize=(8, 5))
plt.barh(features, importance, color=['blue', 'green', 'orange', 'red'])

# Labels and title
plt.xlabel("Feature Importance (1-10)")
plt.ylabel("System Features")
plt.title("Key Features of P2P File Sharing System")
plt.gca().invert_yaxis()  # Invert Y-axis for better readability

# Show the plot
plt.show()
import matplotlib.pyplot as plt

# Features and their relative importance (arbitrary scale)
features = [
    "Multi-threaded Server", 
    "File Metadata Management", 
    "User-Specified Downloads", 
    "Error Handling"
]
importance = [9, 8, 7, 8]  # Scale from 1 to 10

# Create a bar chart
plt.figure(figsize=(8, 5))
plt.barh(features, importance, color=['blue', 'green', 'orange', 'red'])

# Labels and title
plt.xlabel("Feature Importance (1-10)")
plt.ylabel("System Features")
plt.title("Key Features of P2P File Sharing System")
plt.gca().invert_yaxis()  # Invert Y-axis for better readability

# Show the plot
plt.show()
