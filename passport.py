from PIL import Image, ImageFilter

# Define the dimensions of the passport photo (in pixels)
PHOTO_WIDTH = 600
PHOTO_HEIGHT = 600

# Define the dimensions and position of the face in the photo (in pixels)
FACE_WIDTH = 350
FACE_HEIGHT = 450
FACE_X = 125
FACE_Y = 0

# Load the image
image_path = 'test.jpeg'  # Replace with the actual path to your image
image = Image.open(image_path)

# Resize the image to the passport photo dimensions
image = image.resize((PHOTO_WIDTH, PHOTO_HEIGHT))

# Extract the face region from the image
face_region = image.crop((FACE_X, FACE_Y, FACE_X + FACE_WIDTH, FACE_Y + FACE_HEIGHT))

# Apply image cleaning operations
# For example, you can apply filters to enhance the image quality
cleaned_face = face_region.filter(ImageFilter.SHARPEN)

# Create a new blank image with the passport photo dimensions
passport_photo = Image.new('RGB', (PHOTO_WIDTH, PHOTO_HEIGHT))

# Paste the cleaned face onto the blank image
passport_photo.paste(cleaned_face, (FACE_X, FACE_Y))

# Display the passport photo
passport_photo.show()

# Save the passport photo
passport_photo.save('')  # Replace with the desired save path
