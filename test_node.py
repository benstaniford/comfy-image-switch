import torch
import sys
import os

# Add the current directory to Python path for testing
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from image_switch_node import ImageSwitchNode

def test_image_switch_node():
    """Test the ImageSwitchNode functionality."""
    
    # Create test images
    image1 = torch.ones((1, 256, 256, 3), dtype=torch.float32)  # White image
    image2 = torch.zeros((1, 256, 256, 3), dtype=torch.float32)  # Black image
    image3 = torch.full((1, 256, 256, 3), 0.5, dtype=torch.float32)  # Gray image
    
    # Create node instance
    node = ImageSwitchNode()
    
    # Test 1: Select first image
    print("Test 1: Selecting image 1")
    result = node.switch_image(select=1, image_1=image1, image_2=image2, image_3=image3)
    assert torch.equal(result[0], image1), "Failed to select image 1"
    print("✓ Passed")
    
    # Test 2: Select second image
    print("Test 2: Selecting image 2")
    result = node.switch_image(select=2, image_1=image1, image_2=image2, image_3=image3)
    assert torch.equal(result[0], image2), "Failed to select image 2"
    print("✓ Passed")
    
    # Test 3: Select third image
    print("Test 3: Selecting image 3")
    result = node.switch_image(select=3, image_1=image1, image_2=image2, image_3=image3)
    assert torch.equal(result[0], image3), "Failed to select image 3"
    print("✓ Passed")
    
    # Test 4: Select non-existent image (should fallback to first available)
    print("Test 4: Selecting non-existent image (fallback test)")
    result = node.switch_image(select=5, image_1=image1, image_2=image2)
    assert torch.equal(result[0], image1), "Failed to fallback to first available image"
    print("✓ Passed")
    
    # Test 5: No images provided (should create default black image)
    print("Test 5: No images provided (default image test)")
    result = node.switch_image(select=1)
    assert result[0].shape == (1, 512, 512, 3), "Default image has wrong shape"
    assert torch.all(result[0] == 0), "Default image is not black"
    print("✓ Passed")
    
    print("\nAll tests passed! 🎉")

if __name__ == "__main__":
    test_image_switch_node()
