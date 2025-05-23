


from utils.data_loader import load_images_and_labels
import matplotlib.pyplot as plt

# Path to your training set
base_dir = 'data/train'  # adjust if needed

images, labels = load_images_and_labels(base_dir)

print(f"Total images loaded: {len(images)}")
print(f"First image shape: {images[0].shape}")
print(f"First label: {labels[0]}")

# Display a few images
for i in range(3):
    plt.imshow(images[i])
    plt.title(f"Label: Grade {labels[i]}")
    plt.axis('off')
    plt.show()
